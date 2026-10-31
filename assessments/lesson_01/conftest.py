"""Load explicit learner attempts without modifying them."""
import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]


@pytest.fixture
def load_student():
    def load(relative, function):
        path = (ROOT / relative).resolve()
        if not path.is_relative_to((ROOT / "student_work").resolve()) or path.suffix != ".py":
            pytest.fail("Submission must be a Python file inside student_work")
        if not path.is_file():
            pytest.fail(f"Submission missing: {relative}; create your own attempt from the lesson contract")
        spec = importlib.util.spec_from_file_location("academy_attempt", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        result = getattr(module, function, None)
        if not callable(result):
            pytest.fail(f"Implement {function} in {relative}; see the Lesson 01 contract")
        return result
    return load
