# AOA Tool Map

## Scope

This file defines the role of each tool in the Arts of August proof-of-concept system.

It applies to:

`ASQ_Freelance/Arts_of_August_System/`

This file should be read alongside:

* `AOA_SYSTEM/ICM_RULES.md`
* `AOA_SYSTEM/POC_DEFINITION_OF_DONE.md`

## Purpose

The Arts of August system uses multiple tools, but each tool should have a clear role.

The goal is to avoid tool confusion, duplicate work, unnecessary context loading, and unclear source-of-truth decisions.

Each tool should do the job it is best suited for.

## Core Tool Principle

### Firestore Supersession — Effective 2026-07-21

This section overrides older Notion-era tool-routing statements elsewhere in this file.

* Repo master CSVs are the portable structured-record source of truth.
* Firestore is the live application database for approved artwork, product, content, event, and opportunity records.
* Codex or another approved implementation tool validates master CSVs, performs stable-ID upserts, and verifies Firestore by reading it back.
* Firestore is not used for Markdown instructions, secrets, unreviewed drafts, or automatic deletion.
* Notion is no longer part of the active update loop. Its schemas and exports are retained only for migration provenance and historical comparison.

For a record update, follow `../AOA_UPDATE_WORKFLOW.md`. For ownership and identifiers, follow `../AOA_DATABASE_MAP.md` and `../AOA_RELATION_RULES.md`.

Do not ask every tool to do everything.

Use each tool for its strongest role:

* The repo is the source of truth.
* Google Workspace (Gmail, Calendar, Drive) feeds real-world business inputs.
* Gemini extracts and summarizes Google-native content.
* ChatGPT thinks, frames, synthesizes, and writes strategy and handoff prompts.
* Codex or Claude Code implement scoped repo changes, scripts, and validation.
* Markdown stores stable instructions and system knowledge.
* Notion is an optional dashboard and export layer.
* Lovable displays approved public outputs and powers the customer chatbot.
* Square handles transactions (original checkout links and in-person POS).
* Printful and Printify fulfill print-on-demand orders.
* Canva and mockup tools create visual assets.
* Google Drive holds large assets and deliverables.
* GitHub tracks version history.

See `AOA_SYSTEM/SYSTEM_MAP.md` for the full architecture overview.

## Tool Roles

## ChatGPT

### Primary Role

Strategy, architecture, orchestration, drafting, and review.

### Use ChatGPT for

* system design
* workflow sequencing
* proof-of-concept planning
* client-facing offer framing
* case study writing
* prompt and work order drafting
* reviewing Codex or Claude Code outputs
* reviewing Lovable copy or structure
* defining approval gates
* translating messy ideas into structured plans
* deciding whether a change belongs in markdown, Notion, Lovable, or elsewhere

### Do not use ChatGPT for

* storing live artwork records long term
* acting as the final inventory database
* replacing Notion as the operational source of truth
* making unreviewed public changes
* maintaining files only in chat history

### Standard Pattern

Use ChatGPT before implementation when the task requires judgment, framing, architecture, or client-facing language.

## ChatGPT Projects

### Primary Role

Stable context home base for the Arts of August system.

### Use ChatGPT Projects for

* storing stable system context
* keeping key markdown files accessible
* maintaining the overall AOA system direction
* helping ChatGPT understand the current operating model
* reviewing project-level decisions

### Do not use ChatGPT Projects for

* storing every image or asset
* replacing the repo
* replacing Notion
* keeping every rough note forever
* loading unnecessary files into every task

### Standard Pattern

Use the project for stable context, not every working file.

## Markdown Files

### Primary Role

Source of truth for system instructions.

### Use markdown for

* ICM rules
* tool maps
* SOPs
* schema definitions
* workflow docs
* prompt templates
* decision logs
* context packets
* proof-of-concept definitions
* case study drafts
* agent instructions

### Do not use markdown for

* live inventory tracking
* frequently changing operational statuses
* large image storage
* final customer-facing asset storage
* data that should live in Notion

### Standard Pattern

If the file explains how the system works, it probably belongs in markdown.

## Folders

### Primary Role

Context separation and agent guidance.

### Use folders for

* separating system docs from workflows
* separating schemas from live records
* separating stable context from assets
* helping AI tools read only what they need
* keeping the repo navigable

### Do not use folders for

* hiding duplicate source-of-truth files
* storing large unneeded assets in the active repo
* creating deeply nested structures without purpose

### Standard Pattern

A folder should help a human or AI agent understand what to read next.

## GitHub

### Primary Role

Version history, backup, sharing, and review.

### Use GitHub for

* tracking repo changes
* commits
* branches if needed
* reviewing diffs
* preserving history
* sharing system structure or case study work

### Do not use GitHub for

* storing private client data that should stay elsewhere
* storing large image libraries unless intentionally managed
* replacing Notion operational records

