# Shopify Themes — Documentazione completa (Book)

> **Fonte:** https://shopify.dev/docs/storefronts/themes
> **Estratto il:** 2026-06-08
> **Obiettivo:** riproduzione fedele (1:1) di tutta la sezione *Themes* della documentazione Shopify, organizzata come libro navigabile.

## Nota sul metodo
Il contenuto è estratto pagina per pagina dalla doc ufficiale. Per ogni pagina sono preservati: titoli, testo, liste, **tabelle di parametri/attributi**, **code block** (Liquid/JSON/JS verbatim), note e avvisi. È escluso solo il "chrome" del sito (barra di navigazione, menu laterale, footer, widget "On this page"). Le eventuali pagine non catturate sono elencate esplicitamente alla fine di ogni capitolo, così la copertura resta tracciabile.

---

## Struttura del libro

Legenda: `›` = voce con sotto-pagine espandibili.

### 1. GETTING STARTED → [`01-getting-started.md`](01-getting-started.md)
- Overview
- › Quick start

### 2. KEY CONCEPTS → [`02-key-concepts.md`](02-key-concepts.md)
- Architecture
- › Layouts
- › Templates
- › Sections
- › Section groups
- › Blocks
- Snippets
- › Settings
- › Config
- › Locales

### 3. BEST PRACTICES → [`03-best-practices.md`](03-best-practices.md)
- Overview
- Sections and blocks
- JavaScript and stylesheet tags
- › Performance
- Accessibility
- › Theme editor
- › Design
- Merchant stores
- Version control
- File transformation
- Deceptive code

### 4. DEVELOPER TOOLS → [`04-developer-tools.md`](04-developer-tools.md)
- Overview
- › CLI
- GitHub integration
- VS Code extension
- Prettier plugin
- LiquidDoc
- › Theme Check
- Theme editor
- Code editor
- Theme Access app
- › Dev stores
- Collaborator accounts
- › Theme Inspector
- Lighthouse CI

### 5. THEME FEATURES → [`05-theme-features.md`](05-theme-features.md)
- Overview
- Integrating apps
- › Product merchandising
- › Pricing and payments
- › Delivery and fulfillment
- › Customer engagement
- › Markets
- › Site navigation and search
- › SEO
- › Trust and security
- › Migrating to Online Store 2.0
- Sign-in redirects
- Troubleshooting

### 6. SELL THEMES → [`06-sell-themes.md`](06-sell-themes.md)
- › Theme Store
  - Overview
  - Requirements
  - › Testing
  - › Review process
  - › Theme success
  - Theme revenue share

---

## Copertura finale (estrazione completata)

### Parte 1 — Documentazione Themes (sezione `/themes/`)
| # | Capitolo | File | Pagine | Righe |
|---|----------|------|-------:|------:|
| 1 | Getting Started | [`01-getting-started.md`](01-getting-started.md) | 3 | 357 |
| 2 | Key Concepts (Architecture) | [`02-key-concepts.md`](02-key-concepts.md) | 51 | 9.442 |
| 3 | Best Practices | [`03-best-practices.md`](03-best-practices.md) | 16 | 1.647 |
| 4 | Developer Tools | [`04-developer-tools.md`](04-developer-tools.md) | 18 | 2.878 |
| 5 | Theme Features | [`05-theme-features.md`](05-theme-features.md) | 56 | 5.953 |
| 6 | Sell Themes (Theme Store) | [`06-sell-themes.md`](06-sell-themes.md) | 13 | 3.029 |

### Parte 2 — Reference per lo sviluppo (Liquid + Theme APIs, sezione `/api/`)
| # | Capitolo | File | Pagine | Righe |
|---|----------|------|-------:|------:|
| 7 | Liquid — Overview & Objects | [`07-liquid-objects.md`](07-liquid-objects.md) | 137 | 7.335 |
| 8 | Liquid — Tags | [`08-liquid-tags.md`](08-liquid-tags.md) | 28 | 2.733 |
| 9 | Liquid — Filters (A–L) | [`09-liquid-filters-part1.md`](09-liquid-filters-part1.md) | 89 | 6.535 |
| 10 | Liquid — Filters (M–Z) | [`10-liquid-filters-part2.md`](10-liquid-filters-part2.md) | 77 | 4.292 |
| 11 | Theme APIs (Ajax + Section Rendering) | [`11-theme-apis.md`](11-theme-apis.md) | 7 | 2.046 |

