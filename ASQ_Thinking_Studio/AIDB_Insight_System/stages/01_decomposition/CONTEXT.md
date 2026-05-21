# CONTEXT.md — Stage 01: Episode Decomposition

## What this stage does

Takes a raw episode transcript and produces a set of structured insight objects.

One episode → 5–10 insight objects.

Each insight object is a single argued position extracted from the episode — a claim with a source, a context, a claim type, a confidence level, and a distortion risk assessment. Not a summary. Not a highlight. An argued position that can travel without losing its meaning.

---

## Inputs

| Type | File | Notes |
|------|------|-------|
| Layer 4 (working) | `../../episodes/[episode-name]/transcript.md` | Raw transcript or structured notes |
| Layer 3 (reference) | `../../references/shareability-rubric_framework.md` | Scoring criteria |
| Layer 3 (reference) | `../../references/insight-object-schema.md` | Required fields for each object |
| Layer 3 (reference) | `../../_config/aidb-brand-constraints.md` | What the system must never do |

---

## Process

**Step 1 — Read the full episode**
Do not extract moments while reading. Read for the overall argument, the tensions, the turns. Identify what the episode is actually claiming, not just what it discusses.

**Step 2 — Identify candidate moments**
Find 8–12 moments that could become insight objects. A moment qualifies if it:
- Makes a specific argued position (not just a topic mention)
- Could make someone think of a specific person or situation
- Reframes something the audience already has an opinion about
- Could travel to a Slack channel, email thread, or team discussion and land usefully

**Step 3 — Score each candidate**
Run each moment through the shareability rubric:
- Specificity
- Novelty
- Actionability
- Trust density
- Channel fit

Drop any moment that fails two or more criteria.

**Step 4 — Build insight objects**
For each passing moment, populate the minimum viable fields:
- `source`: episode title, date, speaker, timestamp if available
- `claim_type`: fact / interpretation / prediction / opinion / warning
- `confidence`: high / medium / low + one sentence of reasoning
- `distortion_risk`: one sentence — how could this be misread if separated from source

**Step 5 — Flag for extended fields**
Review the full set of objects. Flag any object that:
- References a specific model, tool, or AI capability
- Makes a prediction about the future
- Contradicts a common assumption
- Could connect to objects from other episodes

Flagged objects get extended fields populated in Stage 02.

---

## Outputs

Write to `output/[episode-name]-insight-objects.md`

Format each object as:

```markdown
## [Object ID] — [Short title]

**Claim:** [One sentence stating the argued position]

**Source:** [Episode title] | [Date] | [Speaker role] | [Timestamp if available]
**Claim type:** [fact / interpretation / prediction / opinion / warning]
**Confidence:** [high / medium / low] — [one sentence of reasoning]
**Distortion risk:** [one sentence]

**Shareability scores:**
- Specificity: [high/medium/low]
- Novelty: [high/medium/low]
- Actionability: [high/medium/low]
- Trust density: [high/medium/low]
- Channel fit: [Slack / email / LinkedIn / team meeting]

**Extended fields needed:** [yes/no] — [reason if yes]
```

---

## Quality check before closing stage

- Every object has a one-sentence claim statement
- No object has a distortion risk left blank
- At least one object is flagged for extended fields
- No object is a summary of the episode — each one is a specific argued position
- The set as a whole covers more than one audience type

If any of these fail, revise before moving to Stage 02.