### Standard Pattern

Commit meaningful system changes after review.

## Codex in VS Code

### Primary Role

Implementation agent for scoped repo work.

### Use Codex for

* creating markdown files
* editing repo documentation
* updating folder structure
* applying approved file changes
* checking diffs
* making small code or config edits
* following explicit work orders
* summarizing what changed

### Do not use Codex for

* inventing the AOA business strategy
* making broad unsupervised repo changes
* deleting or renaming files without approval
* editing live data records unless explicitly instructed
* reading the entire repo by default
* working from vague prompts

### Standard Pattern

Give Codex:

* one task
* specific files to read
* specific files it may edit
* files it must not edit
* acceptance criteria
* instruction to show the diff before commit

## Claude Code

### Primary Role

Alternative implementation agent for repo/file workflows.

### Use Claude Code for

* scoped markdown edits
* repo file updates
* workflow implementation
* reviewing local structure
* applying approved work orders
* checking file consistency

### Do not use Claude Code for

* open-ended system strategy
* unsupervised architecture changes
* duplicate work already assigned to Codex
* reading large context folders without need

### Standard Pattern

Use either Codex or Claude Code for a task, not both at the same time unless intentionally comparing outputs.

## Notion

### Primary Role

Optional dashboard and export layer.

Notion is not required in the publishing path. The repo holds the source records.

### Use Notion for

* viewing structured records in a visual database interface
* exporting or sharing records externally
* surfacing status views for review
* artwork records
* product records
* content records
* event records
* opportunity records
* statuses
* availability
* pricing
* publish state
* review state
* performance notes

### Do not use Notion for

* long system philosophy
* giant SOPs
* source-of-truth workflow rules
* raw chat history
* large file libraries
* replacing markdown instruction files
* acting as a required publishing gate

### Standard Pattern

Notion is available as a view and export layer. Publishing workflows can complete without writing to Notion.

Existing Notion fields and schemas are preserved. See `AOA_SYSTEM/NOTION_OPERATING_SCHEMA.md`.

## Lovable

### Primary Role

Public output layer.

### Use Lovable for

* shop pages
* product detail pages
* landing pages
* client-facing demo pages
* public-facing page layouts
* displaying approved artwork/product data
* turning structured records into visible web surfaces

### Do not use Lovable for

* primary data storage
* final source of truth for artwork/product records
* unapproved public changes
* long-term system instruction storage

### Standard Pattern

Lovable should display approved data, not become the system brain.

## Canva

### Primary Role

Visual production and lightweight asset creation.

### Use Canva for

* social graphics
* event graphics
* simple promotional assets
* presentation visuals
* brand layouts
* mockup adjustments when useful

### Do not use Canva for

* structured system data
* source-of-truth records
* long-term workflow instructions
* operational tracking

### Standard Pattern

Use Canva when visual judgment and layout matter more than structured data.

## Mockup Tools

### Primary Role

Create visual selling assets for artwork.

### Use mockup tools for

* room mockups
* framed artwork previews
* lifestyle images
* product display assets
* shop and content visuals

### Do not use mockup tools for

* artwork records
* final system storage
* metadata management
* product availability
* pricing decisions

### Standard Pattern

Mockups support the shop and content layers but do not define the artwork record.

## Google Drive or External Asset Storage

### Primary Role

Storage for large assets, exports, and deliverables.

### Use external storage for

* master photos
* edited artwork images
* print files
* mockups
* event photos
* exported PDFs
* final client deliverables
* large folders that should not be scanned by AI tools by default

### Do not use external storage for

* active repo source-of-truth instructions
* files Codex needs to edit regularly
* system rules
* schemas
* core workflow docs

### Standard Pattern

Keep the active repo lightweight. Store heavy assets externally and reference them intentionally when needed.

## Square

### Primary Role

Checkout and payment path.

### Use Square for

* payment links
* checkout
* product purchase flow
* sales processing
* customer purchase confirmation

### Do not use Square for

* system workflow instructions
* full artwork context
* AI-readable source-of-truth data
* content planning
* event planning

### Standard Pattern

Square is the transaction layer, not the context layer.

## Etsy

### Primary Role

Marketplace channel, if used.

### Use Etsy for

* marketplace listings
* discovery through Etsy search
* print or product sales if Kaleigh chooses
* existing sales channel continuity

### Do not use Etsy for

* full system source of truth
* master artwork records
* internal content planning
* long-term context management

### Standard Pattern

Etsy is a channel. Notion is the record source.

## Google Workspace

### Primary Role

Business input layer.

### Use Google Workspace for

* Gmail: capturing opportunities, inquiries, and event invitations
* Google Calendar: tracking event and deadline dates
* Google Drive: storing master artwork images, print files, exports, and synced context packets
* Gemini: extracting and summarizing Google-native content

