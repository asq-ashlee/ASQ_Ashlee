# AOA Artwork Image Editing Workflow

Last updated: 2026-05-28
Status: active
Workspace: AOA_artwork-lab
Workflow Type: Artwork image preparation / documentation editing

---

## Purpose

This workflow defines how Arts of August artwork images should be reviewed and edited before they become operational source images for artwork records, product planning, listings, submissions, and distribution workflows.

The goal is not to stylize the image.

The goal is to create an accurate, consistent documentation image that represents the physical artwork as faithfully as possible while reducing photo-related issues such as uneven lighting, color exaggeration, glare, visible canvas edges, and over-sharpening.

This workflow supports:

* artwork intake
* artwork documentation
* color correction
* image readiness review
* product-studio handoff
* listing image preparation
* submission image preparation
* future AI-assisted editing support

---

## Core Principle

Edit the photograph to better represent the artwork.

Do not edit the artwork to make it look more dramatic, saturated, polished, or commercially impressive.

The final image should feel:

* accurate
* calm
* clean
* visually faithful
* not over-processed
* ready for downstream workflows

---

## Human + AI Roles

### AI Role

AI may assist with:

* identifying color exaggeration
* suggesting Lightroom adjustments
* detecting lighting issues
* identifying crop and edge problems
* recommending image-specific correction patterns
* flagging when an edit is likely complete
* creating editing notes for the artwork record

AI should not:

* override the artist’s visual judgment
* assume the physical artwork’s true color
* push images toward trend-based aesthetics
* over-brighten or over-saturate the artwork
* crop into the artwork
* remove or alter artwork details
* invent final print readiness details

### Human Role

The owner/artist is responsible for:

* comparing the image against the physical artwork
* confirming color accuracy
* deciding when the edit is complete
* approving the final documentation image
* confirming whether visible edges, shadows, or texture are part of the artwork or photo artifact

Human review is required before image export is treated as approved operational memory.

---

## Required Inputs

Before editing, gather:

* source artwork image
* artwork ID, if assigned
* physical artwork available for comparison, if possible
* intended use of image:

  * documentation
  * print source
  * Etsy listing
  * website listing
  * submission
  * social/content
* known artwork details:

  * medium
  * dimensions
  * orientation
  * presence of gold foil/metallic paint
  * presence and location of signature

---

## Standard Lightroom Base Preset

Apply the standard base preset first:

```text
AOA Artwork Documentation — JPEG Base
```

This preset is the neutral starting point for artwork documentation.

It may include:

* Profile
* Light
* Color
* Effects
* Detail
* Optics

It should not include:

* Crop
* Geometry
* White Balance
* Healing/Remove
* Masking
* Lens Blur
* AI generative edits

---

## Base Editing Logic

After applying the preset, do not adjust every setting by default.

Only correct what the specific image is exaggerating or failing to capture accurately.

Ask:

1. What looks different from the physical artwork?
2. Is the issue global or local?
3. Is this an artwork issue or a photo/lighting issue?
4. Can it be corrected without distorting the painting?
5. Is the full artwork, including signature, still visible?

---

# Image Review Decision System

## 1. Blue-Heavy Coastal Paintings

Use this pattern for paintings with strong blue water, blue sky, coastal horizons, or cool shadows.

### Common Issue

Camera/preset may make blues look too electric, too cool, or too digitally saturated.

### Suggested Adjustments

```text
Blue Saturation: -3 to -8
Blue Luminance: +3 to +6
Aqua Saturation: -3
Highlights: -25 to -40
Exposure: only tiny changes if needed
```

### Watch For

* water becoming too electric
* sky becoming too blue
* shadows losing warmth
* painting feeling colder than the physical piece

### Stop When

The blue still feels like the painting, but not like the camera intensified it.

---

## 2. Gold Foil / Metallic Highlight Paintings

Use this pattern for paintings with gold foil, metallic paint, bright gold horizon lines, sun reflections, or reflective accents.

