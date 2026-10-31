# Lesson 01 — Python Control Flow and Business Logic

**Stage:** Python Programming Foundations · **Edition:** full-course reference, assessment v2
**Duration:** 60–90 minutes of active learning including labs when basic syntax is familiar; remediation or a first encounter may need longer. Split at section boundaries without dropping material.
**Prerequisites:** basic variables, lists/dictionaries, function calls and running a Python file. The diagnostic determines which refreshers you need. Prior Python/LangGraph projects are useful context, not a reason to repeat syntax you can already demonstrate.

## Learning outcomes and course route
You will translate ambiguous business language into decision tables, implement ordered Boolean rules, validate before comparison, distinguish truthiness from validity, choose between guards and nested branches, process batches without losing records, and justify a loop or comprehension in review. You will demonstrate those skills through independently authored code, boundary tests and a small changed requirement.

This chapter is the teaching source. [DIAGNOSTIC.md](DIAGNOSTIC.md) maps existing skill to sections you can skip; [GUIDED_LAB.md](GUIDED_LAB.md) contains the staged lab, [ASSIGNMENT.md](ASSIGNMENT.md) specifies the independent work, and [the assessment](../../assessments/lesson_01/ASSESSMENT.md) defines the evidence gate. Do not work through all elementary examples if you have already demonstrated them. Do not confuse skipping instruction with passing the practical assessment.

A typical route allocates 8 minutes to diagnosis, 20–25 to needed teaching and the worked example, 15 to guided programming, 20 to independent work, 7 to debugging, and 10 to assessment/review. These are estimates, not timers that award completion. A strong diagnostic shortens refreshers; it does not remove independent implementation. FULL COURSE MODE is the default even on a phone. MOBILE REVIEW MODE is optional reinforcement when explicitly requested.

## 1. From business language to an executable policy
Imagine joining a team that automates a support queue. A stakeholder says, “Escalate important tickets quickly, but don't page anyone for work that's already closed.” An LLM could produce a plausible label from that sentence, but a teammate still needs to know exactly when the system sends a notification. If two engineers interpret “quickly” differently, the code can pass their individual examples and still implement different products. A professional first step is to turn the sentence into a policy with observable inputs and outcomes.

For our worked scenario, the team agrees on this policy: closed tickets require no notification; unfamiliar or unusable open-ticket data goes to manual review; open tickets waiting at least 60 minutes go to the on-call engineer; VIP tickets reach on-call after 15 minutes; other open tickets reach the service desk after 15 minutes. Everything else remains queued. These are fictional educational rules, not real service commitments.

| Order | Condition | Outcome | Why this row exists |
| --- | --- | --- | --- |
| 1 | status is closed | IGNORE | Lifecycle takes precedence over timing |
| 2 | status unknown, or open-ticket timing/flag invalid | REVIEW | Unusable data cannot safely trigger a page |
| 3 | minutes >= 60 OR (VIP AND minutes >= 15) | ON_CALL | Two distinct ways to require escalation |
| 4 | minutes >= 15 | SERVICE_DESK | Remaining delayed tickets get ordinary escalation |
| 5 | otherwise | QUEUE | Every accepted input needs a defined outcome |

A decision table makes overlap visible. A VIP ticket at 60 minutes matches rows 3 and 4, so the table must specify which outcome wins. Here the first matching row wins. It also makes boundaries visible: “at least 15” includes 15, and a test at 14 will exercise a different route. Requirements become easier to discuss when you can point to a row rather than a vague adjective.

Here is one narrow slice of that policy, assuming the timing and flag have already been validated. It is a demonstration of Boolean reasoning, not the assignment solution:

```python
minutes = 15
vip = True
long_wait = minutes >= 60              # False at exactly 15.
vip_wait = vip and minutes >= 15       # True: both requirements hold.
needs_on_call = long_wait or vip_wait  # True: either route is enough.
print(needs_on_call)                   # True
```

The intermediate names reveal the policy. In a code review you can explain why a VIP flag alone is insufficient: the ticket must also reach the waiting boundary. That explanation matters more than recognizing the keyword `and`. Your future AI workflow may classify a ticket upstream, but the deterministic policy should remain testable without a model, network or live customer data.

