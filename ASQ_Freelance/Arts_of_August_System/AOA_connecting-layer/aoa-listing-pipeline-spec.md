# AOA Listing Pipeline — Machine-Ready Spec
# Arts of August | Notion → Printful → Etsy

Last updated: 2026-05-23
Status: active

---

## Overview

This spec defines the end-to-end process for publishing a Printful print listing from a Notion-approved art piece to a live Etsy listing.

Pipeline shape: **automated → HUMAN → automated**

Three stages cannot be automated and require human execution:
- Visual design adjustment per variant in Printful's canvas editor
- Mockup selection (taste + rules)
- Final Etsy publish confirmation

Everything else is data-driven and automatable via Printful API + Etsy API.

---

## Trigger Condition

**Source:** Notion Art Pieces dataset
**Filter:** `Status = approved`
**Scope:** Only process `Product Type = Printful Print` product records linked to the approved art piece

---

## Phase 1 — Read and Group Variants

### Input
Notion Products dataset, filtered to:
- `artwork_id` matching the approved art piece
- `Product Type = Printful Print`
- `Status = ready-for-review`

### Grouping Rule
Group product records by:
```
artwork_id + Format + Printful Product
```

Each group = **one Printful listing**.

Within each group, collect:
- All unique `Size` values → listing size variants
- All unique `Frame Color` values → listing frame color variants
- `Price` per unique `Size` (all frame colors of the same size share the same price)
- `Orientation` (consistent within group — validate; error if mixed)
- `Printful Product` value → maps to Printful catalog category

### Output per Group
```
{
  artwork_id: string,
  title: string,                    // from Art Pieces > Title
  orientation: horizontal|vertical|square,
  printful_product: string,         // e.g. "Framed Canvas (in)"
  sizes: [string],                  // e.g. ["8×10", "16×20", "24×32"]
  frame_colors: [string],           // e.g. ["White", "Brown", "Black"]
  price_by_size: { size: price },   // e.g. { "8×10": 95, "16×20": 180, "24×32": 230 }
  image_url: string,                // Google Drive link from Art Pieces > Image field
  description: string,              // Art Pieces > Description
  story: string,                    // Art Pieces > Story
  subject: string,                  // Art Pieces > Subject
  location: string,                 // Art Pieces > Location
  light_description: string,        // Art Pieces > Light Description
  tags: [string]                    // Art Pieces > Tags (max 13)
}
```

---

## Phase 2 — Printful Product Creation (API)

### Printful Catalog Navigation
| Printful Product value | Catalog path |
|---|---|
| Framed Canvas (in) | Home & Living > Wall Art > Canvas Prints > Framed Canvas (in) |
| Canvas (in) | Home & Living > Wall Art > Canvas Prints > Canvas (in) |
| Thin Canvas (in) | Home & Living > Wall Art > Canvas Prints > Thin Canvas (in) |

### Product Setup
- Select orientation from group data
- Select all size variants from group data
- Select all frame color variants from group data
- No other product selections required before clicking Start Designing

### Print File
1. Download image from `image_url` (Google Drive)
2. Upload to Printful via Files API or manual upload
3. Apply image to product

---

## Phase 3 — HUMAN CHECKPOINT: Visual Design

**Location:** Printful canvas designer (Uploads → Layers tabs)

**Steps per size variant:**
1. Verify correct file is selected in Layers tab
2. Verify print quality shows Good / 300+ DPI
3. Adjust image position so:
   - No opaque diagonal grey stripe in the center print area
   - No white space visible in the center print area
   - Image extends slightly outside the printed area (into bleed) but not fully filling the bleed
   - Minimize cropping while allowing for physical printing shift
4. Printful auto-adjusts same-size variants with different frame colors — only adjust per size, not per color

**Mockup Selection Rules**

After adjusting all size variants, click Publish → Mockups tab.

Settings:
- Format: JPG
- Mode: Basic (auto-generated)

| Mockup Style | Selection Rule | Quantity |
|---|---|---|
| Flat | Largest size, dark frame color (brown or black); this becomes main listing image (teal star) | 1 |
| Lifestyle (hand holding) | One per size, random frame color per | 3 |
| Product Details (corner closeup) | One per frame color | 3 (one per color) |
| Lifestyle 2 | Largest size, random frame color | 1 |
| Lifestyle 3 | Largest size, random frame color | 1 |
| Lifestyle 4 | Largest size, random frame color | 1 |
| Lifestyle 5 | Largest size, random frame color | 1 |

Target: ~12 of 20 mockup slots used.
Main listing mockup: Flat, largest size, dark frame color.

Click Continue when done.

---

## Phase 4 — Pricing (API or Manual)

**Tab:** Set Pricing

