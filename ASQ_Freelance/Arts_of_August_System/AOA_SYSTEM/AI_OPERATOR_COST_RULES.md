# AOA AI Operator Cost Rules

## Scope

This file defines which AI tool to use for which type of task in the Arts of August system, and the rationale for those assignments.

"Cost" here means context cost, token cost, tool-switching cost, and review burden — not just billing.

It applies to:

`ASQ_Freelance/Arts_of_August_System/`

Read alongside:

* `AOA_SYSTEM/TOOL_MAP.md`
* `AOA_SYSTEM/ICM_RULES.md`
* `AOA_SYSTEM/SYSTEM_MAP.md`

---

## Core Principle

Do not ask every AI tool to do everything.

Each AI operator has a strongest lane. Route tasks to the tool that can complete them with the least context overhead, the most reliable output, and the clearest human review path.

---

## Gemini

### Primary role

Google-native extraction and summarization.

### Use Gemini for

* extracting structured fields from Gmail messages (opportunities, inquiries, event details)
* summarizing Google Calendar events for planning context
* reading and summarizing Google Docs or Sheets within the Google ecosystem
* processing Drive files when the task is native to Google Workspace
* quick extraction tasks where the input already exists in Google tools

### Do not use Gemini for

* repo edits or file implementation
* final architecture decisions
* replacing ChatGPT for synthesis and strategy
* replacing Claude Code for implementation
* tasks that require reading the repo directly

### Standard handoff pattern

Gemini output → paste structured result → ChatGPT or Claude Code for next action.

---

## ChatGPT

### Primary role

Architecture, synthesis, quality assurance, and handoff prompt writing.

### Use ChatGPT for

* system design and workflow decisions
* synthesizing inputs from multiple sources into a structured plan
* writing or reviewing handoff prompts and work orders
* QA review of Claude Code or Codex outputs
* reviewing Lovable copy or structure
* client-facing language, offer framing, and case study writing
* evaluating opportunity fit
* deciding where something belongs (markdown, Notion, Lovable, elsewhere)
* translating messy notes into structured plans

### Do not use ChatGPT for

* direct repo file editing
* implementation-level file changes
* long-term record storage
* replacing Gemini for Google-native extraction

### Standard pattern

Use ChatGPT when the task requires judgment, synthesis, architecture, framing, or cross-context thinking.

ChatGPT designs the plan. Claude Code or Codex implements it.

---

## Claude Code / Codex

### Primary role

Repo edits, scripts, validation, and implementation.

### Use Claude Code for

* creating and editing markdown files in the repo
* applying approved work orders to the repo
* updating schema files, data placeholder files, or workflow docs
* writing and running validation scripts
* checking file consistency across the repo
* applying scoped file changes with a clear diff
* implementing approved architecture decisions

### Use Codex for

Same as Claude Code. Use one or the other per task, not both simultaneously unless intentionally comparing outputs.

### Do not use Claude Code for

* open-ended system strategy
* inventing architecture without an approved plan
* making changes that affect Notion, Lovable, or Square directly
* making unsupervised changes across the entire repo

### Standard pattern

Give Claude Code:

* one task
* specific files to read
* specific files it may edit
* files it must not edit
* acceptance criteria

Claude Code shows the diff. Human reviews before committing.

---

## AI Operator Decision Table

| Task type | Use |
|-----------|-----|
| Extract fields from Gmail | Gemini |
| Summarize a Calendar event | Gemini |
| Synthesize a workflow plan | ChatGPT |
| Write a handoff prompt or work order | ChatGPT |
| QA review a Claude Code output | ChatGPT |
| Write client-facing offer language | ChatGPT |
| Edit a markdown file in the repo | Claude Code |
| Update a CSV schema or data file | Claude Code |
| Run a validation script | Claude Code |
| Apply an approved work order | Claude Code |
| Design system architecture | ChatGPT |
| Extract metadata from Drive files | Gemini |
| Evaluate opportunity fit | ChatGPT |
| Create a new workflow doc | Claude Code (with ChatGPT plan) |

---

## Handoff Chain

Standard handoff pattern for non-trivial tasks:

```
Gemini (extract from Google Workspace)
    ↓
ChatGPT (synthesize, plan, write work order)
    ↓
Claude Code (implement in repo)
    ↓
Human review and approval
    ↓
Publish or commit
```

Not every task requires all steps. Simple repo edits go directly to Claude Code.

---

## Cost Avoidance Rules

1. Do not reload the entire system context for every task. Use context packets.
2. Do not run the same extraction in both Gemini and ChatGPT. Pick one.
3. Do not ask ChatGPT to do implementation-level file edits. Use Claude Code.
4. Do not ask Claude Code to design architecture. Use ChatGPT first.
5. Do not send large unstructured inputs (full databases, long chat logs) into AI tools. Extract and structure first.
6. If a task requires more than three context files, consider splitting it.
