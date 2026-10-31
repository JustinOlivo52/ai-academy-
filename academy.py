"""Offline curriculum navigation, never an automatic teaching/grading engine."""
import argparse
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent


def current_lesson(root=ROOT):
    progress = (root / "progress/PROGRESS.md").read_text(encoding="utf-8")
    matches = re.findall(r"^Current lesson:\s*(\d{1,2})\s*$", progress, re.MULTILINE)
    if len(matches) != 1 or not 1 <= int(matches[0]) <= 20:
        raise ValueError("Expected exactly one Current lesson: 01–20 field in progress/PROGRESS.md")
    number = int(matches[0])
    lessons = list((root / "lessons").glob(f"{number:02d}-*/LESSON.md"))
    if len(lessons) != 1:
        raise ValueError(f"Expected exactly one LESSON.md for lesson {number:02d}")
    return lessons[0]


def main():
    parser = argparse.ArgumentParser(description="AI Engineering Academy navigation (does not teach or grade)")
    parser.add_argument("command", choices=["next", "list", "status"])
    args = parser.parse_args()
    if args.command == "list":
        for lesson in sorted((ROOT / "lessons").glob("[0-9][0-9]-*/LESSON.md")):
            print(lesson.parent.name)
    elif args.command == "status":
        print((ROOT / "progress/PROGRESS.md").read_text(encoding="utf-8"))
    else:
        try:
            print(current_lesson())
        except ValueError as error:
            parser.exit(2, f"{error}\n")


if __name__ == "__main__":
    main()
