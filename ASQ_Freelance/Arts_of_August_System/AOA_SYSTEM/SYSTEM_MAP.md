# AOA System Map

Last updated: 2026-09-16

## Scope

This file maps the full Arts of August system architecture.

It applies to:

`ASQ_Freelance/Arts_of_August_System/`

Read alongside:

* `AOA_SYSTEM/ICM_RULES.md`
* `AOA_SYSTEM/TOOL_MAP.md`
* `AOA_SYSTEM/CHANNEL_MAP.md`
* `AOA_SYSTEM/COMMERCE_MAP.md`
* `AOA_SYSTEM/GOOGLE_WORKSPACE_OPERATING_MAP.md`
* `AOA_SYSTEM/AI_OPERATOR_COST_RULES.md`
* `AOA_SYSTEM/AOA_ARTWORK_AGENT.md`
* `AOA_connecting-layer/artwork-studio-bridge-contract.md`

---

## Architecture Principle

### Firestore Operating Model — Effective 2026-07-21

* Master CSVs in `AOA_datasets/` are the portable structured-record source of truth.
* Firestore project `stoked-proxy-502319-c4` is the live application database.
* Live collections are `artworks`, `products`, `content`, `events`, and `opportunities`.
* Every governed Firestore document ID equals its stable master CSV ID.
* Approved CSV changes reach Firestore through validated stable-ID upserts.
* Missing CSV rows never authorize automatic Firestore deletion.
* Notion and dated Notion exports are historical migration references, not active workflow dependencies.

See `../AOA_DATABASE_MAP.md`, `../AOA_UPDATE_WORKFLOW.md`, and `../AOA_RELATION_RULES.md`.

The repo is the source of truth.

Notion is not required in the publishing path. It is an optional dashboard and export layer.

Every other layer serves a specific, bounded function.

---

## System Layers

### Layer 0: Artist Interface — Artwork Studio

Artwork Studio is the artist-facing interface for governed artwork workflows.

Its job is to make the workflow understandable and pleasant for Kaleigh while keeping operational complexity behind the system boundary.

Artwork Studio may:

* collect the source photograph and factual artwork details;
* present deterministic master-image controls/review;
* show lifestyle/presentation mockups;
* show public copy and metadata for review;
* collect artist approvals;
* show friendly progress and real website previews;
* request final publication approval.

Artwork Studio must not:

* become a competing source of truth;
* store privileged GitHub/Google/Firebase/Lovable credentials in browser-side code;
* independently invent artwork metadata or publication state;
* bypass AOA governance;
* silently publish an artwork.

Its production integration is defined by `AOA_connecting-layer/artwork-studio-bridge-contract.md`.

### Layer 1: Source of Truth — Repo

The GitHub repo holds:

* system rules and ICM docs
* schema definitions
* artwork records (CSV)
* product records (CSV)
* workflow docs
* prompt templates
* approved AI drafts
* data placeholders for sales, campaigns, POD maps, and channels

No content may be considered permanent until it exists in the repo.

### Layer 2: Business Input / Asset Layer — Google Workspace

Google Workspace feeds structured business context and durable governed assets into the system.

* Gmail → opportunities and inquiries
* Google Calendar → events and deadlines
* Google Drive → source/master/presentation assets, synced repo context, print files
* Gemini → Google-native extraction and summarization

Canonical artwork masters stored in Drive must be faithful non-generative photographic derivatives of the artist's source image. Presentation/lifestyle assets remain separate derivative assets.

See: `AOA_SYSTEM/GOOGLE_WORKSPACE_OPERATING_MAP.md`

### Layer 3: Governed Orchestration — AOA Agent / Bridge

The AOA Artwork Agent and authenticated bridge translate artist-level actions into existing governed workflows.

The artist-facing seven-action contract is:

1. `startArtwork`
2. `prepareMaster`
3. `approveMaster`
4. `prepareArtwork`
5. `approveArtwork`
6. `prepareWebsite`
7. `publishArtwork`

The bridge is allowed to orchestrate routine, field-bounded backend actions quietly where the governing workflow explicitly permits delegation. Technical safeguards such as validation, Firestore dry runs, rollback capture, conditional writes, and read-back verification remain mandatory even when they are not shown in the artist UI.

The bridge is not a source of truth and must not receive broader authority than the current reviewed artwork requires.

See:

* `AOA_SYSTEM/AOA_ARTWORK_AGENT.md`
* `AOA_connecting-layer/artwork-studio-bridge-contract.md`
* `AOA_connecting-layer/post-approval-handoff.md`
* `AOA_UPDATE_WORKFLOW.md`

### Layer 4: AI Operator Layer

AI tools serve distinct roles.

