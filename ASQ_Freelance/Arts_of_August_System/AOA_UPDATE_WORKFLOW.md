# Arts of August Update Workflow

Last updated: 2026-07-21

## Purpose

Use this process to update the Arts of August master datasets and synchronize approved records to Firestore from VS Code.

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
