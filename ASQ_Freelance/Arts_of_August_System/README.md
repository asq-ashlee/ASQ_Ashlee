# Arts of August System

The Arts of August system turns an artist's body of work into structured, reusable sales and marketing infrastructure.

The repo master CSVs are the portable source of truth. Firestore is the live application database. Google Workspace is the business input layer. Lovable is the public storefront and customer chatbot. Square is the transaction layer. Printful and Printify are POD fulfillment providers. Notion is a historical migration and optional export layer, not an active dependency.

Use this README as the front door to the system. Start with the governance files to understand the operating rules, tool roles, and proof-of-concept boundary. Then open the relevant workspace for the task at hand.

## Start Here by Task

* To understand the system architecture: start with [AOA_SYSTEM/SYSTEM_MAP.md](AOA_SYSTEM/SYSTEM_MAP.md)
* To understand tool roles: start with [AOA_SYSTEM/TOOL_MAP.md](AOA_SYSTEM/TOOL_MAP.md)
* To intake new artwork: start with [AOA_artwork-lab/](AOA_artwork-lab/)
* To update records: start with [AOA_datasets/](AOA_datasets/)
* To synchronize master records with Firestore: start with [AOA_UPDATE_WORKFLOW.md](AOA_UPDATE_WORKFLOW.md)
* To create content: start with [AOA_distribution-studio/](AOA_distribution-studio/)
* To prepare products: start with [AOA_product-studio/](AOA_product-studio/)
* To review sales or POD data: start with [data/](data/)

## System Governance

* [System map](AOA_SYSTEM/SYSTEM_MAP.md) - full architecture overview, layer definitions, and system flow.
* [ICM rules](AOA_SYSTEM/ICM_RULES.md) - source-of-truth rules, context loading rules, approval gates, and AI operating standards.
* [Tool map](AOA_SYSTEM/TOOL_MAP.md) - role of each tool in the Arts of August system.
* [Channel map](AOA_SYSTEM/CHANNEL_MAP.md) - distribution and sales channel definitions.
* [Commerce map](AOA_SYSTEM/COMMERCE_MAP.md) - Square, Printful, and Printify operating rules.
* [Google Workspace operating map](AOA_SYSTEM/GOOGLE_WORKSPACE_OPERATING_MAP.md) - Gmail, Calendar, Drive, and Gemini as the business input layer.
* [AI operator cost rules](AOA_SYSTEM/AI_OPERATOR_COST_RULES.md) - which AI tool to use for which task.
* [POC definition of done](AOA_SYSTEM/POC_DEFINITION_OF_DONE.md) - what must be true before the proof of concept is considered complete.
* [Database map](AOA_DATABASE_MAP.md) - master CSV and Firestore collection mapping.
* [Relation rules](AOA_RELATION_RULES.md) - stable-ID relationships between system objects.
* [Notion operating schema](AOA_SYSTEM/NOTION_OPERATING_SCHEMA.md) - historical Notion field definitions retained for migration reference.

## Source Intelligence

* [Arts of August source-intelligence README](AOA_source-intelligence/00-README-Arts-of-August.md) - brand, voice, product, workflow, and AI-generation source materials.

## Workspaces

* [Artwork lab](AOA_artwork-lab/) - artwork intake, image editing, SOPs, templates, and draft outputs.
* [Datasets](AOA_datasets/) - master CSV records for artwork, products, content, events, and opportunities.
* [Distribution studio](AOA_distribution-studio/) - content workflows, platform notes, drafts, approvals, and submissions.
* [Product studio](AOA_product-studio/) - product-generation workflow and product outputs.
* [Connecting layer](AOA_connecting-layer/) - placement rules, pipeline specs, readiness reviews, and post-approval handoffs.
* [Feedback analytics](AOA_feedback-analytics/) - performance-review workflow and feedback context.

## Data

* [data/assets/mockups.csv](data/assets/mockups.csv) - mockup asset tracking
* [data/campaigns.csv](data/campaigns.csv) - campaign tracking
* [data/sales/sales.csv](data/sales/sales.csv) - all sales transactions
* [data/pod/printful-map.csv](data/pod/printful-map.csv) - artwork-to-Printful product mapping
* [data/pod/printify-map.csv](data/pod/printify-map.csv) - artwork-to-Printify product mapping
* [data/channels/kit-email.csv](data/channels/kit-email.csv) - Kit email campaign tracking
