# AOA ICM Rules

## Scope

This file applies ICM principles specifically to the Arts of August proof-of-concept system.

Broader ASQ Ashlee ICM principles may be defined separately at the parent system level. This file governs how context, tools, records, workflows, and AI agents should operate inside:

`ASQ_Freelance/Arts_of_August_System/`

## Purpose

The Arts of August system is designed to turn an artist’s body of work into structured, reusable sales and marketing infrastructure.

The system should help Arts of August move from scattered artwork information, images, notes, events, and opportunities into a repeatable workflow where each artwork can support:

* artwork records
* product listings
* shop pages
* content drafts
* event materials
* email or social copy
* gallery and opportunity applications
* future decision-making

This is not only a website project. It is a context-managed artist operating system.

## Core Principle

AI should not be asked to remember everything or read everything.

AI should read the smallest useful context packet, complete the bounded task, produce an auditable output, and wait for human approval before anything public, permanent, or customer-facing changes.

## Source of Truth Rules

### Markdown is the source of truth for system instructions

Use markdown files for:

* system rules
* SOPs
* workflow instructions
* schema definitions
* agent instructions
* prompt templates
* approval checklists
* case study notes
* tool maps
* decision logs

Markdown files should be short, modular, and easy for both humans and AI tools to read.

Do not bury stable operating rules in chat history.

Do not make AI infer system behavior from scattered notes.

### Notion is the source of truth for live business records

Use Notion for records that change during operation, including:

* artworks
* products
* events
* content items
* opportunities
* statuses
* availability
* pricing
* publish state
* review state
* performance notes

Notion should hold structured objects, not long system philosophy.

If a record needs to be reused across shop pages, content, events, or applications, it should live in Notion.

### Lovable is the public output layer

Use Lovable for:

* public shop pages
* product detail pages
* landing pages
* demo pages
* client-facing system surfaces

Lovable should display or transform approved system data.

Lovable should not be treated as the source of truth for artwork, product, event, or content records.

### ChatGPT is the strategy and orchestration layer

Use ChatGPT for:

* system design
* workflow sequencing
* offer framing
* client-facing language
* case study writing
* prompt writing
* reviewing outputs from Codex, Claude Code, Lovable, or Notion
* turning messy ideas into structured plans

ChatGPT may help design system files, but final operating files should be saved in the repo or Notion, not left only in chat.

### Codex and Claude Code are implementation agents

Use Codex or Claude Code for:

* creating files
* editing markdown
* updating repo structure
* applying scoped changes
* reviewing local files
* implementing code or configuration
* following an approved work order

Do not ask implementation agents to invent the business strategy, rewrite the system architecture, or make unapproved changes across the repo.

Implementation agents should receive narrow tasks with explicit context files and acceptance criteria.

## Context Loading Rules

Before an AI agent starts work, it should know:

1. What task it is doing
2. Which context files to read
3. Which files or records it may edit
4. Which files or records it must not edit
5. What output format is expected
6. What approval gate applies
7. What counts as done

Agents should not load the entire system unless the task explicitly requires full-system review.

Use context packets instead of giant master documents.

Recommended context packets include:

* `ICM_RULES.md`
* `TOOL_MAP.md`
* `POC_DEFINITION_OF_DONE.md`
* `ARTIST_VOICE_CONTEXT.md`
* `ARTWORK_INTAKE_CONTEXT.md`
* `SHOP_OUTPUT_CONTEXT.md`
* `CONTENT_SYSTEM_CONTEXT.md`
* `EVENT_WORKFLOW_CONTEXT.md`
* `OPPORTUNITIES_AGENT_CONTEXT.md`
* `SCHEMA_INDEX.md`

Each workflow should identify its required context packet before work begins.

## Work Order Pattern

Every Codex or Claude Code task should follow this pattern:

```text
Task:
[What the agent should do]

Read first:
[List only the required context files]

Allowed to edit:
[List files or folders the agent may change]

Do not edit:
[List files or folders the agent must not change]

Output:
[Expected files, summary, or diff]

Acceptance criteria:
[How Ashlee will know the task is complete]

Approval:
Do not publish, push, delete, rename, or overwrite major files without human review.
```

## Human Approval Gates

AI may draft, structure, summarize, recommend, and prepare outputs.

A human must approve before:

* an artwork title is finalized
* a price changes
* an artwork is marked available or sold
* a product page goes live
* a public description is published
* a social post or email is sent
* an event page is published
* an opportunity application is submitted
* a gallery, venue, partner, or customer is contacted
* a workflow rule becomes permanent
* a schema change affects existing records

For Arts of August, Kaleigh approves artistic representation, artwork details, final voice, visual presentation, pricing, and publication.

Ashlee approves system architecture, workflow design, context structure, repo changes, and proof-of-concept scope.

## Write-Back Rules

AI outputs should be written back only when the destination is clear.

Write to markdown when the output is:

* an instruction
* a workflow
* a template
* a system rule
* a case study section
* a reusable prompt
* a decision log

Write to Notion when the output is:

* an artwork record
* a product record
* a content item
* an event record
* an opportunity record
* a status update
* a performance note
* a review note

