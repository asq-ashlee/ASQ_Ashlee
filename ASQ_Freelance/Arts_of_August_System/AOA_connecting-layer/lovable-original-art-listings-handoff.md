# Lovable Handoff - Original Art Listings

Status: draft for Lovable setup
Source system: Arts of August
Website: artsofaugust.org
Platform: Lovable, React/TypeScript

---

## Goal

Set up original artwork listings on the Arts of August website using approved artwork records only.

Lovable is the public display layer. It should display approved system data and send purchases to Square checkout links. It should not become the source of truth for artwork metadata, pricing, inventory, images, or checkout status.

---

## Source of Truth

Approved artwork data originates in Notion and is mirrored in:

`AOA_datasets/artworks/artworks.csv`

Field definitions are documented in:

`AOA_datasets/artworks/artworks.schema.md`

Website-specific rules are documented in:

`AOA_distribution-studio/platform-notes/website.md`

---

## Lovable Project Structure

The website should use:

- `src/data/artworks.ts` for artwork data
- `src/assets/` for local web-ready artwork images

The site should not fetch from Notion at runtime. Updates happen through a manual sync process that pulls approved Notion data and real artwork images into the Lovable project.

---

## Required Listing Fields

Each original artwork listing should support these fields:

| Website field | Source field |
|---|---|
| Stable ID | `artwork_id` |
| Title | `Title` |
| URL slug | `Slug` |
| Image | downloaded from `Image`, saved in `src/assets/` |
| Alt text | `Alt_Text` |
| Status | `Status` |
| Original availability | `Original_Available` |
| Price | `Base_Price` |
| Dimensions | `Size` |
| Medium | `Medium` |
| Support | `Support` |
| Category | `Category` |
| Description | `Description` |
| Short story/hook | `Story` |
| Subject | `Subject` |
| Location | `Location` |
| Time of day | `Time_of_Day` |
| Light description | `Light_Description` |
| Tags | `Tags` |
| Mood | `Mood` |
| Colors | `Colors` |
| Square checkout link | Notion `Square Checkout URL` |

The artwork `Title` must be the clean display title only, such as `Rose Tide`. Do not use long SEO marketplace titles as the site title.

---

## Publishing Gate

Do not display an artwork on the website unless all of the following are true:

- `Image_Status` is `Master Image Approved`
- `Human_Approved` is `yes`
- `Status` is `available` or `coming-soon`
- `Description` is approved, not an AI draft
- `Story` is approved, not an AI draft
- `Base_Price` is confirmed if the original is for sale
- `Image` points to a real approved artwork photograph
- The image has been downloaded and saved to `src/assets/`
- The artwork data has been committed to the Arts of August dataset
- `Square Checkout URL` is populated when `Status` is `available`

If any required data is missing, show nothing for that artwork and flag it for review.

---

## Image Rules

Never generate, substitute, or use AI artwork images as placeholders.

Every displayed artwork must have a real approved photograph. Do not add an entry to `src/data/artworks.ts` unless the matching image file exists in `src/assets/`.

Recommended file convention:

`[artwork-id]-[title-slug]-web.[ext]`

Example:

`AOA-ART-0062-rose-tide-web.jpg`

---

## Purchase Behavior

The website does not process transactions directly.

For available original artwork:

- Show the price from `Base_Price`
- Show a purchase button only when `Square Checkout URL` exists
- The purchase button should link out to Square

For coming-soon artwork:

- Do not require a Square link
- Use non-purchase language such as `Coming soon`

For sold or unavailable artwork:

- Do not show an active purchase button
- Display the status clearly

---

## Suggested TypeScript Shape

```ts
export type Artwork = {
  artworkId: string;
  title: string;
  slug: string;
  status: "available" | "coming-soon" | "sold" | "not-for-sale";
  originalAvailable: boolean;
  price?: number;
  dimensions: string;
  medium: string;
  support?: string;
  category?: string;
  imageSrc: string;
  altText: string;
  description: string;
  story: string;
  subject?: string;
  location?: string;
  timeOfDay?: string;
  lightDescription?: string;
  tags?: string[];
  mood?: string[];
  colors?: string[];
  squareCheckoutUrl?: string;
};
```

---

## Gallery Card Display

Each listing card should show:

- artwork image
- title
- story
- dimensions
- medium
- price when available
- availability/status

The card can link to a detail page using `Slug`.

---

## Detail Page Display

Each artwork detail page should show:

- large real artwork image
- title
- story
- description
- dimensions, medium, support
- category, subject, location, light description where available
- price
- Square purchase button if available

Use `Alt_Text` for the image alt attribute. Do not replace alt text with story copy.

---

## Copy Rules

Description and story are different:

- `Description` is the longer human-facing listing copy
- `Story` is a short lyrical note or hook
- `Alt_Text` is literal, descriptive, and accessibility/search oriented

Do not mix these fields.

---

## Paste-Ready Lovable Instruction

Use the Arts of August approved artwork dataset to build original art listing support. Treat Lovable as the public display layer only. Artwork data should live in `src/data/artworks.ts`, images should live in `src/assets/`, and each displayed artwork must come from an approved Notion/dataset record with a real approved photograph.

Create a gallery and detail-page data model for original artworks using the fields listed in this handoff. Display image, title, story, dimensions, medium, price, status, and a Square checkout button when an artwork is available and has a `Square Checkout URL`. Do not process payments on the website. Do not generate or use placeholder artwork images. Do not manually invent metadata, prices, availability, or checkout links. If required fields are missing, exclude the artwork and flag it for review.

---

## Existing Reference Docs

- `AOA_distribution-studio/platform-notes/website.md`
- `AOA_datasets/artworks/artworks.schema.md`
- `AOA_SYSTEM/NOTION_OPERATING_SCHEMA.md`
- `AOA_connecting-layer/post-approval-handoff.md`
- `AOA_SYSTEM/COMMERCE_MAP.md`
- `AOA_source-intelligence/04-Listing-System.txt`
