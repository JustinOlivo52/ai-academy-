"""Tests of actual complete teaching code, separate from unimplemented labs."""
from copy import deepcopy
from pathlib import Path
import runpy

import pytest

ROOT = Path(__file__).resolve().parents[1]
WORKED = ROOT / "lessons/01-python-diagnostic-and-control-flow/examples/escalation.py"
escalation_channel = runpy.run_path(str(WORKED))["escalation_channel"]


@pytest.mark.parametrize("minutes,vip,expected", [
    (0, False, "QUEUE"), (0, True, "QUEUE"), (14, False, "QUEUE"), (14, True, "QUEUE"),
    (15, False, "SERVICE_DESK"), (15, True, "ON_CALL"),
    (59, False, "SERVICE_DESK"), (59, True, "ON_CALL"),
    (60, False, "ON_CALL"), (60, True, "ON_CALL"), (1440, False, "ON_CALL"),
])
def test_escalation_boundaries(minutes, vip, expected):
    assert escalation_channel({"status": "open", "minutes_waiting": minutes, "vip": vip}) == expected


@pytest.mark.parametrize("minutes", [None, "60", 60.0, True, False, -1, 1441, [], {}])
def test_invalid_minutes_review(minutes):
    assert escalation_channel({"status": "open", "minutes_waiting": minutes, "vip": False}) == "REVIEW"


@pytest.mark.parametrize("vip", [None, "False", 0, 1, []])
def test_strict_vip(vip):
    assert escalation_channel({"status": "open", "minutes_waiting": 60, "vip": vip}) == "REVIEW"


@pytest.mark.parametrize("record", [{}, {"status": "pending"}, {"status": "open"},
    {"status": "open", "minutes_waiting": 60}, {"status": "open", "vip": True}])
def test_missing_unknown_fields_review(record):
    assert escalation_channel(record) == "REVIEW"


def test_lifecycle_precedes_timing_validation():
    assert escalation_channel({"status": "closed", "minutes_waiting": "bad", "vip": "False"}) == "IGNORE"


def test_worked_example_has_no_effects(capsys):
    ticket = {"status": "open", "minutes_waiting": 60, "vip": False, "notes": ["fictional"]}
    before = deepcopy(ticket)
    assert escalation_channel(ticket) == "ON_CALL"
    assert ticket == before
    captured = capsys.readouterr()
    assert captured.out == captured.err == ""


def test_worked_demo_output(capsys):
    runpy.run_path(str(WORKED), run_name="__main__")
    assert capsys.readouterr().out == "S-10 IGNORE\nS-11 SERVICE_DESK\nS-12 ON_CALL\nS-13 REVIEW\nS-14 QUEUE\n"


def test_guided_starter_imports_without_solving_the_lab():
    starter = ROOT / "lessons/01-python-diagnostic-and-control-flow/labs/GUIDED_STARTER.py"
    namespace = runpy.run_path(str(starter))
    assert namespace["escalation_channel"]({"status": "closed"}) == "IGNORE"
    with pytest.raises(NotImplementedError, match="Learner implements"):
        namespace["preview_escalations"]([])
