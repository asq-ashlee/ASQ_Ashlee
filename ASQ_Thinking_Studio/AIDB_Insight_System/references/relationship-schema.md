# Relationship Schema

## Core principle
A relationship object is not a tag or a link. It is a structured claim that two insight objects are in an argumentative relationship — with enough context to verify that claim before it becomes part of a macro-story arc.

---

## What a relationship object is

When two insight objects from different moments in the AIDB archive say something to each other — one updates the other, one contradicts the other, one confirms a prediction the other made — that connection is worth capturing as its own structured object.

A relationship object does three things:
1. Names the two insight objects in relationship
2. States the type of relationship and the reasoning behind it
3. Records the compatibility check so the connection can be audited before it enters a macro-story arc

---

## Required fields

| Field | Type | Description |
|-------|------|-------------|
| `relationship_id` | string | Unique ID for this connection — `REL-[EPISODE-CODE]-[N]` |
| `source_id` | string | ID of the newer or active insight object (Object A) |
| `target_id` | string | ID of the prior or related insight object (Object B) |
| `type` | enum | The logical nature of the connection — see vocabulary below |
| `reasoning` | string | One sentence explaining why these two objects are connected |
| `compatibility` | object | Results of the compatibility check — see fields below |

---

## Relationship type vocabulary

| Type | Meaning |
|------|---------|
| `agrees-with` | Two objects support the same claim independently, from different angles or times |
| `contradicts` | Two objects make opposing claims |
| `updates` | Same argument, new evidence materially changes the picture |
| `confirms` | A prediction in the target object proven correct by the source object |
| `reverses` | A position explicitly changed — source object walks back what target object claimed |
| `extends` | Builds on a claim without changing its direction |
| `qualifies` | Introduces a scope limit or condition on the target object without opposing it |

**On `agrees-with` vs `extends`:** `agrees-with` means two objects arrive at the same place independently. `extends` means one object builds directly on the other's argument. Use `agrees-with` for convergence, `extends` for continuation.

**On `qualifies`:** Use when the source object says "yes, but only under these conditions" or "yes, except in this case." It does not contradict; it narrows. A qualification is a legitimate connection but should be handled carefully in macro-story arcs — it complicates the arc rather than advancing it.

---

## Compatibility check fields

These fields map directly onto the macro-story compatibility checklist in `insight-object-schema.md`. Every field must be completed before a relationship object can enter a macro-story arc.

| Field | Type | Description |
|-------|------|-------------|
| `time_delta_days` | integer | Days between source and target episode dates |
| `claim_type_compatible` | boolean | Are the claim types logically connectable — e.g., fact-to-fact, or interpretation-to-interpretation? |
| `confidence_compatible` | boolean | Does the confidence level of each object support the weight being placed on this connection? |
| `speaker_intent_compatible` | boolean | Are the speaker relationships comparable — e.g., not connecting a host framing to a quoted source as if they carry equal authority? |
| `scope_overlap` | array of strings | The topic areas where both objects have jurisdiction |

If any boolean is `false`, flag the relationship before connecting. A flagged relationship can still be recorded — but it must not silently enter a macro-story arc.

---

## Optional macro-story fields

Activated when a relationship is promoted into a macro-story arc. Leave blank at the draft stage.

| Field | Type | Description |
|-------|------|-------------|
| `arc_id` | string | ID of the macro-story arc this relationship belongs to |
| `arc_shape` | enum | The narrative shape of the arc — see vocabulary below |
| `unresolved_tension` | string | The open question the arc has not yet answered |

**Arc shape vocabulary:**

| Shape | Meaning |
|-------|---------|
| `prediction_aging` | A prediction is being tracked across time — has it held, shifted, or broken? |
| `tension_resolving` | Two opposing objects are moving toward resolution |
| `position_reversing` | A clear reversal is taking shape across multiple objects |
| `confirmation_building` | Evidence is accumulating that a claim was correct |
| `argument_emerging` | Two objects from different episodes form an arc that neither contained alone — the connection creates meaning that didn't exist in either object |

**On `argument_emerging`:** This is the highest-value arc shape in the system. It is also the highest-risk. Use the full compatibility check and document the unresolved tension carefully before promoting an emerging arc into a macro-story.

---

## Example relationship object

```yaml
relationship_id: REL-WCCA-01
source_id: AIDB-2026-05-WCCA-02
target_id: AIDB-2026-03-EP05-04
type: qualifies
reasoning: >
  The WCCA object introduces a task-vs-discovery distinction that narrows the earlier
  prediction — agents will handle transactions but not discovery-based shopping — without
  opposing the general claim that agentic commerce is coming.
compatibility:
  time_delta_days: 42
  claim_type_compatible: true
  confidence_compatible: true
  speaker_intent_compatible: true
  scope_overlap:
    - Agentic Commerce
    - Consumer Behavior
macro_story:
  arc_id: ARC-COMMERCE-01
  arc_shape: argument_emerging
  unresolved_tension: >
    Can agents handle the discovery quest, or are they structurally limited
    to the transaction task?
```

---

## Relationship ID format

`REL-[EPISODE-CODE]-[N]`

Where `[EPISODE-CODE]` is the short code for the episode where the relationship was identified (the source object's episode), and `[N]` is a sequential number within that episode's relationship set.

Example: `REL-WCCA-01`, `REL-WCCA-02`, `REL-AGCOM-01`

---

## What this file is not

This schema defines the structure of relationship objects. It does not define:
- The insight objects being connected (see `insight-object-schema.md`)
- The macro-story arcs themselves (defined at the arc level once multiple relationships are approved)
- The compatibility checklist process (see `insight-object-schema.md` — Macro-story compatibility check)

---

*Part of the AIDB Insight System — Layer 3 reference*
*ASQ Ashlee — May 2026*
*Stable across runs. Update only when the relationship vocabulary or compatibility logic changes.*
