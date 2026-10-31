# Independent lab — support-ticket priority and reporting

**Time:** about 20 minutes after needed teaching/guided practice. Contract: assessment v2 includes new priority behavior AND the unchanged summary contract v1. Previous summary attempts/evidence remain valid as v1; do not rewrite them to resemble a supplied answer. No full solution is included.

Work in student_work/lesson_01.py if it is still your unused workspace. Preserve previous attempts; otherwise choose a new file and set ACADEMY_SUBMISSION to its repository-relative Python path. The optional STARTER.py supplies signatures only. Do not copy it over completed work.

## Function A: priority_for(ticket)
- Input is a dictionary. Only urgency and impact are relevant. Missing either field is invalid; extra fields/IDs are ignored.
- Each score must have exact type int, excluding bool, and inclusive range 1..5. Strings, floats, None, containers and out-of-range integers are invalid. No coercion and no mutation.
- Return the string INVALID if either score is invalid. This is a defined decision, not an exception for bad score values.
- Otherwise return HIGH if urgency >= 4 AND impact >= 4.
- Otherwise return MEDIUM if urgency >= 3 OR impact >= 3.
- Otherwise return LOW. Every valid record gets exactly one priority. HIGH wins where predicates overlap.
- No printing, external effects or shared mutable state. Top-level non-dictionaries are outside this contract.

Examples: urgency=4/impact=4 → HIGH; 5/2 → MEDIUM; 2/2 → LOW; True/5 → INVALID. Produce your own decision table before implementation, including an overlapping case and two malformed cases. Do not implement the worked waiting-time/VIP policy here.

## Function B: summarize_tickets(tickets), unchanged v1
- Input is a list of dictionaries; IDs/extra fields are not validated or changed. Top-level non-lists/non-dictionary records are outside scope.
- Return exactly {"total": int, "urgent": int, "non_urgent": int, "invalid": int}, all nonnegative ordinary integer counts.
- Count every record in total. Valid urgency has exact type int in 1..5, excluding bool. Missing, None, strings (including "4"), floats, booleans, containers and out-of-range values are invalid, with no coercion.
- Valid urgency >= 4 is urgent; valid urgency below 4 is non_urgent. Invalid records count once in invalid and processing continues. Categories are exclusive.
- Empty input returns all four zeros. Each call returns a fresh summary; never mutate input, print or perform I/O. Invariant: total == urgent + non_urgent + invalid.

Example: [{"urgency":4}, {"urgency":2}, {}, {"urgency":"5"}, {"urgency":5}] → {"total":5, "urgent":2, "non_urgent":1, "invalid":2}.

The summary's urgent category uses urgency only. HIGH priority uses urgency AND impact. Do not derive urgent count from priority_for; a high-urgency/low-impact ticket is urgent but may only have MEDIUM priority. This distinction is the main professional integration requirement.

## Deliverables and acceptance criteria
1. Both learner-authored functions with contract-correct decisions, validation and readable control flow.
2. At least three learner-written pytest tests: one overlap/threshold distinction, one malformed score/type case, and one multi-record or non-mutation regression. Explain what plausible bug each test would catch; do not merely repeat one happy path three times.
3. An explanation of guard placement, rule order, scope of return/continue, and the summary partition invariant.
4. Supplied suites actually pass on the final submission, and own tests run with results recorded. In chat, an unexecuted attempt remains execution pending.

```bash
python -m pytest -q assessments/lesson_01/test_priority.py assessments/lesson_01/test_summary.py
# Run your own test file separately too, using its actual path.
```

Initially these explicit suites fail because student functions are unfinished. Default `python -m pytest -q` checks course material/tooling only. Never change acceptance expectations to make incorrect code pass. The later practice/calculate_priority lab remains available for function/module refactoring in Lesson 03; these are separate attempts, not overwritten work.

## Assessment extension
After reviewing the submission, the assessor gives a fresh small requirement (with an explicit contract) to implement and test without hints. It is not published as the current assignment's hidden requirement. Passing requires that evidence as well as conceptual explanation and a checked edge case. Doing this lab with hints earns practice; use a fresh variation to demonstrate independent mastery.
