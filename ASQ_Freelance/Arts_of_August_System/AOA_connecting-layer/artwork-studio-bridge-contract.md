# AOA Artwork Studio Bridge Contract

Last updated: 2026-09-16
Status: active

## Purpose

This contract defines the boundary between an artist-facing Artwork Studio interface and the governed Arts of August operational system.

The Artwork Studio is a thin human interface. It is not a database, source of truth, publishing system, or independent workflow engine. The governed AOA system remains responsible for identity, records, assets, Firestore promotion, website implementation, publication safeguards, and verification.

Primary architecture:

`Artwork Studio → authenticated AOA bridge → governed AOA workflows → Repo / Drive / Firestore / Lovable`

The bridge must preserve existing AOA governance while translating simple artist actions into bounded internal workflow operations.

## Source-of-Truth Boundaries

- Master CSVs in `AOA_datasets/` remain the portable structured-record source of truth.
- Firestore remains the live application database.
- Google Drive remains the governed durable asset store for approved artwork images and presentation assets.
- Lovable remains the public display layer, not a source of truth.
- The Artwork Studio must not create a competing production artwork database or independent catalog.
- Temporary browser/UI state is not an approved operational record.

## Seven-Action Interface

The bridge exposes seven conceptual artist-facing actions. Implementations may use HTTP endpoints, RPC, MCP, or another authenticated transport, but the semantics below are fixed.

### 1. `startArtwork`

Purpose: begin intake for one physical original.

Accepts, as available:
- source artwork photograph/file;
- title or request for title help;
- dimensions;
- medium/support;
- year/date to the level actually known;
- price;
- availability;
- checkout link;
- optional location;
- optional artist note/story.

Authorizes:
- intake-state creation;
- evidence classification;
- identity/conflict checks;
- collection of genuinely missing facts.

Does not authorize:
- permanent record mutation;
- Firestore production writes;
- public website publication.

### 2. `prepareMaster`

Purpose: produce a faithful canonical-master candidate from the supplied source photograph.

Rules:
- canonical-master preparation must use deterministic, non-generative photographic transformations only;
- permitted operations include crop, rotation/straightening, perspective correction, lens/optics correction, exposure, white balance, temperature/tint, restrained levels/curves, and restrained highlight/shadow correction;
- no generative image editing, synthesis, inpainting, outpainting, style transfer, reconstruction, content-aware replacement, or AI repainting may touch artwork pixels;
- sharpening, clarity, texture, contrast, saturation, or similar operations must not materially alter brushwork, edge softness, texture, tonal relationships, or color character;
- if a deterministic editor is unavailable, stop and request/use a non-generative editing path rather than falling back to image generation;
- preserve the best available source resolution and avoid destructive downscaling or lossy re-encoding for the archival/canonical asset unless the governed asset workflow explicitly requires it.

Returns:
- master candidate;
- correction summary sufficient for audit;
- any unresolved fidelity issue requiring artist review.

### 3. `approveMaster`

Purpose: record the artist's judgment that the prepared master faithfully represents the physical painting.

Natural-language equivalents include `Approve Master`, `That matches the painting`, or another unambiguous approval in the current artwork context.

Authorizes:
- use of the exact reviewed master as the canonical image for downstream artwork work;
- continued metadata, presentation, and listing preparation.

Does not authorize:
- public publication;
- substitution of a different master without renewed approval.

If the master changes materially after approval, master approval is invalidated and must be obtained again.

### 4. `prepareArtwork`

Purpose: run the governed Artwork Lab interpretation/intake logic after master approval and prepare the artist-review package.

May produce, where supported by evidence and schema:
- title suggestions when requested;
- description;
- story/hook;
- alt text;
- subject;
- light description;
- mood;
- colors;
- category;
- orientation;
- tags/discovery terms;
- series/location/time-of-day only when confirmed or otherwise permitted by evidence rules;
- one or more presentation/lifestyle mockups.

Rules:
- preserve evidence classes: Owner/Artist Confirmed, Source Verified, Visually Observed, AI Interpretation, Unknown;
- unknown remains unknown;
- never invent physical facts, business facts, provenance, location, time of day, or artist intent;
- a mockup is a derivative presentation asset only and must never replace the canonical master;
- where a lifestyle mockup is generated, the environment may be generated, but the approved artwork must be faithfully composited/referenced and must not be regenerated or redrawn.

Returns a concise artist-facing review package plus complete structured metadata for the governed record.

### 5. `approveArtwork`

Purpose: record artist approval of the reviewed artwork package: canonical master, presentation/lifestyle mockup state, title, price/availability, public copy, and relevant metadata.

Natural-language equivalents include `Approve Artwork`, `Looks good`, or another unambiguous approval after the review package is shown.

