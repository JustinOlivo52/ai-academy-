"""Explicit student acceptance tests; intentionally outside default course checks."""
from copy import deepcopy
import importlib.util
import os
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]


@pytest.fixture
def summarize():
    path = (ROOT / os.environ.get("ACADEMY_SUBMISSION", "student_work/lesson_01.py")).resolve()
    if not path.is_relative_to((ROOT / "student_work").resolve()) or path.suffix != ".py":
        pytest.fail("ACADEMY_SUBMISSION must name a Python file inside student_work")
    if not path.is_file():
        pytest.fail(f"Submission does not exist: {path}")
    spec = importlib.util.spec_from_file_location("academy_student_attempt", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    function = getattr(module, "summarize_tickets", None)
    if not callable(function):
        pytest.fail("Implement summarize_tickets(tickets) in your student file; see Lesson 01 contract v1")
    return function


def expected(total=0, urgent=0, non_urgent=0, invalid=0):
    return dict(total=total, urgent=urgent, non_urgent=non_urgent, invalid=invalid)


def test_empty(summarize):
    assert summarize([]) == expected()


@pytest.mark.parametrize("value,urgent", [(1, False), (2, False), (3, False), (4, True), (5, True)])
def test_each_valid_boundary(summarize, value, urgent):
    assert summarize([{"urgency": value}]) == expected(1, int(urgent), int(not urgent))


@pytest.mark.parametrize("record", [{}, {"urgency": None}, {"urgency": "4"},
    {"urgency": 4.0}, {"urgency": True}, {"urgency": False},
    {"urgency": 0}, {"urgency": 6}, {"urgency": -1}, {"urgency": []}, {"urgency": {}}])
def test_invalid_once(summarize, record):
    assert summarize([record]) == expected(1, invalid=1)


def test_mixed_batch_continues(summarize):
    tickets = [{"urgency": 4}, {}, {"urgency": 2}, {"urgency": "5"}, {"urgency": 5}]
    result = summarize(tickets)
    assert result == expected(5, 2, 1, 2)
    assert result["total"] == result["urgent"] + result["non_urgent"] + result["invalid"]


def test_input_preserved(summarize):
    tickets = [{"urgency": 5, "notes": ["fictional"]}, {}, {"urgency": "4"}]
    before = deepcopy(tickets)
    summarize(tickets)
    assert tickets == before


def test_fresh_calls_and_integer_counts(summarize):
    first = summarize([{"urgency": 5}])
    assert all(type(count) is int and count >= 0 for count in first.values())
    first["urgent"] = 99
    assert summarize([]) == expected()
    assert summarize([{"urgency": 1}]) == expected(1, non_urgent=1)


def test_no_output(summarize, capsys):
    summarize([{"urgency": 4}])
    captured = capsys.readouterr()
    assert captured.out == captured.err == ""
