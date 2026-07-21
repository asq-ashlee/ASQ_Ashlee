# Arts of August Database Map

Last updated: 2026-07-21

## Authority Model

| Layer | Role |
|---|---|
| Markdown | Rules, schemas, workflows, and approval requirements |
| Master CSVs | Portable source of truth for structured records |
| Firestore | Live application database synchronized from approved master CSVs |
| Notion exports | Historical migration inputs; not an active source of truth |

## Master-to-Firestore Map

| Object | Master CSV | Stable ID | Firestore collection |
|---|---|---|---|
| Artwork | `AOA_datasets/artworks/artworks.csv` | `artwork_id` | `artworks` |
| Product | `AOA_datasets/products/products.csv` | `product_id` | `products` |
| Content | `AOA_datasets/content/content.csv` | `content_id` | `content` |
| Event | `AOA_datasets/events/events.csv` | `event_id` | `events` |
| Opportunity | `AOA_datasets/opportunities/opportunities.csv` | `opportunity_id` | `opportunities` |

Firestore project: `stoked-proxy-502319-c4`.

Each stable ID is also the Firestore document ID. Never replace it with an auto-generated document ID.

## Migration Baseline

As verified on 2026-07-21:

| Collection | Records |
|---|---:|
| `artworks` | 63 |
| `products` | 123 |
| `content` | 1 |
| `events` | 16 |
| `opportunities` | 14 |

These counts are a migration baseline, not a permanent schema rule.
