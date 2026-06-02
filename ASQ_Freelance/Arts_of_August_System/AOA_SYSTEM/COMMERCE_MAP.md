# AOA Commerce Map

## Scope

This file defines the commerce architecture for Arts of August, including transaction processing and print-on-demand fulfillment.

It applies to:

`ASQ_Freelance/Arts_of_August_System/`

Read alongside:

* `AOA_SYSTEM/SYSTEM_MAP.md`
* `AOA_SYSTEM/CHANNEL_MAP.md`
* `AOA_SYSTEM/ICM_RULES.md`

---

## Core Principle

Commerce has two distinct layers: transaction and fulfillment.

Square is the transaction layer.
Printful and Printify are fulfillment providers for print-on-demand products.

Neither Square nor POD providers are product databases or content systems.

---

## Transaction Layer — Square

### Role

Square processes all money movement for Arts of August.

### What Square handles

* original artwork purchase links (online checkout)
* in-person POS at markets, shows, and events
* payment processing and confirmation
* sales receipts

### What Square does not handle

* artwork record storage
* product descriptions or metadata
* content planning
* inventory management for the system
* Lovable data display

### Square operating pattern

1. Artwork is approved and priced in the artwork record.
2. A Square checkout link is generated for the original artwork.
3. The link is placed in the Lovable product page.
4. Customer clicks the link, completes checkout in Square.
5. Sale is logged in `data/sales/sales.csv` after confirmation.

### Square and in-person sales

* Square POS is used for in-person transactions at markets and events.
* Product selection for events is based on approved artwork and product records, not Square catalog.
* In-person sale data should be recorded in `data/sales/sales.csv` after the event.

### Square data tracked

`data/sales/sales.csv`

---

## Print-on-Demand Fulfillment

### Principle

Printful and Printify may both be active POD providers at the same time.

POD provider technical details (product IDs, variant IDs, sync product IDs, pricing) belong in provider-specific maps, not in artwork records.

Artwork records reference the artwork. Provider maps connect artwork to POD product instances.

### Printful

**Role:** POD fulfillment provider.

**What it handles:**

* print fulfillment for approved artwork products
* product variants (size, substrate, framing options)
* order routing when a sale triggers a POD fulfillment

**Data map:** `data/pod/printful-map.csv`

**Operating pattern:**

1. Artwork is approved and ready for products.
2. Printful product is created using the approved artwork image.
3. Printful product ID and variant IDs are logged in `data/pod/printful-map.csv`.
4. Product is connected to the Lovable shop or Etsy listing.
5. Customer orders route to Printful for fulfillment.

### Printify

**Role:** Alternative or concurrent POD fulfillment provider.

**What it handles:**

* print fulfillment for approved artwork products
* may be used for specific product types or price points
* product variants per Printify catalog

**Data map:** `data/pod/printify-map.csv`

**Operating pattern:**

Same as Printful. The provider map distinguishes which products route to which provider.

### POD Rules

1. Both Printful and Printify may be active simultaneously.
2. POD technical details (product IDs, variant IDs) belong only in provider maps, not artwork CSV records.
3. Artwork records do not need POD fields. The relationship is maintained in `data/pod/`.
4. A new POD product requires an approved artwork image and an approved product record before setup.
5. POD product publish requires human approval.

---

## Commerce Data Files

| File | Purpose |
|------|---------|
| `data/sales/sales.csv` | All sales transactions (online + in-person) |
| `data/pod/printful-map.csv` | Artwork-to-Printful product mapping |
| `data/pod/printify-map.csv` | Artwork-to-Printify product mapping |

---

## Commerce Rules Summary

1. Square is the transaction layer. It is not the product database or content system.
2. Square handles original artwork online checkout and in-person POS.
3. Printful and Printify are fulfillment providers, not artwork databases.
4. POD provider details live in provider maps, not artwork records.
5. All commerce decisions (pricing, availability, product launch) require human approval.
6. Sales data is recorded in `data/sales/sales.csv` after confirmation.
