# 18. AI & Agentic Commerce

> **Cattura del:** 2026-06-08 (la cattura del libro circostante riflette la stessa data).
>
> ⚠️ **Quest'area evolve rapidamente.** L'agentic commerce su Shopify (UCP, MCP storefront/catalog, AI Toolkit) è documentazione *nuova e in rapido cambiamento*. Endpoint, nomi di tool, versioni del protocollo e disponibilità delle feature cambiano spesso — Shopify stessa avvisa che "API URLs are subject to change". Ogni sezione di questo capitolo riporta la fonte (`> Fonte:`) verificata via fetch diretto delle pagine ufficiali. Dove un argomento è annunciato ma non documentato, o dove non è stato possibile confermare un contenuto, è segnalato con una nota `> ⚠️ Nota: non verificato / in evoluzione`.
>
> **Nota di scope.** I file *lato tema* (`agents.md.liquid`, `llms.txt.liquid`, `llms-full.txt.liquid`) sono trattati nel capitolo dedicato all'architettura dei temi. Qui catturiamo i documenti di **piattaforma/concetto**: il protocollo UCP, i server MCP per agenti shopping, il Dev MCP per sviluppatori e la guida a costruire esperienze AI su Shopify. Una sola pagina di piattaforma (`agents.md.liquid` come documento di discovery) è inclusa qui perché definisce l'oggetto `agents` e gli endpoint UCP/MCP a cui gli agenti si agganciano.

Questo capitolo copre cinque aree:

1. **Agentic commerce / UCP** — il Universal Commerce Protocol e come Shopify lo implementa lungo l'intero buyer journey.
2. **llms.txt & agents.md (piattaforma)** — gli endpoint agent-facing auto-generati su ogni store e l'oggetto `agents`.
3. **Storefront / Catalog MCP** — i server MCP per lo shopping agentico (single-store e cross-merchant), Cart MCP, Checkout MCP, Customer Accounts MCP.
4. **Shopify Dev MCP (`@shopify/dev-mcp`)** — l'MCP server per sviluppatori e l'AI Toolkit (install + tool esposti).
5. **Building AI on Shopify** — come costruire esperienze AI con i server MCP e l'AI Toolkit.

---

## 1. Agentic commerce / UCP (Universal Commerce Protocol)

> Fonte: <https://shopify.dev/docs/agents> (fetched 2026-06-08)

### Build commerce agents with UCP

