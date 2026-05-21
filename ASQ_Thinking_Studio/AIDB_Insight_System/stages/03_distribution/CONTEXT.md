# CONTEXT.md — Stage 03: Distribution

## What this stage does

Takes scored insight objects from Stage 01 and produces finished, channel-ready cards.

This is the stage that makes insight objects useful for real people in real channels. The card is the shareable output. The insight object is what makes the card trustworthy.

---

## Inputs

| Type | File | Notes |
|------|------|-------|
| Layer 4 (working) | `../01_decomposition/output/[episode-name]-insight-objects.md` | Scored objects |
| Layer 3 (reference) | `../../references/insight-card_template.md` | Three card format templates |
| Layer 3 (reference) | `../../_config/audience-definitions.md` | Who gets which card and why |
| Layer 3 (reference) | `../../_config/aidb-brand-constraints.md` | What cards must never do |
| Layer 3 (reference) | `../../_config/ashlee-voice_style-guide.md` | Voice and tone |

---

## Process

**Step 1 — Select objects for cards**

Not every insight object becomes a card in every run. Select the 2–3 objects with the highest combined shareability scores. Prioritize:
- Objects with high specificity (they make someone think of a specific person)
- Objects with clear channel fit (you know exactly where this lands)
- Objects with low distortion risk (they can travel safely)

**Step 2 — Match format to object**

| If the object... | Use this format |
|-----------------|----------------|
| Pushes back on a narrative or reframes a story | Reality Check |
| Surfaces an assumption worth questioning before a decision | Product Question |
| Gives language to something a team is experiencing but hasn't named | Team Prompt |

**Step 3 — Identify the recipient**

Before writing the card, name:
- Who is the sender (the AIDB listener who will forward this)
- Who is the recipient (the specific person or team who needs it)
- What channel does it land in (Slack, email, LinkedIn, team meeting)

If you cannot name a specific sender-recipient pair, the object is not ready to be a card. Go back to Step 1.

**Step 4 — Write the card**

Use the template from `insight-card_template.md`. Follow the format exactly. Do not add fields. Do not summarize the episode. One moment, one card, one channel.

Every card ends with the episode link. Always. Attribution travels with the card.

**Step 5 — Brand check**

Before finalizing, run each card against `aidb-brand-constraints.md`. A card that fails the brand check does not ship regardless of how good the insight is.

---

## Outputs

Write to `output/[episode-name]-cards.md`

Also copy finished cards to `../../episodes/[episode-name]/cards.md` so the episode folder is self-contained.

Format:

```markdown
## Card [number]: [Short title]

**Format:** [Reality Check / Product Question / Team Prompt]
**Sender:** [Who forwards this]
**Recipient:** [Who receives it]
**Channel:** [Where it lands]
**Insight object source:** [Object ID from Stage 01]

---

[Card content exactly as it would be pasted]

---

**Brand check:** [passed / failed — note reason if failed]
```

---

## Quality check before closing stage

- Every card has a named sender and recipient — not a category, a specific type of person
- Every card ends with the episode link
- No card summarizes the episode — it carries one moment
- All cards pass the brand check
- At least two different card formats are represented across the set
