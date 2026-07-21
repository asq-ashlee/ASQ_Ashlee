# Claude Code Handoff — Create Approved Artwork Record

## Task

Create the approved artwork metadata record for **AOA-ART-0062 — Rose Tide** in the Arts of August artwork dataset.

This intake draft has been approved for metadata by human review. Create the artwork record only. Do not create product records, listing records, Notion pushes, or distribution assets in this step.

---

## Artwork Record ID

**Artwork ID:** `AOA-ART-0062`

---

## Source Image

**Current source image path:**  
`/mnt/data/AOA_ART_gallery-wrap_12x12_rose-tide.jpg`

Use this as the current reference image for the approved artwork record. If the repository has an established artwork image folder or naming convention, place/rename according to the current post-approval handoff rules before linking it in the record.

---

## Approved Artwork Metadata

```yaml
artwork_id: AOA-ART-0062
title: Rose Tide
slug: rose-tide
category: Coastal Landscape / Seascape
orientation: Square
dimensions: 12x12
medium:
  - Oil
support: Canvas
canvas_finish: Gallery Wrap
original_product_finish_value: Gallery Wrap (Original)
original_price: 399
currency: USD
availability: Original Available
location_internal: Scarborough, Maine
location_public: Maine coast
public_location_note: Use “Maine coast” publicly unless Kaleigh later confirms Scarborough should be named in public-facing copy.
series: New Art June 2026
date_created: 2026
source: Artist-provided intake details and uploaded artwork image
workflow_status: Metadata Complete
metadata_status: Approved
human_review_status: Approved for metadata
```

---

## Title Handling

Use the clean artwork title only in the artwork record:

```yaml
title: Rose Tide
```

Do **not** use an SEO-extended title in the artwork title field.

Do **not** change the artwork title to:
- Rose Tide in Scarborough
- Scarborough Rose Tide
- Pink Sunset Over Scarborough
- Rose Tide Maine Seascape

Those terms may be used later in listing metadata if approved, but they should not replace the artwork title.

---

## Public-Facing Location Rule

Scarborough is approved as internal inspiration/location metadata only.

For public-facing copy, use:

```yaml
public_location: Maine coast
```

Do not publish Scarborough in product descriptions, listing descriptions, alt text, or marketing copy unless Kaleigh explicitly approves it later.

---

## Approved Description

Rose light settles across the tide as the shoreline begins to darken.

This 12x12 original oil painting holds a quiet Maine coastal evening, with violet clouds, pink reflection, and low island forms stretching across the water. Dark rocks ground the foreground, giving weight to the softness of the sky above.

The piece stays close to the edge of day: open water, changing light, and the last color held briefly on the surface.

---

## Approved Story

A quiet Maine tide held in rose and violet light before the shoreline falls into shadow.

---

## Approved Alt Text

Rose Tide — original oil painting of a rose-pink and violet evening sky over calm coastal water, dark island silhouettes, and rocky shoreline on the Maine coast, on a 12x12 gallery wrap canvas by Maine artist Kaleigh Anderson.

---

## Visual / Interpretation Notes

Rose and violet light moves across the sky in loose, layered strokes, softening into lavender-blue near the horizon. Low island shapes sit in dark silhouette across the water, while the foreground is held by rocky shoreline forms in charcoal, slate, muted brown, and small warm ochre marks.

The scene is connected to Scarborough and the Maine coast through atmosphere rather than exact detail. For public-facing copy, describe it as coastal Maine unless Kaleigh later wants the Scarborough inspiration named directly.

---

## Structured Metadata Fields