### Parte 3 — Piattaforma dev (Apps, Headless, Functions, Custom Data, AI)
| # | Capitolo | File | Pagine | Righe |
|---|----------|------|-------:|------:|
| 12 | Custom Apps — Foundations & Auth | [`12-apps-foundations.md`](12-apps-foundations.md) | 22 | 2.823 |
| 13 | Custom Apps — Build & Operate | [`13-apps-build-operate.md`](13-apps-build-operate.md) | 21 | 4.296 |
| 14 | App Extensions | [`14-app-extensions.md`](14-app-extensions.md) | 14 | 3.343 |
| 15 | Headless & Hydrogen | [`15-headless-hydrogen.md`](15-headless-hydrogen.md) | 39 | 7.936 |
| 16 | Shopify Functions | [`16-functions.md`](16-functions.md) | 23 | 5.669 |
| 17 | Custom Data (Metafields & Metaobjects) | [`17-custom-data.md`](17-custom-data.md) | 16 | 5.356 |
| 18 | AI & Agentic Commerce | [`18-ai-agentic.md`](18-ai-agentic.md) | 18 | 1.839 |
| | **TOTALE (1+2+3)** | | **~648** | **77.632** |

**Dimensione totale:** ~3,3 MB di markdown.
Liquid coperto: **135 objects, 28 tags, 166 filters**.

### Per disegno NON estratto (reference auto-generati → via MCP, non dump)
Elencati come URL negli appendici `## Pagine aggiuntive` dei rispettivi capitoli, MAI nascosti:
- **Admin API (GraphQL/REST)** schema completo
- **Storefront API** + **Customer Account API** schema
- **Hydrogen / Hydrogen React** reference per-componente/hook
- **Polaris** component reference
- **Webhook topic** enum completo
- **App Bridge / Checkout UI** reference per-componente

### Note di fedeltà — Parte 3
- **Cap. 13:** doc billing ristrutturata (ora "Shopify App Pricing"; vecchia Billing API = "Manual Pricing legacy") — catturate entrambe.
- **Cap. 15:** 2 pagine con code JSX/PKCE rese in modo imperfetto dal fetch → note inline con rimando alla fonte.
- **Cap. 18 (area in evoluzione):** verificato dal codice `@shopify/dev-mcp@1.14.0` e dai repo GitHub; UCP `/docs/agents`, Storefront/Checkout/Cart MCP confermati; Universal Cart API e alcuni tool Customer-Accounts MCP non confermati (elencati in `Cosa NON è stato trovato`).

### Note di fedeltà — Parte 2
- **Cap. 7 — objects:** index della doc è client-rendered (non scrappabile), quindi l'elenco objects è stato ricostruito dal set canonico + cross-reference; 135 objects catturati, 1 slug inesistente (`payment`) scartato. Trimming minimo segnalato su `country_option_tags` (array stati USA) e `transaction` (YAML receipt).
- **Cap. 8 — tags:** 28 tag catturati (incluso `doc`/LiquidDoc); `deprecated-tags` non ha pagina indice (404), ma il suo unico leaf `include` è catturato.
- **Cap. 9/10 — filters:** index e pagine-categoria sono client-rendered; enumerazione fatta dalla tassonomia ufficiale + `filters.json` di `theme-liquid-docs`, con output di esempio presi dalle pagine live. Split A–L / M–Z complementare, senza overlap. `class_list` recuperato via ricerca (404 al fetch diretto).
- **Cap. 11 — APIs:** gli endpoint cart (`/cart/add.js`, `/update.js`, ecc.) NON sono pagine separate: vivono nella pagina "Cart". Section Rendering API è sotto `/api/ajax/section-rendering`.

### Note di fedeltà (lette in fondo a ciascun capitolo)
- **Cap. 2 — `settings/fonts`:** catturati prosa, tabelle e code block; l'elenco esaustivo delle centinaia di handle font (`family_weight`) è l'unico blocco volutamente omesso, segnalato con URL fonte.
- **Cap. 5 — "Integrating apps":** non ha pagina propria sotto `/themes/`; risolve al contenuto app-blocks (`architecture/blocks/app-blocks`), catturato per intero. Due sample di codice risultano troncati a monte da Shopify stessa (filtri storefront) — segnalato inline con rimando a Dawn.
- **Cap. 4 — Shopify CLI:** il reference per-comando vive fuori dall'albero (`/docs/api/shopify-cli/theme`), linkato come indice. Tool legacy (CLI 2.x, Theme Kit) non espansi.
- **Slug corretti durante il crawl** (gli indizi della sidebar differivano dagli URL reali): `best-practices/editor`, `tools/online-editor`, `tools/shopify-liquid-vscode`, `tools/liquid-prettier-plugin`, `trust-security`, `delivery-fulfillment`, `sign-in`, `store/test-theme`, `store/success`.

*Stato estrazione: ✅ completata. Ogni capitolo riporta in fondo l'elenco completo degli URL catturati e di eventuali pagine saltate.*
