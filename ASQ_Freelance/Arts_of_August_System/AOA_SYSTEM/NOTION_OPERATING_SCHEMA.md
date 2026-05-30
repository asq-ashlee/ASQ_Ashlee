# AOA Notion Operating Schema

## Scope

This file defines the operating schema for the Arts of August Notion system.

It applies to:

`ASQ_Freelance/Arts_of_August_System/`

This file should be read alongside:

* `AOA_SYSTEM/ICM_RULES.md`
* `AOA_SYSTEM/TOOL_MAP.md`
* `AOA_SYSTEM/POC_DEFINITION_OF_DONE.md`

## Purpose

The Arts of August Notion system is the live operational database for managing the artist business.

It supports:

* artwork inventory
* original artwork sales
* print/product records
* website publishing
* content planning
* event planning
* opportunity tracking
* gallery and application follow-up
* AI-assisted reuse of approved context

The goal is not only to support the proof of concept.

The goal is to create a real operating backbone that Arts of August can use now, while also providing proof that the same system can be adapted for other artists.

## Core Source-of-Truth Rule

Markdown explains how the system works.

Notion stores the live business records.

Lovable displays approved public outputs.

AI tools draft, structure, review, and assist — but humans approve public-facing meaning, price, representation, and publication.

---

# Database Overview

The Arts of August Notion system should use five primary databases:

1. Art Pieces
2. Products
3. Content
4. Events
5. Opportunities

## Database Relationship Model

```text
Art Pieces
  ↓
Products
  ↓
Shop / Etsy / Square / Lovable

Art Pieces
  ↓
Content

Events
  ↓
Content

Opportunities
  ↓
Events, if accepted or confirmed

Art Pieces
  ↓
Events, if artwork is shown or sold at an event

Products
  ↓
Events, if prints/products are brought to an event
```

---

# 1. Art Pieces Database

## Purpose

The Art Pieces database is the source of truth for original artworks.

Each record represents one original work by Kaleigh Anderson / Arts of August.

This database supports:

* artwork inventory
* original availability
* original pricing
* artwork documentation
* website shop/detail pages
* AI-readable artwork context
* SEO/GEO-ready descriptions
* content generation
* event inventory planning
* opportunity/application materials

## What belongs here

Use Art Pieces for:

* original artwork identity
* stable artwork ID
* public display title
* artwork story
* original price
* original availability
* master image status
* artist-approved description
* artwork-level alt text
* medium, dimensions, subject, mood, color, location
* Square checkout link for the original
* relations to Products, Content, Events, and Opportunities

## What does not belong here

Do not use Art Pieces for:

* every print size or variant
* Etsy listing variants
* Printful product details
* mockup-specific metadata
* event-specific inventory notes
* content draft statuses unrelated to the artwork
* long workflow instructions

Those belong in Products, Events, Content, or markdown.

## Required fields

| Field                | Property Type        | Notes                                                                                                    |
| -------------------- | -------------------- | -------------------------------------------------------------------------------------------------------- |
| Title                | Title                | Public display title.                                                                                    |
| artwork_id           | Text                 | Stable ID, such as `AOA-ART-0001`. Never change once assigned.                                           |
| Slug                 | Text                 | URL-safe slug for website detail page.                                                                   |
| Status               | Select               | Public-facing status: `available`, `sold`, `commission`, `coming-soon`, `not-for-sale`.                  |
| Workflow Status      | Select               | Internal operating stage. Separate from public status.                                                   |
| Human Approved       | Checkbox             | Required before website/public sync.                                                                     |
| AI Draft Complete    | Checkbox             | Indicates AI-generated context has been drafted.                                                         |
| Image Status         | Select               | Master image workflow status.                                                                            |
| Image                | URL or Files & Media | Approved master image reference. Use the current Google Drive architecture unless intentionally changed. |
| Medium               | Select               | Example: `Oil on canvas`.                                                                                |
| Dimensions           | Text                 | Example: `20" × 20"`.                                                                                    |
| Orientation          | Select               | `landscape`, `portrait`, `square`.                                                                       |
| Price (Original)     | Number               | Raw number. Currency formatting is fine if stored as number.                                             |
| Original Available   | Checkbox             | Operational indicator. Should align with Status.                                                         |
| Square Checkout URL  | URL                  | Original artwork purchase link. Belongs here, not Products.                                              |
| Description          | Text / Rich Text     | Full public description.                                                                                 |
| Story                | Text                 | Short sensory or narrative hook.                                                                         |
| Alt Text             | Text                 | Literal image description for accessibility, SEO, and AI readability.                                    |
| Tags                 | Multi-select         | Search/filter/context tags.                                                                              |
| Mood                 | Multi-select or Text | Atmosphere/context.                                                                                      |
| Colors               | Multi-select or Text | Useful for search, content, and filtering.                                                               |
| Subject              | Text                 | What the painting depicts.                                                                               |
| Location             | Text                 | Place or inspiration location, if known.                                                                 |
| Time of Day          | Select or Text       | Example: morning, afternoon, dusk, evening.                                                              |
| Light Description    | Text                 | How the light appears in the work.                                                                       |
| Series               | Select               | Use Select for now. Promote to a Series database only if needed later.                                   |
| Display Order        | Number               | Optional manual sort for website.                                                                        |
| Products Linked      | Relation             | Relation to Products database.                                                                           |
| Content Linked       | Relation             | Relation to Content database.                                                                            |
| Events Linked        | Relation             | Relation to Events database.                                                                             |
| Opportunities Linked | Relation             | Relation to Opportunities database, when submitted or referenced.                                        |
| Next Action          | Text                 | What needs to happen next.                                                                               |
| Needs Review         | Checkbox             | Used for Ashlee/Kaleigh cleanup queue.                                                                   |
| POC Candidate        | Checkbox             | Marks records used in proof of concept.                                                                  |
| POC Role             | Select               | `Primary POC Artwork`, `Supporting Example`, `Not in POC`.                                               |

