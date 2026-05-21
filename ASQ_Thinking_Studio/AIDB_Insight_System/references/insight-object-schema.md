# insight-object-schema.md

A reference file for building and validating insight objects across all stages.

---

## What is an insight object

An insight object is a single argued position extracted from an episode. Not a summary. Not a highlight. Not a quote. An argued position — a claim with a source, a context, a claim type, a confidence level, and a distortion risk assessment.

The difference:
- Summary: "The episode discussed consumer AI adoption"
- Highlight: "NLW said consumer AI is clearly working"
- Insight object: "Consumer AI has proven adoption but unresolved monetization — the open question is not whether it works but whether it can generate revenue before enterprise AI locks in the economic logic of the next cycle" [interpretation, medium confidence, distortion risk: could be read as bearish on consumer AI when the claim is actually neutral on outcome but specific about timing]

---

## Minimum viable fields

Required on every insight object. No object is complete without all four.

### `source`
Episode title, date, speaker role, timestamp if available.
Format: `[Episode title] | [Date] | [Speaker role] | [Timestamp]`
Example: `Who Cares About Consumer AI | May 2026 | Host (NLW) | ~14:30`

### `claim_type`
One of: fact / interpretation / prediction / opinion / warning
- **Fact**: verifiable, sourced claim ("Robinhood reported a 47% drop in crypto trading revenue")
- **Interpretation**: reading of facts or events ("AI is being used as a convenient alibi for layoffs")
- **Prediction**: forward-looking claim ("shopping agents will struggle with discovery-based behavior")
- **Opinion**: host or guest perspective ("the highest-impact AI users treat it as a reasoning partner")
- **Warning**: flagged risk or concern ("offloading the quest to an agent may remove what makes shopping satisfying")

### `confidence`
high / medium / low + one sentence of reasoning.
- **High**: well-supported by evidence cited in the episode
- **Medium**: reasonable inference from available evidence, not directly proven
- **Low**: speculative, early-signal, or prediction-dependent

### `distortion_risk`
One sentence: how could this be misread if separated from its source?
This field is mandatory. If you cannot name a distortion risk, you have not thought carefully enough about the object.

---

## Extended fields

Activated when an object is flagged for cross-episode use or macro-story recombination.

### `human_time_context`
What was happening in the AI/world/company landscape when this was said.
Why it matters: an object about "AI replacing workers" means something different in a hot hiring market vs a recessionary one.

### `event_context`
Which specific model launch, policy change, company move, market shift, or cultural event this relates to.
Be specific. "The AI boom" is not an event context. "GPT-4o launch week" or "post-Coinbase layoff announcement" is.

### `speaker_relationship`
One of: host framing / guest claim / quoted source / personal interpretation / prediction / aggregated research
Why it matters: a host framing has different epistemic weight than a quoted source or a guest claim.

### `surrounding_argument`
What came before and after this moment in the original episode.
Keep to 2–3 sentences. The goal is to preserve the argument context, not summarize the episode.

### `dependency_context`
What the listener needs to know for the insight to make sense.
Example: "requires understanding that Robinhood and Coinbase have similar revenue structures"

### `scope_boundary`
Where this insight applies and where it should not be overextended.
Example: "applies to task-based consumer AI products; does not apply to enterprise deployments or developer tools"

### `recombination_rules`
What kinds of other insight objects this can safely connect to.
Example: "can connect to objects about AI economics, monetization timelines, or consumer behavior; should not connect to objects about AI safety or regulation without a bridge object"

### `argument_relationships`
Links to related objects with relationship type:
- agrees-with
- contradicts
- updates (same argument, new evidence)
- confirms (prediction proven right)
- reverses (position changed)
- supports (provides evidence for)
- qualifies (limits or nuances)
- extends (takes the argument further)

Format: `[Relationship type] — [Object ID] | [Episode] | [One sentence explaining the connection]`

---

## Compatibility check for cross-episode connections

Before linking two objects from different episodes, verify all five:

1. **Time**: Are these claims from comparable moments in the AI landscape? A claim from 2023 about GPT-3 connecting to a 2026 claim about Claude 4 may need a bridge object.
2. **Claim type**: Are you connecting compatible claim types? Fact-to-fact and interpretation-to-interpretation are safe. Fact-to-speculation needs flagging.
3. **Confidence**: Does the confidence level hold across both objects? A low-confidence prediction should not anchor a high-confidence arc.
4. **Speaker intent**: Are both objects from comparable speaker roles? Host framing vs guest claim vs quoted research have different epistemic weight.
5. **Scope boundary**: Does the connection overextend either object's stated scope?

Document any failures. Do not suppress them.

---

## Object ID convention

Format: `[Episode code]-[sequence number]`
Example: `WCCA01` = Who Cares About Consumer AI, object 1

Episode codes: use initials of episode title, max 4 characters.

---

## Core principle

**Portable does not mean contextless.**

An insight object that cannot travel without being misunderstood is not ready. The distortion risk field is how you test this. If you cannot name how the object could be misread, you have not finished building it.
