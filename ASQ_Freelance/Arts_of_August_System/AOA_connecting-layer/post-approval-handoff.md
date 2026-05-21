# AOA Post-Approval Handoff
# Arts of August — Connecting Layer
Last updated: 2026-05-21
Status: active

---

## Purpose

This document defines exactly what happens after an artwork draft is approved.

It closes the gap between:
- Artwork Lab (draft approved)
- Operational Memory (record committed to dataset and Notion)

Without this document, the post-approval path is undefined and the system cannot move artwork from approved draft into live products and content.

---

## When This Document Applies

This handoff is triggered when:
- An artwork intake draft has been reviewed by the owner
- Approval Status is set to: Approved for Operational Memory
- The draft file is in `AOA_artwork-lab/aoa-ai-drafts/`

---

## Step 1 — Rename Source Files

When an artwork is approved, rename all associated files to match the approved artwork ID and title slug.

### File naming convention
`[artwork-id]-[title-slug]-[file-type].[ext]`

### File types
- `master` — original high-resolution edited file (stored in Google Drive)
- `print` — Printful-spec ready file (stored in Google Drive + uploaded to Printful)
- `web` — web-optimized version for the website (if generated separately)

### Example
Approved artwork: AOA-ART-0002, title "Light Through the Clouds"

Before approval:
- `2026-05-evening-light-master.jpg`
- `IMG_4829_print.jpg`

After approval:
- `AOA-ART-0002-light-through-the-clouds-master.jpg`
- `AOA-ART-0002-light-through-the-clouds-print.jpg`

### Where to rename
- Rename files in Google Drive
- Rename local copies in `AOA_artwork-lab/New_Art/`
- Update the `Image` field in the artwork dataset record to reflect the new Drive filename/URL

---

## Step 2 — Move the Draft File

After approval, move the AI draft file from the drafts folder to the approved folder.

From: `AOA_artwork-lab/aoa-ai-drafts/[artwork-name]-ai-draft.md`
To: `AOA_artwork-lab/aoa-approved/[artwork-id]-[title-slug]-approved.md`

Example:
- From: `aoa-ai-drafts/2026-05-evening-light-ai-draft.md`
- To: `aoa-approved/AOA-ART-0002-light-through-the-clouds-approved.md`

The original draft file should not be deleted — it is the historical record of the AI interpretation and owner corrections.

---

## Step 3 — Write the Artwork Dataset Record

Transfer approved metadata from the draft file into the artworks dataset.

File: `AOA_datasets/artworks/artwork_records/AOA_ART_[XXXX].csv`

Fields to populate from the approved draft:
- artwork_id (assign next sequential ID)
- Title (approved title only — not title suggestions)
- Status: approved
- Category
- Orientation
- Size (original canvas dimensions)
- Original Available
- Base Price (from pricing logic — 05-Product-System.txt)
- Date Created
- Tags (approved tags only)
- Mood
- Colors
- Image (Google Drive URL of renamed master file)
- Primary Use
- AI Ready: Yes
- Description (approved description)
- Story (approved story — lyrical one sentence)
- Subject
- Location
- Time of Day
- Light Description
- AI Draft Complete: Yes
- Human Approved: Yes
- Workflow Status: Ready for Products

Do not copy AI Draft content into this record. Only approved, owner-confirmed content goes into the dataset.

---

## Step 4 — Write Product Dataset Records

Using the approved artwork record, generate product records in:
`AOA_datasets/products/product_records/AOA_PRD_[XXXX].csv`

### Product record rules
- One record per product variant
- Reference 05-Product-System.txt for product type selection
- Reference 09-Printful-Pricing.txt for correct sizes and retail prices
- Use the artwork's aspect ratio to determine the correct size family
- Original painting = 1 record
- Framed canvas prints = 3 sizes × 3 frame colors = 9 records (standard landscape/portrait/square)
- Panoramic artworks = 3 unframed canvas sizes = 3 records
- Status: ready-for-review (not live until owner confirms)

### Product record ID convention
`AOA-PRD-[artwork-number]-[variant-number]`
Example: AOA-PRD-0002-001 through AOA-PRD-0002-010

---

## Step 5 — Update Google Drive Image Field

Once the master file is renamed and re-uploaded to Google Drive:
1. Get the shareable link from Google Drive
2. Update the `Image` field in the artwork dataset record CSV
3. Commit the updated record

This is the last field that may remain as a placeholder after initial record creation. Do not push to Notion until this field is populated.

---

## Step 6 — Push to Notion

Once artwork record and product records are complete and the Image field is populated:

Push the following to the three Notion databases:

**Art Pieces database:**
- One row per artwork
- All fields from the artwork dataset record
- Image field populated with Google Drive URL

**Products database:**
- One row per product record
- All fields from the product dataset records
- Link each product row to its parent artwork row in Art Pieces

**Content database:**
- Content records are created in a separate workflow (Distribution Studio)
- Do not push placeholder content records — only push approved content

### Notion push rules
- Only approved records go to Notion
- Notion is operational memory — not a draft space
- Do not push AI Draft content, TBD fields, or unconfirmed data
- If any required field is missing, resolve it before pushing

---

## Step 7 — Update Workflow Status

After Notion push is confirmed:

Update the artwork record:
- Workflow Status: `Products Ready` (if product records are complete)
- Or: `In Distribution` (if content workflow has begun)

Update the draft file in `aoa-approved/`:
- Add a final note: "Pushed to Notion [date]"

---

## Step 8 — Hand Off to Product Studio

Notify Product Studio that the artwork is ready for:
- Printful product creation (upload print file, select sizes/colors/orientation)
- Mockup generation
- Etsy listing creation
- Website entry (`artworks.ts` update)

The Product Studio receives:
- The approved artwork dataset record
- The approved product dataset records
- The print-ready file (renamed, in Google Drive)
- The `artworks.ts` entry (generated as part of the artwork record workflow)

---

## File Naming Quick Reference

| File | Convention | Example |
|---|---|---|
| Master artwork file | `[id]-[slug]-master.[ext]` | `AOA-ART-0002-light-through-the-clouds-master.jpg` |
| Print-ready file | `[id]-[slug]-print.[ext]` | `AOA-ART-0002-light-through-the-clouds-print.jpg` |
| Web-optimized file | `[id]-[slug]-web.[ext]` | `AOA-ART-0002-light-through-the-clouds-web.jpg` |
| Approved draft | `[id]-[slug]-approved.md` | `AOA-ART-0002-light-through-the-clouds-approved.md` |
| Artwork record | `AOA_ART_[XXXX].csv` | `AOA_ART_0002.csv` |
| Product record | `AOA_PRD_[XXXX].csv` | `AOA_PRD_0002.csv` |

---

## Checklist — One Artwork Through the Full Cycle

Use this checklist for every artwork from approval to Notion:

- [ ] Draft marked Approved for Operational Memory
- [ ] Source files renamed to convention
- [ ] Draft file moved from aoa-ai-drafts/ to aoa-approved/
- [ ] Artwork dataset record written and committed
- [ ] Product dataset records written and committed
- [ ] Google Drive image URL added to artwork record
- [ ] Records pushed to Notion (Art Pieces + Products)
- [ ] Workflow Status updated in artwork record
- [ ] Product Studio notified — ready for Printful + mockups + listing
