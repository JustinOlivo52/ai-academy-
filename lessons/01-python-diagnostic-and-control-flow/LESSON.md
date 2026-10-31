# Lesson 01 — Python Diagnostic and Control Flow

**Stage:** Python Programming Foundations · **Status:** reference chapter, contract v1
**Duration:** 90–120 minutes across multiple sessions; 15–20 minutes can cover one concept and a small exercise.
**Prerequisites:** recognize variables, numbers, strings and basic Python syntax. Dictionary access and the small function interface needed here are refreshed below. No packages, LLM account or terminal are needed to begin on a phone.

## Objectives
By the end you can trace a branch and loop, translate a written rule into an exact Boolean condition, count matching records without resetting state, skip invalid records without stopping a batch, and independently write, test and explain a non-mutating summary function. These are behaviors to demonstrate, not boxes awarded for reading.

## 1. Decisions are executable requirements
A program executes statements in order unless control flow changes that order. A condition produces a Boolean, `True` or `False`. An `if` runs its indented body when the condition is true. An `else` covers the remaining case. Indentation is part of Python's syntax: four spaces inside a block show which statements belong together.

```python
minutes_waiting = 12
if minutes_waiting >= 10:  # Includes exactly ten minutes.
    print("Check the queue")
else:
    print("Continue monitoring")
# Output: Check the queue
```

Read the condition aloud: “minutes waiting is greater than or equal to ten.” A requirement saying “at least” includes equality, whereas “more than” does not. Professional confidence starts with making this translation explicit and checking the boundary. For a threshold of ten, check nine, ten and eleven rather than testing only a large value that would satisfy either interpretation.

`=` assigns a value; `==` asks whether two values are equal. `!=` means unequal; `<` and `<=` are the corresponding lower-bound comparisons. `and` requires both conditions, `or` requires at least one, and `not` reverses a truth value. Use parentheses when combining rules so the intended grouping is visible to the next engineer.

```python
is_weekday = True
open_requests = 6
if is_weekday and open_requests > 0:
    print("Staff the queue")  # Both requirements hold.
# Output: Staff the queue
```

### Branch ordering and the diagnostic
`elif` means “otherwise, if.” In an `if`/`elif`/`else` chain, Python chooses the first true branch and skips the rest. Two independent `if` statements can both run. Choose a chain when outcomes are mutually exclusive; use separate conditions when more than one action should happen.

```python
attempts = 3
if attempts >= 5:
    print("Stop")
elif attempts >= 2:
    print("Retry carefully")
else:
    print("Retry normally")
# Output: Retry carefully. The >= 5 branch was false.
```

**Instructor pause — diagnostic:** What prints below, and why? Wait for the learner's response before explaining the result or offering a hint.

```python
urgency = 5
if urgency >= 3:
    print("Standard queue")
elif urgency >= 5:
    print("Priority queue")
else:
    print("Low priority")
```

If the answer shows confusion, trace conditions in execution order using a different value. Then ask the learner to change the order to match the intended priority. Do not repair their code for them.

## 2. A loop repeats work; state remembers results
A list stores an ordered collection. A `for` loop binds its loop variable to each item in turn. The indented block runs once per item. When the list is empty, the block runs zero times; execution resumes after the loop. There is no need for a special empty-list branch if the initial state already represents the correct empty result.

```python
delays = [0, 8, 2]
for delay in delays:
    print(delay * 2)  # delay is a new item on each iteration.
# Output on separate lines: 0, 16, 4
```

The loop variable holds the current item, not the entire list. To remember information across iterations, initialize an accumulator before the loop. `+=` adds to the existing value. A variable created inside a loop is not a new persistent total on each iteration if you assign zero to it every time: that assignment erases the previous total.

### Practical walkthrough — total waiting time
This is a separate example, not the ticket-summary assignment. The requirement is to total nonnegative waiting times, ignoring a negative value that indicates unavailable data.

