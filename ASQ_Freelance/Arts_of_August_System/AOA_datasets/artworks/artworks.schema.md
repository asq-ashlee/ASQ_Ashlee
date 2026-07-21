# Artworks Dataset Schema

## Purpose
Portable record of Arts of August artwork metadata.

## Source
Originally exported from Notion Artwork database.

## Primary File
artworks.csv

## Fields

### Identity
- artwork_id: stable Arts of August ID. Example: AOA-ART-0001.
- Title: approved artwork title.
- Slug: URL-safe lowercase slug derived from title. Example: rose-tide.
- Alt_Text: approved alt text for web and accessibility use.
- Status: artwork lifecycle status. Values: approved / available / coming-soon / retired.
- Series: named collection or release group. Example: New Art June 2026.

### Classification
- Category: artwork category. Examples: Coastal Landscape / Seascape, Floral, Landscape / Marsh.
- Orientation: portrait / landscape / square.
- Size: original artwork size. Example: 12x12.
- Medium: paint medium. Example: Oil.
- Support: physical support. Example: Canvas.
- Source: how the record was originated. Example: Artist-provided intake details and uploaded artwork image.

### Availability and Pricing
- Original_Available: yes / no — whether the original is still available.
- Base_Price: numeric original artwork price. No currency symbol.
- Date_Created: year or date the artwork was created.

### Discovery
- Tags: semicolon-separated discovery tags.
- Mood: semicolon-separated emotional tone descriptors.
- Colors: semicolon-separated palette notes.

### Image
- Image: Google Drive URL for the master image file.
- Image_Status: image readiness stage. Values: Image Received / Editing in Progress / Edit Complete — Pending Review / Master Image Approved / Image Exported.

### Copy
- Primary_Use: intended use or merchandising direction.
- AI_Ready: yes / no — whether enough source information exists for AI to draft from.
- Description: approved artwork description.
- Story: single-line artist or atmospheric note.
- Subject: visual subject description.
- Location: public-facing place reference, if known. Use location_public from the approved record (not internal/inspiration location).
- Time_of_Day: dawn / morning / afternoon / evening / sunset / night.
- Light_Description: observed light condition in plain language.

### Workflow
- AI_Draft_Complete: yes / no — whether an AI draft has been generated.
- Human_Approved: yes / no — whether human review is complete.
- Workflow_Status: current operational stage. Examples: Metadata Complete / Ready for Products / Active.

## Notion Export Notes

The AOA_exports/Notion/ folder holds Notion database exports by date. These are not the master dataset — they are source comparison files.

Notion export columns that map to master CSV fields:
- Notion "Dimensions" → CSV "Size"
- Notion "Price (Original)" → CSV "Base_Price"
- Notion "Master File Location" → CSV "Image"
- Notion "AI Ready (enough source info exists...)" → CSV "AI_Ready"
- Notion "AI Draft Complete (AI has already generated...)" → CSV "AI_Draft_Complete"

Notion export columns that are Notion-operational only (do not copy to master CSVs):
- Next Action, Products Linked, Content Linked, Opportunities Linked, Events Linked, POC Candidate, POC Role, Needs Review, Square Checkout URL, Display Order

## Record Rules

- Each artwork must have one stable `artwork_id`.
- `artwork_id` should not depend on Notion page IDs.
- Blank Notion export rows should be removed before committing the dataset.
- Notion links may be preserved as references, but they are not primary IDs.