### Do not use Google Workspace for

* replacing the repo as the source of truth
* storing system rules or workflow docs as the primary copy
* sending automated responses without human approval

### Standard Pattern

Google Workspace captures real-world business inputs. Those inputs are extracted (by Gemini or manually) and brought into the repo or Notion for structured processing.

See `AOA_SYSTEM/GOOGLE_WORKSPACE_OPERATING_MAP.md`

## Gemini

### Primary Role

Google-native extraction and summarization.

### Use Gemini for

* extracting structured fields from Gmail messages
* summarizing Google Calendar events for planning context
* processing Google Docs or Sheets within the Google ecosystem
* Drive file summarization when the task is native to Google Workspace

### Do not use Gemini for

* repo editing or file implementation
* final architecture decisions
* replacing ChatGPT for strategy and synthesis
* replacing Claude Code for implementation

### Standard Pattern

Gemini output is passed to ChatGPT or Claude Code for the next action.

See `AOA_SYSTEM/AI_OPERATOR_COST_RULES.md`

## Printful

### Primary Role

Print-on-demand fulfillment provider.

### Use Printful for

* fulfilling print orders (canvas prints, framed prints, paper prints)
* managing product variants by size and substrate
* order routing when a POD sale is triggered

### Do not use Printful for

* storing artwork records or metadata
* acting as the product database
* replacing the repo as the source of truth for product information

### Standard Pattern

Printful technical details (product IDs, variant IDs, sync status) are tracked in `data/pod/printful-map.csv`, not in artwork records.

## Printify

### Primary Role

Alternative or concurrent print-on-demand fulfillment provider.

### Use Printify for

* fulfilling print orders, particularly for specific product types or price points
* managing product variants per Printify catalog
* concurrent POD fulfillment when both Printful and Printify are active

### Do not use Printify for

* storing artwork records or metadata
* acting as the product database
* replacing the repo as the source of truth

### Standard Pattern

Printify technical details are tracked in `data/pod/printify-map.csv`.

Printful and Printify may both be active providers. The provider map determines which products route to which provider.

See `AOA_SYSTEM/COMMERCE_MAP.md`

## Tool Chain by Workflow

## Artwork Intake

Recommended tool chain:

1. Kaleigh creates or provides artwork and photo.
2. External asset storage holds master image.
3. ChatGPT helps define intake structure if needed.
4. Notion stores artwork record.
5. Codex updates any related workflow docs if needed.
6. Kaleigh approves final artwork details.

Primary tools:

* Notion
* Markdown
* ChatGPT
* External asset storage

## Photography and Master Edit SOP

Recommended tool chain:

1. ChatGPT drafts SOP from Ashlee and Kaleigh notes.
2. Markdown stores SOP.
3. Kaleigh tests process.
4. Ashlee updates SOP after review.
5. Codex applies final file changes.

Primary tools:

* ChatGPT
* Markdown
* Codex
* External asset storage

## Shop Output

Recommended tool chain:

1. Repo holds approved artwork/product records (CSV).
2. Mockup tools or Canva create approved visuals.
3. Lovable displays shop and product pages.
4. Square handles checkout (original artwork) or Printful/Printify handles POD fulfillment.
5. Kaleigh approves publication.
6. Notion may optionally mirror approved records.

Primary tools:

* Repo (CSV records)
* Lovable
* Square
* Printful / Printify (POD)
* Canva or mockup tools
* Google Drive (asset storage)

## Content Workflow

Recommended tool chain:

1. Notion supplies artwork, product, event, or opportunity record.
2. ChatGPT drafts content based on approved context.
3. Notion stores content item and status.
4. Canva supports visual asset creation if needed.
5. Kaleigh approves before publishing.

Primary tools:

* Notion
* ChatGPT
* Canva
* External publishing channels

## Event Workflow

Recommended tool chain:

1. Notion stores event record.
2. Notion connects event to artworks/products/content.
3. ChatGPT drafts event plan and copy.
4. Canva creates promo graphics if needed.
5. Kaleigh approves promotion and product selection.

Primary tools:

* Notion
* ChatGPT
* Canva
* External asset storage

## Opportunities Workflow

Recommended tool chain:

1. ChatGPT or another research tool helps identify opportunities.
2. Notion stores opportunity records.
3. ChatGPT helps evaluate fit and draft materials.
4. Kaleigh approves applications.
5. Ashlee updates workflow or rubric in markdown if needed.

Primary tools:

* ChatGPT
* Notion
* Markdown
* External websites or application portals

## Required Context Files by Workflow

Use this section to keep AI tasks bounded.

Before asking ChatGPT, Codex, Claude Code, or another AI tool to work on a workflow, provide only the files needed for that workflow unless the task explicitly requires broader system review.

### Full-System Review

Read first:

