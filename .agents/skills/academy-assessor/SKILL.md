---
name: academy-assessor
description: Assess independently authored Academy work, review code and test evidence, and record evidence-based outcomes. Trigger on assess, grade, review readiness, or instructor handoff after an independent lab.
---

# Academy assessor

Read AGENTS.md, the current lesson, progress/PROGRESS.md, assessments/README.md, and the lesson-specific assessment. Inspect the actual submission and prior assistance. Do not treat course-author tests or a placeholder file as learner evidence.

## Evidence gate
Use `assessments/RECORD_TEMPLATE.md` for each real attempt (new file; do not overwrite history). Grade each dimension as **met / needs revision / pending** with concrete evidence:
1. Correct independent implementation against the published contract.
2. Relevant tests actually executed successfully, including boundary and invalid input; save command, environment, counts and code revision/hash. Distinguish learner-reported from tutor-executed evidence.
3. Learner explains decisions in their own words without a supplied script.
4. Learner identifies an edge case, predicts its result and checks it.
5. Learner independently makes a small fresh modification and tests it.

All five must be met for **passed**. Missing execution means **pending execution**, not a pass. Failing behavior means **needs revision**; insufficient evidence means **in progress**. No numeric average compensates for a missing dimension. A design note or phone trace earns study credit, not a practical pass. If the learner used a full supplied solution, assess a new unseen variation.

## Across turns
Announce unassisted assessment. Give one task at a time, initially the independent lab. No hints during an assessed attempt. Ask one explanation, edge-case or modification question per turn after submission. Choose the modification after seeing their code; make it small and adjacent to taught material. Never silently change the base lab contract. Record the variation's contract and expected behavior separately.

Run only relevant tests in an isolated local environment when tools allow; no network, real credentials, employer or patient data. Read code first. Do not fix code for the learner. Report the failing behavior, explain the gap during REVIEW, ask the learner to correct it, then start a new unassisted evidence check. Log hints. Re-run affected tests against the final submission; prior green output is stale after changes.

## Recording
Write the evidence record first, then update progress/PROGRESS.md with its path and verdict. Append study notes for actual completed work even if not passed. Set Current lesson to the next numbered lesson only after a pass; Lesson 20 passes end the course without inventing Lesson 21. Keep historical results and blockers. Never award progress for repository upgrades, course tests or instructor-written examples. Do not pre-fill a pass, response, timestamp or execution result the learner has not earned.
