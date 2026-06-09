<div align="center">

# Shopify Development Skill for AI Agents

**The entire shopify.dev reference, as an installable skill for Claude Code, Amp & Cursor.**
Your agent looks up the *exact, verbatim* Shopify docs — Liquid, themes, apps, Hydrogen, Functions — instead of hallucinating APIs.

18 chapters · ~648 pages · 1:1 verbatim · by [Uppify](https://github.com/uppifyagency)

</div>

---

## What is this?

`shopify-development` is a **reference skill**: the complete Shopify developer documentation, captured 1:1 and reorganized so an AI agent with **zero context** can navigate straight to the precise answer it needs.

It is **not** a set of summaries. The reference is kept verbatim (parameter tables, schemas, code examples). A thin navigation layer — a router + symbol indexes — sits on top so the agent greps the right heading and reads only that slice.

## What's inside

| Area | Coverage |
|------|----------|
| **Themes & Architecture** | Layouts, JSON templates, sections, blocks, snippets, settings, config, locales (full schemas) |
| **Liquid Reference** | 135 objects · 28 tags · 155 filters — signatures, parameters, examples |
| **Theme APIs** | Ajax cart API + Section Rendering API |
| **Custom Apps & Extensions** | OAuth/session tokens, App Bridge, webhooks, billing, Admin/Checkout/Customer-account/POS extensions |
| **Headless & Hydrogen** | Storefront API usage, Hydrogen, Oxygen, Customer Account API |
| **Shopify Functions** | Discounts, validation, cart transform, delivery/payment customization |
| **Custom Data & AI** | Metafields, metaobjects, agentic commerce (UCP/MCP) |

## Install

### Claude Code
```bash
git clone https://github.com/uppifyagency/Shopify-Development-Skill-for-AI-Agents.git
cp -r Shopify-Development-Skill-for-AI-Agents/shopify-development ~/.claude/skills/
```
For a single project instead of globally, copy into `<your-project>/.claude/skills/`.

### Amp
```bash
cp -r Shopify-Development-Skill-for-AI-Agents/shopify-development ~/.config/agents/skills/
```
Project-local: copy into `.agents/skills/`.

Then just ask your agent to build something for Shopify — it auto-loads the skill on any Shopify task.

## How it works

```
shopify-development/
├── SKILL.md            # router: orientation + task-routing + lookup protocol
├── cheatsheet.md       # one-page quick reference
├── indexes/            # liquid-objects, liquid-filters, liquid-tags, schemas, task-routing
└── reference/          # 18 chapters, verbatim 1:1
```

1. **Install** the folder into your agent's skills directory.
2. The agent **auto-loads** `SKILL.md` on any Shopify task.
3. It **routes** via the indexes → opens the right reference file at the right heading → reads only that slice. Verbatim, traceable, never guessed.

## Scope & limits

Covers the conceptual + how-to + reference (Liquid/schema/API-usage) docs 1:1. It intentionally does **not** dump the giant auto-generated GraphQL/REST schemas (Admin, Storefront, Customer Account) — those change often and are best queried live via the [Shopify Dev MCP server](https://www.npmjs.com/package/@shopify/dev-mcp). Every omitted reference is listed (with its URL) inside the relevant chapter.

## Contact

Questions or work with us → **email.vlad.vrinceanu@gmail.com**

## License & attribution

The skill structure, indexes and navigation are released under the [MIT License](LICENSE).
The documentation content under `shopify-development/reference/` is derived from Shopify's developer
documentation (shopify.dev) and remains © Shopify Inc.; every page links to its official source.
See [NOTICE](NOTICE). Uppify is an independent project and is not affiliated with or endorsed by Shopify.
