"""Student-facing acceptance tests; run when ready to implement ticket_rules."""
import pytest
from practice.ticket_rules import calculate_priority

@pytest.mark.parametrize('urgency,impact,expected',[(5,5,'HIGH'),(4,4,'HIGH'),(3,2,'MEDIUM'),(1,1,'LOW')])
def test_priorities(urgency,impact,expected):
    assert calculate_priority(urgency,impact)==expected

@pytest.mark.parametrize('urgency,impact',[(0,3),(6,1),(True,4),('5',3)])
def test_reject_invalid(urgency,impact):
    with pytest.raises((ValueError,TypeError)):
        calculate_priority(urgency,impact)