Before writing production logic, identify assumptions too. Is status guaranteed? Is `"15"` acceptable as a number? Is a missing VIP flag equivalent to False? This course deliberately makes those choices explicit instead of silently normalizing questionable input. The diagnostic now checks whether you can already handle related decisions, validation and batches. The instructor presents Diagnostic A as one coherent programming task and waits, then uses its evidence to skip unnecessary refreshers.

## 2. Boolean logic, short-circuiting and truthiness
A comparison such as `minutes >= 15` produces `True` or `False`. A condition is a decision about data; a variable assignment stores data. `=` assigns, `==` compares and `is None` checks for the missing-value sentinel. Once basic syntax is familiar, most real mistakes come from how conditions are combined and what the program assumes about their operands.

`and` requires both predicates to hold. `or` requires at least one. `not` reverses truthiness. For our escalation rule, an ordinary long wait is sufficient on its own, while VIP escalation requires both VIP status and enough waiting time. Parentheses document grouping, even when Python's precedence would produce the same result. Python evaluates `not` before `and`, and `and` before `or`; do not make a reviewer reconstruct a dense expression's precedence to understand a business rule.

| A | B | A and B | A or B |
| --- | --- | --- | --- |
| False | False | False | False |
| False | True | False | True |
| True | False | False | True |
| True | True | True | True |

Notice that this table describes Boolean operands. In Python, `and` and `or` can return an operand itself rather than a new bool. `display_name = supplied_name or "Anonymous"` chooses a fallback for any false-like supplied name. That may be convenient for display text, but it can erase meaningful zero values when used for numeric defaults. Choose an explicit `is None` check when the requirement distinguishes zero from missing.

```python
reported_minutes = 0
wrong_default = reported_minutes or 30   # 0 is false-like: result becomes 30.
explicit_default = 30 if reported_minutes is None else reported_minutes
print(wrong_default, explicit_default)  # 30 0
print(bool("False"), bool(""))          # True False
```

False-like built-in values include `None`, `False`, numeric zero and empty containers/strings. A nonempty string is true-like even if its contents are `"False"`, `"0"` or `"no"`. Consequently, `if ticket.get("vip")` is not adequate validation for a Boolean VIP field. Truthiness asks “does this value act as true in a condition?” Validation asks “is this value allowed by this interface?” They are different questions.

Python short-circuits conditions from left to right. With `and`, a false left operand makes the right operand unnecessary; with `or`, a true left operand makes it unnecessary. That lets you establish safety before a numeric comparison:

```python
candidate = "15"
valid_minutes = type(candidate) is int and 0 <= candidate <= 1440
print(valid_minutes)  # False; the string is never compared with integers.
```

Reversing those operands can raise `TypeError` before the type check has a chance to protect the comparison. More Boolean operators do not automatically make an expression robust: evaluation order matters. If a compound condition becomes hard to reason about, name its parts or use guards rather than nesting more parentheses.

`not (is_closed or is_invalid)` means both that the ticket is not closed and that it is not invalid. De Morgan's rule rewrites this as `(not is_closed) and (not is_invalid)`. This is useful when checking a negative requirement, but the clearest expression is often a positive name such as `can_route`. Avoid ambiguous names like `flag` and double negatives like `not is_not_ready`.

**Section checkpoint:** Explain why `ticket.get("vip") or False` does not validate a VIP field received as the string `"False"`, and describe the contract you would enforce instead. This is one explanation task; the instructor waits before feedback.

## 3. Ordered decisions, guards and early returns
An `if`/`elif`/`else` chain selects the first true branch. It is not a search for the most specific or most important condition. When conditions overlap, order is part of the behavior. Checking the general waiting rule before the on-call rule would send an hour-old ticket to the service desk, because both thresholds hold and the general branch wins first.

```python
def wait_band(minutes):
    if minutes >= 60:           # Specific/highest threshold first.
        return "long"
    elif minutes >= 15:
        return "delayed"
    return "recent"            # Remaining validated values.

print(wait_band(60), wait_band(14))  # long recent
```

