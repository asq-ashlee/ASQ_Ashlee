# Arts of August Update Workflow

Last updated: 2026-07-21

## Purpose

Use this process to update the Arts of August master datasets and synchronize approved records to Firestore from VS Code.

This document governs execution only when the owner's operational command resolves to it through `AOA_WORKFLOW_INDEX.md` or the owner explicitly invokes this update workflow. An approval state or approval declaration alone does not authorize a CSV write, Firestore synchronization, or any other step in this document.

## Normal Update Path

1. Edit the applicable master CSV in `AOA_datasets/`.
2. Preserve its header and every existing stable ID.
3. Give each new row a unique stable ID that follows the database map and schema.
4. Validate required IDs, duplicates, column alignment, and relationships.
5. Obtain human review for artistic facts, prices, public copy, availability, and schema changes.
6. Run the Firestore importers from the `ASQ_Ashlee` repository root:

```powershell
python "ASQ_Freelance\Arts_of_August_System\scripts\import_artworks.py"
python "ASQ_Freelance\Arts_of_August_System\scripts\import_databases.py"
```

7. Confirm every expected ID is present and no IDs are missing.
8. Review unexpected Firestore IDs. Never delete them automatically.
9. Commit approved CSV, script, and documentation changes to version history.

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

The scripts use Google Application Default Credentials. If authentication expires:

```powershell
gcloud.cmd auth application-default login
gcloud.cmd auth application-default set-quota-project stoked-proxy-502319-c4
```

Never commit credentials, service-account keys, access tokens, or secrets.

## Deletion Rule

Firestore deletion is a separate, explicit operation:

1. identify the exact collection and document ID;
2. confirm it is not represented in the master CSV;
3. obtain explicit human approval;
4. delete only the confirmed target;
5. read the collection again and verify expected IDs and counts.

## Governed Firestore Artwork Promotion

An approved artwork change reaches Firestore only through a reviewed plan and
`scripts/promote_artwork.py`. The approved artifact and per-artwork CSV must be
identical to their committed `HEAD` versions, and each target value must agree
with both sources. Dry run is the default. A write requires a separate,
artwork-specific phrase and one update-time-conditioned document update.

The promoter saves the full before-state for rollback and verifies the complete
document plus all reverse relationships afterward. Blank intake relationship
arrays never authorize deletion. Drive, Notion, website, publication, and
product-record mutations are outside this operation.
