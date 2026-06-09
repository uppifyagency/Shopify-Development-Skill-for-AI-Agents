# Task routing — "I need to do X" → where to look

Detailed map from a concrete development task to the exact reference file(s) and section(s).
After landing on a file, `Grep` the named heading and `Read` only that slice. Paths are
relative to the skill root (`../reference/...`, `../indexes/...`).

## Themes — Liquid authoring

- **Output a value / read store data** (product, cart, customer, shop…) →
  `../indexes/liquid-objects.md` → `reference/07-liquid-objects.md` (`### <object>`).
- **Loop, conditionals, assign, render a snippet/section** →
  `../indexes/liquid-tags.md` → `reference/08-liquid-tags.md` (`## <tag>`).
- **Transform/format a value** (money, image_url, date, t, where, map…) →
  `../indexes/liquid-filters.md` → `reference/09-...` (A–L) or `reference/10-...` (M–Z) (`## <cat> — <filter>`).
- **Images / responsive media** → filters `image_url`, `image_tag`, `img_tag`, objects `image`, `media`, `model`, `video`.
- **Money / currency** → filters `money*`, object `money`, `currency`; localization in ref/05 (markets).
- **Translation / i18n** → filters `t`/`translate`, object `localization`; ref/02 §2.10 Locales.

## Themes — Architecture & structure (reference/02)

- **Theme file/folder structure & how it fits together** → §2.1 Theme Architecture.
- **Layouts** (`theme.liquid`, `checkout.liquid`, alternate layouts) → §2.2.
- **Templates** (JSON vs Liquid, product/collection/cart/page/blog/search/404, alternate, metaobject) → §2.3.
- **Sections** (Liquid + `{% schema %}`, presets, blocks within, app/static sections) → §2.4 + `../indexes/schemas.md`.
- **Section groups** (header/footer/aside dynamic areas, migrate) → §2.5.
- **Blocks** (theme blocks, schema, targeting, static vs dynamic, app blocks, AI blocks) → §2.6 + `../indexes/schemas.md`.
- **Snippets** (`render`, scope) → §2.7.
- **Settings** (input setting types, sidebar settings, dynamic sources, fonts) → §2.8 + `../indexes/schemas.md`.
- **Config** (`settings_schema.json`, `settings_data.json`, `markets.json`) → §2.9.
- **Locales** (storefront vs schema locale files) → §2.10.

## Themes — Build, quality, tooling, features

- **Start a theme / Skeleton / customize** → reference/01.
- **Performance / Core Web Vitals / stylesheet subsetting** → reference/03 (Performance).
- **Accessibility** → reference/03 (Accessibility).
- **Theme editor integration / preview inspector / design / color system** → reference/03.
- **Version control / file transformation / deceptive code policy** → reference/03.
- **Shopify CLI for themes** (dev, push/pull, environments, CI/CD, migrate) → reference/04 (CLI).
- **Theme Check** (lint config, commands, checks) → reference/04 (Theme Check).
- **GitHub integration / VS Code / Prettier / LiquidDoc / Theme Inspector / Lighthouse CI** → reference/04.

## Themes — Dynamic behavior (reference/11)

- **Ajax cart** (`/cart/add.js`, `update.js`, `change.js`, `clear.js`, `cart.js`) → §Ajax API → Cart.
- **Predictive search / product JSON / recommendations** → §Ajax API.
- **Re-render a section without reload** → §Section Rendering API.

## Themes — Commerce features (reference/05)

- **Subscriptions / purchase options / selling plans (theme side)** → §Pricing and payments → subscriptions.
- **Discounts display, unit pricing, accelerated checkout, installments** → §Pricing and payments.
- **Markets / multi-currency / multi-language** → §Markets.
- **SEO / metadata / robots.txt / hreflang** → §SEO.
- **Site navigation, search, storefront/tag filtering** → §Site navigation and search.
- **Product merchandising, media, recommendations, bundles, gift cards** → §Product merchandising.
- **Delivery/pickup, customer engagement, trust & security (captcha, badges)** → respective sections.
- **Migrate to Online Store 2.0** → §Migrating to Online Store 2.0 (also ref/02 §2.3 JSON templates).

