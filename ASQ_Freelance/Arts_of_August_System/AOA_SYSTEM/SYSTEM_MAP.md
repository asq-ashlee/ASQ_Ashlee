# AOA System Map

## Scope

This file maps the full Arts of August system architecture as of the system-layer update (2026-06).

It applies to:

`ASQ_Freelance/Arts_of_August_System/`

Read alongside:

* `AOA_SYSTEM/ICM_RULES.md`
* `AOA_SYSTEM/TOOL_MAP.md`
* `AOA_SYSTEM/CHANNEL_MAP.md`
* `AOA_SYSTEM/COMMERCE_MAP.md`
* `AOA_SYSTEM/GOOGLE_WORKSPACE_OPERATING_MAP.md`
* `AOA_SYSTEM/AI_OPERATOR_COST_RULES.md`

---

## Architecture Principle

### Firestore Operating Model — Effective 2026-07-21

This section supersedes older Notion-era architecture statements elsewhere in this file.

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

### Layer 2: Business Input — Google Workspace

Google Workspace feeds structured business context into the system.

* Gmail → opportunities and inquiries
* Google Calendar → events and deadlines
* Google Drive → master assets, synced repo context, print files
* Gemini → Google-native extraction and summarization

See: `AOA_SYSTEM/GOOGLE_WORKSPACE_OPERATING_MAP.md`

### Layer 3: AI Operator Layer

Three AI tools serve distinct roles.

* Gemini: Google-native extraction and summarization
* ChatGPT: architecture, synthesis, QA, and handoff prompts
* Claude Code / Codex: repo edits, scripts, validation, and implementation

See: `AOA_SYSTEM/AI_OPERATOR_COST_RULES.md`

### Layer 4: Optional Dashboard — Notion

Notion may be used to:

* view structured records in a visual database interface
* export or share records externally
* surface status views for review

Notion is not required in the publishing path.

AI tools do not need to write to Notion to complete a workflow.

Existing Notion fields and schemas are preserved. See: `AOA_SYSTEM/NOTION_OPERATING_SCHEMA.md`

### Layer 5: Public Storefront — Lovable

Lovable is the public output layer.

* displays approved artwork and product records
* powers the customer-facing chatbot
* chatbot reads only approved public JSON or structured data

Lovable should not be treated as a database or source of truth.

All public changes require human approval before they go live.

### Layer 6: Transaction Layer — Square

Square handles all commerce transactions.

* original artwork checkout links
* in-person POS
* payment processing

Square is not the product database. Square is not the content system.

See: `AOA_SYSTEM/COMMERCE_MAP.md`

### Layer 7: POD Fulfillment — Printful / Printify

Printful and Printify may both exist as active POD providers.

POD provider technical details (product IDs, variant IDs, sync status) belong in provider maps, not artwork records.

See: `data/pod/printful-map.csv` and `data/pod/printify-map.csv`

### Layer 8: Distribution Channels

* Lovable: owned storefront and customer chatbot
* Etsy: marketplace channel (preserved, optional)
* Instagram: organic social
* Facebook: social distribution
* Kit: email list

See: `AOA_SYSTEM/CHANNEL_MAP.md`

---

## System Flow Summary

```
Artist / Kaleigh
    ↓
Artwork Intake (artwork-lab)
    ↓
Repo (CSV record + markdown draft)
    ↓
Google Drive (master image)
    ↓
Human Approval Gate
    ↓
Lovable (public display)     Square (checkout link)
    ↓                              ↓
Customer chatbot            In-person POS / online order
                                   ↓
                          Printful / Printify (POD fulfillment)
```

Business inputs arrive from Google Workspace (Gmail, Calendar).
AI operators (Gemini, ChatGPT, Claude Code) work in their bounded lanes.
Notion is available as an optional view layer at any stage.

---

## Human Approval Gates

The following transitions always require human approval:

* artwork record → approved status
* approved record → Lovable display
* approved record → Square checkout link published
* any public-facing copy change
* any price change
* any schema change affecting existing records
* any POD product publish

Kaleigh approves: artistic representation, titles, pricing, visual presentation, publication.
Ashlee approves: system architecture, workflow design, repo changes, proof-of-concept scope.
