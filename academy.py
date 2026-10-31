"""Simple local curriculum navigation. No network or AI dependency."""
from pathlib import Path
import argparse

ROOT = Path(__file__).resolve().parent
LESSONS = sorted((ROOT / "lessons").glob("[0-9][0-9]-*"))

def main():
    parser = argparse.ArgumentParser(description="AI Engineering Academy")
    parser.add_argument("command", choices=["next", "list", "status"])
    args = parser.parse_args()
    progress = (ROOT / "progress" / "PROGRESS.md").read_text(encoding="utf-8")
    if args.command == "list":
        for lesson in LESSONS:
            print(lesson.name)
    elif args.command == "status":
        print(progress)
    else:
        import re
        m = re.search(r"Current lesson:\s*(\d+)", progress)
        number = int(m.group(1)) if m else 1
        if number < 1 or number > len(LESSONS):
            raise SystemExit("Update progress/PROGRESS.md Current lesson to 01–20")
        print(LESSONS[number-1] / "LESSON.md")

if __name__ == "__main__":
    main()
