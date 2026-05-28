# Prompt: Process Money Inbox

Use this prompt with Claude Code, Codex, ChatGPT, or another assistant that can access the repo.

---

You are working inside the ASQ Finance Context System.

Read:
- CLAUDE.md
- README.md
- 01_context/finance-context-brief.md
- 01_context/category-map.md
- 00_capture/money-inbox.md

Then process unprocessed notes from `00_capture/money-inbox.md`.

For each note:
1. Classify it.
2. Update relevant JSONL records in `02_records`.
3. Update relevant Markdown reports in `03_reports`.
4. Update decision files in `04_decisions` if needed.
5. Add missing-info questions to `00_capture/questions-for-ashlee.md`.
6. Archive processed notes in `archive/processed-inbox.md`.

Do not invent missing information.
Use "unknown" where needed.
Use tax-category guesses only, not tax advice.
Keep the system simple.