The `elif` is optional after a branch that returns. Once a return executes, that function call ends; later statements in the function cannot run. Using `if` followed by `if` can therefore express the same sequence of exclusive outcomes here. By contrast, two independent `if` statements that only print or append can both execute. Decide whether your requirements describe one result or multiple actions before choosing a structure.

A guard clause handles a disqualifying or exceptional case near the beginning, then exits. This keeps the ordinary path less indented. Guards are especially helpful when one cannot safely evaluate the business rule until input is valid. The following teaching function determines a display instruction for a single waiting-time value. It is not a ticket-summary implementation:

```python
def waiting_label(minutes):
    if type(minutes) is not int:
        return "review"            # Type guard protects later comparisons.
    if minutes < 0:
        return "review"            # Domain guard rejects impossible values.
    if minutes == 0:
        return "just arrived"      # Zero is valid and has a specific meaning.
    return "waiting"

print(waiting_label(None), waiting_label(0))  # review just arrived
```

This function is equivalent in purpose to a deeply nested valid-type/valid-range branch, but it makes rejection paths explicit. Guards do not mean “return everywhere.” In a function that processes one record, an early return often makes sense. In a function processing an entire list, returning because one record is invalid would abandon the rest of the batch. The scope of the function determines whether an early return is correct.

Sometimes the right response to invalid data is an exception, sometimes a structured invalid outcome. The contract must choose. Our worked routing example returns REVIEW because manual processing is a valid outcome. Later lessons explore exception boundaries when an entire operation cannot proceed. Do not catch every exception merely to return a normal-looking label; that can hide programming defects as data problems.

A review should ask whether all accepted inputs reach a result, whether any rule is unreachable, and whether the order is intentional. A comment saying “check priority” adds little. A comment saying “closed tickets bypass timing validation because no notification will be sent” records a policy choice a future maintainer might otherwise undo.

**Section checkpoint:** A queue processor calls `return` when it encounters one malformed ticket. Explain when that is correct and when it loses work, using the difference between a single-record function and a batch function.

## 4. Validation and boundary design
A field's name does not prove its type. JSON-like records can carry a number, a numeric string, `None`, a Boolean, or no key at all. Dictionary indexing such as `ticket["urgency"]` asserts a key exists; `.get("urgency")` produces `None` when absent. Use indexing for guaranteed required structure and `.get` when the contract explicitly handles missing data. Neither lookup mutates the dictionary.

For urgency scores this course requires exact integers in 1..5, with no coercion. Why reject `"4"` instead of converting it? Because silent conversion decides an upstream data-quality question without documenting it. A later ingestion layer may deliberately normalize strings, but a business function should have a stable contract. Why reject `True`? Because `bool` is a subclass of `int`, and the number-like behavior of True is not evidence that a Boolean flag is a meaningful urgency score.

```python
print(isinstance(True, int))  # True: Python's type hierarchy.
print(type(True) is int)      # False: exact built-in int only.
score = 4
valid_score = type(score) is int and 1 <= score <= 5
print(valid_score)            # True
```

Exact type checks are a deliberate choice for these simple educational contracts. They are not a universal replacement for `isinstance`, abstract interfaces or typed validation models. A type hint such as `score: int` documents an expectation; ordinary Python does not enforce it at runtime. You still need to decide where validation belongs.

Boundary tests should separate neighboring decisions. For an urgent threshold of 4, use 3, 4 and 5. For the validity domain, use 0, 1, 5 and 6. A large valid number might test the urgency branch but never detect that the code used `>` instead of `>=` at the threshold. Types such as `4.0` and `True` can compare equal to integers, so checking only returned numeric equality is insufficient when the contract specifies exact types.

Missing, invalid and nonmatching are distinct categories. A valid score of 2 is non-urgent; a missing score is invalid. If both increment a “not urgent” count, the result conceals data quality. Make the partition explicit: every input belongs to exactly one category, and the categories sum to the total. That invariant catches entire families of errors, including double-counting and skipped records.

