"""Upsert validated Arts of August master datasets into Firestore."""

import csv
from pathlib import Path

from google.cloud import firestore


PROJECT_ID = "stoked-proxy-502319-c4"
SYSTEM_ROOT = Path(__file__).resolve().parents[1]
BATCH_SIZE = 400

DATASETS = {
    "events": (SYSTEM_ROOT / "AOA_datasets" / "events" / "events.csv", "event_id"),
    "products": (
        SYSTEM_ROOT / "AOA_datasets" / "products" / "products.csv",
        "product_id",
    ),
    "content": (
        SYSTEM_ROOT / "AOA_datasets" / "content" / "content.csv",
        "content_id",
    ),
    "opportunities": (
        SYSTEM_ROOT / "AOA_datasets" / "opportunities" / "opportunities.csv",
        "opportunity_id",
    ),
}


def load_records(path: Path, id_field: str) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        if not reader.fieldnames or id_field not in reader.fieldnames:
            raise ValueError(f"{path} must contain {id_field}")
        rows = list(reader)

    records: list[dict[str, str]] = []
    seen_ids: set[str] = set()
    for line_number, raw_row in enumerate(rows, start=2):
        if None in raw_row:
            raise ValueError(f"{path}:{line_number} contains extra CSV columns")
        row = {
            key.strip(): (value or "").strip()
            for key, value in raw_row.items()
            if key
        }
        record_id = row.get(id_field, "")
        if not record_id:
            raise ValueError(f"{path}:{line_number} has no {id_field}")
        if record_id in seen_ids:
            raise ValueError(f"{path} contains duplicate ID {record_id}")
        seen_ids.add(record_id)
        records.append(row)
    return records


def upload_collection(
    db: firestore.Client,
    collection_name: str,
    path: Path,
    id_field: str,
) -> set[str]:
    records = load_records(path, id_field)
    collection_ref = db.collection(collection_name)

    for batch_start in range(0, len(records), BATCH_SIZE):
        batch_rows = records[batch_start : batch_start + BATCH_SIZE]
        batch = db.batch()
        for record in batch_rows:
            batch.set(collection_ref.document(record[id_field]), record)
        batch.commit()

    expected_ids = {record[id_field] for record in records}
    print(f"Uploaded {len(records)} records to {collection_name}")
    return expected_ids


def main() -> None:
    db = firestore.Client(project=PROJECT_ID)
    expected_by_collection: dict[str, set[str]] = {}

    for collection_name, (path, id_field) in DATASETS.items():
        expected_by_collection[collection_name] = upload_collection(
            db, collection_name, path, id_field
        )

    for collection_name, expected_ids in expected_by_collection.items():
        actual_ids = {
            document.id for document in db.collection(collection_name).stream()
        }
        missing = sorted(expected_ids - actual_ids)
        unexpected = sorted(actual_ids - expected_ids)
        print(
            f"Verified {collection_name}: {len(expected_ids & actual_ids)}/"
            f"{len(expected_ids)} expected present; total={len(actual_ids)}; "
            f"missing={len(missing)}; unexpected={len(unexpected)}"
        )
        if missing:
            raise RuntimeError(f"{collection_name} missing IDs: {missing}")
        if unexpected:
            print(f"Unexpected existing IDs in {collection_name}: {unexpected}")


if __name__ == "__main__":
    main()
