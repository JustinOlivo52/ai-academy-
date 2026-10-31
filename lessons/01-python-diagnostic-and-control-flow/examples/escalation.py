"""Worked teaching example: waiting-time escalation, not the student assignment."""


def escalation_channel(ticket):
    """Route a fictional ticket under the Lesson 01 worked-example policy.

    Closed tickets are ignored before timing validation. Open tickets require
    exact integer minutes 0..1440 and an explicit Boolean vip value.
    """
    status = ticket.get("status")
    if status == "closed":
        return "IGNORE"  # Lifecycle policy wins; no notification is needed.
    if status != "open":
        return "REVIEW"  # Unknown lifecycle state must not trigger paging.

    minutes = ticket.get("minutes_waiting")
    vip = ticket.get("vip")
    if type(minutes) is not int or not 0 <= minutes <= 1440:
        return "REVIEW"  # Reject bool, strings, missing and out-of-range data.
    if type(vip) is not bool:
        return "REVIEW"  # Do not interpret a nonempty string as a Boolean flag.

    needs_on_call = minutes >= 60 or (vip and minutes >= 15)
    if needs_on_call:
        return "ON_CALL"
    if minutes >= 15:
        return "SERVICE_DESK"
    return "QUEUE"


def demo():
    tickets = [
        {"ticket_id": "S-10", "status": "closed"},
        {"ticket_id": "S-11", "status": "open", "minutes_waiting": 15, "vip": False},
        {"ticket_id": "S-12", "status": "open", "minutes_waiting": 15, "vip": True},
        {"ticket_id": "S-13", "status": "open", "minutes_waiting": "60", "vip": False},
        {"ticket_id": "S-14", "status": "open", "minutes_waiting": 5, "vip": False},
    ]
    for ticket in tickets:
        print(ticket["ticket_id"], escalation_channel(ticket))


if __name__ == "__main__":
    demo()