```yaml
subject:
  - Coastal water
  - Island silhouettes
  - Rocky shoreline
  - Rose-pink evening sky

location:
  internal: Scarborough, Maine
  public: Maine coast
  public_location_confirmed: false

time_of_day: Evening / sunset

light_description: Rose-pink and violet evening light diffused through cloud cover and reflected across calm coastal water.

mood:
  - Quiet
  - Coastal
  - Atmospheric
  - Reflective
  - Softened
  - Still

colors:
  - Rose pink
  - Lavender
  - Violet
  - Mauve
  - Blush
  - Slate blue
  - Charcoal
  - Muted black
  - Warm ochre
  - Soft gray

tags:
  - coastal painting
  - seascape painting
  - pink sky painting
  - Maine coastal art
  - Maine coast painting
  - ocean landscape
  - island painting
  - sunset seascape
  - rocky shoreline
  - violet sky
  - original oil painting
  - square canvas
  - 12x12 painting
  - gallery wrap original
  - coastal wall art
  - evening tide
  - atmospheric landscape
  - rose pink seascape
```

Do not add Scarborough public-facing tags yet. Optional tags such as `Scarborough Maine art`, `Scarborough coastal painting`, and `Scarborough Maine seascape` should remain excluded unless public-facing Scarborough use is later approved.

---

## Original Artwork Product Notes for Future Product Studio Use

These details may be stored as artwork-level reference metadata, but do not create product records in this task.

```yaml
original_product_candidate:
  product_type: Original Painting
  medium: Oil on canvas
  dimensions: 12x12
  finish: Gallery Wrap (Original)
  availability: Original Available
  price: 399
  currency: USD
  fulfillment: Artist direct / manual shipping or local pickup
  status: Requires Product Studio handoff before product record creation
```

---

## Print Product Suggestions for Future Product Studio Review

Do not create these product records now.

```yaml
print_suggestions_unapproved:
  product_type: Framed Canvas Prints (Printful)
  ratio_family: Square
  possible_sizes:
    - 12x12
    - 16x16
  finish_value: Floating Frame (Printful)
  frame_colors:
    - White
    - Brown
    - Black
  constraint: Do not crop artwork.
  review_required: Product Studio Review
```

---

## Sales Channel Notes

```yaml
suggested_sales_channels:
  - Website
  - Etsy
  - Art Show / Market
  - Gallery
```

---

## Content Opportunity Notes

```yaml
content_opportunities:
  instagram: Short post or reel focused on the rose-pink sky, canvas texture, and contrast between soft water and dark shoreline.
  pinterest: Square-format pin using natural search language around pink coastal painting, Maine seascape, Maine coast art, and original oil painting.
  email_concept: "New from the June collection: Rose Tide"
  launch_hook: A Maine coastal evening in rose and violet light.
  seasonal_positioning:
    - New Art June 2026
    - Summer coast
    - Evening tide
    - Maine shoreline
    - Soft sunset palette
```

---

## Implementation Instructions for Claude Code

1. Locate the current artwork dataset record structure in the repository.
2. Create a new approved artwork record for `AOA-ART-0062`.
3. Use the approved metadata above exactly unless the repository schema requires field-name normalization.
4. Keep title as `Rose Tide`.
5. Set `workflow_status` to `Metadata Complete`.
6. Preserve `Scarborough, Maine` as internal location/inspiration.
7. Use `Maine coast` as the public-facing location.
8. Do not include Scarborough in public-facing description, story, alt text, listing title, or tags.
9. Store original price as numeric `399` where possible, with `USD` as currency if the schema supports it.
10. Do not create product records yet.
11. Do not create Printful records yet.
12. Do not push to Notion unless the post-approval handoff process explicitly calls for it and the user separately confirms.
13. After record creation, report the created file path and any schema normalization changes.

---

## Human Review Notes Already Resolved

- Title approved for metadata: `Rose Tide`
- Date Created: `2026`
- Dimensions: `12x12`
- Medium: `Oil`
- Finish: `Gallery Wrap`
- Original price: `$399`
- Availability: `Original Available`
- Series: `New Art June 2026`
- Public-facing Scarborough use: not approved; default to `Maine coast`

---

## Do Not Do

- Do not rename the artwork title to include Scarborough.
- Do not generate an SEO title as the artwork title.
- Do not create live listings.
- Do not create product records.
- Do not publish or schedule content.
- Do not invent a precise Scarborough landmark.
- Do not crop the artwork image.
