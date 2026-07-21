# Arts of August Relation Rules

Last updated: 2026-07-21

## Core Rule

Relations use stable Arts of August IDs, not Notion URLs, display titles, row numbers, or Firestore auto-IDs.

## Stable ID Formats

| Object | Field | Format |
|---|---|---|
| Artwork | `artwork_id` | `AOA-ART-0001` |
| Product | `product_id` | `AOA-PRD-0001-001` |
| Legacy unlinked product | `product_id` | `AOA-PRD-LEGACY-0001` |
| Content | `content_id` | `AOA-CNT-0001` |
| Event | `event_id` | `AOA-EVT-0001` |
| Opportunity | `opportunity_id` | `AOA-OPP-0001` |

## Relationship Rules

- Product to artwork: store the parent `artwork_id`.
- Content, event, and opportunity relationships store stable IDs when known.
- Use semicolon-separated stable IDs in CSV when multiple relationships are required.
- Firestore retains the same relationship fields as the master CSV.
- A relationship may remain blank when the source does not establish it reliably.
- Never guess a relationship from similar titles alone.
- Never use a Notion page URL as the only relationship identifier.

## Legacy Product Rule

`AOA-PRD-LEGACY-*` identifies a migrated product whose source did not provide a trustworthy artwork relationship. If a human later confirms its parent artwork, add the correct `artwork_id` but keep the existing `product_id`.

## Rename Rule

Titles, names, slugs, statuses, prices, and copy may change after approval. Stable IDs never change because of a rename.
