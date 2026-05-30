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

Do not ask every tool to do everything.

Use each tool for its strongest role:

* ChatGPT thinks, frames, reviews, and writes strategy.
* Codex or Claude Code implement scoped repo changes.
* Markdown stores stable instructions and system knowledge.
* Notion stores live records.
* Lovable displays approved public outputs.
* Canva and mockup tools create visual assets.
* Google Drive or external storage holds large assets and deliverables.
* GitHub tracks version history.

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

Live operational database.

### Use Notion for

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
* structured context that should be reused across outputs

### Do not use Notion for

* long system philosophy
* giant SOPs
* source-of-truth workflow rules
* raw chat history
* large file libraries
* replacing markdown instruction files

### Standard Pattern

If the object changes during business operation, it probably belongs in Notion.

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

1. Notion holds approved artwork/product records.
2. Mockup tools or Canva create approved visuals.
3. Lovable displays shop and product pages.
4. Square handles checkout.
5. Kaleigh approves publication.

Primary tools:

* Notion
* Lovable
* Square
* Canva or mockup tools
* External asset storage

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

## Tool Decision Rules

If the question is “What should we do?” use ChatGPT.

If the question is “Where should this live?” use ICM rules and ChatGPT.

If the question is “Can you edit these files?” use Codex or Claude Code.

If the question is “What is the current status of this artwork/product/content/event?” use Notion.

If the question is “What should the public see?” use Lovable after approval.

If the question is “What visual should we use?” use Canva or mockup tools.

If the question is “Where is the master file?” use external asset storage.

If the question is “What changed?” use GitHub diff/history.

## Operating Standard

One tool does not own the whole system.

Each tool should serve its layer.

When unsure, ask:

1. Is this instruction, record, output, asset, or transaction?
2. Who needs to approve it?
3. Does it belong in markdown, Notion, Lovable, external storage, or payment tooling?
4. What is the smallest context needed for the next action?
