"""Course-tooling checks; never learner assessment credit."""
import contextlib
import importlib.util
import io
from pathlib import Path
import re
import subprocess
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/01-python-diagnostic-and-control-flow"


def load_navigation():
    spec = importlib.util.spec_from_file_location("academy_navigation", ROOT / "academy.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_current_lesson_resolves_and_cli_from_other_directory(tmp_path):
    assert load_navigation().current_lesson() == LESSON / "LESSON.md"
    result = subprocess.run([sys.executable, str(ROOT / "academy.py"), "next"],
                            cwd=tmp_path, capture_output=True, text=True, check=True)
    assert Path(result.stdout.strip()).is_file()


@pytest.mark.parametrize("field", ["", "Current lesson: 0", "Current lesson: 21",
    "Current lesson: nope", "Current lesson: 01\nCurrent lesson: 02"])
def test_bad_progress_never_silently_resets(tmp_path, field):
    (tmp_path / "progress").mkdir()
    (tmp_path / "progress/PROGRESS.md").write_text(field)
    with pytest.raises(ValueError, match="exactly one Current lesson"):
        load_navigation().current_lesson(tmp_path)


def test_missing_lesson_is_actionable(tmp_path):
    (tmp_path / "progress").mkdir()
    (tmp_path / "progress/PROGRESS.md").write_text("Current lesson: 01")
    with pytest.raises(ValueError, match="LESSON.md"):
        load_navigation().current_lesson(tmp_path)


def test_ambiguous_lesson_rejected(tmp_path):
    (tmp_path / "progress").mkdir()
    (tmp_path / "progress/PROGRESS.md").write_text("Current lesson: 01")
    for name in ["01-first", "01-duplicate"]:
        folder = tmp_path / "lessons" / name
        folder.mkdir(parents=True)
        (folder / "LESSON.md").write_text("draft")
    with pytest.raises(ValueError, match="exactly one LESSON"):
        load_navigation().current_lesson(tmp_path)


def test_lesson_examples_execute_with_documented_output():
    text = (LESSON / "LESSON.md").read_text()
    blocks = re.findall(r"```python\n(.*?)```", text, re.DOTALL)
    expected = ["Check the queue", "Staff the queue", "Retry carefully", "Standard queue",
                "0\n16\n4", "10\n0", "True", "True\nFalse\nTrue", "Unsupported size", "", ""]
    assert len(blocks) == len(expected)
    for block, output in zip(blocks, expected):
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            exec(compile(block, str(LESSON / "LESSON.md"), "exec"), {})
        assert stream.getvalue().strip() == output


def test_optional_starter_is_importable_but_unfinished():
    namespace = {}
    exec((LESSON / "STARTER.py").read_text(), namespace)
    with pytest.raises(NotImplementedError, match="Learner implements"):
        namespace["summarize_tickets"]([])


def test_relative_markdown_links_resolve():
    # Check actual authored links, not free-form backtick references or placeholders.
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", path.read_text()):
            if "://" in target or target.startswith("#"):
                continue
            assert (path.parent / target.split("#")[0]).exists(), (path, target)
