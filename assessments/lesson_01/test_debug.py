"""Reproduce course bugs by default; select a learner correction to assess the fix."""
import os
from pathlib import Path
import runpy

import pytest

ROOT = Path(__file__).resolve().parents[2]


@pytest.fixture
def preview(load_student):
    submission = os.environ.get("ACADEMY_DEBUG_SUBMISSION")
    if submission:
        return load_student(submission, "preview_escalations")
    return runpy.run_path(str(ROOT / "lessons/01-python-diagnostic-and-control-flow/labs/buggy_preview.py"))["preview_escalations"]


def test_debug_empty(preview):
    assert preview([]) == []


def test_debug_continues_after_closed(preview):
    tickets = [
        {"ticket_id": "B-1", "status": "open", "minutes_waiting": 60, "vip": False},
        {"ticket_id": "B-2", "status": "closed"},
        {"ticket_id": "B-3", "status": "open", "minutes_waiting": 2, "vip": False},
    ]
    assert preview(tickets) == [("B-1", "ON_CALL"), ("B-2", "IGNORE"), ("B-3", "QUEUE")]


def test_debug_closed_first_is_still_a_record(preview):
    assert preview([{"ticket_id": "B-0", "status": "closed"}]) == [("B-0", "IGNORE")]