Do not repair the caller's dictionaries to make tests easier. Other code may hold a reference to the same objects. Reading, validating and constructing a separate output avoids surprising a downstream component. In tests, compare against a deep copy when nested fields are present; a shallow list copy would still share its inner dictionaries and could hide mutation.

## 5. Batch control flow and comprehensions
A loop is repeated decision-making with state. An accumulator should be initialized once for the scope over which it summarizes. If it is reset inside the loop, the output reflects only the final iteration's partial history. If it is global or a mutable default argument, it can leak values across unrelated calls. A fresh local result on each call makes behavior easier to test and reason about.

`continue` skips the remaining statements for the current iteration. `break` exits the nearest loop. `return` exits the whole function. These are not interchangeable ways to “skip bad data.” For a batch summary, bad data may need to be counted and processing continued. For a search for the first matching record, stopping early can be exactly what the contract requires. Always connect the control statement to the operation's purpose.

```python
def total_recorded_waits(values):
    total = 0                       # Lives for this one function call.
    for value in values:
        if value is None:
            continue                # Missing observation, not end of batch.
        total += value              # Assumes other values are numeric.
    return total                    # Runs even when the input is empty.

print(total_recorded_waits([3, None, 7]))  # 10
print(total_recorded_waits([]))            # 0
```

Trace the accumulator for `[3, None, 7]`: initialize to zero, add three, skip the missing observation without changing the total, add seven, then return ten. Empty input performs zero loop iterations, so the initialized value is already the correct result. This is an example of choosing a useful initial state rather than adding special-case branches to compensate for a misplaced return.

A comprehension is appropriate when a single expression maps or filters an already-understood collection. For validated fictional tickets, extracting the IDs of open tickets is concise:

```python
validated = [{"ticket_id": "T-1", "status": "open"},
             {"ticket_id": "T-2", "status": "closed"}]
open_ids = [ticket["ticket_id"] for ticket in validated
            if ticket["status"] == "open"]
print(open_ids)  # ['T-1']
```

Read this as “the ID for each ticket whose status is open.” It constructs a new list and preserves iteration order. It does not copy or validate every nested object. It should not perform network calls or mutate input as a side effect. When processing needs several validation guards, separate counters, rejection reasons and multiple decisions, an ordinary loop exposes the workflow more clearly. Clever syntax is not a professional requirement; explainable behavior is.

A useful clean-code progression is: implement the explicit loop, establish tests, then consider a comprehension only if it simplifies the already-correct transformation. Do not refactor and change policy simultaneously; otherwise a failing test leaves two possible causes. The independent summary assignment is intentionally a good place to prefer a loop over a dense comprehension.

**Section checkpoint:** Explain which of these operations suits a comprehension better: extracting IDs from validated open records, or producing four counters while recording invalid data. Justify the choice in terms of clarity and control flow.

## 6. Full worked example — support-ticket escalation
The complete teaching implementation is in [examples/escalation.py](examples/escalation.py). Its policy uses waiting time and VIP status; your independent assignment uses urgency/impact decisions and a summary, so this is a model of engineering practice rather than a ready-made lab answer.

### Step 1: Set the contract and policy precedence
Input is a dictionary. `status` must be open or closed. A closed ticket returns IGNORE immediately even if timing data is absent: our policy explicitly says no notification will be sent. Open tickets require an exact integer `minutes_waiting` from 0 through 1440 and an explicit Boolean `vip`. Unknown status or invalid open-ticket fields return REVIEW. Other dictionary keys are ignored and never changed. No function sends a page; it returns a decision for another layer to act on.

### Step 2: Implement rejection guards before the ordinary path
The complete single-record teaching implementation follows. Its guards and policy predicate are annotated so you can trace the whole decision, not infer missing code.

```python
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
```

```python
# Complete runnable source: examples/escalation.py
from pathlib import Path
import runpy
example = runpy.run_path(str(Path("lessons/01-python-diagnostic-and-control-flow/examples/escalation.py")))
route = example["escalation_channel"]
print(route({"status": "closed"}))  # IGNORE despite absent timing fields.
print(route({"status": "open", "minutes_waiting": "60", "vip": False}))  # REVIEW
```

