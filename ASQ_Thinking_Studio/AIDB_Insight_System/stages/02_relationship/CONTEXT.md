# CONTEXT.md — Stage 02: Relationship Mapping

## What this stage does

Takes the insight objects produced in Stage 01 and maps their relationships — within the episode and across the archive.

This is the stage that turns a set of isolated objects into a connected knowledge graph.

---

## Inputs

| Type | File | Notes |
|------|------|-------|
| Layer 4 (working) | `../01_decomposition/output/[episode-name]-insight-objects.md` | Objects from Stage 01 |
| Layer 3 (reference) | `../../references/insight-object-schema.md` | Extended fields specification |
| Layer 3 (reference) | `../../episodes/` | Prior episode objects for cross-episode linking |
| Layer 3 (reference) | `../../references/relationship-schema.md` | Relationship object structure, type vocabulary, and compatibility check fields |

---

## Process

**Step 1 — Populate extended fields for flagged objects**

For every object flagged in Stage 01, populate the extended fields:

- `human_time_context`: What was happening in the AI/world/company landscape when this was said
- `event_context`: Which model launch, policy change, company move, or market shift this relates to
- `speaker_relationship`: Host framing / guest claim / quoted source / personal interpretation / prediction
- `surrounding_argument`: What came before and after this moment in the original episode
- `dependency_context`: What the listener needs to know for the insight to make sense
- `scope_boundary`: Where this insight applies and where it should not be overextended
- `recombination_rules`: What kinds of other insight objects this can safely connect to

**Step 2 — Map within-episode relationships**

Review the full set of objects from this episode. Identify pairs or groups that are in argumentative relationship:

- **Agrees-with**: two objects that reinforce the same position
- **Contradicts**: two objects that are in tension with each other
- **Supports**: one object provides evidence for another
- **Qualifies**: one object limits or nuances another
- **Extends**: one object takes another's argument further

Document each relationship with one sentence explaining why the connection is valid.

**Step 3 — Check cross-episode connections**

Scan prior episode objects in the `episodes/` folder. Look for objects that share:
- The same ongoing argument (consumer vs enterprise, hype vs reality, etc.)
- The same specific claim updated by new evidence
- A prediction made in a prior episode that this episode confirms, reverses, or updates

For each valid cross-episode connection, run the compatibility check:
- Time: are these claims from comparable moments in the AI landscape?
- Claim type: are you connecting compatible claim types?
- Confidence: does the confidence level hold across both objects?
- Speaker intent: are both objects from comparable speaker roles?
- Scope boundary: does the connection overextend either object's stated scope?

Only document connections that pass all five checks.

**Step 4 — Flag macro-story candidates**

Any chain of three or more connected objects — within or across episodes — that traces an argument developing over time is a macro-story candidate. Flag it with:
- A working title for the arc
- The objects it includes
- The argument shape (what is being traced: a prediction aging, a tension resolving, a position reversing)

---

## Outputs

**Draft (per run):** `stages/02_relationship/output/[episode-name]-relationships.json`
Contains all relationship objects identified in this run, compatibility checks completed, macro-story fields blank until arc review.

**Approved archive (after review):** `episodes/[episode-name]/relationships.json`
Move from draft output after Ashlee reviews and approves connections. Once a relationship object is moved here, treat it as append-only. Do not silently edit approved files. If a connection needs revision, add a new relationship object pointing back to the original with an `updates` or `reverses` type.

---

## Quality check before closing stage

- No cross-episode connection documented without a compatibility check
- Every macro-story candidate has a clear argument shape, not just a shared topic
- Extended fields are populated for all flagged objects
- At least one within-episode relationship is documented

If the episode is the first in the archive, cross-episode section will be empty. That is fine. Document it as "archive: no prior episodes to compare."