```python
def total_wait(values):
    total = 0                 # Initial state; also correct for an empty list.
    for value in values:
        if value < 0:
            continue          # Skip this item, then visit the next one.
        total += value        # This item contributes to the running total.
    return total              # Return only after the entire batch is visited.

print(total_wait([3, -1, 7]))   # Output: 10
print(total_wait([]))          # Output: 0
```

Walk through the state rather than guessing from the final output:

| Step | Current value | Decision | Total afterward |
| --- | --- | --- | --- |
| Before loop | — | initialize | 0 |
| First visit | 3 | include | 3 |
| Second visit | -1 | skip | 3 |
| Third visit | 7 | include | 10 |
| After loop | — | return | 10 |

`continue` skips the rest of the current iteration. `break` exits the loop entirely. `return` exits the entire function, not just the loop. These are different scopes of control. A `return` indented inside the loop can silently process only the first record. With an empty input, that misplaced return might never execute and Python would return `None` implicitly.

The example assumes numeric values. A string such as `"3"` would make the comparison fail. That does not mean every function must solve every input problem; it means its contract must say which inputs it supports. The independent lab below explicitly defines bad urgency values.

**Instructor pause:** Ask the learner to predict the result for `[0, -1, 4]`, including the total after each visit. Wait before introducing the next concept.

## 3. Records, missing fields and safe comparisons
A dictionary associates names with values. A ticket might be `{"ticket_id": "T-101", "urgency": 4}`. `ticket["urgency"]` retrieves a required key but raises `KeyError` if it is absent. `ticket.get("urgency")` returns `None` when it is absent. `None` is a sentinel meaning no value; it is not the number zero and must not be compared with an integer using `>=`.

```python
job = {"name": "daily-export"}
value = job.get("retries")
print(value is None)  # Output: True. The key was absent.
```

Do not use `if not value` as a substitute for a precise missing-value rule. Zero, `False`, an empty string and `None` are all false-like in a condition, but they can mean different things. A reliable batch processor classifies bad data deliberately instead of accidentally treating it as a low score.

For this lesson's lab, only ordinary integer urgency values from 1 through 5 are valid. Boolean values are excluded, even though Python treats `bool` as a subtype of `int`. That makes an exact type check useful here:

```python
print(type(3) is int)     # True
print(type(True) is int)  # False
print(isinstance(True, int))  # True: bool is an int subclass.
```

This is a deliberate contract choice, not a universal ban on `isinstance`. Later lessons will cover validation models and richer interfaces. Here, separate “is the value valid?” from “does a valid value meet the business rule?” Validate type before numeric comparisons. Python short-circuits Boolean expressions: with `and`, a false left side prevents evaluation of the right side; with `or`, a true left side prevents it. Clear separate branches are equally acceptable.

```python
size = "large"
if type(size) is int and size > 0:
    print("Numeric positive size")
else:
    print("Unsupported size")
# Output: Unsupported size. Python never compares "large" with zero.
```

A dictionary lookup does not mutate the input. Assigning to `ticket["urgency"]` does. Avoid “fixing” input records by adding defaults or converting strings in place when the contract promises not to change them. Other code may still hold a reference to that same dictionary.

**Instructor pause:** Ask the learner what `get` returns for an absent key, and why comparing that result to 4 needs a prior decision. Wait for an answer.

## 4. Why this matters in an engineering role
An automation engineer often receives a batch of API records, validates fields and chooses a route. A single misplaced return can silently discard most of the batch. A loose comparison can send a boundary case down the wrong path. A hidden mutation can make a later API request or test behave differently.

In Project 1 you will build a ticket processor. Lesson 01 supplies its first small, deterministic reporting component; Lesson 02 adds indexing, Lesson 03 separates interfaces and priority rules, and later lessons add validation, files and tests. This lesson's **urgent** means urgency alone is at least 4. Project 1's later **HIGH priority** means urgency AND impact are at least 4. These are different named requirements; do not combine them accidentally.

