# Artworks Dataset Schema

## Purpose

Portable record of Arts of August artwork metadata.

This dataset exists so Arts of August artwork records can live outside any single platform while still syncing cleanly with Notion, website systems, Etsy, Printful, Kit, social content workflows, and future tools.

## Source

Originally exported from the Notion **Art Pieces** database.

## Primary File

`artworks.csv`

## Recommended Folder Location

```text
AOA_datasets/
  artworks/
    artworks.csv
    artworks.schema.md
    README.md
    records/
      AOA_ART_0001.csv
```

## Dataset Role

`artworks.csv` is the portable artwork record truth.

Notion may remain the working dashboard, but the dataset should be structured so it can be moved, versioned, reviewed, transformed, or imported into other systems later.

## Record Rules

- Each artwork must have one stable `artwork_id`.
- `artwork_id` should be created by Arts of August and should not depend on Notion page IDs.
- Use the format `AOA-ART-0001`, `AOA-ART-0002`, etc.
- Do not change an `artwork_id` once it has been assigned.
- Blank Notion export rows should be removed before committing the dataset.
- Notion links may be preserved as references, but they are not primary IDs.
- File names may use underscores, such as `AOA_ART_0001.csv`, while record IDs should use hyphens, such as `AOA-ART-0001`.
- Human review remains required before any record is treated as final.

## Fields

### artwork_id

Stable Arts of August artwork ID.

Example: `AOA-ART-0001`

Required: Yes  
Source: Arts of August  
Notes: This is the primary portable ID for the artwork.

### Title

Approved artwork title.

Required: Yes  
Source: Human approved / Artwork Lab  
Notes: Should follow the Arts of August title system when applicable.

### Status

Artwork lifecycle status.

Examples:
- intake
- draft
- interpreted
- complete
- approved
- product-ready
- published
- archived

Required: Yes  
Source: Notion / Artwork Lab

### Category

Artwork category.

Examples:
- Coastal
- Landscape
- Floral
- Abstract
- Still Life

Required: Recommended  
Source: Human / AI-assisted metadata

### Orientation

Artwork orientation.

Allowed values:
- portrait
- landscape
- square

Required: Recommended  
Source: Artwork dimensions / human review

### Size

Original artwork size.

Example: `20x16`

Required: Recommended  
Source: Artist/manual record  
Notes: Should describe the original artwork size, not every product size.

### Original Available

Whether the original artwork is still available.

Allowed values:
- Yes
- No
- N/A

Required: Recommended  
Source: Artist/manual record

### Base Price

Base price for the original artwork, if applicable.

Example: `$399.00`

Required: Optional  
Source: Artist/manual record  
Notes: Product pricing for prints may live in product datasets instead.

### Date Created

Date the artwork was created.

Example: `01/01/2016`

Required: Optional  
Source: Artist/manual record

### Tags

Discovery tags.

Required: Optional  
Source: AI-assisted + human reviewed  
Notes: Tags should remain literal and searchable. Do not use poetic language here.

### Mood

Restrained emotional tone.

Examples:
- airy
- calm
- nostalgic
- peaceful

Required: Optional  
Source: AI-assisted + human reviewed  
Notes: Should stay grounded and not overly dramatic.

### Colors

Palette notes.

Example: `coastal neutrals, soft blue, sunwashed wood, warm white`

Required: Optional  
Source: Visual analysis / human review

### Image

Image link, file path, or source reference.

Required: Recommended  
Source: Local file / Notion / website asset  
Notes: Prefer stable relative file paths when possible.

### Primary Use

Primary merchandising or workflow use.

Examples:
- living room
- print candidate
- collection anchor
- website feature
- social content

Required: Optional  
Source: Human / AI-assisted recommendation

### AI Ready

Whether the artwork is ready for AI interpretation.

Allowed values:
- Yes
- No

Required: Optional  
Source: Workflow status

### Description

Approved artwork description.

Required: Optional  
Source: Artwork Lab / human approved  
Notes: Should follow Arts of August voice rules: observational, atmospheric, grounded, and restrained.

### Story

Artist/context note.

Required: Optional  
Source: Human / Artwork Lab  
Notes: Use carefully. Arts of August should avoid over-explaining or turning every piece into a full narrative.

### Subject

Visual subject.

Examples:
- coastal path
- rowboat
- marsh
- sky
- shoreline

Required: Optional  
Source: Visual analysis / human review

### Location

Place reference, if known.

Examples:
- Maine
- coastal Maine
- Scarborough, Maine

Required: Optional  
Source: Human / artwork context

### Time of Day

Observed or implied time of day.

Examples:
- dawn
- morning
- afternoon
- evening
- dusk

Required: Optional  
Source: Visual analysis / human review

### Light Description

Observed light condition.

Example: `soft evening light over coastal neutrals`

Required: Optional  
Source: Visual analysis / human review  
Notes: This field is especially important for Arts of August because light carries much of the emotional tone.

### AI Draft Complete

Whether an AI-generated interpretation draft exists.

Allowed values:
- Yes
- No

Required: Optional  
Source: Workflow status

### Human Approved

Whether the record has been reviewed and approved by the human.

Allowed values:
- Yes
- No

Required: Recommended  
Source: Human review

### Products Linked

Related product records.

Example: `A Place to Return — Canvas 8x10`

Required: Optional  
Source: Product Studio / Notion relation  
Notes: For long-term portability, this may eventually use product IDs instead of product names.

### Content Linked

Related content records.

Example: `A Place to Return — IG Post 01`

Required: Optional  
Source: Distribution Studio / Notion relation  
Notes: For long-term portability, this may eventually use content IDs instead of content names.

### Workflow Status

Current operational stage.

Examples:
- intake
- ai-draft-complete
- awaiting-human-review
- approved
- product-mapped
- listed
- published

Required: Recommended  
Source: Workflow system

## Cleanup Rules for Notion Exports

When exporting from Notion:

1. Save the untouched export in `AOA_exports/notion/YYYY-MM-DD/raw-export/`.
2. Copy the relevant CSV into `AOA_datasets/artworks/`.
3. Rename the working copy to `artworks.csv`.
4. Remove fully blank rows.
5. Add `artwork_id` if missing.
6. Preserve useful Notion fields, but do not rely on Notion page IDs as primary identifiers.
7. Review field names for consistency before using the file in downstream workflows.

## Recommended Master CSV Columns

```text
artwork_id,
Title,
Status,
Category,
Orientation,
Size,
Original Available,
Base Price,
Date Created,
Tags,
Mood,
Colors,
Image,
Primary Use,
AI Ready,
Description,
Story,
Subject,
Location,
Time of Day,
Light Description,
AI Draft Complete,
Human Approved,
Products Linked,
Content Linked,
Workflow Status
```

## Relationship to Other Datasets

The artworks dataset may connect to:

- `products.csv`
- `listings.csv`
- `content.csv`
- `collections.csv`
- `channels.csv`

For long-term portability, related records should eventually use stable IDs rather than names alone.

Examples:
- `product_id`
- `listing_id`
- `content_id`
- `collection_id`

## Human Review Rule

AI may assist with metadata, interpretation, description drafting, tagging, and product/content suggestions.

Human review is required before:
- approving artwork metadata
- publishing descriptions
- creating product records
- syncing final records to public sales channels
