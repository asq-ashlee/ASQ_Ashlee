# AOA New Artwork Intake Workflow

## Purpose

This workflow processes a newly introduced artwork into structured operational metadata for the Arts of August system.

This workflow transforms:

Artwork Image
↓
Structured Operational Intelligence

---

## Required Before Starting

This workflow requires:

* Image Status = `Master Image Approved`
* AOA Artwork Image Editing Session Notes complete
* Approved and exported image file saved in the artwork's working folder

Do not generate metadata against an unapproved or unedited source image.

If the image has not been through the editing workflow, begin there first:
`AOA_artwork-image-editing_workflow.md`

---

## Processing Path

Select exactly one governed identity path before operational promotion:

- `Net-New Physical Original Intake` — use when the owner/artist confirms a newly created distinct physical original that is not represented in the governed master and is not a legacy-gap candidate.
- `Existing Stable-ID Re-intake` — use when the physical original already has a stable artwork ID.
- `Confirmed Missing Physical Original Intake` — use for a legacy-only candidate human-confirmed as a distinct original absent from the master.
- `Unresolved Candidate Identity Review` — use when identity or relationship to an existing original remains unresolved.

A net-new intake may be drafted without a permanent ID. Permanent ID allocation happens only after owner approval through `AOA_UPDATE_WORKFLOW.md`: read the current master CSV, use the next sequential unused ID after the highest current suffix, and collision-check before writing. Notion does not allocate or reserve artwork IDs.

---

## Read First

Before processing artwork, review:

- CLAUDE.md
- asq-ashlee_context.md
- asq-freelance_context.md
- arts-of-august_context.md
- AOA_artwork-lab_context.md
- all files inside AOA_source-intelligence/

---

## Workflow Goals

Generate:
- title suggestions
- emotional interpretation
- structured metadata
- discovery tags
- product opportunities
- marketing opportunities

Outputs should align with:
- Arts of August tone
- emotional warmth
- coastal nostalgia
- human-centered storytelling
- operational consistency

---

## Required Metadata Outputs

Generate:

- Title Suggestions
  - **Title field rule:** The Title field in the Artwork database is the clean artwork title only. Example: 'What the Garden Kept' — not 'What the Garden Kept — Terracotta Pot Floral Original Oil Painting'. The long SEO/Etsy-optimized title belongs on the product or listing record. Never write the long title to the Artwork database Title field.
- Slug (URL-safe version of approved title — lowercase, hyphens, no special characters)
  - **Slug rule:** Use the approved title with hyphens between words, no punctuation, and all lowercase.
- Category
- Orientation
- Medium
- Support
- Source
- Date Created
  - **Date Created rule:** Date Created = the date Kaleigh painted the artwork. This is not the intake date, the processing date, or today's date. If the paint date is not known or not provided, leave this field blank. Do not default to the current date. Flag it as missing instead.
- Mood
- Colors
- Tags
- Description
- Story
- Alt Text (one literal sentence describing the image — for SEO and accessibility, not poetic)
- Subject
- Location (if identifiable and approved for public use)
- Time of Day
- Light Description
- Primary Use
- Series (suggest if applicable — leave blank if no clear series grouping)
- Suggested Product Types
- Suggested Sales Channels
- Suggested Content Opportunities

Physical facts such as medium, support, date, price, dimensions, availability, and public location must come from trusted evidence or owner/artist confirmation. Do not fill them from AI inference.

---

## Product Exploration

Suggest likely print formats, framing styles, home placement, customer environments, and sales channels. Product suggestions are non-authoritative until Product Studio review.

---

## Content Exploration

Suggest Instagram opportunities, Pinterest opportunities, email concepts, launch hooks, storytelling angles, and seasonal positioning.

---

## Important Constraints

Avoid generic AI phrasing, keyword stuffing, corporate language, exaggerated emotional language, and over-written poetry.

Preserve emotional grounding, familiarity, calm warmth, visual specificity, quiet nostalgia, and human tone.

---

## Human Review Required

All generated outputs require human review before operational promotion, publishing, product generation, listing creation, or content scheduling.

The intake itself does not write the master CSV or Firestore. Owner approval makes the artwork eligible for the separately governed post-approval handoff.

---

## Final Workflow Update

After metadata is complete, use a schema-supported Workflow Status such as `Metadata Complete`. Do not mark `Ready for Products` until the image and product prerequisites are actually satisfied.

---

## After Approval — Next Steps

When an artwork draft is approved, read and follow:
`AOA_connecting-layer/post-approval-handoff.md`

That handoff resolves stable ID allocation from the current master CSV, writes and validates the master/per-artwork records, and routes any separately authorized Firestore promotion. Notion is not the routine operational editing or ID-allocation path.
