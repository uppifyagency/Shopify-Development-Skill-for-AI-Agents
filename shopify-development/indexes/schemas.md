# Shopify Theme Schemas & Architecture — Lookup Index

**How to use:** Open `reference/02-key-concepts.md` and Grep for the named `## 2.x` heading
(or the more specific `### 2.x.y` / `##### attr` heading) in the "Grep for" column.
Top-level sections are `## 2.1 … 2.10`. This index tells you WHERE a schema, attribute,
or input type is documented — it is not a substitute for reading the section.

Derived entirely from `reference/02-key-concepts.md` (~9,400 lines). All content verified against the file.

---

## 1. Schema map

| Schema / construct | What it covers | Grep for (`reference/02-key-concepts.md`) |
| --- | --- | --- |
| **Theme architecture (overview)** | Directory structure, component types, assets, the 9 theme folders | `## 2.1`, then `### Theme Architecture` |
| **Layouts** (`theme.liquid`, custom layouts) | Layout subtypes (General / Checkout), `content_for_header`, `content_for_layout`, template-specific CSS | `## 2.2`, then `### Layouts` |
| **checkout.liquid** | Checkout layout (Plus only, deprecated for Info/Shipping/Payment + Thank-you/Order-status) | `### 2.2.1 checkout.liquid` |
| **Templates (overview)** | JSON vs Liquid, **Template types** list, location | `## 2.3`, then `#### Template types` |
| **Template types list** | 404, agents.md.liquid, article, blog, cart, collection, gift_card.liquid, index, list-collections, llms-full.txt.liquid, llms.txt.liquid, page, password, product, robots.txt.liquid, search, metaobject | `#### Template types` |
| **JSON template structure** (root: `layout`, `wrapper`, `sections`, `order`; section data format `type`/`disabled`/`settings`/`blocks`/`block_order`) | The fixed JSON template schema + `wrapper` property | `### 2.3.1 JSON templates`, then `##### Schema` |
| **Liquid templates** | `.liquid` markup templates | `### 2.3.2 Liquid templates` |
| **Alternate templates** | `product.alternate.json` naming/suffix | `### 2.3.3 Alternate templates` |
| **Metaobject theme templates** | `metaobject/{type}` templates | `### 2.3.4 Metaobject theme templates` |
| Per-template-type pages | 404, agents.md, article, blog, cart, collection, gift_card, index, list-collections, llms-full.txt, llms.txt, page, password, product, robots.txt, search | `### 2.3.5`–`### 2.3.20` (one per template) |
| **Section `{% schema %}`** | Top-level section schema and all its attributes (see §below) | `### 2.4.1 Section schema`, then `#### Section schema` |
| **Section groups JSON** (root: `type`, `name`, `sections`, `order`) | Section-group data file structure + section-data format | `## 2.5`, then `### Section groups` → `#### Schema` |
| **Migrate static sections → section groups** | Conversion guidance | `### 2.5.1 Migrate static sections to section groups` |
| **Block `{% schema %}`** (theme blocks) | Theme-block schema attributes (see §below) | `### 2.6.2 Block schema`, then `#### Block schema` |
| **Theme blocks (Quick Start)** | Creating theme blocks, `/blocks` folder | `### 2.6.1 Theme blocks (Quick Start)` |
| **Theme block targeting** (`@theme`, `@app`, explicit type, recommended blocks) | Which blocks a section/block accepts as children | `### 2.6.3 Theme block targeting` |
| **Static blocks** (`{% content_for 'block' %}`) | Statically rendering a single block | `### 2.6.4 Static blocks` |
| **Dynamic sources (theme blocks)** | Connecting block settings to dynamic data | `### 2.6.5 Dynamic sources (theme blocks)` |
| **Section blocks** (locally-defined blocks in a section schema) | Blocks defined inside a section's `blocks` array | `### 2.6.6 Section blocks` |
| **App blocks for themes** (`@app`, app-block wrapper) | App-provided blocks | `### 2.6.7 App blocks for themes` |
| **AI generated theme blocks** | AI-authored blocks | `### 2.6.8 AI generated theme blocks` |
| **Snippets** (`{% render %}`, scoping, LiquidDoc `{% doc %}` `@param`/`@example`) | Reusable Liquid; not shown in editor | `## 2.7`, then `### Snippets` |
| **Theme settings (overview)** | Config-driven Theme settings; input vs sidebar categories; conditional settings; translate settings | `## 2.8`, then `### Settings` |
| **Input setting types** | Every configurable input type + standard attributes (see §2 below) | `### 2.8.1 Input settings` |
| **Sidebar settings** (`header`, `paragraph`; `content`, `info`) | Informational, non-value settings | `### 2.8.2 Sidebar settings` |
| **Dynamic data sources** | Resource attrs & metafield values bound to settings | `### 2.8.3 Dynamic data sources` |
| **Fonts** (`font_picker`, Shopify font library, `font_modify`) | Font settings & the font object | `### 2.8.4 Fonts` |
| **Config files (overview)** | The 3 config files + `theme_info` metadata context | `## 2.9`, then `### Config` → `#### Subtypes` |
| **settings_schema.json** (array of `{name, settings}`; `theme_info` object) | Theme-settings schema + theme metadata attributes | `### 2.9.1 settings_schema.json` |
| **settings_data.json** (`current`, `presets`, `platform_customizations`; theme presets) | Saved setting values; presentational settings; limits (1.5MB, ≤5 presets) | `### 2.9.2 settings_data.json` |
| **markets.json** | Market-specific customization inheritance (single parent per market) | `### 2.9.3 markets.json` |
| **Locales (overview)** | Storefront vs Schema locale files; Category/Group/Description hierarchy; naming (IETF tags, `*.default.json`) | `## 2.10`, then `### Locales` → `#### Subtypes` |
| **Storefront locale files** (`.json`) | Storefront content translations; `t` filter | `### 2.10.1 Storefront locale files` |
| **Schema locale files** (`.schema.json`) | Theme-editor settings translations; `t:` references | `### 2.10.2 Schema locale files` |
| **Section schema `locales` object** | Per-section translations (separate from `/locales` dir) | `### 2.4.1 Section schema` → `##### locales` |

