"""Read-only artwork identity checks for the future AOA bridge.

This module takes governed CSV bytes as an input. It has no network or write path.
The eventual authenticated service must obtain a fresh CSV snapshot server-side.
"""

import csv
import io
import re
import unicodedata


class InvalidArtworkIndex(ValueError):
    pass


def _key(value):
    value = unicodedata.normalize("NFKC", str(value or "")).casefold()
    return " ".join(value.split())


def _slug(value):
    value = unicodedata.normalize("NFKD", str(value or "")).casefold()
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")


def check_identity(csv_text, *, artwork_id=None, title=None, slug=None):
    """Return a conflict, ambiguity, or clear result; never allocate an ID.

    Title and slug are compared independently. A title-only match is intentionally
    treated as a conflict that needs human review, even if two works could share
    a title. No match is not permission to create an artwork.
    """
    if not any((artwork_id, title, slug)):
        raise ValueError("Provide an artwork ID, title, or slug")
    reader = csv.DictReader(io.StringIO(csv_text))
    if not reader.fieldnames or not {"artwork_id", "Title", "Slug"} <= set(reader.fieldnames):
        raise InvalidArtworkIndex("Missing governed identity columns")
    rows = list(reader)
    if any(None in row for row in rows):
        raise InvalidArtworkIndex("Malformed artwork CSV row")

    matched = []
    for row in rows:
        reasons = []
        if artwork_id and _key(row["artwork_id"]) == _key(artwork_id):
            reasons.append("artwork_id")
        if slug and _slug(row["Slug"]) == _slug(slug):
            reasons.append("slug")
        if title and _key(row["Title"]) == _key(title):
            reasons.append("title")
        if reasons:
            matched.append({
                "artwork_id": row["artwork_id"],
                "title": row["Title"],
                "slug": row["Slug"],
                "matched_on": reasons,
            })

    if len(matched) > 1:
        return {"state": "ambiguous", "matches": matched}
    if matched:
        return {"state": "existing", "matches": matched}
    return {"state": "clear", "matches": []}
