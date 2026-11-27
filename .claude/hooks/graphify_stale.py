"""Stop hook: keep graphify-out/ in sync with the repo.

- Code changed only  -> run `graphify update .` (AST, no LLM, free).
- Notes/docs changed -> block the stop once and ask Claude to run
  `/graphify . --update` (user approved auto-update on 2026-11-27).
- No change, no graph, already blocked once, or any error -> exit 0 silently.

Run with the interpreter that has graphify installed, e.g.
  python -I .claude/hooks/graphify_stale.py
"""
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SEMANTIC = ("document", "paper", "image", "video")


def rel(p):
    try:
        return Path(p).resolve().relative_to(ROOT).as_posix()
    except Exception:
        return str(p)


def main():
    try:
        payload = json.loads(sys.stdin.read() or "{}")
    except Exception:
        payload = {}
    if payload.get("stop_hook_active"):
        return 0
    os.chdir(ROOT)
    if not Path("graphify-out/graph.json").exists():
        return 0

    from graphify.detect import detect_incremental
    from graphify.paths import out_path
    from graphify.watch import _read_build_excludes, _read_build_gitignore

    r = detect_incremental(
        Path("."),
        extra_excludes=_read_build_excludes(out_path()),
        gitignore=_read_build_gitignore(out_path()),
    )
    new = r.get("new_files", {}) or {}
    deleted = list(r.get("deleted_files", []) or [])
    code = list(new.get("code", []))
    docs = [f for t in SEMANTIC for f in new.get(t, [])]
    if not code and not docs and not deleted:
        return 0

    if not docs and not any(not str(d).endswith((".py", ".sh", ".json", ".js", ".ts")) for d in deleted):
        # Code-only change: free AST refresh, no need to bother Claude.
        exe = Path(sys.executable).with_name("Scripts") / "graphify.exe"
        cmd = [str(exe)] if exe.exists() else [sys.executable, "-m", "graphify"]
        subprocess.run(cmd + ["update", "."], cwd=ROOT, timeout=100,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return 0

    changed = [rel(f) for f in docs] + [f"(deleted) {rel(f)}" for f in deleted]
    shown = ", ".join(changed[:10]) + (f", … (+{len(changed) - 10} more)" if len(changed) > 10 else "")
    reason = (
        f"graphify graph is stale: {len(changed)} note/doc file(s) changed since the last build "
        f"({shown}). Run the graphify skill with args '. --update' now - auto-update is approved "
        f"by the user in CLAUDE.md, do not ask. Report the token cost briefly, do not commit, then finish."
    )
    # ensure_ascii: Windows pipes default to cp1252, keep the JSON pure ASCII.
    print(json.dumps({"decision": "block", "reason": reason}))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # never break the session
        print(f"graphify_stale hook error: {exc}", file=sys.stderr)
        sys.exit(0)