Separating pure computation from printing, file writes and model calls makes code easier to review and test. A pure summary function returns data for another layer to display. The same input should produce the same output, without changing caller-owned records or making network calls.

## Guided practice — one task per turn
The instructor should reveal these progressively, never as a list of homework during conversation.

1. With numeric urgency values `[4, 2, 5]`, write a loop and condition that count values at least 4. Expected count: 2. First state the initial count and why it belongs outside the loop. Let the learner submit before hints.
2. Change the values to `[3, 4, 1, 5]`. Ask for the count after each iteration, then have the learner change the rule to “strictly greater than 4” and predict the changed result. Do not give both versions of the code.
3. Use `[{"urgency": 5}, {}, {"urgency": 2}]`. Ask for code that visits all records and skips a missing urgency. Only add type and range checks after the learner explains why the missing value needs special handling.

For an incorrect answer, explain with a trace rather than immediately rewriting code. First hint: identify which statement owns the remembered total. Stronger hint: show a loop skeleton with the update and condition left blank. If a solution is supplied at the learner's request, mark that activity assisted and use a fresh variation for assessment.

## Independent assignment — summarize a fictional queue
Work in `student_work/lesson_01.py`; preserve existing contents and add your own function. If it already contains a completed attempt, create a new attempt file instead and set `ACADEMY_SUBMISSION` to its repository-relative path when running tests. `STARTER.py` in this lesson is an optional interface-only template; it is not a solution and must not overwrite your work.

Implement `summarize_tickets(tickets)`. A function begins with `def`, receives its named argument, and returns a value to its caller. `print` displays text; it does not substitute for returning a dictionary. The lab deliberately supplies the interface so you can focus on control flow; Lesson 03 studies function design in depth.

### Exact contract, version 1
- Input is a Python list of dictionaries. IDs and extra fields are not validated or changed in this lesson. Records need not have an ID for this summary. Non-list input and non-dictionary records are outside scope.
- Count every input record in `total`, including invalid ones.
- A valid urgency has exact type `int` (not bool) and is in inclusive range 1..5. Missing urgency, `None`, strings (including `"4"`), floats, booleans and out-of-range integers are invalid. Do not coerce them.
- Valid urgency >= 4 counts in `urgent`; valid urgency below 4 counts in `non_urgent`.
- Every invalid record counts once in `invalid` and processing continues to the next record. Invalid is not also non-urgent.
- Return exactly `{"total": int, "urgent": int, "non_urgent": int, "invalid": int}` with nonnegative counts. For every input, `total == urgent + non_urgent + invalid`.
- Empty input returns all four counts as zero. Return a fresh summary for each call; do not reuse global state, mutate input, print output or perform I/O.

Before code, write your proposed interface and two input/output examples, including a boundary or invalid case. For this sample:

```python
tickets = [
    {"ticket_id": "T-101", "urgency": 4},
    {"ticket_id": "T-102", "urgency": 2},
    {"ticket_id": "T-103"},
    {"ticket_id": "T-104", "urgency": "5"},
    {"ticket_id": "T-105", "urgency": 5},
]
# Required return value:
# {"total": 5, "urgent": 2, "non_urgent": 1, "invalid": 2}
```

Deliver your function, at least one learner-written regression test, and an explanation in your own words. The instructor reviews actual work, not a hypothetical finished solution.

### Automated tests and running them
From the repository root, after installing requirements:

```bash
python -m pytest -q assessments/lesson_01/test_summary.py
```

The suite covers empty input, every valid boundary, missing/malformed values, mixed batches, continuation, non-mutation, repeat calls and no printed output. Initially it fails because the preserved student file has no function; the optional STARTER raises `NotImplementedError` when called. Both are intentional incomplete states, not installation failures. Once you implement the function, failing assertions identify behavior to investigate. Do not weaken tests to get green output.