## Recommended select values

### Status

* available
* sold
* commission
* coming-soon
* not-for-sale

### Workflow Status

* Intake Needed
* Drafted
* Needs Image Review
* Needs Artist Review
* Ready for Products
* Ready for Shop
* Ready for Content
* Live
* Archived

### Image Status

* Image Needed
* Image Received
* Editing in Progress
* Edit Complete — Pending Review
* Master Image Approved
* Image Exported

## Readiness rules

### Artwork is intake-ready when

* artwork_id exists
* title exists
* medium exists
* dimensions exist
* image exists or image status is clear
* price/status decision is known
* enough context exists to draft description and alt text

### Artwork is shop-ready when

* Status is `available` or `coming-soon`
* Human Approved is checked
* Image Status is `Master Image Approved`
* Slug is populated
* Alt Text is populated
* Description and Story are populated
* Medium and Dimensions are populated
* Price is populated if available for sale
* Square Checkout URL is populated if purchase is enabled

### Artwork is content-ready when

* Human Approved is checked
* Story or Description is populated
* Alt Text or Subject is populated
* Image is approved
* Content angle is clear enough to draft from

---

# 2. Products Database

## Purpose

The Products database is the source of truth for sellable product versions connected to an artwork.

Products may include:

* canvas prints
* framed prints
* print sizes
* Etsy products
* Printful variants
* product mockups
* product-specific sales channels

## What belongs here

Use Products for:

* print/product variants
* Etsy listing URLs
* Printful records
* format, size, frame, product type
* channel-specific status
* product-level pricing
* product mockups
* product production notes

## What does not belong here

Do not use Products for:

* original artwork identity
* original artwork story
* original Square checkout link
* artwork-level alt text
* artwork-level medium
* public original availability

Those belong in Art Pieces.

## Required fields

| Field               | Property Type        | Notes                                                                    |
| ------------------- | -------------------- | ------------------------------------------------------------------------ |
| Product Name        | Title                | Product/listing name.                                                    |
| product_id          | Text                 | Stable product ID if used.                                               |
| Source Artwork      | Relation             | Relation to Art Pieces.                                                  |
| artwork_id          | Rollup or Text       | Pull from related Art Piece if possible.                                 |
| Product Type        | Select               | Original, Canvas Print, Framed Print, Paper Print, Card, Digital, Other. |
| Format              | Select               | Canvas, framed canvas, paper, etc.                                       |
| Size                | Text                 | Example: `16" × 20"`.                                                    |
| Price               | Number               | Product price.                                                           |
| Sales Channels      | Multi-select         | Etsy, Printful, Lovable, Square, In-person, Other.                       |
| Etsy URL            | URL                  | Product/listing URL for prints or marketplace listing.                   |
| Printful URL / ID   | URL or Text          | If applicable.                                                           |
| Product Status      | Select               | Operational product status.                                              |
| Etsy Status         | Select               | If imported from Etsy or actively managed there.                         |
| Mockup Status       | Select               | Tracks whether product visuals are ready.                                |
| Primary Mockup File | URL or Files & Media | Approved product visual.                                                 |
| Lovable Status      | Select               | Whether this product should appear on website.                           |
| Notes               | Text                 | Product-specific notes.                                                  |
| Next Action         | Text                 | Next operational step.                                                   |
| POC Product         | Checkbox             | Used for POC filtering.                                                  |

