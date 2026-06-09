---
name: shopify-development
description: >-
  Reference knowledge base for Shopify development — Online Store themes (Liquid,
  sections, blocks, schemas, templates), theme JS APIs (Ajax, Section Rendering),
  custom apps & extensions (auth, App Bridge, webhooks, billing, admin/checkout/
  customer-account/POS extensions), headless & Hydrogen, Shopify Functions, custom
  data (metafields/metaobjects), and AI/agentic commerce. Use whenever building,
  editing, debugging, reviewing, or answering questions about Shopify themes, Liquid
  code, Shopify apps, Hydrogen storefronts, Functions, metafields, or any shopify.dev
  topic. This is a 1:1 reference (verbatim docs) navigated via precise indexes.
allowed-tools:
  - Read
  - Grep
  - Glob
argument-hint: [topic, Liquid object/tag/filter, surface, or task]
---

# Shopify Development — Reference Library

A faithful (1:1) reference of the Shopify developer documentation, organized as a
navigable library. **648 pages across 18 reference chapters** + symbol indexes.
Source: shopify.dev, captured 2026-06-08.

> This skill is a **reference book you look things up in**, not a set of summaries.
> The `reference/` files hold the exact, verbatim docs (parameter tables, schemas,
> code examples). You navigate to the precise slice you need — you do **not** read
> whole files. Treat it like an API reference, not a tutorial.

## How to use this skill (lookup protocol)

You almost never need a whole reference file. To answer a Shopify question or do a
Shopify task:

1. **Identify the surface** (theme? Liquid? app? headless? function? custom data?) →
   use **Task routing** below or [indexes/task-routing.md](indexes/task-routing.md).
2. **For a specific Liquid symbol** (object/tag/filter) → look it up in the matching
   index to get the exact file + heading:
   - [indexes/liquid-objects.md](indexes/liquid-objects.md) — 135 objects
   - [indexes/liquid-filters.md](indexes/liquid-filters.md) — 155 filters
   - [indexes/liquid-tags.md](indexes/liquid-tags.md) — 28 tags
   - [indexes/schemas.md](indexes/schemas.md) — section/block/settings/config/template schemas
3. **Jump to the exact content**: open the named `reference/NN-*.md` file and
   `Grep` the heading the index gives you (e.g. `### product`, `## array — map`,
   `## 2.4 Sections`), then `Read` only that slice (use offset/limit on big files).
4. **Need a fast answer for common things** → [cheatsheet.md](cheatsheet.md) first.

Big files (ch02 ~9.4k lines, ch07 ~7.3k lines) must be read by slice via Grep+offset,
never whole.

## Orientation — the Shopify dev surfaces (mental model)

Pick the right surface before diving in; they use different tech and docs:

- **Online Store theme** — server-rendered storefront written in **Liquid** + JSON
  templates/sections/blocks. The "default" store. → `reference/01–06`, Liquid `07–11`.
- **Custom app** — code that extends the **admin** or adds backend logic; auths via
  OAuth/session tokens, talks to the **Admin API**, can ship **extensions**.
  → `reference/12–14`.
- **Headless / Hydrogen** — custom storefront (React/Hydrogen on Oxygen) consuming
  the **Storefront API**; replaces the Liquid theme. → `reference/15`.
- **Shopify Functions** — server-side custom logic (discounts, validation, delivery/
  payment customization) compiled to Wasm. → `reference/16`.
- **Custom data** — metafields & metaobjects extend any resource. → `reference/17`.
- **AI / agentic** — make a store operable by AI agents (UCP, MCP, llms.txt/agents.md).
  → `reference/18`.

A theme and a Hydrogen storefront are mutually exclusive choices; apps/functions/
custom-data layer onto either.

## Task routing (most common)