### Section `{% schema %}` attributes — quick jump

All under `### 2.4.1 Section schema`. Grep the `##### <attr>` heading:

| Attribute | Purpose | Grep for |
| --- | --- | --- |
| `name` | Section title in the theme editor | `##### name` |
| `tag` | Wrapper HTML element (`article`/`aside`/`div`/`footer`/`header`/`section`) | `##### tag` |
| `class` | Extra class added to the `shopify-section` wrapper | `##### class` |
| `limit` | Max times the section can be added (1 or 2) | `##### limit` |
| `settings` | Section-specific input/sidebar settings array | `##### settings` |
| `blocks` | Locally-defined or referenced blocks (`type`,`name`,`limit`,`settings`; `@theme`/`@app`; dynamic titles) | `##### blocks` |
| `max_blocks` | Lower the 50-block-per-section limit | `##### max_blocks` |
| `presets` | Add-section picker configs (`name`,`category`,`settings`,`blocks`) | `##### presets` |
| `default` | Default config for statically-rendered sections | `##### default` |
| `locales` | Per-section translation strings | `##### locales` |
| `enabled_on` | Restrict to template/section-group types (`templates`,`groups`) | `##### enabled_on` |
| `disabled_on` | Exclude template/section-group types (`templates`,`groups`) | `##### disabled_on` |

### Block `{% schema %}` attributes (theme blocks) — quick jump

All under `### 2.6.2 Block schema`. Grep the `##### <attr>` heading:

| Attribute | Purpose | Grep for |
| --- | --- | --- |
| `name` | Block title in the theme editor (+ dynamic titles from `heading`/`title`/`text` ids) | `##### name` |
| `settings` | Block-specific input settings array | `##### settings` |
| `blocks` | Accepted child blocks (`@app`, `@theme`, explicit type; nested ≤8 deep; `{% content_for 'blocks' %}`) — note: theme blocks can't define LOCAL blocks | `##### blocks` |
| `presets` | Add-block picker configs (`name`,`category`,`settings`,`blocks`) | `##### presets` |
| `tag` | Wrapper element (any string ≤50 chars, or `null` for no wrapper) | `##### tag` |
| `class` | Extra class added to the `shopify-block` wrapper | `##### class` |

> Section vs block presets share the same shape (`name`,`category`,`settings`,`blocks`). Static blocks don't count toward `max_blocks`. `{{ block.shopify_attributes }}` is required on the top-level element for editor compatibility (esp. with `"tag": null`).

---

## 2. Input setting types reference (§2.8.1)

Source: `### 2.8.1 Input settings`. **Standard attributes** (Grep `##### Standard attributes`):
`type` (req), `id` (req), `label` (req), `default`, `info`.
Grep any type below as `##### <type>`.

**30 input setting types total: 7 basic + 23 specialized.**

### Basic input settings (7) — Grep `##### Basic input settings`

