"""Independent priority contract v2. Explicit suite, unfinished until learner work."""
from copy import deepcopy
import os

import pytest


@pytest.fixture
def priority(load_student):
    return load_student(os.environ.get("ACADEMY_SUBMISSION", "student_work/lesson_01.py"), "priority_for")


# Independent expected decision table: rows are urgency 1..5, columns impact 1..5.
MATRIX = [
    ["LOW", "LOW", "MEDIUM", "MEDIUM", "MEDIUM"],
    ["LOW", "LOW", "MEDIUM", "MEDIUM", "MEDIUM"],
    ["MEDIUM", "MEDIUM", "MEDIUM", "MEDIUM", "MEDIUM"],
    ["MEDIUM", "MEDIUM", "MEDIUM", "HIGH", "HIGH"],
    ["MEDIUM", "MEDIUM", "MEDIUM", "HIGH", "HIGH"],
]


@pytest.mark.parametrize("urgency,impact,expected", [
    (u, i, MATRIX[u-1][i-1]) for u in range(1, 6) for i in range(1, 6)])
def test_all_valid_pairs(priority, urgency, impact, expected):
    assert priority({"urgency": urgency, "impact": impact}) == expected


@pytest.mark.parametrize("field", ["urgency", "impact"])
@pytest.mark.parametrize("invalid", [None, True, False, "4", 4.0, 0, 6, -1, [], {}])
def test_invalid_score_never_classified(priority, field, invalid):
    ticket = {"urgency": 5, "impact": 5, field: invalid}
    assert priority(ticket) == "INVALID"


@pytest.mark.parametrize("ticket", [{}, {"urgency": 4}, {"impact": 4}])
def test_missing_fields(priority, ticket):
    assert priority(ticket) == "INVALID"


def test_input_preserved_and_no_output(priority, capsys):
    ticket = {"urgency": 5, "impact": 2, "notes": ["fictional"]}
    before = deepcopy(ticket)
    assert priority(ticket) == "MEDIUM"
    assert ticket == before
    captured = capsys.readouterr()
    assert captured.out == captured.err == ""
