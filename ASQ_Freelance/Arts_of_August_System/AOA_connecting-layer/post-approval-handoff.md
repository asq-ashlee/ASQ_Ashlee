# AOA Post-Approval Handoff
# Arts of August — Connecting Layer
Last updated: 2026-09-16
Status: active

## Purpose

This workflow governs the operational handoff after the owner approves an artwork intake. The master CSVs are the portable structured-record source of truth. Firestore is the live application database. Notion exports are historical/migration evidence only and are not an ID-allocation or routine editing layer.

For artist-facing Artwork Studio flows, read alongside `artwork-studio-bridge-contract.md`. The bridge may perform the routine steps below quietly after a valid `approveArtwork` action, while retaining every validation and safety requirement in this workflow.

## Trigger

One of:

- an explicit command to execute the post-approval handoff; or
- a valid artist-facing `approveArtwork` / `prepareWebsite` invocation through the governed Artwork Studio bridge, as defined in `artwork-studio-bridge-contract.md` and `../AOA_UPDATE_WORKFLOW.md`.

A generic approval outside an applicable governed context does not authorize mutation.

## Preconditions

- Identity is confirmed for one physical original.
- The canonical master has been prepared non-generatively and approved when required for website preparation.
- Owner-reviewed facts are distinguishable from AI suggestions and historical claims.
- Any required unresolved identity conflict is cleared.
- Image state is recorded truthfully.
- The reviewed artwork package and the authorization context are bound to the same artwork.

A missing or unapproved master image may block downstream products/publication without blocking creation of a bounded master metadata row, unless the invoking bridge action specifically promises website preparation.

## Step 1 — Resolve Stable Artwork ID

For an existing artwork, preserve its current stable ID.

For a net-new physical original, follow `../AOA_UPDATE_WORKFLOW.md` Stable ID Allocation for Net-New Records:
- allocate from the current master `AOA_datasets/artworks/artworks.csv`;
- use the next sequential unused four-digit suffix after the highest ID in that master;
- collision-check before writing;
- never source or reserve the number from Notion.

Legacy candidates require their governed identity disposition before permanent ID allocation.

## Step 2 — Finalize Approved Intake Artifact

Record the stable ID, approved title, approved/current facts, unresolved blanks, exact image status, structured Artwork Lab outputs, exact approved asset references, and the owner's approval. Preserve provenance and evidence classes. Do not convert unknown facts into guesses.

## Step 3 — Write the Artwork Master

Update `AOA_datasets/artworks/artworks.csv` using the exact schema/header. Preserve all existing rows and IDs. For a new row:
- write only confirmed or owner-approved values plus permitted AI interpretation fields;
- leave genuinely unknown fields blank;
- use semicolon separators for Tags, Mood, and Colors;
- keep `Image` blank until an exact governed Drive master is bound;
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
- master row and per-artwork mirror agree;
- exact reviewed values remain unchanged;
- canonical-master and mockup references remain correctly distinguished.

## Step 5 — Governed Asset Binding

Once an exact master image is approved, rename/store governed assets using:

`[artwork-id]-[title-slug]-[file-type].[ext]`

Valid file-type examples include `master`, `mockup`, `lifestyle`, `print`, and `web` where applicable.

The canonical master must be a faithful non-generative derivative of the artist's source photograph. Never bind an AI-regenerated/repainted image as the canonical master.

Update the master `Image` URL only after the exact governed Drive master exists. Keep presentation/lifestyle assets separate from the canonical `Image` field unless a future schema explicitly adds governed derivative fields.

## Step 6 — Firestore Promotion

Firestore is updated only through the governed update/promotion path in `../AOA_UPDATE_WORKFLOW.md`.

Dry run remains the default where supported. A write requires artwork-specific authorization, rollback capture, conditional-write safeguards where implemented, and read-back verification. Blank relationship arrays never authorize deletion.

For an Artwork Studio invocation, the bridge may translate the valid artist-level authorization into the promoter's technical confirmation mechanism only under the explicit delegation rules in `../AOA_UPDATE_WORKFLOW.md` and `artwork-studio-bridge-contract.md`.

The artist should not be asked to type or understand the internal confirmation token when that delegated path is valid.

## Step 7 — Website Preparation Handoff

When invoked through `prepareWebsite`, continue into the website adapter only after the governed record/assets required by the current website implementation are ready and verified.

The handoff must use:
- exact approved facts;
- exact approved canonical master;
- exact approved lifestyle/presentation asset state;
- confirmed price/availability;
- confirmed checkout link where required;
- complete approved description/story/alt/discovery metadata required by the website adapter.

Lovable is the public display layer, not source of truth.

The bridge may implement/build the website preview quietly, but it must stop before public deployment.

## Quiet-Orchestration Rule

For successful artist-facing runs, do not turn ID allocation, GitHub commits, Drive binding, CSV validation, Firestore confirmation tokens, rollback capture, or website build mechanics into separate artist checklist items.

These details remain auditable in administrative logs/reports. Surface them to the artist only when a decision or failure genuinely requires human action.

Never hide a failed check, substitute a different asset/URL, or simulate completion.

## Stopping Point

For a record-only handoff, stop when the approved artwork record and mirror are updated and validated, with Firestore state truthfully reported.

For a governed Artwork Studio `prepareWebsite` run, continue through routine asset/record/Firestore handoff and website implementation, then stop at a real website preview.

Public publication always remains a separate `publishArtwork` action / explicit publication approval.