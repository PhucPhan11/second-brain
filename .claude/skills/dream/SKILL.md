---
name: dream
description: Consolidates what was captured in log/ into the second-brain notes (notes/ and index.md), like memory consolidation during sleep. Use only when the user explicitly asks to run "dream" or to consolidate their notes/logs. Do not use for capturing a note ("remember X"), searching notes, or editing a single note.
---

# Dream

## Steps

### Step 1: Read today's bullets

Run this from anywhere inside the repo:

```bash
bash "$(git rev-parse --show-toplevel)/.claude/skills/dream/scripts/read_today.sh"
```

The script is read-only. It prints a header (note count, log file count, total bytes), then `index.md`, every `.md` file under `notes/`, and every file under `log/`, each sorted by path and preceded by `===== FILE: <repo-relative path> =====`. If `index.md`, `notes/` or `log/` is missing or empty, it prints `===== MISSING: <path> =====` in its place.

Use its output as the input for the remaining steps.

### Step 2: Pick the subject for each log bullet

If step 1 printed `===== MISSING: log/ =====`, or the log files contain no bullets, stop here and reply only "nothing to dream".

Otherwise, assign every log bullet from step 1 to exactly one subject. A subject is a note: subject `deploys` is `notes/deploys.md`. Reuse an existing subject from `index.md` when one fits. Create a new kebab-case subject only when none fits.

### Step 3: Classify each bullet

Compare each bullet against its subject's note and give it exactly one action:

- `seen`: the note already says the same thing.
- `supersede`: the bullet contradicts a note line.
- `new`: everything else, including every bullet whose subject has no note yet.

For `seen` and `supersede`, copy `line` from the NOTE text, not from the log bullet: five or more consecutive words, exactly as written, from a line that is not struck through (`~~…~~`). Write `text` as the bullet should read in the note, without the leading `- ` and without a date; the script adds both.

Put every action into one Plan that follows this contract:

```text
Plan     {"actions": [Action, ...]}

Action
  subject  string  required   kebab-case, the note is notes/<subject>.md
  action   string  required   "new" | "seen" | "supersede"
  text     string  required for new and supersede, ignored for seen
                   the bullet as it should read in the note
  line     string  required for seen and supersede, ignored for new
                   locates the line to re-date or strike. Copy five or more
                   consecutive words from that note line exactly, not from the
                   log bullet, whose wording usually differs. First match wins

Example:
{"actions": [
  {"subject": "working-with-claude", "action": "seen", "line": "always ask back when unsure, never build on assumptions"},
  {"subject": "working-with-claude", "action": "new", "text": "plan mode first, then one approval"},
  {"subject": "deploys", "action": "supersede", "line": "staging deploys go out Tuesday 9am", "text": "staging deploys go out Wednesday 9am"},
  {"subject": "deploys", "action": "new", "text": "rollback is a revert commit, never a force push"}
]}
```

### Steps 4–6: Write, refresh and archive (one script call)

`scripts/dream.py` does all three steps in a single call. Do not edit the files yourself.

- **Step 4: Write them.** Appends every log bullet to `hot.md`, then applies the actions to `notes/`. `new` appends `- <text> (<date>)`. `seen` re-dates the matched line. `supersede` strikes the matched line through as `- ~~<old text>~~` and puts `- <text> (<date>)` right under it. A missing note is created with `# <subject>` as its heading.
- **Step 5: Refresh index.md and hot.md.** Adds an index entry for every note not yet listed, drops entries whose file is gone, and keeps the last line. Trims `hot.md` to its most recent bullets, 200 words max.
- **Step 6: Archive the processed logs.** Moves every file in `log/` to `archive/log/<date>/`.

The script validates the whole Plan before writing anything. If it finds a problem it prints every error, exits 1 and writes nothing; fix the Plan and run it again. Run it with the Bash tool, because the heredoc needs bash.

Make one tool call: pipe one JSON object into the script. Add no summary and no follow up.

```bash
python3 .claude/skills/dream/scripts/dream.py <<'JSON'
<the Plan object>
JSON
```