Write to Lovable only when the output is:

* approved public page structure
* approved component copy
* approved display logic
* approved page content

If the destination is unclear, stop and ask.

## Token and Context Budget Rules

Do not use AI to repeatedly re-process the same context.

Stable instructions should live in markdown.

Live records should live in Notion.

Each workflow should start from a small context packet and a specific record, not the entire system.

Avoid pasting full databases, long chats, or unrelated files into AI tools.

When possible, pass:

* one task
* one workflow context
* one schema
* one record or small record set
* one expected output

If an AI task requires more than three context packets, ask whether the task should be split.

## Repo and Asset Rules

The active repo should stay lightweight and context-clean.

Large images, mockups, exports, print files, and final asset folders should not be treated as core AI-readable context unless they are needed for a specific task.

Use the repo for:

* markdown instructions
* workflow docs
* schema docs
* lightweight examples
* system decision records
* approved prompts

Use external asset storage for:

* master photos
* edited artwork images
* mockups
* print files
* event photos
* exported PDFs
* final deliverables

If an asset is needed for a workflow, reference it intentionally rather than making agents scan large folders.

## System Object Rules

The system should treat the following as core objects.

### Artwork

A unique creative work by the artist.

May generate:

* product listings
* shop pages
* captions
* emails
* event materials
* gallery language
* print products
* collector notes

### Product

A sellable version of an artwork.

May include:

* original painting
* print
* framed print
* canvas print
* commission option
* event-only product

### Content Item

A planned or published marketing asset.

May include:

* Instagram post
* reel prompt
* email
* website section
* event blurb
* artist note
* gallery statement

### Event

An in-person or online selling, showing, or community moment.

May connect to:

* artworks
* products
* content items
* venue
* date
* promotion plan
* post-event notes

### Opportunity

A gallery, market, membership, juried show, partnership, press opportunity, or application.

May connect to:

* artist bio
* artwork examples
* deadlines
* requirements
* application drafts
* status
* decision notes

## Workflow Rules

### Artwork Intake

The artwork intake workflow should convert a finished artwork and its source information into a structured artwork record.

It should use:

* photography SOP
* artwork schema
* artist voice context
* pricing or product context if needed

It should produce:

* artwork record draft
* title options if needed
* description draft
* alt text
* tags or themes
* missing information checklist

It should not publish anything without review.

### Shop Output

The shop workflow should convert approved artwork and product records into public-facing shop content.

It should use:

* artwork record
* product record
* shop output context
* approved images or mockups

It should produce:

* product page copy
* image alt text
* availability display
* Square or checkout link placement
* SEO/GEO-ready page structure

It should not treat Lovable as the source of truth.

### Content System

The content workflow should convert approved artwork, event, or opportunity context into reusable content drafts.

It should use:

* artwork record
* artist voice context
* content schema
* channel-specific instructions
* review status

It should produce:

* content draft
* channel
* intended audience
* CTA
* source artwork or event
* review state

It should not auto-publish.

### Event Workflow

The event workflow should turn an event record into a promotion and preparation plan.

It should use:

* event record
* product or artwork records
* content system context
* venue details
* timing

It should produce:

* event content plan
* product list
* promotional copy
* prep checklist
* post-event review fields

It should not assume inventory without checking current records.

### Opportunities Workflow

The opportunities workflow should find, evaluate, and prepare applications for relevant artist opportunities.

It should use:

* opportunity schema
* artist goals
* artist bio
* artwork records
* scoring rubric

It should produce:

* opportunity record
* fit score
* rationale
* requirements checklist
* draft application materials when requested

It should not submit applications or contact organizations without approval.

## SEO and GEO Rule

The system should support both SEO and GEO.

SEO means making public pages clear, crawlable, useful, and structured for traditional search.

GEO means making the artist’s work, story, products, and context easier for AI systems to understand, summarize, retrieve, and reuse accurately.

The system should not replace SEO with GEO.

The system should maintain a structured context layer that can feed both SEO-ready and GEO-ready outputs.

## Decision Log Rule

When a system decision is made, record it in a decision log if it changes how the system works.

Examples:

* choosing Notion as the live record source
* choosing Square as the checkout path
* choosing Lovable as the public shop layer
* changing a schema
* changing approval gates
* choosing a mockup workflow
* changing the POC scope

A decision log entry should include:

* date
* decision
* reason
* affected files or workflows
* open questions

## POC Rule

The proof of concept should stay intentionally small.

The first POC should prove that three artworks can move through the full system loop:

1. photographed using the SOP
2. entered into the artwork database
3. transformed into product and shop-ready outputs
4. supported by approved mockups or images
5. displayed in the shop or demo layer
6. turned into content drafts
7. documented as a repeatable workflow

Do not wait for the entire system to be complete before testing the loop.

The POC is successful if the system proves that one artist’s body of work can become structured, reusable, AI-supported sales and marketing infrastructure.

## Operating Standard

Build once.

Reuse everywhere.

Load only the needed context.

Keep source-of-truth rules visible.

Let AI draft and structure.

Let humans approve meaning, taste, price, and publication.

Store decisions where they can be found again.