## Recommended select values

### Product Status

* Draft
* Needs Artwork Link
* Needs Mockup
* Needs Listing Copy
* Ready for Review
* Active
* Paused
* Archived

### Mockup Status

* Not Needed
* Needed
* In Progress
* Approved
* Needs Replacement

### Lovable Status

* Not Used
* Ready for Website
* Live
* Hidden
* Needs Review

## Readiness rules

### Product is Etsy-ready when

* Product Name exists
* Source Artwork relation exists
* Product Type exists
* Price exists
* Mockup or listing image exists
* Etsy URL is populated after publication

### Product is website-ready when

* Source Artwork relation exists
* related Art Piece is approved
* Product Status is Active or Ready for Website
* Mockup is approved if displayed
* sales channel is clear

---

# 3. Content Database

## Purpose

The Content database is the output planning layer.

It stores reusable drafts and published content generated from:

* Art Pieces
* Products
* Events
* Opportunities
* artist/process/brand context

## What belongs here

Use Content for:

* Instagram captions
* Facebook posts
* email copy
* website blurbs
* event promotion copy
* product/story snippets
* artist process posts
* gallery/application support language
* performance notes

## What does not belong here

Do not use Content for:

* full artwork source records
* product inventory
* event logistics
* opportunity requirements
* system instructions

Those belong in the related databases or markdown.

## Required fields

| Field             | Property Type | Notes                                                                                                  |
| ----------------- | ------------- | ------------------------------------------------------------------------------------------------------ |
| Name              | Title         | Internal content item name.                                                                            |
| Title             | Text          | Public or draft content title/headline.                                                                |
| Source Type       | Select        | Artwork, Product, Event, Opportunity, Brand, Process.                                                  |
| Art Piece         | Relation      | Optional relation to Art Pieces.                                                                       |
| Product           | Relation      | Optional relation to Products.                                                                         |
| Event             | Relation      | Optional relation to Events.                                                                           |
| Opportunity       | Relation      | Optional relation to Opportunities.                                                                    |
| Platform          | Select        | Instagram, Facebook, Email, Website, Etsy, LinkedIn, Other.                                            |
| Content Type      | Select        | Caption, Reel Prompt, Email, Story, Website Copy, Event Blurb, Application Draft, Other.               |
| Content Goal      | Select        | Awareness, Shop Click, Event Promo, Artist Story, Application Support, Collector Trust, Process Proof. |
| Hook              | Text          | Opening angle.                                                                                         |
| Caption / Copy    | Rich Text     | Draft or final copy.                                                                                   |
| CTA               | Text          | Call to action.                                                                                        |
| Status            | Select        | Workflow status.                                                                                       |
| Review Owner      | Select        | Ashlee, Kaleigh, Both.                                                                                 |
| Approved          | Checkbox      | Required before publishing.                                                                            |
| Scheduled Date    | Date          | Optional.                                                                                              |
| Published Date    | Date          | Optional.                                                                                              |
| Published URL     | URL           | Link after publication.                                                                                |
| Performance Notes | Text          | Post-publish learning.                                                                                 |
| Repurpose Later   | Checkbox      | Useful reuse marker.                                                                                   |

## Recommended select values

### Status

* Idea
* Draft Needed
* Drafted
* Needs Review
* Approved
* Scheduled
* Published
* Repurpose Later
* Archived

## Readiness rules

### Content is publish-ready when

* Caption / Copy is complete
* Platform is selected
* CTA is clear
* source record is linked, if applicable
* Approved is checked
* Kaleigh has approved artistic representation if artwork-specific

---

# 4. Events Database

## Purpose

The Events database is the source of truth for confirmed public appearances and show history.

It should include both:

* upcoming events
* past shows / where-shown history

Status determines where and how an event appears on the website.

## What belongs here

Use Events for:

* markets
* art walks
* gallery shows
* exhibits
* public displays
* open studios
* workshops
* pop-ups
* confirmed fairs
* past show history
* event logistics
* event promotion
* post-event notes