`python -m pytest -q` checks course integrity only. It never proves your lab is complete. The later `practice/test_ticket_rules.py` tests a different assignment. On a phone you can submit code in chat and reason through cases; until somebody actually executes the acceptance suite, execution evidence stays pending.

## Debugging challenge — find the early exit
A colleague wrote this separate waiting-time function:

```python
def sum_delays(delays):
    total = 0
    for delay in delays:
        total += delay
        return total
```

Requirement: sum every numeric value; empty input returns 0. Reproduce with `[2, 3, 4]` (expected 9) and `[]` (expected 0). Predict actual behavior before running. Explain the smallest root cause, write the correction yourself in a new student file, and add regression tests for multi-item and empty input. Do not just special-case these two inputs. The instructor should ask for one step at a time and wait before revealing the cause.

## Knowledge checks — ask one at a time
1. When do two independent `if` statements behave differently from an `if`/`elif` chain?
2. Why does placing an accumulator initialization inside a loop change a batch result?
3. How do `continue`, `break` and `return` differ when used inside a function's loop?
4. Why must a missing or malformed urgency be handled before comparison, and why is `True` invalid in this contract?
5. Which tests distinguish urgency `> 4` from `>= 4`, and how would you demonstrate that input was not mutated?

## Common mistakes and troubleshooting
| Symptom | Likely cause | Investigation |
| --- | --- | --- |
| Only one record counted | return inside loop, or break used to skip invalid data | Trace a three-record input and mark the exit point |
| Count never exceeds one | counter reset inside the loop | Write the value before/after each visit |
| Urgency 4 not urgent | strict > instead of inclusive >= | Test values 3, 4 and 5 separately |
| KeyError for one ticket | direct indexing of an optional field | Compare required-key access with get |
| TypeError comparing values | invalid type reached numeric comparison | Inspect type before applying the rule |
| True counted as urgency 1 | isinstance(True, int) is true | Check the exact contract and type behavior |
| Empty input returns None | return only runs during iteration | Trace zero iterations; inspect function exit |
| Result prints but caller gets None | print used instead of return | Assign the call result and inspect it |
| Second call has old counts | shared/global accumulator | Call twice with different batches |
| Original dictionaries changed | assignment used to normalize input | Compare a deep copy before and after |

When an assertion fails, read its input and expected output, reproduce the smallest case, predict the path, then run it. Change one cause and repeat the relevant check. Do not add broad exception handling to hide a control-flow bug. If pytest is unavailable, install requirements in the selected interpreter; if imports fail, run from the repository root and verify the selected submission path.

## Summary
Conditions translate requirements into branches; their order and boundaries are observable behavior. Loops repeat those decisions across records, while accumulators preserve information across iterations. Validation separates unusable data from valid data that does not match a business rule. Return data after the whole batch, keep caller-owned input intact, and check both ordinary and edge cases. These habits make small changes explainable in a review and form the base of the progressive ticket processor.

## Completion criteria
- [ ] Guided work and the debugging challenge completed by the learner.
- [ ] Independent summary meets the published contract and relevant tests actually pass.
- [ ] Learner-written regression test covers an explained bug or edge case.
- [ ] Five knowledge checks discussed; misconceptions corrected by the learner.
- [ ] Unassisted explanation, one checked edge case and a small fresh modification meet the assessment gate.
- [ ] Evidence record saved; only then mark passed and advance. Reading alone is studied, never mastery.

## Go Deeper — two resources
1. **Official Python tutorial — control flow:** https://docs.python.org/3/tutorial/controlflow.html
2. **Real Python — for loops:** https://realpython.com/python-for-loop/

These are optional reinforcement, not prerequisites. If either is inaccessible or requires membership, continue with this chapter. Link verification status is recorded in `curriculum/LINK_AUDIT.md`.

## Next lesson
After a passed assessment, continue to Lesson 02 — Lists, dictionaries and comprehensions. If interrupted, record the exact pending question and resume there; do not restart or advance based on time spent.
