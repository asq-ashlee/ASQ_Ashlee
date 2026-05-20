
# Arts of August Placement Rules

Last updated: 2026-05-20
Status: active

## Purpose

This file defines where new files, ideas, workflows, rules, datasets, drafts, and outputs should live inside the Arts of August system.

Use this file before adding new folders, moving files, or asking AI where something belongs.

---

## Core Rule

Do not create a new workspace unless the work represents a distinct mental mode.

Most new materials should become:
- a source rule
- a connecting-layer reference
- a dataset record
- a workspace artifact
- an export
- or a platform note

Not every new idea needs a new folder.

---

## Placement Decision Rules

### Whole-system context

If something applies to the entire Arts of August system, put it in:

`arts-of-august_context.md`

Use for:
- overall purpose
- business model
- workflow pipeline
- workspace routing
- system-wide human + AI relationship
- system-wide operational principles

---

### Source Intelligence

If something defines reusable truth about the brand, product system, listing system, workflow, voice, or generation rules, put it in:

`AOA_source-intelligence/`

Use for:
- brand foundation
- voice and language rules
- title system
- listing system
- product system
- workflow system
- AI generation rules

These files are stable reference material.

---

### Connecting Layer

If something explains how source truth translates into tools, platforms, schemas, channels, or data movement, put it in:

`AOA_connecting-layer/`

Use for:
- placement rules
- design rules
- schema mapping
- Notion mapping
- channel mapping
- export rules
- platform adapter rules
- decisions about how information moves between systems

These files are translation rules, not working drafts.

---

### Datasets

If something is a structured record or database mirror, put it in:

`AOA_datasets/`

Use for:
- artwork records
- product records
- listing records
- content records
- channel records
- submission/opportunity records
- schema files for datasets

Datasets should be portable and should not depend on Notion as the only source of truth.

---

### Artwork Lab

If something only applies to artwork intake, artwork interpretation, metadata, mood, visual analysis, or preparing artwork for downstream workflows, put it in:

`AOA_artwork-lab/`

Use for:
- new artwork intake
- artwork interpretation drafts
- image review notes
- metadata generation
- artwork descriptions
- artwork titles
- artwork approval notes

Artwork Lab turns artwork into structured operational memory.

---

### Product Studio

If something applies to product creation, product mapping, pricing logic, print sizes, Printful feasibility, listing readiness, or product records, put it in:

`AOA_product-studio/`

Use for:
- product drafts
- product records
- approved products
- size mapping
- aspect ratio decisions
- print product planning
- original artwork product notes
- product/listing readiness notes

Product Studio turns artwork records into sellable product structures.

---

### Distribution Studio

If something prepares approved artwork, products, or opportunities for an outside audience, put it in:

`AOA_distribution-studio/`

Use for:
- social posts
- email drafts
- website copy
- Etsy copy adaptation
- captions
- creative scripts, such as reel scripts, video scripts, launch scripts, or spoken content drafts
- launch copy
- event announcements
- gallery submissions
- marketplace applications
- feature pitches
- platform notes

Distribution Studio turns approved material into audience-facing output.

---

### Feedback Analytics

If something relates to performance, learning, audience response, sales results, channel review, or post-launch improvement, put it in:

`AOA_feedback-analytics/`

Use for:
- performance notes
- post-launch review
- sales observations
- social/email performance
- feedback summaries
- what worked / what did not
- recommendations for future cycles

Feedback Analytics turns results into system learning.

---

### Exports

If something is ready to leave the system or is a snapshot from another platform, put it in:

`AOA_exports/`

Use for:
- raw Notion exports
- channel-ready CSVs
- Etsy-ready files
- website-ready files
- Kit-ready files
- social publishing files
- archived exports by date

Exports are snapshots or delivery files, not the primary working source.

---

## Special Cases

### Platform Notes

Platform notes belong in:

`AOA_distribution-studio/platform-notes/`

Use them for channel-specific rules such as:
- Instagram caption style
- Facebook posting rules
- Kit email rules
- Etsy listing adaptation
- website content structure

Platform notes are reusable reference files, not drafts.

---

### Submissions

Show, gallery, marketplace, and feature submissions belong in:

`AOA_distribution-studio/submissions/`

Use them for:
- application requirements
- draft submissions
- submitted applications
- artist bios
- artist statements
- image checklists
- feature pitches

Submissions are audience/opportunity-facing distribution work.

---

### Creative Scripts

Creative scripts belong in:

`AOA_distribution-studio/content-drafts/video-scripts/`

or the closest relevant `content-drafts/` subfolder.

Use for:
- reel scripts
- short video scripts
- spoken launch scripts
- workshop promo scripts
- story sequence scripts

Creative scripts are audience-facing content drafts, not technical automation.

---

### Technical Scripts

Do not create an `AOA_scripts/` folder unless technical automation becomes a real repeated workflow.

Examples that might justify scripts later:
- repeated CSV cleanup
- Notion sync
- schema validation
- API export/import
- automated file conversion

Until then, do not add technical scripts.

---

## When Unsure

Ask these questions in order:

1. Does this apply to the whole Arts of August system?
   - Put it in `arts-of-august_context.md`.

2. Is this a reusable rule about brand, voice, product, listing, or workflow?
   - Put it in `AOA_source-intelligence/`.

3. Does this explain how information moves between tools, platforms, or systems?
   - Put it in `AOA_connecting-layer/`.

4. Is this a structured record or database mirror?
   - Put it in `AOA_datasets/`.

5. Is this about interpreting artwork?
   - Put it in `AOA_artwork-lab/`.

6. Is this about creating products?
   - Put it in `AOA_product-studio/`.

7. Is this about publishing, promoting, submitting, or adapting content for an audience?
   - Put it in `AOA_distribution-studio/`.

8. Is this about learning from results?
   - Put it in `AOA_feedback-analytics/`.

9. Is this ready to send out, upload, or archive as a platform snapshot?
   - Put it in `AOA_exports/`.

If none of these clearly apply, do not create a new folder immediately. Add a note to the closest existing workspace and revisit after the workflow repeats.
