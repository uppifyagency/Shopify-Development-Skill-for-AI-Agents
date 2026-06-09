# Shopify dev — cheatsheet (quick reference)

The single-page essentials. For exact signatures/params, jump to the reference via the indexes.

## Theme file structure (Online Store 2.0)

```
theme/
├── layout/        theme.liquid (required), checkout.liquid, password.liquid
├── templates/     *.json (OS2.0) or *.liquid — product.json, collection.json, index.json…
│   └── customers/ account, login, order…
├── sections/      *.liquid with {% schema %}; *.json section groups (header-group.json…)
├── blocks/        theme blocks (*.liquid with {% schema %})
├── snippets/      *.liquid (rendered via {% render %})
├── assets/        css, js, images, fonts
├── config/        settings_schema.json, settings_data.json
└── locales/       en.default.json (storefront), en.default.schema.json (editor)
```

## Liquid essentials

```liquid
{{ output }}                      {% logic %}
{% assign x = product.title %}
{% if cart.item_count > 0 %} … {% elsif … %} … {% else %} … {% endif %}
{% for p in collection.products %} {{ forloop.index }} {{ p.title }} {% endfor %}
{% render 'snippet', var: value %}   {# preferred; isolated scope. include is deprecated #}
{% liquid                            # multi-line, tagless
  assign n = cart.item_count
  if n > 0
    echo n
  endif
%}
{{ 'app.js' | asset_url | script_tag }}
{{ 'style.css' | asset_url | stylesheet_tag }}
```

Most-used filters: `money`, `money_with_currency`, `image_url` (`| image_url: width: 800`),
`image_tag`, `t` (translate), `default`, `where`, `map`, `sort`, `escape`, `json`, `date`,
`url_for_type`, `link_to`. → full list in [indexes/liquid-filters.md](indexes/liquid-filters.md).

## Section skeleton (with schema)

```liquid
<div class="my-section">{{ section.settings.heading }}</div>

{% schema %}
{
  "name": "My section",
  "tag": "section",
  "settings": [
    { "type": "text", "id": "heading", "label": "Heading", "default": "Hello" }
  ],
  "blocks": [
    { "type": "item", "name": "Item", "settings": [ … ] }
  ],
  "max_blocks": 16,
  "presets": [ { "name": "My section" } ]
}
{% endschema %}
```
Access: `section.settings.<id>`, loop `section.blocks` → `block.settings.<id>` + `{{ block.shopify_attributes }}`.
Full schema attrs & all input setting types → [indexes/schemas.md](indexes/schemas.md), ref/02 §2.4/§2.6/§2.8.

## Settings input types (most used)

`text`, `textarea`, `richtext`, `inline_richtext`, `html`, `number`, `range`, `checkbox`,
`select`, `radio`, `color`, `color_scheme`, `color_background`, `font_picker`, `image_picker`,
`url`, `video`, `video_url`, `product`, `product_list`, `collection`, `collection_list`,
`blog`, `page`, `article`, `link_list`, `liquid`, `text_alignment`. → ref/02 §2.8.

## Ajax cart (theme JS) — ref/11

```
POST /cart/add.js            add items
GET  /cart.js                current cart (JSON)
POST /cart/update.js         update line quantities/attributes/note
POST /cart/change.js         change one line by id/line
POST /cart/clear.js          empty cart
```
Re-render sections without reload → Section Rendering API (`?sections=` / `sections` param).

## Shopify CLI (themes) — ref/04

```
shopify theme dev            local preview + hot reload
shopify theme push / pull    sync with store
shopify theme check          lint (Theme Check)
shopify theme init           new theme from Skeleton
```

## Shopify CLI (apps) — ref/12

```
shopify app dev              run app locally with tunnel
shopify app deploy           deploy app + extensions
shopify app generate extension
```

## Choosing a surface

| Want… | Use |
|---|---|
| Standard storefront, fast to build | Online Store **theme** (Liquid) |
| Fully custom storefront / React | **Headless + Hydrogen** (Storefront API) |
| Extend the admin / backend logic / sell in App Store | **Custom app** + Admin API |
| Custom discount/checkout/delivery logic | **Shopify Functions** |
| Extra fields on any resource | **Metafields / Metaobjects** |
| Make store usable by AI agents | **UCP / MCP** (ref/18) |

## What's NOT in this book (→ Shopify Dev MCP)

Full Admin/Storefront/Customer **GraphQL schemas**, per-component Hydrogen/Polaris/Checkout-UI
reference, full webhook-topic enum. URLs are listed in each chapter's `## Pagine aggiuntive`.
