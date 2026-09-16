import unittest

from bridge_identity import InvalidArtworkIndex, check_identity


CSV = """artwork_id,Title,Slug
AOA-ART-0065,Eastern Trail Marsh,eastern-trail-marsh
AOA-ART-0064,Anchored in Wild Bloom,anchored-in-wild-bloom
"""


class IdentityCheckTests(unittest.TestCase):
    def test_live_lovable_listing_cannot_be_recreated(self):
        result = check_identity(
            CSV, artwork_id="AOA-ART-0065",
            title="Eastern Trail Marsh", slug="eastern-trail-marsh",
        )
        self.assertEqual(result["state"], "existing")
        self.assertEqual(result["matches"][0]["matched_on"],
                         ["artwork_id", "slug", "title"])

    def test_matching_only_title_still_requires_review(self):
        result = check_identity(CSV, title="  eastern trail marsh  ")
        self.assertEqual(result["state"], "existing")

    def test_conflicting_keys_are_ambiguous(self):
        result = check_identity(
            CSV, artwork_id="AOA-ART-0064", slug="eastern-trail-marsh",
        )
        self.assertEqual(result["state"], "ambiguous")

    def test_no_match_is_only_clear_not_creation(self):
        self.assertEqual(check_identity(CSV, title="New Painting")["state"], "clear")

    def test_missing_columns_fail_closed(self):
        with self.assertRaises(InvalidArtworkIndex):
            check_identity("Title\nEastern Trail Marsh\n", title="Eastern Trail Marsh")


if __name__ == "__main__":
    unittest.main()
