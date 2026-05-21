# Arts of August — Artwork Lab Readiness Review

Last updated: 2026-05-21
Status: active — pending human review

---

## Purpose

This document reviews the current readiness of the Arts of August Artwork Lab to continue processing new artwork and supporting downstream product, listing, and content workflows.

It is based on a full review of:
- arts-of-august_context.md
- AOA_artwork-lab_context.md
- AOA-new-artwork-intake_workflow.md
- AOA-artwork-intake-template.md
- all files inside AOA_source-intelligence/
- existing AI drafts in AOA_artwork-lab/aoa-ai-drafts/
- AOA_connecting-layer/placement-rules.md
- AOA_datasets/artworks/artworks.schema.md

---

## 1. What Is Already Working Well

**Workflow documentation is solid.**
The intake workflow (`AOA-new-artwork-intake_workflow.md`) is clearly written, well-scoped, and operationally grounded. It defines what to read, what to generate, and what constraints apply. A new session can follow it without additional explanation.

**Source intelligence files are comprehensive.**
All eight source-intelligence files are present, internally consistent, and together give AI enough brand, voice, product, listing, and generation guidance to produce usable drafts without significant drift.

**The two existing AI drafts are high quality.**
Both `2026-05-evening-light-ai-draft.md` and `2026-05-pink-twilight-ai-draft.md` follow the template structure correctly. They preserve the Arts of August tone. They do not use generic AI filler language or over-written poetry. They correctly label emotional positioning as suggestions and flag operational notes for each downstream team (Product, Listing, Content).

**The intake template enforces human review structurally.**
The template includes an explicit Workflow Status field ("AI Draft — Pending Human Review"), a Human Review Notes section, and a three-state Approval Status (Pending / Approved / Needs Revision). The structure makes it hard to accidentally skip the review step.

**Placement rules are clear and decision-tree formatted.**
`placement-rules.md` covers every workspace, every edge case, and provides a sequential decision process when placement is uncertain. It is ready for use now.

**The dataset schema is well-defined.**
`artworks.schema.md` defines every field, its source of truth, and its human-review requirements. It correctly identifies which fields belong to Printful, which belong to artist records, and which are AI-assisted.

---

## 2. Whether the Artwork Intake Workflow Is Clearly Documented

**Yes, with one gap.**

The workflow is clearly documented for the intake stage. It defines what context files to read, what outputs to generate, what constraints apply, and what the human review trigger is.

**Gap:** The workflow does not document what happens after a draft is approved. It ends with "Set Artwork Workflow Status: Ready for Products" but does not describe:
- Where the approved file goes (does it stay in `aoa-ai-drafts/`? Move? Get renamed?)
- How approved metadata moves into `AOA_datasets/artworks/`
- How product-studio receives the handoff

This post-approval path needs to be documented before drafts can be safely moved into operational memory.

---

## 3. Whether the Human Review Step Is Clear Enough

**Partially clear.**

The intake workflow states: "All generated outputs require human review before publishing, product generation, listing creation, and content scheduling." The template enforces this with the Approval Status field.

**What is not yet clear:**
- Who conducts the review (owner, consultant, or both)
- What "approved" specifically means — does the owner correct fields in the draft file? Write new notes? Create a separate approved record?
- What happens if a field like a title is partially approved but a description needs revision — the three-state status does not cover partial approval

**Recommendation:** Before the next artwork batch, define a short human-review protocol. It does not need to be elaborate — one paragraph clarifying what the reviewer marks, corrects, and signs off on would be enough.

---

## 4. Whether AI Draft Files Are Stored in the Right Place

**Mostly yes, with a folder naming inconsistency.**

The two existing drafts are stored in:
`AOA_artwork-lab/aoa-ai-drafts/`

The intake workflow (as described in context) references:
`AOA_AI-Drafts/[artwork-name]-ai-draft.md`

These point to the same folder but use different capitalization and formatting conventions. This inconsistency will cause confusion when onboarding a new AI session or collaborator. One naming convention should be chosen and used consistently across the workflow, template, and context files.

The placement rules do not explicitly call out the AI-drafts subfolder — they describe `AOA_artwork-lab/` broadly. The subfolder is implied but not named. Consider adding it.

---

## 5. Gaps Before Continuing With More New Artwork

**Gap 1: Two context files referenced in the workflow do not appear to exist in this workspace.**

The intake workflow's "Read First" section lists:
- `asq-ashlee_context.md`
- `asq-freelance_context.md`

Neither file was found in the Arts of August system folder. **Decision (2026-05-21):** These context files should be marked as optional in the intake workflow unless a session is operating from the full ASQ Ashlee parent repository where those files are present. When working within the Arts of August system folder alone, `arts-of-august_context.md` and the source-intelligence files provide sufficient brand and operational context for intake work.

**Gap 2: Three images in `AOA_artwork-lab/New_Art/` have no AI drafts.**

The following files have no corresponding draft:
- `IMG_4829.png`
- `IMG_4829_print.jpg`
- `IMG_1385.JPG`

