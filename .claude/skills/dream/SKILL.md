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

### Step 2: TODO — not yet defined

### Step 3: TODO — not yet defined

### Step 4: TODO — not yet defined

### Step 5: TODO — not yet defined

### Step 6: TODO — not yet defined