* Gemini: Google-native extraction and summarization
* ChatGPT: architecture, synthesis, QA, conversation/interface orchestration
* Claude Code / Codex: repo edits, scripts, validation, and implementation

Canonical artwork-image preparation must never use generative image reconstruction/repainting. Generative tools may be used for clearly separate presentation environments only when the approved artwork itself is preserved faithfully.

See: `AOA_SYSTEM/AI_OPERATOR_COST_RULES.md`

### Layer 5: Optional Dashboard — Notion

Notion may be used to:

* view structured records in a visual database interface
* export or share records externally
* surface status views for review

Notion is not required in the publishing path.

AI tools do not need to write to Notion to complete a workflow.

Existing Notion fields and schemas are preserved. See: `AOA_SYSTEM/NOTION_OPERATING_SCHEMA.md`

### Layer 6: Live Application Data — Firestore

Firestore is the live application database, populated only through governed synchronization/promotion paths.

Artwork Studio does not write Firestore directly from browser code. A server-side governed bridge/service may invoke the approved promotion path using least-privilege authentication.

For one artwork, production promotion remains bounded, plan-driven, rollback-capable, and verified after write.

### Layer 7: Public Storefront — Lovable

Lovable is the public output layer.

* displays approved artwork and product records
* powers the customer-facing website experience
* may consume code-backed artwork adapters/assets under current implementation

Lovable should not be treated as a database or source of truth.

Website preparation may occur after `approveArtwork`, but public deployment always requires separate `publishArtwork` / explicit publication approval for the reviewed preview.

### Layer 8: Transaction Layer — Square

Square handles all commerce transactions.

* original artwork checkout links
* in-person POS
* payment processing

Square is not the product database. Square is not the content system.

See: `AOA_SYSTEM/COMMERCE_MAP.md`

### Layer 9: POD Fulfillment — Printful / Printify

Printful and Printify may both exist as active POD providers.

POD provider technical details (product IDs, variant IDs, sync status) belong in provider maps, not artwork records.

See: `data/pod/printful-map.csv` and `data/pod/printify-map.csv`

### Layer 10: Distribution Channels

* Lovable: owned storefront and customer chatbot
* Etsy: marketplace channel (preserved, optional)
* Instagram: organic social
* Facebook: social distribution
* Kit: email list

See: `AOA_SYSTEM/CHANNEL_MAP.md`

---

## System Flow Summary

```text
Artist / Kaleigh
    ↓
Artwork Studio / ChatGPT interface
    ↓
Authenticated AOA bridge / Artwork Agent
    ↓
Artwork Lab intake + deterministic master preparation
    ↓
Artist master approval
    ↓
Artwork metadata + lifestyle/presentation mockup
    ↓
Artist artwork approval
    ↓
Quiet governed handoff
    ├── Repo master + per-artwork record
    ├── Google Drive governed assets
    └── Firestore promotion + verification
    ↓
Lovable website preparation
    ↓
Real website preview
    ↓
Artist publication approval
    ↓
Lovable deploy + live verification
    ↓
Customer / Square checkout
```

Business inputs arrive from Google Workspace (Gmail, Calendar).
AI operators work in their bounded lanes.
Notion is available as an optional view layer at any stage.

---

## Human Approval Semantics

The artist should normally encounter three judgment moments:

1. **Master approval** — Does the prepared image faithfully represent the physical painting?
2. **Artwork approval** — Are the title, facts, price/availability, public copy, metadata, and presentation/lifestyle mockup acceptable?
3. **Publication approval** — Is the reviewed website preview ready to go live?

`approveArtwork` may authorize routine governed preparation needed to create the website preview when the bridge contract and invoked workflows explicitly permit delegation. This can include field-bounded repo writes, Drive asset binding, validation, and governed Firestore promotion.

`approveArtwork` does not authorize public publication.

`publishArtwork` is the separate publication gate and applies only to the reviewed website version.

Kaleigh approves: artistic representation, titles, pricing, availability, visual presentation, public copy, and publication.

Ashlee approves: system architecture, workflow design, schema changes, broad repo/system changes, and proof-of-concept scope.

Routine one-artwork mutations may be delegated to the governed bridge; schema changes, deletions, unrelated-record changes, and broader architectural changes may not.

---

## Quiet-Orchestration Principle

Governance should constrain the system, not become the artist's checklist.

After a valid artist-facing approval, successful routine backend mechanics should be handled quietly. The system may show friendly progress such as:

`Saving artwork → Securing images → Preparing website → Ready for review`

Internal details such as ID allocation, CSV validation, GitHub commits, Drive binding, Firestore confirmation tokens, rollback capture, and build mechanics remain auditable but are not normal artist-facing tasks.

Failures, unresolved facts, publication decisions, or non-delegable system-owner decisions must still be surfaced clearly. Quiet orchestration never permits silent failure or weakened safeguards.