### Common Issue

Gold foil often photographs as neon yellow, green-yellow, or blown-out highlight.

### Suggested Global Adjustments

```text
Highlights: -35 to -50
Whites: -5 to -10
Yellow Saturation: -8 to -18
Yellow Luminance: -5 to -12
Orange Saturation: -3 to -8
```

### Suggested Local Mask for Bright Gold Areas

Use a Brush Mask if only one area is too bright.

```text
Highlights: -20
Whites: -10 to -15
Saturation: -5
Texture: -5
```

### Watch For

* gold turning neon
* gold becoming green-yellow
* gold becoming dull or gray
* foil overpowering the rest of the painting
* losing the material quality of the original

### Stop When

The gold reads as metallic and present, but not digitally glowing.

### Additional Recommendation

For Etsy, website, or product listings, capture two image types when possible:

1. straight documentation image
2. angled detail image showing foil/metallic reflection intentionally

---

## 3. Pink / Purple Sunset Paintings

Use this pattern for pink skies, lavender water, purple clouds, soft sunset scenes, and dusk paintings.

### Common Issue

Magenta and purple can become too candy-colored or too saturated after the base preset.

### Suggested Adjustments

```text
Magenta Saturation: -5 to -10
Purple Saturation: -3 to -8
Red Saturation: -3 to -6
Highlights: -25 to -35
Whites: -5
Contrast: -5
```

### Watch For

* sky becoming too pink
* water becoming neon lavender
* warm horizon losing its glow
* shadows becoming muddy

### Stop When

The pink/purple atmosphere is still present, but the image feels believable and close to the physical artwork.

---

## 4. Red / Green Architectural or Garden Paintings

Use this pattern for brick buildings, ivy, garden scenes, red/green contrast, or shaded street scenes.

### Common Issue

Red brick and green foliage can become too strong, too contrasty, or too saturated.

### Suggested Adjustments

```text
Red Saturation: -5 to -8
Red Luminance: +3
Green Saturation: -5
Green Luminance: +3 to +5
Yellow Saturation: -3
Shadows: +5 to +10
```

### Watch For

* brick becoming too red
* greenery becoming neon
* shaded scenes becoming too bright
* architectural detail becoming harsh

### Stop When

The piece keeps its shaded atmosphere while remaining clear enough for documentation.

---

## 5. Soft Gray / Misty Atmospheric Paintings

Use this pattern for muted water scenes, gray-blue skies, misty coastal paintings, fog, soft clouds, or quiet light.

### Common Issue

Too much contrast, clarity, or saturation can destroy the softness of the piece.

### Suggested Adjustments

```text
Highlights: -35 to -45
Whites: -5 to -10
Shadows: +5 only
Contrast: -5
Clarity: keep low
Texture: use preset amount or lower
```

### Watch For

* misty atmosphere becoming too sharp
* soft clouds becoming harsh
* foreground becoming over-defined
* muted colors becoming too saturated

### Stop When

The painting remains soft, quiet, and readable.

Do not “fix” softness if softness is part of the artwork.

---

## 6. Uneven Room Lighting / Photo Lighting Issues

Use this pattern when one side of the image is darker, the bottom is brighter, or room lighting is visibly affecting the photo.

### Common Issue

This is a photograph problem, not an artwork color problem.

Do not fix it with global color adjustments.

Use masking.

### Dark Side Correction

Use Masking → Linear Gradient.

```text
Exposure: +0.10 to +0.20
Shadows: +10
Highlights: -5
Saturation: -2
```

### Bright Area Correction

Use a second Linear Gradient if a lower or side area is too bright.

```text
Exposure: -0.05 to -0.15
Highlights: -10 to -20
Whites: -5
```

### Watch For

* overcorrecting one side
* making the painting look flat
* creating visible gradient artifacts
* changing the actual artwork color

### Stop When

The lighting no longer calls attention to itself.

---

## 7. Crop, Geometry, and Artwork Edges

