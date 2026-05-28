# AOA Website Platform Note — artsofaugust.org

Last updated: 2026-05-28
Status: active

---

## Platform

artsofaugust.org is built in Lovable (React/TypeScript).
Artwork data is sourced from `src/data/artworks.ts`.
Images are stored in `src/assets/`.

---

## Source of Truth

Notion is the source of truth for all artwork records.

The website is updated via sync-on-demand: when a sync is manually triggered, artwork data and images are pulled from Notion and committed to the Lovable project. The site does not fetch from Notion at runtime.

Artwork data must never be manually typed or AI-generated directly into `artworks.ts`. All entries must originate from an approved Notion record.

---

## Website Publishing Gate

An artwork may not appear on the website unless ALL of the following conditions are met.

### Required in the AOA artwork record

- [ ] `Image Status` = `Master Image Approved`
- [ ] `Human Approved` = `Yes`
- [ ] `Status` = `available`
- [ ] `Description` — approved, not AI draft
- [ ] `Story` — approved, not AI draft
- [ ] `Base Price` — confirmed
- [ ] `Image` field populated with a Google Drive URL pointing to a real, approved photograph

### Required before sync

- [ ] The actual artwork photograph (not AI-generated, not a placeholder) has been exported and saved to Google Drive
- [ ] The Etsy listing URL is available (or the artwork is confirmed as website-only with no Etsy link)
- [ ] The artwork dataset record has been committed to this repository

### Image rule — no exceptions

Never generate, substitute, or use an AI-generated image as a stand-in for real artwork on the website.

If a real approved photograph is not available, do not add the artwork entry to the site. Stop and wait for the image.

This rule applies regardless of whether a TypeScript entry, a Notion record, or an Etsy listing exists. An entry is incomplete without a real photograph.

---

## Sync Process

When triggered manually:

1. Query Notion Art Pieces database — filter: `Status = available`, `Human Approved = Yes`, `Image Status = Master Image Approved`
2. For each matching artwork:
   - Download the master image from the Google Drive URL in the `Image` field
   - Save to `src/assets/[artwork-id]-[title-slug]-web.[ext]`
   - Generate or update the entry in `src/data/artworks.ts`
3. Review the diff before publishing — confirm images are real photographs
4. Publish only after human review

---

## What the Website Displays

The website gallery shows:
- Artwork image (real photograph only)
- Title
- Story (one-sentence lyrical note)
- Dimensions
- Price
- Etsy listing link (if available) — "Inquire / buy →"

The website does not process transactions. Etsy handles all sales.

---

## Lovable AI Rules

These rules apply to any AI working inside the Lovable project:

1. Never generate or substitute artwork images. If an artwork entry is requested without a real photograph attached, stop and ask for the image file.
2. Never add an entry to `artworks.ts` without a corresponding image file in `src/assets/`.
3. All new artwork entries must come from a Notion sync, not from manual TypeScript edits or AI drafts.
4. Placeholder images are never acceptable.

---

## Related

- `AOA_connecting-layer/post-approval-handoff.md` — Step 8 defines when the website entry is generated
- `AOA_datasets/artworks/artworks.schema.md` — field definitions and required values
- `AOA_connecting-layer/aoa-listing-pipeline-spec.md` — listing pipeline context
