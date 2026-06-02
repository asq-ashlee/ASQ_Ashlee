# AOA Channel Map

## Scope

This file maps the distribution and sales channels used by Arts of August and defines the role of each.

It applies to:

`ASQ_Freelance/Arts_of_August_System/`

Read alongside:

* `AOA_SYSTEM/SYSTEM_MAP.md`
* `AOA_SYSTEM/COMMERCE_MAP.md`
* `AOA_SYSTEM/ICM_RULES.md`

---

## Core Principle

The repo holds the source records. Channels display or distribute approved outputs.

No channel is the source of truth. No channel receives unapproved content.

---

## Owned Channels

### Lovable — Owned Storefront

**Role:** Public-facing storefront and customer chatbot.

**What it displays:**

* approved artwork records (title, description, price, image, availability)
* approved product listings
* shop pages
* artist landing pages
* collection or theme pages

**Customer chatbot:**

* reads only approved public JSON or structured data
* does not have access to internal records, pricing history, or draft content
* chatbot responses are generated from approved data only

**Publishing rules:**

* all Lovable content requires human approval before going live
* Lovable data source is approved public JSON pushed from the repo
* Lovable is not used to store or edit records

**Data source:** `data/` folder structured records (approved outputs)

---

### Kit — Email List

**Role:** Direct email channel to collectors and subscribers.

**What it sends:**

* new artwork announcements
* event invitations
* collection previews
* studio notes and artist emails

**Data tracked:** `data/channels/kit-email.csv`

**Publishing rules:**

* all emails require Kaleigh approval before send
* email content is drafted from approved artwork records
* Kit is not the source of truth for artwork or event records

---

## Marketplace Channels

### Etsy

**Role:** Marketplace channel. Optional. Preserved from prior system.

**What it handles:**

* marketplace product listings
* discovery via Etsy search
* print or original sales via Etsy platform

**Relationship to repo:**

* Etsy listings are generated from approved artwork and product records
* Etsy is not the source of truth
* Etsy-specific fields are tracked in existing Etsy import files

**Data file:** `AOA_datasets/artworks/art-pieces-etsy-import.csv`

**Note:** Etsy is not required in the core publishing path. It is an optional marketplace layer.

---

## Social Channels

### Instagram

**Role:** Primary visual social channel.

**What it distributes:**

* artwork reveals
* studio content
* event promotion
* collection previews
* behind-the-scenes content

**Platform notes:** `AOA_distribution-studio/platform-notes/instagram.md`

**Publishing rules:**

* content drafted from approved artwork records and artist voice context
* Kaleigh approves before posting

---

### Facebook

**Role:** Secondary social channel.

**What it distributes:**

* event promotion
* artwork announcements
* community and show updates

**Platform notes:** `AOA_distribution-studio/platform-notes/facebook.md`

**Publishing rules:**

* content drafted from approved content items
* Kaleigh approves before posting

---

## Commerce Channels

### Square — Online and In-Person

**Role:** Transaction layer.

**What it handles:**

* original artwork checkout links (online)
* in-person POS at markets and events
* payment confirmation

**Note:** Square is a channel for completing purchases. It is not a product database or content system.

See: `AOA_SYSTEM/COMMERCE_MAP.md`

---

## Channel Rules

1. Channels display or distribute approved outputs. They do not define records.
2. No channel receives content that has not been reviewed and approved.
3. Lovable and Kit are the primary owned-channel surfaces.
4. Etsy is preserved and optional.
5. Square is the transaction endpoint, not a channel for discovery or content.
6. Social channels are distribution surfaces, not record storage.
7. Channel-specific performance data is tracked in `data/channels/` and `data/sales/`.
