#!/usr/bin/env python3
"""dream, steps 4-6: apply a Plan (JSON on stdin) to the second brain.

  4. Write:   append the log bullets to hot.md, apply the actions to notes/
  5. Refresh: rebuild index.md, trim hot.md to its newest 200 words
  6. Archive: move every log file to archive/log/<date>/

Everything is validated and computed in memory first. If anything is wrong,
every error is printed, nothing is written, and the exit code is 1.
Standard library only, Python 3.9+.
"""
import argparse
import difflib
import json
import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path, PurePosixPath

INDEX = "index.md"
HOT = "hot.md"
INDEX_FOOTER = "Search these with grep / head / tail. Open a whole note only when you need all of it"
HOT_MAX_WORDS = 200
SUMMARY_MAX_WORDS = 12
LINE_MIN_WORDS = 5
KINDS = ("new", "seen", "supersede")
KEYS = {"subject", "action", "text", "line"}

KEBAB = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
BULLET = re.compile(r"(\s*[-*]\s+)(.*?)\s*")  # groups: prefix, body
DATE_SUFFIX = re.compile(r"\s*\(\d{4}-\d{2}-\d{2}\)$")
INDEX_ENTRY = re.compile(r"- (notes/.+\.md)\s*")
INDENT = re.compile(r"(\s+)[-*]\s")


class DreamError(Exception):
    pass


def read_text(path):
    try:
        return path.read_bytes().decode("utf-8")
    except UnicodeDecodeError as e:
        raise DreamError(f"{path}: not valid UTF-8 ({e})")


class Doc:
    """A text file held in memory as lines, keeping the file's newline style."""

    def __init__(self, root, rel):
        self.rel = rel
        self.path = root / rel
        self.original = read_text(self.path) if self.path.is_file() else None
        text = self.original or ""
        self.newline = "\r\n" if "\r\n" in text else "\n"
        self.lines = text.replace("\r\n", "\n").split("\n")
        if self.lines[-1] == "":
            self.lines.pop()
        self.original_lines = list(self.lines)

    @property
    def exists(self):
        return self.original is not None

    @property
    def present(self):
        """Exists on disk or was created in memory by this run."""
        return self.exists or bool(self.lines)

    @property
    def changed(self):
        if self.original is None:
            return bool(self.lines)
        return self.render() != self.original

    def render(self):
        return "".join(line + self.newline for line in self.lines)


class Workspace:
    def __init__(self, root):
        self.root = root
        self.docs = {}

    def doc(self, rel):
        if rel not in self.docs:
            self.docs[rel] = Doc(self.root, rel)
        return self.docs[rel]


def files_under(root, top, suffix=""):
    """Repo-relative paths of the files under root/top, in `LC_ALL=C sort` order."""
    base = root / top
    if not base.is_dir():
        return []
    rels = (p.relative_to(root).as_posix() for p in base.rglob("*")
            if p.is_file() and p.name.endswith(suffix))
    return sorted(rels, key=lambda rel: rel.encode("utf-8"))


def bullet(line):
    """(prefix, body) of a non-empty bullet line, else None."""
    m = BULLET.fullmatch(line)
    return m.groups() if m and m.group(2) else None


def is_struck(body):
    return len(body) >= 4 and body.startswith("~~") and body.endswith("~~")


def squash(text):
    return " ".join(text.split())


def words(lines):
    return sum(len(line.split()) for line in lines)


def append_line(lines, line):
    """Append after the last non-blank line, keeping a blank line under a heading."""
    while lines and not lines[-1].strip():
        lines.pop()
    if lines and lines[-1].startswith("#"):
        lines.append("")
    lines.append(line)


def find_line(lines, needle):
    """Index of the first live (not struck) bullet containing needle, else None."""
    needle = squash(needle)
    for i, line in enumerate(lines):
        b = bullet(line)
        if b and not is_struck(b[1]) and needle in squash(b[1]):
            return i
    return None


# --- Plan validation -------------------------------------------------------

def check_plan(raw):
    """Return (actions, errors). actions is None when the Plan's shape is unusable."""
    try:
        plan = json.loads(raw)
    except json.JSONDecodeError as e:
        return None, [f"plan is not valid JSON: {e}"]
    if not isinstance(plan, dict) or set(plan) != {"actions"}:
        return None, ['plan must be an object with exactly one key, "actions"']
    if not isinstance(plan["actions"], list) or not plan["actions"]:
        return None, ['"actions" must be a non-empty list']
    return plan["actions"], []