Build unified agentic experiences that securely act on behalf of buyers with the [Universal Commerce Protocol (UCP)](https://ucp.dev) and Shopify's UCP-compliant MCP servers.

#### Start building

[Install the toolkit, then walk the full flow from discovery to order tracking.](https://shopify.dev/docs/agents/get-started/quickstart)

#### How to get started

Install the UCP CLI and [Shopify AI Toolkit](https://shopify.dev/docs/apps/build/ai-toolkit) plugin for your supported AI tool. Built for agent workflows, the CLI provides structured commands to search the Catalog, build carts, create checkouts, hand off buyers, and track orders. The toolkit's `ucp` skill helps agents apply UCP best practices against each merchant's live schema.

Before you install, make sure you have Node.js 18 or higher. The toolkit is supported on any agent that supports the skills format.

##### Claude Code

Install the UCP CLI:

```terminal
npm install -g @shopify/ucp-cli
```

Install the Shopify plugin:

```terminal
claude plugin install shopify-ai-toolkit@claude-plugins-official
```

##### Cursor

Install the UCP CLI:

```terminal
npm install -g @shopify/ucp-cli
```

In Cursor Chat:

```terminal
/add-plugin shopify
```

##### Gemini CLI

Install the UCP CLI:

```terminal
npm install -g @shopify/ucp-cli
```

Install the Shopify extension:

```terminal
gemini extensions install https://github.com/Shopify/shopify-ai-toolkit
```

##### VS Code

Install the UCP CLI:

```terminal
npm install -g @shopify/ucp-cli
```

In Command Palette > Chat, install plugin from source:

```
https://github.com/Shopify/shopify-ai-toolkit
```

#### Universal cart

One Cart, every brand. The Universal Cart API lets AI agents collect items from any merchant, on or off Shopify, into a single, unified cart, all via UCP.

[Join the early access waitlist.](https://docs.google.com/forms/d/e/1FAIpQLSd0p9DP-7ANuhqGoNePjczPhSWmTBwAiFbfIKgs2G95MC9YAQ/viewform?usp=preview)

> ⚠️ Nota: non verificato / in evoluzione — La **Universal Cart API** è in *early access* su waitlist; non esiste (al 2026-06-08) una pagina di reference pubblica con tool/endpoint da catturare. Fonte: la sezione "Universal cart" della pagina `/docs/agents`.

#### How Shopify does UCP

Shopify's MCP tools implement UCP at every step of the buyer journey:

- **Negotiate and authenticate**: Identify your agent and get the right access tier.
- **Discover products**: Search across hundreds of millions of Shopify listings.
- **Carts and checkout**: Build carts, convert them to checkouts, and hand off to the merchant for payment.
- **Monitor orders**: Receive order webhooks and fetch fresh order state on demand.

#### Negotiate and authenticate

"Define a profile so Shopify can verify your agent and apply the right rate limits and tool access." Higher trust tiers unlock broader access, including direct checkout completion. Profiles are hosted at a well-known URL and referenced on every UCP request.

- [Host a UCP profile for capability negotiation and signed-request verification.](https://shopify.dev/docs/agents/profiles)
- [Trust tiers, capability matrix, and rate limits per tier.](https://shopify.dev/docs/agents/profiles/auth-and-rate-limiting)

#### Discover products

Query products across all Shopify merchants with the Global Catalog, or scope results to a single merchant with a Storefront Catalog. When buyers pick a product, fetch the variant details you need to build a cart or hand off to a checkout permalink.

- [Search products across every Shopify merchant from a single endpoint.](https://shopify.dev/docs/agents/catalog/global-catalog)
- [Scope discovery to a single merchant's storefront.](https://shopify.dev/docs/agents/catalog/storefront-catalog)

#### Carts and checkout

"Build carts as buyers iterate. Add line items, apply localization, and estimate totals" across multiple conversation turns. When buyers are ready, convert the cart into a checkout and refer them to the merchant storefront to complete payment. Trusted agents can complete checkouts directly.

- [Build and iterate on carts with line items, localization, and buyer context.](https://shopify.dev/docs/agents/carts-and-checkout/cart-mcp)
- [Convert carts into checkouts and complete purchases for trusted agents.](https://shopify.dev/docs/agents/carts-and-checkout/checkout-mcp)

#### Monitor orders

"After checkout, monitor order lifecycle changes (fulfillment events, refunds, returns," exchanges, and cancellations) with UCP-shaped order webhooks. Fetch fresh order state on demand with the `get_order` MCP tool when the buyer asks "Where's my order?" or when reconciling a missed webhook.

- [Fetch fresh order state on demand with the `get_order` tool.](https://shopify.dev/docs/agents/orders/order-mcp)
- [Subscribe to lifecycle events for fulfillment, returns, refunds, and edits.](https://shopify.dev/docs/agents/orders/order-webhooks)

---

### Quickstart — full agentic flow with the UCP CLI

> Fonte: <https://shopify.dev/docs/agents/get-started/quickstart> (fetched 2026-06-08)

This quickstart runs the full agentic commerce flow with the UCP CLI, from product discovery to order tracking, in about five minutes. For a hand-rolled walkthrough that builds the same flow against Shopify's MCP servers directly, see the [six-part tutorial series](https://shopify.dev/docs/agents/get-started/authentication).

#### What you'll learn

- Initialize a local UCP profile.
- Search the global Catalog for products.
- Build a cart at a specific merchant.
- Convert that cart into a checkout.
- Track an order after purchase.

#### Requirements

- Node.js 18 or higher.
- A supported AI tool: Claude Code, Cursor, Gemini CLI, or VS Code.

#### Step 1: Install the UCP CLI and Shopify AI Toolkit

Install the UCP CLI for your terminal and the Shopify AI Toolkit plugin for your AI provider.

**Claude Code** — Install the UCP CLI:

```terminal
npm install -g @shopify/ucp-cli
```

Install the Shopify plugin:

```terminal
claude plugin install shopify-ai-toolkit@claude-plugins-official
```

**Cursor** — Install the UCP CLI:

```terminal
npm install -g @shopify/ucp-cli
```

Cursor Chat: Add the plugin:

```terminal
/add-plugin shopify
```

**Gemini CLI** — Install the UCP CLI:

```terminal
npm install -g @shopify/ucp-cli
```

Install the Shopify extension:

```terminal
gemini extensions install https://github.com/Shopify/shopify-ai-toolkit
```

**VS Code** — Install the UCP CLI:

```terminal
npm install -g @shopify/ucp-cli
```

Command Palette > Chat: Install Plugin From Source:

```
https://github.com/Shopify/shopify-ai-toolkit
```

#### Step 2: Initialize your profile

The CLI uses a local profile to identify your agent on every merchant-scoped request. Initialize it once and the CLI reuses it for every operation.

```bash
ucp profile init --name agent
```

Response:

```json
{
  "profile": "agent",
  "path": "~/.ucp/profiles/agent.yaml",
  "active": true
}
```

Run `ucp doctor` at any time to verify your setup is healthy.

#### Step 3: Search the Catalog

The global Catalog searches across millions of products from Shopify-powered merchants. Pass a natural-language query and optional context:

```bash
ucp catalog search \
  --set /query='wireless headphones under $100' \
  --set /context/address_country=US \
  --view :compact \
  --format md
```

Response:

```
| title                                       | price | currency | variant                                       | buy                                                       |
|---------------------------------------------|-------|----------|-----------------------------------------------|-----------------------------------------------------------|
| Sony WH-CH520 Wireless Bluetooth Headphones | 5999  | USD      | gid://shopify/ProductVariant/41293818167385   | https://audiogear.example.com/cart/41293818167385:1       |
| JBL Tune 510BT Wireless On-Ear Headphones   | 4999  | USD      | gid://shopify/ProductVariant/49158410436908   | https://soundsource.example.com/cart/49158410436908:1     |
```

Each result names the merchant it came from in `seller.domain`. Pick a product and copy its variant `id` and the merchant URL for the next step.

#### Step 4: Build a cart

Pass the variant `id` and the merchant URL to `ucp cart create`:

```bash
ucp cart create --business https://{merchant-domain} \
  --set /line_items/0/item/id='{variant_id}' \
  --set /line_items/0/quantity=1 \
  --set /context/address_country=US
```

Response:

```json
{
  "result": {
    "id": "gid://shopify/Cart/abc123",
    "currency": "USD",
    "line_items": [
      {
        "id": "gid://shopify/CartLine/xyz789",
        "item": {
          "id": "gid://shopify/ProductVariant/41293818167385",
          "title": "Sony WH-CH520 Wireless Bluetooth Headphones"
        },
        "quantity": 1,
        "subtotal": 5999
      }
    ],
    "totals": [
      {"type": "subtotal", "display_text": "Subtotal", "amount": 5999},
      {"type": "total", "display_text": "Total", "amount": 5999}
    ],
    "continue_url": "https://audiogear.example.com/cart/c/abc123"
  }
}
```

The merchant returns a cart with confirmed pricing and a `continue_url` the buyer can use to finish in their browser. Save the returned `cart.id` for the next step.

#### Step 5: Convert to checkout

When the buyer commits, convert the cart into a checkout:

```bash
ucp checkout create --business https://{merchant-domain} \
  --input '{"cart_id":"{cart_id}","line_items":[]}'
```

Response:

```json
{
  "result": {
    "id": "gid://shopify/Checkout/def456",
    "status": "incomplete",
    "continue_url": "https://audiogear.example.com/checkouts/def456"
  }
}
```

Inspect what the merchant expects next (fulfillment address, shipping selection) with `--input-schema`, then update and complete:

```bash
ucp checkout update {checkout_id} --input-schema --business https://{merchant-domain}
ucp checkout update {checkout_id} --business https://{merchant-domain} --input '...'
ucp checkout complete {checkout_id} --business https://{merchant-domain}
```

Response:

```json
{
  "result": {
    "id": "gid://shopify/Checkout/def456",
    "status": "completed",
    "order_id": "gid://shopify/Order/789"
  }
}
```

If the merchant requires buyer review, the CLI can hand off to the browser. Set an escalation hook before running checkout:

```bash
export UCP_ON_ESCALATION='jq -r .url | xargs open'
```

#### Step 6: Track the order

After checkout, look up the order by ID:

```bash
ucp order get {order_id} --business https://{merchant-domain}
```

Response:

```json
{
  "result": {
    "id": "gid://shopify/Order/789",
    "financial_status": "paid",
    "fulfillment_status": "unfulfilled",
    "line_items": [
      {
        "title": "Sony WH-CH520 Wireless Bluetooth Headphones",
        "quantity": 1,
        "subtotal": 5999
      }
    ],
    "totals": [
      {"type": "total", "display_text": "Total", "amount": 5999}
    ],
    "currency": "USD"
  }
}
```

#### Next steps

- [Build it from scratch](https://shopify.dev/docs/agents/get-started/authentication) — Hand-roll the same flow against Shopify's MCP servers to see what the CLI does under the hood.
- [UCP CLI reference](https://github.com/Shopify/ucp-cli) — Full command reference and advanced options.

---

### Agent profiles and UCP negotiation

> Fonte: <https://shopify.dev/docs/agents/profiles> (fetched 2026-06-08)

In the [Universal Commerce Protocol (UCP)](https://ucp.dev/documentation/core-concepts/), a platform profile is a JSON document that describes the protocol version and capabilities the platform supports.

When your agents call UCP-shaped MCP tools, Shopify acts as the business in the negotiation. Shopify uses your profile to learn what your agent declares, intersect it with what the shop supports, and settle on a single negotiated set for the session.

This page points to hosted agent profile fixtures you can reference from `meta.ucp-agent.profile` to use and test UCP. For more detail, see the [UCP specification](https://ucp.dev/2026-04-08/specification/overview/).

#### How it works

Negotiation for UCP involves two profiles:

- **Business profile:** Published by the merchant or platform operating the commerce API, typically at `/.well-known/ucp` on the business origin. On Shopify, this exists at the merchant storefront (`{shop}.myshopify.com/.well-known/ucp`). It describes that party's protocol version, services, capabilities, payment handlers, and signing keys.
- **Platform profile:** Published at an HTTPS URL you host, it describes your agent's declared protocol version and capabilities. You include this URL on every relevant request so the business can fetch, potentially cache, and negotiate.

Negotiation is server-selects. The business computes the intersection of its capabilities with the platform's and chooses the active set, including which extension capabilities apply (for example, fulfillment or discount layered on checkout). Extensions that depend on a parent capability are pruned if that parent does not end up in the intersection.

Negotiation follows this sequence:

1. Your request includes the platform profile URL.
2. Shopify (the business) fetches and validates the profile.
3. Protocol version alignment is checked against what the shop supports.
4. Capability intersection runs; matching capability names, compatible capability versions, then dependency pruning for extensions.
5. Responses include negotiated UCP metadata (including active capabilities) where applicable.

If the profile cannot be loaded, is invalid, or yields no compatible capabilities, you get an error path instead of a successful negotiation.

#### Usage

Include the agent profile URI in the `meta.ucp-agent.profile` field of your MCP request:

```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "id": 1,
  "params": {
    "name": "create_checkout",
    "arguments": {
      "meta": {
        "ucp-agent": {
          "profile": "https://shopify.dev/ucp/agent-profiles/2026-04-08/valid-with-capabilities.json"
        }
      },
      "input": {
        "lines": []
      }
    }
  }
}
```

This profile triggers UCP discovery: profile fetch, validation, version negotiation, and caching.

#### Valid profile fixtures (hosted by Shopify for testing)

Shopify hosts ready-to-use profile fixtures. Reference these URLs in `meta.ucp-agent.profile` to test negotiation paths. Versions available: **`2026-04-08`**, **`2026-01-23`**, **`draft`**.

A **"with capabilities"** profile declares checkout plus multiple extensions; the business intersects with its own capabilities, keeping matches and pruning orphaned extensions. Example URL:

```text
https://shopify.dev/ucp/agent-profiles/2026-04-08/valid-with-capabilities.json
```

It contains (version `2026-04-08`):

```json
{
  "ucp": {
    "version": "2026-04-08",
    "services": {
      "dev.ucp.shopping": [
        {
          "version": "2026-04-08",
          "spec": "https://ucp.dev/2026-04-08/specification/overview",
          "transport": "rest",
          "schema": "https://ucp.dev/2026-04-08/services/shopping/rest.openapi.json",
          "endpoint": "https://business.example.com/ucp/v1"
        }
      ]
    },
    "capabilities": {
      "dev.ucp.shopping.checkout": [
        {
          "version": "2026-04-08"
        }
      ],
      "dev.ucp.shopping.fulfillment": [
        {
          "version": "2026-04-08",
          "extends": ["dev.ucp.shopping.checkout", "dev.ucp.shopping.cart"]
        }
      ],
      "dev.ucp.shopping.buyer_consent": [
        {
          "version": "2026-04-08",
          "extends": "dev.ucp.shopping.checkout"
        }
      ],
      "dev.ucp.shopping.discount": [
        {
          "version": "2026-04-08",
          "extends": ["dev.ucp.shopping.checkout", "dev.ucp.shopping.cart"]
        }
      ],
      "dev.ucp.shopping.cart": [
        {
          "version": "2026-04-08",
          "spec": "https://ucp.dev/2026-04-08/specification/cart",
          "schema": "https://ucp.dev/2026-04-08/schemas/shopping/cart.json"
        }
      ],
      "dev.ucp.shopping.order": [
        {
          "version": "2026-04-08",
          "spec": "https://ucp.dev/2026-04-08/specification/order",
          "schema": "https://ucp.dev/2026-04-08/schemas/shopping/order.json"
        }
      ],
      "dev.ucp.shopping.catalog.search": [
        {
          "version": "2026-04-08",
          "spec": "https://ucp.dev/2026-04-08/specification/catalog/search",
          "schema": "https://ucp.dev/2026-04-08/schemas/shopping/catalog_search.json"
        }
      ],
      "dev.ucp.shopping.catalog.lookup": [
        {
          "version": "2026-04-08",
          "spec": "https://ucp.dev/2026-04-08/specification/catalog/lookup",
          "schema": "https://ucp.dev/2026-04-08/schemas/shopping/catalog_lookup.json"
        }
      ],
      "dev.shopify.catalog": [
        {
          "version": "2026-04-08",
          "spec": "https://shopify.dev/docs/agents/catalog/storefront-catalog",
          "schema": "https://shopify.dev/ucp/schemas/2026-04-08/shopify_catalog.json",
          "extends": ["dev.ucp.shopping.catalog.lookup", "dev.ucp.shopping.catalog.search"]
        }
      ],
      "dev.shopify.catalog.global": [
        {
          "version": "2026-04-08",
          "spec": "https://shopify.dev/docs/agents/catalog/global-catalog",
          "schema": "https://shopify.dev/ucp/schemas/2026-04-08/shopify_catalog_global.json",
          "extends": ["dev.ucp.shopping.catalog.lookup", "dev.ucp.shopping.catalog.search"]
        }
      ]
    },
    "payment_handlers": {}
  }
}
```

A **"checkout only"** profile declares only the checkout capability with no extensions; the business intersects and returns checkout alone. Negotiation succeeds, but tools won't include fulfillment or discount input fields in their schemas. Example URL:

```text
https://shopify.dev/ucp/agent-profiles/2026-04-08/checkout-only.json
```

Contents (version `2026-04-08`):

```json
{
  "ucp": {
    "version": "2026-04-08",
    "services": {
      "dev.ucp.shopping": [
        {
          "version": "2026-04-08",
          "spec": "https://ucp.dev/2026-04-08/specification/overview",
          "transport": "rest",
          "schema": "https://ucp.dev/2026-04-08/services/shopping/rest.openapi.json",
          "endpoint": "https://business.example.com/ucp/v1"
        }
      ]
    },
    "capabilities": {
      "dev.ucp.shopping.checkout": [
        {
          "version": "2026-04-08"
        }
      ]
    },
    "payment_handlers": {}
  }
}
```

> **Nota:** Le versioni `2026-01-23` usano `transport: "a2a"` con `endpoint` puntato a `/.well-known/agent-card.json` invece di REST. Le versioni `draft` rispecchiano la struttura `2026-04-08` con `version: "draft"`. Tutte le combinazioni `{2026-04-08, 2026-01-23, draft} × {valid-with-capabilities, checkout-only}` sono ospitate ai relativi URL.

#### Invalid profile fixtures (per testare i fallimenti di negoziazione)

Shopify ospita anche profili che provocano fallimenti, utili per testare l'error handling. Per ogni scenario esistono le tre versioni (`2026-04-08`, `2026-01-23`, `draft`):

| Scenario | URL pattern (esempio `2026-04-08`) | Comportamento |
| - | - | - |
| **Empty capabilities** | `.../2026-04-08/empty-capabilities.json` | Profilo valido con versione corretta ma `capabilities: {}`. Niente da intersecare → la negoziazione non riesce. |
| **Missing version** | `.../2026-04-08/missing-ucp-version.json` | JSON valido ma manca `ucp.version`. La negoziazione di versione fallisce prima dell'intersezione delle capability. |
| **Unsupported version** | `.../2026-04-08/unsupported-ucp-version.json` | Dichiara una `ucp.version` non supportata (es. `2026-01-11`). Fallimento immediato, nessuna intersezione. |
| **Capability version mismatch** | `.../2026-04-08/capability-version-mismatch.json` | Una capability usa una versione non supportata (es. `2099-01-23`). Intersezione parziale: le capability compatibili passano, quella in mismatch viene scartata. |
| **Profile too large** | `.../2026-04-08/too-large.json` | JSON valido ma oltre la dimensione massima. Errore `profile_too_large`, nessuna negoziazione. |
| **Malformed JSON** | `.../2026-04-08/malformed.json` | Payload non è JSON valido; il profilo non può essere parsato. |

---

### Auth and rate limiting (trust tiers)

> Fonte: <https://shopify.dev/docs/agents/profiles/auth-and-rate-limiting> (fetched 2026-06-08)

UCP traffic to Shopify's MCP servers is classified into three tiers based on how your agent identifies itself. Each tier has different capabilities and rate-limiting allowances. Stronger identification means higher rate limits and access to more sensitive tools.

#### Traffic tiers — capability matrix

| Auth type | Catalog tools | Cart tools | Checkout tools | `complete_checkout` | Order tools |
| - | - | - | - | - | - |
| **Token** | Yes | Yes | Yes | When the token is granted permission to complete purchases | Yes, with the `read_global_api_orders` scope |
| **Signed** | Yes | Yes | Yes | No | No |
| **Anonymous** | Yes | Yes | Yes | No | No |

Rate-limit guidance:

- **Rate limits scale with identification.** The Token tier gets the highest limits, Signed gets lower limits, and Anonymous gets the lowest.
- **Checkout MCP is rate-limited more strictly than Cart MCP at every tier.** Use Cart MCP to iterate on line items, refine context, and estimate totals, and reserve Checkout MCP for buyers who are ready to purchase.
- **Order MCP is for on-demand reads.** Reserve `get_order` for buyer-initiated views and reconciling missed webhooks. For proactive lifecycle updates, subscribe to Order webhooks.

#### Token tier

Agents authenticating with a credential issued through Dev Dashboard, such as a global API token, customer accounts token, or shop access token.

- **How to authenticate:** "JWT passed with Bearer token authentication."
- **What you can do:** Access cart, checkout, and order tools at the highest rate limits. Call `complete_checkout` when your token has been granted the required permission to complete purchases on the shop's behalf. Call `get_order` when your token includes the `read_global_api_orders` scope. Order access is restricted to orders placed through your agent.

#### Signed tier

Agents that haven't created an API key but have implemented HTTP signatures per the UCP specification.

- **How to authenticate:** "HTTP Message Signatures per RFC 9421 using ECDSA P-256." Shopify verifies the signature against the public key published in your agent's well-known UCP profile.
- **What you can do:** Access cart and checkout tools at lower rate limits than the Token tier. `complete_checkout` and order tools aren't available at this tier.

#### Anonymous tier

Agents that haven't identified themselves to Shopify.

- **How to authenticate:** "No credentials or signatures provided. Send the request without an Authorization header or signature headers."
- **What you can do:** Access catalog, cart, and checkout build/edit tools at the lowest rate limits. `complete_checkout` and order tools aren't available at this tier.

---

## 2. llms.txt & agents.md (piattaforma)

> Fonte: <https://shopify.dev/changelog/customize-llmstxt-llms-fulltxt-and-agentsmd> (changelog, posted **May 28, 2026**) e <https://shopify.dev/docs/storefronts/themes/architecture/templates/agents-md-liquid> (fetched 2026-06-08).

> **Nota di scope:** i template *lato tema* (`llms.txt.liquid`, `llms-full.txt.liquid`) sono trattati nel capitolo temi. Qui catturiamo il documento di piattaforma `agents.md` come **documento di discovery agent-facing**, perché definisce l'oggetto `agents` e gli endpoint UCP/MCP a cui gli agenti si agganciano.

### Changelog — Customize /llms.txt, /llms-full.txt and /agents.md

**Posted:** May 28, 2026 — **Tags:** Themes

Shopify stores now feature a default `agents.md` file accessible at `/agents.md`, with "/llms.txt and /llms-full.txt also pointing to this content by default."

**Customization options.** Developers can add templates under **Online Store > Themes > Edit code** to serve different content per path:

- `templates/agents.md.liquid` — controls `/agents.md` (and the default for the other two paths)
- `templates/llms.txt.liquid` — controls `/llms.txt` only
- `templates/llms-full.txt.liquid` — controls `/llms-full.txt` only

**Fallback behavior.** When no template exists for a given path, the system defaults to your `agents.md` template, then to Shopify's generated default content.

### agents.md.liquid — il documento di discovery agent-facing

The `agents.md.liquid` template renders the `agents.md` file, which is hosted at the `/agents.md` URL.

The `agents.md` file is the canonical, agent-facing description of a store. It tells AI agents and shopping assistants how to discover the store's commerce capabilities and how to transact with it, including:

- The store's [Universal Commerce Protocol (UCP)](https://ucp.dev) discovery and Model Context Protocol (MCP) endpoints.
- Read-only browsing URLs for product, collection, and search data.
- The store's published policies.
- Guidance for personal shopping agents, such as the [Shop skill](https://shop.app/SKILL.md).

Shopify generates an `agents.md` file by default, which works for most shops, so this template isn't included in any themes by default.

> **Tip:** "The `agents.md` file is served at the bare primary domain, without a locale or Shopify Markets subfolder prefix."

#### Relationship to llms.txt and llms-full.txt

`agents.md` is the canonical agent-discovery document. The `/llms.txt` and `/llms-full.txt` URLs are alternate URLs that mirror the content of `/agents.md` by default on Shopify stores, so agents that request either one still find a usable document.

Because of this, the `agents.md.liquid` template is the fallback for all three URLs. When a request is served, Shopify looks for a theme template in the following order, and uses the first one it finds:

| URL | Template lookup order |
| - | - |
| `/agents.md` | `agents.md.liquid` → Shopify-generated default |
| `/llms.txt` | `llms.txt.liquid` → `agents.md.liquid` → Shopify-generated default |
| `/llms-full.txt` | `llms-full.txt.liquid` → `agents.md.liquid` → Shopify-generated default |

This means that if you add only an `agents.md.liquid` template, then it is used for all three URLs. To make one of the `llms` URLs diverge, add a dedicated `llms.txt.liquid` or `llms-full.txt.liquid` template — it takes precedence for that URL only, while the others keep mirroring `agents.md`.

#### Location

The `agents.md.liquid` template is located in the `templates` directory of the theme:

```text
└── theme
  ├── layout
  ├── templates
  |   ...
  |   ├── agents.md.liquid
  |   ...
  ...
```

To add it: from your Shopify admin, go to **Online Store > Themes**, find the theme, click **... > Edit code**, locate the **Templates** folder, right-click > **New File**, name it `agents.md.liquid`, and press Enter.

#### Content — the `agents` object

This template cannot be a JSON template. "It must be `agents.md.liquid`." The template accepts standard Markdown and [Liquid](https://shopify.dev/docs/api/liquid). To help you build agent instructions with values that stay in sync with the store's actual commerce configuration, the template exposes an `agents` object alongside the standard global Liquid objects.

The `agents` object provides auto-populated UCP and agent-interaction metadata for the store:

| Property | Type | Description |
| - | - | - |
| `agents.store_name` | string | The name of the store. |
| `agents.store_url` | string | The full URL of the store, using the bare primary domain. |
| `agents.ucp_discovery_url` | string | The UCP discovery URL for the store (`{store_url}/.well-known/ucp`). |
| `agents.mcp_endpoint_url` | string | The MCP (Model Context Protocol) endpoint URL (`{store_url}/api/ucp/mcp`). |
| `agents.ucp_versions` | array of string | The supported UCP versions, newest first. Derived from the store's UCP implementation, so it stays in sync automatically. |
| `agents.currency` | string | The store's primary currency code, such as `USD`. |
| `agents.sitemap_url` | string | The store's sitemap URL (`{store_url}/sitemap.xml`). |

Example template:

```liquid
# Agent Instructions — {{ agents.store_name }}

This document describes how AI agents can interact with the online store at {{ agents.store_url }}.

## Commerce Protocol (UCP)

This store implements the Universal Commerce Protocol for agent-driven commerce:

- Discovery: `GET {{ agents.ucp_discovery_url }}`
- MCP endpoint: `POST {{ agents.mcp_endpoint_url }}`

### Supported UCP versions
{% for version in agents.ucp_versions %}
- {{ version }}{% if forloop.first %} (latest stable){% endif %}
{% endfor %}

## Read-only browsing

- All products: `GET /collections/all`
- Product JSON: `GET /products/{handle}.json`
- Sitemap: {{ agents.sitemap_url }}

Pricing and availability are returned in {{ agents.currency }}.
```

> **Caution:** "Avoid outputting potentially private merchant data, such as contact email addresses or phone numbers, in this file."

#### Usage

When you provide an `agents.md.liquid` template, it replaces the Shopify-generated `agents.md` and, unless overridden, the content served at `/llms.txt` and `/llms-full.txt`. "It's strongly recommended to keep the UCP and MCP endpoints discoverable by using the `agents` object rather than hardcoding URLs."

> ⚠️ Nota: non verificato / in evoluzione — In community/blog di terze parti si menzionano endpoint aggiuntivi auto-shipped come `/.well-known/ucp` e `/sitemap_agentic_discovery.xml` su ogni store. Il discovery `/.well-known/ucp` è confermato dalla doc ufficiale (oggetto `agents.ucp_discovery_url` e pagina profiles). Una pagina dev ufficiale specifica per `sitemap_agentic_discovery.xml` non è stata trovata al 2026-06-08; trattalo come non confermato.


---

## 3. Storefront / Catalog MCP (server MCP per lo shopping agentico)

### 3.1 About Storefront MCP

> Fonte: <https://shopify.dev/docs/apps/build/storefront-mcp> (fetched 2026-06-08)

Connect any AI assistant to real-time commerce data from Shopify stores with Model Context Protocol (MCP) servers. Help customers search, ask, and buy in natural language.

#### Model Context Protocol

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) standardizes how applications provide context to AI models. It creates a consistent way for AI systems to access Shopify's commerce data and features.

MCP uses a client-server architecture:

- **MCP client:** Your [Shopify app](https://shopify.dev/docs/apps/build/build) that connects with AI models and passes their requests to MCP servers.
- **MCP servers:** API endpoints that provide structured access to Shopify's commerce data, such as products, cart operations, and customer information.
- **Chat UI:** A [Shopify theme extension](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions/build) that shows a customer-facing chat window.

The backend works as an MCP client while the frontend (Chat UI) provides the customer experience. This approach lets you connect any AI model to Shopify without custom integration.

#### Benefits of MCP

Build AI shopping experiences that convert browsers into buyers.

**MCP capabilities:**

- **Product discovery:** Natural-language search with product recommendations
- **Cart management:** Create carts, add or remove items, and complete checkout
- **Store information:** Answer questions about policies, shipping, returns, and FAQs
- **Order management:** Track order status and process returns

**App features:**

- **AI-powered chat:** Add an embedded chat bubble for real-time shopping help
- **Built-in MCP client:** Connect to Shopify's tools for search, cart, and orders
- **Persistent context:** Keep conversations coherent by remembering past messages
- **Custom chat UI:** Style your theme extension to match your store's brand
- **Streaming responses:** Create a natural chat experience with message streaming

#### MCP servers

Connect to these MCP servers to extend your AI assistant's capabilities:

- **[Storefront MCP server](https://shopify.dev/docs/apps/build/storefront-mcp/servers/storefront)** — Connect to a store's catalog, cart, and policies to help customers shop with that merchant.
- **[Customer accounts MCP server](https://shopify.dev/docs/apps/build/storefront-mcp/servers/customer-account)** — Help customers track orders, manage returns, and access their account information.

A tutorial — [Build a Storefront AI agent](https://shopify.dev/docs/apps/build/storefront-mcp/build-storefront-ai-agent) — walks through creating an AI shopping assistant.

---

### 3.2 Storefront MCP server (tools & endpoints)

> Fonte: <https://shopify.dev/docs/apps/build/storefront-mcp/servers/storefront> (fetched 2026-06-08)

Connect your AI agent to a specific Shopify store's catalog, shopping cart, and policies. The Storefront MCP server helps customers browse and buy with their selected merchant.

> **UCP catalog capability:** Storefront MCP implements the [UCP Catalog capability](https://ucp.dev/latest/specification/catalog/) and its [MCP binding](https://ucp.dev/latest/specification/catalog/mcp/). The `search_catalog`, `lookup_catalog`, and `get_product` tools conform to the UCP specification.

#### How it works

1. A shopper asks about products while browsing a store.
2. Your agent searches the store's catalog and manages carts.
3. The shopper adds items and completes checkout.

#### Connect to the server

Each Shopify store has its own MCP server endpoint that exposes storefront features:

```text
https://{shop}.myshopify.com/api/mcp
```

This endpoint is unique to each store and gives access to all storefront commerce capabilities.

> **Caution:** By using the Shopify MCP servers, you agree to the [Shopify API License and Terms of Use](https://www.shopify.com/legal/api-terms).

#### Create an API request

Storefront MCP servers don't require authentication. Replace `{shop}.myshopify.com` with the store's actual domain, send requests to the MCP endpoint, and include the `Content-Type` header:

```js
// Basic setup for Storefront MCP server requests
const storeDomain = 'your-store.myshopify.com';
// Standard Storefront MCP endpoint (cart, policies)
const mcpEndpoint = `https://${storeDomain}/api/mcp`;


// UCP catalog endpoint (search_catalog, lookup_catalog, get_product)
const ucpMcpEndpoint = `https://${storeDomain}/api/ucp/mcp`;


// UCP catalog tools require an agent profile in every request
const agentProfile = 'https://shopify.dev/ucp/agent-profiles/examples/2026-04-08/valid-with-capabilities.json';


// Example: search for products using UCP catalog tools
fetch(ucpMcpEndpoint, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    jsonrpc: '2.0',
    method: 'tools/call',
    id: 1,
    params: {
      name: 'search_catalog',
      arguments: {
        meta: {
          'ucp-agent': { profile: agentProfile }
        },
        catalog: {
          query: 'coffee'
        }
      }
    }
  })
});
```

> **Note:** Some stores may restrict access. Always test with your specific store.

#### Tool endpoints — two distinct endpoints

| Tools | Endpoint |
| - | - |
| **UCP catalog tools** (`search_catalog`, `lookup_catalog`, `get_product`) — use a `catalog` wrapper object | `https://{shop}.myshopify.com/api/ucp/mcp` |
| **Standard tools** (`get_cart`, `update_cart`, `search_shop_policies_and_faqs`) | `https://{shop}.myshopify.com/api/mcp` |

#### Available tools

**`search_catalog`** — Searches the store's product catalog. Key parameters (inside `catalog` object): `query` (free-text), `context` (buyer signals: country, language, currency, intent), `filters` (categories or price range in minor currency units), `pagination` (cursor, limit).

```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "id": 1,
  "params": {
    "name": "search_catalog",
    "arguments": {
      "meta": {
        "ucp-agent": {
          "profile": "https://shopify.dev/ucp/agent-profiles/examples/2026-04-08/valid-with-capabilities.json"
        }
      },
      "catalog": {
        "query": "organic coffee beans",
        "context": {
          "address_country": "US",
          "intent": "Customer prefers fair trade products"
        }
      }
    }
  }
}
```

**`lookup_catalog`** — Retrieves products or variants by identifier. Key parameters (inside `catalog`): `ids` (array, required, up to 10), `context`, `filters`.

```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "id": 1,
  "params": {
    "name": "lookup_catalog",
    "arguments": {
      "meta": {
        "ucp-agent": {
          "profile": "https://shopify.dev/ucp/agent-profiles/examples/2026-04-08/valid-with-capabilities.json"
        }
      },
      "catalog": {
        "ids": ["gid://shopify/Product/123", "gid://shopify/ProductVariant/456"],
        "context": {
          "address_country": "US"
        }
      }
    }
  }
}
```

**`get_product`** — Retrieves full details for a single product, with optional interactive variant selection. Key parameters (inside `catalog`): `id` (required), `selected` (option selections, e.g. `[{"name": "Color", "label": "Blue"}]`), `preferences` (option names in relaxation priority order), `context`, `filters`.

```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "id": 1,
  "params": {
    "name": "get_product",
    "arguments": {
      "meta": {
        "ucp-agent": {
          "profile": "https://shopify.dev/ucp/agent-profiles/examples/2026-04-08/valid-with-capabilities.json"
        }
      },
      "catalog": {
        "id": "gid://shopify/Product/123",
        "selected": [
          {"name": "Color", "label": "Blue"}
        ],
        "context": {
          "address_country": "US"
        }
      }
    }
  }
}
```

> **Note:** These catalog tools conform to the [UCP catalog specification](https://ucp.dev/specification/catalog/).

**`search_shop_policies_and_faqs`** — Answers questions about the store's policies, products, and services. Key parameters: `query` (required), `context` (optional).

```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "id": 1,
  "params": {
    "name": "search_shop_policies_and_faqs",
    "arguments": {
      "query": "What is your return policy for sale items?",
      "context": "Customer is looking at discounted winter jackets"
    }
  }
}
```

> **Tip:** Use only the provided answer to form your response. Don't include external information that might be inaccurate. For better store policy management, consider using the [Knowledge Base app](https://apps.shopify.com/shopify-knowledge-base).

**`get_cart`** — Retrieves the current contents of a cart, including item details and checkout URL. Key parameters: `cart_id`.

```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "id": 1,
  "params": {
    "name": "get_cart",
    "arguments": {
      "cart_id": "gid://shopify/Cart/abc123def456"
    }
  }
}
```

**`update_cart`** — Updates quantities of items, adds new items, or creates a new cart (when no `cart_id` is provided). Set quantity to 0 to remove an item. Key parameters: `cart_id` (creates a new cart if not provided), `lines` (array, required; each with `quantity` and optional `line_item_id`).

```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "id": 1,
  "params": {
    "name": "update_cart",
    "arguments": {
      "cart_id": "gid://shopify/Cart/abc123def456",
      "add_items": [
        {
          "line_item_id": "gid://shopify/CartLine/line2",
          "merchandise_id": "gid://shopify/ProductVariant/789012",
          "quantity": 2
        }
      ]
    }
  }
}
```

---

### 3.3 About Catalogs (Global vs Storefront)

> Fonte: <https://shopify.dev/docs/agents/catalog> (fetched 2026-06-08)

Shopify provides two catalog interfaces for AI agents to discover and retrieve products. **Global Catalog** searches across all Shopify merchants, while **Storefront Catalog** is scoped to a single merchant's store. Both implement the [UCP Catalog capability](https://ucp.dev/2026-04-08/specification/catalog/), but they differ in scope, authentication, and available features.

**Global Catalog:**

| | |
| - | - |
| **Scope** | All Shopify merchants |
| **Endpoint** | `https://catalog.shopify.com/api/ucp/mcp` |
| **Auth** | [Agent profile](https://shopify.dev/docs/agents/profiles) (no API key needed) |
| **Extensions** | [Global Catalog extension](https://shopify.dev/docs/agents/catalog/global-catalog-extension) |
| **Best for** | Cross-merchant discovery, comparison shopping |

**Storefront Catalog:**

| | |
| - | - |
| **Scope** | Single merchant store |
| **Endpoint** | `https://{storeDomain}/api/ucp/mcp` |
| **Auth** | [Agent profile](https://shopify.dev/docs/agents/profiles) (no API key needed) |
| **Extensions** | [Storefront Catalog extension](https://shopify.dev/docs/agents/catalog/storefront-catalog-extension) |
| **Best for** | Single-store agents |

#### Tools

Both catalog interfaces expose the same three tools.

**`search_catalog`** — Find products by keyword. Global Catalog returns products from across all Shopify merchants, clustered by Universal Product ID (UPID); Storefront Catalog returns products scoped to a single store.

Global Catalog MCP request:

```json
{
  "catalog": {
    "query": "organic cotton sweater",
    "filters": {
      "ships_to": {"country": "US"},
      "available": true
    }
  }
}
```

Storefront Catalog MCP request:

```json
{
  "catalog": {
    "query": "organic cotton sweater"
  }
}
```

**`lookup_catalog`** — Retrieve products or variants by identifier. A single Global Catalog request resolves up to 50 identifiers; Storefront Catalog supports up to 10. Unresolved IDs are reported in `messages`.

Global Catalog MCP request:

```json
{
  "catalog": {
    "ids": [
      "gid://shopify/p/7f3a2b8c1d9e",
      "gid://shopify/ProductVariant/12345678"
    ],
    "context": {"address_country": "US"}
  }
}
```

Storefront Catalog MCP request:

```json
{
  "catalog": {
    "ids": ["gid://shopify/Product/1001"]
  }
}
```

**`get_product`** — Retrieve full details for a single product, including all option combinations with availability signals and checkout links. Pass `selected` to anchor a specific variant and `preferences` to control how the server relaxes selections.

Global Catalog MCP request:

```json
{
  "catalog": {
    "id": "gid://shopify/p/7f3a2b8c1d9e",
    "selected": [{"name": "Color", "label": "Black"}],
    "preferences": ["Color", "Size"]
  }
}
```

Storefront Catalog MCP request:

```json
{
  "catalog": {
    "id": "gid://shopify/Product/1001",
    "selected": [{"name": "Color", "label": "Blue"}]
  }
}
```

#### Usage guidelines (both interfaces)

- **Don't cache or re-use images:** "Images may only be used in connection with the related merchant's product listing and must be rendered in real-time (not downloaded to servers)."
- **Don't cache search results:** Catalog results reflect merchant preferences on pricing, availability, and presentation. Caching results isn't allowed.
- **Rate limits:** Catalog queries are subject to rate limits. Keyless catalog access doesn't support rate limit increases. To request an increase, use an authenticated API key and contact Shopify through Dev Dashboard.
- **Inferred fields:** Some fields might be inferred by Shopify's AI and might not always be present or have varying accuracy. Inferred fields are marked with the `Inferred` label.
- **Endpoint URLs might change:** API URLs are subject to change.

#### Saved Catalogs (Global Catalog feature)

By default, Global Catalog queries return products from any eligible merchant. You can narrow these results at runtime using parameters like price range, shipping origin, shops, or product taxonomies. If your agent consistently uses the same parameters, you can save a Catalog configuration in the Dev Dashboard to avoid repeating them on every request.

Catalog filter options:

- **Inputs**: Whether the Catalog queries all of Shopify or products from a specific store.
- **Overrides**: Custom filters (e.g. limit to certain Taxonomy category IDs).
- **Access**: Where the custom URL for your saved Catalog can be retrieved, and requesting access to additional agentic-commerce features.

If a slug for a saved catalog is provided in Catalog Search operations, then its parameters and filters always take precedence.


---

### 3.4 Cart MCP

> Fonte: <https://shopify.dev/docs/agents/carts-and-checkout/cart-mcp> (fetched 2026-06-08)

The Cart MCP server enables AI agents to build and iterate on a cart before the buyer commits to purchase. When the buyer is ready to buy, convert the cart into a checkout with Checkout MCP.

Cart MCP implements the UCP cart capability (`dev.ucp.shopping.cart`, version `2026-04-08`). A cart serves as a pre-checkout container for line items, localization context, and optional buyer information. The tools accept unauthenticated requests, which lets you estimate totals and share a cart before collecting credentials.

#### Cart vs. checkout

- **Carts have a long TTL.** Use them for browsing sessions where the buyer is still exploring. Iterate on `line_items` and `context` across multiple turns, share the cart's `continue_url`, and let the cart persist while they decide.
- **Checkouts are short-lived.** Create one only when the buyer is ready to purchase. Each checkout session represents an active transaction with stricter freshness, idempotency, and rate-limit guarantees.

#### Use with the AI Toolkit / UCP CLI

The [Shopify AI Toolkit](https://shopify.dev/docs/apps/build/ai-toolkit) installs the `ucp` skill, which lets agents call each Cart MCP tool by name. Ask in natural language (`"add this variant to a new cart"`) and the skill picks the right [UCP CLI](https://github.com/Shopify/ucp-cli) command, or run `ucp cart` directly. Run `ucp cart <subcommand> --input-schema --business <url>` to fetch the merchant's live input schema before composing payloads.

```bash
# Create
ucp cart create --business https://{shop}.example.com \
  --set /line_items/0/item/id='gid://shopify/ProductVariant/12345' \
  --set /line_items/0/quantity=1 \
  --set /context/address_country=US

# Get
ucp cart get gid://shopify/Cart/cart_abc123 --business https://{shop}.example.com

# Update
ucp cart update gid://shopify/Cart/cart_abc123 --business https://{shop}.example.com \
  --set /line_items/0/quantity=2

# Cancel
ucp cart cancel gid://shopify/Cart/cart_abc123 --business https://{shop}.example.com
```

#### Tool routing (when to use Cart vs Checkout)

| Use case | Recommended tool |
| - | - |
| Browsing, exploration, total estimates across turns | Cart MCP |
| Sharing a cart link with the buyer | Cart MCP (`continue_url`) |
| Buyer is ready to purchase | Checkout MCP |
| Completing the order in your application | Checkout MCP (`complete_checkout`) |

#### Make requests

All requests follow JSON-RPC 2.0. Send `POST` to `https://{shop-domain}/api/ucp/mcp`. Cart tools accept unauthenticated requests — no Bearer token needed for `create_cart`, `get_cart`, `update_cart`, or `cancel_cart`. Every request must include a `meta` object with `meta["ucp-agent"].profile`. For `cancel_cart`, also include `meta["idempotency-key"]` (UUID). The cart is returned in `result.structuredContent`.

#### Cart tools

- **`create_cart`** — Create a new cart with line items and optional buyer context. Required params: `meta` (with `ucp-agent.profile`), `cart` (with `line_items` required; optional `context`, `buyer`, `signals`).
- **`get_cart`** — Retrieve the current state of a cart. Required: `meta`, `id`. If the cart doesn't exist/expired, returns a successful `result` whose `messages` array contains an `unrecoverable` error with code `not_found`.
- **`update_cart`** — Replace the cart's contents (PUT semantics).
- **`cancel_cart`** — Cancel an active cart. Requires `meta["idempotency-key"]` (UUID).

> **Caution:** `update_cart` uses **PUT semantics**. Each request replaces the cart's full state with the payload you send. Omit a field (for example `line_items` or `context`) and it's removed from the cart. This differs from Storefront API and AJAX cart mutations, which patch individual fields. There is no server-side merge of partial updates.

Example `create_cart` direct call:

```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "id": 1,
  "params": {
    "name": "create_cart",
    "arguments": {
      "meta": {
        "ucp-agent": {
          "profile": "https://shopify.dev/ucp/agent-profiles/examples/2026-04-08/valid-with-capabilities.json"
        }
      },
      "cart": {
        "line_items": [
          {
            "quantity": 2,
            "item": {
              "id": "gid://shopify/ProductVariant/12345678901"
            }
          }
        ],
        "context": {
          "address_country": "US",
          "address_region": "CA",
          "postal_code": "94105"
        }
      }
    }
  }
}
```

Example `create_cart` response:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "structuredContent": {
      "cart": {
        "ucp": {
          "version": "2026-04-08",
          "capabilities": {
            "dev.ucp.shopping.cart": [{ "version": "2026-04-08", "spec": "https://ucp.dev/2026-04-08/specification/cart" }]
          }
        },
        "id": "gid://shopify/Cart/cart_abc123",
        "currency": "USD",
        "line_items": [
          {
            "id": "gid://shopify/CartLine/li_1?cart=cart_abc123",
            "item": {
              "id": "gid://shopify/ProductVariant/12345678901",
              "title": "Organic Cotton Sweater",
              "price": 8900
            },
            "quantity": 2,
            "totals": [
              { "type": "subtotal", "amount": 17800, "display_text": "Subtotal" },
              { "type": "total", "amount": 17800, "display_text": "Total" }
            ]
          }
        ],
        "totals": [
          { "type": "subtotal", "amount": 17800, "display_text": "Subtotal" },
          { "type": "total", "amount": 17800, "display_text": "Total" }
        ],
        "messages": [],
        "continue_url": "https://shop.example.com/cart/c/cart_abc123",
        "expires_at": "2026-05-08T15:17:07Z"
      }
    }
  }
}
```

#### Error handling (Cart & Checkout share this model)

UCP distinguishes between **protocol errors** and **business outcomes**:

- **Business outcomes:** Application-level results from successful processing, returned as JSON-RPC `result` with the UCP envelope and a `messages` array (e.g. expired cart, unavailable merchandise, adjusted quantity).
- **Protocol errors:** Transport-level failures (authentication, rate limiting, unavailability) that prevent processing. Returned as JSON-RPC `error` with code `-32000`, or `-32001` for discovery errors.

When rate-limited, retry after the delay in the HTTP `Retry-After` header; apply exponential backoff with jitter when the header is absent. Don't retry inside the same checkout or payment lifecycle without an `idempotency-key`.

---

### 3.5 Checkout MCP

> Fonte: <https://shopify.dev/docs/agents/checkout/mcp> (fetched 2026-06-08)

The Checkout MCP server enables AI agents to create and manage checkout sessions, convert carts into checkouts, and refer buyers to the merchant storefront to complete purchases. Checkout MCP implements the UCP checkout capability (`dev.ucp.shopping.checkout`). All requests require authentication or a signed request.

> **Info — Use Cart MCP for iteration.** "Checkout MCP is rate-limited more strictly than Cart MCP across all tiers. Iterate on line items, localization, and estimated totals on a cart, then create a checkout when the buyer is ready to buy."

#### Authenticate

Obtain client credentials (client ID and secret) from the **Catalog** section of Dev Dashboard. Use them to retrieve a token. All requests require the `Authorization: Bearer {token}` header. JWT tokens from Dev Dashboard credentials have a 60-minute TTL.

```bash
curl --request POST \
  --url https://api.shopify.com/auth/access_token \
  --header 'Content-Type: application/json' \
  --data '{
    "client_id": "{your_client_id}",
    "client_secret": "{your_client_secret}",
    "grant_type": "client_credentials"
  }'
```

Response:

```json
{
    "access_token": "f8563253df0bf277ec9ac6f649fc3f17",
    "scope": "read_global_api_catalog_search",
    "expires_in": 86399
}
```

#### Make requests

All requests follow JSON-RPC 2.0. Send `POST` to `https://{shop-domain}/api/ucp/mcp`. Every request must include a `meta` object with `meta["ucp-agent"].profile`. For `complete_checkout` and `cancel_checkout`, also include `meta["idempotency-key"]` (UUID). The checkout is returned in `result.structuredContent`. Platforms may use [HTTP Message Signatures](https://ucp.dev/2026-04-08/specification/signatures) (RFC 9421) for agent authentication in addition to or instead of Bearer tokens.

#### Checkout tools

For get/update/complete/cancel operations, pass the checkout session ID as the top-level `id` in `arguments` (not within the `checkout` object).

- **`create_checkout`** — Create a new checkout session with line items and buyer information. Accepts an optional top-level `cart_id` to convert a Cart-MCP cart into a checkout.
- **`get_checkout`** — Retrieve the current state of a checkout session.
- **`update_checkout`** — Update a checkout session (PUT semantics; each request replaces the full checkout state).
- **`complete_checkout`** — Submit payment and place the order. Requires `meta["idempotency-key"]`. When a checkout returns `requires_escalation`, direct the buyer to `continue_url`.
- **`cancel_checkout`** — Cancel an active checkout session. Requires `meta["idempotency-key"]`.

> **Caution:** `update_checkout` uses **PUT semantics**. Each request replaces the full checkout state with the payload you send. Omit a field (for example `line_items` or `buyer`) and it is removed from the checkout. There is no server-side merge of partial updates.

Example `create_checkout` direct call:

```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "id": 1,
  "params": {
    "name": "create_checkout",
    "arguments": {
      "meta": {
        "ucp-agent": {
          "profile": "https://shopify.dev/ucp/agent-profiles/examples/2026-04-08/valid-with-capabilities.json"
        }
      },
      "checkout": {
        "currency": "USD",
        "line_items": [
          {
            "quantity": 2,
            "item": {
              "id": "gid://shopify/ProductVariant/12345678901"
            }
          }
        ],
        "buyer": {
          "email": "buyer@example.com"
        },
        "fulfillment": {
          "methods": [
            {
              "type": "shipping",
              "destinations": [
                {
                  "first_name": "Jane",
                  "last_name": "Smith",
                  "street_address": "123 Main Street",
                  "address_locality": "Brooklyn",
                  "address_region": "NY",
                  "postal_code": "11201",
                  "address_country": "US"
                }
              ]
            }
          ]
        }
      }
    }
  }
}
```

Example `complete_checkout` direct call (note the `idempotency-key`):

```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "id": 1,
  "params": {
    "name": "complete_checkout",
    "arguments": {
      "meta": {
        "ucp-agent": {
          "profile": "https://shopify.dev/ucp/agent-profiles/examples/2026-04-08/valid-with-capabilities.json"
        },
        "idempotency-key": "661e9500-f39c-52e5-b827-557766551111"
      },
      "id": "gid://shopify/Checkout/abc123?key=xyz789",
      "checkout": {
        "payment": {
          "instruments": [
            {
              "id": "pm_1234567890abc",
              "handler_id": "gpay_7k2m",
              "type": "card"
            }
          ]
        }
      }
    }
  }
}
```

Completed-order response (excerpt):

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "structuredContent": {
      "id": "gid://shopify/Checkout/abc123?key=xyz789",
      "status": "completed",
      "order": {
        "id": "gid://shopify/Order/9876543210",
        "permalink_url": "https://shop.example.com/orders/9876543210"
      }
    }
  }
}
```

#### Convert a cart into a checkout

When both cart and checkout capabilities are negotiated, `create_checkout` accepts an optional top-level `cart_id`. Rules:

- **Cart contents win.** The merchant uses the cart's `line_items`, `context`, and `buyer`; overlapping fields in the `checkout` payload are ignored.
- **`checkout` becomes optional.** You can omit it and let the cart drive the checkout.
- **Idempotent conversion.** If an incomplete checkout already exists for the cart, the server returns that existing session. Safe to retry.
- **Linked lifecycle.** The cart remains linked to the checkout for its duration (supports back-to-storefront flows).

Outcomes when `cart_id` can't be resolved: `invalid_cart_id` (not a valid Shopify GID), `cart_not_found` (doesn't exist or expired).

> **Note:** "`cart_id` is currently accepted as input but is not returned on checkout response objects." Store the cart ID on your side if you need to reference it after conversion.

#### Checkout status lifecycle

| Status | Description |
| --- | --- |
| `incomplete` | Checkout is missing required information. Inspect `messages` (including each message's `severity`) and resolve via `update_checkout`. |
| `requires_escalation` | Checkout requires buyer input or review not available via API. Check `messages` for `severity: requires_buyer_input` or `severity: requires_buyer_review` and hand off via `continue_url`. |
| `ready_for_complete` | All information is collected. Call `complete_checkout` or hand off via `continue_url`. |
| `complete_in_progress` | Merchant is processing the `complete_checkout` request. |
| `completed` | Order placed successfully. |
| `canceled` | Checkout session is invalid or expired. Start a new session if needed. |

**General access.** For most partners referring checkout sessions from Catalog, responses include `status: requires_escalation`, a `messages` array, and a `continue_url`. For general access, directing buyers to that URL is how checkout completes; you do **not** call `complete_checkout`. Append query parameters to `continue_url` for attribution:

```text
https://merchant.example/checkout/cn/...?utm_source=your_agent&utm_medium=agentic_commerce&utm_campaign=example
```

---

### 3.6 Customer Accounts MCP Server

> Fonte: <https://shopify.dev/docs/apps/build/storefront-mcp/servers/customer-account> (fetched 2026-06-08)

The Customer accounts MCP server provides tools for customer-specific actions, including order management and account details. Use this server for authenticated customer requests (checking order status, retrieving order details, managing account preferences).

#### Requirements

- Your store must have a custom domain configured.
- Your app must meet [Shopify's protected customer data requirements](https://shopify.dev/docs/apps/launch/protected-customer-data).
- You must have completed the customer accounts MCP integration steps.

#### Endpoint (dynamically discovered)

```javascript
// Discover the MCP endpoint from the shop's storefront domain
const discoveryResponse = await fetch(`https://${shopDomain}/.well-known/customer-account-api`);
const apiConfig = await discoveryResponse.json();

// Use the discovered MCP endpoint
const mcpEndpoint = apiConfig.mcp_api;
// Result: "https://{shopDomain}/customer/api/mcp"
```

#### Authentication (OAuth 2.0 + PKCE)

Requires an OAuth 2.0 access token via the authorization code grant flow with PKCE. Steps: update the app TOML with customer authentication config and redirect URIs; deploy; request Level 2 protected customer data (PII) access from the Partner dashboard; install on the dev store; discover OAuth URLs from the storefront discovery endpoint; implement the authorization code flow with PKCE; authenticate requests with the token.

```toml
[access_scopes]
scopes = "customer_read_customers, customer_read_orders..."

[customer_authentication]
redirect_uris = [
  "https://your-app-domain.com/callback"
]
```

OAuth discovery:

```javascript
const oauthDiscoveryResponse = await fetch(`https://${shopDomain}/.well-known/openid-configuration`);
const oauthConfig = await oauthDiscoveryResponse.json();
// oauthConfig.authorization_endpoint, oauthConfig.token_endpoint, ...
```

Authorization request (PKCE):

```javascript
const params = new URLSearchParams({
  client_id: 'YOUR_APP_ID',          // Your AppID serves as the OAuth client_id
  redirect_uri: 'YOUR_REDIRECT_URI', // Must match TOML (localhost allowed in local dev)
  response_type: 'code',
  scope: 'customer-account-mcp-api:full',
  state: 'RANDOM_HEX',               // 16-byte hex for CSRF protection
  code_challenge: 'PKCE_CHALLENGE',  // SHA256 hashed and base64URL encoded
  code_challenge_method: 'S256'
});
const authUrl = `${oauthConfig.authorization_endpoint}?${params}`;
window.location.href = authUrl;
```

The flow begins when your app attempts to access customer data without a valid token: the server returns `401 Unauthorized`, you initiate OAuth, handle the callback (exchange the code + original `code_verifier` for a token at `token_endpoint`), store the token, and retry the original MCP request with the `Authorization` header. Restart the server with `shopify app dev --use-localhost` after configuring.

#### Available tools

Use `tools/list` to discover available tools and their schemas. Common patterns: IDs follow `gid://shopify/<Type>/<id>`; order numbers may include an optional `#` prefix; quantities are positive integers; dates are ISO 8601; monetary amounts include currency codes.

> ⚠️ Nota: non verificato / in evoluzione — La pagina ufficiale **non elenca per nome** i singoli tool del Customer Accounts MCP: rimanda a `tools/list` per la scoperta runtime degli schemi. Non inventare nomi di tool: introspetta con `tools/list` sul tuo store.

#### Error handling & rate limits

- Validation errors return specific, descriptive messages.
- Processing errors return `Unable to process the request, try again`.
- Not-found errors return clear messages (e.g. `Order not found with number: {order_number}`).
- Tools follow [standard API rate limiting](https://shopify.dev/docs/api/usage/limits#rate-limits).


---

## 4. Shopify Dev MCP (`@shopify/dev-mcp`) & AI Toolkit

> **Importante (verifica struttura repo):** al 2026-06-08 il repo `github.com/Shopify/dev-mcp` restituisce **404** (sia via WebFetch sia via `gh api`). Lo stesso README "Shopify Dev MCP - AI Agent Plugin" è ora pubblicato dentro `github.com/Shopify/Shopify-AI-Toolkit`. Il pacchetto npm `@shopify/dev-mcp` esiste ancora (versione **1.14.0**) ma il suo tarball non contiene README. La doc ufficiale di riferimento è la pagina **Shopify AI Toolkit**. I nomi dei tool del Dev MCP riportati sotto sono stati **estratti dal codice `dist/` del pacchetto npm 1.14.0** (verifica diretta).

### 4.1 Shopify AI Toolkit — overview & install

> Fonte: <https://shopify.dev/docs/apps/build/ai-toolkit> (fetched 2026-06-08)

The Shopify AI Toolkit connects your AI tools to the Shopify platform. With the Toolkit, you can build apps using Shopify's documentation, API schemas, and code validation, and manage your Shopify store through the CLI's store execute capabilities. The Toolkit ensures your agent works with Shopify correctly, rather than guessing at how things are implemented.

You can set up the AI Toolkit in three ways:

- **Install the plugin** (recommended) — updates automatically.
- **Install with agent skills** — manually add some or all of the AI Toolkit's agent skill files.
- **Install with the Dev MCP server** — connect to Shopify's developer resources through an MCP server.

#### Requirements

- Node.js 18 or higher.
- A supported AI tool: Claude Code, Codex, Cursor, Gemini CLI, Hermes (plugin only), or Visual Studio Code.

#### Install with a plugin (recommended)

**Claude Code:**

```terminal
claude plugin install shopify-ai-toolkit@claude-plugins-official
```

**Codex:** Open the Codex desktop app → **Plugins** marketplace → search **Shopify** → on the Shopify AI Toolkit plugin click **Add Plugin**.

**Cursor:**

```terminal
/add-plugin shopify
```

**Gemini CLI:**

```terminal
gemini extensions install https://github.com/Shopify/shopify-ai-toolkit
```

**Hermes:**

```terminal
curl -fsSL https://raw.githubusercontent.com/Shopify/Shopify-AI-Toolkit/main/.hermes-plugin/install.sh -o /tmp/shopify-hermes-install.sh
bash /tmp/shopify-hermes-install.sh
```

**VS Code:** Ensure the [Agent plugins](https://code.visualstudio.com/docs/copilot/customization/agent-plugins) preview is enabled. Command Palette → **Chat: Install Plugin From Source** → enter:

```
https://github.com/Shopify/shopify-ai-toolkit
```

#### Install with agent skills

Browse the [full list of skills](https://github.com/Shopify/Shopify-AI-Toolkit/tree/main/skills) on GitHub. Manually added skills don't auto-update.

```terminal
npx skills add Shopify/shopify-ai-toolkit
```

Install a single skill with `--skill` (example: only the GraphQL Admin API skill):

```terminal
npx skills add Shopify/shopify-ai-toolkit --skill shopify-admin
```

> **Skill disponibili nel repo `Shopify-AI-Toolkit/skills` (verificato via `gh api`, 2026-06-08):** `shopify-admin`, `shopify-app-store-review`, `shopify-custom-data`, `shopify-customer`, `shopify-dev`, `shopify-functions`, `shopify-hydrogen`, `shopify-liquid`, `shopify-onboarding-dev`, `shopify-onboarding-merchant`, `shopify-partner`, `shopify-payments-apps`, `shopify-polaris-admin-extensions`, `shopify-polaris-app-home`, `shopify-polaris-checkout-extensions`, `shopify-polaris-customer-account-extensions`, `shopify-pos-ui`, `shopify-storefront-graphql`, `shopify-use-shopify-cli`, `ucp`.

#### Install with the Dev MCP server

The server runs locally and doesn't require authentication.

**Claude Code:**

```terminal
claude mcp add --transport stdio shopify-dev-mcp -- npx -y @shopify/dev-mcp@latest
```

**Codex CLI** — add to `~/.codex/config.toml`:

```toml
[mcp_servers.shopify-dev-mcp]
command = "npx"
args = ["-y", "@shopify/dev-mcp@latest"]
```

> **Note:** Codex uses TOML format with `mcp_servers` (snake_case) instead of JSON with `mcpServers` (camelCase).

**Cursor** — add to your MCP servers:

```json
{
  "mcpServers": {
    "shopify-dev-mcp": {
      "command": "npx",
      "args": ["-y", "@shopify/dev-mcp@latest"]
    }
  }
}
```

If you see connection errors on Windows, try this alternative:

```json
{
  "mcpServers": {
    "shopify-dev-mcp": {
      "command": "cmd",
      "args": ["/k", "npx", "-y", "@shopify/dev-mcp@latest"]
    }
  }
}
```

**Gemini CLI** — add to `settings.json` (add `--scope user` to make it available across all projects):

```json
{
  "mcpServers": {
    "shopify-dev-mcp": {
      "command": "npx",
      "args": ["-y", "@shopify/dev-mcp@latest"]
    }
  }
}
```

**VS Code** — Command Palette → **MCP: Open User Configuration** → add to `mcp.json`:

```json
{
  "servers": {
    "shopify-dev-mcp": {
      "command": "npx",
      "args": ["-y", "@shopify/dev-mcp@latest"]
    }
  }
}
```

#### Related resources

- **[Shopify CLI](https://shopify.dev/docs/apps/build/cli-for-apps)** — Command-line tool for building Shopify apps and themes.
- **[Scaffold an app](https://shopify.dev/docs/apps/build/scaffold-app)** — Get started building with Shopify by scaffolding your app.

---

### 4.2 Dev MCP server — README (consolidato nel repo AI Toolkit)

> Fonte: README "Shopify Dev MCP - AI Agent Plugin" da <https://github.com/Shopify/Shopify-AI-Toolkit> (fetched via `gh api`, 2026-06-08). Il repo standalone `Shopify/dev-mcp` è 404.

Connect your AI tools to the Shopify platform. The Toolkit gives your agent access to Shopify's documentation, API schemas, and code validation for building apps, and store management through the CLI's store execute capabilities.

**Install:**

- **Claude Code:**

  ```
  /plugin marketplace add Shopify/shopify-ai-toolkit
  /plugin install shopify-plugin@shopify-ai-toolkit
  ```

- **Cursor:** Install from the [Cursor Marketplace](https://cursor.com/marketplace/shopify).
- **Gemini CLI:** `gemini extensions install https://github.com/Shopify/shopify-ai-toolkit`
- **OpenAI Codex:** In the Codex CLI, run `/plugins`, search for **Shopify**, and select **Add to Codex**.
- **VS Code:** Command Palette (`CMD+SHIFT+P`) → **Chat: Install Plugin From Source** → paste `https://github.com/Shopify/shopify-ai-toolkit`.

**What you get:**

- **Docs and API schemas:** Search Shopify's documentation and API schemas without leaving your editor.
- **Code validation:** Validate GraphQL queries, Liquid templates, and UI extensions against Shopify's schemas.
- **Store management:** Manage your Shopify store through the CLI's store execute capabilities.
- **Auto-updates:** The plugin updates automatically as new capabilities are released.

**Telemetry / opt-out.** The skill scripts (`scripts/search_docs.mjs`, `scripts/validate.mjs`, `scripts/log_skill_use.mjs`) send a usage event to `https://shopify.dev/mcp/usage` on each invocation (tool name, skill name/version, model/client name, search query + response, validation result, etc.). A `PostToolUse` hook emits a `skill_invocation` event. **This is on by default.** To opt out — for skill scripts, the MCP server, and the hook — set:

```
OPT_OUT_INSTRUMENTATION=true
```

> **Contributing:** "Thanks for your interest but we don't accept pull requests. Any pull requests will be automatically closed."

---

### 4.3 Dev MCP — tool esposti & variabili d'ambiente

> Fonte: estratti dal codice `dist/` del pacchetto npm **`@shopify/dev-mcp@1.14.0`** (verifica diretta via `npm pack` + grep, 2026-06-08). Allineati con la descrizione ufficiale ("search our docs, introspect API schemas") del [changelog del 31 marzo 2025](https://shopify.dev/changelog/mcp-server-for-the-shopify-dev-assistant).

Il Dev MCP server espone i seguenti tool (nomi confermati come stringhe registrate nel codice):

| Tool | Scopo (da nome + descrizione nel codice) |
| - | - |
| `learn_shopify_api` | Tool di bootstrap: l'agente lo chiama per primo per imparare a usare le API Shopify e ottenere il contesto/versione corretti (controlla `shopify.app.toml`, `extension.toml`, ecc.). |
| `search_docs_chunks` | Cerca su shopify.dev documentazione ed esempi di codice (ricerca a "chunk"). |
| `fetch_full_docs` | Recupera il contenuto completo di pagine di documentazione specifiche per dettaglio. |
| `introspect_graphql_schema` | Esplora e recupera sezioni rilevanti dello schema GraphQL (Admin/Storefront) via introspezione. |
| `validate_graphql_codeblocks` | Valida blocchi di codice GraphQL contro lo schema Shopify. |
| `validate_theme` | Valida un tema (file/path di tema). |
| `validate_theme_codeblocks` | Valida blocchi di codice Liquid/tema. |
| `validate_component_codeblocks` | Valida blocchi di codice di componenti (es. Polaris / web components). |

> ⚠️ Nota: non verificato / in evoluzione — La pagina dev ufficiale **non pubblica più una tabella discorsiva dei tool del Dev MCP** (rimanda all'AI Toolkit). I nomi sopra sono accurati per la **v1.14.0**; possono cambiare tra versioni. Per la lista autoritativa in runtime, interroga il server con `tools/list`.

**Variabili d'ambiente (estratte da `dist/`):**

| Env var | Effetto |
| - | - |
| `OPT_OUT_INSTRUMENTATION` | Disattiva la telemetria (`=true`). |
| `LIQUID_VALIDATION_MODE` | Controlla la modalità di validazione Liquid. |
| `MCP_INSTRUCTIONS_OVERRIDE_DIR` | Directory per override delle istruzioni MCP. |
| `STOREFRONT_WEB_COMPONENTS` | Abilita supporto/contesto per Storefront Web Components. |
| `USE_LEGACY_SEARCH` | Usa il motore di ricerca legacy invece del nuovo `search_docs_chunks`. |
| `NODE_ENV` | Standard Node environment. |

---

### 4.4 Changelog di riferimento

> Fonte: <https://shopify.dev/changelog/mcp-server-for-the-shopify-dev-assistant> (posted **March 31, 2025**)

Shopify released an MCP Server that integrates with AI assistants like Cursor and Claude desktop. It "gives your AI assistant access to Shopify's development resources, enabling it to search our docs, introspect API schemas, and get up-to-date answers about Shopify APIs." Key features: searching Shopify's documentation, introspecting API schemas, obtaining current information about Shopify APIs.

> Fonte: <https://shopify.dev/changelog/shopify-ai-toolkit-connect-your-ai-tools-to-the-shopify-platform> (posted **April 9, 2026**)

The Shopify AI Toolkit is now available. Developers can "build apps using Shopify's documentation, API schemas, and code validation, and manage your Shopify store through the CLI's store execute capabilities." Supported tools: Claude Code, Cursor, Gemini CLI, Visual Studio Code, Codex CLI (skills and MCP only). Installable via plugin (primary), agent skills, or the Dev MCP server.

---

## 5. Building AI on Shopify

> Fonte: sintesi verificata dalle pagine ufficiali già citate sopra (AI Toolkit, Storefront MCP, `/docs/agents`). Non esiste, al 2026-06-08, una pagina unica intitolata "Building AI experiences on Shopify" con contenuto distinto: la guida è distribuita tra l'AI Toolkit (lato sviluppo) e i server MCP (lato runtime/shopping). Vedi anche la nota in fondo su Sidekick.

Shopify offre due piani su cui costruire esperienze AI:

1. **Lato sviluppo (build apps/themes con assistenza AI).** Usa la **Shopify AI Toolkit** / **Dev MCP** per dare all'agente di coding accesso a documentazione, schemi GraphQL e validazione del codice (sezione 4). Il pattern chiave è il **forced validation loop**: gli skill come `shopify-admin`, `shopify-liquid`, `shopify-functions`, `shopify-hydrogen` includono script (`scripts/search_docs.mjs`, `scripts/validate.mjs`) che l'agente è tenuto a eseguire per verificare sintassi e compatibilità di schema prima di restituire codice.

2. **Lato runtime (build agentic shopping experiences).** Usa i **server MCP UCP-compliant** (Storefront/Catalog/Cart/Checkout/Order, sezione 3) per far sì che un agente cerchi prodotti, costruisca carrelli, crei checkout e tracci ordini per conto di un buyer. L'architettura a due livelli — **Storefront MCP** per il singolo store e **Catalog MCP (Global)** per la discovery cross-merchant — espone il commercio alla granularità ottimale per ogni task.

Funzione di "function calling": i tool MCP **sono** le funzioni che il modello chiama (JSON-RPC `tools/call`), quindi il "function calling" su Shopify si realizza connettendo il modello a questi server MCP via un MCP client (il backend della tua app), come descritto in *About Storefront MCP* (sezione 3.1).

> ⚠️ Nota: non verificato / in evoluzione — **Sidekick for developers.** Il changelog "MCP Server for the Shopify dev assistant" e materiale di terze parti collegano il Dev MCP al "Shopify dev assistant" (e a *Sidekick* come assistente AI merchant-facing nell'admin). Al 2026-06-08 **non è stata trovata una pagina dev ufficiale con API/SDK per costruire *su* Sidekick** come piattaforma per sviluppatori; Sidekick risulta un prodotto merchant-facing nell'admin, non un'API documentata. Non documentare API Sidekick non confermate.

---

## Cosa NON è stato trovato / da verificare

Argomenti cercati ma **non** confermati come documentazione dev ufficiale (o solo parzialmente), al 2026-06-08:

- **Repo `github.com/Shopify/dev-mcp` standalone** — restituisce **404**. Il README è ora dentro `github.com/Shopify/Shopify-AI-Toolkit`. Il pacchetto npm `@shopify/dev-mcp@1.14.0` esiste ma il tarball non include README; i nomi dei tool sono stati estratti dal `dist/`.
- **Tabella ufficiale dei tool del Dev MCP** — la pagina dev non pubblica più una tabella discorsiva; rimanda all'AI Toolkit. I tool elencati (sezione 4.3) sono verificati dal codice 1.14.0, non da una tabella di prosa ufficiale.
- **Universal Cart API** — annunciata su `/docs/agents` ma in *early access* (waitlist); nessuna pagina di reference pubblica con endpoint/tool.
- **`/sitemap_agentic_discovery.xml`** — citato da blog/community di terze parti come endpoint auto-shipped; **nessuna pagina dev ufficiale** trovata che lo documenti. Confermati invece: `/agents.md`, `/llms.txt`, `/llms-full.txt`, `/.well-known/ucp`, `/api/ucp/mcp`, `/api/mcp`.
- **Nomi dei tool del Customer Accounts MCP** — la pagina ufficiale non li elenca per nome; rimanda a `tools/list` per la scoperta runtime degli schemi. Non inventati qui.
- **Sidekick "for developers" (API/SDK)** — nessuna pagina dev ufficiale con API per costruire su Sidekick; risulta prodotto merchant-facing nell'admin. Da verificare se/quando Shopify pubblicherà una developer surface.
- **Pagina unica "Building AI experiences on Shopify"** — non esiste come pagina singola distinta; la guida è distribuita tra AI Toolkit e server MCP (sezione 5 è una sintesi verificata, non una pagina catturata 1:1).

### Pagine ufficiali confermate ma NON catturate integralmente in questo capitolo (riferimenti, per completezza)

Confermate esistenti via WebSearch/link interni, non fetchate per intero (coperte concettualmente sopra o fuori scope di dettaglio):

- `https://shopify.dev/docs/agents/get-started/authentication` (tutorial "Authenticate your agent")
- `https://shopify.dev/docs/agents/get-started/search-catalog` (tutorial "Discover products with Shopify Catalog")
- `https://shopify.dev/docs/agents/get-started/build-a-cart`
- `https://shopify.dev/docs/agents/get-started/checkout`
- `https://shopify.dev/docs/agents/catalog/global-catalog` e `.../storefront-catalog` (reference UCP per i tre tool, già catturati a livello di About Catalogs)
- `https://shopify.dev/docs/agents/catalog/global-catalog-extension` e `.../storefront-catalog-extension`
- `https://shopify.dev/docs/agents/orders/order-mcp` (`get_order`) e `.../orders/order-webhooks`
- `https://shopify.dev/docs/apps/build/storefront-mcp/build-storefront-ai-agent` (tutorial)
- Specifica UCP esterna: `https://ucp.dev/` (protocollo open, Apache 2.0, co-sviluppato con Google)
