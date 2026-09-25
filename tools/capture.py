"""Append a note as a bullet to today's log: .second-brain/log/YYYY-MM-DD.md"""
import sys
from datetime import date
from pathlib import Path

LOG_DIR = Path(__file__).resolve().parent.parent / "log"


def main():
    note = " ".join(" ".join(sys.argv[1:]).split())
    if not note:
        sys.exit('usage: python capture.py "your note"')
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    path = LOG_DIR / f"{date.today().isoformat()}.md"
    with path.open("a", encoding="utf-8") as f:
        f.write(f"- {note}\n")
    print(f"Saved to {path}")


if __name__ == "__main__":
    main()