## What does not belong here

Do not use Events for:

* unconfirmed applications
* opportunities still being considered
* marketplace research
* generic marketing strategy
* artwork records

Unconfirmed applications belong in Opportunities.

## Required fields

| Field                | Property Type        | Notes                                                                          |
| -------------------- | -------------------- | ------------------------------------------------------------------------------ |
| Title                | Title                | Public event name.                                                             |
| Slug                 | Text                 | Stable URL-friendly ID.                                                        |
| Status               | Select               | Upcoming, Past, Draft, Cancelled, Postponed.                                   |
| Type                 | Select               | show, first-friday, market, workshop, display, open-studio, popup, commission. |
| Start date           | Date                 | Include time when known.                                                       |
| End date             | Date                 | Optional; use for multi-day events.                                            |
| Timezone             | Select               | Default `America/New_York`.                                                    |
| Venue name           | Text                 | Event venue.                                                                   |
| Street address       | Text                 | For local SEO/maps if known.                                                   |
| City                 | Text                 | City.                                                                          |
| State                | Select               | Default `ME`.                                                                  |
| Postal code          | Text                 | ZIP/postal code.                                                               |
| Country              | Select               | Default `US`.                                                                  |
| Latitude             | Number               | For map/structured data.                                                       |
| Longitude            | Number               | For map/structured data.                                                       |
| Short description    | Text                 | 1–2 sentence preview.                                                          |
| Long description     | Rich Text            | Detail page/event story.                                                       |
| Hero image           | Files & Media or URL | One primary event image/flyer.                                                 |
| Hero image alt text  | Text                 | Accessibility/SEO description.                                                 |
| RSVP / external link | URL                  | Facebook, Eventbrite, venue page, etc.                                         |
| Featured             | Checkbox             | Pin/highlight upcoming event.                                                  |
| Ticket price         | Text                 | Free, $25, etc.                                                                |
| Ticket URL           | URL                  | If different from RSVP.                                                        |
| Map URL              | URL                  | Google Maps or venue map link.                                                 |
| Art Pieces Shown     | Relation             | Relation to Art Pieces.                                                        |
| Products Available   | Relation             | Relation to Products.                                                          |
| Content Linked       | Relation             | Relation to Content.                                                           |
| Source Opportunity   | Relation             | Relation to Opportunities, if applicable.                                      |
| Inventory Plan       | Rich Text            | What is going to the event.                                                    |
| Booth Fee            | Number               | If applicable.                                                                 |
| Booth / Site Number  | Text                 | Example: site 93.                                                              |
| Load-in Time         | Date                 | If known.                                                                      |
| Load-out Time        | Date                 | If known.                                                                      |
| Co-exhibitor(s)      | Text                 | Example: Susan Roux.                                                           |
| Contact Name         | Text                 | Organizer/contact.                                                             |
| Contact Email        | Email                | Organizer/contact email.                                                       |
| Contact Phone        | Phone                | Organizer/contact phone.                                                       |
| Notes                | Rich Text            | Internal notes.                                                                |
| Outcome Notes        | Rich Text            | Post-event sales, feedback, learnings.                                         |

## Marketing / SEO fields

| Field            | Property Type        | Notes                                  |
| ---------------- | -------------------- | -------------------------------------- |
| SEO Title        | Text                 | Optional override.                     |
| Meta Description | Text                 | Optional search snippet.               |
| OG Image         | Files & Media or URL | Defaults to Hero image if blank.       |
| Canonical URL    | URL                  | If event primarily lives elsewhere.    |
| Keywords         | Multi-select         | Search/GEO taxonomy.                   |
| Region Code      | Text                 | Example: `US-ME`.                      |
| Place Name       | Text                 | Example: Portland, Maine.              |
| Service Area     | Multi-select         | Greater Portland, Midcoast Maine, etc. |

## Social / email workflow fields

| Field                | Property Type | Notes                                            |
| -------------------- | ------------- | ------------------------------------------------ |
| Announce Date        | Date          | First planned post/send.                         |
| Last Shared          | Date          | Last promotion date.                             |
| Channels Posted      | Multi-select  | Instagram, Facebook, Email list, Etsy, LinkedIn. |
| Facebook Groups      | Multi-select  | Optional.                                        |
| Email Broadcast Sent | Checkbox      | Track event email.                               |
| Social Copy — Short  | Text          | Short caption.                                   |
| Social Copy — Long   | Rich Text     | Newsletter/email version.                        |
| Hashtags             | Text          | Reusable tag set.                                |

