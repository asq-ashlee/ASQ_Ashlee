"""Import the Arts of August master artwork dataset into Firestore."""

import csv
from pathlib import Path

from google.cloud import firestore


PROJECT_ID = "stoked-proxy-502319-c4"
COLLECTION_NAME = "artworks"
CSV_FILE_PATH = (
    Path(__file__).resolve().parents[1]
    / "AOA_datasets"
    / "artworks"
    / "artworks.csv"
)
BATCH_SIZE = 400


def load_artworks() -> list[dict[str, str]]:
    """Load and validate artwork rows before making any Firestore writes."""
    with CSV_FILE_PATH.open(mode="r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        if not reader.fieldnames or "artwork_id" not in reader.fieldnames:
            raise ValueError("CSV must contain an artwork_id column")

        artworks: list[dict[str, str]] = []
        seen_ids: set[str] = set()

        for line_number, row in enumerate(reader, start=2):
            if None in row:
                raise ValueError(f"Line {line_number} contains extra CSV columns")

            cleaned_row = {
                key.strip(): (value or "").strip()
                for key, value in row.items()
                if key
            }
            if not any(cleaned_row.values()):
                continue

            artwork_id = cleaned_row.get("artwork_id", "")
            if not artwork_id:
                raise ValueError(f"Line {line_number} has no artwork_id")
            if artwork_id in seen_ids:
                raise ValueError(f"Duplicate artwork_id: {artwork_id}")

            seen_ids.add(artwork_id)
            artworks.append(cleaned_row)

    return artworks


def upload_artworks() -> int:
    """Upsert validated artworks using stable IDs and return the write count."""
    artworks = load_artworks()
    db = firestore.Client(project=PROJECT_ID)
    collection_ref = db.collection(COLLECTION_NAME)

    for batch_start in range(0, len(artworks), BATCH_SIZE):
        batch_rows = artworks[batch_start : batch_start + BATCH_SIZE]
        batch = db.batch()

        for artwork in batch_rows:
            doc_ref = collection_ref.document(artwork["artwork_id"])
            batch.set(doc_ref, artwork)

        batch.commit()
        print(f"Uploaded {batch_start + len(batch_rows)} of {len(artworks)} records")

    return len(artworks)


if __name__ == "__main__":
    count = upload_artworks()
    print(
        f"Migration complete: imported {count} artworks into "
        f"{COLLECTION_NAME!r} in {PROJECT_ID!r}."
    )
