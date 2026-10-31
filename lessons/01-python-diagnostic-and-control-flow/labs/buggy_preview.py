"""Intentionally faulty debugging exercise; never a production example.

Contract: return every input record's (ticket_id, channel), including IGNORE,
preserve order/input, and return [] for empty input. Reproduction checks should
fail until the LEARNER creates a corrected version in a new student file.
"""
from pathlib import Path
import runpy

ROOT = next(parent for parent in Path(__file__).resolve().parents
            if (parent / "academy.py").is_file())
escalation_channel = runpy.run_path(str(
    ROOT / "lessons/01-python-diagnostic-and-control-flow/examples/escalation.py"
))["escalation_channel"]


def preview_escalations(tickets):
    result = []
    for ticket in tickets:
        channel = escalation_channel(ticket)
        if channel == "IGNORE":
            break
        result.append((ticket["ticket_id"], channel))
        return result


if __name__ == "__main__":
    sample = [
        {"ticket_id": "B-1", "status": "open", "minutes_waiting": 60, "vip": False},
        {"ticket_id": "B-2", "status": "closed"},
        {"ticket_id": "B-3", "status": "open", "minutes_waiting": 2, "vip": False},
    ]
    print(preview_escalations(sample))
    print(preview_escalations([]))
