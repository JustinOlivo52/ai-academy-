"""Guided preview tests; practice evidence, not lesson mastery."""
from copy import deepcopy
import os

import pytest


@pytest.fixture
def preview(load_student):
    return load_student(os.environ.get("ACADEMY_GUIDED_SUBMISSION", "student_work/lesson_01_preview.py"),
                        "preview_escalations")


def test_empty_and_fresh(preview):
    first = preview([])
    assert first == []
    first.append(("injected", "QUEUE"))
    assert preview([]) == []


def test_every_record_in_order(preview):
    tickets = [
        {"ticket_id": "G-1", "status": "open", "minutes_waiting": 60, "vip": False},
        {"ticket_id": "G-2", "status": "closed"},
        {"ticket_id": "G-3", "status": "open", "minutes_waiting": 3, "vip": False},
        {"ticket_id": "G-4", "status": "open", "minutes_waiting": "15", "vip": True},
    ]
    assert preview(tickets) == [("G-1", "ON_CALL"), ("G-2", "IGNORE"),
                                ("G-3", "QUEUE"), ("G-4", "REVIEW")]


def test_preserves_input_and_no_output(preview, capsys):
    tickets = [{"ticket_id": "G-5", "status": "open", "minutes_waiting": 15,
                "vip": False, "notes": ["fictional"]}]
    before = deepcopy(tickets)
    assert preview(tickets) == [("G-5", "SERVICE_DESK")]
    assert tickets == before
    captured = capsys.readouterr()
    assert captured.out == captured.err == ""
