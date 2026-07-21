# Arts of August Master Datasets

Last updated: 2026-07-21

This folder contains the portable structured source of truth for Arts of August records. Firestore is the live application database synchronized from these approved CSVs.

## Masters

- `artworks/artworks.csv`
- `products/products.csv`
- `content/content.csv`
- `events/events.csv`
- `opportunities/opportunities.csv`

Each row requires a stable ID. The same ID is used as the Firestore document ID.

## Operating Rules

1. Edit a master, not a dated Notion export.
2. Preserve headers and stable IDs.
3. Validate the entire CSV before upload.
4. Keep values as portable CSV text unless an approved schema changes the Firestore type contract.
5. Follow `../AOA_UPDATE_WORKFLOW.md`.
6. Treat Notion exports as migration evidence only.

## Import Commands

From the repository root:

```powershell
python "ASQ_Freelance\Arts_of_August_System\scripts\import_artworks.py"
python "ASQ_Freelance\Arts_of_August_System\scripts\import_databases.py"
```

Imports are stable-ID upserts. They do not delete documents missing from a CSV.
