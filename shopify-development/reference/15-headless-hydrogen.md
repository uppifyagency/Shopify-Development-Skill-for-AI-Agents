# 15. Headless & Hydrogen

Headless commerce decouples the storefront (the frontend customers see) from the commerce engine (Shopify's backend). Instead of using Online Store themes and Liquid, you build a custom frontend in any framework and connect it to Shopify through the Storefront API and the Customer Account API. Shopify offers a "batteries-included" path — **Hydrogen**, its React-Router-based framework, deployed for free on **Oxygen**, its global edge hosting — as well as a "bring your own stack" path where you wire Shopify's composable APIs into your existing infrastructure.

This chapter collects the conceptual and how-to **guides** for building headless on Shopify. It does **not** reproduce the auto-generated GraphQL schema for the Storefront API or the Customer Account API, nor the full per-component/per-hook Hydrogen API reference — those huge reference trees are linked under "Pagine aggiuntive (URL elencati, non estratti)" at the end of each section.

## Indice

1. **Headless overview** — what headless is, build options, the Headless channel, Storefront API access tokens, Hydrogen vs custom.
2. **Hydrogen** — getting started, project structure, routing, data fetching, components & hooks, caching, SEO, deployment.
3. **Oxygen** — deploying to Shopify's edge hosting, environments, CDN/caching.
4. **Customer Account API** — overview, authentication, and usage guides.
5. **Storefront API usage** — querying, pagination, cart, metafields (guides only).

---

# Parte 1 — Headless overview

Mini-TOC:
- Build Headless Commerce (overview)
- Custom storefronts (getting started)
- Options for building headless (build options)
- Bring your own headless stack
- Building with the Storefront API
- Getting started with the Storefront API
- Manage the Headless channel

## Build Headless Commerce

> Fonte: https://shopify.dev/docs/storefronts/headless

Get all the power of Shopify under the hood, with complete control over the frontend. Start building quickly with Hydrogen, Shopify's official headless framework, or add Shopify APIs to your existing tech stack.

### Hydrogen and Oxygen

Get started fast with Shopify's batteries-included framework for headless commerce. Build with off-the-shelf components, then deploy for free.

```terminal
npm create @shopify/hydrogen@latest
```

#### Build-ready components

Hydrogen includes a suite of components and utilities pre-wired for Shopify APIs. Skip writing boilerplate code and focus on creating high-performance storefronts tailored to your unique brand.

#### Free hosting

Deploy your Hydrogen app to Oxygen, Shopify's global edge hosting platform. Get continuous deployment, push-to-preview, and instant rollbacks included at no extra cost.

#### Fast by default

Hydrogen is built on React Router, so speed comes standard. Server-side rendering, progressive enhancement, and nested routes ensure that your storefront always feels fast.

### Bring your own stack

Use any framework, tooling, or hosting—Shopify's composable APIs can integrate into your existing infrastructure and workflows. Install the Headless channel to create storefronts and manage API tokens and permissions quickly.

#### Get headless apps for your custom storefront

Integrate the latest apps and platforms with your custom storefront, so you can focus on building what's unique to your experience.

---

## Custom storefronts

> Fonte: https://shopify.dev/docs/storefronts/headless/getting-started

Commerce is constantly evolving. As a developer, you can build commerce integrations in all the places where merchants want to sell and where their customers want to buy. This guide introduces you to building headless with Shopify by explaining custom storefronts, how they work, and how they accelerate your commerce development.

### What is a custom storefront?

A custom storefront is a model of building headless, where the frontend and backend of your storefront are independent of each other. You build the frontend. Merchants use Shopify's commerce engine behind their bespoke storefront experiences.

### How custom storefronts work

A custom storefront is designed, built, and managed by you. This is the frontend. You can use your preferred tech stack and a development framework that you already know to build faster. You build headless by integrating your custom frontend with Shopify's powerful commerce primitives, capabilities, and backend operations.

#### Data and commerce capabilities

Your custom storefront uses data and commerce capabilities from Shopify. This is the backend. Data might include products, collections, and customers. Commerce capabilities might include cart and international pricing.

#### Building on an API-first platform

Headless commerce doesn't apply just to websites. For example, Shopify can also be used in other kinds of shopping experiences such as mobile apps, video games, smart devices, and more.

The benefit of building on an API-first platform is the flexibility and power of enabling new customer touchpoints, while using the same shared commerce data and backend tools that the Shopify platform provides.

Complex solutions can involve connecting other business systems to the frontend or backend, such as the following:

* Content management systems (CMS)
* Customer relationship management (CRM)
* Enterprise resource planning (ERP) systems
* Product information management (PIM) systems

### When should I build a custom storefront?

If a merchant's desired business system architecture, business process, or customer experience can't be achieved with Shopify's existing sales channels, custom themes, and apps, then consider building a custom storefront.

Consider building a custom storefront in the following scenarios:

* You're building a unique storefront experience that isn't possible or easily achievable with existing web or mobile tools.
* You have an existing web frontend technology stack that doesn't include Liquid.
* You want to integrate Shopify-powered commerce into an existing infrastructure.
* You have robust omni-channel needs, with multiple channels not being offered out of the box.
* You're either using or looking to use a content management system (CMS) for more complex content needs that are integrated into your storefront experience.

However, before taking on the commitment, make sure that the merchant is comfortable with taking on the added costs and complexity of managing a custom storefront solution. The merchant should also have development resources available to manage the ongoing integration after launch.

### Key benefits

Building a custom storefront offers the following key benefits:

* **Flexibility**: The Storefront API is device-agnostic and platform-agnostic. You can build a custom storefront using any programming language, which makes your workflow flexible.
* **Customization**: You can build a solution that grows and adapts with a merchant's business. As customer trends and interactions change, the commerce solution can adapt quickly to long-term market shifts in customer acquisition.
* **Integration**: Bring your own tools, technology stack, and experience, and integrate your custom backend with Shopify commerce data.

### Examples

With a custom storefront solution, you have complete flexibility in your frontend tech stack and development framework. The following examples describe some of the ways that you can customize a storefront:

* Sell products from a native mobile app or a progressive web application (PWA)
* Sell products in augmented reality (AR) or virtual reality (VR) game experiences
* Sell products in video livestreams
* Sell products through the Internet of things (IoT), such as selling food directly from a smart fridge
* Sell products through a buy button added to an existing website

#### Hydrogen demo store

The Hydrogen demo store is Shopify's example custom storefront. You can refer to it to understand how a custom storefront can be put together, or fork it as a starting point to build your own custom storefront.

[Explore the source code of the example Hydrogen demo store.](https://github.com/Shopify/hydrogen-demo-store)

### Build options

Shopify provides a range of development frameworks, SDKs, and software tools to accelerate your development process.

### Next steps

* Learn about your options for building custom storefronts.

---

## Options for building headless

> Fonte: https://shopify.dev/docs/storefronts/headless/getting-started/build-options

There are many options to build custom storefronts that integrate with Shopify using the Storefront API.

The Hydrogen stack is Shopify's opinionated fullstack approach. There are alternative tools and options for any stack that you might choose.

| Customization type | Build with |
| - | - |
| Build a custom storefront with a React Router app and Shopify's frontend commerce tooling | Hydrogen |
| Build a custom storefront using a third-party React framework and Shopify's library of components, reusable functions, and utilities | Hydrogen React |
| Build headless using the framework of your choice and Shopify's backend using only the Storefront API | Headless channel |

### Hydrogen and Oxygen

Built on React Router, Hydrogen is "a Shopify storefront toolkit that provides a set of components, functions, and utilities used for building custom storefronts on React Router apps." It integrates with the Storefront API to access commerce data.

### Channels

You can use the Shopify admin to manage your commerce data across multiple channels to ensure all customer touchpoints remain synchronized. You can create custom channels complementary to your online store, such as mobile apps or alternative websites.

#### The Hydrogen channel

The Hydrogen channel enables deployment of Hydrogen storefronts to Oxygen, Shopify's included edge hosting environment. It automatically creates and populates the environment variables necessary for Storefront API integration.

The Shopify GitHub integration for Oxygen allows you to connect a Git repository to the Hydrogen channel within the Shopify admin. GitHub provides version control, change history tracking, and centralized code management.

The Hydrogen channel also provides order attribution, enabling visibility into GMV generated through the channel within your Shopify admin.

You can install the Hydrogen channel through the Shopify App Store.

#### The Headless channel

The Headless channel enables "headless and self-hosted Hydrogen experiences" without requiring a custom app.

This channel "provides a single place to create and manage access tokens for the Storefront API." You can create multiple custom storefronts with automatically included public and private access tokens. The channel allows you to rotate private access tokens and manage storefront permissions.

The channel includes Shopify's standard channel features: product publishing, order attribution, and analytics with sales reporting by channel. Order attribution operates at the channel level.

### Additional SDKs

Shopify provides a range of SDKs and software tools to accelerate development. These tools help you create unique buying experiences across websites, apps, and video games.

### Next steps

Build a custom storefront with the following options:

* Add the Headless channel and get started building with the Storefront API
* Get started with Hydrogen React
* Get started with Hydrogen and begin building a custom storefront

---

## Bring your own headless stack

> Fonte: https://shopify.dev/docs/storefronts/headless/bring-your-own-stack

Shopify's composable commerce APIs allow you to integrate Shopify into nearly any technology stack, so you have the freedom to use the frameworks, hosting, and workflows that work best for you.

### Install the Headless channel

To start accessing the Storefront API and the Customer Account API, you need to install the [Headless channel](https://apps.shopify.com/headless) from the Shopify App Store.

This channel gives you a single place to manage API access for all your client applications. It enables you to publish products to the Headless sales channel, as well as manage API permissions and credentials.

> **Info:** If you want to display products on an existing site or platform, you can skip installing the Headless channel and use [Storefront Web Components](https://shopify.dev/docs/api/storefront-web-components) instead.

### Create a storefront

You can create multiple storefronts in the Headless channel.

Each storefront has its own set of API tokens, but all storefronts in the Headless channel share the same API permissions.

1. From your Shopify admin, under **Sales channels**, click **Headless**.
2. Click **Add storefront**.
3. (Optional) On the storefront detail page, click **Rename** to edit the storefront's default name.

### Manage API permissions

You can control which store data is available through the Storefront or Customer Account APIs. All storefronts in the Headless channel share the same API permissions.

1. From your Shopify admin, under **Sales channels**, click **Headless**.
2. Click the name of the storefront that you want to update.
3. Under **Manage API access**, click **Manage** for the API that you want to update.
4. Under **Permissions**, click the edit icon.
5. Check the permission scopes that you want enabled.
6. Click **Save**.

### Rotate API credentials

For security purposes, you can update your API credentials at any time.

1. From your Shopify admin, under **Sales channels**, click **Headless**.
2. Click the name of the storefront to update.
3. Under **Manage API access**, click **Manage** for the API that you want to update.
4. Under **Rotate credentials**, click **Generate new token**. Both the old and new credentials are valid until you delete the old credentials.
5. Update your client apps with the new credentials.

* The Storefront API access relies on an API token.
* The Customer Account API might have a Client ID and a Client Secret, depending on the type of access.

6. After you've updated your apps, delete the old credentials by clicking **Revoke**.

### Configure routes

The standard format for product URLs is `/products/:handle`. If your storefront uses a different structure, then it's recommended that you provide a server-side redirect (3XX) from the expected `/products/:handle` path to the product page.

It's also recommended that your storefront supports [cart permalinks](https://help.shopify.com/en/manual/checkout-settings/cart-permalink). [View example implementation](https://github.com/Shopify/hydrogen-demo-store)

### Delete a storefront

Deleting a storefront in the Headless channel revokes all its access tokens. You need to update any clients using those tokens.

1. From your Shopify admin, under **Sales channels**, click **Headless**.
2. Click the name of the storefront that you want to delete.
3. Click **Delete storefront**.
4. To confirm, click **Delete storefront**.

### Next steps

From here, what you build is up to you! The Storefront API and the Customer Account API provide a wide selection of commerce primitives that enable you to integrate Shopify into your existing tech stack, or create something new.

* Learn more about [getting started with the Storefront API](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api).
* Learn more about [getting started with the Customer Account API](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api).
* Learn more about [headless with B2B](https://shopify.dev/docs/storefronts/headless/bring-your-own-stack/b2b).
* Consult the complete [Storefront API Reference](https://shopify.dev/docs/api/storefront).
* Consult the complete [Customer Account API Reference](https://shopify.dev/docs/api/customer).

---

## Building with the Storefront API

> Fonte: https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api

The Storefront API is the foundational layer of custom storefronts. It provides you the commerce primitives to build custom, scalable, and performant shopping experiences.

### What is the Storefront API?

The Storefront API provides access to Shopify's primitives and capabilities such as displaying products and collections, adding items to the cart, calculating contextual pricing, and more.

You can use the Storefront API to build unique commerce experiences on any platform, including the web, native apps, games, and social media, using the frontend tools of your choice.

### When to use the Storefront API

The Storefront API helps you create a seamless and engaging shopping experience for your customers by leveraging the robust commerce functionality of Shopify. Headless builds are made efficient and performant with the following resources:

* **Built-in commerce essentials**: Leverage the full power of the Shopify admin to manage your back-office products like pricing, inventory, and metafields. Use the Storefront API to deliver performant buyer experiences with optimized cart, contextual pricing, subscriptions, and more.
* **Operate at a global scale**: Backed by the infrastructure that supports over 2 million Shopify businesses, build your custom storefront on the platform that's fast, flexible, and feature-rich.
* **Build your way**: Bring your own tech stack, requirements, and experience. Build on top of Shopify's proven Storefront API that serves 1M+ queries per minute.
* **Developer tools**: Improve your developer experience by helping you learn about the API.

Because the Storefront API uses the Shopify backend, you can focus on building a unique and customized shopping experience with strong brand representation. You can create custom pages, themes, and order management experiences that are fully integrated with a storefront.

### API versioning

The Storefront API is versioned, with new releases four times a year. We strongly recommend updating your apps to make requests to the latest stable API version every quarter. However, if your app uses a stable version that is no longer supported, then Shopify falls forward and responds to your request with the same behavior as the oldest supported stable version.

### Authentication and authorization

The Storefront API supports both tokenless access and token-based authentication.

#### Tokenless access

Tokenless access allows API queries without an access token providing access to essential features such as:

* Products and Collections
* Selling Plans
* Search
* Pages, Blogs, and Articles
* Cart (read/write)

Tokenless access has a query complexity limit of 1,000. Query complexity is calculated based on the cost of each field in the query.

#### Token-based authentication

For access to all Storefront API features, an access token is required. The following features require token-based authentication:

* Product Tags
* Metaobjects and Metafields
* Menu (Online Store navigation)
* Customers

The Storefront API has the following types of token-based access:

**Public Authentication**: The public token is used for client side queries and mutations. As every buyer has a different IP, the token scales to support large amounts of traffic.

**Private Access**: The private token provides authenticated access to the Storefront API and is used for server-side queries and mutations.

> **Caution:** Unlike public access tokens, private access tokens should be treated as secret and not used on the client-side. We recommend only requesting the scopes that your app needs, to reduce the security risk if the token leaks.

### What is the Headless channel?

Make headless and self-hosted Hydrogen experiences possible in the Headless channel without needing to create a custom app.

The Headless channel provides a single place to create and manage access tokens for the Storefront API. You can use the channel to create multiple custom storefronts. Storefronts that you create through the channel automatically include public and private access tokens with shop permission for the Storefront API. In the channel, you can rotate your private access token and manage storefront permissions.

Additionally, the channel gives you all of Shopify's channel features, such as product publishing and order attribution, and analytics and reporting sales by channel.

Order attribution is at the channel level, and a Headless storefront is treated as a channel.

[Get started with the Headless channel](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/getting-started).

### Reference

[Storefront API reference](https://shopify.dev/docs/api/storefront)

Consult the Storefront API reference for available objects, queries, and mutations.

### Developer tools

Shopify provides tools to help you learn how to use the Storefront API.

[Storefront API GraphiQL explorer](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/api-exploration/graphiql-storefront-api) — Use the interactive GraphiQL explorer for the Storefront API on a demo shop.

[Storefront API learning kit](https://github.com/Shopify/storefront-api-learning-kit) — A downloadable package of a complete set of sample GraphQL queries to the Storefront API.

### Limitations

* You can have a maximum of 100 active storefronts and access tokens per shop.

### Next steps

* [Get started](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/getting-started) building headless with the Storefront API and start querying data.

---

## Getting started with the Storefront API

> Fonte: https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/getting-started

> **Note:** If you're building with Hydrogen, then refer to the Hydrogen documentation for getting started.

The Storefront API is a GraphQL API that requires an access token associated with a specific Shopify store. You can call the API from any HTTP client.

You can have a maximum of 100 active storefronts and access tokens per shop.

The Shopify API is framework agnostic. You can build using your framework of choice, such as Hydrogen, Next.js, Vue, and more. This guide teaches you how to get started building a storefront.

### What you'll learn

In this tutorial, you'll learn how to do the following tasks:

* Install the Headless channel to your Shopify admin
* Generate Storefront API access tokens
* Manage storefront permissions

### Requirements

* You have the staff role on the Shopify store that you're working with.
* You have **Apps and channels** permissions on the Shopify store that you're working with.

### Step 1: Enable Storefront API access

Install the Headless channel from the Shopify App Store. On installation, click **Create storefront** to generate public and private access tokens that enable public and private, authenticated access to the Storefront API.

Make note of the private access token, as you'll use this token to authenticate requests to the Storefront API.

#### (Optional) Create another storefront

> **Note:** The following instructions assume that you've pinned the Headless channel in your Shopify admin. If you haven't, then you can access the channel using the **Search** field.

1. From your Shopify admin, under **Sales channels**, click **Headless**.
2. Click **Add storefront**.

### Step 2: Manage permissions

Managing permissions controls what your custom storefront can display from your Shopify store.

1. From your Shopify admin, select the **Headless** sales channel.
2. From the list, select the storefront.
3. Beside **Storefront API permissions**, click **Edit**.
4. Select the permissions for the storefront.
5. Click **Save**.

### Step 3: Set up request headers

Before you make requests to the Storefront API, you need to set up your request headers with the private access token that you received when creating your storefront. To learn more about how to set up request headers for your development framework, refer to the Storefront API reference.

### Step 4: Make queries

After you've selected the Storefront API permissions for your custom storefront and have Storefront API access tokens, you can make queries using the Storefront API.

Shopify provides the following resources for learning how to make GraphQL queries to Shopify's Storefront API:

* **GraphiQL explorer**: Start exploring the Storefront API on a demo shop with the interactive GraphiQL explorer.
* **Storefront API Learning Kit**: Download example queries from the Storefront API Learning Kit.

### Next steps

* Learn how to manage your Headless channel, including how to rotate private access tokens.
* Learn how to query products and collections.

---

## Manage the Headless Channel

> Fonte: https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/manage-headless-channels

You can manage the Headless channel by creating new storefronts, rotating your private access tokens, editing store names, managing storefront permissions, order attribution, and more. The Headless channel gives you all of Shopify's channel features, such as product publishing, scheduled product publishing, analytics, and reporting sales by channel.

> **Note:** The following instructions assume that you've pinned the Headless channel in your Shopify admin. If you haven't, then you can access the channel using the **Search** field.

### What you'll learn

You'll learn how to do the following tasks:

* Add a custom storefront using the Headless channel
* View a list of your custom storefronts
* Edit storefront names
* Rotate private access tokens
* Edit storefront permissions
* Order attribution
* Delete storefronts

### Requirements

* You've completed the Getting started with the Storefront API guide.

### Add storefronts

You can have a maximum of 100 active storefronts and access tokens per shop.

1. From your Shopify admin, under **Sales channels**, click **Headless**.
2. On the **Storefronts** page, click **Add storefront**.

### View custom storefronts

1. From your Shopify admin, under **Sales channels**, click **Headless**.
2. On the **Storefronts** page, optionally select a storefront to view it.

### Edit storefront names

1. From your Shopify admin, under **Sales channels**, click **Headless**.
2. On the **Storefronts** page, select the storefront to rename.
3. Beside **Storefront name**, click **Edit**.
4. Type the new name for the storefront.
5. Click **Save**.

### Rotate private access tokens

> **Caution:** "After you delete your old private access token, you need to update any applications or scripts to use the new token, or else you won't be able to access the Storefront API."

1. From your Shopify admin, under **Sales channels**, click **Headless**.
2. On the **Storefronts** page, select the storefront to rotate the access tokens for.
3. In the **Storefront API tokens** card, under **Rotate private access token**, click **Generate new token**.
4. Update any applications or scripts to use the new token. The old token remains valid until you delete it.
5. Beside the old private access token, click **Delete**.
6. When prompted, click **Delete token**.

### Request storefront permissions

Permissions control what Storefront API data custom storefronts can display in your Shopify store. When you install the channel, a default set of permissions is created for you. You can edit these.

> **Caution:** "Both Storefront and Admin API permissions are shared across all storefronts."

1. From your Shopify admin, under **Sales channels**, click **Headless**.
2. On the **Storefronts** page, select a storefront to edit permissions for.
3. In the **Storefront API permissions** card, click **Edit**.
4. Select or deselect permissions for the store.
5. Click **Save**.

### Order attribution

Order attribution is at the channel level, and a Headless storefront is treated as a channel.

1. From your Shopify admin, click **Orders**.
2. In the **Channel** column, sales attributed to the Headless channel are displayed as the name of the **Storefront** through which the sale was made.

### Delete storefronts

> **Caution:** "Deleting a storefront invalidates its Storefront API tokens."

1. From your Shopify admin, under **Sales channels**, click **Headless**.
2. On the **Storefronts** page, select a storefront to edit permissions for.
3. In the **Delete storefront** card, click **Delete storefront**.
4. Click **Delete storefront**.

### Next steps

* Learn more about Storefront API authorization and rate limiting.
* Learn more about Storefront API access tokens.
* Learn how to publish products and schedule product publishing with the Headless channel.
* Learn how to view analytics and reporting sales by channel with the Headless channel.

---

# Parte 2 — Hydrogen

Hydrogen is Shopify's React-Router-based framework for headless commerce. It provides components, hooks and utilities pre-wired to Shopify APIs, a CLI, and first-class deployment to Oxygen.

Mini-TOC:
- Hydrogen (API overview)
- Getting started with Hydrogen and Oxygen
- Hydrogen and Oxygen fundamentals (architecture, project structure, React Router, Oxygen)
- Fetch Shopify API data in Hydrogen (data fetching)
- Fetch third-party API data with Hydrogen
- Performant data loading with Hydrogen
- Caching Shopify API data with Hydrogen and Oxygen
- Caching third-party API data with Hydrogen and Oxygen
- Analytics event tracking with Hydrogen
- SEO in Hydrogen
- Internationalization with Shopify Markets (overview + guides)
- Deployments (overview, GitHub CI/CD, custom CI/CD, environments)
- Migrate from the online store to Hydrogen
- Debugging (Subrequest Profiler)
- Cookbook (Express server, third-party API)

## Hydrogen (API overview)

> Fonte: https://shopify.dev/docs/api/hydrogen

Hydrogen represents Shopify's curated framework approach for headless commerce development. Built atop [React Router](https://reactrouter.com/home), it delivers "tools, utilities, and best-in-class examples for building dynamic and performant commerce applications."

### Setup

Begin by creating a new Hydrogen project through your preferred package manager, then import necessary components, hooks, or utilities into your application.

#### Creating a New Hydrogen Project

**npm**
```txt
npm create @shopify/hydrogen@latest
```

**yarn**
```txt
yarn create @shopify/hydrogen
```

### Authentication

Hydrogen requires authentication with both the [Storefront API](https://shopify.dev/docs/api/storefront) and the [Customer Account API](https://shopify.dev/docs/api/customer). The framework includes built-in API clients for secure query and mutation handling.

You may establish access tokens by installing either the [Hydrogen sales channel](https://apps.shopify.com/hydrogen) (which supports Oxygen hosting) or the [Headless sales channel](https://apps.shopify.com/headless) (for external hosting options). Both APIs provide public credentials suitable for client-side usage.

#### Authenticating a Hydrogen App

**server.js**
```js
const {storefront} = createStorefrontClient({
  cache,
  waitUntil,
  i18n: {language: 'EN', country: 'US'},
  publicStorefrontToken: env.PUBLIC_STOREFRONT_API_TOKEN,
  privateStorefrontToken: env.PRIVATE_STOREFRONT_API_TOKEN,
  storeDomain: env.PUBLIC_STORE_DOMAIN,
  storefrontId: env.PUBLIC_STOREFRONT_ID,
  storefrontHeaders: getStorefrontHeaders(request),
});
```

**.env**
```txt
SESSION_SECRET="foobar"
PUBLIC_STOREFRONT_API_TOKEN="3b580e70970c4528da70c98e097c2fa0"
PUBLIC_STORE_DOMAIN="hydrogen-preview.myshopify.com"
```

### Versioning

Hydrogen releases align with quarterly [Storefront API](https://shopify.dev/api/storefront) versions. For instance, Storefront API version `2023-10` pairs with Hydrogen versions `2023.10.x`.

> **Caution:** Breaking changes in API versions carry forward to corresponding Hydrogen releases.

### Hydrogen and Hydrogen React

Hydrogen is "built on React Router," though many components, hooks, and utilities derive from [Hydrogen React](https://shopify.dev/docs/api/hydrogen-react), a framework-agnostic package. The Hydrogen package re-exports these resources for convenience, so imports should target `@shopify/hydrogen`.

#### Importing Hydrogen Components

**example-page.jsx**
```jsx
import {ShopPayButton} from '@shopify/hydrogen';

export function renderShopPayButton({variantId, storeDomain}) {
  return <ShopPayButton variantIds={[variantId]} storeDomain={storeDomain} />;
}
```

### Resources

- [Custom storefronts on Shopify](https://shopify.dev/custom-storefronts) — Design, build, and manage custom storefronts
- [Hydrogen on GitHub](https://github.com/Shopify/hydrogen) — Track the project, report issues, and preview upcoming features

---

## Getting started with Hydrogen and Oxygen

> Fonte: https://shopify.dev/docs/storefronts/headless/hydrogen/getting-started

This tutorial will walk you through the process of creating a new Hydrogen storefront, linking it to your Shopify store, and then deploying it to Oxygen.

### Requirements

* [Node.js v16.20+](https://nodejs.org/) and [npm v8.19+](https://www.npmjs.com/)
* [Hydrogen channel](https://apps.shopify.com/hydrogen)

### Step 1: Create a new Hydrogen storefront

In your terminal, create a new Hydrogen project using example data from [Mock.shop](https://mock.shop):

```text
npm create @shopify/hydrogen@latest -- --quickstart
```

> **Note:** The `--quickstart` flag is shorthand for a set of recommended options for trying Hydrogen. You can drop it to see the available customizations.

You'll see a confirmation message with some details about your new project:

```text
Shopify:   Mock.shop
Language:  JavaScript
Routes:
  • Home (/ & /:catchAll)
  • Page (/pages/:handle)
  • Cart (/cart/* & /discount/*)
  • Products (/products/:handle)
  • Collections (/collections & /collections/:handle)
  • Policies (/policies & /policies/:handle)
  • Blogs (/blogs/*)
  • Account (/account/*)
  • Search (/api/predictive-search & /search)
  • Robots (/robots.txt)
  • Sitemap (/sitemap.xml)
```

### Step 2: Run the dev server

After installation, open your new project and start the dev server:

```text
cd hydrogen-quickstart
shopify hydrogen dev
```

Once the dev server is running, open `http://localhost:3000` in your browser and you'll see Mock.shop inventory.

### Step 3: Link your Hydrogen project to Shopify

By default, your Hydrogen project displays example products from [Mock.shop](https://mock.shop). To show your own products, link your local project to Shopify, create a new storefront, and sync your environment variables.

1. Link your Hydrogen project to Shopify:

   ```text
   npx shopify hydrogen link
   ```

   Follow the prompts to log in to your Shopify account and create a new storefront:

   ```text
   ✓  my-shopify-store

       ?  Select a Hydrogen storefront to link:
       ✓  Create a new storefront

       ?  New storefront name:
       >  hydrogen-quickstart
   ```

2. Update your project's environment variables:

   ```text
   npx shopify hydrogen env pull
   ```

   Your terminal will show a diff like this:

   ```text
   - SESSION_SECRET="foobar"
       - PUBLIC_STORE_DOMAIN="mock.shop"
       + PUBLIC_STOREFRONT_ID=[ID]
       + PUBLIC_STOREFRONT_API_TOKEN=[TOKEN]
       + PRIVATE_STOREFRONT_API_TOKEN=[TOKEN]
       + PUBLIC_CUSTOMER_ACCOUNT_API_CLIENT_ID=[ID]
       + PUBLIC_CUSTOMER_ACCOUNT_API_URL=https://shopify.com/[ID]
   ```

To confirm that the link works, run `npm run dev` and open `http://localhost:3000`. You'll now see your storefront inventory in your browser.

### Step 4: Deploy to Oxygen

After your Hydrogen storefront is linked, you can deploy it to Oxygen hosting to make it publicly accessible:

1. Deploy your project to Oxygen:

   ```text
   npx shopify hydrogen deploy
   ```

2. At the prompt to pick which environment to deploy to, select **Preview**.

The Hydrogen CLI builds your storefront, creates a new Oxygen deployment, and returns a preview link in your terminal. Open the preview link in your browser to see the deployment URL.

### Next steps

Congratulations! You've created a new Hydrogen storefront, connected it to Shopify, and made your first deployment to Oxygen.

[Hydrogen and Oxygen fundamentals](https://shopify.dev/docs/storefronts/headless/hydrogen/fundamentals) — Explore the key components of the Hydrogen and Oxygen stack and how they work together.

---

## Hydrogen and Oxygen fundamentals

> Fonte: https://shopify.dev/docs/storefronts/headless/hydrogen/fundamentals

Hydrogen and Oxygen make up Shopify's recommended stack for headless commerce. The different parts of the system work together to make it faster and easier to build and deploy headless Shopify stores.

### Architecture

Three key parts of the Hydrogen stack work together to enable a unified developer experience:

| Technology | What it does |
| - | - |
| **Hydrogen** (App) | A set of components, utilities, and design patterns that make it easier to work with Shopify APIs. Hydrogen projects are React Router apps that are preconfigured with Shopify-specific features and functionality. Hydrogen handles API client credentials, provides off-the-shelf components that are pre-wired for Shopify API data, and includes CLI tooling for local development, testing, and deployment. |
| **React Router** (Framework) | The open-source React framework that Hydrogen is built on top of. React Router handles routing, data fetching, server-side rendering, UI reactivity, and styling. |
| **Oxygen** (Hosting) | Shopify's global serverless hosting platform, built for deploying Hydrogen storefronts at the edge. Oxygen handles deployment environments, environment variable management, caching, and integration with Shopify's CDN. |

Developing each layer of this tech stack together provides an end-to-end developer experience that reduces boilerplate code, improves productivity, and promotes optimal performance, accessibility, and SEO practices.

### Hydrogen

#### Project structure

Hydrogen projects are structured like typical React Router apps and you can configure them to your preferences. The following is the default Quickstart project structure:

```sh
📂 hydrogen-quickstart/
├── 📁 app/
│   ├── 📁 assets/
│   ├── 📁 components/
│   ├── 📁 graphql/
│   ├── 📁 lib/
│   ├── 📁 routes/
│   ├── 📁 styles/
│   ├── entry.client.jsx
│   ├── entry.server.jsx
│   └── root.jsx
├── 📁 public/
├── CHANGELOG.md
├── README.md
├── customer-accountapi.generated.d.ts
├── env.d.ts
├── jsconfig.json
├── package.json
├── postcss.config.js
├── server.js
├── storefrontapi.generated.d.ts
└── vite.config.js
```

#### Packages and dependencies

Hydrogen bundles a set of dependencies that work together to enable end-to-end development and deployment:

| Package | Description |
| - | - |
| `@shopify/hydrogen` | Main Hydrogen package. Contains components specific to React Router and utilities for interacting with Shopify APIs. Extends the framework-agnostic `@shopify/hydrogen-react` package. |
| `@shopify/hydrogen-cli` | CLI tool for working with Hydrogen projects. |
| `@shopify/mini-oxygen` | Local development server based on Oxygen. |
| `@shopify/remix-oxygen` | Remix adapter that enables Hydrogen to be served on Oxygen. |

#### Hydrogen channel

The Hydrogen sales channel app needs to be installed on your Shopify store to enable the following features:

* A Hydrogen sales channel where you can publish product inventory.
* Oxygen hosting, to deploy your Hydrogen projects.
* Managing storefronts and deployment environments, including environment variable management.
* Access to deployment logs.

#### Routes

The standard format for product URLs is `/products/:handle`. If your storefront uses a different structure, then it's recommended that you provide a server-side redirect (3XX) from the expected `/products/:handle` path to the product page.

It's also recommended that your storefront supports cart permalinks.

### React Router

React Router is the open-source React-based framework that Hydrogen is built on top of. Hydrogen projects are React Router apps with a set of preconfigured options, bundled with a collection of Shopify-optimized components and utilities. Hydrogen includes a custom React Router adapter that compiles your project for hosting on Oxygen.

> **Tip:** Consider completing "React Router's 30-minute getting started tutorial" for a solid foundation on the architecture and conventions of React Router apps.

#### Key React Router concepts

| Concept | Details |
| - | - |
| Nested routes | React Router maps the nesting logic of app URLs to the nesting logic of components and data-loading. This allows all page data to load in parallel, reducing overall load times. |
| Loaders | React Router loaders are functions that load data so that it can be rendered server-side, which reduces the amount of JavaScript that's sent to the client. In Hydrogen, loaders fetch data from Shopify APIs and third-party sources. |
| Actions | React Router actions are functions that accept web-standard form data from clients in order to update state, mutate data, or trigger side effects. |
| SSR | React Router apps default to server-side rendering (SSR), where their React components are rendered as HTML before being sent to the browser. |
| Progressive enhancement | Because React Router actions use web standard technology like HTML forms, they typically work without JavaScript, but can be enhanced with client-side JavaScript when it's available. This, along with an SSR-first approach, means React Router apps typically deliver smaller bundle sizes that load faster. |

### Oxygen

Oxygen is Shopify's global deployment platform that's built for hosting Hydrogen storefronts at the edge. It provides multiple deployment environments, so you can preview every change before shipping it to production. Oxygen supports continuous deployment using GitHub, or you can configure your own custom CI/CD system.

Enable access to Oxygen by installing the Hydrogen channel.

#### Supported plans

Oxygen is available at no extra charge on paid Shopify plans:

* Pause and build
* Basic
* Shopify
* Advanced
* Plus

Oxygen isn't available on Starter plans or development stores.

#### Technical specs

Oxygen is a worker-based JavaScript runtime, based on Cloudflare's open-source `workerd` library. It supports web standard APIs such as Fetch, Cache, Streams, Web Crypto, and more. Some Node.js APIs aren't available. Check the Oxygen runtime details for a complete list.

If you prefer, you can self-host Hydrogen.

#### Limitations

You can use Oxygen for hosting commerce storefronts. It's subject to the Shopify Acceptable Use Policy. Misuse or abuse of Oxygen might lead to throttling, suspension, or termination.

* **Workers:**
  * Must be 10 MB or less
  * The startup time (the duration it takes for the worker to begin processing requests) must be 400 milliseconds or less.
  * Must be named `index.js`. The optional source map file must be named `index.js.map`.
  * Are limited to 30 seconds of CPU time per request
  * Can consume 128 MB max of memory. Exceeding this limit could mean dropped requests.
  * Are limited to 110 custom environment variables
  * Outbound API requests must complete within 2 minutes

* **Static assets, maximum file sizes:**
  * Images: 20 MB
  * Video: 1 GB
  * 3D models: 500 MB
  * Other files: 20 MB

> **Caution:** Ensure your requests go directly to Oxygen. Because proxies can conflict with Oxygen's bot mitigation systems and cause SEO issues, Oxygen doesn't support proxies in front of your Oxygen deployments.

### Next steps

[Fetch product data from Shopify](https://shopify.dev/docs/storefronts/headless/hydrogen/data-fetching) — Learn how to query Shopify's Storefront API for product data and render it in Hydrogen.

---

## Fetch Shopify API data in Hydrogen

> Fonte: https://shopify.dev/docs/storefronts/headless/hydrogen/data-fetching

Hydrogen uses [Remix `loader` functions](https://remix.run/docs/main/route/loader) to handle all queries to the Storefront API, Customer Account API, and [third-party data sources](https://shopify.dev/docs/storefronts/headless/hydrogen/data-fetching/third-party).

Loading data efficiently is important to keeping your Hydrogen app fast and performant. Follow these examples and best practices to ensure your Hydrogen storefront is delivering the fastest experience for customers.

### Query Shopify APIs

Hydrogen provides built-in API clients for the Storefront API and the Customer Account API.

#### Query the Storefront API

The following is an example of how the `/products/:handle` route can query the Storefront API and then render that product data in a component.

> **Tip:** This example demonstrates a simple version of this pattern. However, it can be extended to cover more complex behaviors, including more robust error handling, GraphQL query fragments and directives, deferred loading for non-critical data, server-side caching for non-personalized data, and more.

**Query product data from the Storefront API — `/app/routes/products.$productHandle.jsx`**

JavaScript:

```jsx
import {useLoaderData} from '@shopify/remix-oxygen';

// Fetch and return API data with a Remix loader function
export async function loader({params, context}) {
  const {handle} = params;
  const {storefront} = context;
  const {product} = await storefront.query(PRODUCT_QUERY, {
    variables: {handle},
  });
  return {product};
}

// Render the component using data returned by the loader
export default function Product() {
  const {product} = useLoaderData();
  return (
    <h1>{product.title}</h1>
  )
}

// Query the product title by its ID
const PRODUCT_QUERY = `#graphql
  product(handle: $handle) {
    title
  }`
```

TypeScript:

```tsx
import {useLoaderData} from '@shopify/remix-oxygen';
import type { LoaderArgs } from '@shopify/remix-oxygen';
import type { Product } from '@shopify/hydrogen/storefront-api-types';

// Fetch and return API data with a Remix loader function
export async function loader({params, context}: LoaderArgs) {
  const {handle} = params;
  const {storefront} = context;
  const {product} = await storefront.query(PRODUCT_QUERY, {
    variables: {handle},
  });
  return {product};
}

// Render the component using data returned by the loader
export default function Product() {
  const {product} = useLoaderData<typeof loader>();
  return (
    <h1>{product.title}</h1>
  )
}

// Query the product title by its ID
const PRODUCT_QUERY = `#graphql
  product(handle: $handle) {
    title
  }
`
```

#### Query the Customer Account API

The following is an example of how the `/account/order/:id` route can query the Customer Account API to display information about a single order. This example assumes that a customer is logged in.

**Query customer order data from the Customer Account API — `app/routes/account.orders.$id.tsx`**

JavaScript:

```jsx
import {useLoaderData} from '@shopify/remix-oxygen';

// Fetch and return API data with a Remix loader function
export async function loader({params, context}) {
  const orderId = atob(params.id);

  const {data, errors} = await context.customerAccount.query(
    CUSTOMER_ORDER_QUERY,
    {
      variables: {orderId},
    },
  );

  if ((errors && errors.length) || !(data && data.order)) {
    throw new Error('Order not found');
  }

  return {order: data.order};
}

// Render the component using data returned by the loader
export default function Order() {
  const {order} = useLoaderData();

  if (order) {
    return (
      <h1>{order.name}</h1>
    )
  }
}

// Query the order name by its ID
const CUSTOMER_ORDER_QUERY = `#graphql
  query Order($orderId: ID!) {
    order(id: $orderId) {
      name
    }
  }`
```

TypeScript:

```tsx
import {useLoaderData} from '@shopify/remix-oxygen';
import type { LoaderArgs } from '@shopify/remix-oxygen';

// Fetch and return API data with a Remix loader function
export async function loader({params, context}: LoaderArgs) {
  const orderId = atob(params.id);

  const {data, errors} = await context.customerAccount.query(
    CUSTOMER_ORDER_QUERY,
    {
      variables: {orderId},
    },
  );

  if (errors?.length || !data?.order) {
    throw new Error('Order not found');
  }

  return {order: data.order};
}

// Render the component using data returned by the loader
export default function Order() {
  const {order} = useLoaderData();

  if (order) {
    return (
      <h1>{order.name}</h1>
    )
  }
}

// Query the order name by its ID
const CUSTOMER_ORDER_QUERY = `#graphql
  query Order($orderId: ID!) {
    order(id: $orderId) {
      name
    }
  }`
```

### Caching loaded data

Hydrogen caches Storefront API data by default. It also includes a set of utilities to customize caching rules for individual API queries. Consult the [Hydrogen caching docs](https://shopify.dev/docs/storefronts/headless/hydrogen/caching) for more details about configuring server-side cache rules, including creating your own custom caching rules.

> **Note:** To avoid storing Personally Identifiable Information (PII) or other sensitive data, "the Customer Account API client doesn't cache any requests." Caching this information could lead to unauthorized access or data breaches, compromising user privacy and security.

> **Caution:** The Storefront API client caches responses by default. If you query customer-specific data through the Storefront API (for example, the `customer` query), you must explicitly disable caching at both the subrequest and full-page levels to avoid leaking personal data to other users. Learn how to [prevent caching customer-specific data](https://shopify.dev/docs/storefronts/headless/hydrogen/caching#prevent-caching-customer-specific-data).

The following simplified example shows how to cache data for longer when querying for the product title, which is an API resource that typically doesn't change frequently:

**Customizing caching in loader functions — `/app/routes/products.$productHandle.jsx`**

JavaScript:

```jsx
import {useLoaderData} from '@shopify/remix-oxygen';

export async function loader({params, context}) {
  const {handle} = params;
  const {storefront} = context;
  const {product} = await storefront.query(PRODUCT_QUERY, {
    variables: {handle},
    // Pass a `cache` option with your query to customize API request caching.
    cache: storefront.CacheLong()
  });
  return {product};
}

export default function Product() {
  const {product} = useLoaderData();
  return (
    <h1>{product.title}</h1>
  )
}

const PRODUCT_QUERY = `#graphql
  product(handle: $handle) {
    id
    title
  }`
```

TypeScript:

```tsx
import {useLoaderData} from '@remix-run/react';
import type { LoaderArgs } from '@shopify/remix-oxygen';
import type { Product } from '@shopify/hydrogen/storefront-api-types';

export async function loader({params, context}: LoaderArgs) {
  const {handle} = params;
  const {storefront} = context;
  const {product} = await storefront.query(PRODUCT_QUERY, {
    variables: {handle},
    // Pass a `cache` option with your query to customize API request caching.
    cache: storefront.CacheLong()
  });
  return {product};
}

export default function Product() {
  const {product} = useLoaderData<typeof loader>();
  return (
    <h1>{product.title}</h1>
  )
}

const PRODUCT_QUERY = `#graphql
  product(handle: $handle) {
    id
    title
  }
`
```

### Next steps

* Learn more about [caching Shopify API data with Hydrogen](https://shopify.dev/docs/storefronts/headless/hydrogen/caching)
* [Paginate your Hydrogen data queries](https://shopify.dev/docs/storefronts/headless/hydrogen/data-fetching/pagination) to work with large product collections
* Explore the Storefront API with Hydrogen's [built-in GraphiQL client](https://shopify.dev/docs/storefronts/headless/hydrogen/data-fetching/graphiql)

---

## Fetch third-party API data with Hydrogen

> Fonte: https://shopify.dev/docs/storefronts/headless/hydrogen/data-fetching/third-party

Hydrogen includes a built-in client and utilities for [fetching data](https://shopify.dev/docs/storefronts/headless/hydrogen/data-fetching) with Shopify's Storefront API and Customer Account API.

If you need to access data from third-party sources, then you can re-use these utilities and design patterns. By consistently using the same methods for data fetching regardless of the source, your app logic is simpler to understand, and your app will be more performant.

### What you'll build

In this guide, you'll use Hydrogen's built-in utilities to query the [GraphQL Rick and Morty API](https://rickandmortyapi.com/documentation/#graphql) and display a list of characters.

This simplified example shows how to re-use Hydrogen tools to create a new API client, add it to the Remix context, and query your data from any route.

### Step 1: Create a new third-party API client

The following example re-uses existing Hydrogen utilities to create an API client that handles caching with the same tooling and method that Hydrogen uses for Shopify API queries. This keeps data fetching and caching behaviors consistent across your app.

**Create a third-party API client — `/app/lib/createRickAndMortyClient.server.js`**

JavaScript:

```js
import {createWithCache, CacheLong} from '@shopify/hydrogen';

export function createRickAndMortyClient({
  cache,
  waitUntil,
  request,
}) {
  const withCache = createWithCache({cache, waitUntil, request});

  async function query(
    query,
    options = {variables: {}, cacheStrategy: CacheLong()},
  ) {
    const result = await withCache.fetch(
      'https://rickandmortyapi.com/graphql',
      {
        method: 'POST',
        headers: {
          'Content-type': 'application/json',
        },
        body: JSON.stringify({
          query,
          variables: options.variables,
        }),
      },
      {
        cacheKey: ['r&m', query, JSON.stringify(options.variables)],
        cacheStrategy: options.cacheStrategy,
        shouldCacheResponse: (body) =>
          body.error == null || body.error.length === 0,
      },
    );
    return result.data;
  }

  return {query};
}
```

TypeScript:

```ts
import {createWithCache, CacheLong, type CachingStrategy} from '@shopify/hydrogen';

export function createRickAndMortyClient({
  cache,
  waitUntil,
  request,
}: {
  cache: Cache;
  waitUntil: ExecutionContext['waitUntil'];
  request: Request;
}) {
  const withCache = createWithCache({cache, waitUntil, request});

  async function query<T = any>(
    query: `#graphql:rickAndMorty${string}`,
    options: {
      variables?: object;
      cacheStrategy?: CachingStrategy;
    } = {variables: {}, cacheStrategy: CacheLong()},
  ) {
    const result = await withCache.fetch<{data: T; error: string}>(
      'https://rickandmortyapi.com/graphql',
      {
        method: 'POST',
        headers: {
          'Content-type': 'application/json',
        },
        body: JSON.stringify({
          query,
          variables: options.variables,
        }),
      },
      {
        cacheKey: ['r&m', query, JSON.stringify(options.variables)],
        cacheStrategy: options.cacheStrategy,
        shouldCacheResponse: (body: {data: T; error: string}) =>
          body.error == null || body.error.length === 0,
      },
    );
    return result.data;
  }

  return {query};
}
```

### Step 2: Create the API client and pass to the Remix context

You can now add your API client to the app's context file so it's available to load data from your routes.

**Pass API client to Remix context — `/app/lib/context.js`**

JavaScript:

```js
// ...Existing context.js imports here...
import {createRickAndMortyClient} from './app/lib/createRickAndMortyClient.server';

export async function createAppLoadContext(
  request: Request,
  env: Env,
  executionContext: ExecutionContext,
) {
  // ... Existing context creation code here...

  // Create the Rick and Morty API Client
  const rickAndMorty = createRickAndMortyClient({
    cache,
    waitUntil,
    request,
  });

  return {
    ...hydrogenContext,
    rickAndMorty,
  };
};
```

TypeScript:

```ts
// ...Existing context.ts imports here...
import {createRickAndMortyClient} from './app/lib/createRickAndMortyClient.server';

export async function createAppLoadContext(
  request: Request,
  env: Env,
  executionContext: ExecutionContext,
) {
  // ... Existing context creation code here...

  // Create the Rick and Morty API Client
  const rickAndMorty = createRickAndMortyClient({
    cache,
    waitUntil,
    request,
  });

  return {
    ...hydrogenContext,
    rickAndMorty,
  };
};
```

### Step 3: Query and render the list of entries

You can now query your `rickAndMorty` API client from any loader function, on any route, using the same caching utilities that Hydrogen uses to query Shopify's Storefront API.

The following simplified example shows how to render an unordered list of character names on the `/characters` route:

**Render character index route — `/app/routes/characters._index.jsx`**

JSX:

```jsx
import {json} from '@shopify/remix-oxygen';
import {useLoaderData} from '@remix-run/react';
import {CacheShort} from '@shopify/hydrogen';

// Fetch and return API data with a Remix loader function
export async function loader({context}) {
  const {characters} = await context.rickAndMorty.query(CHARACTERS_QUERY, {
    cache: CacheShort(),
  });
  return json({characters});
}

// Render the component using data returned by the loader
export default function Characters() {
  const {characters} = useLoaderData();
  return (
    <div>
      <h1>Rick & Morty Characters</h1>
      <ul>
        {(characters.results || []).map((character) => (
          <li key={character.name}>{character.name}</li>
        ))}
      </ul>
    </div>
  );
}

// Query the API for a list of characters
const CHARACTERS_QUERY = `#graphql:rickAndMorty
  query {
    characters(page: 1) {
      results {
        name
        id
      }
    }
  }
`;
```

TSX:

```tsx
import {json, type LoaderFunctionArgs} from '@shopify/remix-oxygen';
import {useLoaderData} from '@remix-run/react';
import {CacheShort} from '@shopify/hydrogen';

// Fetch and return API data with a Remix loader function
export async function loader({context}: LoaderFunctionArgs) {
  const {characters} = await context.rickAndMorty.query(CHARACTERS_QUERY, {
    cache: CacheShort(),
  });
  return json({characters});
}

type Character = {
  name: string;
  id: string;
};

// Render the component using data returned by the loader
export default function Characters() {
  const {characters} = useLoaderData<typeof loader>();
  return (
    <div>
      <h1>Rick & Morty Characters</h1>
      <ul>
        {(characters.results || []).map((character: Character) => (
          <li key={character.name}>{character.name}</li>
        ))}
      </ul>
    </div>
  );
}

// Query the API for a list of characters
const CHARACTERS_QUERY = `#graphql:rickAndMorty
  query {
    characters(page: 1) {
      results {
        name
        id
      }
    }
  }
`;
```

Run `shopify hydrogen dev` to start the development server, then open http://localhost:3000/characters to verify that the query succeeded.

### Next steps

* Learn about [querying first-party Shopify APIs with Hydrogen](https://shopify.dev/docs/storefronts/headless/hydrogen/data-fetching)
* Learn more about [caching third-party API data](https://shopify.dev/docs/storefronts/headless/hydrogen/caching/third-party) with Hydrogen

---

## Pagination (Hydrogen data fetching)

> Fonte: https://shopify.dev/docs/storefronts/headless/hydrogen/data-fetching/pagination

The Storefront API limits how many items can be queried at once. This encourages better app performance by only querying what's immediately necessary to render the page.

However, sometimes you might have long lists of products, collections, or orders. Rather than rendering every item in the list, for better performance you should only render one page at a time. The Storefront API uses cursors to paginate through lists of data and the `Pagination` component enables you to render those pages.

It's important to maintain the pagination state in the URL for the following reasons:

* Users can navigate to a product and return back to the same scrolled position in a list.
* The list state is shareable by URL.
* Search engine crawlers are also able to index the pages when the pagination state is stored in the URL.

To set up pagination inside your app, do the following tasks:

### Setup the paginated query

First, set up a GraphQL query to the Storefront API to return paginated content. A query needs to have the arguments `first`, `last`, `startCursor`, and `endCursor`.

The query response needs to include `pageInfo` with `hasPreviousPage`, `hasNextPage`, `startCursor`, and `endCursor` passed to it.

**`app/route/products.jsx`**

```js
const PRODUCT_CARD_FRAGMENT = `#graphql
  fragment ProductCard on Product {
    id
    title
    publishedAt
    handle
    vendor
    variants(first: 1) {
      nodes {
        id
        image {
          url
          altText
          width
          height
        }
        price {
          amount
          currencyCode
        }
        compareAtPrice {
          amount
          currencyCode
        }
        selectedOptions {
          name
          value
        }
        product {
          handle
          title
        }
      }
    }
  }
`;


const ALL_PRODUCTS_QUERY = `#graphql
  query AllProducts(
    $first: Int
    $last: Int
    $startCursor: String
    $endCursor: String
  ) {
    products(first: $first, last: $last, before: $startCursor, after: $endCursor) {
      nodes {
        ...ProductCard
      }
      pageInfo {
        hasPreviousPage
        hasNextPage
        startCursor
        endCursor
      }
    }
  }
  ${PRODUCT_CARD_FRAGMENT}
`;
```

Hydrogen provides the utility `getPaginationVariables` to help calculate these variables from URL parameters. We recommend using the utility to pass the variables to the query within your loader:

**`app/route/products.jsx`**

```js
import {getPaginationVariables} from '@shopify/hydrogen';
import {json} from '@shopify/remix-oxygen';


export async function loader({context, request}) {
  const variables = getPaginationVariables(request, {
    pageBy: 4,
  });


  const {products} = await context.storefront.query(ALL_PRODUCTS_QUERY, {
    variables,
  });


  return json({
    products,
  });
}
```

### Render the `Pagination` component

Pass the entire query connection to the `Pagination` component. The component provides a `render` prop with all the nodes in the list. Map the nodes by product ID and render them.

> Nota di estrazione: nei blocchi JSX seguenti l'estrattore della pagina sorgente ha reso i tag `<Link>` come `<link ... />` auto-chiudenti, perdendo il testo figlio; sono riprodotti come catturati. Nel codice reale di Hydrogen questi sono componenti `<Link to={product.id}>{product.title}</Link>` di React Router.

**`app/route/products.jsx`**

```jsx
import { Pagination } from "@shopify/hydrogen";
import { useLoaderData, Link } from "@remix-run/react";


export default function () {
  const { products } = useLoaderData();


  return (
    <Pagination connection={products}>
      {({ nodes }) => {
        return nodes.map((product) => (
          <link key={product.id} to={product.id} />
            {product.title}
          
        ));
      }}
    </Pagination>
  );
}
```

The `Pagination` component's render prop provides convenience links to either load more or previous product pages from nodes:

**`app/route/products.jsx`**

```jsx
import { Pagination } from "@shopify/hydrogen";
import { useLoaderData, Link } from "@remix-run/react";


export default function () {
  const { products } = useLoaderData();


  return (
    <Pagination connection={products}>
      {({ nodes, NextLink, PreviousLink, isLoading  }) => (
        <>
          <PreviousLink>
            {isLoading ? "Loading..." : "Load previous products"}
          </PreviousLink>
          {nodes.map((product) => (
            <link key={product.id} to={product.id} />
              {product.title}
            
          ))}
          <NextLink>{isLoading ? "Loading..." : "Load next products"}</NextLink>
        
      )}
    </Pagination>
  );
}
```

### Complete pagination example

The following is a complete example of data fetching using pagination:

**`app/route/products.jsx`**

```jsx
import {getPaginationVariables, Pagination} from '@shopify/hydrogen';
import {useLoaderData, Link} from '@remix-run/react';
import {json} from '@shopify/remix-oxygen';


export async function loader({context, request}) {
  const variables = getPaginationVariables(request, {
    pageBy: 4,
  });


  const {products} = await context.storefront.query(ALL_PRODUCTS_QUERY, {
    variables,
  });


  return json({
    products,
  });
}


export default function () {
  const {products} = useLoaderData();


  return (
    <Pagination connection={products}>
      {({nodes, NextLink, PreviousLink, isLoading}) => (
        <>
          <PreviousLink>
            {isLoading ? 'Loading...' : 'Load previous products'}
          </PreviousLink>
          {nodes.map((product) => (
            <link key={product.id} to={product.id} />
              {product.title}
            
          ))}
          <NextLink>{isLoading ? 'Loading...' : 'Load next products'}</NextLink>
        
      )}
    </Pagination>
  );
}


const PRODUCT_CARD_FRAGMENT = `#graphql
  fragment ProductCard on Product {
    id
    title
    publishedAt
    handle
    vendor
    variants(first: 1) {
      nodes {
        id
        image {
          url
          altText
          width
          height
        }
        price {
          amount
          currencyCode
        }
        compareAtPrice {
          amount
          currencyCode
        }
        selectedOptions {
          name
          value
        }
        product {
          handle
          title
        }
      }
    }
  }
`;


const ALL_PRODUCTS_QUERY = `#graphql
  query AllProducts(
    $first: Int
    $last: Int
    $startCursor: String
    $endCursor: String
  ) {
    products(first: $first, last: $last, before: $startCursor, after: $endCursor) {
      nodes {
        ...ProductCard
      }
      pageInfo {
        hasPreviousPage
        hasNextPage
        startCursor
        endCursor
      }
    }
  }
  ${PRODUCT_CARD_FRAGMENT}
`;
```

### Automatically load pages on scroll

We can change the implementation to support loading subsequent pages on scroll. Add the dependency `react-intersection-observer` and use the following example:

**`app/route/products.jsx`**

```jsx
import { Pagination } from "@shopify/hydrogen";
import { useEffect } from "react";
import { useLoaderData, useNavigate } from "@remix-run/react";
import { useInView } from "react-intersection-observer";


export default function () {
  const { products } = useLoaderData();
  const { ref, inView, entry } = useInView();


  return (
    <Pagination connection={products}>
      {({ nodes, NextLink, hasNextPage, nextPageUrl, state }) => (
        <>
          <ProductsLoadedOnScroll
            nodes={nodes}
            inView={inView}
            hasNextPage={hasNextPage}
            nextPageUrl={nextPageUrl}
            state={state}
          />
          <NextLink ref={ref}>Load more</NextLink>
        
      )}
    </Pagination>
  );
}


function ProductsLoadedOnScroll({ nodes, inView, hasNextPage, nextPageUrl, state }) {
  const navigate = useNavigate();


  useEffect(() => {
    if (inView && hasNextPage) {
      navigate(nextPageUrl, {
        replace: true,
        preventScrollReset: true,
        state,
      });
    }
  }, [inView, navigate, state, nextPageUrl, hasNextPage]);


  return nodes.map((product) => (
    <link key={product.id} to={product.id} />
      {product.title}
    
  ));
}
```

---

## GraphiQL explorer (Hydrogen)

> Fonte: https://shopify.dev/docs/storefronts/headless/hydrogen/data-fetching/graphiql

For convenience, Hydrogen includes a local GraphiQL explorer to help you create queries and learn about Shopify's Storefront API.

### Requirements

Make sure you have the following environment variables in place:

* `PUBLIC_STORE_DOMAIN`
* `PUBLIC_STOREFRONT_API_VERSION`
* `PUBLIC_STOREFRONT_API_TOKEN`

### GraphiQL

The GraphiQL interface is available by default when running the Hydrogen CLI in development mode.

**Terminal**

npm:
```terminal
npx shopify hydrogen dev
```
Yarn:
```terminal
yarn shopify hydrogen dev
```
pnpm:
```terminal
pnpm shopify hydrogen dev
```

With the development server running, navigate to the `/graphiql` path on your local development server (such as `http://localhost:3000/graphiql`).

If you're not using the Hydrogen CLI, or want to customize the GraphiQL interface, you can do so by creating a `graphiql` route in your project:

**Optional route for GraphiQL — `<root>/app/routes/graphiql.jsx`**

JavaScript:

```jsx
import {graphiqlLoader} from '@shopify/hydrogen';
import {redirect} from '@shopify/remix-oxygen';

export async function loader(args) {
  if (process.env.NODE_ENV === 'development') {
    // Default Hydrogen GraphiQL behavior
    return graphiqlLoader(args);
  }

  return redirect('/');
}
```

TypeScript:

```tsx
import {graphiqlLoader} from '@shopify/hydrogen';
import {redirect, type LoaderArgs} from '@shopify/remix-oxygen';

export async function loader(args: LoaderArgs) {
  if (process.env.NODE_ENV === 'development') {
    // Default Hydrogen GraphiQL behavior
    return graphiqlLoader(args);
  }

  return redirect('/');
}
```

> **Note:** "If you're creating your own `graphiql` route, then make sure it's not available in production." You can use `process.env.NODE_ENV` to enforce tree-shaking.

---

## Performant Data Loading with Hydrogen

> Fonte: https://shopify.dev/docs/storefronts/headless/hydrogen/performance/data-loading

Performance starts with how you load data onto a page. Hydrogen gives you the ability to fetch data server-side, but if it's not done efficiently, then your store's [Time To First Byte](https://web.dev/articles/ttfb) (TTFB) can suffer. "TTFB is the time it takes for your website to start loading from when it's requested, until it first starts to show on your screen."

To better understand these requests that fetch data, Hydrogen ships with a tool called the [Subrequest Profiler](https://shopify.dev/docs/storefronts/headless/hydrogen/debugging/subrequest-profiler). This should be your first stop in diagnosing performance issues.

This document offers a set of best practices for Hydrogen merchants to support efficient data loading, improving the speed of storefronts and customer experience.

### Fetch Data in Parallel

It's common for pages to fetch data from more than one source. For example, your product page might fetch some product information from Shopify and additional content from a third party service such as a CMS.

When awaiting this data it's easy to end up with a "request waterfall", where each request is made one after another, causing an often avoidable delay. Where possible, it's faster to execute these requests simultaneously.

This can be achieved inside your data loaders using `Promise.all`:

```js
export async function loader({params, context}) {
  const {handle} = params;
  const {storefront, thirdPartyContent} = context;

  // Do this
  const [product, thirdPartyContent] = await Promise.all([
    // Both queries execute in parallel
    storefront.query(PRODUCT_QUERY, variables: {handle}),
    thirdPartyContent(),
  ]);

  // Not this
  const product = await storefront.query(PRODUCT_QUERY, variables: {handle});
  const thirdPartyContent = await thirdPartyContent(); // Starts after product query finishes
}
```

As a general rule, only critical data should be prioritized and awaited. For example, product information.

### Prioritize Critical Data

"The more data you need to start rendering a page, the longer your TTFB will be. A longer TTFB delays the page load, which negatively affects the user experience and potentially increases bounce rates."

Fortunately, with Hydrogen you can prioritize critical data and stream in any non-critical data later, which enables you to minimize your TTFB. Critical data is anything that you need before rendering the page, such as product information. Non-critical data is anything that can load after the page renders, such as reviews, or anything below the fold.

Defer non-critical data and stream the response so that the page can begin to render as soon as critical data is retrieved.

```js
export async function loader({params, context}) {
  const {handle} = params;
  const {storefront, fetchReviews} = context;

  // Do this
  const reviews = fetchReviews(handle); // Non-critical data can render whenever it finishes (important to make sure these are initiated before any awaited requests)
  const product = await storefront.query(PRODUCT_QUERY); // Page render awaits critical data
  return defer({product, reviews});

  // Not this
  const reviews = await fetchReviews(handle);
  const product = await storefront.query(PRODUCT_QUERY); // The critical data is delayed until after reviews finish loading!
  return json({product, reviews});
}
```

In order to render streamed data, you need to use `<Suspense>` from React and `<Await>` from React Router.

```jsx
export default function Product() {
  const { product, reviews } = useLoaderData();
  return (
    <>
      {/* Critical product data renders immediately */}
      <ProductDetails data={product} />
      {/* Non-critical review data displays fallback content until the data streams in */}
      <Suspense fallback={<ReviewsSkeleton />}>
        <Await resolve={reviews}>
          {(reviews) => <ProductReviews data={reviews} />}
        </Await>
      </Suspense>
    </>
  );
}
```

### Optimize the Loading Sequence

"The order of your requests in the loader matters. By initiating deferred (streamed) requests first, you can prevent them being blocked by critical (`await`ed) data. It might seem counterintuitive to start loading non-critical data first, but this ensures that all data loads in parallel."

```js
export async function loader({params, context}) {
  const {handle} = params;
  const {storefront, fetchReviews} = context;

  // Do this
  const reviews = fetchReviews(handle) // Loads in parallel with the product query
    .catch((error) => {
      // Log any errors, but don't throw them, so that the page can still render
      console.error(error);
      return null;
    });
  const product = await storefront.query(PRODUCT_QUERY);
  return defer({product, reviews});

  // Not this
  const product = await storefront.query(PRODUCT_QUERY);
  const reviews = fetchReviews(handle); // Blocked by the product query
  return defer({product, reviews});
}
```

### Eliminate Data Dependencies

It's important to keep in mind that the way third party data is modeled can have an impact on performance. Try to organize it in a way that allows you to perform multiple queries at the same time instead of one after the other. Take the following example where it's common to store and lookup data by product ID.

By using the product ID as the key, your product page first needs to look up the product ID from Shopify before it can fetch any information. This creates a request waterfall.

```js
// Storing data like this...
{
  [productId]: {
    some: "content..."
  }
}

// ...creates a waterfall because your second query has to wait on the product ID
const { product } = await storefront.query(PRODUCT_QUERY, variables: {handle});
const thirdPartyData = await 3PClient.query(3P_PRODUCT_QUERY, { productId: product.id });
```

In contrast, by storing the data by the product handle, you can fetch all data in parallel:

```js
// Storing data like this...
{
  [productHandle]: {
    some: "content..."
  }
}

// ...allows you to fetch all data at once (faster!)
const [{ product }, thirdPartyData] = await Promise.all([
  storefront.query(PRODUCT_QUERY, variables: {handle}),
  3PClient.query(3P_PRODUCT_QUERY, { handle }),
]);
```

### Separate Critical and Non-Critical Queries

"Larger queries are slower to execute. If a single query contains both critical and non-critical data, consider splitting it into multiple queries so you can defer the non-critical content."

A good example is found on the product page. A product query often fetches all of the product's variants up front, which can be a lot of data. By splitting it into two queries and deferring all of the possible variants, the product page can render more quickly, with the variant data streaming in after the initial page load. [See Hydrogen's Skeleton template for reference](https://github.com/Shopify/hydrogen/blob/main/templates/skeleton/app/routes/products.%24handle.tsx).

```js
export async function loader({params, context}) {
  const {handle} = params;
  const {storefront} = context;

  // Do this
  const variants = storefront.query(VARIANTS_QUERY, variables: {handle}); // Bigger, slower query
  const product = await storefront.query(PRODUCT_QUERY, variables: {handle}); // Smaller, faster query
  return defer({product, variants});

  // Not this
  const product = await storefront.query(PRODUCT_AND_VARIANTS_QUERY, variables: {handle}); // One big slow query
  return json({product});
}
```

Query splitting also provides more fine-grained control over your caching. Each query can use the best caching strategy for its data type.

### Do Not Over-Fetch

Fetching data that isn't used (aka over-fetching) increases response times and causes unnecessary processing.

The great part about GraphQL is you have the ability to request only the data you need for your page, so make sure that every field in your query is being used on your page—and if it's not, get rid of it!

```js
const CollectionCard = (collection) => {
  return (
    <div>
      <Image data={collection.image} />
      <h2>{collection.title}</h2>
    </div>
  );
};

// Do this
const COLLECTIONS = `#graphql
  query FeaturedCollections {
    collections(first:10) {
      nodes { # Only fetch the fields required to render the collection card
        id
        title
        image {
          id
          url
          altText
          width
        }
      }
    }
  }
`;

// Not this
const COLLECTIONS = `#graphql
  query FeaturedCollections {
    collections(first:3) {
      nodes {
        id
        title
        image {
          id
          url
          altText
          width
        }
        products(first:250) { # Collection card doesn't use products, this can be removed
          ...Product
        }
      }
    }
  }
`;
```

Review your loaders to ensure that you're only requesting resources that are actually required and your GraphQL queries only contain fields that are used.

### Leverage Caching

"Fetching data over the network takes time. You can eliminate this delay for future visitors by caching the response of each subrequest."

Think of caching as a last line of defense. After you have an efficient data loading strategy in place, supercharge the storefront by caching your subrequests. For data that changes regularly, adopt short-term caching. For stable data, implement longer-term caching strategies.

> **Caution:** Never cache personalized content, like carts. This can lead to a scenario where one user's data is mistakenly shown to another.

The Storefront API client built into Hydrogen includes the following [caching strategies](https://shopify.dev/docs/storefronts/headless/hydrogen/caching#caching-strategies):

```js
// Default caching strategy (suitable for most queries)
storefront.query(QUERY);

// No cache (e.g. personalized data)
storefront.query(QUERY, {cache: storefront.CacheNone()});

// Short caching strategy (e.g. product price)
storefront.query(QUERY, {cache: storefront.CacheShort()});

// Long caching strategy (e.g. shop name)
storefront.query(QUERY, {cache: storefront.CacheLong()});

// Custom caching strategy (e.g. third party CMS data)
storefront.query(QUERY, {cache: storefront.CacheCustom()});
```

For third party data, use Hydrogen's built-in [`withCache`](https://shopify.dev/docs/storefronts/headless/hydrogen/caching/third-party#hydrogen-s-built-in-withcache-utility) utility.

> **Info:** You can manually bust the cache by triggering an Oxygen redeploy.

---

## Caching Shopify API data with Hydrogen and Oxygen

> Fonte: https://shopify.dev/docs/storefronts/headless/hydrogen/caching

Hydrogen and Oxygen provide built-in caching to speed up Hydrogen storefronts. The caching API is based on the web-standard Cache-Control API.

By default, Hydrogen automatically caches [Storefront API](https://shopify.dev/docs/api/storefront) data when using Hydrogen's built-in API client. You can customize or disable caching behavior for every request. You can optionally extend Hydrogen's built-in utilities to [cache data from third-party APIs](https://shopify.dev/docs/storefronts/headless/hydrogen/caching/third-party).

Customer Account API data is never cached, because it's personalized for each user.

### Caching strategies

Hydrogen includes recommended caching strategies to help you determine which cache control header to set. The following table lists the available caching strategies and their associated cache control headers and cache durations:

| Caching strategy | Cache control header | Cache duration |
| --- | --- | --- |
| `CacheShort()` | `public, max-age=1, stale-while-revalidate=9` | 10 seconds |
| `CacheLong()` | `public, max-age=3600, stale-while-revalidate=82800` | 1 day |
| `CacheNone()` | `no-store` | No cache |
| `CacheCustom()` | Define your own cache control header | Custom |

#### Default caching strategy

By default, each sub-request applies a strategy with the following cache options, which revalidates data after one second and caches it for up to one day:

```txt
public, max-age=1, stale-while-revalidate=86399
```

### Subrequest caching

You can configure the caching strategy for Storefront API data by passing a `cache` option with your query.

The following simplified example shows a component that displays product titles. Because titles don't change often, it caches the data using the `CacheLong()` strategy.

**Caching product data with Hydrogen — `/app/routes/products/$productHandle.jsx`**

JavaScript:

```jsx
import {useLoaderData} from '@shopify/remix-oxygen';

export async function loader({params, context}) {
  const {handle} = params;
  const {storefront} = context;

  const {product} = await storefront.query(PRODUCT_QUERY, {
    variables: {handle},
    // Product titles change less often, so they can be cached with CacheLong().
    cache: storefront.CacheLong()
  });
  return {product};
}

export default function Product() {
  const {product} = useLoaderData();
  return (
    <h1>{product.title}</h1>
  )
}

const PRODUCT_QUERY = `#graphql
  product(handle: $handle) {
    id
    title
  }`
```

TypeScript:

```tsx
import {useLoaderData} from '@react-router';
import type { LoaderArgs } from '@shopify/remix-oxygen';
import type { Product } from '@shopify/hydrogen/storefront-api-types';

export async function loader({params, context}: LoaderArgs) {
  const {handle} = params;
  const {storefront} = context;

  const {product} = await storefront.query(PRODUCT_QUERY, {
    variables: {handle},
    // Product titles change less often, therefore CacheLong().
    cache: storefront.CacheLong()
  });
  return {product};
}

export default function Product() {
  const {product} = useLoaderData<typeof loader>();
  return (
    <h1>{product.title}</h1>
  )
}

const PRODUCT_QUERY = `#graphql
  product(handle: $handle) {
    id
    title
  }
`
```

### Prevent caching customer-specific data

Customer Account API data is automatically excluded from caching, but the Storefront API `customer` query also returns personalized data. Because the Storefront API client caches responses by default, you need to explicitly disable caching at both the subrequest and full-page levels to avoid leaking one customer's data to another.

#### Disable subrequest caching

Pass `CacheNone()` to the Storefront API query to prevent the customer data response from being stored in the subrequest cache:

**Disabling subrequest caching for customer data — `/app/routes/account.jsx`**

JavaScript:

```jsx
import {useLoaderData} from '@shopify/remix-oxygen';

export async function loader({context}) {
  const {storefront} = context;
  const {customer} = await storefront.query(CUSTOMER_QUERY, {
    variables: {
      customerAccessToken: context.session.get('customerAccessToken'),
    },
    cache: storefront.CacheNone(),
  });
  return {customer};
}

export default function Account() {
  const {customer} = useLoaderData();
  return <h1>Welcome, {customer.firstName}</h1>;
}

const CUSTOMER_QUERY = `#graphql
  query CustomerDetails($customerAccessToken: String!) {
    customer(customerAccessToken: $customerAccessToken) {
      firstName
      lastName
      email
    }
  }`;
```

TypeScript:

```tsx
import {useLoaderData} from '@shopify/remix-oxygen';
import type {LoaderArgs} from '@shopify/remix-oxygen';

export async function loader({context}: LoaderArgs) {
  const {storefront} = context;
  const {customer} = await storefront.query(CUSTOMER_QUERY, {
    variables: {
      customerAccessToken: context.session.get('customerAccessToken'),
    },
    cache: storefront.CacheNone(),
  });
  return {customer};
}

export default function Account() {
  const {customer} = useLoaderData<typeof loader>();
  return <h1>Welcome, {customer.firstName}</h1>;
}

const CUSTOMER_QUERY = `#graphql
  query CustomerDetails($customerAccessToken: String!) {
    customer(customerAccessToken: $customerAccessToken) {
      firstName
      lastName
      email
    }
  }`;
```

#### Disable full-page caching

Using `CacheNone()` on the subrequest prevents caching the API response, but Remix can still cache the rendered HTML response. To prevent shared caches and Oxygen's [full-page cache](https://shopify.dev/docs/storefronts/headless/hydrogen/caching/full-page-cache) from storing the page, set a `Cache-Control` header on the loader response. You can choose between two approaches depending on whether you want the browser to cache the response for the individual user:

* **`no-store`** — Disables all caching entirely. No cache, including the user's browser, stores the response. Use this when the data changes frequently or when you don't want any cached version to exist.
* **`private, max-age=<seconds>`** — Prevents shared caches (Oxygen, CDNs, proxies) from storing the response, but allows the user's own browser to cache it for the specified duration. Use this when you want to improve performance for the same user navigating back to the page without risking data leakage to other users.

> **Caution:** If you use a `public` `Cache-Control` header or omit the header entirely on routes that return customer-specific data, the rendered HTML page could be cached by shared caches and served to other users, exposing personal information such as names, emails, and order history.

### Custom caching strategies

If you don't want to use the caching strategies built into Hydrogen, then you can create your own with the `CacheCustom()` function. This function accepts options compatible with the Cache-Control API.

The following strategy directs clients to revalidate the cached data when it's no longer fresh, not to transform the data, and to consider it fresh for a maximum of 30 seconds:

**Example custom caching strategy**

JavaScript:

```js
storefront.CacheCustom({
  mode: 'must-revalidate, no-transform',
  maxAge: 30,
})
```

TypeScript:

```ts
storefront.CacheCustom({
  mode: 'must-revalidate, no-transform',
  maxAge: 30,
})
```

### Cache-Control API

Hydrogen and Oxygen caching strategies are compatible with the HTTP Header [`Cache-Control` API](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control), with a small number of exceptions.

The following options are available when creating a custom caching strategy with `CacheCustom()`:

| Option | Type | Description |
| --- | --- | --- |
| `mode` | String | One or more comma-separated directives for how caches should handle response data. Accepts `public`, `private`, `no-store`, `must-revalidate`, and `no-transform`. |
| `maxAge` | Number | The length of time, in seconds, to cache the response. |
| `staleWhileRevalidate` | Number | The length of time, in seconds, to serve a stale response while fetching a fresh one in the background. |
| `sMaxAge` | Number | The length of time, in seconds, that proxies or CDNs can store the response. |
| `staleIfError` | Number | The length of time, in seconds, for the browser to serve a cached response instead when it receives a 5xx error. Note that `staleIfError` is ignored when caching sub-requests. Instead, use `staleWhileRevalidate` to return stale data if errors are thrown during the revalidation period. |

#### Cache-Control API exceptions

The `no-cache` directive isn't supported by Oxygen because it instructs the browser not to use the cached data until the server returns a `304 (Not Modified)` status from server. However, Oxygen doesn't return the `304` response status code, so this directive has no effect.

---

## Caching third-party API data with Hydrogen and Oxygen

> Fonte: https://shopify.dev/docs/storefronts/headless/hydrogen/caching/third-party

> **Note:** This guide might not be compatible with features introduced in Hydrogen version 2025-05 and above. Check the latest [documentation](https://shopify.dev/docs/api/hydrogen) if you encounter any issues.

The API client built into Hydrogen includes [caching strategies for Storefront API data](https://shopify.dev/docs/storefronts/headless/hydrogen/caching). However, if you make `fetch` requests to third-party APIs in your Hydrogen app, then the following behavior occurs:

* HTTP GET responses are cached according to their response headers.
* POST requests aren't cached.

There are several ways to manage caching of third-party data with Hydrogen and Oxygen:

1. Hydrogen's built-in `withCache` utility (recommended)
2. Creating custom abstractions
3. Caching content manually

> **Note:** If you [host your Hydrogen app on another provider](https://shopify.dev/docs/storefronts/headless/hydrogen/deployments/self-hosting) instead of Oxygen, then caching might work differently. Consult your provider for details on its caching capabilities.

### Hydrogen's built-in withCache utility

Hydrogen includes a [`createWithCache`](https://shopify.dev/docs/api/hydrogen/latest/utilities/caching/createwithcache) utility to support caching third-party API calls. This utility wraps an arbitrary number of sub-requests under a single cache key.

#### Step 1: Create and inject the utility function

To start, create a `withCache` function in your project server file and pass it as part of the Remix context.

The following example shows how `withCache` works with Oxygen:

**Create the withCache utility — `/server.js`**

JavaScript:

```jsx
import {createStorefrontClient, createWithCache} from '@shopify/hydrogen';
import {createRequestHandler} from '@shopify/remix-oxygen';

export default {
  async fetch(request, env, executionContext) {
    const cache = await caches.open('hydrogen');
    const waitUntil = (promise) => executionContext.waitUntil(promise);

    const {storefront} = createStorefrontClient({
      cache,
      waitUntil,
      // ...
    });

    // Create withCache object
    const withCache = createWithCache({cache, waitUntil, request});

    const handleRequest = createRequestHandler({
      build: remixBuild,
      mode: process.env.NODE_ENV,
      // Pass withCache to the Remix context
      getLoadContext: () => ({storefront, withCache, waitUntil}),
    });

    return handleRequest(request);
  },
};
```

TypeScript:

```tsx
import {createStorefrontClient, createWithCache} from '@shopify/hydrogen';
import {createRequestHandler} from '@shopify/remix-oxygen';

export default {
  async fetch(request: Request, env: Env, executionContext: ExecutionContext) {
    const cache = await caches.open('hydrogen');
    const waitUntil = (promise: Promise<unknown>) => executionContext.waitUntil(promise);

    const {storefront} = createStorefrontClient({
      cache,
      waitUntil,
      // ...
    });

    // Create withCache object
    const withCache = createWithCache({cache, waitUntil, request});

    const handleRequest = createRequestHandler({
      build: remixBuild,
      mode: process.env.NODE_ENV,
      // Pass withCache to the Remix context
      getLoadContext: () => ({storefront, withCache, waitUntil}),
    });

    return handleRequest(request);
  },
};
```

Type declaration file:

```tsx
/**
 * For TypeScript projects, import Hydrogen's included `withCache` types
 * in the Remix context by adding them to your Remix type declaration file.
 */

import type {Storefront, WithCache} from '@shopify/hydrogen';

declare module '@shopify/remix-oxygen' {
  export interface AppLoadContext {
    storefront: Storefront;
    withCache: WithCache;
    waitUntil: (promise: Promise<unknown>) => void;
  }
}
```

#### Step 2: Call `withCache.fetch` in Remix loaders and actions

After you pass the utility function to the Remix context, `withCache` is available in all Remix loaders and actions.

In the following example, the `withCache.fetch` function wraps a standard `fetch` query to a third-party CMS:

**Cache a sub-request to a third-party API using withCache — `/app/routes/pages/example.jsx`**

JavaScript:

```jsx
const CMS_API_ENDPOINT = 'https://example-cms.com/api';

export async function loader({request, context}) {
  { storefront, withCache } = context;
  const query = `query { product { id } }`;

  /**
   *  The cache key is used to uniquely identify the stored value in cache.
   *  If caching data for logged-in users, then make sure to add something
   *  unique to the user in the cache key, such as their email address.
  */
  const cacheKey = [CMS_API_ENDPOINT, query];

  const {data} = await withCache.fetch(
    CMS_API_ENDPOINT, // URL to fetch
    { // Fetch options
      method: 'POST',
      body: JSON.stringify({query}),
      headers: {'Content-Type': 'application/json'},
    },
    { // Caching options
      cacheKey,
      cacheStrategy: storefront.CacheLong(),
      shouldCacheResponse: () => true, // withCache.fetch will only cache when response.ok
    },
  );

  return {idFromCMS: data.product.id};
}
```

TypeScript:

```tsx
import type {LoaderFunctionArgs} from '@shopify/remix-oxygen';

const CMS_API_ENDPOINT = 'https://example-cms.com/api';

export async function loader({request, context: {storefront, withCache}}: LoaderFunctionArgs) {
  const query = `query { product { id } }`;

  /**
   *  The cache key is used to uniquely identify the stored value in cache.
   *  If caching data for logged-in users, then make sure to add something
   *  unique to the user in the cache key, such as their email address.
  */
  const cacheKey = [CMS_API_ENDPOINT, query];

  const {data} = await withCache.fetch<{product: {id: string}}>(
    CMS_API_ENDPOINT, // URL to fetch
    { // Fetch options
      method: 'POST',
      body: JSON.stringify({query}),
      headers: {'Content-Type': 'application/json'},
    },
    { // Caching options
      cacheKey,
      cacheStrategy: storefront.CacheLong(),
      shouldCacheResponse: () => true, // withCache.fetch will only cache when response.ok
    },
  );

  return {idFromCMS: data!.product.id};
}
```

### Custom cache abstractions

Instead of using `withCache.fetch` directly in your routes, you can also create custom abstractions around it. For example, you can make your own CMS fetcher and inject it in the Remix context.

You can create as many abstractions as needed for your third-party APIs, and they will be available in Remix loaders and actions. For TypeScript projects, you should add types accordingly in the `remix.env.d.ts` file.

**Create a custom abstraction — `/server.js`**

JavaScript:

```jsx
import {createStorefrontClient, createWithCache} from '@shopify/hydrogen';
import {createRequestHandler} from '@shopify/remix-oxygen';

export default {
  async fetch(request, env, executionContext) {
    const cache = await caches.open('hydrogen');
    const waitUntil = (promise) => executionContext.waitUntil(promise);

    const {storefront} = createStorefrontClient({
      cache,
      waitUntil,
      // ...
    });

    const withCache = createWithCache({cache, waitUntil, request});

    const fetchMyCMS = (
      query: string,
      cacheStrategy = storefront.CacheLong(),
    ) => {
      const CMS_API_ENDPOINT = 'https://example-cms.com/api';
      const cacheKey = [CMS_API_ENDPOINT, query];

      return withCache.fetch(
        CMS_API_ENDPOINT,
        {
          method: 'POST',
          body: JSON.stringify({query}),
          headers: {'Content-Type': 'application/json'},
        },
        {
          cacheKey,
          cacheStrategy,
          // Cache if there are no data errors or specific data that make this result not suited for caching
          shouldCacheResponse: (result) =>
            !(result?.errors || result?.isLoggedIn),
        },
      );
    };

    const handleRequest = createRequestHandler({
      build: remixBuild,
      mode: process.env.NODE_ENV,
      getLoadContext: () => ({storefront, fetchMyCMS, waitUntil}),
    });

    return handleRequest(request);
  },
};
```

TypeScript:

```tsx
import {createStorefrontClient, createWithCache} from '@shopify/hydrogen';
import {createRequestHandler} from '@shopify/remix-oxygen';

export default {
  async fetch(request: Request, env: Env, executionContext: ExecutionContext) {
    const cache = await caches.open('hydrogen');
    const waitUntil = (promise: Promise<unknown>) => executionContext.waitUntil(promise);

    const {storefront} = createStorefrontClient({
      cache,
      waitUntil,
      // ...
    });

    const withCache = createWithCache({cache, waitUntil, request});

    const fetchMyCMS = <My3PDataResponse>(
      query: string,
      cacheStrategy = storefront.CacheLong(),
    ) => {
      const CMS_API_ENDPOINT = 'https://example-cms.com/api';
      const cacheKey = [CMS_API_ENDPOINT, query];

      return withCache.fetch<My3PDataResponse>(
        CMS_API_ENDPOINT,
        {
          method: 'POST',
          body: JSON.stringify({query}),
          headers: {'Content-Type': 'application/json'},
        },
        {
          cacheKey,
          cacheStrategy,
          // Cache if there are no data errors or specific data that make this result not suited for caching
          shouldCacheResponse: (result: My3PDataResponse) =>
            !(result?.errors || result?.isLoggedIn),
        },
      );
    };

    const handleRequest = createRequestHandler({
      build: remixBuild,
      mode: process.env.NODE_ENV,
      getLoadContext: () => ({storefront, fetchMyCMS, waitUntil}),
    });

    return handleRequest(request);
  },
};
```

Alternatively, if you need to include extra logic within the custom cache abstraction itself, there is `withCache.run`.

**Create a custom abstraction with withCache.run — `/server.js`**

JavaScript:

```jsx
import {createStorefrontClient, createWithCache} from '@shopify/hydrogen';
import {createRequestHandler} from '@shopify/remix-oxygen';

export default {
  async fetch(request, env, executionContext) {
    const cache = await caches.open('hydrogen');
    const waitUntil = (promise) => executionContext.waitUntil(promise);

    const {storefront} = createStorefrontClient({
      cache,
      waitUntil,
      // ...
    });

    const withCache = createWithCache({cache, waitUntil, request});

    const fetchMyCMS = (
      query: string,
      cacheStrategy = storefront.CacheLong(),
    ) => {
      const CMS_API_ENDPOINT = 'https://example-cms.com/api';
      const cacheKey = [CMS_API_ENDPOINT, query];

      return withCache.run(
        {
          cacheKey,
          cacheStrategy,
          // Cache if there are no data errors
          shouldCacheResult: (result) => result.errors.length === 0,
        },
        async () => {
          const response = await fetch(CMS_API_ENDPOINT, {
            method: 'POST',
            body: JSON.stringify({query}),
            headers: {'Content-Type': 'application/json'},
          });

          if (!response.ok) return {errors: ['Something went wrong']};

          const {product} = await response.json();

          return {id: product.id, errors: []};
        },
      );
    };

    const handleRequest = createRequestHandler({
      build: remixBuild,
      mode: process.env.NODE_ENV,
      getLoadContext: () => ({storefront, fetchMyCMS, waitUntil}),
    });

    return handleRequest(request);
  },
};
```

TypeScript:

```tsx
import {createStorefrontClient, createWithCache} from '@shopify/hydrogen';
import {createRequestHandler} from '@shopify/remix-oxygen';

export default {
  async fetch(request: Request, env: Env, executionContext: ExecutionContext) {
    const cache = await caches.open('hydrogen');
    const waitUntil = (promise: Promise<unknown>) => executionContext.waitUntil(promise);

    const {storefront} = createStorefrontClient({
      cache,
      waitUntil,
      // ...
    });

    const withCache = createWithCache({cache, waitUntil, request});

    const fetchMyCMS = <My3PDataResponse>(
      query: string,
      cacheStrategy = storefront.CacheLong(),
    ) => {
      const CMS_API_ENDPOINT = 'https://example-cms.com/api';
      const cacheKey = [CMS_API_ENDPOINT, query];

      return withCache.run<My3PDataResponse>(
        {
          cacheKey,
          cacheStrategy,
          // Cache if there are no data errors
          shouldCacheResult: (result: My3PDataResponse) => result.errors.length === 0,
        },
        async () => {
          const response = await fetch(CMS_API_ENDPOINT, {
            method: 'POST',
            body: JSON.stringify({query}),
            headers: {'Content-Type': 'application/json'},
          });

          if (!response.ok) return {errors: ['Something went wrong']};

          const {product} = await response.json<{product: {id: string}}>();

          return {id: product.id, errors: []};
        },
      );
    };

    const handleRequest = createRequestHandler({
      build: remixBuild,
      mode: process.env.NODE_ENV,
      getLoadContext: () => ({storefront, fetchMyCMS, waitUntil}),
    });

    return handleRequest(request);
  },
};
```

#### Overriding default caching behavior

By default, [`withCache.fetch`](https://shopify.dev/docs/api/hydrogen/latest/utilities/caching/createwithcache#createWithCache-returns) will cache successful fetches (i.e. those where `response.ok` is true), and [`withCache.run`](https://shopify.dev/docs/api/hydrogen/latest/utilities/caching/createwithcache#createWithCache-returns) will always cache the result. This may not always be desirable, for example a CMS query may technically respond with an `ok` status code, but the response data might still contain errors. In these cases, you can override the default caching behavior.

To override the default caching behavior for `withCache.fetch`, you need to use `shouldCacheResponse`, which takes 2 params: the response data, and the `Response` object itself:

**Custom cache behavior for withCache.fetch — `/server.js`**

JavaScript:

```jsx
withCache.fetch(
  CMS_API_ENDPOINT,
  {
    method: 'POST',
    body: JSON.stringify({query}),
    headers: {'Content-Type': 'application/json'},
  },
  {
    cacheKey,
    cacheStrategy,
    shouldCacheResponse: (result, response) =>
      response.status === 200 && !result.isLoggedIn,  // Do not cache if the buyer is in a logged in state
  },
);
```

TypeScript:

```tsx
withCache.fetch<My3PDataResponse>(
  CMS_API_ENDPOINT,
  {
    method: 'POST',
    body: JSON.stringify({query}),
    headers: {'Content-Type': 'application/json'},
  },
  {
    cacheKey,
    cacheStrategy,
    shouldCacheResponse: (result: My3PDataResponse, response: Response) =>
      response.status === 200 && !result.isLoggedIn,  // Do not cache if the buyer is in a logged in state
  },
);
```

To override the default caching behavior for `withCache.run`, you need to use `shouldCacheResult`, which only takes 1 param: the result of the inner function:

**Custom cache behavior for withCache.run — `/server.js`**

JavaScript:

```jsx
withCache.run(
  {
    cacheKey,
    cacheStrategy,
    shouldCacheResult: (result) => result.errors.length === 0,
  },
  async () => {
    ...
  },
);
```

TypeScript:

```tsx
withCache.run<My3PDataResponse>(
  {
    cacheKey,
    cacheStrategy,
    shouldCacheResult: (result: My3PDataResponse) => result.errors.length === 0,
  },
  async () => {
    ...
  },
);
```

### Manual caching

As an alternative to the `withCache` utility, you can also directly use the `cache` instance that's passed to the Storefront client and available in `storefront.cache`.

This cache instance follows the [Cache API](https://developer.mozilla.org/en-US/docs/Web/API/Cache). Using the cache instance directly is a low-level approach and you need to handle all the cases and features manually, including error handling and stale-while-revalidate.

The following example shows how to cache a request to a third-party API with Oxygen:

**Cache a sub-request to a third-party API using the cache instance — `/app/routes/pages/example.jsx`**

JavaScript:

```jsx
const CMS_API_ENDPOINT = 'https://my-cms.com/api';

export async function loader({request, context: {storefront, waitUntil}}) {
  const body = JSON.stringify(Object.fromEntries(new URL(request.url).searchParams.entries()));

  // Create a new request based on a unique key representing the API request.
  // This could use any unique URL that depends on the API request.
  // For example, it could concatenate its text body or its sha256 hash.
  const cacheUrl = new URL(CMS_API_ENDPOINT);
  cacheUrl.pathname = '/cache' + cacheUrl.pathname + generateUniqueKeyFrom(body);
  const cacheKey = new Request(cacheUrl.toString());

  // Check if there's a match for this key.
  let response = await storefront.cache.match(cacheKey);

  if (!response) {
    // Since there's no match, fetch a fresh response.
    response = await fetch(CMS_API_ENDPOINT, {body, method: 'POST'});
    // Make the response mutable.
    response = new Response(response.body, response);
    // Add caching headers to the response.
    response.headers.set('Cache-Control', 'public, max-age=10')
    // Store the response in cache to be re-used the next time.
    waitUntil(storefront.cache.put(cacheKey, response.clone()));
  }

  return response;
}
```

TypeScript:

```tsx
import type {LoaderArgs} from '@shopify/remix-oxygen';

const CMS_API_ENDPOINT = 'https://my-cms.com/api';

export async function loader({request, context: {storefront, waitUntil}}: LoaderArgs) {
  const body = JSON.stringify(Object.fromEntries(new URL(request.url).searchParams.entries()));

  // Create a new request based on a unique key representing the API request.
  // This could use any unique URL that depends on the API request.
  // For example, it could concatenate its text body or its sha256 hash.
  const cacheUrl = new URL(CMS_API_ENDPOINT);
  cacheUrl.pathname = '/cache' + cacheUrl.pathname + generateUniqueKeyFrom(body);
  const cacheKey = new Request(cacheUrl.toString());

  // Check if there's a match for this key.
  let response = await storefront.cache.match(cacheKey);

  if (!response) {
    // Since there's no match, fetch a fresh response.
    response = await fetch(CMS_API_ENDPOINT, {body, method: 'POST'});
    // Make the response mutable.
    response = new Response(response.body, response);
    // Add caching headers to the response.
    response.headers.set('Cache-Control', 'public, max-age=10')
    // Store the response in cache to be re-used the next time.
    waitUntil(storefront.cache.put(cacheKey, response.clone()));
  }

  return response;
}
```

---

## Oxygen Full-page cache

> Fonte: https://shopify.dev/docs/storefronts/headless/hydrogen/caching/full-page-cache

The full-page cache feature in Oxygen can reduce the time that's required to load page content for subsequent visits, because Oxygen can quickly serve the cached content instead of having to execute the Hydrogen storefront worker to generate a response. This results in a faster and more responsive user experience, which can lead to increased conversions.

This guide provides an introduction to the full-page cache feature, including its benefits and how it works.

### How it works

The full-page cache feature in Oxygen helps you optimize the performance of Hydrogen storefronts by caching the generated response from your Hydrogen storefront worker. This is typically an HTML page.

Full-page cache works by intercepting incoming requests and checking if a cached version of the requested content is available. This check for the cached version can have the following outcomes, depending on its state:

* If a cached version is found and it's not stale, then the cached content is served to the user. No request is made to the Hydrogen storefront worker.
* If a cached version is found and it is stale, then the cached content is served to the user. The Hydrogen storefront worker is executed in the background and Oxygen caches the response to be used for future requests.
* If a cached version isn't found, then the Hydrogen storefront worker is executed for that request, and Oxygen caches the response to be used for future requests.

#### Caching criteria

For Oxygen to consider a response from a Hydrogen storefront worker execution as cacheable, the response must meet the following criteria:

* Be a response to a `GET` request
* Have a `2XX` or `3XX` status code.
* Have a `public` `Oxygen-Cache-Control` header set with a non zero `max-age`, or `s-maxage`, value.
* Have a `Vary` header set with a value to indicate what requests can be served using the cached response.

> **Caution:** If a Hydrogen storefront worker's response was generated with server-side personalization, for example a serialized cart session, this might result in Oxygen serving a seemingly outdated cached response, or serving the same cart session to multiple users. It's your responsibility to ensure that pages opted into Oxygen's full-page cache can be served for requests with the same path, method, and request headers as specified by `Vary`. For routes that return customer-specific data, you must set appropriate `Cache-Control` headers to prevent personal data from being cached and served to other users. Learn how to [prevent caching customer-specific data](https://shopify.dev/docs/storefronts/headless/hydrogen/caching#prevent-caching-customer-specific-data).

##### `Oxygen-Cache-Control` response header

Full-page cache relies on the `Oxygen-Cache-Control` header that's returned in Hydrogen storefront worker responses to determine if a response can be cached and for how long.

Set the `Oxygen-Cache-Control` header to `public` for responses that can be cached, and include a `max-age` directive in the header to specify the maximum amount of time that the response can be cached. This header is sent in the client response.

The following table describes the supported `Oxygen-Cache-Control` response headers that you can use in Oxygen, and provides some examples of each header directive that can be used to control cache behavior:

| Header directive | Description | Example usage |
| - | - | - |
| `public` | Indicates that the response can be cached by any cache. | `Oxygen-Cache-Control: public` |
| `max-age` | Specifies the maximum amount of time, in seconds, that the response can be cached. | `Oxygen-Cache-Control: public, max-age=3600` |
| `s-maxage` | Specifies the maximum amount of time, in seconds, that the response can be cached by shared caches. | `Oxygen-Cache-Control: public, s-maxage=7200` |
| `stale-while-revalidate` | Indicates that the cache can serve stale content while it fetches a fresh version in the background. | `Oxygen-Cache-Control: public, max-age=3600, stale-while-revalidate=600` |

##### `Vary` response header

Oxygen uses the `Vary` response header to determine which incoming request headers should be used when looking for a cached response for the requested path.

When a Hydrogen storefront worker sets a `Vary` response header, Oxygen will respect it.

For example, if a Hydrogen storefront worker returns a `Vary: Accept-Encoding`, then Oxygen serves the same cached response for every incoming request for a particular path with the same `Accept-Encoding` request header value.

> **Note:** By default, Hydrogen storefront workers don't return a `Vary` response header. You need to decide what's best based on your implementation. A good default is `Accept-Encoding, Accept-Language`.

##### `Oxygen-Full-Page-Cache` client response header

The `Oxygen-Full-Page-Cache` header is an informational response header that's always returned by Oxygen to clients. It's used to help developers debug and understand the cache status of a response in a full-page cache implementation. The header has the following possible values, which each indicate a different cache status:

| Header value | Description |
| - | - |
| `Miss` | The requested resource wasn't found in the cache, and a new response was generated. This occurs when the cache doesn't have a matching entry for the requested path, and the response is generated by the Hydrogen storefront worker. |
| `Hit` | The requested resource was found in the cache, and the cached response is still up to date. This occurs when the cache has a matching entry for the requested path, and the response isn't stale according to the cache's `max-age`, which is specified in the `Oxygen-Cache-Control` response header. |
| `Stale` | The requested resource was found in the cache, but the cached response is stale. This occurs when the cache has a matching entry for the request, but the response is considered stale according to the cache's `max-age`, which is specified in the `Oxygen-Cache-Control` response header. In this case, the stale response is served, and a request is made to the Hydrogen storefront worker to asynchronously update the cache with a new response. |
| `Uncacheable` | The requested resource can't be cached by Oxygen. This occurs in the following scenarios: The request has a method other than `GET`. The response doesn't have an `Oxygen-Cache-Control` header. The response doesn't have a `public` directive specified in the `Oxygen-Cache-Control` header. The response doesn't have a `2XX` or `3XX` status code. The response has a `Set-Cookie` header. The response doesn't have a `Vary` header. The response has a `Vary: *` header. |

##### Limitations

Full-page cache is designed to work with Hydrogen storefront workers and has the following limitations:

* You can't purge Oxygen's full page cache for the currently deployed worker. You either need to wait for the cached response to expire, or make a new deployment of your Hydrogen storefront worker to start with a fresh cache.
* Oxygen won't be able to serve a cached response from a previous deployment on a new deployment.
* The headers specified for `Vary` will use those header(s) complete values. There is no way to use only specific cookies, for example.

---

## Search Engine Optimization for Hydrogen

> Fonte: https://shopify.dev/docs/storefronts/headless/hydrogen/seo

Optimizing Hydrogen for search engines and social media requires configuring the following things:

1. Meta tags and descriptions
2. `sitemap.xml`
3. `robots.txt`

This guide walks you through the process of setting up each one.

> **Note:** This isn't a comprehensive guide to SEO best practices. Check the Shopify blog for more resources on commerce SEO.

### Meta tags

Hydrogen uses Remix's built-in `meta` features for SEO tags, and includes the `getSeoMeta` utility, which makes it easier and more consistent to render SEO meta tags.

> **Note:** Check out the Remix docs on `meta` exports for more details.

The `getSeoMeta` utility accepts SEO metadata about the current route, then renders the corresponding HTML meta tags in your document `<head>`:

**getSeoMeta example input and output — `/app/routes/example.jsx`**

JSX input:

```jsx
export const meta = () => {
  return getSeoMeta({
    title: 'Example title',
  });
};
```

HTML output:

```html
<head>
  <!-- ... -->
  <title>Example title</title>
  <meta property="og:title" content="Example title" />
  <meta property="twitter:title" content="Example title" />
  <!-- ... -->
</head>
```

It includes support for titles, descriptions, images, canonical URLs, JSON-LD and more. Check the `getSeoMeta` reference for a complete list of supported features.

#### Step 1: Import `getSeoMeta` and use it in your `meta` exports

The SEO data you want will vary by route. For example, you'll want to render different tags on a product page versus the home page. The following example code shows how the basic pattern applies across all your storefront routes:

**Import and use getSeoMeta — `/app/routes/root.jsx`**

JavaScript:

```jsx
import {getSeoMeta} from '@shopify/hydrogen';
// ...
export async function loader() {
   return {
     //...
     // Return an SEO object in your loader data
     seo: {
       title: "Storefront name",
       description: "Storefront description, including relevant keywords to help new customers find your page",
     },
   };
 }

// Pass the loader data to the meta export
export const meta = ({data}) => {
  // pass your SEO object to getSeoMeta()
  return getSeoMeta(data.seo);
};
```

TypeScript:

```tsx
import {getSeoMeta} from '@shopify/hydrogen';
import {type MetaFunction} from '@react-router';
// ...
export async function loader({context}: LoaderFunctionArgs) {
   return {
     //...
     // Return an SEO object in your loader data
     seo: {
       title: "Storefront name",
       description: "Storefront description, including relevant keywords to help new customers find your page",
     },
   };
 }

// Pass the loader data to the meta export
export const meta: MetaFunction<typeof loader> = ({data}) => {
  // pass your SEO object to getSeoMeta()
  return getSeoMeta(data.seo);
};
```

#### Step 2: Merge SEO data from nested routes

Often, two or more nested routes are returning SEO data. In general, you'll want to use the most specific SEO tags available for your route.

For example, if you're on the product page, you want to show a title and description of your product, not the store name and description from the root route.

The following code examples show how to return SEO data from a nested product route, then merge it with SEO data from the root route. By mapping over SEO data returned by all nested routes, the most specific SEO data "wins", overwriting SEO data from higher in the routing structure:

**Merge SEO data from nested routes — Root route (`/app/routes/root.jsx`)**

```jsx
import {getSeoMeta} from '@shopify/hydrogen';
// ...
export async function loader({context}) {
   return {
     //...
     // Return basic shop SEO data
     seo: {
       title: "Storefront name",
       description: "Storefront description, including relevant keywords to help new customers find your page",
     },
   };
 }

export const meta = ({data}) => {
  // Pass your SEO object to getSeoMeta()
  return getSeoMeta(data.seo);
};

// Switch to the "Product handle route" to see how these relate
```

Product handle route:

```jsx
import {getSeoMeta} from '@shopify/hydrogen';
// ...
export async function loader({context}) {
   const {product} = await context.storefront.query(/* GraphQL query */);
   return {
     //...
     // Return product SEO data
     seo: {
       title: product.seo.title || product.title,
       description: product.seo.description || product.description,
       // ...this could also include image URLs, prices, and more
     },
   };
 }

/// Pass all product loader data to the meta export
export const meta = ({matches}) => {
  // Map data from all routes. More specific SEO data from nested routes
  // overrides more general SEO data from parent routes.
  return getSeoMeta(...matches.map((match) => match.data.seo));
};
```

#### Step 3 (Optional): Intercept and override route SEO data

You can implement your own logic inside `meta` exports to customize the SEO metadata that each route returns.

As an example, by default Hydrogen removes query parameters from canonical URLs. If you wanted to add them back, the following is an example of how you could do that:

**Override SEO data with custom logic — `/app/routes/root.jsx`**

JavaScript:

```jsx
import {getSeoMeta} from '@shopify/hydrogen';
// ...
export const meta = ({data, location}) => {
  return getSeoMeta(data.seo).map((meta) => {
    if (meta.rel === 'canonical') {
      return {
        ...meta,
        // Overwrite the default value of meta.href to append the URL params
        href: meta.href + location.search,
      };
    }
    return meta;
  });
};
```

TypeScript:

```tsx
import {getSeoMeta} from '@shopify/hydrogen';
import {type MetaFunction} from '@react-router';
// ...
export const meta: MetaFunction<typeof loader> = ({data, location}) => {
  return getSeoMeta(data.seo).map((meta) => {
    if (meta.rel === 'canonical') {
      return {
        ...meta,
        // Overwrite the default value of meta.href to append the URL params
        href: meta.href + location.search,
      };
    }
    return meta;
  });
};
```

### sitemap.xml

Hydrogen's base template includes `sitemap.xml` and `sitemap.$type.$page.xml` routes by default. If your project doesn't already have these files, then you can generate them with the following Shopify CLI command:

```sh
npx shopify hydrogen generate route sitemap
```

By default, the sitemap files are cached for 24 hours.

#### Limitations

* When you add or remove pages, the sitemap is automatically updated within one day. Similarly, if you unpublish a product, then the product is removed automatically from the sitemap.

### robots.txt

Hydrogen's base template includes a `robots.txt` route by default. If your project doesn't already have a `robots.txt` file, you can generate a new one with the Hydrogen CLI:

```sh
npx shopify hydrogen generate route robots
```

By default, Hydrogen's `robots.txt` file is cached for 24 hours.

#### robots.txt on Oxygen

If you deploy to Oxygen, then your `robots.txt` file is only served in your public production environment, and only if you have a custom domain set.

If you make a non-production deployment accessible with a shareable link or an auth bypass token, then Oxygen overrides the deployment's `robots.txt` file with a `disallow` rule for all bots and crawlers. This prevents exposing content prematurely, as well as potential SEO harm from duplicated content.

### Next steps

[Track analytics with Hydrogen](https://shopify.dev/docs/storefronts/headless/hydrogen/analytics) — Implement analytics for your Hydrogen project, with Shopify and third-party services.

---

## Analytics Event Tracking with Hydrogen

> Fonte: https://shopify.dev/docs/storefronts/headless/hydrogen/analytics/tracking

Learn how to implement analytics events in your Hydrogen project and send tracked events to Shopify analytics and, optionally, third-party services.

> **Tip:** Hydrogen includes analytics by default as of version 2024.4.3. You only need to do these tasks if you're upgrading an older version.

### Requirements

* [Hydrogen channel installed](https://apps.shopify.com/hydrogen)
* [Complete "Getting started with Hydrogen and Oxygen"](https://shopify.dev/docs/storefronts/headless/hydrogen/getting-started)
* [Configure Customer Privacy API settings](https://shopify.dev/docs/storefronts/headless/hydrogen/analytics/consent)

### Project setup: update `root.jsx`

To start sending analytics events, you set up the `Analytics` component in your Hydrogen project's root route. The high-level steps are:

1. Import the `Analytics` component and the `getShopAnalytics` utility from Hydrogen. The `Analytics` component automatically checks for [consent](https://shopify.dev/docs/storefronts/headless/hydrogen/analytics/consent) before collecting any event data.
2. Update the root loader to destructure the `env` object from the Hydrogen context.
3. Return the `shop` object by calling the `getShopAnalytics` utility — this function automatically collects the credentials required to send analytics events to Shopify.
4. Return the `consent` object with its required values. If you're using Shopify's cookie banner, then make sure `withPrivacyBanner` is set to `true`.
5. Update the root component to wrap your Hydrogen app with the `Analytics.Provider` component.

> **Caution:** If you haven't [configured consent](https://shopify.dev/docs/storefronts/headless/hydrogen/analytics/consent) through the Customer Privacy API, then analytics events won't fire and no data is tracked.

The imports needed at the top of `/app/root.jsx`:

```jsx
import {
  useNonce,
  getShopAnalytics,
  Analytics,
} from '@shopify/hydrogen';
import {
  Links,
  Meta,
  Outlet,
  Scripts,
  useRouteError,
  useRouteLoaderData,
  ScrollRestoration,
  isRouteErrorResponse,
} from 'react-router';
import favicon from '~/assets/favicon.svg';
import resetStyles from '~/styles/reset.css?url';
import appStyles from '~/styles/app.css?url';
import {PageLayout} from '~/components/PageLayout';
import {FOOTER_QUERY, HEADER_QUERY} from '~/lib/fragments';

import {ThirdPartyAnalyticsIntegration} from '~/components/ThirdPartyAnalyticsIntegration';

/**
 * This is important to avoid re-fetching root queries on sub-navigations
 * @type {ShouldRevalidateFunction}
 */
export const shouldRevalidate = ({
  formMethod,
  currentUrl,
  nextUrl,
}) => {
  // revalidate when a mutation is performed e.g add to cart, login...
  if (formMethod && formMethod !== 'GET') return true;

  // revalidate when manually revalidating via useRevalidator
```

> Nota di estrazione: la pagina sorgente è una guida interattiva passo-passo in cui ogni passaggio mostra lo stesso file `root.jsx` con una modifica evidenziata; l'estrattore ha riprodotto ripetutamente solo l'intestazione del file. I passaggi sostanziali sono elencati sopra; `getShopAnalytics` ([reference](https://shopify.dev/docs/api/hydrogen/current/utilities/getshopanalytics)) restituisce l'oggetto `shop`, e l'app va avvolta in `<Analytics.Provider>`.

### Update routes with analytics subcomponents

To track page views, add pageview components to each route you want to track. Each route type has its own preset analytics subcomponent that takes a `data` prop:

* Product details page: `Analytics.ProductView` ([reference](https://shopify.dev/docs/api/hydrogen/current/components/analytics/analytics-productview))
* Collections: `Analytics.CollectionView` ([reference](https://shopify.dev/docs/api/hydrogen/current/components/analytics/analytics-collectionview))
* Search results: `Analytics.SearchView` ([reference](https://shopify.dev/docs/api/hydrogen/current/components/analytics/analytics-searchview))
* Cart: `Analytics.CartView` ([reference](https://shopify.dev/docs/api/hydrogen/current/components/analytics/analytics-cartview))

**Product details page — `/app/routes/products.$handle.jsx` (imports + add `<Analytics.ProductView data={...} />`)**

```jsx
import {useLoaderData} from 'react-router';
import {
  getSelectedProductOptions,
  Analytics,
  useOptimisticVariant,
  getProductOptions,
  getAdjacentAndFirstAvailableVariants,
  useSelectedOptionInUrlParam,
} from '@shopify/hydrogen';
import {getVariantUrl} from '~/lib/variants';
import {ProductPrice} from '~/components/ProductPrice';
import {ProductImage} from '~/components/ProductImage';
import {ProductForm} from '~/components/ProductForm';

/**
 * @type {MetaFunction<typeof loader>}
 */
export const meta = ({data}) => {
  return [{title: `Hydrogen | ${data?.product.title ?? ''}`}];
};

/**
 * @param {LoaderFunctionArgs} args
 */
export async function loader(args) {
  // Start fetching non-critical data without blocking time to first byte
  const deferredData = loadDeferredData(args);

  // Await the critical data required to render initial state of the page
  const criticalData = await loadCriticalData(args);

  return {...deferredData, ...criticalData};
}
```

**Collections — `/app/routes/collections.$handle.jsx` (imports + `<Analytics.CollectionView data={...} />`)**

```jsx
import {redirect, useLoaderData, Link} from 'react-router';
import {
  getPaginationVariables,
  Image,
  Money,
  Analytics,
} from '@shopify/hydrogen';
import {useVariantUrl} from '~/lib/variants';
import {PaginatedResourceSection} from '~/components/PaginatedResourceSection';

/**
 * @type {MetaFunction<typeof loader>}
 */
export const meta = ({data}) => {
  return [{title: `Hydrogen | ${data?.collection.title ?? ''} Collection`}];
};

/**
 * @param {LoaderFunctionArgs} args
 */
export async function loader(args) {
  const deferredData = loadDeferredData(args);
  const criticalData = await loadCriticalData(args);
  return {...deferredData, ...criticalData};
}
```

**Search — `/app/routes/search.jsx` (imports + `<Analytics.SearchView />`)**

```jsx
import {useLoaderData} from 'react-router';
import {getPaginationVariables, Analytics} from '@shopify/hydrogen';
import {SearchForm} from '~/components/SearchForm';
import {SearchResults} from '~/components/SearchResults';
import {getEmptyPredictiveSearchResult} from '~/lib/search';

export const meta = () => {
  return [{title: `Hydrogen | Search`}];
};

export async function loader({request, context}) {
  const url = new URL(request.url);
  const isPredictive = url.searchParams.has('predictive');
  const searchPromise = isPredictive
    ? predictiveSearch({request, context})
    : regularSearch({request, context});

  searchPromise.catch((error) => {
    console.error(error);
    return {term: '', result: null, error: error.message};
  });

  return await searchPromise;
}
```

**Cart — `/app/routes/cart.jsx` (complete example with `<Analytics.CartView />`)**

```jsx
import {useLoaderData, data} from 'react-router';
import {CartForm, Analytics} from '@shopify/hydrogen';
import {CartMain} from '~/components/CartMain';

export const meta = () => {
  return [{title: `Hydrogen | Cart`}];
};

export const headers = ({actionHeaders}) => actionHeaders;

export async function action({request, context}) {
  const {cart} = context;

  const formData = await request.formData();

  const {action, inputs} = CartForm.getFormInput(formData);

  if (!action) {
    throw new Error('No action provided');
  }

  let status = 200;
  let result;

  switch (action) {
    case CartForm.ACTIONS.LinesAdd:
      result = await cart.addLines(inputs.lines);
      break;
    case CartForm.ACTIONS.LinesUpdate:
      result = await cart.updateLines(inputs.lines);
      break;
    case CartForm.ACTIONS.LinesRemove:
      result = await cart.removeLines(inputs.lineIds);
      break;
    case CartForm.ACTIONS.DiscountCodesUpdate: {
      const formDiscountCode = inputs.discountCode;
      const discountCodes = formDiscountCode ? [formDiscountCode] : [];
      discountCodes.push(...inputs.discountCodes);
      result = await cart.updateDiscountCodes(discountCodes);
      break;
    }
    case CartForm.ACTIONS.GiftCardCodesUpdate: {
      const formGiftCardCode = inputs.giftCardCode;
      const giftCardCodes = formGiftCardCode ? [formGiftCardCode] : [];
      giftCardCodes.push(...inputs.giftCardCodes);
      result = await cart.updateGiftCardCodes(giftCardCodes);
      break;
    }
    case CartForm.ACTIONS.BuyerIdentityUpdate: {
      result = await cart.updateBuyerIdentity({
        ...inputs.buyerIdentity,
      });
      break;
    }
    default:
      throw new Error(`${action} cart action is not defined`);
  }

  const cartId = result?.cart?.id;
  const headers = cartId ? cart.setCartId(result.cart.id) : new Headers();
  const {cart: cartResult, errors, warnings} = result;

  const redirectTo = formData.get('redirectTo') ?? null;
  if (typeof redirectTo === 'string') {
    status = 303;
    headers.set('Location', redirectTo);
  }

  return data(
    {
      cart: cartResult,
      errors,
      warnings,
      analytics: {
        cartId,
      },
    },
    {status, headers},
  );
}

export async function loader({context}) {
  const {cart} = context;
  return await cart.get();
}

export default function Cart() {
  const cart = useLoaderData();

  return (
    <div className="cart">
      <h1>Cart</h1>
      <CartMain layout="page" cart={cart} />
      <Analytics.CartView />
    </div>
  );
}
```

If your cart is a side panel, you can publish the `cart_viewed` event with `useAnalytics` from your header component (`/app/components/Header.jsx`), importing `useAnalytics` and `useOptimisticCart` from `@shopify/hydrogen`.

If you get the following error message in your browser console, make sure your cart query includes the `updatedAt` field:

```
[h2:error:CartAnalytics] Can't set up cart analytics events because the `cart.updatedAt` value is missing from your GraphQL cart query. In standard Hydrogen projects, the cart query is contained in `app/lib/fragments.js`. Make sure it includes `cart.updatedAt`.
```

The cart query fragment lives in `/app/lib/fragments.js`:

```javascript
// NOTE: https://shopify.dev/docs/api/storefront/latest/queries/cart
export const CART_QUERY_FRAGMENT = `#graphql
  fragment Money on MoneyV2 {
    currencyCode
    amount
  }
  fragment CartLine on CartLine {
    id
    quantity
    attributes {
      key
      value
    }
    cost {
      totalAmount {
        ...Money
      }
      amountPerQuantity {
        ...Money
      }
      compareAtAmountPerQuantity {
        ...Money
      }
    }
    merchandise {
      ... on ProductVariant {
        id
        availableForSale
        compareAtPrice {
          ...Money
        }
        price {
          ...Money
        }
        requiresShipping
        title
        # ... (fragment continues; ensure cart.updatedAt is included in the cart query)
```

### Optional: Implement Custom Analytics with Third-Party Services

Using the `Analytics.Provider` component, you can create your own subcomponents to send events to third-party analytics services, in addition to Shopify. In your custom component, import the `useAnalytics` hook from Hydrogen, `register` the integration, `subscribe` to events, and call `ready()` when set up. See the [Web Pixels API standard events](https://shopify.dev/docs/api/web-pixels-api/standard-events) reference for the full event list.

**`/app/components/ThirdPartyAnalyticsIntegration.jsx`**

```jsx
import {useAnalytics} from '@shopify/hydrogen';
import {useEffect} from 'react';

export function ThirdPartyAnalyticsIntegration() {
  const {subscribe, register} = useAnalytics();
  // Register this analytics integration - this will prevent any analytics events
  // from being sent until this integration is ready
  const {ready} = register('Third Party Analytics Integration');

  useEffect(() => {
    // Standard events
    subscribe('page_viewed', (data) => {
      console.log('ThirdPartyAnalyticsIntegration - Page viewed:', data);
    });
    subscribe('product_viewed', (data) => {
      console.log('ThirdPartyAnalyticsIntegration - Product viewed:', data);
    });
    subscribe('collection_viewed', (data) => {
      console.log('ThirdPartyAnalyticsIntegration - Collection viewed:', data);
    });
    subscribe('cart_viewed', (data) => {
      console.log('ThirdPartyAnalyticsIntegration - Cart viewed:', data);
    });
    subscribe('cart_updated', (data) => {
      console.log('ThirdPartyAnalyticsIntegration - Cart updated:', data);
    });

    // Custom events
    subscribe('custom_checkbox_toggled', (data) => {
      console.log(
        'ThirdPartyAnalyticsIntegration - Custom checkbox toggled:',
        data,
      );
    });

    // Mark this analytics integration as ready as soon as it's done setting up
    ready();
  }, []);

  return null;
}
```

Once you've created your custom analytics component, import it into your root route and add it as a child of `<Analytics.Provider>` (so it can subscribe to events and receive analytics data).

### Next Steps

[Validate and troubleshoot Hydrogen analytics](https://shopify.dev/docs/storefronts/headless/hydrogen/analytics/validation) — Test that your analytics are working and check for common errors.

---

## Internationalization with Shopify Markets

> Fonte: https://shopify.dev/docs/storefronts/headless/hydrogen/markets

### Introduction

Shopify Markets enables merchants to expand globally by creating localized shopping experiences in different languages and currencies. Hydrogen provides React Router-based patterns for internationalization (i18n) that integrate with a merchant's market configuration and make locales available throughout the application and Storefront API queries.

### Requirements

* Completion of the Hydrogen Getting Started guide with a Hello World example
* Store regions and languages configured using Shopify Markets
* Familiarity with using the Storefront API with Shopify Markets

### Setup the default locale

Before configuring your Hydrogen Storefront, establish a default `language` and `country code` to ensure proper language and currency usage throughout the app. This guide explains how to add or update the default language for your custom storefront.

[Setup the default locale](https://shopify.dev/docs/storefronts/headless/hydrogen/markets/default-locale)

### Setup a multi-region and multilingual storefront

For storefronts supporting multiple regions and languages, Shopify recommends using separate URLs for each locale to improve search engine and screen reader accessibility. Two methods are available:

| Option | URL examples |
| --- | --- |
| Localization scheme using URL paths | `hydrogen.shop/fr`, `hydrogen.shop/es` |
| Localization scheme using domains and subdomains | `hydrogen.fr`, `hydrogen.es` |

The URL paths method requires only app-level configuration without domain infrastructure setup.

[Setup i18n with URL paths](https://shopify.dev/docs/storefronts/headless/hydrogen/markets/multiple-languages-url-paths)

[Setup i18n with domains and subdomains](https://shopify.dev/docs/storefronts/headless/hydrogen/markets/multiple-languages-domains)

### Create a country selector

Users benefit from being able to switch storefronts to their preferred country. Providing this functionality enhances user experience.

[How to setup a country selector](https://shopify.dev/docs/storefronts/headless/hydrogen/markets/country-selector)

### Localization detection using headers, cookies, or URL search params

While locale approximation is possible through headers, cookies, or URL parameters, Shopify recommends this approach only for enhancing user experience. A suitable example involves displaying a banner asking users to confirm their country preference. Conversely, automatic redirection represents poor implementation.

This approach has limitations: "page caching ignores locale cookies, headers and URL search params. SEO bots tend to origin from the US, don't have cookies and will not change their `accept-language` headers."

[Learn how to setup localization detection using headers, cookies or URL search params](https://shopify.dev/docs/storefronts/headless/hydrogen/markets/locale-detection)

### Developer tools and resources

[Shopify Markets](https://help.shopify.com/en/manual/markets)

### Next steps

* Set up default locale for your storefront
* Set up multiregion and multilingual storefronts with URL paths
* Set up multiregion and multilingual storefronts with domains and subdomains
* Create a country selector for user preference selection
* Set up locale detection using response headers, cookies, or URL search parameters

---

## Migrate from the online store to Hydrogen

> Fonte: https://shopify.dev/docs/storefronts/headless/hydrogen/migrate

This guide outlines considerations when migrating from the online store to Hydrogen.

### Shared carts

Online store carts are compatible with the Storefront API and vice versa, making it possible to share carts between channels.

Both Liquid and Hydrogen cart IDs are stored in a `cart` cookie, which prevents customers from losing carts when migrating to or from Hydrogen.

> **Warning:** In order for shared carts to work, the same products must be published to both the Online Store channel and your Hydrogen storefront.

### Subdomain for checkout

Regardless of whether you're using the online store or Hydrogen, customers are always directed back to a Shopify-hosted checkout. Traditionally, a checkout URL might look something like `{shop}.myshopify.com/123456/checkouts…`.

To make sure your Hydrogen site works correctly, assign a subdomain for your storefront to checkout. For example, if your Hydrogen store is `example.com`, then assign `checkout.example.com` to checkout. To do this:

1. [Connect the subdomain](https://help.shopify.com/en/manual/domains/add-a-domain/connecting-domains/connect-subdomain)
2. Set the **Target** to **Online Store**.
3. Set the **Domain** type to **Primary**.

### Configure routing

When you're migrating from Themes to Headless, you can define your own routes. For example, you might set the route that your cart is on at `example.com/bag` instead of `example.com/cart`.

To make sure that backlinks continue to work correctly, make sure you set up redirects for any customized routes.

The following is an example of setting up a redirect from `/cart`:

**`/app/routes/cart.jsx`**

```jsx
// Catch `/cart` and redirect to `/bag`
import {redirect} from '@shopify/remix-oxygen';


export function loader() {
  return redirect('/bag');
}
```

### Online store redirects and canonical links

To make sure any backlinks, such as from integrations, send traffic to your Hydrogen storefront and not your Liquid-based Online Store, be sure to set up redirects to take customers to your Hydrogen storefront.

For more information, refer to the [redirect traffic](https://shopify.dev/docs/storefronts/headless/hydrogen/migrate/redirect-traffic) doc.

### Product feeds

If you use Shopify's out-of-the-box product feeds, then you'll need to set up feed rules (for example, Facebook and Google) to use your Hydrogen storefront's domain.

### Password protection

Online store password protection prevents Hydrogen checkouts. To remove password protection, do the following:

1. From the Shopify admin, under **Sales channels**, click **Online Store** > **Preferences**.
2. In the **Restrict store access** section, deselect **Restrict access to visitors with the password**.
3. Click **Save**.

### Notifications

You can update notifications to use the same domain as your Hydrogen storefront.

1. From the Shopify admin, click **Settings** > **Notifications**.
2. Update the **Notification URLs** setting.

### Next Steps

* [Go live with Hydrogen](https://shopify.dev/docs/storefronts/headless/hydrogen/production-checklist#go-live-guide) for merchants ready to publish their new Hydrogen storefront.

---

## Set the default locale (Markets)

> Fonte: https://shopify.dev/docs/storefronts/headless/hydrogen/markets/default-locale

[Internationalization with Shopify Markets](https://shopify.dev/docs/storefronts/headless/hydrogen/markets) helps merchants expand their business to a global audience by creating shopping experiences in local languages and currencies.

Each Hydrogen app should have a default `language` and `country` in order to receive the correct language and currency for your storefront.

This guide shows you how to add or update your custom storefront's default language.

### Requirements

* You've completed the Hydrogen getting started with a `Hello World` example project.
* You can make queries to the Storefront API.
* You've setup your store's regions and languages using Shopify Markets.

### Step 1: Set the default language and country

In `server.js`, when creating the Hydrogen's storefront client, set the values for `i18n`'s `language` and `country`, using the Storefront API's supported [language](https://shopify.dev/docs/api/storefront/latest/enums/LanguageCode) and [country](https://shopify.dev/docs/api/storefront/latest/enums/CountryCode) codes.

This ensures that the default `country` and `language` are available as context for your React Router loaders.

The following example sets the language to non-regional English and the country to Canada (`/server.js`):

```js
...
const {storefront} = createStorefrontClient({
  ...
  // Update your default language and country code
  i18n: {language: 'EN', country: 'CA'},
  ...
});
```

### Step 2: Update the HTML lang attribute

The `lang` HTML attribute is used to identify the language to screen readers and search engines. Update the HTML roots to match the `language` in `server.js` (`/app/root.jsx`):

```jsx
export default function App() {
  return (
    // Update your default lang attribute
    <html lang="EN">
      ...
    </html>
  );
}
```

Add to `CatchBoundary` component if it exists:

```jsx
export function CatchBoundary() {
  return (
    <html lang="EN">
      ...
    </html>
  );
}
```

Add to `ErrorBoundary` component if it exists:

```jsx
export ErrorBoundary({error}: {error: Error}) {
  return (
    <html lang="EN">
      ...
    </html>
  );
}
```

### Step 3: Make sure redirects are properly url encoded

If you have multilingual handles for your product or collection, for example, `products/スノーボード`, make sure to encode url when making redirects (`/app/routes/($locale).products.$productHandle.js`):

```js
export async function loader({params, request, context}) {
  const {productHandle} = params; // productHandle = 'スノーボード'

  ...

  if (noSelectedProductVariant) {
    // Use URL to prevent accidental double url encoding
    const newUrl = new URL(
      `/products/${productHandle}?${firstVariantSearchParams.toString()}`,
      'http://example.com'  // Any domain to satisfy the URL api
    );

    // Redirect to '/products/%E3%82%B9%E3%83%8E%E3%83%BC%E3%83%9C%E3%83%BC%E3%83%89?Size=154cm&Color=Syntax'
    throw redirect(newUrl.pathname + newUrl.search, 302);
  }

  ...
```

### Next steps

* Setup multiregion and multilingual storefront with URL paths.
* Setup multiregion and multilingual storefront with domains and subdomains.

---

## Setup multilingual and multi-regional storefronts with URL paths (Markets)

> Fonte: https://shopify.dev/docs/storefronts/headless/hydrogen/markets/multiple-languages-url-paths

> **Note:** This guide might not be compatible with features introduced in Hydrogen version 2025-05 and above. Check the latest [documentation](https://shopify.dev/docs/api/hydrogen) if you encounter any issues.

In this guide you will learn how to setup your Hydrogen project for supporting multi-region and multilingual storefronts by using URL paths.

For example, say you have a storefront that should work in English (EN) and in non-regional French (FR) for different customers. You will setup the project to handle requests as following:

| Language | URL path |
| - | - |
| English | `ca.hydrogen.shop` |
| French | `ca.hydrogen.shop/fr` |

### Requirements

* You have a working Hydrogen project (see the getting started guide).
* You have setup the regions and languages you chose for your store with Shopify Markets.
* You're familiar with using the Storefront API with Shopify Markets.

### Step 1: Create a utility that checks the requested URL paths locale

Create a utility function that reads the requested host and directory path which return the right `Locale` object using the Storefronts API's supported language and country codes.

> **Tip:** You can use the `/app/lib/utils.js` in the Hydrogen demo store as a reference.

The following is an example utility function with the following locales `en_CA`, `fr_CA` and `en_US` (`/app/lib/utils.js`):

```js
export function getLocaleFromRequest(request) {
  // Get the user request URL
  const url = new URL(request.url);

  // Match the URL host
  switch (url.host) {
    case 'ca.hydrogen.shop':
      // This regex matches `/fr/` paths in the request
      if (/^\/fr($|\/)/.test(url.pathname)) {
        return {
          language: 'FR',
          country: 'CA',
        };
      } else {
        return {
          language: 'EN',
          country: 'CA',
        };
      }
      break;
    default:
      return {
        language: 'EN',
        country: 'US',
      };
  }
}
```

The `Locale` object returned should resemble the following example (TypeScript type):

```ts
import {
  CountryCode,
  LanguageCode,
} from '@shopify/storefront-kit-react/storefront-api-types';


export type Locale = {
  language: LanguageCode;
  country: CountryCode;
};
```

### Step 2: Match routes that contain language in the URL

Using React Router's optional segments, add `($locale)` in front of your routes. This ensures that routes such as `/products/123` and `/fr/products/123` match the same product route file, so that the correct page is rendered.

Before file rename with `($locale)`:

```markdown
├── app
│   ├── routes
│   │   ├── _index.tsx
│   │   ├── products.$productHandle.tsx
...
```

After renaming the routes with `($locale)`:

```markdown
├── app
│   ├── routes
│   │   ├── ($locale)._index.tsx
│   │   ├── ($locale).products.$productHandle.tsx
...
```

At this point, you should see your pages render when you make requests to `/fr/` URL paths.

### Step 3: Add i18n to the storefront client

In your `server.js`, update `i18n` to the result of the utility function when creating the Hydrogen storefront client. By doing this, you now have the locale available throughout the app for every storefront query (`/server.js`):

```js
const {storefront} = createStorefrontClient({
  ...
  i18n: getLocaleFromRequest(request),
  ...
});
```

### Step 4: Add @inContext directive to your GraphQL queries

To support international pricing and languages in Storefront API, you need to pass the `$country` and `$language` with an `@inContext` directive within any requests. Hydrogen automatically injects these parameters.

Before:

```jsx
const FEATURED_QUERY = `#graphql
  query homepage {
    collections(first: 3, sortKey: UPDATED_AT) {
      nodes {
        id
        title
        handle
        image {
          altText
          width
          height
          url
        }
      }
    }
  }
   `;
```

After:

```jsx
const FEATURED_QUERY = `#graphql
  query homepage($country: CountryCode, $language: LanguageCode)
     @inContext(country: $country, language: $language) {
    collections(first: 3, sortKey: UPDATED_AT) {
      nodes {
        id
        title
        handle
        image {
          altText
          width
          height
          url
        }
      }
    }
  }
   `;
```

You don't need to manually provide query variables for `country` and `language`. You can make the query with `storefront.query` in the data loader:

```js
export async function loader({
  context: {storefront},
}) {
  return json({
    featureCollections: await storefront.query<{
      collections;
    }>(FEATURED_COLLECTIONS_QUERY),
  });
}
```

Hydrogen automatically injects the locale parameters to `storefront.query` based on what was defined in `i18n` when you created the client. For example, if a request came from `hydrogen.fr`, then the country `CA` and language `FR` are used. If you want to override the locale, supply the query variables:

```js
export async function loader({
  context: {storefront},
}) {
  return json({
    featureCollection: await storefront.query(FEATURED_COLLECTIONS_QUERY, {
      variables: {
        country: 'CA',    // Always query back in CA currency
        language: 'FR',   // Always query back in FR language
      }
    }),
  });
}
```

### Step 5: Match non-existent pages

A request to `/this-route-does-not-exist` should return a `404` not found page. To achieve this, create a `$.(tsx|jsx)` file in the `/app/routes/` folder. This Remix splat route will handle all the non-matching routes (`/app/routes/$.jsx`):

```js
export async function loader() {
  throw new Response('Not found', {status: 404});
}

export default function Component() {
  return null;
}
```

### Step 6: Handle invalid URL lang parameters

In `/app/routes/index.jsx`, set up handling of invalid URL parameters localization. For example, any request with lang parameter `au` when you don't handle this language should return a `404`:

```js
export async function loader({
  request,
  params,
  context,
}) {
  const {language, country} = context.storefront.i18n;

  if (
    params.locale &&
    params.locale.toLowerCase() !== `${language}-${country}`.toLowerCase()
  ) {
    // If the locale URL param is defined, yet we still are on `EN-US`
    // the locale param must be invalid, send to the 404 page
    throw new Response(null, {status: 404});
  }
  ...
}
```

### Step 7: Create a utility function to add a language path prefix

Create a utility function that adds the locale path prefix to any URL path. For example, if the path is `/products` and the buyer prefers the locale `fr_CA`, then the utility converts it to `/fr/products` (`/server.js`):

```js
export function usePrefixPathWithLocale(path) {
  const [root] = useMatches();
  const selectedLocale = root.data.selectedLocale;

  return selectedLocale
    ? `${selectedLocale.pathPrefix}${
        path.startsWith('/') ? path : '/' + path
      }`
    : path;
}
```

### Step 8: Create Link component with locale path prefix

Create a `<Link />` wrapper component that adds the locale path prefix.

> **Caution:** Make sure your project is using this `Link` component for all inbound navigation. This ensures the prefix locale gets appended for every link. For example navigating from `fr/products` to `fr/collections` without this `Link` component loses the `fr` path.

`/app/components/Link.js`:

```js
import {
  Link as RemixLink,
  NavLink as RemixNavLink,
  useMatches,
} from '@remix-run/react';
import {usePrefixPathWithLocale} from '~/lib/utils';

export function Link(props) {
  const {to, className, ...resOfProps} = props;
  const [root] = useMatches();
  const selectedLocale = root.data.selectedLocale;

  let toWithLocale = to;

  if (typeof to === 'string') {
    toWithLocale = selectedLocale ? `${selectedLocale.pathPrefix}${to}` : to;
  }

  if (typeof className === 'function') {
    return (
      <RemixNavLink
        to={toWithLocale}
        className={className}
        {...resOfProps}
      />
    );
  }

  return (
    <RemixLink to={toWithLocale} className={className} {...resOfProps} />
  );
}

export function usePrefixPathWithLocale(path) {
  const [root] = useMatches();
  const selectedLocale = root.data.selectedLocale;

  return selectedLocale
    ? `${selectedLocale.pathPrefix}${
        path.startsWith('/') ? path : '/' + path
      }`
    : path;
}
```

### Step 9: Make sure redirects are properly url encoded

If you have multilingual handles for your product or collection, for example, `products/スノーボード`, make sure to encode url when making redirects (`/app/routes/($locale).products.$productHandle.js`):

```js
export async function loader({params, request, context}) {
  const {productHandle} = params; // productHandle = 'スノーボード'

  ...

  if (noSelectedProductVariant) {
    // Use URL to prevent accidental double url encoding
    const newUrl = new URL(
      `/products/${productHandle}?${firstVariantSearchParams.toString()}`,
      'http://example.com'  // Any domain to satisfy the URL api
    );

    // Redirect to '/products/%E3%82%B9%E3%83%8E%E3%83%BC%E3%83%9C%E3%83%BC%E3%83%89?Size=154cm&Color=Syntax'
    throw redirect(newUrl.pathname + newUrl.search, 302);
  }

  ...
```

### Next steps

* [Create a country selector](https://shopify.dev/docs/storefronts/headless/hydrogen/markets/country-selector): Learn how to setup a country selector to allow users to choose their own country.

---

## Create a Country Selector (Markets)

> Fonte: https://shopify.dev/docs/storefronts/headless/hydrogen/markets/country-selector

> **Note:** This guide might not be compatible with features introduced in Hydrogen version 2025-05 and above. Check the latest [documentation](https://shopify.dev/docs/api/hydrogen) if you encounter any issues.

In this guide you will learn how to create a country selector so that buyers can change the store language and currency.

### Requirements

* You've completed the Hydrogen getting started with a `Hello World` example project.
* You've setup the regions and languages for your store with Shopify Markets.
* You've completed the setup multi-region and multilingual storefront with URL paths or with domains and subdomains tutorial.
* You're familiar with using the Storefront API with Shopify Markets.

### Step 1: Provide a list of available countries

Create a JSON file with a list of available countries that will be rendered at every page. You can use the `/app/data/countries.js` file in the Hydrogen demo store as a point of reference.

For performance and SEO reasons, Shopify recommends using a static JSON variable for the countries. Optionally, you can create a build script that generates this file on build.

`/app/data/countries.js`:

```js
export const countries = {
  default: {
    language: 'EN',
    country: 'US',
    label: 'United States (USD $)', // Labels to be shown in the country selector
    host: 'hydrogen.shop', // The host and pathPrefix are used for linking
  },
  'en-ca': {
    language: 'EN',
    country: 'CA',
    label: 'Canada (CAD $)',
    host: 'ca.hydrogen.shop',
  },
  'fr-ca': {
    language: 'EN',
    country: 'CA',
    label: 'Canada (Français) (CAD $)',
    host: 'ca.hydrogen.shop',
    pathPrefix: '/fr',
  },
  'en-au': {
    language: 'EN',
    country: 'AU',
    label: 'Australia (AUD $)',
    host: 'hydrogen.au',
  },
};
```

`/app/data/countries.ts`:

```ts
import type {
CountryCode,
LanguageCode,
} from '@shopify/hydrogen/storefront-api-types';

export type Locale = {
  language: LanguageCode;
  country: CountryCode;
  label: string;
  host: string;
  pathPrefix?: string
};

export const countries: Record<string, Locale> = {
  default: {
    language: 'EN',
    country: 'US',
    label: 'United States (USD $)', // Labels to be shown in the country selector
    host: 'hydrogen.shop', // The host and pathPrefix are used for linking
  },
  'en-ca': {
    language: 'EN',
    country: 'CA',
    label: 'Canada (CAD $)',
    host: 'ca.hydrogen.shop',
  },
  'fr-ca': {
    language: 'EN',
    country: 'CA',
    label: 'Canada (Français) (CAD $)',
    host: 'ca.hydrogen.shop',
    pathPrefix: '/fr',
  },
  'en-au': {
    language: 'EN',
    country: 'AU',
    label: 'Australia (AUD $)',
    host: 'hydrogen.au',
  },
};
```

### Step 2: Create getLocaleFromRequest utility

Create the `getLocaleFromRequest` utility function. This function will read the request and determine the locale to be used throughout the app (`/app/lib/utils.js`):

```js
import {countries} from '~/data/countries';

export function getLocaleFromRequest(request) {
  const url = new URL(request.url);

  switch (url.host) {
    case 'ca.hydrogen.shop':
      if (/^\/fr($|\/)/.test(url.pathname)) {
        return countries['fr-ca'];
      } else {
        return countries['en-ca'];
      }
      break;
    case 'hydrogen.au':
      return countries['en-au'];
      break;
    default:
      return countries['default'];
  }
}
```

### Step 3: Add the selected locale in the root loader function

This step gets the user's request and finds the associated locale. You should make the selected locale available throughout the app with the `loader` (`/app/root.jsx`):

```jsx
export async function loader({context, request}) {
  ...
  return defer({
    ...,
    selectedLocale: await getLocaleFromRequest(request),
  });
}
```

### Step 4: Create a resource route for the available countries

A Remix resource route is useful when the UI fetches the available countries to display (`/routes/($locale).api.countries.js`):

```jsx
import {json} from '@remix-run/server-runtime';
import {CacheLong, generateCacheControlHeader} from '@shopify/hydrogen';
import {countries} from '~/data/countries';

export async function loader() {
  return json(
    {...countries},
    {headers: {'cache-control': generateCacheControlHeader(CacheLong())}},
  );
}

// no-op
export default function CountriesResourceRoute() {
  return null;
}
```

### Step 5: Render the available countries as a form

Create a `CountrySelector` component using Remix Forms (`/app/components/CountrySelector.jsx`):

```jsx
import {Form, useMatches, useLocation, useFetcher} from '@remix-run/react';
import {useEffect, useState} from 'react';

export function CountrySelector() {
  const [root] = useMatches();
  const selectedLocale = root.data.selectedLocale;
  const {pathname, search} = useLocation();

  const [countries, setCountries] = useState({});

  // Get available countries list
  const fetcher = useFetcher();
  useEffect(() => {
    if (!fetcher.data) {
      fetcher.load('/api/countries');
      return;
    }
    setCountries(fetcher.data);
  }, [countries, fetcher.data]);

  const strippedPathname = pathname.replace(selectedLocale.pathPrefix, '');

  return (
    <details>
      <summary>{selectedLocale.label}</summary>
      <div className="overflow-auto border-t py-2 bg-contrast w-full max-h-36">
        {countries &&
          Object.keys(countries).map((countryKey) => {
            const locale = countries[countryKey];
            const hreflang = `${locale.language}-${locale.country}`;

            return (
              <Form method="post" action="/locale" key={hreflang}>
                <input type="hidden" name="language" value={locale.language} />
                <input type="hidden" name="country" value={locale.country} />
                <input
                  type="hidden"
                  name="path"
                  value={`${strippedPathname}${search}`}
                />
                <button type="submit">{locale.label}</button>
              </Form>
            );
          })}
      </div>
    </details>
  );
}
```

### Step 6: Handle form submit

Create the `/app/routes/($locale).jsx` route that will handle the form submit action:

```jsx
import {redirect} from '@shopify/remix-oxygen';
import invariant from 'tiny-invariant';
import {countries} from '~/data/countries';

export const action = async ({request, context}) => {
  const {session} = context;
  const formData = await request.formData();

  // Make sure the form request is valid
  const languageCode = formData.get('language');
  invariant(languageCode, 'Missing language');

  const countryCode = formData.get('country');
  invariant(countryCode, 'Missing country');

  // determine where to redirect to relative to where user navigated from
  // ie. hydrogen.shop/collections -> ca.hydrogen.shop/collections
  const path = formData.get('path');
  const toLocale = countries[`${languageCode}-${countryCode}`.toLowerCase()];

  const cartId = await session.get('cartId');

  // Update cart buyer's country code if there is a cart id
  if (cartId) {
    await updateCartBuyerIdentity(context, {
      cartId,
      buyerIdentity: {
        countryCode,
      },
    });
  }

  const redirectUrl = new URL(
    `${toLocale.pathPrefix || ''}${path}`,
    `https://${toLocale.host}`
  );

  return redirect(redirectUrl, 302);
};

async function updateCartBuyerIdentity({storefront}, {cartId, buyerIdentity}) {
  const data = await storefront.mutate(UPDATE_CART_BUYER_COUNTRY, {
    variables: {
      cartId,
      buyerIdentity,
    },
  });
}

const UPDATE_CART_BUYER_COUNTRY = `#graphql
  mutation CartBuyerIdentityUpdate(
    $cartId: ID!
    $buyerIdentity: CartBuyerIdentityInput!
  ) {
    cartBuyerIdentityUpdate(cartId: $cartId, buyerIdentity: $buyerIdentity) {
      cart {
        id
      }
    }
  }
`;
```

TypeScript (`/app/routes/($locale).tsx`):

```tsx
import type {
  CountryCode,
  LanguageCode,
  CartBuyerIdentityInput,
  Cart,
} from '@shopify/hydrogen/storefront-api-types';
import {redirect, type AppLoadContext, type ActionFunction} from '@shopify/remix-oxygen';
import invariant from 'tiny-invariant';
import {countries} from '~/data/countries';

export const action: ActionFunction = async ({request, context}) => {
  const {session} = context;
  const formData = await request.formData();

  // Make sure the form request is valid
  const languageCode = formData.get('language') as LanguageCode;
  invariant(languageCode, 'Missing language');

  const countryCode = formData.get('country') as CountryCode;
  invariant(countryCode, 'Missing country');

  // Determine where to redirect to relative to where user navigated from
  // ie. hydrogen.shop/collections -> ca.hydrogen.shop/collections
  const path = formData.get('path');
  const toLocale = countries[`${languageCode}-${countryCode}`.toLowerCase()];

  const cartId = await session.get('cartId');

  // Update cart buyer's country code if there is a cart id
  if (cartId) {
    await updateCartBuyerIdentity(context, {
      cartId,
      buyerIdentity: {
        countryCode,
      },
    });
  }

  const redirectUrl = new URL(
    `${toLocale.pathPrefix || ''}${path}`,
    `https://${toLocale.host}`,
  ).toString();

  return redirect(redirectUrl, 302);
};

async function updateCartBuyerIdentity(
  {storefront}: AppLoadContext,
  {
    cartId,
    buyerIdentity,
  }: {
    cartId: string;
    buyerIdentity: CartBuyerIdentityInput;
  },
) {
  const data = await storefront.mutate<{
    cartBuyerIdentityUpdate: {cart: Cart};
  }>(UPDATE_CART_BUYER_COUNTRY, {
    variables: {
      cartId,
      buyerIdentity,
    },
  });

  invariant(data, 'No data returned from Shopify API');

  return data.cartBuyerIdentityUpdate.cart;
}

const UPDATE_CART_BUYER_COUNTRY = `#graphql
  mutation CartBuyerIdentityUpdate(
    $cartId: ID!
    $buyerIdentity: CartBuyerIdentityInput!
  ) {
    cartBuyerIdentityUpdate(cartId: $cartId, buyerIdentity: $buyerIdentity) {
      cart {
        id
      }
    }
  }
`;
```

### Step 7: Make sure re-rendering happens at the root HTML

Make sure to provide a `key` to the components that will change due to localization, especially for URL path localization schemes. Sometimes React won't know when to re-render a component; to avoid this, add localization as a key in the `App` (`/app/root.jsx`):

```jsx
export default function App() {
  const data = useLoaderData();
  const locale = data.selectedLocale;

  return (
    <html lang={locale.language}>
      <head>
        <Seo />
        <Meta />
        <Links />
      </head>
      <body>
        <Layout
          layout={data.layout}
          key={`${locale.language}-${locale.country}`} // key by hreflang
        >
          <Outlet />
        </Layout>
        <Debugger />
        <ScrollRestoration />
        <Scripts />
      </body>
    </html>
  );
}
```

---

# Parte 3 — Oxygen (hosting & deployments)

Oxygen is Shopify's global edge hosting platform for Hydrogen storefronts. This section covers deployments, environments, CI/CD, and the runtime.

Mini-TOC:
- Deployments (overview, continuous/manual deployment, shareable links, rollbacks, redeployments, immutability, retention)
- Environments (managing, environment variables, visibility, URLs)
- Hydrogen CI/CD with GitHub
- Custom CI/CD

## Deployments

> Fonte: https://shopify.dev/docs/storefronts/headless/hydrogen/deployments

A deployment is an immutable snapshot of your Hydrogen app, running on Oxygen. Every deployment has its own unique preview URL so that you can view, test, or approve changes before merging them and deploying to production. You can also deploy to specific [environments](https://shopify.dev/docs/storefronts/headless/hydrogen/environments).

### Continuous deployment

Developers typically prefer automated systems that deploy their app whenever they update its code base. These types of workflows are broadly known as continuous integration or continuous delivery/deployment (CI/CD) systems.

Hydrogen and Oxygen support [CI/CD with GitHub](https://shopify.dev/docs/storefronts/headless/hydrogen/deployments/github) out of the box. You can also [create your own CI/CD workflows](https://shopify.dev/docs/storefronts/headless/hydrogen/deployments/custom-ci-cd) using the Hydrogen CLI.

[Deploy with GitHub (recommended)](https://shopify.dev/docs/storefronts/headless/hydrogen/deployments/github) — Automatically create deployments whenever you merge or push changes to your connected GitHub repo.

[Custom CI/CD](https://shopify.dev/docs/storefronts/headless/hydrogen/deployments/custom-ci-cd) — Configure your own advanced CI/CD workflows, such as deploying from BitBucket or GitLab.

### Manual deployment

You can create a new deployment from your local development environment with the Hydrogen CLI `deploy` command. The Hydrogen CLI builds, uploads, and deploys your app, then returns the deployment's unique URL.

```terminal
npx shopify hydrogen deploy
```

Consult the Hydrogen CLI reference for the complete list of options for the [`deploy`](https://shopify.dev/docs/api/shopify-cli/hydrogen/hydrogen-deploy) command.

### Shareable links

Deployments are private by default, which means that you need to be logged in to your store to view them. If your store is on the Basic plan or above, then you can create shareable links that let anyone view deployments, even if they're not logged in.

Be aware of the following when you use shareable links:

* Shareable links are URLs that include a token that bypasses the deployment's login requirement. Be sure to give shareable links only to people you trust.
* Making changes to a shareable link takes up to 30 seconds.
* Oxygen blocks search engines from indexing shared deployments with a `disallow` rule on the deployment's `robots.txt` file. This prevents potential harm to SEO caused by duplicated content.

#### Create a shareable link

1. In your Hydrogen storefront, open the deployment details page for the deployment that you want to update.
2. Click **Share**.
3. Select **Anyone with the link**.
4. Click **Copy link** to copy the shareable link to your clipboard.
5. Click **Close**.

#### Reset a shareable link

Resetting a shareable link revokes its existing token and creates a new one. The old link will stop working and people will need to use the new shareable link to view the deployment.

1. In your Hydrogen storefront, open the deployment details page for the deployment that you want to update.
2. Click **Share**.
3. Click **Reset link**.
4. Click **Reset** to confirm.
5. Click **Copy link** to copy the new link.
6. Click **Close**.

#### Remove a shareable link

Removing a shareable link revokes its existing token, which returns the deployment to its default state, meaning it's accessible only to logged-in staff.

1. In your Hydrogen storefront, open the deployment details page for the deployment to update.
2. Click **Share**.
3. Click **Staff accounts only**.
4. Click **Close**.

### Deployment rollbacks

By default, [environment URLs](https://shopify.dev/docs/storefronts/headless/hydrogen/environments#environment-urls) point to the environment's most recent deployment.

If the most recent update contains a bug or other error, you can temporarily roll back to a previous deployment while you work on a fix. Rolling back doesn't redeploy or delete any deployments; it simply changes which deployment the environment URL points to.

> **Caution:** Oxygen deployments are immutable, which means that their environment variables could be outdated. Always verify that a previous deployment works as expected before rolling back to it.

#### Roll back to a previous deployment

Only production and custom environments can be rolled back.

1. On your Hydrogen storefront overview page, click `…` on the environment to roll back.
2. Click **View deployments**.
3. In the list of deployments, click `…` beside the deployment to roll back to.
4. Click **Make this the current deployment**.
5. Click **Make current for {Environment}** to confirm.

The next time that you push an update to its linked branch, the environment will return to the default behavior of pointing to the most recent deployment.

### Redeployments

Redeploying an Oxygen environment creates a new deployment that re-uses the original deployment's immutable code, but injects the current set of [environment variables](https://shopify.dev/docs/storefronts/headless/hydrogen/environments#environment-variables).

Redeployments are available for production and custom environments, but not the preview environment. When you edit an environment variable in the Shopify admin, you'll be prompted with the option to redeploy the relevant environments, but you can redeploy at any time.

#### Redeploy an environment

Redeploying an environment redeploys its current deployment only. Older deployments in that environment aren't redeployed.

1. On the storefront overview page, click the three dots in the upper right of the environment you want to redeploy.
2. Click **Redeploy environment**.
3. Click **Redeploy** to confirm.

### Deployment immutability

Every deployment in Oxygen is immutable: each deployment is a snapshot of your Hydrogen project's codebase at a specific point in time. Typically, that snapshot is an individual Git commit.

Deployments retain all the environment variables that they had when they were first deployed. If you update your environment variables, then older deployments won't use the updated values until you redeploy.

### Deployment retention policy

Oxygen's data retention policy is designed to ensure that your Hydrogen storefront is always available to customers, and that you can always roll back to a previous deployment in case of error.

Oxygen deployments remain accessible for a minimum of six months. After that time, deployments are deleted, including their bundled worker files, logs, and preview URLs.

Your ten most recent Oxygen deployments per environment always remain accessible, regardless of how old they are.

#### Log data retention

Deployments' runtime logging data is available for up to one month. If you need to retain logging data for longer than that, then consider connecting a [log drain](https://shopify.dev/docs/storefronts/headless/hydrogen/logging).

---

## Environments

> Fonte: https://shopify.dev/docs/storefronts/headless/hydrogen/environments

Hydrogen [storefronts](https://shopify.dev/docs/storefronts/headless/hydrogen/storefronts) can contain multiple environments, to which you make [deployments](https://shopify.dev/docs/storefronts/headless/hydrogen/deployments).

Each environment is linked to a branch in your Hydrogen app's Git repository:

| Environment | Associated Git branch |
| - | - |
| **Production** | Default branch. You can edit the production environment to select a different branch. |
| **Custom environments** | Optional. Define multiple custom environments, with each one linked to its own branch. |
| **Preview** | All other branches not linked to a production or custom environment. |

Each environment can have its own set of environment variables, which allows you to use different values in your app depending on the environment. This can be useful for testing, feature development, and security.

### Managing environments

The production and preview environments are required for all storefronts, and can't be deleted. In addition to these required environments, you can optionally create additional custom environments to develop new features, test out ideas, and more.

#### Create a new environment

1. In your Hydrogen storefront, click **Storefront settings**.
2. Click **Environments and variables**.
3. Click **Add environment**.
4. Select an existing repository branch to link to the environment, or create a new branch.
5. Type a name for the branch. The name determines the environment URL.
6. Select whether to make the environment public or private.
7. Optional: Under **Copy environment variables**, select an existing environment to copy variables from.
8. Click **Save**.

#### Update an environment

1. In your Hydrogen storefront, click **Storefront settings**.
2. Click **Environments and variables**.
3. Click the environment to edit.
4. Make your changes.
5. Click **Save**.

#### Delete a custom environment

1. In your Hydrogen storefront, click **Storefront settings**.
2. Click **Environments and variables**.
3. Click the environment to delete.
4. Click **Delete environment**.

### Environment variables

Each environment can have its own set of environment variables, which are key-value pairs. Variable keys can be called in your app code, and return contextual values for the environment where the deployment is running. Each environment can have a maximum of 110 unique environment variables.

#### Accessing environment variable values in your app

Hydrogen automatically adds your environment variables to a request's `context` object. You can access the values of environment variables from a loader or action:

JavaScript:

```js
export const loader = async ({context}) => {
  const publicStoreDomain = context.env.PUBLIC_STORE_DOMAIN;
};
```

TypeScript:

```ts
export const loader = async ({context}: LoaderFunctionArgs) => {
  const publicStoreDomain = context.env.PUBLIC_STORE_DOMAIN;
};
```

#### Create a new environment variable

1. In your Hydrogen storefront, click **Storefront settings**.
2. Click **Environments and variables**.
3. Under **Variables**, click **Add variable**.
4. Under **Key**, type a key. It's a common convention for keys to use all-capital letters and underscores, such as `EXAMPLE_API_TOKEN`.
5. Under **Value**, add the value.
6. Optional: Check **Make this value secret** to hide the value after saving. This can be useful for sensitive information like API keys.
7. Under **Environments**, select the environments where the value should be returned.
8. Click **Save**.

Click **Add another value** to add additional values for other environments.

#### Edit an environment variable

You can edit keys and values, as well as which environments they apply to.

1. In your Hydrogen storefront, click **Storefront settings**.
2. Click **Environments and variables**.
3. Click the environment variable to update.
4. Make your changes.
5. Click **Save**.

You might want to redeploy any environments that require the updated variables.

#### Delete an environment variable

Deleting an environment variable deletes the key and all its associated values.

1. In your Hydrogen storefront, click **Storefront settings**.
2. Click **Environments and variables**.
3. Click the environment variable to delete.
4. Click **Delete variable**.
5. Click **Delete variable** to confirm.

#### Required environment variables

Oxygen requires the following variables to query your store's data. They're automatically added when you create a storefront. Some variables are read-only, meaning they can't be edited directly.

| Variable | Description | Read-only? |
| - | - | - |
| `PRIVATE_STOREFRONT_API_TOKEN` | Your private Storefront API access token, used for server-side queries. This token is read-only, but can be rotated. | Yes |
| `PUBLIC_CUSTOMER_ACCOUNT_API_CLIENT_ID` | Your Customer Account API client ID. This token is read-only, but can be rotated. | Yes |
| `PUBLIC_CUSTOMER_ACCOUNT_API_URL` | The URL endpoint that accepts Customer Account API authentication requests. | Yes |
| `PUBLIC_STORE_DOMAIN` | Your store domain ID (such as `example.myshopify.com`). | Yes |
| `PUBLIC_STOREFRONT_API_TOKEN` | Your Storefront API access token, used for client-side queries. | Yes |
| `PUBLIC_STOREFRONT_ID` | Your Hydrogen storefront's numeric ID. | Yes |
| `SESSION_SECRET` | The value that React Router uses to sign session cookies. | No |

#### Rotate your private Storefront API token

If your private Storefront API access token is exposed publicly, then you should rotate it to protect sensitive data and prevent abuse.

1. In your Hydrogen storefront, click **Storefront settings**.
2. Click **Storefront API**.
3. Under **Rotate private access token**, click **Generate new token**.
4. Click **Generate new token** to confirm.
5. Optional: If you have other client apps using your private API token, then update them with the new token value.
6. Under **Past private access token**, click **Delete**.
7. Push a commit to your GitHub repo to trigger a new deployment. At this time, Oxygen doesn't automatically re-deploy environments when rotating API tokens.

#### Immutability

Oxygen deployments are immutable, which includes their environment variable values. This means any changes to environment variables don't affect deployments that were made in the past.

If you create or update environment variables, then you need to redeploy before your changes will take effect.

### Environment visibility

By default, environments are private, which means that you need to be logged into your store to view them. You can also make an environment public, meaning anyone with the URL can view it.

#### Toggle an environment to public or private

1. In your Hydrogen storefront, click **Storefront settings**.
2. Click **Environments and variables**.
3. Click the environment to edit.
4. Under **URL privacy**, select either **Public** or **Private**.
5. Click **Save**.

> **Note:** Page load speed on private deployment URLs is slower because authentication must be verified on each route. Toggling the deployment to public improves load time but also means that anyone with access to the link can view the page.

#### Public environment limits

Stores have a limited number of public environments available, based on their plan.

| Plan | Public environment limit |
| - | - |
| Pause and build | 0 |
| Basic | 1 |
| Shopify | 1 |
| Advanced | 1 |
| Shopify Plus | 25 |
| Plus Partner Sandbox stores | 1 |

### Environment URLs

Each environment has an automatically generated URL. By default, this URL always points to the most recent deployment to that environment.

### Next steps

* Learn how to [deploy your Hydrogen storefront](https://shopify.dev/docs/storefronts/headless/hydrogen/deployments) to Oxygen and other runtimes.

---

## Hydrogen CI/CD with GitHub

> Fonte: https://shopify.dev/docs/storefronts/headless/hydrogen/deployments/github

Hydrogen supports CI/CD with GitHub out of the box. If you connect the Hydrogen channel to GitHub, then Oxygen will automatically deploy every time you push or merge changes in your Hydrogen repository.

When using Hydrogen with GitHub, you have two options:

* Connect an existing Hydrogen app repository
* Scaffold a new repository from the Shopify admin

### Requirements

* A Shopify account on a supported plan
* A GitHub account
* The Hydrogen app installed on your store
* The Shopify GitHub App installed on your GitHub account

### Connect an existing repo

If you created a Hydrogen app with the CLI, then you can upload your repository to GitHub and then connect it to Shopify.

#### Step 1: Connect your GitHub repo to the Hydrogen channel

1. In the Shopify admin, under **Sales channels**, click **Hydrogen**.
2. Click **Create storefront**.
3. Type a name for your new storefront. The name can be edited later.
4. Make sure **Set up GitHub continuous deployment now** is selected.
5. Select your GitHub account or organization from the dropdown.
6. Select the repository for your Hydrogen app.
7. Click **Connect**.

Oxygen pulls a copy of your Hydrogen app code base and automatically creates a preview deployment. The Shopify GitHub app also opens a pull request in your repo to add a GitHub Actions workflow file to handle future deployments.

#### Step 2: Merge your Oxygen workflow file

To create deployments, "Oxygen requires a GitHub workflow file in your repository. The Shopify GitHub app automatically opens a pull request to create this file when you connect a repo."

Follow these steps to finish configuring your Hydrogen app for continuous deployment to Oxygen:

1. In the Hydrogen channel, click the name of the storefront that you just created.
2. Click **Review and merge on GitHub** to open the pull request in a new tab.
3. Follow GitHub's prompts to merge the PR.
4. Close the tab to return to the Hydrogen storefront overview.

Oxygen will automatically create a new deployment in your production environment and continue watching your repo for updates. Each time you push one or more commits to your repo, Oxygen will create a new preview deployment with your changes.

### Create a new repo

You can create a new Hydrogen storefront and scaffold a new GitHub repository directly from the Shopify admin:

1. In the Shopify admin, under **Sales channels**, click **Hydrogen**.
2. Click **Create storefront**.
3. Type a name for your new storefront. The name can be edited later.
4. Make sure **Set up GitHub continuous deployment now** is selected.
5. Select your GitHub account or organization from the dropdown.
6. Type a name for the new repository.
7. Click **Create <repository name>**.
8. (Optional) If you want the repository to be public, then click **Create <repository name> as a public repository**.
9. Select **JavaScript** or **TypeScript** for your project language.
10. Click **Create**.

Shopify scaffolds a new Hydrogen app in your GitHub account, displays the storefront overview page, and automatically creates the first deployment of your storefront. Clone the new repo to start working on your Hydrogen app.

### Enable deployment PR comments

You can configure Shopify to comment on your pull requests with deployment preview links. This allows you to quickly access deployments in context, without needing to open the Shopify admin.

To enable deployment PR comments on GitHub:

1. In your Hydrogen storefront, click **Storefront settings**.
2. Click **Oxygen deployments**.
3. Under **Git repository**, check **Comment on pull requests with deployment preview links**.
4. (Optional) If you want preview links to be visible without needing to be logged into your store, select **Anyone with the link**. This option uses shareable links.

To test that comments are working, create a pull request for your Hydrogen app. The Shopify GitHub bot adds a comment, then updates it with more details as the deployment proceeds.

### Oxygen GitHub workflow

"Deployments to Oxygen from GitHub are controlled by an Oxygen workflow file in your Hydrogen app." If you connected an existing repo, then Shopify will automatically open a PR to add this file when you connect a repository. If you created a new repo from the Shopify admin, then this file was automatically added.

This is an example of what an Oxygen workflow file looks like (`/.github/workflows/oxygen-deployment-0000000000.yml`):

```yml
# Don't change the line below!
#! oxygen_storefront_id: 0000000000


name: Storefront 0000000000
on: [push]


permissions:
  contents: read
  deployments: write


jobs:
  deploy:
    name: Deploy to Oxygen
    timeout-minutes: 30
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3


      - name: Setup node.js
        uses: actions/setup-node@v4
        with:
          node-version: 'lts/*'
          check-latest: true


      - name: Cache node modules
        id: cache-npm
        uses: actions/cache@v4
        env:
          cache-name: cache-node-modules
        with:
          path: ~/.npm
          key: ${{ runner.os }}-build-${{ env.cache-name }}-${{ hashFiles('**/package-lock.json') }}
          restore-keys: |
            ${{ runner.os }}-build-${{ env.cache-name }}-
            ${{ runner.os }}-build-
            ${{ runner.os }}-


      - name: Install dependencies
        run: npm ci


      - name: Build and Publish to Oxygen
        run: npx shopify hydrogen deploy
        env:
          SHOPIFY_HYDROGEN_DEPLOYMENT_TOKEN: ${{ secrets.OXYGEN_DEPLOYMENT_TOKEN_0000000000 }}
```

This is a standard GitHub Actions workflow file and you can edit it to customize your CI/CD workflows in GitHub. However, there are a few key points to be aware of:

* The first comment line refers to the immediate line following, which contains the app's associated storefront ID. Do not modify this.
* By default, the workflow installs app dependencies with npm. If you use a different package manager, then you'll need to edit this file to prevent errors caused by multiple lockfiles, as well as to manage module caching.

#### Alternate package managers

If you're using a package manager other than npm, such as Yarn or pnpm, note the following:

* Hydrogen and Oxygen use npm by default. Shopify can't guarantee compatibility with other package managers.
* "The Oxygen deployment workflow file uses npm by default, and assumes the presence of a package-lock.json file." You can edit the workflow file to use your preferred package manager. In particular, check that the steps to install dependencies, cache modules, and build your app are updated to use the correct commands.

### Next steps

* Support other version control platforms or more complex deployment systems with custom CI/CD workflows.
* Learn more about creating and managing Hydrogen environments.

---

## Deploy from any CI/CD system with deployment tokens (Custom CI/CD)

> Fonte: https://shopify.dev/docs/storefronts/headless/hydrogen/deployments/custom-ci-cd

Hydrogen supports [continuous deployment from GitHub](https://shopify.dev/docs/storefronts/headless/hydrogen/deployments/github) out of the box. But if you use another version control platform like BitBucket or GitLab, or want to create your own custom continuous integration or continuous delivery/deployment system (CI/CD), then you can use the Hydrogen CLI [`deploy`](https://shopify.dev/docs/api/shopify-cli/hydrogen/hydrogen-deploy) command in any context with a valid Oxygen deployment token.

### Oxygen deployment tokens

The `deploy` command requires a secret Oxygen deployment token. You can create and manage deployment tokens through your storefront settings. If you don't pass a deployment token with the `deploy` command, then the deployment fails.

Every Hydrogen storefront has a default deployment token that's automatically managed by Shopify and can't be removed or edited. If your default token is ever leaked, you can rotate it by clicking the **rotate** icon in your tokens list.

#### Create an Oxygen deployment token

1. In the Hydrogen storefront you want to deploy with a custom CI/CD workflow, click **Storefront settings**.
2. Click **Oxygen deployments**.
3. Under **Oxygen deployment tokens** click **Create new token**.
4. Confirm with **Generate new token**. The new token will be added to your token list with a placeholder name.
5. (Optional) Give the token a more descriptive name by clicking the **pencil icon**, typing in your preferred name, then clicking the **check icon**. The token's name has no effect on its functionality.

Each token is valid for one year. When it expires, delete it and create a new one.

For security reasons, it's best to create a new token for each service, instead of reusing the same token across different services.

#### Delete an Oxygen deployment token

Oxygen deployment tokens should be kept secret. If your token ever leaks, delete it and create a new one to keep your storefront secure.

1. In the Hydrogen storefront you want to update, click **Storefront settings**.
2. Click **Oxygen deployments**.
3. Beside the token you want to delete, click the **trash icon**.
4. Click **Delete token** to confirm.

### Using Oxygen deployment tokens

Once you've created a token, you can use it with the Hydrogen CLI `deploy` command in any supported context.

Oxygen deployment tokens are sensitive and should be kept secret. Most CI/CD platforms offer a way to securely store tokens and other secrets. Check with your service provider about how to securely store and use tokens in your workflows.

If your deployment token is exposed, delete it and create a new one.

#### Copy an Oxygen deployment token

1. In the Hydrogen storefront you want to configure CI/CD for, click **Storefront settings**.
2. Click **Oxygen deployments**.
3. Beside the token you want to copy, click the **clipboard icon**. The token value is copied to your clipboard.

### Example workflows

1. Copy the generated Oxygen deployment token.
2. Open your CI/CD system's project settings.
3. Locate the section for environment or repository variables.

* In Bitbucket go to your project > pipelines > starter pipeline > Add variable
* In GitLab go to your project > settings > CI/CD > Variables

4. In your CI/CD create a new variable with the name **SHOPIFY_HYDROGEN_DEPLOYMENT_TOKEN** and not the custom name you created when generating the token.
5. Save the variable in the CI/CD.

To run the integration process whenever the watcher branch changes, adjust your workflow or config file. The following are some examples. However every CI/CD is different and might require different inputs.

In the following examples, the Oxygen deployment token has been saved as a variable named `SHOPIFY_HYDROGEN_DEPLOYMENT_TOKEN`.

#### Bitbucket

Consult the BitBucket docs for full details on pipelines and variables and secrets.

```yml
image: atlassian/default-image:4

pipelines:
  default:
    - step:
        name: 'Build and deploy to Oxygen'
        script:
          - npm ci
          - npx shopify hydrogen deploy --token $SHOPIFY_HYDROGEN_DEPLOYMENT_TOKEN
```

#### GitLab

Consult the GitLab docs for full details on pipelines and variables. Ensure that the token and branches are not set to protected.

```yml
stages:
  - build-and-deploy

build-and-deploy:
  image: node:18
  stage: build-and-deploy
  script:
    - npm ci
    - npx shopify hydrogen deploy --token $SHOPIFY_HYDROGEN_DEPLOYMENT_TOKEN
```

#### CircleCI

Consult the CircleCI docs for full details about pipelines and environment variables.

```yml
# Use the latest 2.1 version of CircleCI pipeline process engine.
# See: https://circleci.com/docs/configuration-reference
version: 2.1
# Define a job to be invoked later in a workflow.
# Refer to https://circleci.com/docs/configuration-reference/#jobs
jobs:
  deploy-hydrogen-storefront-to-oxygen:
    docker:
      - image: cimg/node:current
    steps:
      - checkout
      - run:
          name: "Install Dependencies, Build and Deploy Storefront"
          command: |
            npm ci
            npx shopify hydrogen deploy --token $SHOPIFY_HYDROGEN_DEPLOYMENT_TOKEN

workflows:
  storefront-deploy:
    jobs:
      - deploy-hydrogen-storefront-to-oxygen
```

---

# Parte 4 — Customer Account API

The Customer Account API lets you build authenticated, customer-scoped experiences (view orders, manage profile and addresses, etc.) on a custom storefront. This section captures the overview + authentication reference and the how-to guides (not the full GraphQL schema).

Mini-TOC:
- GraphQL Customer Account API (overview + authentication/authorization reference)
- Building with the Customer Account API (overview)
- Getting started with the Customer Account API
- Authenticate customers with the Customer Account API
- Using the Customer Account API with Hydrogen

## GraphQL Customer Account API (overview + authentication)

> Fonte: https://shopify.dev/docs/api/customer

Create personalized, customer authenticated experiences with the Customer Account API. The API offers a full range of options making it possible for customers to view their orders, manage their profile and much more.

### Authentication

This guide will provide an overview of the new authentication system for the Customer Account API and help developers understand how to use it effectively.

#### Overview

The Customer Account API is designed to serve as the primary source for customer-scoped data and authenticated customer actions. To ensure secure access to this data, a robust authentication system is in place for developers.

#### Authentication process

We support two types of clients:

* **Confidential** - A client capable of keeping a client secret confidential. This type is typically used for server-side applications.
* **Public** - A client unable to keep a client secret confidential. This type is typically used for client-side applications, including web and mobile clients.

For **public clients**, we use [Proof Key for Code Exchange](https://datatracker.ietf.org/doc/html/rfc7636) or PKCE to mitigate the risk of authorization code interception.

In order to authenticate and utilize the Customer Account API, the sections below outline the necessary steps required by the [OAuth 2.0 authorization specification](https://datatracker.ietf.org/doc/html/rfc6749).

#### Discovery endpoints

Discovery endpoints are standardized URLs that return configuration data about a shop's authentication and API endpoints. Use these endpoints whenever you need to authenticate customers or make API requests to ensure your application works with any shop's configuration.

Using discovery endpoints automatically provides authentication and API URLs rather than hardcoding URLs. This keeps your integration working as Shopify's infrastructure evolves and automatically resolves the correct URLs for any shop, removing the need for hardcoded domain dependencies.

Your app can use the following discovery endpoints on the storefront domain:

* **OpenID configuration**
  * **Endpoint**: `GET /.well-known/openid-configuration`
  * **Returns**:
    * Authentication endpoints (authorization, token, logout URLs)
    * Standard OpenID Connect discovery format
* **Customer Account API configuration**:
  * **Endpoint**: `GET /.well-known/customer-account-api`
  * **Returns**:
    * Customer Account API endpoints (GraphQL API, MCP API)
    * Shopify-specific discovery format

### Authorization request

```ts
// First, discover the authentication endpoints
const discoveryResponse = await fetch(`https://${shopDomain}/.well-known/openid-configuration`);
const authConfig = await discoveryResponse.json();


// Now build the authorization request using the discovered endpoint
const clientId = process.env.CLIENT_ID;
const authorizationRequestUrl = new URL(authConfig.authorization_endpoint);


authorizationRequestUrl.searchParams.append(
  'scope',
  'openid email customer-account-api:full'
);
authorizationRequestUrl.searchParams.append(
  'client_id',
  clientId
);
authorizationRequestUrl.searchParams.append(
  'response_type',
  'code'
);
authorizationRequestUrl.searchParams.append(
  'redirect_uri',
  `<redirect_uri>`
);
authorizationRequestUrl.searchParams.append(
  'state',
  '<state>'
);
authorizationRequestUrl.searchParams.append(
  'nonce',
  '<nonce>'
);


// Optional: locale and region_country for market-aware login
// See: /docs/storefronts/headless/building-with-the-customer-account-api/market-aware-auth-urls


// Public client
const verifier = await generateCodeVerifier();
const challenge = await generateCodeChallenge(verifier);
localStorage.setItem('code-verifier', verifier);


authorizationRequestUrl.searchParams.append(
  'code_challenge',
  challenge
);
authorizationRequestUrl.searchParams.append(
  'code_challenge_method',
  'S256'
);


window.location.href = authorizationRequestUrl.toString()
```

#### Discover authentication endpoints

Before initiating the authorization flow, discover the authentication endpoints from the shop's storefront domain. The response contains `authorization_endpoint`, `token_endpoint`, `end_session_endpoint`, and `jwks_uri`.

The example code demonstrates how to:

1. Make a request to the discovery endpoint.
2. Parse the JSON response to access the authentication URLs.
3. Use these discovered endpoints in your OAuth flow.

You should include this discovery step once, at the beginning of your authentication flow. Then you can reuse the discovered endpoints throughout your application.

```ts
const discoveryUrl = `https://${shopDomain}/.well-known/openid-configuration`;


const response = await fetch(discoveryUrl);
const config = await response.json();


// config contains:
// {
//   "authorization_endpoint": "https://{shopDomain}/authentication/oauth/authorize",
//   "token_endpoint": "https://{shopDomain}/authentication/oauth/token",
//   "end_session_endpoint": "https://{shopDomain}/authentication/logout",
//   "jwks_uri": "https://{shopDomain}/authentication/.well-known/jwks.json",
//   "issuer": "https://shopify.com/authentication/{shopId}"
// }
```

#### Authorization

To redirect a customer to the login page, use the `authorization_endpoint` from the discovery response with the following parameters:

| Parameter | Value | Description |
|-----------|-------|-------------|
| **scope** | `openid email customer-account-api:full` | **Required.** A list of scope names separated by space. Scopes are attached to all access tokens issued from this authorization request and determine what data these access token will be able to retrieve from API endpoints. |
| **client_id** | `<client_id>` | **Required.** Unique UUID associated with the application. This should be visible in the Customer Account API settings of the given application / storefront. |
| **response_type** | `code` | **Required.** Implies that authorization code flow will be used. |
| **redirect_uri** | `<redirect_uri>` | **Required.** URL to redirect with `authorization code` after successful authentication. This has to be one of the redirect URIs defined in the customer account api settings of the given application/storefront. For public mobile applications, the scheme must be "shop.{shop_id}.*." |
| **state** | `<state>` | **Required.** A string of characters which will be returned along with the `code` during callback/redirect. This is used to prevent CSRF/XSRF. |
| **nonce** | `<nonce>` | This is used to mitigate replay attacks. The `nonce` will be returned in the `id_token` as part of the Obtain access token step. |
| **prompt** | `none` | Specifies that no login screen should be shown to the user. If a session is present, a `code` is returned that can be used in the Obtain access token step. If no session is present, a login_required error is returned to your redirect_uri endpoint. |
| **locale** | `en` | Specifies the language for the login screen. Supports regional variants that load market-specific translations configured for the market and language. For example, `fr-CA` for French Canadian or `en-GB` for British English. Refer to the `LanguageCode` enum for all supported language codes. |
| **region_country** | `CA` | Specifies the market context for the login experience, loading market-specific policies, branding, and content. Uses an ISO 3166-1 Alpha-2 country code. For example, `US`, `CA`, `GB`, `DE`, `FR`. If the specified country code doesn't match a configured market, then the primary market context is used. Use alongside `locale` for a fully localized, market-aware login experience. |
| **login_hint** | `<email>` | An email address of a user who is trying to authenticate. If present, the hint simplifies the sign-in flow by prefilling the email field in the sign-in form. |

#### Public client

In addition to the parameters above, public clients (web or mobile) need to provide the parameters outlined below.

| Parameter | Value | Description |
|-----------|-------|-------------|
| **code_challenge** | `<code_verifier>` | **Required.** A string that is derived from the `code_verifier` using a hashing algorithm. The `code_verifier` is a string that is randomly generated by the client. |
| **code_challenge_method** | `S256` | **Required.** The code challenge method. |

> **Info:** An example implementing a code challenge and verifier can be seen in the Code challenge and verifier section.

**Authorization Request (full example):**

```ts
// First, discover the authentication endpoints
const discoveryResponse = await fetch(`https://${shopDomain}/.well-known/openid-configuration`);
const config = await discoveryResponse.json();


const clientId = process.env.CLIENT_ID;
const authorizationRequestUrl = new URL(config.authorization_endpoint);


authorizationRequestUrl.searchParams.append(
  'scope',
  'openid email customer-account-api:full'
);
authorizationRequestUrl.searchParams.append(
  'client_id',
  clientId
);
authorizationRequestUrl.searchParams.append(
  'response_type',
  'code'
);
authorizationRequestUrl.searchParams.append(
  'redirect_uri',
  `<redirect_uri>`
);
authorizationRequestUrl.searchParams.append(
  'state',
  '<state>'
);
authorizationRequestUrl.searchParams.append(
  'nonce',
  '<nonce>'
);


// Optional: locale and region_country for market-aware login
// authorizationRequestUrl.searchParams.append('locale', 'fr-CA');
// authorizationRequestUrl.searchParams.append('region_country', 'CA');


// Public client
const verifier = await generateCodeVerifier();
const challenge = await generateCodeChallenge(verifier);
localStorage.setItem('code-verifier', verifier);


authorizationRequestUrl.searchParams.append(
  'code_challenge',
  challenge
);
authorizationRequestUrl.searchParams.append(
  'code_challenge_method',
  'S256'
);


window.location.href = authorizationRequestUrl.toString()
```

#### Retrieve code to get access token

When a customer successfully completes a login and is redirected to the uri specified in the parameters above, a `code` is received as a query parameter. The code will be utilized in the Obtain access token step and enables you to make requests to the Customer Account API.

The optional `state` parameter will also be returned if it was part of the original Authorization step above.

#### Obtain access token

To authenticate with the Customer Account API, your application needs to obtain an access token. You can request an access token by sending a `POST` request to the `token_endpoint` discovered from the OpenID configuration.

If in the Authorization step a `nonce` was passed, it can be validated using the Retrieving nonce step.

This will return a json result that contains the `access_token`, `refresh_token`, `id_token` and `expires_in` (in seconds) of the access token.

**Confidential client only:** Headers containing authorization credentials are required in order to get an access token. See the Authorization header section for more details.

Troubleshooting:
* If a response code of `301` is returned, ensure the correct `shop_id` is specified in the `POST` request.
* If a response code of `400` with a message of `invalid_grant` is returned, then ensure that padding is removed (for example, `=`) from your base64-encoded code challenge in the Authorization step. Additionally, make sure to replace "+" with "-" and "/" with "_" to ensure compatibility with URL encoding.
* If a response code of `401` with a message of `invalid_client` is returned, then verify that the `client_id` is correct.
* If a response code of `401` with a message of `invalid_token` in the `www-authenticate` header is returned, then ensure that an `origin` header is specified in the request. Verify that the `origin` header specified is set in the list of Javascript Origin(s) in the Customer Account API settings page.
* If a response code of `403` with a message of `You do not have permission to access this website` is returned, then ensure that a `user-agent` header is specified in the request.

With this access token, you can now make requests to the Customer Account API.

| Parameter | Value | Description |
|-----------|-------|-------------|
| **grant_type** | `authorization_code` | **Required.** Must be set to `authorization_code`. |
| **client_id** | `<client_id>` | **Required.** Same client_id used in the `authorize` request. |
| **redirect_uri** | `<redirect_uri>` | **Required.** Same redirect_uri specified in the first `/authorize` request. |
| **code** | `<code>` | **Required.** The `code` received as a parameter as part of the Retrieve code section. |

Public Client (additional parameter):

| Parameter | Value | Description |
|-----------|-------|-------------|
| **code_verifier** | `<code_verifier>` | **Required.** The `code_verifier` used to generate the `code_challenge` in the Authorization section. |

**Obtain Access Token:**

```ts
// First, discover the authentication endpoints
const discoveryResponse = await fetch(`https://${shopDomain}/.well-known/openid-configuration`);
const config = await discoveryResponse.json();


const clientId = process.env.CLIENT_ID;
const body = new URLSearchParams();


body.append('grant_type', 'authorization_code');
body.append('client_id', clientId);
body.append(
  'redirect_uri',
  `<redirect_uri>`,
);
body.append('code', code);


// Public Client
const codeVerifier = localStorage.getItem('code-verifier');
body.append('code_verifier', codeVerifier);


const headers = {
  'content-type': 'application/x-www-form-urlencoded',
  // Confidential Client
  'Authorization': 'Basic `<credentials>`'
}


// Use the discovered token_endpoint
const response = await fetch(config.token_endpoint, {
  method: 'POST',
  headers: headers,
  body,
});


interface AccessTokenResponse {
  access_token: string;
  expires_in: number;
  id_token: string;
  refresh_token: string;
}


const {access_token, expires_in, id_token, refresh_token} =
  await response.json<AccessTokenResponse>();
```

#### Use refresh token

The access token retrieved in the previous step has an associated `expires_in` property (in seconds). Once that has passed, the access token is invalid and needs to be refreshed.

The procedure to refresh the token is very similar to the Obtain access token step except different parameters are passed. To refresh your token, make a `POST` request to the `token_endpoint` from the discovery response:

| Parameter | Value | Description |
|-----------|-------|-------------|
| **grant_type** | `refresh_token` | **Required.** Must be set to `refresh_token`. |
| **client_id** | `<client_id>` | **Required.** Same client_id used in the `authorize` request. |
| **refresh_token** | `<refresh_token>` | **Required.** The `refresh_token` received as part of the Obtain access token step. |

**Refresh Token:**

```ts
// First, discover the authentication endpoints
const discoveryResponse = await fetch(`https://${shopDomain}/.well-known/openid-configuration`);
const config = await discoveryResponse.json();


const clientId = process.env.CLIENT_ID;
const body = new URLSearchParams();


body.append('grant_type', 'refresh_token');
body.append('client_id', clientId);
body.append('refresh_token', refresh_token);


const headers = {
  'content-type': 'application/x-www-form-urlencoded',
  // Confidential Client
  'Authorization': 'Basic `<credentials>`'
}


// Use the discovered token_endpoint
const response = await fetch(config.token_endpoint, {
  method: 'POST',
  headers: headers,
  body,
});


interface AccessTokenResponse {
  access_token: string;
  expires_in: number;
  id_token: string;
  refresh_token: string;
}


const {access_token, expires_in, refresh_token} =
  await response.json<Omit<AccessTokenResponse, 'id_token'>>();
```

#### Authorization header (confidential client only)

An Authorization Header is a Base64 encode of the `client_id` and `client_secret` and is required for certain requests.

```js
const clientId = process.env.CLIENT_ID;
const clientSecret = process.env.CLIENT_SECRET;


const credentials = btoa(`${clientId}:${clientSecret}`);
```

#### Code challenge and verifier (public client only)

A code challenge and verifier are needed when doing requests from a public client in order to verify that the client is the same client that initiated the authorization request.

```ts
export async function generateCodeVerifier() {
  const rando = generateRandomCode();
  return base64UrlEncode(rando);
}


export async function generateCodeChallenge(codeVerifier: string) {
  const digestOp = await crypto.subtle.digest(
    { name: "SHA-256" },
    new TextEncoder().encode(codeVerifier)
  );
  const hash = convertBufferToString(digestOp);
  return base64UrlEncode(hash);
}


function generateRandomCode() {
  const array = new Uint8Array(32);
  crypto.getRandomValues(array);
  return String.fromCharCode.apply(null, Array.from(array));
}


function base64UrlEncode(str: string) {
  const base64 = btoa(str);
  // This is to ensure that the encoding does not have +, /, or = characters in it.
  return base64.replace(/\+/g, "-").replace(/\//g, "_").replace(/=/g, "");
}


function convertBufferToString(hash: ArrayBuffer) {
  const uintArray = new Uint8Array(hash);
  const numberArray = Array.from(uintArray);
  return String.fromCharCode(...numberArray);
}
```

#### Generating state

The state parameter is used to maintain the state of the client application during the Authorization step. It acts as a security measure to prevent cross-site request forgery (CSRF) attacks. This `state` is then returned as a parameter in addition to the `code` in the Retrieve code step and can be used to verify that the response matches the request.

```ts
export async function generateState(): Promise<string> {
  const timestamp = Date.now().toString();
  const randomString = Math.random().toString(36).substring(2);
  return timestamp + randomString;
}
```

#### Generating nonce

A nonce (number used once) is a random or unique value used to prevent replay attacks. It can be provided in the Authorization step to ensure the freshness and integrity of the communication. Once passed as part of the Authorization step, it can be verified in the Obtain access token step.

```ts
export async function generateNonce(length: number) {
  const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  let nonce = '';


  for (let i = 0; i < length; i++) {
    const randomIndex = Math.floor(Math.random() * characters.length);
    nonce += characters.charAt(randomIndex);
  }


  return nonce;
}
```

#### Retrieving nonce

In the Obtain access token step an `id_token` is returned, this is an encoded JWT token that once decoded contains the nonce that was passed in the Authorization step.

```ts
export async function getNonce(token: string) {
  return decodeJwt(token).payload.nonce;
}


export function decodeJwt(token: string) {
  const [header, payload, signature] = token.split('.');


  const decodedHeader = JSON.parse(atob(header));
  const decodedPayload = JSON.parse(atob(payload));


  return {
    header: decodedHeader,
    payload: decodedPayload,
    signature,
  };
}
```

#### Logging out

To log out a customer, redirect them to the `end_session_endpoint` discovered from the OpenID configuration:

| Parameter | Value | Description |
|-----------|-------|-------------|
| **id_token_hint** | `<id_token>` | **Required.** The `id_token` received as part of the Obtain access token step. |
| **post_logout_redirect_uri** | `<post_logout_redirect_uri>` | **Required.** The URI to redirect to after logging out. If this isn't specified, then the uri to redirect to will to one of the URIs in the Logout URI setting. |

**Mobile client:** For mobile clients, the logout uri can be called as an API endpoint that returns a `200 OK` status code on successful logout, rather than performing a redirect. `id_token_hint` is still required.

#### Stay authenticated from Headless storefront to Checkout

There are two ways to authenticate the buyer in checkout:

* **The buyer identity on the cart**: Set a `customerAccessToken` on the cart via [`cartBuyerIdentityUpdate`](https://shopify.dev/docs/api/storefront/latest/mutations/cartBuyerIdentityUpdate), then redirect to [`checkoutUrl`](https://shopify.dev/docs/api/storefront/latest/objects/Cart#field-checkouturl). Checkout authenticates and authorizes the session for that specific cart.
* **Customer Accounts session authentication**: Append `sso=silent` to the `checkoutUrl` to verify the buyer's active session on the Customer Accounts domain via OIDC.

For detailed guidance, see [Authenticate buyers in checkout](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/checkout-authentication).

### Endpoints and queries

The Customer Account API is available only in GraphQL.

#### Discover API endpoints

Before making API requests, discover the GraphQL endpoint dynamically from the shop's storefront domain. The response contains `graphql_api` and `mcp_api` endpoints with the current API version already included.

```ts
const apiDiscoveryUrl = `https://${shopDomain}/.well-known/customer-account-api`;


const response = await fetch(apiDiscoveryUrl);
const apiConfig = await response.json();


// apiConfig contains:
// {
//   "graphql_api": "https://{shopDomain}/customer/api/{LATEST_API_VERSION}/graphql",
//   "mcp_api": "https://{shopDomain}/customer/api/mcp"
// }
// Note: URLs will use the shop's configured customer accounts domain,
// which may be a custom vanity domain instead of myshopify.com


// Use the discovered GraphQL endpoint directly (already includes version)
const graphqlEndpoint = apiConfig.graphql_api;
```

Like other Shopify APIs, the Customer Account API releases once a quarter. If you need a specific API version, then construct the [versioned URL](https://shopify.dev/docs/api/usage/versioning) from the discovered URL.

```
https://{shop-domain}/customer/api/2026-04/graphql
```

If this request responds with a `500`, then verify you don't have any misspelled parameters when obtaining the access token.

**Dynamic GraphQL Endpoint — Node.js:**

```js
// First discover the API endpoints
const apiDiscoveryResponse = await fetch(`https://${shopDomain}/.well-known/customer-account-api`);
const apiConfig = await apiDiscoveryResponse.json();

// Use the discovered endpoint directly
const graphqlEndpoint = apiConfig.graphql_api;

const response = await fetch(graphqlEndpoint, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    Authorization: {access_token},
  },
  body: JSON.stringify({
    operationName: 'SomeQuery',
    query: 'query { customer { emailAddress { emailAddress }}}',
    variables: {},
  }),
});
```

**cURL:**

```bash
# First discover the API endpoint
API_CONFIG=$(curl -s https://{shopDomain}/.well-known/customer-account-api)
GRAPHQL_ENDPOINT=$(echo $API_CONFIG | jq -r '.graphql_api')

# Use the discovered endpoint to make API calls (version already included)
curl -X POST \
  "${GRAPHQL_ENDPOINT}" \
  -H 'Content-Type: application/json' \
  -H 'Authorization: {access_token}' \
  -d '
  query {
    customer {
      emailAddress {
        emailAddress
      }
    }
  }
  '
```

### Directives

A directive provides a way for apps to describe additional options to the GraphQL executor. It lets GraphQL change the result of the query or mutation based on the additional information provided by the directive.

#### @inContext (Language)

In Customer Account API versions higher than 2025-04, the `@incontext` directive takes an optional language code argument and applies this to the query or mutation. This example shows how to return user errors that are translated into French `@incontext(language: FR)`.

```graphql
mutation customerAddressUpdate @inContext(language: FR){
  customerAddressUpdate(address: {phoneNumber: "invalid123"}, addressId: "gid://shopify/CustomerAddress/123456" ) {
    userErrors {
      code
      field
      message
    }
  }
}
```

Response:

```json
{
  "data": {
    "customerAddressUpdate": {
      "userErrors": [
        {
          "code": "PHONE_NUMBER_NOT_VALID",
          "field": null,
          "message": "Le numéro de téléphone n'est pas valide."
        }
      ]
    }
  },
  "extensions": {
    "context": {
      "country": "CA",
      "language": "FR"
    },
    "cost": {
      "requestedQueryCost": 10,
      "actualQueryCost": 10
    }
  }
}
```

### Rate limits

The Customer Account API is rate-limited using calculated query costs, measured in cost points. Each field returned by a query costs a set number of points. The total cost of a query is the sum of all the fields it returns, so more complex queries cost more to run.

This API limits each app to 7500 cost points per store and customer. This quota replenishes at a rate of either 100.0 or 200.0 cost points per second, depending on your plan.

Most fields cost 1 point. Most mutations cost 10 points. The best way to determine the true cost of a query is to run it. The API response includes information about the total query cost and the client's current quota under the extensions key. Include a `Shopify-GraphQL-Cost-Debug=1` header to receive a more detailed breakdown of the query cost.

Request:

```graphql
{
  customer {
    firstName
    lastName
  }
}
```

Throttled response:

```json
{
    "errors": [{
      "message": "Throttled",
      "extensions": {
        "code": "THROTTLED",
        "documentation": "https://shopify.dev/api/usage/limits#rate-limits"
      }
    }]
  }
```

### Status and error codes

All API queries return HTTP status codes that contain more information about the response.

#### 200 OK

GraphQL HTTP status codes are different from REST API status codes. Most importantly, the GraphQL API can return a `200 OK` response code in cases that would typically produce 4xx or 5xx errors in REST.

#### Error handling

The response for the errors object contains additional detail to help you debug your operation. The response for mutations contains additional detail to help debug your query. To access this, you must request `userErrors`.

Properties:

* **errors** (array) - A list of all errors returned
* **errors[n].message** (string) - Contains details about the error(s).
* **errors[n].extensions** (object) - Provides more information about the error(s) including properties and metadata.
* **extensions.code** (string) - Shows error codes common to Shopify. Additional error codes may also be shown.
  * **THROTTLED** - The client has exceeded the rate limit. Similar to 429 Too Many Requests.
  * **SHOP_INACTIVE** - The shop is not active. This can happen when stores repeatedly exceed API rate limits or due to fraud risk.
  * **INTERNAL_SERVER_ERROR** - Shopify experienced an internal error while processing the request. This error is returned instead of 500 Internal Server Error in most circumstances.

Sample 200 error responses — Throttled:

```json
{
  "errors": [
    {
      "message": "Throttled",
      "extensions": {
        "code": "THROTTLED",
        "documentation": "https://shopify.dev/api/usage/limits#rate-limits"
      }
    }
  ]
}
```

Internal:

```json
{
  "errors": [
    {
      "message": "Internal error. Looks like something went wrong on our end. Request ID: 1b355a21-7117-44c5-8d8b-8948082f40a8 (include this in support requests).",
      "extensions": {
        "code": "INTERNAL_SERVER_ERROR"
      }
    }
  ]
}
```

#### 4xx and 5xx status codes

The 4xx and 5xx errors occur infrequently. They are often related to network communications, your account, or an issue with Shopify's services. Many errors that would typically return a 4xx or 5xx status code return an HTTP 200 errors response instead.

* **400 Bad Request** — The server will not process the request.
* **401 Unauthorized** — The client does not have correct authentication credentials.
* **402 Payment Required** — The shop is frozen. The shop owner will need to pay the outstanding balance to unfreeze the shop.
* **403 Forbidden** — The shop is forbidden. Returned if the store has been marked as fraudulent.
* **404 Not Found** — The resource isn't available. This is often caused by querying for something that's been deleted.
* **423 Locked** — The shop isn't available. This can happen when stores repeatedly exceed API rate limits or due to fraud risk.
* **5xx Errors** — An internal error occurred in Shopify. Check the Shopify status page for more information.

Sample error codes:

```
HTTP/1.1 400 Bad Request
{
  "errors": {
    "query": "Required parameter missing or invalid"
  }
}
```

```
HTTP/1.1 401 Unauthorized
{
  "errors": "User does not have access"
}
```

```
HTTP/1.1 402 Payment Required
{
  "errors": "This shop's plan does not have access to this feature"
}
```

```
HTTP/1.1 403 Access Denied
{
  "errors": "User does not have access"
}
```

```
HTTP/1.1 404 Not Found
{
  "errors": "Not Found"
}
```

```
HTTP/1.1 423 Locked
{
  "errors": "This shop is unavailable"
}
```

```
HTTP/1.1 500 Internal Server Error
{
  "errors": "An unexpected error occurred"
}
```

---

## Building with the Customer Account API

> Fonte: https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api

The Customer Account API offers a secure way to access private customer-scoped data, enabling you to build personalized, customer-authenticated experiences in your custom storefronts or apps. You can access data including customers, orders, payments, fulfillment, discounts, refunds, and metafields.

### Benefits

The Customer Account API provides the following benefits:

* **Seamless authentication**: The hosted customer authentication system enables passwordless login for customers, allowing them to have a single sign-on experience across custom storefronts, online store, accounts, and checkout.
* **Data scoping**: The Customer Account API scopes data to each store and customer. This granular approach allows developers to build applications that cater to specific customer needs, offering personalized experiences and targeted marketing.
* **Enhanced security**: The Customer Account API requires authentication for each request and ensures that authorized applications can access sensitive customer information. This added layer of security protects both merchants and customers from unauthorized access and potential data breaches that could expose sensitive customer information.

### API versioning

The Customer Account API is versioned, with new releases four times a year. We strongly recommend updating your apps to make requests to the latest API version.

### Reference

[Customer Account API reference](https://shopify.dev/docs/api/customer) — Consult the Customer Account API reference for available objects, queries, and mutations.

### Next steps

* [Get started](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/getting-started) with the Customer Account API and learn how to query data.
* [Authenticate buyers in checkout](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/checkout-authentication) to carry buyer authentication from your headless storefront into checkout.
* [Build market-aware auth URLs](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/market-aware-auth-urls) for headless storefronts using `locale` and `region_country` parameters.

---

## Getting started with the Customer Account API

> Fonte: https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/getting-started

The Customer Account API is a GraphQL API that requires an access token associated with a specific customer. You can call the API from any HTTP client, including mobile clients. This guide shows you how to get started building unique customer experiences with the Customer Account API.

### What you'll learn

In this tutorial, you'll learn how to do the following tasks:

* Enable customer accounts.
* Configure Customer Account API access on the Headless and Hydrogen sales channels.
* Perform authorization requests and make queries.
* Rotate credentials.

### Requirements

* You have **Apps and channels** permissions on the Shopify store that you're working with.
* You have installed the [Headless](https://apps.shopify.com/headless) or [Hydrogen](https://apps.shopify.com/hydrogen) sales channel from the Shopify App Store.

### Step 1: Enable customer accounts

Shopify's customer accounts feature is required to use the Customer Account API. Customer accounts allow you to seamlessly persist customer logins across online store, Hydrogen, and checkout.

1. From your Shopify admin, click **Settings**.
2. Click **Customer accounts**.
3. Under **Accounts in online store and checkout** section, click on **Edit**.
4. Choose **Customer accounts**.
5. Click **Save**.

### Step 2: Configure Customer Account API access

To use the Customer Account API, you first need to enable it and get your access credentials.

1. From your Shopify admin, under **Sales channels**, click **Headless** or **Hydrogen**.
2. Select your storefront.
3. Complete one of the following steps:
   * If you selected **Headless**, then navigate to **Customer Account API settings**.
   * If you selected **Hydrogen**, then navigate to **Storefront settings**.
4. Optional: Modify the client type.
   * **Public clients**: For applications that are strictly client-side, or that don't have a server-side session where they can store the refresh token safely, for example, SPA, mobile applications, or Hydrogen.
   * **Web clients**: Suitable for web applications where the client-side environment is the primary interface for user interactions.
   * **Mobile clients**: Designed for mobile applications that require access to the API and don't have a server-side session for securely storing refresh tokens, for example, iOS and Android.
   * **Confidential clients**: For applications that have a back-end to perform the authorization request and a server-side session to hold the refresh token, for example, Express.js, ASP.NET, or Rails.
5. From the **Credentials** section, copy the client ID (and client secret, if applicable) to use in your requests.
6. From the **Permissions** section, verify that the right permission controls are set for your custom storefront.
7. Under **Application endpoints**, record the Authorization, Token, and Logout endpoints to be used in your requests.
8. In the **Application setup** section, specify the following client application settings:
   * **Callback URL(s)**: The allowable list of URLs to redirect to after logging in.
     * **Web applications**: Callback URLs must be in the HTTPS scheme to ensure security.
     * **Mobile applications**: Callback URLs must use the custom scheme `shop.{shop_id}.*` to make the scheme universally unique in accordance with Shopify's mobile application authorization standards.
   * **Javascript origins**: Specifies the origins that are allowed to use a client's OAuth credentials in a JavaScript application. Applies specifically to web-type public clients.
   * **Logout URL** (Optional): The URL to redirect to after logging out. This setting is not applicable to mobile public clients. For mobile clients, a successful logout returns a success message. Following this, any subsequent actions, such as navigating to a specific screen or displaying a confirmation message, are determined by the specific behaviors programmed into the mobile application.

> **Note:** Shopify doesn't support the use of `localhost` or any `http` based URL due to security concerns. For development purposes, we recommend using a tunnelling service, such as [ngrok](https://ngrok.com/).

### Step 3: Perform authorization requests and make queries

To authenticate and use the Customer Account API, the OAuth 2.0 authorization specification needs to be implemented by the client.

#### Authorize

Begin the flow by redirecting a user to the Authorization endpoint (recorded in Step 2 above) and specify the following required parameters:

* `scope`: Determine what data the access token will be able to retrieve from the API endpoints.
* `client_id`: Recorded from Step 2 above.
* `response_type`: Set to `code` to specify the authorization code flow.
* `redirect_uri`: Specify one of the callback URLs defined in Step 2 above.
* `state`: A string of characters which will be returned along with the code during callback/redirect.

In addition to the parameters above, public clients need to implement a code challenge and verifier and specify the `code_challenge` which is a string derived from the `code_verifier` using a hashing algorithm and the `code_challenge_method` defining the type of hashing algorithm used (ie. S256).

You can also pass optional `locale` and `region_country` parameters for a market-aware login experience.

#### Obtain token

To obtain an access token, the client must make a `POST` request to the Token endpoint specified in Step 2 above, including the following required parameters:

* `grant_type`: Set to `authorization_code`.
* `client_id`: The same `client_id` as used in the Authorize step.
* `code`: The authorization code received in the Authorize step.
* `redirect_uri`: The same URL specified in the Authorize step.

Confidential clients are required to send their `client_id` and `client_secret` in the Authorization header.

If successful, the client will receive an access token. More details on the Obtain access token step can be found in the reference guide.

#### Call the API

After you've completed the OAuth 2.0 authorization flow for the Customer Account API and you have received a token from a logged-in customer, you can now make queries using the Customer Account API.

For an example of how to use the Customer Account API with a Hydrogen storefront, refer to the Using Customer Account API with Hydrogen tutorial and consult the Customer Account API reference for available objects, queries, and mutations.

> **Note:** To streamline development, there are multiple OAuth libraries available in a variety of different languages.

### Rotate credentials

> **Caution:** After you revoke your old credentials, you need to update any applications or scripts that use these credentials, or else you won't be able to access the Customer Account API. Revoking credentials can't be undone.

1. In the **Credentials** section, under **Rotate credentials**, click **Generate new credentials**.
2. Update any applications or scripts with the new credentials. The old credentials remain valid until you revoke them.
3. When all applications or scripts have been updated, click **Revoke** next to the old credentials.
4. When prompted, click **Revoke credentials**.

### Next steps

* Follow the Using Customer Account API with Hydrogen tutorial.
* Learn more about the Customer Account API.

---

## Using the Customer Account API with Hydrogen

> Fonte: https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen

This tutorial shows how to create a login button on a Hydrogen storefront that lets a customer authenticate using the Customer Account API. If the login succeeds, then the site displays a welcome message with their email address.

### What you'll learn

After you've completed this tutorial, you'll be able to authenticate a Customer and make Customer Account API queries within a Hydrogen storefront.

### Requirements

* You have completed the Getting started with the Customer Account API guide.
* You have completed Getting started with Hydrogen guide.
* You've installed the Hydrogen or Headless sales channel.

### Limitations

* Multipass currently doesn't support the Customer Account API. If you require single sign-on from an external website in your storefront, then you should use the code in our multipass example, which uses the legacy customer account flow.
* mock.shop, which provides example product data, doesn't support the Customer Account API. You must use a production store's credentials to work with the Customer Account API.

### Step 1: Set up a public domain for local development

Customer Account API authentication doesn't support the use of `localhost` due to security concerns. For development purposes, use a tunnelling service, such as ngrok. In this step, you'll learn how to use ngrok to set up a public HTTPS domain that connects to your local Hydrogen application.

#### Set up ngrok

Install and run ngrok in your development environment.

1. Set up an ngrok account.
2. In your ngrok settings, add a static domain.
3. Install the ngrok CLI.
4. In a terminal, start ngrok using the following command:

```sh
ngrok http --domain=<your-ngrok-domain> 3000
```

#### Add your ngrok domain to the content security policy

Modify your Hydrogen app's content security policy to allow the development domain as a `connect-src`. Your content security policy is typically located in `/app/entry.server.tsx`.

```js
import {createContentSecurityPolicy} from '@shopify/hydrogen';

createContentSecurityPolicy({
  connectSrc: [
    // (ie. 'wss://<your-ngrok-domain>.app:*')
    'wss://<your-tunneled-host>:*',
  ],
});
```

### Step 2: Set up the environment

Configure the necessary Customer Account API settings in the Shopify admin so you can send the initial authentication request to Shopify.

#### Open the Customer Account API settings

1. In the Shopify admin, open the **Hydrogen** sales channel.
2. Click the storefront you're adding the customer account API functionality for.
3. Click **Storefront settings**.
4. Click **Customer Account API** to open the API settings.

#### Update the application setup

For the Customer Account API to recognize your domain as a valid authentication host, edit your Customer Account API settings.

1. Under **Application setup**, click **Edit** `✎` to edit the endpoints.
2. Under **Callback URI(s)**, click **Add Callback URI**, and add your ngrok domain, with `/account/authorize` appended:

   ```sh
   https://<your-ngrok-domain>.app/account/authorize
   ```

   This is the URI your application will redirect to to continue the OAuth process after a successful customer login.
3. Under **JavaScript origin(s)**, click **Add origin**, and then add your ngrok domain.
4. Under **Logout URI**, click **Add Logout URI**, and then add your ngrok domain.

> **Tip:** If you don't see **JavaScript origin(s)** and **Logout URI** options, you'll need to switch to a **Public** client type. You can find this option at the top of the **Customer Account API** settings.

#### Set up the environment variables

There is only one environment variable needed to set up Customer Account API in your application:

**`PUBLIC_CUSTOMER_ACCOUNT_API_CLIENT_ID`**: A token that represents a client used in all authentication requests. You can retrieve the token by navigating to the **Customer Account API** settings page > **Customer Account API Credentials**.

**Production storefront:** When deploying to Oxygen, these variables are automatically created and used in your production environment.

**Local development:** When developing Hydrogen locally, store your environment variables in an `.env` file. You can automatically download the required variables with Shopify CLI:

1. Run `npx shopify hydrogen link` in your Hydrogen project to link it to your Shopify store.
2. Run `npx shopify hydrogen env pull` to download your environment variables and write them to your local `.env` file.

### Step 3: Create the Customer Account API client

> **Note:** The Skeleton template version 2024.7.5 and higher has a Customer Account API client by default and you can skip this step. Check `package.json` to see your Skeleton template version.

If you need to manually create a Customer Account API client, then complete the following steps: create a new Customer Account API client in your `server` file using the `createCustomerAccountClient` utility. Pass the new client to `createCartHandler` to ensure that the logged-in customer is persisted from your store through to checkout. Pass the new client to the application's `context` so the utility can be accessed throughout the application.

> **Note:** The Customer Account API client uses the latest version of the API by default. If you need to use a specific version, then you can specify the version when you create the client.

JavaScript:

```jsx
import * as remixBuild from '@remix-run/dev/server-build';
import {
  createCartHandler,
  storefrontRedirect,
  createCustomerAccountClient,
} from '@shopify/hydrogen';
import {
  createRequestHandler,
} from '@shopify/remix-oxygen';
import {AppSession} from '~/lib/session';

export default {
  async fetch(
    request,
    env,
    executionContext,
  ) {
    try {
      const waitUntil = executionContext.waitUntil.bind(executionContext);
      const session = await AppSession.init(request, [env.SESSION_SECRET]);

      const customerAccount = createCustomerAccountClient({
        waitUntil,
        request,
        session,
        customerAccountId: env.PUBLIC_CUSTOMER_ACCOUNT_API_CLIENT_ID,
        shopId: env.SHOP_ID,
      });

      const cart = createCartHandler({
        customerAccount,
        // additional options here
      });

      const handleRequest = createRequestHandler({
        getLoadContext: () => ({
          customerAccount,
        }),
        // additional options here
      });

      const response = await handleRequest(request);

      if (response.status === 404) {
        return storefrontRedirect({request, response, storefront});
      }

      return response;
    } catch (error) {
      console.error(error);
      return new Response('An unexpected error occurred', {status: 500});
    }
  },
};
```

TypeScript:

```tsx
import * as remixBuild from '@remix-run/dev/server-build';
import {
  createCartHandler,
  storefrontRedirect,
  createCustomerAccountClient,
} from '@shopify/hydrogen';
import {
  createRequestHandler,
  type AppLoadContext,
} from '@shopify/remix-oxygen';
import {AppSession} from '~/lib/session';

export default {
  async fetch(
    request: Request,
    env: Env,
    executionContext: ExecutionContext,
  ): Promise<Response> {
    try {
      const waitUntil = executionContext.waitUntil.bind(executionContext);
      const session = await AppSession.init(request, [env.SESSION_SECRET]);

      const customerAccount = createCustomerAccountClient({
        waitUntil,
        request,
        session,
        customerAccountId: env.PUBLIC_CUSTOMER_ACCOUNT_API_CLIENT_ID,
        shopId: env.SHOP_ID,
      });

      const cart = createCartHandler({
        customerAccount,
        // additional options here
      });

      const handleRequest = createRequestHandler({
        getLoadContext: () => ({
          customerAccount,
        }),
        // additional options here
      });

      const response = await handleRequest(request);

      if (response.status === 404) {
        return storefrontRedirect({request, response, storefront});
      }

      return response;
    } catch (error) {
      console.error(error);
      return new Response('An unexpected error occurred', {status: 500});
    }
  },
};
```

`createCustomerAccountClient` expects a session, implemented based on `HydrogenSession`, to persist auth tokens and the customer's logged-in state. You can view an example of a Hydrogen session in the Hydrogen GitHub repo.

### Step 4: Create auth routes

Your application requires three routes for customer login and logout operations. The default routes are as follows:

* `/account/login`: A route that redirects the user to a Shopify login.
* `/account/authorize`: A route that authorizes the customer after they log in.
* `/account/logout`: A route that logs the customer out.

> **Tip:** If you chose to scaffold routes when creating your app, then your app already has the required routes in place. To generate a set of standard routes, including basic account-related functionality, run `npx shopify hydrogen setup`.

#### Create the login route

1. In the `routes` folder, create a new file called `account_.login.[js|ts]`.
2. In the new file, add the `context.customerAccount.login()` function in the loader.

This function is responsible for redirecting users to Shopify to log in. To display the login screen in a specific language or market context, pass `locale` and `countryCode` options to `context.customerAccount.login()`. The SDK maps `countryCode` to the `region_country` URL parameter internally.

JavaScript:

```jsx
export async function loader({context}) {
  return context.customerAccount.login();
}
```

TypeScript:

```tsx
import type {LoaderFunctionArgs} from '@shopify/remix-oxygen';

export async function loader({context}: LoaderFunctionArgs) {
  return context.customerAccount.login();
}
```

Note the use of underscore in `account_.login.ts`. This is to ensure that no layout is rendered when this route is accessed.

> **Tip:** If you need to override the default behavior or change the login route location, then you can implement a `customAuthStatusHandler`.

#### Create the authorization route

1. In the `routes` folder, create a new file called `account_.authorize.[js|ts]`.
2. In the new file, add the `context.customerAccount.authorize()` function in the loader.

After a successful login, Shopify redirects to this authorize route. It continues the OAuth process, exchanges the access token, and persists the result to your application session. If you choose to place this route somewhere else in the application, then use the `authUrl` option with a relative url, and add the full public domain auth path in the Callback URI of the Customer Account API application setup.

JavaScript:

```jsx
export async function loader({context}) {
  return context.customerAccount.authorize();
}
```

TypeScript:

```tsx
import type {LoaderFunctionArgs} from '@shopify/remix-oxygen';

export async function loader({context}: LoaderFunctionArgs) {
  return context.customerAccount.authorize();
}
```

At the end of this authorization step, the application redirects back to the page that initiated the login. Use the `customAuthStatusHandler` option to change this behavior.

#### Create the logout route

1. In the `routes` folder, create a new file called `account_.logout.[js|ts]`.
2. In the new file, add the `context.customerAccount.logout()` function in the action. Avoid including this function in the loader.

The logout action should be triggered by a user event, like clicking a logout button, not when a component is being loaded that can occur by page load or prefetching.

JavaScript:

```jsx
export async function action({context}) {
  return context.customerAccount.logout();
}
```

TypeScript:

```tsx
import {type ActionFunctionArgs} from '@shopify/remix-oxygen';

export async function action({context}: ActionFunctionArgs) {
  return context.customerAccount.logout();
}
```

You can set up a redirect that takes place after the logout step using the `admin` setting in the application setup step.

### Step 5: Query the Customer Account API

After you've set up your auth routes, you can start querying the Customer Account API. In this step, you'll create a new `account` route that queries for a logged in customer's first and last name.

1. In the `routes` folder, create a new file called `account.[jsx|tsx]`.
2. Add the following code. This code fetches the customer's first and last name from their account. If the customer isn't logged in, calling `query()` will trigger an automatic redirect to the login page, and redirect back to current page at the end of the auth process.

JavaScript:

```jsx
import {Form, useLoaderData} from '@remix-run/react';
import {json} from '@shopify/remix-oxygen';

export async function loader({context}) {
  const {data, errors} = await context.customerAccount.query(`#graphql
      query getCustomer {
        customer {
          firstName
          lastName
        }
      }
      `);

  if (errors?.length || !data?.customer) {
    throw new Error('Customer not found');
  }

  return json(
    {customer: data.customer},
    {
      headers: {
        'Cache-Control': 'no-cache, no-store, must-revalidate',
        'Set-Cookie': await context.session.commit(),
      },
    },
  );
}

export default function () {
  const {customer} = useLoaderData();

  return customer ? (
    <>
      <b>
        Welcome {customer.firstName} {customer.lastName}
      </b>
      <Form method="post" action="/logout">
        <button>Logout</button>
      </Form>
    </>
  ) : null;
}
```

TypeScript:

```tsx
import {Form, useLoaderData} from '@remix-run/react';
import {type LoaderFunctionArgs, json} from '@shopify/remix-oxygen';

export async function loader({context}: LoaderFunctionArgs) {
  const {data, errors} = await context.customerAccount.query<{
      customer: {firstName: string; lastName: string};
    }>(`#graphql
      query getCustomer {
        customer {
          firstName
          lastName
        }
      }
      `);

  if (errors?.length || !data?.customer) {
    throw new Error('Customer not found');
  }

  return json(
    {customer: data.customer},
    {
      headers: {
        'Cache-Control': 'no-cache, no-store, must-revalidate',
        'Set-Cookie': await context.session.commit(),
      },
    },
  );
}

export default function () {
  const {customer} = useLoaderData<typeof loader>();

  return customer ? (
    <>
      <b>
        Welcome {customer.firstName} {customer.lastName}
      </b>
      <Form method="post" action="/logout">
        <button>Logout</button>
      </Form>
    </>
  ) : null;
}
```

> **Tip:** You need to commit the session at the end of a loader/action with any customer logged in check. A logged in check can trigger an access token refresh, which won't persist in your application unless session is committed to the `Set-Cookie` header.

The `query` and `mutate` functions follow GraphQL standards and return both `data` and `errors` objects. The `errors` object typically returns GraphQL errors such as a syntax error for querying for unknown field name. Most of the time, the existence of the `errors` object means that the query isn't successful and there is nothing to show. However, during a mutation, it is possible to receive partial data while still experiencing errors. You should always handle errors gracefully, either by showing a message to the user, or re-throwing them for your application's `ErrorBoundary` to catch.

> **Warning:** Never cache Customer Account API data or store personally identifiable information (PII). Caching this type of data causes risk of unauthorized access or data breaches, compromising user privacy and security. If you use the Storefront API `customer` query, you must also explicitly disable subrequest and full-page caching to prevent personal data from being served to other users.

### Step 6: Check the customer logged in state

You can check whether a visitor is logged in without triggering an automatic login redirect. For instance, you might want to conditionally display a **Log in** or **Account details** link in a menu.

1. In the root file of your application, add `customerAccount.isLoggedIn()` in the loader.
2. Return this promise using Remix's deferred data loading pattern. This allows the user interface to render before the login check is complete.

Note that you need to `commit()` the session at the end of any loader or action that checks a customer's logged-in state.

JavaScript:

```jsx
import {defer} from '@shopify/remix-oxygen';
import {Await, NavLink, useLoaderData} from '@remix-run/react';
import {Suspense} from 'react';

export async function loader({context}) {
  const isLoggedInPromise = context.customerAccount.isLoggedIn();

  return defer(
    {isLoggedInPromise},
    {
      headers: {
        'Set-Cookie': await context.session.commit(),
      },
    },
  );
}

export default function App() {
  const {isLoggedInPromise} = useLoaderData();

  return (
    <html lang="en">
      <body>
        <header className="header">
          <NavLink prefetch="intent" to="/account">
            <Suspense fallback="Sign in">
              <Await resolve={isLoggedInPromise} errorElement="Sign in">
                {(isLoggedIn) => (isLoggedIn ? 'Account' : 'Sign in')}
              </Await>
            </Suspense>
          </NavLink>
        </header>
        {/* Rest of the application */}
      </body>
    </html>
  );
}
```

TypeScript:

```tsx
import {defer, type LoaderFunctionArgs} from '@shopify/remix-oxygen';
import {Await, NavLink, useLoaderData} from '@remix-run/react';
import {Suspense} from 'react';

export async function loader({context}: LoaderFunctionArgs) {
  const isLoggedInPromise = customerAccount.isLoggedIn();

  return defer(
    {isLoggedInPromise},
    {
      headers: {
        'Set-Cookie': await context.session.commit(),
      },
    },
  );
}

export default function App() {
  const {isLoggedInPromise} = useLoaderData<typeof loader>();

  return (
    <html lang="en">
      <body>
        <header className="header">
          <NavLink prefetch="intent" to="/account">
            <Suspense fallback="Sign in">
              <Await resolve={isLoggedInPromise} errorElement="Sign in">
                {(isLoggedIn) => (isLoggedIn ? 'Account' : 'Sign in')}
              </Await>
            </Suspense>
          </NavLink>
        </header>
        {/* Rest of the application */}
      </body>
    </html>
  );
}
```

### Step 7: Associate a customer with a cart

You can associate a customer with a cart by obtaining a Storefront API `CustomerAccessToken`.

1. Update the Customer Account API client to use the `unstableB2b` option.

   ```js
   const hydrogenContext = createHydrogenContext({
     ...,
     customerAccount: {
       unstableB2b: true,
     },
   });
   ```

2. Access the `CustomerAccessToken` and pass it to the `cart.updateBuyerIdentity` function.

   ```js
   export async function action({context}) {
     const {cart, customerAccount} = context;
     const buyer = await customerAccount.UNSTABLE_getBuyer();

     await cart.updateBuyerIdentity({
       customerAccessToken: buyer.customerAccessToken,
     })
   }
   ```

> **Note:** The `CustomerAccessToken` returned by Customer Account Client can only be used to update the buyer identity of a cart. It cannot be used with a Storefront API `customer` query.

### Next steps

* Explore the GraphQL Customer Account API reference.
* Explore the `createCustomerAccountClient` reference, including additional examples.
* Explore an end-to-end Customer Account API implementation example in the default Hydrogen template.
* Learn how to Manage customer accounts with the Customer Account API.

---

## Authenticate Customers with the Customer Account API (app, OAuth + PKCE)

> Fonte: https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/authenticate-customers
>
> Nota di estrazione: lo strumento di fetch ha restituito questa pagina in forma riassunta anziché verbatim. Il contenuto seguente riflette fedelmente i punti della guida ma i blocchi di codice completi non erano disponibili nella risposta; consultare la pagina sorgente per il codice integrale.

### Overview

This tutorial demonstrates building an OAuth 2.0 authentication flow with PKCE to securely log customers into your app and query their account data through the Customer Account API.

### Key Learning Objectives

The tutorial teaches how to:

* Implement customer authentication using the Customer Account API
* Securely store authentication tokens in a database
* Query the `Customer` object from the Customer Account API

### Prerequisites

* Partner account
* Development store with test data
* Latest Shopify CLI version
* Scaffolded React Router app
* Access to Protected Customer Data (Level 2) for first name, last name, and email fields

### Database Schema Setup

Two Prisma models store OAuth flow data:

* **CodeVerifier** — Temporary storage for PKCE values and state tokens
* **CustomerAccessToken** — Persistent storage for customer access tokens with expiration tracking

Migration command:

```bash
npx prisma migrate dev --name add_code_verifier_access_token
```

### App Configuration

The `shopify.app.toml` file requires:

* Access scopes: `customer_read_orders,customer_read_customers`
* Customer authentication redirect URI pointing to callback endpoint
* HTTPS tunnel URL (ngrok recommended for local development)

### OAuth Flow Implementation

**Authorization Route** — The `/customer-account-api/auth` endpoint:

* Fetches OpenID configuration dynamically from the shop's well-known endpoint
* Generates PKCE security parameters (code verifier, code challenge, state)
* Stores the code verifier in database for later retrieval
* Constructs authorization URL with required OAuth parameters
* Redirects customer to Shopify's login page

PKCE helper functions generate cryptographically secure values using SHA256 hashing.

**Callback Handler** — The `/customer-account-api/callback` endpoint:

* Extracts authorization code and state from callback URL
* Validates state matches original value (CSRF protection)
* Retrieves stored code verifier from database
* Exchanges authorization code for access token via token endpoint
* Stores access token with expiration time in database
* Deletes used code verifier to prevent replay attacks
* Sets session cookie with token ID
* Redirects to authenticated page

### Session Management

Cookie-based session storage persists customer login state:

* HTTP-only, encrypted cookies prevent client-side access
* 1-hour maximum age
* SameSite lax attribute
* Secure flag in production environments

Helper functions manage getting, setting, and destroying customer sessions.

### Customer Data Queries

The `/customer-account-api/order-list` endpoint:

* Retrieves customer token ID from session cookie
* Fetches access token from database
* Verifies token hasn't expired
* Discovers GraphQL endpoint dynamically
* Sends authenticated GraphQL query with Bearer token
* Displays customer information and orders

### Troubleshooting Common Issues

| Issue | Solution |
|-------|----------|
| Invalid client_id | Verify client_id matches shopify.app.toml configuration |
| Invalid redirect_uri | Ensure [customer_authentication] module exists in config with HTTPS tunnel URL |
| Invalid client credentials | Confirm test shop matches SHOP_STOREFRONT_DOMAIN environment variable |
| Customer name not displayed | Request Protected Customer Data access for name and email fields in Dev Dashboard |

### Preview and Testing

```bash
shopify app dev --tunnel-url=https://<your-tunnel-url>:3000
```

Navigate to `https://<your-tunnel-url>/customer-account-api/auth` to initiate the authentication flow. After login, the app redirects to an order list displaying customer data retrieved from the Customer Account API.

### Security Considerations

* PKCE prevents authorization code interception attacks
* State parameter prevents CSRF attacks
* Access tokens stored server-side with expiration tracking
* Code verifiers deleted after single use
* Encrypted HTTP-only cookies prevent XSS token theft
* OpenID discovery prevents hardcoded endpoint dependencies

---

# Parte 5 — Storefront API usage (guides)

How-to guides for querying the Storefront API: products & collections, cart, metafields, and pagination. (The full GraphQL schema is referenced but not extracted.)

Mini-TOC:
- Products and Collections (overview)
- Getting started with querying products and collections
- Create and update a cart with the Storefront API
- Retrieve metafields with the Storefront API
- Pagination (Paginating results with GraphQL)

## Products and Collections (overview)

> Fonte: https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/products-collections

A product represents an individual item for sale in a Shopify store. A collection represents a grouping of products that a shop owner can create to organize them or make their shops easier to browse.

This guide introduces the ways that you can configure products and collections using the GraphQL Storefront API.

### How it works

You can use the Storefront API to complete the following tasks related to products and collections:

* Filter products in a collection
* Retrieve metafields from different resources
* Support local pickup on storefronts
* Manage subscription products on storefronts

> **Tip:** If you're new to the Storefront API, then you can get started by learning how to query products and collections.

### Product filtering

You can use the Storefront API to filter products in a collection. This functionality lets you build a desired customer experience on a storefront, such as the ability to narrow down the search results that you display to customers. For example, you might want to filter products in a collection based on product type, vendor, variant options, price, and whether the product is in stock.

### Metafields

You can retrieve metafields with the Storefront API to access additional information from different types of resources.

By default, the Storefront API can't read metafields. To expose specific metafields to the Storefront API, you need to use the GraphQL Admin API. For each metafield that you want to expose, you need to create a `MetafieldStorefrontVisibility` record. Each `MetafieldStorefrontVisibility` record exposes all metafields that belong to the specified resource and have a specified `namespace` and `key` combination.

#### Retrieving metafields

You can retrieve metafields on the following resources with the Storefront API:

| Resource | Description |
| - | - |
| Article | An article in an online store blog. |
| Blog | An online store blog. |
| Collection | A grouping of products. |
| Customer | A customer account with the store. Customer accounts store contact information for the customer, saving logged-in customers the trouble of having to provide it at every checkout. |
| Order | A customer's request to purchase one or more products from a store. |
| Page | A page to hold static HTML content. Each `Page` object represents a custom page on the online store. |
| Product | An individual item for sale in a Shopify store. |
| ProductVariant | A different version of a product, such as differing sizes or differing colors. |
| Shop | A collection of the general settings and information about a store. |

#### Hiding metafields

After you've exposed metafields with the GraphQL Admin API, and retrieved them with the Storefront API, you can hide metafields from the Storefront API again if you no longer need to access them. For example, you could hide all product metafields that have namespace `testapp` and the key `pizza-size-inches` from the Storefront API.

### Local pickup

You can display a product's availability for local pickup using the following API components:

* **`storeAvailability`**: An object that represents a product variant's availability for in-store pickup at a location, including the estimated amount of time that it takes for the pickup to be ready. `StoreAvailability` is a connection field on the `ProductVariant` object.
* **`Location`**: An object that represents a physical location, including the location's name, address, and latitude and longitude coordinates.
* **`@inContext`**: A directive that provides the ability to contextualize the response. For example, the `@inContext` directive accepts a `preferredLocationId` argument which effects how in-store availability results are sorted.

### Subscription products

You can use the Storefront API to retrieve subscription products on a storefront. Subscription products can be accessed from the `sellingPlan` object.

Selling plans represent how products and variants can be sold and purchased. A selling plan group contains selling plans and represents a selling method. For example, "Subscribe and save" is a selling method where customers pay for goods or services per delivery.

When a customer makes a purchase on a storefront, they're buying a variant. Each variant is associated with a price. The variant's price can be adjusted based on an applied fixed or percentage discount, and whether it's purchased with a selling plan. A selling plan allocation associates a variant with a selling plan. Selling plan allocations describe which selling plans are available for each variant, and what their impact is on pricing.

### Next steps

* Get started by querying products and collections.
* Explore the GraphQL Storefront API reference.

---

## Getting started with querying products and collections

> Fonte: https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/products-collections/getting-started

The Storefront API provides GraphQL access to build custom storefronts. After obtaining access tokens, you can query products, collections, and other store resources.

### What you'll learn

This tutorial covers:

* Requesting public, unauthenticated Storefront API access scopes
* Generating a Storefront API access token
* Querying products and collections

> **Tip:** Shopify Partners can create a development store to test Storefront API queries.

### Requirements

* Completion of the Getting started with the Storefront API guide
* Alternatively: a public or custom app with Storefront API enabled
* Products, product variants, and collections created in your store

### Query products

Use the `products` query to retrieve product lists. This example queries the first 5 product IDs.

**POST** `https://{shop}.myshopify.com/api/{api_version}/graphql.json`

```graphql
{
  products(first:5) {
    edges {
      node {
        id
      }
    }
  }
}
```

Response:

```json
{
  "data": {
    "products": {
      "edges": [
        { "node": { "id": "gid://shopify/Product/1" } },
        { "node": { "id": "gid://shopify/Product/2" } },
        { "node": { "id": "gid://shopify/Product/3" } },
        { "node": { "id": "gid://shopify/Product/4" } },
        { "node": { "id": "gid://shopify/Product/5" } }
      ]
    }
  }
}
```

### Query a single product

Products use globally unique IDs for identification. Use the `product` query with an ID or handle:

```graphql
{
  # You can use `product(handle:)` to query a single product by its handle instead.
  product(id: "gid://shopify/Product/1") {
    title
  }
}
```

Response:

```json
{
  "data": {
    "product": {
      "title": "Black Ban Glasses"
    }
  }
}
```

### Query product variants

Product variants represent different versions (sizes, colors, etc.). Query variants on the Product object:

```graphql
{
  node(id: "gid://shopify/Product/1") {
    id
    ... on Product {
      variants(first: 5) {
        edges {
          node {
            id
          }
        }
      }
    }
  }
}
```

### Query product recommendations

Product recommendations boost sales and conversions. Use `productRecommendations` with:

* `productId`: The global ID of the published product
* `intent`: The recommendation type for different storefront surfaces

```graphql
{
  # The `intent` argument is available only in the unstable API version.
  productRecommendations(productId: "gid://shopify/Product/1", intent: RELATED) {
    id
  }
}
```

> **Note:** Shopify provides auto-generated product recommendations, and merchants can customize them using the Shopify Search & Discovery app.

### Query product media

Query product media using the `media` field on the Product object and fragments for different media types:

```graphql
{
  product(id: "gid://shopify/ProductVariant/1") {
    id
    media(first: 10) {
      edges {
        node {
          mediaContentType
          alt
          ...mediaFieldsByType
        }
      }
    }
  }
}
fragment mediaFieldsByType on Media {
  ...on ExternalVideo {
    id
    embeddedUrl
  }
  ...on MediaImage {
    image {
      url
    }
  }
  ...on Model3d {
    sources {
      url
      mimeType
      format
      filesize
    }
  }
  ...on Video {
    sources {
      url
      mimeType
      format
      height
      width
    }
  }
}
```

### Query collections

Collections group products for organization. Merchants create them manually or with automated rules.

```graphql
{
  collections(first: 2) {
    edges {
      node {
        id
        products(first: 5) {
          edges {
            node {
              id
            }
          }
        }
      }
    }
  }
}
```

### Next steps

Explore additional capabilities with the Storefront API, including filtering and cart management.

---

## Create and update a cart with the Storefront API

> Fonte: https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/cart/manage

A cart contains the merchandise that a customer intends to purchase, and the estimated cost associated with the cart. You can use the [Storefront API](https://shopify.dev/docs/api/storefront) to interact with a cart during a customer's session.

This guide shows how to create a cart and retrieve it, update cart line items and customer information, and retrieve a checkout URL.

### Requirements

* You've completed the [Getting started with the Storefront API](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/getting-started) guide.
* You've created products and product variants in your store.
* You're using version 2022-10 or higher of the Storefront API. To set metafields on a cart, you need to use version 2023-04 or higher of the Storefront API.

### Cart object relationships

Before you start building a cart, we recommend familiarizing yourself with the following API objects and their relationships:

| Object | Description |
| - | - |
| [Cart](https://shopify.dev/docs/api/storefront/latest/objects/Cart) | An object that contains the merchandise that a customer intends to purchase. |
| [CartBuyerIdentity](https://shopify.dev/docs/api/storefront/latest/objects/CartBuyerIdentity) | Identifies the customer that is interacting with the cart. It includes a customer access token that associates the customer with the cart, and a set of preferences that can be used to prefill a checkout session. |
| [Cost](https://shopify.dev/docs/api/storefront/latest/objects/CartCost) | The estimated costs that the customer will pay at checkout. The costs are subject to change and changes display at checkout. Merchants can configure the prices of products on a per country basis in their Shopify admin. The prices that display on a storefront are determined by checkout pricing (final sale price), cart pricing (estimated final sale price via `CartCost`/`CartBuyerIdentity`), and product queries (price on a product page via the `@inContext` directive). |
| [Attribute](https://shopify.dev/docs/api/storefront/latest/objects/Attribute) | An array of custom information for a cart line. Attributes are returned as key-value pairs. |
| [CartLine](https://shopify.dev/docs/api/storefront/latest/objects/CartLine) | A list of line item objects, each containing information about an item in the cart. |
| [Merchandise](https://shopify.dev/docs/api/storefront/latest/unions/Merchandise) | A product variant. It represents one version of a product with several options. |

### Cart ID

The cart ID consists of a token and a secret key parameter in the form of `<token>?key=<secret>`. When you work with any Cart API, you must always provide the full ID.

Example: `gid://shopify/Cart/Z2NwLXVzLWV4YW1wbGU6MDEyMzQ1Njc4OTAxMjM0NTY3ODkw?key=examplekey1234567890`

> Shopify may change the format and length of cart tokens at any time. Apps must be built to handle cart tokens of any format.

The key serves as a verification mechanism for the cart builder, ensuring the protection of the buyer's private data. If you do not include the secret key during a query, the buyer's private details (such as email or address) will be removed from the cart response. Additionally, if you attempt to modify the cart through a mutation without a key, the mutation will fail with an error message indicating the cart does not exist.

> **Caution:** Never expose the `secret` part of the ID. Treat it like a password—don't include it in shareable links, public pages, or any client-side code.

### Step 1: Create a cart and add a line item

You can use the [`cartCreate`](https://shopify.dev/docs/api/storefront/latest/mutations/cartCreate) mutation to create a new cart and add a line item to the cart. In the input, include the line item quantity (`quantity`) and the product variant ID (`merchandiseId`), and specify any attributes (`attributes`) associated with the cart.

If your storefront has context about the buyer that's interacting with the cart (`buyerIdentity`), you can define a preferred delivery method (`deliveryMethod`) in the mutation's input.

> To use pick-up points as a delivery method preference, a `buyerIdentity.countryCode` is required to ensure the buyer's country matches with the pick-up point country.

**POST** `https://{shop}.myshopify.com/api/{api_version}/graphql.json` — GraphQL mutation:

```graphql
mutation {
  cartCreate(
    input: {
      lines: [
        {
          quantity: 1
          merchandiseId: "gid://shopify/ProductVariant/1"
        }
      ],
      # The information about the buyer that's interacting with the cart.
      buyerIdentity: {
        email: "example@example.com",
        countryCode: CA,
        preferences: {
          delivery: {
            deliveryMethod: PICK_UP
          }
        },
      }
      attributes: {
        key: "cart_attribute",
        value: "This is a cart attribute"
      }
    }
  ) {
    cart {
      id
      createdAt
      updatedAt
      lines(first: 10) {
        edges {
          node {
            id
            merchandise {
              ... on ProductVariant {
                id
              }
            }
          }
        }
      }
      buyerIdentity {
        preferences {
          delivery {
            deliveryMethod
          }
        }
      }
      attributes {
        key
        value
      }
      # The estimated total cost of all merchandise that the customer will pay at checkout.
      cost {
        totalAmount {
          amount
          currencyCode
        }
        # The estimated amount, before taxes and discounts, for the customer to pay at checkout.
        subtotalAmount {
          amount
          currencyCode
        }
      }
    }
  }
}
```

### Step 2: Retrieve a cart

You can use the [`cart`](https://shopify.dev/docs/api/storefront/latest/queries/cart) query to retrieve a cart stored on Shopify. In the query, supply the cart ID as your input.

```graphql
query {
  cart(
    id: "gid://shopify/Cart/Z2NwLXVzLWV4YW1wbGU6MDEyMzQ1Njc4OTAxMjM0NTY3ODkw?key=examplekey1234567890"
  ) {
    id
    createdAt
    updatedAt
    lines(first: 10) {
      edges {
        node {
          id
          quantity
          merchandise {
            ... on ProductVariant {
              id
            }
          }
          attributes {
            key
            value
          }
        }
      }
    }
    attributes {
      key
      value
    }
    cost {
      totalAmount {
        amount
        currencyCode
      }
      subtotalAmount {
        amount
        currencyCode
      }
    }
    buyerIdentity {
      email
      phone
      customer {
        id
      }
      countryCode
      preferences {
        delivery {
          deliveryMethod
        }
      }
    }
  }
}
```

### Step 3: Increase an item's quantity

You can use the [`cartLinesUpdate`](https://shopify.dev/docs/api/storefront/latest/mutations/cartLinesUpdate) mutation to add another product variant of the same type to the cart. In the mutation's input, include the cart ID, cart line ID, and the new quantity value.

```graphql
mutation {
  cartLinesUpdate(
    cartId: "gid://shopify/Cart/Z2NwLXVzLWV4YW1wbGU6MDEyMzQ1Njc4OTAxMjM0NTY3ODkw?key=examplekey1234567890"
    lines: {
      id: "gid://shopify/CartLine/1"
      quantity: 3
    }
  ) {
    cart {
      id
      lines(first: 10) {
        edges {
          node {
            id
            quantity
            merchandise {
              ... on ProductVariant {
                id
              }
            }
          }
        }
      }
      cost {
        totalAmount {
          amount
          currencyCode
        }
        subtotalAmount {
          amount
          currencyCode
        }
      }
    }
  }
}
```

### Step 4: Set metafields on a cart

[Metafields](https://shopify.dev/docs/apps/build/custom-data) are a flexible way for your app to add and store additional information about a cart. You can use the [`cartMetafieldsSet`](https://shopify.dev/docs/api/storefront/latest/mutations/cartMetafieldsSet) mutation to create and update metafields on a cart. In the mutation's input, supply the cart ID in the `ownerId` field, and define the parts of the metafield.

```graphql
mutation {
  cartMetafieldsSet(
    metafields:[
      {
        ownerId: "gid://shopify/Cart/1",
        key: "public.materials",
        type: "multi_line_text_field",
        value: "95% Cotton\n5% Spandex"
      },
      {
        ownerId: "gid://shopify/Cart/1",
        key: "public.manufactured",
        type: "single_line_text_field",
        value: "Made in Canada"
      }
  ]) {
    metafields {
      namespace
      key
      value
      type
    }
    userErrors {
      code
      field
      message
    }
  }
}
```

### Step 5: Update customer information and customer preferences for guest checkout journeys

You can use the [`cartBuyerIdentityUpdate`](https://shopify.dev/docs/api/storefront/latest/mutations/cartBuyerIdentityUpdate) mutation to associate customer information and their checkout preferences with the cart, such as a customer's email, phone number, country, preferred delivery method, and pickup location.

Cart delivery addresses can be managed with four mutations:

* [`cartDeliveryAddressesAdd`](https://shopify.dev/docs/api/storefront/latest/mutations/cartDeliveryAddressesAdd)
* [`cartDeliveryAddressesUpdate`](https://shopify.dev/docs/api/storefront/latest/mutations/cartDeliveryAddressesUpdate)
* [`cartDeliveryAddressesRemove`](https://shopify.dev/docs/api/storefront/latest/mutations/cartDeliveryAddressesRemove)
* [`cartDeliveryAddressesReplace`](https://shopify.dev/docs/api/storefront/latest/mutations/cartDeliveryAddressesReplace)

```graphql
mutation {
  cartBuyerIdentityUpdate(
    cartId: "gid://shopify/Cart/Z2NwLXVzLWV4YW1wbGU6MDEyMzQ1Njc4OTAxMjM0NTY3ODkw?key=examplekey1234567890"
    buyerIdentity: {
      email: "example@example.com"
      phone: "800-555-0100"
      countryCode: CA,
      preferences: {
        delivery: {
          deliveryMethod: PICK_UP,
          pickupHandle: "93893525526"
        }
      }
    }
  ) {
    cart {
      id
      buyerIdentity {
        email
        phone
        countryCode
        preferences {
          delivery {
            deliveryMethod
            pickupHandle
          }
        }
      }
    }
  }
}
```

### Step 6: Authenticate customer for logged-in checkouts

You can authenticate the customer by setting a valid `customerAccessToken` in the `cartBuyerIdentityUpdate` mutation or during cart creation. If you append the `customerAccessToken` to the cart, then the buyer will be logged in when they're redirected to checkout.

> This covers authenticating the buyer using the buyer identity on the cart. For an alternative using `sso=silent` or help choosing between approaches, see [Authenticate buyers in checkout](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/checkout-authentication).

```graphql
mutation {
  cartBuyerIdentityUpdate(
    cartId: "gid://shopify/Cart/Z2NwLXVzLWV4YW1wbGU6MDEyMzQ1Njc4OTAxMjM0NTY3ODkw?key=examplekey1234567890"
    buyerIdentity: {
      customerAccessToken: "1b024bde52fcce3c363d2e67f7a13958"
    }
  ) {
    cart {
      id
      buyerIdentity {
        customerAccessToken
      }
    }
  }
}
```

### Step 7: Retrieve a checkout URL

When the buyer is ready to complete checkout, you can query the [`Cart`](https://shopify.dev/docs/api/storefront/latest/queries/cart) object for the [`checkoutUrl`](https://shopify.dev/docs/api/storefront/latest/objects/Cart#field-checkouturl) by supplying the cart's ID as your input. The response includes a URL that redirects customers through Shopify's web checkout.

> When the customer access token is set on the cart, the obtained `checkoutUrl` allows the authenticated buyer to navigate to a logged-in checkout experience. For security reasons, the `checkoutUrl` should be requested when the buyer is ready to navigate to checkout and can be re-requested if it is stale.

To preserve the buyer's logged-in checkout experience, you must include the `Shopify-Storefront-Buyer-IP` header in your Storefront API call when making server side requests.

```graphql
query checkoutURL {
  cart(id: "gid://shopify/Cart/Z2NwLXVzLWV4YW1wbGU6MDEyMzQ1Njc4OTAxMjM0NTY3ODkw?key=examplekey1234567890") {
    checkoutUrl
  }
}
```

Response:

```json
{
  "data": {
    "cart": {
      "checkoutUrl": "https:\/\/exam.myshopify.com\/cart\/c\/29567c413f68cf5e8c1cb623954f3a28"
    }
  }
}
```

### Next steps

* Use the `warnings` return field to manage automatic changes to your cart.
* Learn how to create a cart and a subscription line item.
* Query international prices for products and orders, and explicitly set the context of a cart and checkout.
* Manage customer accounts with the Storefront API.
* Use `@defer` to fetch carrier-calculated rates for the cart.

---

## Retrieve metafields with the Storefront API

> Fonte: https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/products-collections/metafields

You can retrieve metafields with the [Storefront API](https://shopify.dev/docs/api/storefront) to access additional information from different types of resources. This guide describes how to expose metafields to the Storefront API, retrieve them, and hide them from the Storefront API.

### Requirements

* You've completed the Getting started with the Storefront API guide.
* You're familiar with querying products and collections.
* You've created resources that support metafields in your store, and you've created metafields for those resources.
* You're familiar with how metafields work.

> **Note:** You can't create, update, or delete metafields with the Storefront API. If you want to perform these types of operations on metafields, then you need to use the [GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql/latest/objects/metafield).

### Step 1: Expose metafields

> **Important:** As of API version 2025-01, the `metafieldStorefrontVisibilityCreate` mutation has been removed. Use metafield definitions with the `access.storefront` parameter instead.

To expose metafields to the Storefront API, you need to create or update a metafield definition with the `access.storefront` parameter set to `"PUBLIC_READ"`. This can be done using the [`metafieldDefinitionCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/metafielddefinitioncreate) or [`metafieldDefinitionUpdate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/metafielddefinitionupdate) mutations in the GraphQL Admin API.

The following fields are required when creating a metafield definition:

* `namespace` — The namespace for the metafield.
* `key` — The key for the metafield.
* `name` — A human-readable name for the metafield.
* `type` — The metafield type (e.g., `single_line_text_field`, `number_integer`).
* `ownerType` — The resource that owns this metafield (e.g., `PRODUCT`).
* `access.storefront` — Set to `"PUBLIC_READ"` to expose to the Storefront API.

#### Creating a new metafield definition

The following example creates a metafield definition for a product metafield with the namespace `testapp` and the key `pizza-size-inches`, making it accessible via the Storefront API:

```graphql
mutation {
  metafieldDefinitionCreate(
    definition: {
      namespace: "testapp"
      key: "pizza-size-inches"
      name: "Pizza Size (inches)"
      type: "number_integer"
      ownerType: PRODUCT
      access: {
        storefront: "PUBLIC_READ"
      }
    }
  ) {
    createdDefinition {
      id
      namespace
      key
      access {
        storefront
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

JSON response:

```json
{
  "data": {
    "metafieldDefinitionCreate": {
      "createdDefinition": {
        "id": "gid://shopify/MetafieldDefinition/123456",
        "namespace": "testapp",
        "key": "pizza-size-inches",
        "access": {
          "storefront": "PUBLIC_READ"
        }
      },
      "userErrors": []
    }
  }
}
```

You can create multiple metafield definitions. Here's another example for an expiration date metafield:

```graphql
mutation {
  metafieldDefinitionCreate(
    definition: {
      namespace: "testapp"
      key: "expiration-date"
      name: "Expiration Date"
      type: "date"
      ownerType: PRODUCT
      access: {
        storefront: "PUBLIC_READ"
      }
    }
  ) {
    createdDefinition {
      id
      namespace
      key
      access {
        storefront
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

#### Updating an existing metafield definition

If you have an existing metafield definition that needs to be exposed to the Storefront API, you can update it using the `metafieldDefinitionUpdate` mutation:

```graphql
mutation {
  metafieldDefinitionUpdate(
    definition: {
      access: {
        storefront: "PUBLIC_READ"
      }
    }
    id: "gid://shopify/MetafieldDefinition/123456"
  ) {
    updatedDefinition {
      id
      namespace
      key
      access {
        storefront
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

### Step 2: Retrieve metafields

After exposing metafields, you can retrieve them with the Storefront API by using the `metafield` field. You can retrieve a single metafield for a product or a product variant. To specify the metafield that you want to retrieve, use the `namespace` and `key` arguments.

> **Note:** If you have existing metafields that were previously exposed using the deprecated `metafieldStorefrontVisibilityCreate` mutation, you'll need to create or update their metafield definitions with `access.storefront` set to `"PUBLIC_READ"` to maintain Storefront API access.

In the following example, you have a product called "Amazing Frozen Pizza" and you've created metafields that store the size of the pizza and the pizza's expiration date.

```graphql
query {
  product(handle: "amazing-frozen-pizza") {
    pizzaSizeInches: metafield(namespace: "testapp", key: "pizza-size-inches") {
      value
      type
    }
    expirationDate: metafield(namespace: "testapp", key: "expiration-date") {
      value
      type
    }
  }
}
```

JSON response:

```json
{
  "data": {
    "product": {
      "pizzaSizeInches": {
        "value": "9",
        "type": "number_integer"
      },
      "expirationDate": {
        "value": "2025-12-31",
        "type": "date"
      }
    }
  }
}
```

### Step 3: Hide metafields (optional)

If you no longer need to access a metafield with the Storefront API, you can hide it by updating the metafield definition to remove storefront access. Use the `metafieldDefinitionUpdate` mutation and set `access.storefront` to `"NONE"` or simply omit the storefront access.

First, you can retrieve your metafield definitions to find the one you want to update:

```graphql
query {
  metafieldDefinitions(first: 5, namespace: "testapp", ownerType: PRODUCT) {
    edges {
      node {
        id
        namespace
        key
        ownerType
        access {
          storefront
        }
      }
    }
  }
}
```

The following example uses one of the returned IDs to update the metafield definition to remove storefront access:

```graphql
mutation {
  metafieldDefinitionUpdate(
    definition: {
      access: {
        storefront: "NONE"
      }
    }
    id: "gid://shopify/MetafieldDefinition/123456"
  ) {
    updatedDefinition {
      id
      namespace
      key
      access {
        storefront
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

### Next steps

* Learn how to use metafields to store information related to your app and attach that information to Shopify API resources.
* Explore the metafield reference for the Storefront API.

---

## Paginating Results with GraphQL

> Fonte: https://shopify.dev/docs/api/usage/pagination-graphql

When retrieving lists of resources through a connection, you can specify the quantity of results to fetch. Cursor-based pagination allows you to select which subset of results you want to retrieve from a connection.

> **Note:** The maximum retrievable is 250 resources per request. For larger datasets, consider using "[bulk query operations](https://shopify.dev/docs/api/usage/bulk-operations/queries)" through the GraphQL Admin API.

### How It Works

Connections retrieve node lists, where each node represents an object with a "[global ID](https://shopify.dev/docs/api/usage/gids)" and a schema-defined type (such as `Order`). The `orders` connection, for example, locates all `Order` nodes tied to the query root. The `nodes` field functions similarly to a for-loop—it extracts chosen fields from every node within the connection.

To balance performance and user experience, request only a specific quantity of nodes simultaneously. This returned batch is termed a page, with each node's position marked by its cursor.

Retrieving the next page requires indicating the starting node position via a cursor. The `PageInfo` object furnishes cursor information about the current page, which you can apply in subsequent queries using `after` or `before` parameters.

**POST** `https://{shop}.myshopify.com/api/{api_version}/graphql.json`

```graphql
query {
  orders(first: 2) {
    nodes {
      id
      name
      createdAt
    }
  }
}
```

> **Tip:** Node lists can also be obtained using edges.

#### The `PageInfo` Object

Every connection in the GraphQL Admin API includes a `PageInfo` object supporting cursor-based pagination. The structure contains these fields:

| Field | Type | Description |
| - | - | - |
| `hasPreviousPage` | Boolean | Whether results exist before the current page in the connection. |
| `hasNextPage` | Boolean | Whether results exist after the current page in the connection. |
| `startCursor` | string | The cursor of the first node in the `nodes` list. |
| `endCursor` | string | The cursor of the last node in the `nodes` list. |

> **Note:** The GraphQL Partner API's `PageInfo` object includes only `hasNextPage` and `hasPreviousPage` fields.

```graphql
query {
  orders(first: 2) {
    nodes {
      id
      name
      createdAt
    }
    pageInfo {
      hasPreviousPage
      hasNextPage
      startCursor
      endCursor
    }
  }
}
```

### Forward Pagination

All Shopify API connections support forward pagination using these variables:

| Field | Type | Description |
| - | - | - |
| `first` | integer | The requested count of `nodes` per page. |
| `after` | string | The cursor to retrieve `nodes` after in the connection. Typically, pass the previous page's `endCursor` as `after`. |

Include `PageInfo` fields in queries to paginate results. The following example uses `hasNextPage` and `endCursor` fields with query variables to pass the `endCursor` as an argument:

```graphql
query ($numProducts: Int!, $cursor: String) {
  # The `$numProducts` variable is required and is used to specify the number of results to return. The `$cursor` variable isn't required. If the `$cursor` variable is omitted, then the `after` argument is ignored.
  products(first: $numProducts, after: $cursor) {
    nodes {
      title
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```

Variables:

```json
{
  "numProducts": 3,
  "cursor": null
}
```

Using the same query with different variables (passing the previous `endCursor`) retrieves the next page:

```json
{
  "numProducts": 3,
  "cursor": "eyJsYXN0X2lkIjo3MDE3MjQ0MTY0MTUyLCJsYXN0X3ZhbHVlIjoiNzAxNzI0NDE2NDE1MiJ9"
}
```

### Backward Pagination

Some Shopify API connections also provide backward pagination using these variables:

| Field | Type | Description |
| - | - | - |
| `last` | integer | The requested count of `nodes` per page. |
| `before` | string | The cursor to retrieve `nodes` before in the connection. Typically, pass the previous page's `startCursor` as `before`. |

Begin at the end of the node list, then query in reverse page order toward the beginning. The following example uses `hasPreviousPage` and `startCursor` fields with query variables to pass the `startCursor` as an argument:

```graphql
query ($numProducts: Int!, $cursor: String){
  products(last: $numProducts, before: $cursor) {
    nodes {
      title
    }
    pageInfo {
      hasPreviousPage
      startCursor
    }
  }
}
```

The `startCursor` field can be used in subsequent requests as the `before` input to retrieve the previous page.

### Connection Edges

In connections, an `Edge` type characterizes the relationship between the node and its parent. In most scenarios, querying `nodes` and `pageInfo` is preferable to querying `edges`. However, if you require `Edge` metadata, you can query `edges` instead of `nodes`. Each `Edge` contains at minimum the edge's cursor and the node.

```graphql
query ($numProducts: Int!, $cursor: String){
  products(first: $numProducts, after: $cursor) {
    edges {
      cursor
      node {
        title
      }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```

### Search Performance Considerations

Paginating resources using a "[range search](https://shopify.dev/docs/api/usage/search-syntax#search-query-syntax)" might timeout or produce an error if the resource collection is substantially large and the search field differs from the designated (or default) sort key for the queried connection. If your query performs poorly or returns an error, attempt specifying a sort key matching the search field. For example:

```graphql
{
  orders(first: 250, query: "created_at:>'2020-10-21'", sortKey: CREATED_AT) {
    edges {
      node {
        id
      }
    }
  }
}
```

---

# Pagine aggiuntive (URL elencati, non estratti)

Queste pagine sono parte dell'albero Headless/Hydrogen ma non sono state estratte verbatim: si tratta in larga parte di reference auto-generati enormi (schema GraphQL, API per-componente/per-hook) oppure di guide secondarie/varianti già coperte da una pagina equivalente in questo capitolo. Sono elencate qui per completezza e tracciabilità.

## Reference auto-generati (alberi enormi — non estratti)

- Hydrogen API reference (componenti, hook, utilities, ognuno con pagina propria): https://shopify.dev/docs/api/hydrogen
  - Esempi di sotto-pagine reference: `components/pagination`, `components/analytics/*`, `utilities/caching/createwithcache`, `utilities/caching/generatecachecontrolheader`, `utilities/getpaginationvariables`, `utilities/getseometa`, `utilities/getshopanalytics`, `utilities/createcustomeraccountclient`, `utilities/createcarthandler`
- Hydrogen React (package framework-agnostico): https://shopify.dev/docs/api/hydrogen-react
- Storefront API reference (oggetti, query, mutation, enum): https://shopify.dev/docs/api/storefront
  - Tipi citati nel capitolo: `objects/Cart`, `objects/CartBuyerIdentity`, `objects/CartCost`, `objects/CartLine`, `objects/Attribute`, `unions/Merchandise`, `objects/StoreAvailability`, `objects/Location`, `objects/SellingPlan`, `objects/metafield`, `objects/CustomerAccessToken`, `queries/cart`, `queries/products`, `queries/product`, `queries/productRecommendations`, `mutations/cartCreate`, `mutations/cartLinesUpdate`, `mutations/cartMetafieldsSet`, `mutations/cartBuyerIdentityUpdate`, `mutations/cartDeliveryAddresses*`
- Customer Account API reference (oggetti, query, mutation, enum): https://shopify.dev/docs/api/customer
  - Tipi citati: `objects/customer`, `enums/LanguageCode`, `enums/CountryCode`
- Storefront Web Components: https://shopify.dev/docs/api/storefront-web-components
- Hydrogen React: https://shopify.dev/docs/api/hydrogen-react

## Guide secondarie / varianti (non estratte per evitare ridondanza o perché fuori dallo scope GUIDE)

Headless overview / Storefront API exploration & SDK:
- Additional SDKs: https://shopify.dev/docs/storefronts/headless/additional-sdks
- Storefront API GraphiQL explorer (demo shop): https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/api-exploration/graphiql-storefront-api
- Manage customer accounts with the Storefront API (legacy customer flow): https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/customer-accounts
- Filter products in a collection: https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/products-collections/filter-products
- Local pickup on storefronts: https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/products-collections/local-pickup
- Manage subscription products on storefronts: https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/products-collections/subscriptions
- Cart (overview): https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/cart
- Cart warnings: https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/cart/cart-warnings
- International pricing (Markets, Storefront API): https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/markets/international-pricing
- Using `@defer`: https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/defer
- Headless with B2B: https://shopify.dev/docs/storefronts/headless/bring-your-own-stack/b2b

Hydrogen — guide aggiuntive:
- Setup i18n con domini e sottodomini (variante della guida URL paths già estratta): https://shopify.dev/docs/storefronts/headless/hydrogen/markets/multiple-languages-domains
- Localization detection (headers/cookies/URL params): https://shopify.dev/docs/storefronts/headless/hydrogen/markets/locale-detection
- Markets — multiple languages domains: https://shopify.dev/docs/storefronts/headless/hydrogen/markets/multiple-languages-domains
- Redirect traffic to the Hydrogen channel (migrazione): https://shopify.dev/docs/storefronts/headless/hydrogen/migrate/redirect-traffic
- Production checklist / Go live: https://shopify.dev/docs/storefronts/headless/hydrogen/production-checklist
- Storefronts (gestione storefront Hydrogen): https://shopify.dev/docs/storefronts/headless/hydrogen/storefronts
- Oxygen runtime details: https://shopify.dev/docs/storefronts/headless/hydrogen/deployments/oxygen-runtime
- Self-hosting Hydrogen: https://shopify.dev/docs/storefronts/headless/hydrogen/deployments/self-hosting
- Logging / log drains: https://shopify.dev/docs/storefronts/headless/hydrogen/logging
- Content security policy: https://shopify.dev/docs/storefronts/headless/hydrogen/content-security-policy
- On-page optimizations (performance): https://shopify.dev/docs/storefronts/headless/hydrogen/performance/on-page-optimizations
- Subrequest Profiler (debugging): https://shopify.dev/docs/storefronts/headless/hydrogen/debugging/subrequest-profiler
- Analytics — consent (Customer Privacy API): https://shopify.dev/docs/storefronts/headless/hydrogen/analytics/consent
- Analytics — validation/troubleshooting: https://shopify.dev/docs/storefronts/headless/hydrogen/analytics/validation
- Cookbook — Express server: https://shopify.dev/docs/storefronts/headless/hydrogen/cookbook/express
- Cookbook — third-party API: https://shopify.dev/docs/storefronts/headless/hydrogen/cookbook/third-party-api

Customer Account API — guide aggiuntive:
- Market-aware auth URLs: https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/market-aware-auth-urls
- Authenticate buyers in checkout: https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/checkout-authentication
- Manage customer accounts with the Customer Account API: https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/customer-accounts

