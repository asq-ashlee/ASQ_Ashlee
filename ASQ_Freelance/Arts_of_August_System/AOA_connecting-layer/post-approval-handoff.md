# AOA Post-Approval Handoff
# Arts of August — Connecting Layer
Last updated: 2026-09-16
Status: active

## Purpose

This workflow governs the operational handoff after the owner approves an artwork intake. The master CSVs are the portable structured-record source of truth. Firestore is the live application database. Notion exports are historical/migration evidence only and are not an ID-allocation or routine editing layer.

## Trigger

Owner approval of an intake artifact, or an explicit command to execute the post-approval handoff.

## Preconditions

- Identity is confirmed for one physical original.
- Owner-reviewed facts are distinguishable from AI suggestions and historical claims.
- Any required unresolved identity conflict is cleared.
- Image state is recorded truthfully. A missing or unapproved master image may block downstream products/publication without blocking creation of a bounded master metadata row.

## Step 1 — Resolve Stable Artwork ID

For an existing artwork, preserve its current stable ID.

For a net-new physical original, follow `../AOA_UPDATE_WORKFLOW.md` Stable ID Allocation for Net-New Records:
- allocate from the current master `AOA_datasets/artworks/artworks.csv`;
- use the next sequential unused four-digit suffix after the highest ID in that master;
- collision-check before writing;
- never source or reserve the number from Notion.

Legacy candidates require their governed identity disposition before permanent ID allocation.

## Step 2 — Finalize Approved Intake Artifact

Record the stable ID, approved title, approved/current facts, unresolved blanks, exact image status, and the owner's approval. Preserve provenance. Do not convert unknown facts into guesses.

## Step 3 — Write the Artwork Master

Update `AOA_datasets/artworks/artworks.csv` using the exact schema/header. Preserve all existing rows and IDs. For a new row:
- write only confirmed or owner-approved values;
- leave genuinely unknown fields blank;
- use semicolon separators for Tags, Mood, and Colors;
- keep `Image` blank until an exact Drive master is bound;
- record `Image_Status` truthfully;
- do not mark the artwork Ready for Products unless image/product prerequisites are actually met.

When per-artwork record mirrors are in use, create/update `AOA_datasets/artworks/artwork_records/AOA_ART_[XXXX].csv` from the same approved values. The per-artwork record and master row must agree.

## Step 4 — Validate

Before promotion, validate:
- header unchanged;
- required stable ID present;
- no duplicate IDs;
- no duplicate physical-original identity introduced;
- column count/alignment valid;
- schema vocabularies respected;
- master row and per-artwork mirror agree.

## Step 5 — Firestore Promotion

Firestore is updated only through the governed update/promotion path in `../AOA_UPDATE_WORKFLOW.md`. Dry run is the default where supported. A write requires its own authorization, rollback capture, and read-back verification. Blank relationship arrays never authorize deletion.

## Step 6 — Asset Naming and Downstream Handoff

Once an exact master image is approved and bound, rename governed assets using:
`[artwork-id]-[title-slug]-[file-type].[ext]`

Valid file-type examples: `master`, `print`, `web`. Update the master `Image` URL only after the exact Drive file exists. Product Studio, website publication, listings, mockups, and distribution remain separate workflows and are not authorized by this handoff.

## Stopping Point

Stop when the approved artwork record and its mirror are updated and validated, or at a documented prerequisite/confirmation gate. Report whether Firestore promotion was performed; do not imply it occurred if it did not.
