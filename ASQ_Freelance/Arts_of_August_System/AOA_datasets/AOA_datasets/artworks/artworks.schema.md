# Artworks Dataset Schema

## Purpose
Portable record of Arts of August artwork metadata.

## Source
Originally exported from Notion Art Pieces database.

## Primary File
artworks.csv

## Fields

- artwork_id: stable Arts of August ID. Example: AOA-ART-0001.
- Title: approved artwork title.
- Status: artwork lifecycle status.
- Category: artwork category, such as Coastal.
- Orientation: portrait, landscape, square.
- Size: original artwork size.
- Original Available: whether the original is still available.
- Base Price: original artwork base price.
- Date Created: date the artwork was created.
- Tags: discovery tags.
- Mood: restrained emotional tone.
- Colors: palette notes.
- Image: source image link or file reference.
- Primary Use: intended use or merchandising direction.
- AI Ready: whether artwork is ready for AI interpretation.
- Description: approved artwork description.
- Story: artist/context note.
- Subject: visual subject.
- Location: place reference, if known.
- Time of Day: dawn, afternoon, evening, etc.
- Light Description: observed light condition.
- AI Draft Complete: whether AI draft exists.
- Human Approved: whether human review is complete.
- Products Linked: related product records.
- Content Linked: related content records.
- Workflow Status: current operational stage.

## Record Rules

- Each artwork must have one stable `artwork_id`.
- `artwork_id` should not depend on Notion page IDs.
- Blank Notion export rows should be removed before committing the dataset.
- Notion links may be preserved as references, but they are not primary IDs.