| Setting | Value |
|---|---|
| Mode | By variant (not general) |
| Include shipping in calculation | ON |
| Destination | USA |

**Price assignment rule:**
- All frame color variants of the same size → same price
- Price sourced from `price_by_size` map built in Phase 1

**Validation:** Every variant must have a price set. No variant left at default.

---

## Phase 5 — Product Details (API or Manual)

**Tab:** Product Details

| Field | Source | Rule |
|---|---|---|
| Product Title | Art Pieces > Title | Use as-is |
| Description | Assembled from Art Pieces fields | See assembly rule below |
| Benefits of on-demand manufacturing | — | Uncheck |
| EU GPSR Compliance | — | Uncheck (no international shipping) |
| Size guide | — | Uncheck |
| Tags | Art Pieces > Tags | Comma-separated, max 13 |
| Product Category | — | Canvas Prints |

**Description Assembly Order:**
```
[description]

[story]

Subject: [subject]
Location: [location]
Light: [light_description]

[Printful-generated specs and disclaimers — keep, do not remove]
```

Remove Printful's standard opening sentences above the specs block. Keep everything from specs onward.

Click Publish.

---

## Phase 6 — HUMAN CHECKPOINT: Etsy Draft Review

After Printful publishes, the product auto-syncs to Etsy as a draft.

**Navigation path:**
Printful My Products → new product → Edit in Etsy → Edit in Etsy (second link on product overview page) → opens Etsy listing admin

**Etsy Tab Checklist**

| Tab | Action |
|---|---|
| Photo & Video | Leave as-is |
| Category | Leave as-is (Digital Prints / Physical Item / Made to order) |
| Item Details | Leave as-is (set in Printful) |
| Item Options | See rules below |
| Personalization | Leave unchecked |
| Price & Inventory | See rules below |
| How It's Made | See rules below |
| Settings | See rules below |

**Item Options rules:**
- SKU: never edit (Printful connector)
- Price: never edit here (edit in Printful only)
- Quantity: change from 999 → randomly 15 or 20
- Visible: all variants ON

**Price & Inventory rules:**
- Allow restock requests: toggle ON
- All other fields: leave as-is (controlled by Printful)

**How It's Made rules:**
- Who made it: I did
- What is it: A finished product
- How does your shop produce this item: skip
- What tools are used: skip (for reprints)
- Production partners: none for now

**Settings rules:**
| Setting | Value |
|---|---|
| Featured Listing | ON (newest product always featured) |
| Etsy Ads | ON |
| Renewal | Change Manual → Automatic |
| Shop Section | Leave as-is (set in Printful) |

Click Publish with Changes.

---

## Field Mapping Reference

| Notion Field | Notion Dataset | Maps To | Stage |
|---|---|---|---|
| Status | Art Pieces | Trigger condition | Phase 1 |
| Title | Art Pieces | Printful product title | Phase 5 |
| Image | Art Pieces | Print file upload | Phase 2 |
| Description | Art Pieces | Description block | Phase 5 |
| Story | Art Pieces | Description block | Phase 5 |
| Subject | Art Pieces | Description block | Phase 5 |
| Location | Art Pieces | Description block | Phase 5 |
| Light Description | Art Pieces | Description block | Phase 5 |
| Tags | Art Pieces | Etsy tags | Phase 5 |
| Orientation | Products | Printful orientation setting | Phase 2 |
| Printful Product | Products | Printful catalog selection | Phase 2 |
| Size | Products | Variant size selection | Phase 2 |
| Frame Color | Products | Variant frame color selection | Phase 2 |
| Price | Products | Variant pricing (by size) | Phase 4 |
| Shipping Model | Products | Validates free shipping applies | Phase 4 |

---

## Automation Boundary Summary

| Phase | Executable By | Blocker |
|---|---|---|
| Phase 1 — Read + Group | Script / Agent | None |
| Phase 2 — Product Creation | Printful API | None |
| Phase 3 — Visual Design | Human | Printful designer is browser-only; no API |
| Phase 3 — Mockup Selection | Human | Taste + rules; no mockup config API |
| Phase 4 — Pricing | Printful API | None |
| Phase 5 — Product Details | Printful API | None |
| Phase 6 — Etsy Draft Edits | Etsy API + Human | Quantity randomization = human judgment; final publish = human approval |

---

## Validation Rules

- `Orientation` must be consistent across all records in a group — raise error if mixed
- `Tags` count must not exceed 13 — truncate or flag if over
- Print file DPI must be 300+ — Printful flags this in the designer; human must verify
- SKU field in Etsy must never be edited — document warning in any automation output
- Price field in Etsy must never be edited directly — always edit in Printful
- International shipping fields (GPSR, EU compliance) are always unchecked — no international shipping offered