The implementation first handles lifecycle. It then validates the waiting time and the VIP flag before evaluating the escalation expression. Each guard both states a rejection rule and protects the assumptions of later code. The ordering is intentional: if your business wanted to audit every closed record's timing too, this contract and its tests would need to change. Requirements, not personal preferences about early returns, decide that behavior.

### Step 3: Name the business predicate and return one decision
After validation the implementation names `needs_on_call = minutes >= 60 or (vip and minutes >= 15)`. That expression is safe because the guards established numeric minutes and a Boolean flag. An early return handles ON_CALL. The remaining delay branch handles SERVICE_DESK, and the final return handles QUEUE. There are no side effects or hidden defaults.

Run the full example from the repository root:

```bash
python lessons/01-python-diagnostic-and-control-flow/examples/escalation.py
```

Expected output:

```text
S-10 IGNORE
S-11 SERVICE_DESK
S-12 ON_CALL
S-13 REVIEW
S-14 QUEUE
```

### Step 4: Trace a realistic boundary, then inspect alternatives
For S-12, status is open so neither lifecycle guard returns. Waiting time 15 is an allowed int and VIP True is an allowed bool. The ordinary long-wait predicate is false, but the VIP-and-delay predicate is true, so ON_CALL returns. The later service-desk condition is never reached even though its threshold also holds. At 14 minutes the VIP predicate becomes false and the result becomes QUEUE. At 60 minutes even non-VIP records route to ON_CALL.

| Case | Guard result | On-call condition | Remaining outcome |
| --- | --- | --- | --- |
| closed, no timing | IGNORE return | not evaluated | not evaluated |
| open, minutes="60" | REVIEW return | not evaluated | not evaluated |
| open, minutes=14, VIP=True | pass | False | QUEUE |
| open, minutes=15, VIP=True | pass | True | ON_CALL |
| open, minutes=15, VIP=False | pass | False | SERVICE_DESK |
| open, minutes=60, VIP=False | pass | True | ON_CALL |

If the general delay branch came first, the last two escalation categories would overlap incorrectly. If a Boolean VIP flag were replaced with the string `"False"`, truthiness could accidentally page someone unless validation caught it. If code normalized `minutes_waiting` in place, a downstream component would see a different record. Each failure is connected to an explicit requirement, so tests can target it without relying on a real notification service.

### Step 5: Test behavior and communicate the change
The repository's worked-example tests cover all 4 combinations of VIP values and threshold sides, malformed values, lifecycle precedence, non-mutation and lack of output. One regression example asserts that open/non-VIP at 60 returns ON_CALL, guarding against a reordered general branch. The source and tests are executable course material, not a production service.

A review-ready explanation would identify the contract, which row wins when rules overlap, what bad data does, and how the 14/15 and 59/60 tests support the claim. “It seems to work on my sample” is weaker evidence because the sample may never separate two plausible policies.

## Guided laboratory — build an escalation preview
Use [GUIDED_LAB.md](GUIDED_LAB.md). The learner implements a batch preview around the worked single-record decision, preserving input order and input objects. It has three stages: explain expected outcomes before coding, implement the preview with a runnable starter and acceptance cases, then add a learner-written boundary regression and explain the choice of loop or comprehension. The instructor teaches the relevant section first and reveals one stage at a time. Do not paste all stages as a quiz list.

## Independent assignment — priority decisions and queue summary
Use [ASSIGNMENT.md](ASSIGNMENT.md). Independently implement `priority_for(ticket)` under the urgency-and-impact policy plus the preserved `summarize_tickets(tickets)` v1 contract. The two functions intentionally answer different business questions. At least three learner-written tests must show meaningful boundaries and malformed-data behavior. The instructor does not write either implementation.

## Debugging exercise — a batch preview that loses work
[labs/buggy_preview.py](labs/buggy_preview.py) is intentionally faulty and is never used as the worked solution. Its contract is to preview every ticket as `(ticket_id, channel)`, preserving order and input, with an empty input returning an empty list. It should use the worked single-record policy. Reproduce the failure on open, closed, then open tickets, and on empty input. The documented correct mixed result includes IGNORE for the closed record and still includes the later open record.