## Recommended views

* Upcoming Calendar
* Upcoming List
* Past Shows
* Drafts
* Needs Hero Image
* Ready to Share
* Needs Inventory Plan
* Featured on Website
* Post-Event Follow-Up

## Readiness rules

### Event is website-ready when

* Status is Upcoming or Past
* Title exists
* Slug exists
* Start date exists, or historical month/date is clear
* Venue name and location exist
* Short description exists
* Type is selected
* Draft/Cancelled events are excluded from website display

### Event is promotion-ready when

* Short description exists
* RSVP or external link exists if applicable
* Hero image exists if needed
* Social Copy — Short is populated
* Announce Date is set
* Inventory plan is started if sales are involved

---

# 5. Opportunities Database

## Purpose

The Opportunities database is the source of truth for leads, applications, calls, certifications, marketplaces, gallery opportunities, press, and partnerships.

Opportunities are not automatically public events.

An opportunity may become an Event if accepted, confirmed, scheduled, or shown publicly.

## What belongs here

Use Opportunities for:

* gallery applications
* juried shows
* public art submissions
* calls for art
* market applications
* certifications
* curated marketplaces
* press opportunities
* retail/wholesale leads
* partnership ideas
* grants
* follow-ups
* waitlists
* acceptance outcomes

## What does not belong here

Do not use Opportunities for:

* confirmed event logistics after acceptance
* final event promotion
* artwork inventory
* product variant records
* generic strategic essays

Confirmed logistics belong in Events. Strategy belongs in markdown.

## Required fields

| Field                        | Property Type | Notes                                                                                                                |
| ---------------------------- | ------------- | -------------------------------------------------------------------------------------------------------------------- |
| Opportunity Name             | Title         | Name of opportunity.                                                                                                 |
| Opportunity Type             | Select        | Gallery, Juried Show, Market, Public Art, Certification, Marketplace, Press, Partnership, Grant, Retail / Wholesale. |
| Status                       | Select        | Researching, Considering, Applied, Accepted, Waitlisted, Declined, Completed, Archived.                              |
| Organization                 | Text          | Host/organization.                                                                                                   |
| Contact Name                 | Text          | Primary contact.                                                                                                     |
| Contact Email                | Email         | Contact email.                                                                                                       |
| Contact Phone                | Phone         | Optional.                                                                                                            |
| Website / Application URL    | URL           | Application or info link.                                                                                            |
| Deadline                     | Date          | Application or response deadline.                                                                                    |
| Event / Show Date            | Date          | If known.                                                                                                            |
| Location                     | Text          | City/venue/region.                                                                                                   |
| Fee                          | Number        | Application/booth/entry fee.                                                                                         |
| Commission %                 | Number        | If sales commission applies.                                                                                         |
| Requirements                 | Rich Text     | Submission rules, image specs, materials, contract notes.                                                            |
| Application Materials Needed | Multi-select  | Bio, artist statement, images, W9, inventory list, price list, contract, payment, other.                             |
| Submitted Artworks           | Relation      | Relation to Art Pieces.                                                                                              |
| Related Products             | Relation      | Optional relation to Products.                                                                                       |
| Related Event                | Relation      | Relation to Events if opportunity becomes confirmed.                                                                 |
| Application Draft            | Rich Text     | Draft outreach/submission copy.                                                                                      |
| Submission Date              | Date          | When application was submitted.                                                                                      |
| Outcome Date                 | Date          | When result was received or expected.                                                                                |
| Outcome Notes                | Rich Text     | Accepted, waitlisted, declined, selected pieces, stipend, site number, etc.                                          |
| Follow-Up Date               | Date          | Next reminder/follow-up.                                                                                             |
| Fit Score                    | Number        | Optional 1–10 score.                                                                                                 |
| Strategic Value              | Multi-select  | Local exposure, collector access, credibility, sales, SEO/GEO, press, portfolio history.                             |
| Next Action                  | Text          | Immediate next step.                                                                                                 |
| Source                       | Select        | Email, Gemini, Lovable, Web Research, Referral, Instagram, Existing Relationship, Other.                             |
| Source File / Email          | URL or Text   | Reference to source material when useful.                                                                            |

## Recommended select values

### Opportunity Type

* Gallery
* Juried Show
* Market
* Public Art
* Certification
* Marketplace
* Press
* Partnership
* Grant
* Retail / Wholesale
* Other

