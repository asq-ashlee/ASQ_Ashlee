# ASQ Finance Context System

This project turns messy financial reality into usable business context.

It is part of the broader ASQ Ashlee ICM system: capture, structure, retrieve, reason, act, and review.

The goal is not to force Ashlee to manually maintain spreadsheets.
The goal is to let Ashlee capture financial information in plain language, then have an AI assistant or code agent turn that information into clean records, reports, reminders, and decisions.

## Core purpose

This system tracks and organizes:

- SaaS subscriptions and AI tools
- Trials, renewal dates, and cancellation deadlines
- Business expenses
- Revenue
- Pricing decisions
- Monthly software burn
- Draft P&L summaries
- Tax questions
- CPA/bookkeeper handoff notes
- Investor/lender readiness information

## The human interface

Ashlee should mainly use:

`00_capture/money-inbox.md`

That file is the messy note capture zone.

Example:

> I signed up for Gamma today. Free trial ends June 8. It will be $120/year. I’m using it for AIDB visuals and ASQ client decks. Cancel before it charges unless I’ve used it for paid work.

The agent should convert that note into:

- a subscription record
- a cancellation watchlist item
- monthly burn impact
- pricing implications if relevant
- open questions if anything is missing

## ICM loop

Money note
→ structured record
→ monthly summary
→ decision support
→ CPA / QuickBooks / investor output

## Core rule

No new tool, trial, subscription, or recurring payment should exist without a captured note or record.

The system can be imperfect.
The capture must be easy.