| If you're doing… | Read |
|---|---|
| Writing Liquid in a template/section | indexes/liquid-* then ref/07,08,09,10 |
| Building/editing a **section** (schema, settings, blocks) | ref/02 §2.4, §2.6, §2.8 + indexes/schemas.md |
| Theme **templates** (product/collection/cart/JSON) | ref/02 §2.3 |
| **Layouts** (theme.liquid, checkout.liquid) | ref/02 §2.2 |
| **Section groups** / dynamic areas | ref/02 §2.5 |
| **Snippets** / `render` | ref/02 §2.7 + tag `render` (ref/08) |
| **Settings** / `settings_schema.json` / config | ref/02 §2.8, §2.9 + indexes/schemas.md |
| **Localization** / translations | ref/02 §2.10 + filters `t`/`translate` |
| New theme / getting started | ref/01 + ref/02 §2.1 |
| Performance, accessibility, best practices | ref/03 |
| Theme tooling (CLI, Theme Check, GitHub) | ref/04 |
| AJAX cart / dynamic cart / **Section Rendering API** | ref/11 |
| Theme features: pricing, subscriptions, markets, SEO, search/filtering | ref/05 |
| Submitting/selling a theme (Theme Store) | ref/06 |
| Build a **custom app** (OAuth, session tokens, App Bridge, CLI) | ref/12 |
| App **webhooks / billing / distribution / compliance** | ref/13 |
| **App extensions** (admin/checkout/customer-account/POS/theme app ext.) | ref/14 |
| **Headless / Hydrogen / Oxygen / Customer Account API** | ref/15 |
| **Shopify Functions** (discounts, validation, cart transform, delivery/payment) | ref/16 |
| **Metafields / Metaobjects / custom data** | ref/17 |
| **AI agents / agentic commerce / UCP / MCP** | ref/18 |

Full version with sub-topics: [indexes/task-routing.md](indexes/task-routing.md).

## Reference chapter map

| # | File | Covers |
|---|------|--------|
| 00 | [reference/00-INDICE.md](reference/00-INDICE.md) | Original book index + fidelity notes |
| 01 | [reference/01-getting-started.md](reference/01-getting-started.md) | Build/customize a theme, quick start |
| 02 | [reference/02-key-concepts.md](reference/02-key-concepts.md) | **Architecture**: layouts, templates, sections, section groups, blocks, snippets, settings, config, locales |
| 03 | [reference/03-best-practices.md](reference/03-best-practices.md) | Performance, accessibility, theme editor, design, version control |
| 04 | [reference/04-developer-tools.md](reference/04-developer-tools.md) | Shopify CLI, Theme Check, GitHub, VS Code, Theme Inspector |
| 05 | [reference/05-theme-features.md](reference/05-theme-features.md) | Pricing, subscriptions, markets, SEO, search/filtering, OS2.0 migration |
| 06 | [reference/06-sell-themes.md](reference/06-sell-themes.md) | Theme Store requirements, testing, review, revenue share |
| 07 | [reference/07-liquid-objects.md](reference/07-liquid-objects.md) | Liquid overview/basics + **135 objects** |
| 08 | [reference/08-liquid-tags.md](reference/08-liquid-tags.md) | **28 Liquid tags** |
| 09 | [reference/09-liquid-filters-part1.md](reference/09-liquid-filters-part1.md) | **Filters A–L** (array→math) |
| 10 | [reference/10-liquid-filters-part2.md](reference/10-liquid-filters-part2.md) | **Filters M–Z** (media→tag) |
| 11 | [reference/11-theme-apis.md](reference/11-theme-apis.md) | Ajax API + Section Rendering API |
| 12 | [reference/12-apps-foundations.md](reference/12-apps-foundations.md) | App architecture, auth/OAuth/session tokens, App Bridge, build tools |
| 13 | [reference/13-apps-build-operate.md](reference/13-apps-build-operate.md) | Webhooks, billing, app config, distribution, compliance |
| 14 | [reference/14-app-extensions.md](reference/14-app-extensions.md) | Admin/Checkout/Customer-account/POS/Theme app extensions |
| 15 | [reference/15-headless-hydrogen.md](reference/15-headless-hydrogen.md) | Headless, Hydrogen, Oxygen, Customer Account API |
| 16 | [reference/16-functions.md](reference/16-functions.md) | Shopify Functions (all types + infra) |
| 17 | [reference/17-custom-data.md](reference/17-custom-data.md) | Metafields & Metaobjects |
| 18 | [reference/18-ai-agentic.md](reference/18-ai-agentic.md) | Agentic commerce, UCP, MCP, llms.txt/agents.md |

## Scope & limits

This library covers the **conceptual + how-to + reference (Liquid/schema/API-usage)**
docs 1:1. It intentionally does **not** dump the giant auto-generated **GraphQL/REST
schemas** (Admin API, Storefront API, Customer Account API), the per-component Hydrogen/
Polaris/Checkout-UI reference, or the full webhook-topic enum — those change often and
are best queried live via the **Shopify Dev MCP server** (`@shopify/dev-mcp`). Every
such omitted reference is listed (with URL) under a `## Pagine aggiuntive` section inside
the relevant chapter, so you always know where to go. The AI/agentic chapter (18) reflects
a fast-moving area; it flags what was unverified at capture time.