**Decision (2026-05-21):** These are to be treated as unreviewed image assets. They should not be processed through the intake workflow unless explicitly included in a future artwork intake prompt. Do not assume they are ready for intake.

**Gap 3: No master `artworks.csv` exists.**

The schema defines `artworks.csv` as the portable artwork record truth. The folder currently contains two individual record files (`AOA_ART_0001.csv` and `AOA_Art_0002.csv.csv` — note the doubled `.csv` extension on the second file) but no consolidated master file. The two approved AI drafts have not been translated into dataset records yet.

**Gap 4: Nested dataset folder.**

There is a duplicated directory: `AOA_datasets/AOA_datasets/`. This is likely an export or copy artifact. It should be reviewed and resolved before the dataset grows further.

**Gap 5: Post-approval handoff.**

**Decision (2026-05-21):** After owner approval, the reviewed artwork draft becomes an approved artwork record. Key metadata is transferred into the master artwork dataset. Product-related opportunities are handed off to AOA_product-studio, while content/storytelling opportunities may be handed off to AOA_distribution-studio. The original AI draft remains stored as a draft artifact and should not be treated as source truth.

---

## 6. Risks of AI Inventing Operational Details

**Risk 1: Specific print dimensions in the drafts — medium risk.**

Both drafts include a Sizing Strategy with specific dimensions:
- S: 12x20 / 16x27
- M: 16x27 / 20x30
- L: 24x40 / 28x42
- XL: 32x54 / 36x60

**Decision (2026-05-21):** All canvas dimensions in existing AI drafts are to be treated as unverified product suggestions, not approved product specifications. They should not be used for product creation until confirmed against Printful's actual canvas size catalog. These dimensions appear to be AI-derived from the 16:9 aspect ratio and do not reflect confirmed Printful offerings. The intake rules correctly state that Printful is the source of truth for POD specifications — these draft dimensions do not meet that standard.

**Risk 2: Third-party platform references — low risk.**

Both drafts suggest sales channels including Saatchi Art and Artsy. These are directional suggestions, not operational facts, and are clearly framed as options rather than confirmed integrations. The listing system rules allow AI to suggest channels. No correction needed, but the human reviewer should treat these as starting points.

**Risk 3: Fulfillment method names — low risk.**

Both drafts reference "Giclée art print service" and "metal print partner" without naming specific vendors. These are appropriate as exploratory suggestions, not operational commitments. The product system allows AI to suggest fulfillment methods while prohibiting fabricated vendor details.

**Risk 4: "In-house framing (if applicable)" — low risk.**

This phrase appears in both drafts. It is hedged with "if applicable" and does not invent a capability. It should remain flagged for human confirmation rather than being treated as an established workflow.

---

## 7. Recommendations Before Moving Drafts Into Operational Memory

1. **Resolve the print dimensions first.** Before the evening-light or pink-twilight drafts move to product-studio, verify the sizing strategy against Printful's actual canvas sizes and replace the AI-generated dimensions with confirmed Printful options. This is the highest operational risk in the current drafts.

2. **Define the post-approval handoff.** Write a short note (in the workflow file or as a separate handoff document) describing what happens after a draft is marked Approved. At minimum: where does the approved draft live, and how does its metadata reach the artworks dataset?

3. **Reconcile the folder naming.** Choose one consistent name for the AI drafts folder and update all references. Lowercase `aoa-ai-drafts/` is what currently exists; use that.

4. **Update the Read First section of the workflow.** Remove or replace `asq-ashlee_context.md` and `asq-freelance_context.md` references if those files do not exist.

5. **Confirm which New_Art images are intake queue.** Clarify the status of `IMG_4829.png`, `IMG_4829_print.jpg`, and `IMG_1385.JPG` before running them through intake.

6. **Do not create dataset records yet.** The artworks dataset is not consolidated. Wait until the master `artworks.csv` is established and the two existing drafts are approved before adding records.

---

## 8. Next Best Claude Code Task After This Review

**Recommended next task: Human review of the two existing AI drafts.**

The most important next action is for the owner (Kaleigh) to review `2026-05-evening-light-ai-draft.md` and `2026-05-pink-twilight-ai-draft.md`, fill in the Human Review Notes section, and update the Approval Status for each.

After that review is complete, the recommended Claude Code task is:

> **Document the post-approval handoff.**
> Based on the owner's corrections and decisions from the human review session, write a short Post-Approval Handoff note (either in the intake workflow or as a new placement-rules entry) that defines what happens after a draft is approved — where files go, how metadata enters the artworks dataset, and how product-studio receives the handoff.

This closes the biggest structural gap and makes the system ready to process artwork at volume without ambiguity about where things land after review.

---

## Summary

The Arts of August Artwork Lab is operationally ready to continue processing new artwork at the intake stage. The workflow, template, and source intelligence files are solid. The two existing AI drafts are high quality and appropriately framed for human review.

The system is **not yet ready** to move approved drafts into full operational memory because the post-approval handoff is not documented, the print dimensions in the current drafts need verification against Printful, and the artworks dataset is not consolidated.

**Do not automate or scale until the post-approval path is defined and at least one draft has completed the full cycle from intake through approved dataset record.**
