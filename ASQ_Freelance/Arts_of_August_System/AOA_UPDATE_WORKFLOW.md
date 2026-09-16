# Arts of August Update Workflow

Last updated: 2026-09-16

## Purpose

Use this process to update the Arts of August master datasets and synchronize approved records to Firestore.

This document governs execution when the owner's operational command resolves to it through the active workflow registry, when the owner explicitly invokes this update workflow, or when a governed interface/bridge invokes it under an authorization contract that explicitly permits delegation.

A generic approval declaration by itself does not authorize a CSV write, Firestore synchronization, or any other step in this document. However, an artist-facing action such as `approveArtwork` may count as an explicit operational command **only** when `AOA_connecting-layer/artwork-studio-bridge-contract.md` applies and the bridge can prove the reviewed artwork context, scope, prerequisites, and approval state.

## Governed Bridge Invocation

For Artwork Studio flows, the authorized bridge may translate a valid `approveArtwork` / `prepareWebsite` workflow action into the technical confirmation needed for the current artwork's routine, field-bounded promotion.

This translation is permitted only when:

1. the exact artwork package has been reviewed and approved;
2. the stable ID/identity is resolved or deterministically allocatable under this workflow;
3. the approved intake artifact and per-artwork CSV match their committed versions where the promoter requires that condition;
4. all target values agree with the approved sources;
5. dry run passes;
6. the operation is limited to the current artwork and approved fields/relationships;
7. rollback capture and post-write verification remain active;
8. no deletion, schema change, unrelated record mutation, or website publication is implied;
9. the bridge records the originating artist-level authorization in its administrative audit context.

The artist does not need to see or type an internal confirmation phrase/token when the governed bridge is the caller. The bridge may generate/supply the artwork-specific technical confirmation deterministically after all prerequisites pass.

If any requirement above fails, stop rather than broadening scope or asking the artist to troubleshoot internal mechanics. Surface a simple blocker and route technical remediation to the system owner/operator.

## Normal Update Path

1. Edit the applicable master CSV in `AOA_datasets/`.
2. Preserve its header and every existing stable ID.
3. Give each new row a unique stable ID that follows the database map and schema.
4. Validate required IDs, duplicates, column alignment, and relationships.
5. Obtain human review for artistic facts, prices, public copy, availability, and schema changes as applicable.
6. Run the applicable Firestore importer/promoter from the `ASQ_Ashlee` repository root.
7. Confirm every expected ID is present and no IDs are missing.
8. Review unexpected Firestore IDs. Never delete them automatically.
9. Commit approved CSV, script, and documentation changes to version history.

Legacy bulk import commands remain:

```powershell
python "ASQ_Freelance\Arts_of_August_System\scripts\import_artworks.py"
python "ASQ_Freelance\Arts_of_August_System\scripts\import_databases.py"
```

For one governed artwork, prefer the plan-driven artwork promoter described below rather than broad imports.

## Stable ID Allocation for Net-New Records

The master CSV, not Notion, governs stable-ID allocation. For a net-new artwork that has been human-confirmed as a distinct physical original and approved for operational memory:

1. Read the current `AOA_datasets/artworks/artworks.csv`.
2. Validate that the proposed title/identity is not already represented and that all existing `artwork_id` values are unique.
3. Find the highest numeric suffix currently present in the master CSV.
4. Propose the next sequential four-digit ID (`highest + 1`).
5. Collision-check that proposed ID against the master CSV and any known governed conflict/reservation evidence. Do not use Notion exports to allocate IDs.
6. Record the allocation in the approved intake/handoff artifact, then write the new row to the master CSV.
7. Validate the full CSV before any Firestore promotion.

If the current master contains a known baseline identity conflict, do not renumber or repair the conflicting records during unrelated intake. An unaffected net-new record may receive the next sequential unused ID so long as the proposed ID itself is not implicated in the conflict.

## Legacy Export Consolidation

The consolidation utility reads the named legacy export files at the Arts of August system root and rebuilds the four non-artwork masters:

```powershell
python "ASQ_Freelance\Arts_of_August_System\scripts\consolidate_databases.py"
```

Run this only when intentionally processing those migration exports. Inspect the resulting master CSV diff before importing. Notion is no longer the routine editing path.

## Synchronization Behavior

- Existing ID: update its Firestore document.
- New ID: create a Firestore document.
- Row removed from CSV: do not delete the Firestore document.
- Blank or duplicate ID: stop before writing that dataset.
- Extra Firestore document: report it for human review.

## Authentication

The scripts use Google Application Default Credentials unless the governed bridge/runtime uses another approved least-privilege server-side authentication path.

For local operator recovery, if authentication expires:

```powershell
gcloud.cmd auth application-default login
gcloud.cmd auth application-default set-quota-project stoked-proxy-502319-c4
```

Never commit credentials, service-account keys, access tokens, or secrets. Never expose privileged credentials to browser-side Artwork Studio code.

## Deletion Rule

Firestore deletion is a separate, explicit operation:

1. identify the exact collection and document ID;
2. confirm it is not represented in the master CSV;
3. obtain explicit human approval;
4. delete only the confirmed target;
5. read the collection again and verify expected IDs and counts.

Neither `approveArtwork` nor `prepareWebsite` authorizes deletion.

## Governed Firestore Artwork Promotion

An approved artwork change reaches Firestore only through a reviewed plan and `scripts/promote_artwork.py` (or its governed service wrapper).

The approved artifact and per-artwork CSV must be identical to their committed `HEAD` versions where required by the promoter, and each target value must agree with both sources. Dry run is the default.

A production write requires artwork-specific authorization. That authorization may be supplied either:

- directly by an authorized operator using the exact technical confirmation mechanism; or
- by the governed Artwork Studio bridge translating a valid artist-level `approveArtwork` / `prepareWebsite` action under the rules in this document and `artwork-studio-bridge-contract.md`.

The promoter saves the full before-state for rollback and verifies the complete document plus all reverse relationships afterward. Blank intake relationship arrays never authorize deletion. Drive, Notion, website publication, product-record mutation, and other distribution remain outside the Firestore operation.

## Public Publication Boundary

No Firestore synchronization, repo update, Drive asset binding, or website-preparation action in this workflow authorizes public publication.

Public deployment remains separately governed by `publishArtwork` / explicit publication approval for the reviewed website preview.