def action_problems(act):
    if not isinstance(act, dict):
        return ["must be an object"]
    problems = []
    unknown = sorted(set(act) - KEYS)
    if unknown:
        problems.append(f"unknown keys {unknown}")
    subject, kind = act.get("subject"), act.get("action")
    if not isinstance(subject, str) or not KEBAB.fullmatch(subject):
        problems.append(f'"subject" must be a kebab-case string, got {subject!r}')
    if kind not in KINDS:
        problems.append(f'"action" must be one of {", ".join(KINDS)}, got {kind!r}')
    if kind in ("new", "supersede"):
        text = act.get("text")
        if not isinstance(text, str) or not text.strip() or "\n" in text or "\r" in text:
            problems.append('"text" must be a non-empty single-line string')
    if kind in ("seen", "supersede"):
        line = act.get("line")
        if not isinstance(line, str) or len(line.split()) < LINE_MIN_WORDS:
            problems.append(f'"line" must have {LINE_MIN_WORDS} or more words, got {line!r}')
    return problems


# --- Step 4: write ---------------------------------------------------------

def log_bullets(root, log_files):
    found = []
    for rel in log_files:
        for line in read_text(root / rel).replace("\r\n", "\n").split("\n"):
            b = bullet(line)
            if b:
                found.append(f"- {b[1]}")
    return found


def apply_action(ws, act, day, changes):
    """Apply one valid action to its note in memory; return a list of problems."""
    subject, kind = act["subject"], act["action"]
    rel = f"notes/{subject}.md"
    doc = ws.doc(rel)

    if kind == "new":
        if not doc.lines:
            doc.lines = [f"# {subject}", ""]
            if not doc.exists:
                changes.append(f"{rel}: created")
        text = act["text"].strip()
        append_line(doc.lines, f"- {text} ({day})")
        changes.append(f'{rel}: added "{text}"')
        return []

    if not doc.present:
        return [f"{rel} does not exist"]
    i = find_line(doc.lines, act["line"])
    if i is None:
        return [f'no live bullet in {rel} contains "{act["line"]}"']
    prefix, body = bullet(doc.lines[i])
    if kind == "seen":
        doc.lines[i] = f"{prefix}{DATE_SUFFIX.sub('', body)} ({day})"
        changes.append(f'{rel}: re-dated "{DATE_SUFFIX.sub("", body)}" to {day}')
    else:
        text = act["text"].strip()
        doc.lines[i:i + 1] = [f"{prefix}~~{body}~~", f"{prefix}{text} ({day})"]
        changes.append(f'{rel}: superseded "{body}" → "{text}"')
    return []


def apply_actions(ws, actions, day, changes):
    """Validate and apply every action in order; return every error found."""
    errors = []
    for i, act in enumerate(actions):
        where = f"actions[{i}]"
        if isinstance(act, dict):
            where += f" ({act.get('subject')}/{act.get('action')})"
        problems = action_problems(act) or apply_action(ws, act, day, changes)
        errors += [f"{where}: {p}" for p in problems]
    return errors


# --- Step 5: refresh -------------------------------------------------------

def summarize(lines):
    for line in lines:
        b = bullet(line)
        if b and not is_struck(b[1]):
            text = DATE_SUFFIX.sub("", b[1]).split()
            more = " ..." if len(text) > SUMMARY_MAX_WORDS else ""
            return " ".join(text[:SUMMARY_MAX_WORDS]) + more
    return "(no bullets yet)"


def rebuild_index(ws, notes, changes):
    doc = ws.doc(INDEX)
    body = list(doc.lines)
    while body and not body[-1].strip():
        body.pop()
    footer, gap = INDEX_FOOTER, 1
    if body and body[-1].strip() == INDEX_FOOTER:
        footer, gap = body.pop(), 0
        while body and not body[-1].strip():
            body.pop()
            gap += 1

    preamble, blocks = [], []  # blocks: (note path, [entry line, summary lines...])
    for line in body:
        m = INDEX_ENTRY.fullmatch(line)
        if m:
            blocks.append((m.group(1), [line]))
        elif blocks:
            blocks[-1][1].append(line)
        else:
            preamble.append(line)

    listed = {path for path, _ in blocks}
    dropped = [path for path, _ in blocks if path not in notes]
    added = [rel for rel in notes if rel not in listed]
    indent = next((m.group(1) for _, block in blocks for line in block[1:]
                   if (m := INDENT.match(line))), "    ")

    lines = list(preamble)
    for path, block in blocks:
        if path in notes:
            lines += block
    for rel in added:
        lines += [f"- {rel}", f"{indent}- {summarize(ws.doc(rel).lines)}"]
    if lines:
        lines += [""] * gap
    doc.lines = lines + [footer]

    if not doc.changed:
        return
    if not doc.exists:
        changes.append(f"{INDEX}: created with {len(added)} entries ({', '.join(added)})")
        return
    parts = []
    if added:
        parts.append(f"+{len(added)} entries ({', '.join(added)})")
    if dropped:
        parts.append(f"-{len(dropped)} dropped ({', '.join(dropped)})")
    changes.append(f"{INDEX}: {', '.join(parts) or 'footer restored'}")


