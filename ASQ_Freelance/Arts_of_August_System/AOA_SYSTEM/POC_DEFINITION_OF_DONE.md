# AOA POC Definition of Done

## Scope

This file defines what must be true for the Arts of August proof of concept to be considered complete.

It applies to:

`ASQ_Freelance/Arts_of_August_System/`

This file should be read alongside:

* `AOA_SYSTEM/ICM_RULES.md`
* `AOA_SYSTEM/TOOL_MAP.md`

## Purpose

The proof of concept should prove that the Arts of August system can turn an artist’s body of work into structured, reusable sales and marketing infrastructure.

The proof of concept does not need to complete the entire future system.

It needs to prove the core loop.

## Core POC Claim

The Arts of August system can take a finished artwork and move it through a repeatable workflow:

```text
Artwork photo
→ structured artwork record
→ product/shop-ready output
→ approved visual assets
→ public shop or demo page
→ reusable content drafts
→ documented workflow
```

If this loop works for three artworks, the proof of concept is strong enough to show to potential artist clients.

## POC Boundary

The first POC should stay intentionally small.

The POC should include:

* 3 artworks
* 1 working artwork intake workflow
* 1 structured artwork database
* 1 simple shop or demo output layer
* 1 mockup or approved visual workflow
* 1 basic content workflow
* 1 case study or demo explanation

The POC should not wait for:

* a full opportunity agent
* full scoring loops
* a complete email marketing system
* full automation
* every Arts of August artwork
* every future service package
* perfect gallery application workflows
* advanced analytics

Those can become Phase 2.

## Definition of Done Summary

The POC is done when three real Arts of August artworks can be shown moving through the system from source photo to reusable sales and marketing outputs.

## Required Deliverables

## 1. ICM and System Governance

### Required

* `AOA_SYSTEM/ICM_RULES.md` exists.
* `AOA_SYSTEM/TOOL_MAP.md` exists.
* `AOA_SYSTEM/POC_DEFINITION_OF_DONE.md` exists.
* The nearest Arts of August README links to the system files.
* Duplicate or empty ICM-related files are cleaned up or logged as cleanup items.

### Done When

A human or AI agent can open the Arts of August system and understand:

* where rules live
* which tool does what
* what the POC is proving
* what is in scope
* what is out of scope

## 2. Photography and Master File Process

### Required

* A photography SOP exists.
* The SOP defines how Kaleigh should photograph artwork.
* The SOP defines what counts as an acceptable master photo.
* The SOP identifies where master photos and edited images should live.
* The SOP includes a basic approval/checklist step before intake.

### Done When

Kaleigh can photograph or provide 3 artworks in a way that is good enough to enter the intake workflow without re-explaining the process each time.

## 3. Artwork Intake Workflow

### Required

* The artwork intake workflow exists in markdown.
* The workflow defines required artwork inputs.
* The workflow defines optional artwork inputs.
* The workflow defines what AI may draft.
* The workflow defines what Kaleigh must approve.
* The workflow produces a structured artwork record.
* The workflow produces a missing-information checklist when inputs are incomplete.

### Done When

Three real artworks have gone through intake and each has an approved or review-ready structured record.

## 4. Notion Artwork Database

### Required

A working Notion artwork database exists with enough fields to support the POC.

Minimum useful fields:

* artwork title
* status
* medium
* dimensions
* year
* price
* availability
* short description
* long description or story
* themes or tags
* image reference
* mockup reference
* product/shop status
* content status
* approval status
* notes

### Done When

The 3 POC artworks exist as structured records and can be reused for shop copy, content drafts, and demo explanation.

## 5. Product or Shop Readiness

### Required

Each of the 3 POC artworks has enough product information to support a shop or demo page.

Minimum useful fields:

* title
* price
* size
* availability
* purchase path or placeholder
* product description
* image or mockup
* alt text
* approval status

### Done When

