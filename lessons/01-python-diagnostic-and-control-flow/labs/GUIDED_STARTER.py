"""Copy only to a new student file; the learner writes the batch preview."""
from pathlib import Path
import runpy

# Find the repository from the file location, whether in labs or student_work.
ROOT = next(parent for parent in Path(__file__).resolve().parents
            if (parent / "academy.py").is_file())
escalation_channel = runpy.run_path(str(
    ROOT / "lessons/01-python-diagnostic-and-control-flow/examples/escalation.py"
))["escalation_channel"]


def preview_escalations(tickets):
    """Return ordered (ticket_id, channel) pairs without changing inputs."""
    raise NotImplementedError("Learner implements the guided batch preview")