| Type | Purpose (1-line) |
| --- | --- |
| `checkbox` | Boolean toggle (on/off); returns a boolean, `false` by default. |
| `number` | Single numeric field; returns a number or `nil`; supports `placeholder`. |
| `radio` | Single-choice radio group; requires `options` (`value`/`label`); returns string. |
| `range` | Slider + input; requires `min`,`max`,`default`; optional `step`,`unit`. |
| `select` | Drop-down or segmented control; requires `options`; optional `group`. |
| `text` | Single-line text; returns string/empty; supports `placeholder`. |
| `textarea` | Multi-line text; returns string/empty; supports `placeholder`. |

### Specialized input settings (23) — Grep `##### Specialized input settings`

| Type | Purpose (1-line) |
| --- | --- |
| `article` | Article picker; returns an `article` object (no `default`). |
| `article_list` | Multi-article picker; array of `article` objects; `limit` (≤50). |
| `blog` | Blog picker; returns a `blog` object (no `default`). |
| `collection` | Collection picker; returns a `collection` object (no `default`). |
| `collection_list` | Multi-collection picker; array of `collection` objects; `limit` (≤50). |
| `color` | Color picker; returns a `color` object or blank. |
| `color_background` | Text field for CSS `background` (no images); returns string. |
| `color_scheme` | Picks a scheme from `color_scheme_group`; returns the scheme object. |
| `color_scheme_group` | Defines schemes (`definition` of `header`/`color`/`color_background` + `role` mapping); `settings_schema.json` only. |
| `font_picker` | Font picker from Shopify font library; returns a `font` object; `default` required. |
| `html` | Multi-line HTML field (strips `<html>`/`<head>`/`<body>`); `placeholder`. |
| `image_picker` | Image picker (alt text + focal point); returns `image` object (no `default`). |
| `inline_richtext` | Inline formatted HTML (bold/italic/link), no `<p>` wrapper. |
| `link_list` | Menu picker; returns a `linklist` object; `default` = `main-menu`/`footer`. |
| `liquid` | Multi-line HTML + limited Liquid (≤50kb); returns string. |
| `metaobject` | Single metaobject picker; requires `metaobject_type`; returns `metaobject` object. |
| `metaobject_list` | Multi-metaobject picker; `metaobject_type` + `limit` (≤50). |
| `page` | Page picker; returns a `page` object (no `default`). |
| `product` | Product picker; returns a `product` object (no `default`). |
| `product_list` | Multi-product picker; array of `product` objects; `limit` (≤50). |
| `richtext` | Multi-line rich text (`<p>`/`<ul>` top-level only in `default`). |
| `text_alignment` | Segmented control of `left`/`right`/`center`; returns string. |
| `url` | URL field + resource picker (articles/blogs/collections/pages/products). |
| `video` | Shopify-hosted video picker; returns a `video` object (no `default`). |
| `video_url` | YouTube/Vimeo URL field; requires `accept` (`youtube`/`vimeo`); exposes `.id`/`.type`. |

### Sidebar settings (NOT input settings) — §2.8.2

`header` and `paragraph` are **sidebar** (informational, value-less) settings, documented separately under
`### 2.8.2 Sidebar settings`. Shared attrs: `type` (req), `content` (req); `header` also supports `info`.
Grep `##### header` / `##### paragraph` there. (They do NOT appear in the §2.8.1 input list.)

---

## Sections mapped

Mapped against the actual file:
- `## 2.1` Theme Architecture, `## 2.2` Layouts (+ `2.2.1` checkout.liquid), `## 2.3` Templates (+ `2.3.1` JSON schema, `2.3.2`–`2.3.20` types/pages).
- `## 2.4` Sections → `2.4.1 Section schema` (all 12 attributes verified verbatim).
- `## 2.5` Section groups (root schema + section-data) and `2.5.1` migration.
- `## 2.6` Blocks → `2.6.1`–`2.6.8` (Quick Start, `2.6.2 Block schema` = 6 attributes, targeting, static, dynamic, section blocks, app blocks, AI blocks).
- `## 2.7` Snippets, `## 2.8` Settings → `2.8.1 Input settings` (full type enumeration), `2.8.2 Sidebar settings`, `2.8.3` Dynamic data sources, `2.8.4` Fonts.
- `## 2.9` Config → `2.9.1` settings_schema.json, `2.9.2` settings_data.json, `2.9.3` markets.json.
- `## 2.10` Locales → `2.10.1` Storefront, `2.10.2` Schema locale files.

**Not located / not present:** the §2.8.1 input list contains **no** `header`/`paragraph` entries (those are §2.8.2 sidebar settings) — counted separately above. No other requested constructs were missing; the file's specialized list adds `article_list`, `color_scheme_group`, `metaobject`, and `metaobject_list` beyond the example list in the task prompt.