Authorizes the bridge to perform routine governed operational preparation needed to make a website preview, including:
- stable-ID allocation/collision checks for a net-new original;
- approved intake artifact finalization;
- master CSV and per-artwork mirror writes;
- validation;
- canonical Drive asset naming/storage/binding;
- governed Firestore dry run, rollback capture, promotion, and read-back verification when the applicable workflow allows the bridge to translate this approval into the required technical confirmation mechanism;
- preparation of the Lovable website implementation and preview.

This is artist-level workflow authorization, not unrestricted system authority. The bridge must remain field-bounded to the reviewed artwork package and current artwork only.

`approveArtwork` does **not** authorize public website publication, unrelated repo changes, schema changes, deletion, POD publishing, Etsy, social, email, or other distribution.

If a governing action requires separate system-owner authorization that cannot legally/technically be delegated through this contract, the bridge must stop and surface one simple human question without exposing internal jargon.

### 6. `prepareWebsite`

Purpose: complete the routine governed backend work necessary to return a real website preview for the approved artwork.

The bridge should orchestrate successful internal steps quietly. It may report artist-friendly progress such as:
- Saving artwork
- Securing images
- Preparing website
- Ready for review

It must not require the artist to type technical confirmation tokens, understand GitHub/Firestore/Drive/Lovable, or manually relay internal commands when the bridge is authorized to do so.

Required safeguards remain in force:
- exact reviewed values/assets only;
- repo/master validation;
- Firestore dry run / rollback / conditional-write / read-back safeguards where applicable;
- build/preview validation;
- no public deployment.

Returns:
- website preview URL/state;
- human-readable summary of what will be published;
- blockers if preview preparation cannot be completed.

### 7. `publishArtwork`

Purpose: publish only the exact website version the artist reviewed.

Natural-language equivalents include `Publish Artwork`, `Publish it`, or `Make it live` in the current preview context.

Requirements:
- a current valid website preview exists;
- publication approval refers to that reviewed version;
- if the preview changes materially afterward, authorization expires and must be obtained again.

Authorizes:
- deployment/publication of that reviewed website version;
- post-deploy verification of the public artwork URL and expected purchase behavior.

The bridge must never describe a pending deployment as complete. The artwork reaches published/verified state only after live verification succeeds or the unresolved verification issue is clearly reported.

## Quiet-Orchestration Rule

Governance constrains the operator; it must not become the artist's checklist.

After an artist-facing action is authorized, the bridge should execute routine reversible/intermediate governed operations without narrating each internal step. Successful GitHub writes, Drive binding, Firestore tokens, rollback capture, schema checks, and deployment mechanics remain available in logs/administrative reporting but are not part of the normal artist UI.

Surface only:
- artist judgment decisions;
- public publication approval;
- missing facts the artist can answer;
- meaningful failures/blockers;
- exceptional system-owner decisions that cannot be delegated.

Never hide or bypass a failed safety check. Quiet orchestration means quiet successful plumbing, not silent failure or weakened safeguards.

## Authorization Translation

The bridge may translate a valid artist-level action into deterministic internal technical authorization only when all of the following are true:

1. this contract and the invoked workflow explicitly permit the translation;
2. scope is limited to the current reviewed artwork and approved fields/assets;
3. all technical preconditions/dry runs/checks pass;
4. rollback/read-back safeguards remain intact;
5. no public publication occurs unless `publishArtwork` is separately authorized.

Technical confirmation phrases/tokens remain machine-level safeguards. They do not need to be exposed to the artist when the bridge is the authorized caller and can generate/supply them deterministically from the approved action context.

## Error Contract

Artist-facing errors should be brief and actionable, for example:

`I couldn't finish preparing this artwork. Nothing was published. Please ask Ashlee for help.`

Administrative logs should preserve the specific failing operation, target, response/error, rollback state, and retry status.

Never simulate success when an external write, upload, promotion, build, deployment, or verification did not complete.

## Security / Transport Requirements

- The deployed Artwork Studio must not receive broad GitHub, Google, Firebase, or Lovable credentials in browser-side code.
- Secrets belong server-side in the bridge/runtime.
- Authentication should identify the permitted artist/operator and bind every mutation to one artwork/workflow context.
- Prefer least-privilege credentials and narrowly scoped actions.
- The bridge must validate server-side rather than trusting client-provided approval state.

## Definition of Done

The bridge contract is implemented correctly when an artist can move through:

`New Artwork → Prepare Image → Presentation → Artwork Details → Preparing Website → Website Preview → Publish`

while the governed AOA system preserves:
- faithful non-generative canonical masters;
- complete structured intake metadata;
- source-of-truth records;
- validated durable assets;
- Firestore safeguards;
- preview-before-publish;
- explicit publication approval;
- verified live state;

without exposing routine backend mechanics to the artist.