### Status

* Researching
* Considering
* Applied
* Accepted
* Waitlisted
* Declined
* Completed
* Archived

### Strategic Value

* Local Exposure
* Collector Access
* Credibility
* Sales Potential
* Press Potential
* Website/GEO Value
* Portfolio History
* Relationship Building
* Seasonal Fit
* High Effort / Low Return

## Readiness rules

### Opportunity is application-ready when

* deadline is known
* application URL or contact exists
* requirements are documented
* submitted artworks are selected or criteria are clear
* application materials are listed
* Kaleigh approves the submitted artwork choices
* Ashlee or Kaleigh approves the final application copy

### Opportunity becomes event-ready when

* accepted or confirmed
* date/location are known
* public display or participation is scheduled
* enough detail exists to create an Event record

---

# Operating Views

## Art Pieces views

* All Art Pieces
* Intake Needed
* Needs Master Image
* Needs Artist Review
* Ready for Products
* Ready for Shop
* Ready for Content
* Website Ready
* POC Candidates
* Live Originals
* Sold / Archived

## Products views

* All Products
* Needs Artwork Link
* Needs Mockup
* Etsy Active
* Printful Products
* Website Products
* POC Products
* Needs Review
* Archived

## Content views

* Ideas
* Draft Needed
* Drafted
* Needs Kaleigh Review
* Approved
* Scheduled
* Published
* Repurpose Later

## Events views

* Upcoming Calendar
* Upcoming List
* Past Shows
* Drafts
* Needs Hero Image
* Ready to Share
* Needs Inventory Plan
* Post-Event Follow-Up

## Opportunities views

* Researching
* Considering
* Applied
* Accepted
* Waitlisted
* Follow Up Needed
* Deadlines This Month
* Accepted — Create Event
* Completed / Archived

---

# POC Use

The POC should be a filtered layer inside the full operating system.

Do not create separate demo-only databases.

Use fields like:

* `POC Candidate`
* `POC Product`
* `POC Role`
* `Featured`
* `Website Ready`

The POC should prove that selected records can move through the full loop:

```text
Artwork → Product → Shop/Website → Content → Event/Opportunity support
```

The first POC should use a small number of polished records, while the larger Notion system continues to support the full Arts of August business.

---

# AI Usage Rules

AI may help:

* generate slugs
* draft alt text
* draft artwork descriptions
* summarize event records
* draft social/email copy
* extract requirements from opportunity emails
* identify missing fields
* recommend readiness status
* create application drafts
* generate website-ready blurbs

AI should not:

* finalize prices
* mark artwork sold
* publish to website
* submit applications
* contact venues or galleries
* invent physical artwork details
* claim color or image accuracy without human approval
* guess event logistics not present in source material

Human approval is required for:

* artwork representation
* price
* final public copy
* shop publication
* event publication
* opportunity submission
* application materials
* partner/gallery outreach

---

# Migration Priorities

## Priority 1 — Stabilize existing databases

* Clean up Art Pieces field names and statuses.
* Confirm original/Square fields live on Art Pieces.
* Confirm Etsy/Printful fields live on Products.
* Add readiness fields and key views.
* Update Content schema so it can relate to Art Pieces, Products, Events, and Opportunities.

## Priority 2 — Create Events database

* Create unified Events database.
* Migrate current upcoming website events.
* Migrate past show history.
* Add views for upcoming, past, ready to share, and needs follow-up.

## Priority 3 — Create Opportunities database

* Add current known opportunities.
* Add submitted/accepted/waitlisted opportunities from email records.
* Link submitted artworks where known.
* Add follow-up dates and next actions.

## Priority 4 — Select POC records

* Choose 3–5 Art Pieces.
* Link Products.
* Create Content examples.
* Connect at least one Event and one Opportunity.
* Use these records to demonstrate the system.

---

# Operating Standard

One record should become many outputs.

One artwork can become:

* original listing
* print products
* website page
* social post
* email blurb
* event inventory item
* gallery submission example
* provenance/process proof

One event can become:

* event page
* local SEO/GEO object
* social promotion
* email reminder
* inventory plan
* post-event history

One opportunity can become:

* application draft
* required materials checklist
* submitted artwork list
* follow-up reminder
* confirmed event
* portfolio credibility signal

Build the context once.

Reuse it carefully.

Keep records clean.

Let AI draft.

Let humans approve.

Store the learning where it can be found again.
