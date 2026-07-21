"""Build stable-ID master CSVs from the latest Arts of August Notion exports."""

import csv
import re
from collections import Counter, defaultdict, deque
from pathlib import Path


SYSTEM_ROOT = Path(__file__).resolve().parents[1]
DATASETS_ROOT = SYSTEM_ROOT / "AOA_datasets"

EXPORTS = {
    "events": SYSTEM_ROOT / "Events 37070b21b17e80418de2fa8e46c79716.csv",
    "products": SYSTEM_ROOT / "Products 35170b21b17e80f4b54fe2baca09a681.csv",
    "content": SYSTEM_ROOT / "Content 35170b21b17e806288c4c710a1e7d8d6.csv",
    "opportunities": SYSTEM_ROOT
    / "Opportunities 37070b21b17e80e2b50ae5bbe21d7a4f.csv",
}

MASTER_CONFIG = {
    "events": ("events.csv", "event_id", "AOA-EVT", "Slug"),
    "content": ("content.csv", "content_id", "AOA-CNT", "Name"),
    "opportunities": (
        "opportunities.csv",
        "opportunity_id",
        "AOA-OPP",
        "Name",
    ),
}


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    if not path.exists():
        raise FileNotFoundError(f"Required export not found: {path}")
    with path.open(encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        if not reader.fieldnames:
            raise ValueError(f"CSV has no header: {path}")
        rows = list(reader)
    if any(None in row for row in rows):
        raise ValueError(f"CSV contains extra columns: {path}")
    return list(reader.fieldnames), rows


def clean_row(row: dict[str, str]) -> dict[str, str]:
    return {key.strip(): (value or "").strip() for key, value in row.items() if key}


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def next_numbered_id(prefix: str, used: set[str]) -> str:
    pattern = re.compile(rf"^{re.escape(prefix)}-(\d{{4}})$")
    highest = max(
        (int(match.group(1)) for value in used if (match := pattern.match(value))),
        default=0,
    )
    candidate = f"{prefix}-{highest + 1:04d}"
    while candidate in used:
        highest += 1
        candidate = f"{prefix}-{highest + 1:04d}"
    return candidate


def consolidate_numbered_master(kind: str) -> tuple[Path, int]:
    filename, id_field, prefix, natural_key = MASTER_CONFIG[kind]
    source_fields, source_rows = read_csv(EXPORTS[kind])
    master_path = DATASETS_ROOT / kind / filename

    existing_by_key: dict[str, str] = {}
    used_ids: set[str] = set()
    if master_path.exists():
        _, existing_rows = read_csv(master_path)
        for row in existing_rows:
            key = (row.get(natural_key) or "").strip().casefold()
            record_id = (row.get(id_field) or "").strip()
            if key and record_id:
                existing_by_key[key] = record_id
                used_ids.add(record_id)

    output_rows: list[dict[str, str]] = []
    seen_keys: set[str] = set()
    for raw_row in source_rows:
        row = clean_row(raw_row)
        key = row.get(natural_key, "").casefold()
        if not key:
            raise ValueError(f"{kind}: blank required field {natural_key}")
        if key in seen_keys:
            raise ValueError(f"{kind}: duplicate {natural_key}: {row[natural_key]}")
        seen_keys.add(key)

        record_id = existing_by_key.get(key)
        if not record_id:
            record_id = next_numbered_id(prefix, used_ids)
            used_ids.add(record_id)
        output_rows.append({id_field: record_id, **row})

    fields = [id_field, *[field for field in source_fields if field != id_field]]
    write_csv(master_path, fields, output_rows)
    return master_path, len(output_rows)


def artwork_title_map() -> dict[str, str]:
    _, rows = read_csv(DATASETS_ROOT / "artworks" / "artworks.csv")
    return {
        row["Title"].strip().casefold(): row["artwork_id"].strip()
        for row in rows
        if row.get("Title") and row.get("artwork_id")
    }


def source_artwork_title(value: str) -> str:
    return re.sub(r"\s+\(https?://.*\)\s*$", "", value).strip()


def product_identity(row: dict[str, str]) -> tuple[str, ...]:
    ignored = {"product_id", "artwork_id"}
    return tuple(
        f"{key}={value.strip()}"
        for key, value in row.items()
        if key not in ignored
    )


def existing_product_ids_by_name() -> dict[str, str]:
    records_dir = DATASETS_ROOT / "products" / "product_records"
    candidates: defaultdict[str, set[str]] = defaultdict(set)
    for path in records_dir.glob("AOA_PRD_*.csv"):
        _, rows = read_csv(path)
        for row in rows:
            name = (row.get("Product Name") or "").strip().casefold()
            product_id = (row.get("product_id") or "").strip()
            if name and product_id:
                candidates[name].add(product_id)
    return {
        name: next(iter(ids))
        for name, ids in candidates.items()
        if len(ids) == 1
    }


def consolidate_products() -> tuple[Path, int]:
    source_fields, source_rows = read_csv(EXPORTS["products"])
    master_path = DATASETS_ROOT / "products" / "products.csv"
    title_to_artwork = artwork_title_map()
    curated_by_name = existing_product_ids_by_name()

    preserved: defaultdict[tuple[str, ...], deque[tuple[str, str]]] = defaultdict(deque)
    if master_path.exists():
        _, existing_rows = read_csv(master_path)
        for existing in existing_rows:
            preserved[product_identity(existing)].append(
                (
                    (existing.get("product_id") or "").strip(),
                    (existing.get("artwork_id") or "").strip(),
                )
            )

    rows: list[dict[str, str]] = []
    used_ids: set[str] = set()
    for raw_row in source_rows:
        row = clean_row(raw_row)
        preserved_values = preserved[product_identity(row)]
        if preserved_values:
            old_product_id, old_artwork_id = preserved_values.popleft()
            row["product_id"] = row.get("product_id") or old_product_id
            row["artwork_id"] = row.get("artwork_id") or old_artwork_id

        notes_match = re.search(r"AOA-PRD-\d{4}-\d{3}", row.get("Notes", ""))
        if not row.get("product_id") and notes_match:
            row["product_id"] = notes_match.group(0)

        name_key = row.get("Product Name", "").casefold()
        if not row.get("product_id") and name_key in curated_by_name:
            row["product_id"] = curated_by_name[name_key]

        if not row.get("artwork_id"):
            title = source_artwork_title(row.get("Source Artwork", "")).casefold()
            row["artwork_id"] = title_to_artwork.get(title, "")

        if row.get("product_id"):
            if row["product_id"] in used_ids:
                raise ValueError(f"Duplicate product_id: {row['product_id']}")
            used_ids.add(row["product_id"])
        rows.append(row)

    next_variant: Counter[str] = Counter()
    for value in used_ids:
        match = re.match(r"^AOA-PRD-(\d{4})-(\d{3})$", value)
        if match:
            next_variant[match.group(1)] = max(
                next_variant[match.group(1)], int(match.group(2))
            )

    legacy_numbers = [
        int(match.group(1))
        for value in used_ids
        if (match := re.match(r"^AOA-PRD-LEGACY-(\d{4})$", value))
    ]
    next_legacy = max(legacy_numbers, default=0)

    for row in rows:
        if row.get("product_id"):
            continue
        artwork_id = row.get("artwork_id", "")
        artwork_match = re.match(r"^AOA-ART-(\d{4})$", artwork_id)
        if artwork_match:
            artwork_number = artwork_match.group(1)
            while True:
                next_variant[artwork_number] += 1
                candidate = (
                    f"AOA-PRD-{artwork_number}-{next_variant[artwork_number]:03d}"
                )
                if candidate not in used_ids:
                    break
        else:
            while True:
                next_legacy += 1
                candidate = f"AOA-PRD-LEGACY-{next_legacy:04d}"
                if candidate not in used_ids:
                    break
        row["product_id"] = candidate
        used_ids.add(candidate)

    if len(used_ids) != len(rows):
        raise ValueError("Products did not receive unique product_id values")

    fields = [
        "product_id",
        "artwork_id",
        *[
            field
            for field in source_fields
            if field not in {"product_id", "artwork_id"}
        ],
    ]
    write_csv(master_path, fields, rows)
    return master_path, len(rows)


def main() -> None:
    results = [consolidate_numbered_master(kind) for kind in MASTER_CONFIG]
    results.append(consolidate_products())
    for path, count in results:
        print(f"Built {path.relative_to(SYSTEM_ROOT)}: {count} records")


if __name__ == "__main__":
    main()