* `AOA_SYSTEM/ICM_RULES.md`
* `AOA_SYSTEM/TOOL_MAP.md`
* `AOA_SYSTEM/POC_DEFINITION_OF_DONE.md`
* relevant README or system overview file

Use when:

* reviewing the whole AOA system
* changing system architecture
* changing source-of-truth rules
* changing proof-of-concept scope
* onboarding a new AI agent to the system

### Artwork Intake

Read first:

* `AOA_SYSTEM/ICM_RULES.md`
* `AOA_SYSTEM/TOOL_MAP.md`
* `AOA_artwork-lab/AOA_artwork-lab_context.md`
* `AOA_artwork-lab/aoa-artwork-sops/photography-and-master-file-SOP.md`
* artwork schema file, if available
* artist voice context file, if available

Use when:

* creating or revising artwork intake workflow
* turning a finished artwork into a structured record
* drafting artwork titles, descriptions, tags, or alt text
* identifying missing artwork information

### Photography and Master File SOP

Read first:

* `AOA_SYSTEM/ICM_RULES.md`
* `AOA_SYSTEM/TOOL_MAP.md`
* `AOA_artwork-lab/aoa-artwork-sops/photography-and-master-file-SOP.md`
* any existing photography notes or draft SOPs

Use when:

* revising the photography process
* updating master file requirements
* defining image approval standards
* changing file naming or asset storage rules

### Shop Output

Read first:

* `AOA_SYSTEM/ICM_RULES.md`
* `AOA_SYSTEM/TOOL_MAP.md`
* shop output context file, if available
* artwork schema file, if available
* product schema file, if available
* approved artwork/product record from Notion
* approved image or mockup reference

Use when:

* creating shop page copy
* creating product detail page copy
* defining Lovable display logic
* preparing SEO/GEO-ready product content
* connecting product records to Square checkout links

### Content Workflow

Read first:

* `AOA_SYSTEM/ICM_RULES.md`
* `AOA_SYSTEM/TOOL_MAP.md`
* content system context file, if available
* artist voice context file, if available
* content schema file, if available
* relevant artwork, product, event, or opportunity record from Notion

Use when:

* drafting social posts
* drafting emails
* creating content prompts
* planning a content batch
* reviewing or scoring content performance

### Event Workflow

Read first:

* `AOA_SYSTEM/ICM_RULES.md`
* `AOA_SYSTEM/TOOL_MAP.md`
* event workflow context file, if available
* event schema file, if available
* content system context file, if available
* relevant event record from Notion
* relevant artwork/product records from Notion

Use when:

* planning event promotion
* selecting event products
* drafting event copy
* creating event prep checklists
* reviewing post-event results

### Opportunities Workflow

Read first:

* `AOA_SYSTEM/ICM_RULES.md`
* `AOA_SYSTEM/TOOL_MAP.md`
* opportunities agent context file, if available
* opportunity schema file, if available
* artist bio or artist voice context file
* relevant artwork records or portfolio examples

Use when:

* researching galleries, markets, memberships, juried shows, or press opportunities
* evaluating opportunity fit
* drafting application materials
* creating requirements checklists
* preparing outreach drafts

### Case Study or Client-Facing Proof of Concept

Read first:

* `AOA_SYSTEM/ICM_RULES.md`
* `AOA_SYSTEM/TOOL_MAP.md`
* `AOA_SYSTEM/POC_DEFINITION_OF_DONE.md`
* relevant workflow files used in the proof of concept
* approved before/after examples
* approved client-facing language or ASQ Ashlee voice context

Use when:

* writing the AOA case study
* preparing a demo for another artist
* creating an offer page
* explaining the system in client-facing language
* documenting proof-of-concept outcomes

## Tool Decision Rules

If the question is “What should we do?” use ChatGPT.

If the question is “Where should this live?” use ICM rules and ChatGPT.

If the question is “Can you edit these files?” use Codex or Claude Code.

If the question is “What is the current record for this artwork/product?” use the repo CSV.

If the question is “What is the current status of this artwork/product/content/event?” use the repo CSV or Notion (optional view).

If the question is “What should the public see?” use Lovable after approval.

If the question is “What visual should we use?” use Canva or mockup tools.

If the question is “Where is the master file?” use Google Drive.

If the question is “What changed?” use GitHub diff/history.

If the question is “What opportunities came in?” use Gmail / Gemini extraction.

If the question is “What events are coming up?” use Google Calendar.

If the question is “Which AI should do this?” use `AOA_SYSTEM/AI_OPERATOR_COST_RULES.md`.

## Operating Standard

One tool does not own the whole system.

Each tool should serve its layer.

When unsure, ask:

1. Is this instruction, record, output, asset, or transaction?
2. Who needs to approve it?
3. Does it belong in markdown, Notion, Lovable, external storage, or payment tooling?
4. What is the smallest context needed for the next action?