Each artwork can be displayed as a sellable or demo-ready item without rewriting its information from scratch.

## 6. Approved Visual Assets

### Required

Each of the 3 artworks has at least one approved visual asset for the POC.

This may be:

* a clean artwork photo
* a room mockup
* a framed mockup
* a product image
* a shop-ready image

### Done When

The shop/demo page and content examples have usable images that Kaleigh approves.

## 7. Lovable Shop or Demo Layer

### Required

A simple public or staging output exists in Lovable or another approved public layer.

It should include:

* a shop or gallery grid
* 3 artwork/product cards
* at least one artwork detail view or detail section
* image
* title
* size
* medium
* price or inquiry language
* availability
* description
* call to action
* approved purchase, inquiry, or placeholder path

### Done When

A potential artist client can see how structured artwork data becomes a public-facing sales or portfolio page.

## 8. Content Workflow

### Required

A basic content workflow exists.

It should define how the system turns an artwork record into:

* social caption draft
* email or newsletter blurb
* website copy
* event blurb or artist note if relevant

The workflow should include:

* source record
* output type
* channel
* draft status
* review status
* approval requirement

### Done When

Each of the 3 POC artworks has at least one content draft generated from the structured artwork record.

## 9. Human Approval Gates

### Required

The POC makes clear what AI can draft and what humans must approve.

Kaleigh approves:

* artwork representation
* title
* pricing
* descriptions
* visual assets
* public-facing content
* final publication

Ashlee approves:

* system structure
* workflow logic
* repo changes
* tool use
* POC scope
* client-facing case study framing

### Done When

No public-facing output is treated as final unless the correct human approval is recorded or clearly indicated.

## 10. Case Study or Demo Explanation

### Required

A short case study or demo explanation exists.

It should explain:

* the original problem
* the system built
* the core loop
* the role of AI
* the source-of-truth structure
* the three-artwork POC
* what changed before vs. after
* what could be adapted for other artists

### Done When

Ashlee can use the case study or demo explanation to talk to 1-2 potential artist clients without needing to explain the entire backend from scratch.

## 11. Client Pilot Readiness

### Required

The POC creates enough clarity to invite 1-2 additional artists into a lighter pilot.

The pilot offer should be explainable as:

* organize your artwork
* structure your inventory
* create reusable sales and marketing assets
* build or improve your shop/output layer
* create content from your existing body of work
* prepare for events or opportunities

### Done When

Ashlee can confidently say:

“I built this system with Arts of August. I’m testing a lighter version with 1-2 other artists.”

## Acceptance Criteria

The POC is complete when all of the following are true:

* 3 artworks have gone through the system.
* Each artwork has a structured record.
* Each artwork has approved or review-ready visual assets.
* Each artwork has shop or demo-ready copy.
* Each artwork has at least one reusable content draft.
* A shop or demo page exists.
* Source-of-truth rules are documented.
* Tool roles are documented.
* Human approval gates are documented.
* The process is repeatable.
* The case study or demo explanation is ready enough to support outreach.

## Out of Scope for First POC

The following are valuable but not required before the first POC is considered done:

* full automation
* full Notion dashboard polish
* complete artist CRM
* full opportunity agent
* automated publishing
* advanced performance scoring
* full email marketing setup
* complete Square automation
* every artwork in the Arts of August inventory
* every event workflow
* every future artist service package
* perfect design polish

## Phase 2 Candidates

After the first POC is complete, consider:

* opportunity agent
* gallery application workflow
* event marketing workflow
* content scoring loop
* email list growth workflow
* artist dashboard
* second artist pilot
* third artist pilot
* client-facing service package
* pricing model
* ASQ Ashlee case study page

## Final POC Standard

The POC is not done when the system feels theoretically complete.

The POC is done when a real artist, using three real artworks, can show a repeatable path from creative work to structured business output.

The first goal is proof.

The second goal is polish.

The third goal is scale.