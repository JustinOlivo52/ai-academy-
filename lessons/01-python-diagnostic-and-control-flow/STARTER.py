"""Optional independent interfaces. Never copy over an existing student attempt."""


def priority_for(ticket):
    """Return HIGH/MEDIUM/LOW/INVALID under independent lab contract v2."""
    raise NotImplementedError("Learner implements the independent priority policy")


def summarize_tickets(tickets):
    """Return total/urgent/non_urgent/invalid counts under unchanged contract v1."""
    raise NotImplementedError("Learner implements the independent summary")
