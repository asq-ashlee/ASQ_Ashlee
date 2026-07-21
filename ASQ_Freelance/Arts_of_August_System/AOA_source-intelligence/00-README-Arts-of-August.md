# FILE 00 — README

## Purpose

This project is the source of truth for Arts of August.

It exists to:

- Preserve brand voice and expression
- Define how artwork becomes products, listings, and content
- Enable consistent AI-assisted outputs without drift

## System Definition

Create artwork → structure it → generate products → generate listings → generate content → publish → learn → repeat

## How to Use

### Structured Data Route

Brand and generation guidance lives in this source-intelligence folder. Structured operational records live in the master CSVs under `../AOA_datasets/` and are synchronized to Firestore project `stoked-proxy-502319-c4` after validation and human review. Notion is not part of the active update loop.

See `../AOA_UPDATE_WORKFLOW.md` and `../AOA_DATABASE_MAP.md`.

When generating anything:

1. Follow **Voice & Expression** rules first
2. Apply the **Title System**
3. Apply the **Listing Structure**
4. Apply **Product Logic**
5. Keep **SEO separate** (tags only)

- System rules: see `../AOA_SYSTEM/ICM_RULES.md` for Arts of August ICM rules, source-of-truth guidance, context loading rules, approval gates, and tool roles.