Crop and geometry corrections should protect the integrity of the artwork.

### Core Rules

```text
Full artwork first.
Signature visible.
Do not crop into the artwork.
Crop out photographed background/canvas side only when possible.
Accept slight imperfection over cutting off artwork.
```

### Use Geometry When

* artwork appears tilted
* vertical/horizontal edges are not square
* the photo was taken slightly off-angle

### Use Crop When

* photo background is visible
* canvas side edge is visible
* black border or room edge is visible
* image needs final framing

### Do Not Crop Out

* signature
* painted edges
* intentional marks
* meaningful texture
* parts of the original artwork

### If Straightening Cuts Off the Signature

Prioritize the signature and full artwork over perfect straightness.

Use:

* looser crop
* reduced geometry correction
* Y Offset if useful
* less aggressive straightening

---

## 8. Detail, Texture, Sharpening, and Noise

Artwork photos should preserve brushwork and canvas texture without becoming crunchy.

### Standard Detail Pattern

```text
Sharpening Amount: 35–40
Radius: 1.0
Detail: 20–25
Masking: 50–60
Noise Reduction Luminance: 5
Noise Reduction Color: 15
```

### Watch For

* brushwork becoming harsh
* canvas texture becoming too crunchy
* soft skies becoming noisy
* dark shadows becoming smudged

### Stop When

The artwork feels clear but not digitally sharpened.

---

# Editing Sequence

Use this sequence for every artwork image.

## Step 1 — Apply Base Preset

Apply:

```text
AOA Artwork Documentation — JPEG Base
```

Do not apply additional style presets.

---

## Step 2 — Identify Image Type

Classify the image by dominant editing need:

* blue-heavy coastal
* gold foil / metallic
* pink-purple sunset
* red-green architectural/garden
* soft gray/misty
* uneven lighting
* crop/edge issue

An image may belong to more than one category.

Example:

```text
Pink-purple sunset + uneven left-side lighting
```

---

## Step 3 — Correct Global Color

Use the image-type adjustment pattern.

Keep global adjustments restrained.

Do not adjust colors that already look accurate.

---

## Step 4 — Correct Local Lighting if Needed

Use masks only when the photo has a local lighting issue.

Examples:

* left side darker
* bottom brighter
* gold center flaring
* room light reflection
* uneven exposure across painting

Prefer:

* Linear Gradient for broad lighting issues
* Brush Mask for small bright gold/foil areas

---

## Step 5 — Review Against Physical Artwork

Ask the owner/artist:

```text
Does this match the physical artwork in normal room light?
Is anything too blue, too pink, too yellow, too dark, or too bright?
Does the image feel accurate rather than enhanced?
```

If the physical artwork is not available, mark the edit as:

```text
AI-Assisted Edit — Pending Physical Artwork Comparison
```

---

## Step 6 — Crop and Geometry

Check:

* full artwork visible
* signature visible
* edges clean
* no distracting background
* no canvas side unless intentionally included
* no important painting area cropped out

Do not save crop/geometry into the base preset.

These are image-specific.

---

## Step 7 — Final Stop Check

Before export, confirm:

```text
Color feels accurate
Lighting feels even
No room-light shadow is distracting
Gold/foil is controlled
Blues are not electric
Pinks/purples are not candy-colored
Texture is visible but not harsh
Full artwork is visible
Signature is visible
Edges/crop are clean
```

If all are true, stop editing.

Do not keep adjusting after the image is documentation-ready.

---

# Export Settings

For print/documentation export:

```text
Image Type: JPG
Dimensions: Full Size
Quality: 100%
Color Space: sRGB
Output Sharpening: Matte Paper
Amount: Standard
Metadata: All Metadata
```

Resolution/PPI may not appear in Lightroom when exporting full size.

Full Size is the priority because it preserves the maximum available pixel dimensions.

---

# File Naming Convention

Use the artwork ID as the base file name.

Example:

```text
AOA_ART_0003.jpg
```

If creating multiple image versions:

```text
AOA_ART_0003.jpg
AOA_ART_0003_detail.jpg
AOA_ART_0003_social.jpg
AOA_ART_0003_submission.jpg
```

Preferred documentation image:

```text
AOA_ART_0003.jpg
```

Optional image types:

```text
_detail = angled texture/foil/detail photo
_social = crop or atmospheric version for social
_submission = clean image prepared for application requirements
```

---

# Artwork Record Notes

When editing is complete, add image preparation notes to the artwork intake record.

Suggested field:

```text
Image Editing Notes
```

Suggested structure:

```text
Base preset applied: AOA Artwork Documentation — JPEG Base

Primary correction type:
- [blue-heavy coastal / gold foil / pink-purple sunset / red-green architectural / misty gray / uneven lighting / crop-edge correction]

Adjustments made:
- [summary of key adjustments]

Masking used:
- [none / linear gradient / brush mask]

Crop/geometry notes:
- [full artwork visible / signature visible / crop loosened / canvas edge removed]

Final image status:
- Editing in Progress
- Edit Complete — Pending Review
- Master Image Approved
```

---

# Agent Instructions

When assisting with artwork image editing, the agent should respond as an editing partner, not as a stylist.

The agent should:

1. identify the likely image type
2. name the main risk in the photo
3. suggest restrained Lightroom adjustments
4. tell the owner what not to overcorrect
5. review updated versions and say when to stop
6. prioritize full artwork visibility and accuracy
7. keep human review central

The agent should not:

* suggest extreme edits
* make the image more dramatic for marketing
* prioritize aesthetics over accuracy
* crop into the artwork
* remove signatures
* treat photo artifacts as intentional artwork details without confirmation
* claim print readiness beyond what the file supports

---

# Agent Response Template

Use this structure when reviewing a new artwork image:

```text
This image looks like: [image type]

Main thing to watch:
[short explanation]

After applying the base preset, try:

Light:
- [settings]

Color Mixer:
- [settings]

Masking:
- [only if needed]

Crop/geometry:
- [specific guidance]

Stop when:
- [clear stop condition]
```

Use this structure when reviewing an updated edit:

```text
This is better because:
- [specific observation]

I would adjust only:
- [one or two tiny changes, if needed]

Or:

I would stop here.

Final checks:
- full artwork visible
- signature visible
- color close to physical artwork
- edges/crop clean
```

---

# Workflow Status Values

Use these status values for image editing:

```text
Image Received
Editing in Progress
Edit Complete — Pending Review
Master Image Approved
Image Exported
```

---

# Important Constraints

Do not treat the edited image as approved unless the owner confirms it.

Do not use the master image as a product source if it crops the artwork, cuts off the signature, or contains major lighting distortion.

Do not create product mockups or listing images until the master image is approved.

Do not alter artwork content.

Do not invent color accuracy if the physical artwork was not compared.

---

# Handoff

When editing is complete and the owner has approved the image:

1. Complete the AOA Artwork Image Editing Session Notes template
2. Export the final file from Lightroom using the export settings in this workflow
3. Name the file using the artwork ID convention: `AOA_ART_XXXX.jpg`
4. Set Image Status: `Master Image Approved`
5. Save the approved file to the artwork's working folder

Then:

Begin `AOA-new-artwork-intake_workflow.md` with the approved image as the source.

Do not begin the intake workflow until:

* the owner has confirmed the image against the physical artwork
* Image Status = `Master Image Approved`
* the session notes template is complete
* the exported file is saved and ready

---

# Future Improvement Notes

For better source images, photograph artwork with:

* even indirect light
* no overhead glare
* camera parallel to artwork
* extra space around all four edges
* signature included
* RAW/DNG capture when possible
* gray card or color reference when possible
* separate angled detail photos for metallic/foil pieces

This reduces the amount of correction needed in Lightroom and improves consistency across artwork records.