"""Server-side, read-only access to the governed AOA artwork index.

The GitHub credential is supplied by the caller. Never put it in the browser
or print it. This module neither caches nor writes artwork records.
"""

import base64
import json
from urllib.request import Request, urlopen

from bridge_identity import InvalidArtworkIndex, check_identity


INDEX_URL = (
    "https://api.github.com/repos/asq-ashlee/ASQ_Ashlee/contents/"
    "ASQ_Freelance/Arts_of_August_System/AOA_datasets/artworks/artworks.csv"
    "?ref=main"
)
MAX_INDEX_BYTES = 5_000_000


class ArtworkSourceUnavailable(RuntimeError):
    pass


def read_governed_index(token):
    """Get the current CSV from the fixed repository path, or fail closed."""
    if not token or not token.strip():
        raise ArtworkSourceUnavailable("Server credential is not configured")
    request = Request(
        INDEX_URL,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "aoa-artwork-studio-bridge",
            "Cache-Control": "no-cache",
        },
    )
    try:
        with urlopen(request, timeout=10) as response:
            payload = response.read(MAX_INDEX_BYTES * 2)
        data = json.loads(payload)
        if data.get("encoding") != "base64" or data.get("type") != "file":
            raise ValueError("Unexpected repository response")
        raw = base64.b64decode(data["content"], validate=False)
        if not raw or len(raw) > MAX_INDEX_BYTES:
            raise ValueError("Artwork index is empty or too large")
        return raw.decode("utf-8-sig"), data["sha"]
    except (OSError, ValueError, KeyError, UnicodeError, TypeError) as exc:
        raise ArtworkSourceUnavailable("Could not read governed artwork index") from exc


def check_current_identity(token, *, artwork_id=None, title=None, slug=None):
    """Return a read-only decision and the source revision checked."""
    csv_text, revision = read_governed_index(token)
    try:
        result = check_identity(csv_text, artwork_id=artwork_id, title=title, slug=slug)
    except InvalidArtworkIndex as exc:
        raise ArtworkSourceUnavailable("Governed artwork index is invalid") from exc
    return {**result, "source_sha": revision}
