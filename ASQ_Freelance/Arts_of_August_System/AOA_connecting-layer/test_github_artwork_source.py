import base64
import io
import json
import unittest
from unittest.mock import patch

from github_artwork_source import (
    ArtworkSourceUnavailable,
    INDEX_URL,
    check_current_identity,
)


class SourceTests(unittest.TestCase):
    def test_reads_fresh_governed_csv_and_detects_existing_listing(self):
        csv_text = (
            "artwork_id,Title,Slug\n"
            "AOA-ART-0065,Eastern Trail Marsh,eastern-trail-marsh\n"
        )
        payload = json.dumps({
            "type": "file", "encoding": "base64", "sha": "reviewed-revision",
            "content": base64.b64encode(csv_text.encode()).decode(),
        }).encode()
        seen = []

        def fake_open(request, timeout):
            seen.append(request)
            self.assertEqual(timeout, 10)
            return io.BytesIO(payload)

        with patch("github_artwork_source.urlopen", side_effect=fake_open):
            result = check_current_identity(
                "server-only-test-token", title="Eastern Trail Marsh",
                slug="eastern-trail-marsh",
            )
        self.assertEqual(result["state"], "existing")
        self.assertEqual(result["source_sha"], "reviewed-revision")
        self.assertEqual(seen[0].full_url, INDEX_URL)
        self.assertEqual(seen[0].get_header("Authorization"),
                         "Bearer server-only-test-token")

    def test_missing_credential_fails_closed(self):
        with self.assertRaises(ArtworkSourceUnavailable):
            check_current_identity("", title="Eastern Trail Marsh")

    def test_repository_error_fails_closed(self):
        with patch("github_artwork_source.urlopen", side_effect=OSError("offline")):
            with self.assertRaises(ArtworkSourceUnavailable):
                check_current_identity("server-only-test-token",
                                       title="Eastern Trail Marsh")


if __name__ == "__main__":
    unittest.main()