Predict behavior, run to reproduce, identify the root causes, then implement your own corrected version in a new student file. Add a failing regression before the correction and show it passing afterward. The supplied reproduction tests are expected to fail against the faulty file. A fix for one sample is insufficient: demonstrate multi-record continuation and empty behavior too. The instructor waits for the learner's investigation before giving hints.

## Conceptual assessment — five review questions
1. Translate the urgency/impact policy into a decision table. Which valid inputs satisfy both the medium and high predicates, and how does the code resolve overlap?
2. Explain truthiness versus validity using zero, None, True and the string "False". What does short-circuit order protect?
3. Compare a guard-return in a single-record function with continue, break and return in a batch processor. Give an appropriate use of each.
4. Explain the summary partition invariant, why input mutation matters, and which tests establish both properties.
5. Choose between a loop and a comprehension for the guided preview and the independent summary; explain how you would test a changed threshold without mixing refactoring with policy changes.

The assessor asks these individually after relevant teaching/lab work, accepts accurate explanations in your own words, and probes a gap rather than requiring memorized wording. Practical assessment additionally requires executed independent code and an unseen small modification; diagnostic exemptions do not bypass that gate.

## Common mistakes, review and troubleshooting
| Symptom | Likely issue | Useful next check |
| --- | --- | --- |
| VIP="False" escalates | truthiness substituted for type validation | exact bool test before the policy |
| urgent boundary behaves differently at 4 | > used where >= was required | adjacent 3/4/5 cases |
| HIGH tickets become MEDIUM | general predicate checked first | truth table for overlap |
| malformed field raises TypeError | comparison before validation | order of guards/short-circuit operands |
| batch ignores records after one bad ticket | break or return used to skip | trace each record and the exit point |
| empty batch returns None | only return is inside a loop | zero-iteration trace |
| counts change across calls | mutable shared/global accumulator | different calls, mutate first result, call again |
| original input changes | normalization performed on caller objects | deep-copy comparison |
| test output is green but no learner code ran | default course checks mistaken for assessment | run the explicit student suite |

Review for descriptive predicate names, explicit policy precedence, useful initial states, limited nesting, no side effects in business functions and comments that explain why a rule exists. Avoid catching broad exceptions to hide contract errors. A clear small function with well-chosen tests is more professional than compressed code that only its author can decipher.

If pytest is missing, install requirements in the selected interpreter and run commands from the repository root. If a student suite reports a missing callable, the starter is still unfinished or the selected file is wrong. It is not evidence that the acceptance suite should be weakened. Phone work can proceed in chat, with execution explicitly pending until the tests run.

## Summary and completion criteria
Control flow turns a policy into execution order. Boolean grouping expresses requirements, guards establish assumptions, ordered branches resolve overlap, and loop control determines how much of a batch gets processed. Truthiness is a language mechanism, not a data schema. Boundary tests distinguish plausible implementations, and invariants plus non-mutation checks expose errors that single happy paths miss. These habits underpin the later ticket CLI, API and AI workflow.

Complete the needed teaching or documented diagnostic exemptions, guided lab (unless independently exempted), debugging regression, independent assignment, five conceptual checks and a fresh small changed requirement. Save actual test evidence and explanation in an assessment record. Only the full gate awards mastery; no upgrade, reading session or default course check changes learner progress.

## Go Deeper — two resources
1. **Official Python tutorial — control flow:** https://docs.python.org/3/tutorial/controlflow.html
2. **Real Python — conditional statements and Boolean behavior:** https://realpython.com/python-conditional-statements/

These reinforce the original chapter; neither is required to understand it. HTTP reachability is logged in the link audit; paid access is never assumed.

## Next lesson
Lesson 02 deepens collection design and transformations after this lesson's assessment passes. If interrupted, resume the exact meaningful section or lab stage with diagnostic exemptions intact. Do not restart with the old one-line branch quiz.