## Themes — Distribution (reference/06)

- **Theme Store requirements / submit / review / testing / revenue share** → reference/06.

## Custom apps (reference/12–14)

- **App architecture, custom vs public** → ref/12.
- **Authentication/authorization** (OAuth, session tokens, token exchange, access scopes) → ref/12 (Auth).
- **App Bridge** (embed in admin, navigation, resource picker) → ref/12 (App Bridge).
- **Shopify CLI for apps / Remix-React Router template / scaffolding / deploy** → ref/12 (Build tools).
- **Webhooks** (subscribe, delivery filtering, verify, troubleshoot, mandatory/compliance) → ref/13 (Webhooks).
- **Billing** (Shopify App Pricing vs Manual Pricing legacy, subscriptions, usage, trials, one-time) → ref/13 (Billing).
- **App config** (`shopify.app.toml`, scopes declaration) → ref/13 (App configuration).
- **Distribution & launch / App Store review / Built for Shopify** → ref/13 (Distribution & launch).
- **Compliance / protected customer data / privacy** → ref/13 (Compliance).
- **Admin UI extensions** (admin action/block/print, targets, target APIs, web components) → ref/14.
- **Checkout UI extensions / Customer account UI extensions / POS UI extensions** → ref/14.
- **Theme app extensions** (app blocks/app embed blocks — bridge apps↔themes) → ref/14 + ref/02 §2.6.

## Headless / Hydrogen (reference/15)

- **Decide headless vs theme / bring-your-own-stack / Storefront API tokens** → ref/15 (Headless overview).
- **Hydrogen** (getting started, routing, data fetching, caching, SEO, markets, deploy) → ref/15 (Hydrogen).
- **Oxygen** (deployments, environments, CI/CD) → ref/15 (Oxygen).
- **Customer Account API** (auth, usage, with Hydrogen) → ref/15 (Customer Account API).
- **Storefront API usage** (products/collections, cart, pagination, metafields) → ref/15 (Storefront API usage).
- For the full Storefront/Customer **GraphQL schema** → use Shopify Dev MCP (not in this book; URLs listed in ref/15 `Pagine aggiuntive`).

## Shopify Functions (reference/16)

- **How functions work / Wasm / Rust vs JS / input queries / testing / deploy / limits** → ref/16 (Overview & infrastructure).
- **Discounts** (product/order/shipping, unified Discount API) → ref/16 §Discount.
- **Cart & checkout validation** → ref/16 §cart-and-checkout-validation.
- **Cart transform** (bundles, line-item changes) → ref/16 §cart-transform.
- **Delivery customization / Payment customization / Fulfillment constraints / Order routing / Pickup** → ref/16 (respective).

## Custom data (reference/17)

- **Metafields** (definitions, owner types, the full TYPES table + validations, access, display) → ref/17 (Metafields).
- **Metaobjects** (definitions, entries, capabilities, use in themes/templates and via API) → ref/17 (Metaobjects).
- **Read/write custom data via Liquid / Admin API / Storefront API** → ref/17 (Reading/writing) + Liquid object `metafield`, `metaobject`.

## AI / agentic commerce (reference/18)

- **UCP / agentic commerce / profiles / catalog / cart-mcp / checkout-mcp** → ref/18 (UCP, MCP sections).
- **Storefront MCP / Customer-account MCP / AI Toolkit** → ref/18.
- **Shopify Dev MCP** (`@shopify/dev-mcp`, tools, install) → ref/18 (Dev MCP).
- **Theme-side agent files** (`agents.md.liquid`, `llms.txt.liquid`, `llms-full.txt.liquid`) → ref/02 §Templates (agents-md/llms-txt) and ref/18.
- ⚠️ This area evolves fast — check ref/18 `Cosa NON è stato trovato` for unverified items.
