# CONTEXT.md — Stage 04: Macro-Story

## What this stage does

Takes macro-story candidates flagged in Stage 02 and develops them into structured argument arcs spanning multiple episodes.

This is the stage that makes AIDB's archive a living knowledge graph rather than a back catalog. It surfaces the arguments Nathan has been making over time — predictions aging, tensions resolving, positions reversing — in a form that is queryable, shareable, and brand-safe.

---

## Inputs

| Type | File | Notes |
|------|------|-------|
| Layer 4 (working) | `../02_relationship/output/[episode-name]-relationships.md` | Macro-story candidates |
| Layer 4 (working) | `../../episodes/*/insight-objects.md` | All prior episode objects |
| Layer 3 (reference) | `../../references/insight-object-schema.md` | Compatibility check fields |
| Layer 3 (reference) | `../../_config/aidb-brand-constraints.md` | Brand safety rules |

---

## Process

**Step 1 — Confirm macro-story candidates**

For each candidate flagged in Stage 02, verify it is a genuine argument arc and not just a shared topic:
- A shared topic is: "multiple episodes mention consumer AI"
- A genuine argument arc is: "Nathan's position on consumer AI monetization has developed from X to Y over time, with specific turning points at Z"

If a candidate is topic-level only, mark it as "theme cluster" not "macro-story." Theme clusters are useful for discovery but not for arc storytelling.

**Step 2 — Trace the arc**

For confirmed macro-stories, document:
- The opening position: what was the original argument (earliest object in the chain)
- The development: what happened to the argument over time (updates, confirmations, contradictions)
- The current state: where does the argument stand now
- Open questions: what is still unresolved

**Step 3 — Run full compatibility check**

For every pair of objects in the arc, verify:
- Time compatibility: claims from comparable moments in the AI landscape
- Claim type compatibility: not mixing facts and speculation without flagging it
- Confidence compatibility: not letting low-confidence objects anchor high-confidence arcs
- Speaker intent compatibility: distinguishing host framing from guest claims
- Scope boundary compatibility: the arc does not overextend any object's stated scope

Document any compatibility issues. Do not suppress them — they are part of the arc's honest representation.

**Step 4 — Write the arc summary**

One page maximum. Structure:
1. Arc title and one-sentence thesis
2. Timeline of key objects with their relationships
3. Current state of the argument
4. Open questions and unresolved tensions
5. Suggested use: how could this arc be shared, surfaced, or queried

---

## Outputs

Write to `output/[arc-name]-macro-story.md`

Format:

```markdown
# [Arc title]

**Thesis:** [One sentence stating the argument being traced]
**Episodes spanned:** [list]
**Object count:** [number]
**Arc shape:** [prediction aging / tension evolving / position reversing / confirmation building]
**Status:** [active — argument still developing / resolved / open]

---

## Timeline

| Date | Episode | Object ID | Development |
|------|---------|-----------|-------------|
| [date] | [episode] | [ID] | [what this object contributed to the arc] |

---

## Current state

[2–3 sentences: where does this argument stand right now]

---

## Open questions

[Bullet list of what is still unresolved]

---

## Compatibility notes

[Any flags from the compatibility check — do not omit these]

---

## Suggested use

[How this arc could be surfaced: query response, briefing, newsletter section, Company Champion resource]
```

---

## Quality check before closing stage

- No arc is confirmed based on topic alone — every arc has a traceable argument shape
- Compatibility issues are documented, not suppressed
- The current state section is honest about what is unresolved
- At least one suggested use is practical and specific
- The arc summary is one page or less — if it is longer, it is two arcs, not one