def trim_hot(doc, changes):
    before = words(doc.lines)
    dropped = 0
    while words(doc.lines) > HOT_MAX_WORDS:
        i = next((i for i, line in enumerate(doc.lines) if bullet(line)), None)
        if i is None:
            break
        del doc.lines[i]
        dropped += 1
    if dropped:
        changes.append(f"{HOT}: trimmed {dropped} oldest bullets ({before} → {words(doc.lines)} words)")


# --- Step 6: archive -------------------------------------------------------

def plan_moves(root, log_files, day):
    moves, taken = [], set()
    for rel in log_files:
        dest = PurePosixPath("archive/log", day, PurePosixPath(rel).relative_to("log"))
        stem, ext, n = dest.stem, dest.suffix, 1
        while dest.as_posix() in taken or (root / dest.as_posix()).exists():
            n += 1
            dest = dest.with_name(f"{stem}.{n}{ext}")
        taken.add(dest.as_posix())
        moves.append((rel, dest.as_posix()))
    return moves


def commit(root, docs, moves):
    for doc in docs:
        doc.path.parent.mkdir(parents=True, exist_ok=True)
        doc.path.write_bytes(doc.render().encode("utf-8"))
    for src, dst in moves:
        target = root / dst
        if target.exists():
            raise FileExistsError(f"{dst} already exists; refusing to overwrite")
        target.parent.mkdir(parents=True, exist_ok=True)
        os.rename(root / src, target)


def print_diff(doc):
    old = f"a/{doc.rel}" if doc.exists else "/dev/null"
    for line in difflib.unified_diff(doc.original_lines, doc.lines, old, f"b/{doc.rel}", lineterm=""):
        print(line)


# --- Main ------------------------------------------------------------------

def dream(root, day, dry_run, raw_plan):
    if not root.is_dir():
        raise DreamError(f"--root {root} is not a directory")
    try:
        raw = raw_plan.decode("utf-8-sig")
    except UnicodeDecodeError as e:
        raise DreamError(f"plan is not valid UTF-8 ({e})")

    ws = Workspace(root)
    changes = []
    actions, errors = check_plan(raw)
    log_files = files_under(root, "log")

    # Step 4a: append the log bullets to hot.md.
    hot = ws.doc(HOT)
    new_bullets = log_bullets(root, log_files)
    for line in new_bullets:
        append_line(hot.lines, line)
    if new_bullets:
        created = "" if hot.exists else "created, "
        changes.append(f"{HOT}: {created}+{len(new_bullets)} bullets")

    # Step 4b: apply the actions to notes/.
    if actions is not None:
        errors += apply_actions(ws, actions, day, changes)
    if errors:
        for error in errors:
            print(f"✗ {error}", file=sys.stderr)
        print(f"{len(errors)} error(s); nothing written", file=sys.stderr)
        return 1

    # Step 5: rebuild index.md, trim hot.md.
    touched = {rel for rel, doc in ws.docs.items() if rel.startswith("notes/") and doc.present}
    notes = sorted(set(files_under(root, "notes", ".md")) | touched, key=lambda rel: rel.encode("utf-8"))
    rebuild_index(ws, notes, changes)
    trim_hot(hot, changes)

    # Step 6: archive every log file.
    moves = plan_moves(root, log_files, day)
    changes += [f"{src}: archived → {dst}" for src, dst in moves]

    changed = [doc for doc in ws.docs.values() if doc.changed]
    if dry_run:
        for doc in changed:
            print_diff(doc)
        for src, dst in moves:
            print(f"rename {src} → {dst}")
        for change in changes:
            print(f"✅ {change} (dry run)")
        print("dry run: nothing written")
        return 0

    commit(root, changed, moves)
    for change in changes:
        print(f"✅ {change}")
    return 0


def iso_day(value):
    try:
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
            raise ValueError
        return date.fromisoformat(value).isoformat()
    except ValueError:
        raise argparse.ArgumentTypeError(f"expected YYYY-MM-DD, got {value!r}")


def repo_root():
    try:
        out = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                             capture_output=True, text=True, check=True)
        return Path(out.stdout.strip())
    except (OSError, subprocess.CalledProcessError):
        return Path.cwd()


def main():
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="dream steps 4-6: apply a Plan read from stdin.")
    parser.add_argument("--root", help="second-brain root (default: git toplevel, else cwd)")
    parser.add_argument("--date", type=iso_day, default=date.today().isoformat(),
                        help="YYYY-MM-DD used for bullets and the archive folder (default: today)")
    parser.add_argument("--dry-run", action="store_true", help="print a diff of every change, write nothing")
    args = parser.parse_args()
    root = Path(args.root).resolve() if args.root else repo_root()
    try:
        return dream(root, args.date, args.dry_run, sys.stdin.buffer.read())
    except DreamError as e:
        print(f"✗ {e}", file=sys.stderr)
        print("nothing written", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
