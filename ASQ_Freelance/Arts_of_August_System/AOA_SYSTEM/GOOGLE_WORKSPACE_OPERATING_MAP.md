# AOA Google Workspace Operating Map

## Scope

This file defines how Google Workspace functions as the business input layer for the Arts of August system.

It applies to:

`ASQ_Freelance/Arts_of_August_System/`

Read alongside:

* `AOA_SYSTEM/SYSTEM_MAP.md`
* `AOA_SYSTEM/AI_OPERATOR_COST_RULES.md`
* `AOA_SYSTEM/ICM_RULES.md`

---

## Core Principle

Google Workspace is the business input layer.

It captures real-world business activity — inquiries, events, assets, and deadlines — and feeds that context into the AOA system.

Google Workspace is not the source of truth for artwork records, product records, or system rules. Those live in the repo.

---

## Gmail

### Role

Opportunity and inquiry capture.

### What it feeds

* gallery and market opportunities
* collector or wholesale inquiries
* press and media contacts
* event invitations and applications
* vendor or partner communication

### Operating pattern

1. Kaleigh or Ashlee identifies an email that contains an opportunity or inquiry.
2. Gemini or manual extraction pulls structured fields from the email.
3. Fields are brought into the repo opportunity record or Notion opportunity record.
4. Human reviews and approves before any response is sent.

### Do not use Gmail for

* storing artwork records
* replacing the repo as the source of truth
* sending automated responses without human approval

---

## Google Calendar

### Role

Event and deadline tracking.

### What it feeds

* art market dates
* show openings
* gallery deadlines
* workshop or community event dates
* content planning anchors

### Operating pattern

1. Events are entered into Google Calendar as they are confirmed.
2. Gemini or manual extraction pulls event details when planning is needed.
3. Fields are brought into the repo event record or Notion event record.
4. Content and product plans are built from confirmed event records.

### Do not use Google Calendar for

* artwork status tracking
* pricing decisions
* product availability

---

## Google Drive

### Role

Asset storage and synced repo context.

### What it stores

* master artwork photos
* edited artwork image files
* print-ready files
* mockup exports
* exported PDFs
* final deliverables
* synced copies of key repo context packets (optional)

### Operating pattern

* Drive links are referenced in artwork records (Image field).
* AI tools are not given broad Drive access by default.
* When an asset is needed for a task, a specific Drive link is passed intentionally.
* Synced context packets (CLAUDE.md, ICM rules, schema files) may be stored in Drive for ChatGPT Project access.

### Do not use Google Drive for

* replacing the repo as the instruction source of truth
* storing system rules or workflow docs as the primary copy
* bulk AI scanning without a specific task

---

## Gemini

### Role

Google-native extraction and summarization.

### Use Gemini for

* extracting structured fields from Gmail messages
* summarizing Calendar events for planning context
* pulling metadata from Drive files when needed
* Google Workspace-connected summarization tasks
* processing Google Sheets or Docs within the Google ecosystem

### Do not use Gemini for

* repo editing or file implementation
* final system architecture decisions
* replacing ChatGPT for strategy and synthesis
* replacing Claude Code for repo edits

### Standard pattern

Use Gemini when the input lives in Google Workspace and the task is extraction or summarization.

Pass the Gemini output to ChatGPT or Claude Code if the task moves into architecture, synthesis, or repo implementation.

---

## Google Workspace Integration Rules

1. Google Workspace is an input layer, not the source of truth.
2. Gemini processes Google-native content. Claude Code processes repo content. ChatGPT synthesizes across both.
3. Drive links in artwork records are references, not embedded assets.
4. No business action (reply, publish, purchase) is triggered from Google Workspace without human approval.
5. Synced Drive files are reference copies only. The repo is authoritative.
