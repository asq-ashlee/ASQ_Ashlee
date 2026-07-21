# ID Conflict — AOA-ART-0060 — RESOLVED

**Conflict detected:** 2026-06-02
**Conflict resolved:** 2026-06-02
**Detected during:** Consolidated artworks.csv build from Notion export `2026_06_02`

---

## Conflict Summary

The artwork ID `AOA-ART-0060` was assigned to two different artworks across two sources.

| Source | artwork_id | Title |
|---|---|---|
| Repo master CSV (`AOA_ART_0060.csv`) | AOA-ART-0060 | What the Garden Kept |
| Notion export (`2026_06_02`) | AOA-ART-0060 | Blue Vase & Quiet Light |

---

## Repo Source-of-Truth Value — Unchanged

**AOA-ART-0060 = What the Garden Kept**

- Source file: `AOA_datasets/artworks/artwork_records/AOA_ART_0060.csv`
- Status: `approved`
- Workflow Status: `Ready for Products`
- Image: confirmed on Google Drive
- Approved record: `AOA_artwork-lab/aoa-approved/AOA-ART-0060-what-the-garden-kept-approved.md`

This record was not modified. AOA-ART-0060 remains assigned to What the Garden Kept.

---

## Conflicting Notion Export Value — Resolved

**Notion AOA-ART-0060 = Blue Vase & Quiet Light**

The `artwork_id` field in Notion was manually set to `AOA-ART-0060` for "Blue Vase & Quiet Light," likely before "What the Garden Kept" was processed through the artwork lab and assigned that ID in the repo. "Blue Vase & Quiet Light" is an Etsy import record with minimal metadata and had not gone through the artwork lab intake process.

---

## Human Decision

**Blue Vase & Quiet Light is a real painting and should remain in the active artwork dataset.**

Confirmed by: Ashlee — 2026-06-02

---

## Resolution

**Blue Vase & Quiet Light has been assigned AOA-ART-0063.**

| Action | Detail |
|---|---|
| New artwork_id | AOA-ART-0063 |
| Individual record created | `AOA_datasets/artworks/artwork_records/AOA_ART_0063.csv` |
| Added to consolidated dataset | `AOA_datasets/artworks/artworks.csv` |
| What the Garden Kept unchanged | AOA-ART-0060 retained as-is |

**Required follow-up:** The `artwork_id` field in Notion for "Blue Vase & Quiet Light" must be updated from `AOA-ART-0060` to `AOA-ART-0063` before the next Notion sync to prevent this conflict from reappearing.

---

## Fields Still Missing for Blue Vase & Quiet Light (AOA-ART-0063)

The following fields were not available in the Notion export and have not been populated. They require artwork lab intake or human review to complete.

- Category
- Date_Created
- Tags
- Mood
- Colors
- Image (Google Drive master file URL)
- Image_Status
- Primary_Use
- Alt_Text
- Description
- Story
- Subject
- Location
- Time_of_Day
- Light_Description
- Series

**Recommended next step:** Run Blue Vase & Quiet Light through the artwork lab intake workflow to complete metadata before listing.

---

**Logged by:** Claude Code — AOA-ART-0063 conflict resolution, 2026-06-02
