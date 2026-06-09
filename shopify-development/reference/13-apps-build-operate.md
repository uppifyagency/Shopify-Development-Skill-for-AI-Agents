# 13. Custom Apps — Build & Operate

Questo capitolo raccoglie le guide concettuali e operative ("how-to") della documentazione Shopify per **costruire e gestire** una Shopify app: webhook, billing, configurazione dell'app, distribuzione e lancio sull'App Store, linee guida di design/UX e conformità (privacy & dati protetti).

Ogni pagina è riprodotta integralmente dal sito ufficiale `shopify.dev`, con l'URL di origine indicato sotto ogni titolo. Le sezioni di puro riferimento (es. l'elenco completo dei topic webhook) sono linkate nella sezione finale **Pagine aggiuntive**.

## Indice delle sezioni

1. [Webhooks](#webhooks)
2. [Billing](#billing)
3. [App configuration](#app-configuration)
4. [Distribution & launch](#distribution--launch)
5. [Design / UX](#design--ux)
6. [Compliance & data protection](#compliance--data-protection)
7. [Pagine aggiuntive](#pagine-aggiuntive)

---

# Webhooks

Mini-indice della sezione:

- [About Webhooks](#about-webhooks)
- [Create a webhook subscription (get started)](#create-a-webhook-subscription)
- [Manage webhook subscriptions](#manage-webhook-subscriptions)
- [Filter webhook deliveries](#filter-webhook-deliveries)
- [Webhooks delivery structure](#webhooks-delivery-structure)
- [Verify webhook deliveries](#verify-webhook-deliveries)
- [Troubleshoot webhooks](#troubleshoot-webhooks)

---

## About Webhooks

> Fonte: https://shopify.dev/docs/apps/build/webhooks

When your app needs information about specific events that have occurred on a shop, it can subscribe to Shopify webhook topics as a mechanism for receiving near-real-time data about these events.

Shopify webhooks are useful for keeping your app in sync with Shopify data, or as a trigger to perform an additional action after that event has occurred. They're also a performant alternative to continuously polling for changes to a shop's data.

This guide provides a quick primer on when to use APIs compared to webhooks, as well as key terminology and behaviors that are specific to Shopify webhooks.

### What you can build

- Send notifications about changes in inventory levels to inventory management clients and pagers.
- Inform shipping companies about changes in orders, returns, or refunds.
- Remove customer data from a database for app uninstalls.
- Integrate data about orders with accounting software.
- Update a product's warranty price based on changes to the product's price.

### How it works

The following example uses the `orders/create` webhook topic to illustrate the difference between polling an API for data about events, versus subscribing to a webhook topic to receive data about events.

1. The app subscribes to the `orders/create` topic for a shop and listens for order creation events.
2. The app specifies an endpoint to receive webhooks for the `orders/create` topic. For example, this might be an HTTPS endpoint hosted by the app server. This endpoint is where the app listens for webhooks.
3. Suppose now that an order is created from that shop.
4. This triggers a webhook to be published to the `orders/create` topic.
5. Shopify sends that webhook, which includes headers and an order payload, to the specified subscription endpoint.

You declare a subscription in `shopify.app.toml` or using the GraphQL Admin API to tell Shopify which topic to watch and where to send deliveries. The four core concepts are:

- **[Manage subscriptions](https://shopify.dev/docs/apps/build/webhooks/subscribe):** Configure which topics your app subscribes to, and where deliveries are sent.
- **[Delivery filtering](https://shopify.dev/docs/apps/build/webhooks/delivery-filtering):** Use `filter` and `include_fields` to narrow which deliveries qualify and what each payload contains.
- **[Delivery structure](https://shopify.dev/docs/apps/build/webhooks/delivery-structure):** Understand the payload format and headers included with each delivery.
- **[Verify deliveries](https://shopify.dev/docs/apps/build/webhooks/verify-deliveries):** Verify HMAC signatures and ignore duplicate deliveries using `X-Shopify-Webhook-Id`.

**Try Events:** Events is Shopify's next-generation subscription mechanism, currently in developer preview for a subset of topics. For supported topics, Events and webhooks can run side by side in the same `shopify.app.toml`. See [Events and webhooks](https://shopify.dev/docs/apps/build/events-webhooks) to compare, or [migrate a subscription](https://shopify.dev/docs/apps/build/events/migrate-from-webhooks) to try Events early.

### Key terminology

#### Webhook subscription

A subscription declares which topic to watch and where to send deliveries: a URL, Google Pub/Sub URI, or Amazon EventBridge ARN. See [Manage subscriptions](https://shopify.dev/docs/apps/build/webhooks/subscribe).

#### Webhook topic

A topic identifies the resource and action that qualifies a delivery. For example, `products/create` fires when a new product is created. See [Manage subscriptions](https://shopify.dev/docs/apps/build/webhooks/subscribe) for the full list of supported topics and required scopes.

#### Headers

Each delivery includes metadata headers such as `X-Shopify-Topic`, `X-Shopify-Webhook-Id`, and `X-Shopify-Hmac-Sha256`. See [Delivery structure](https://shopify.dev/docs/apps/build/webhooks/delivery-structure) for the full headers reference.

### What to expect

Below are some key things to remember when working with webhooks.

#### Ordering event data

As with other webhook systems, Shopify doesn't guarantee ordering within a topic, or across different topics for the same resource. For example, it's possible that a `products/update` webhook might be delivered before a `products/create` webhook.

Shopify recommends using timestamps provided in the header (`X-Shopify-Triggered-At`) or in the payload itself (`updated_at`) to organize webhooks.

#### Implement reconciliation jobs

Your app shouldn't rely solely on receiving data from Shopify webhooks. Because webhook delivery isn't always guaranteed, you should implement reconciliation jobs to periodically fetch data from Shopify.

You could do this in the background, or offer reconciliation and syncing options to the user. For example, the UI of your app could contain a button that triggers a manual reconciliation process by calling the relevant API endpoint, and fetching the requested data.

Many GraphQL queries support `updated_at` filter parameters. Use these filters to build a job that fetches all objects updated since the last time the job ran.

### Next steps

- [Get started with webhooks](https://shopify.dev/docs/apps/build/webhooks/get-started) — Build a working subscription and handler.
- [Webhooks reference](https://shopify.dev/docs/api/webhooks) — Full list of supported topics, payloads, and required scopes.

---

## Create a webhook subscription

> Fonte: https://shopify.dev/docs/apps/build/webhooks/get-started

Subscribe your app to Shopify webhook topics so that it will be alerted when an event occurs on a merchant store.

Suppose you are building a warranty pricing app that determines which warranty options a customer can add to their cart, based on the cost of an order.

When a customer is checking out, the total order cost is used to determine which warranty options a customer can select from.

In this tutorial, you'll subscribe your app to a webhook topic to be alerted whenever a new order is created.

### What you'll learn

In this tutorial, you'll learn how to do the following tasks:

- Use your [app configuration file](https://shopify.dev/docs/apps/tools/cli/configuration#webhooks) to set up a webhook subscription.
- Use cloud-based delivery methods like [Google Cloud's Pub/Sub event bus](https://cloud.google.com/pubsub) to receive webhooks.
- Test your subscription is configured correctly and you are receiving webhooks.

**Info:** Shopify recommends using [Google Pub/Sub](https://cloud.google.com/pubsub) as a cloud-based solution for delivering webhooks. You can also use [Amazon EventBridge](https://aws.amazon.com/eventbridge/). In instances where you want to hand-roll your own webhooks infrastructure, you may prefer your webhooks be delivered through [HTTPS](https://shopify.dev/docs/apps/webhooks/configuration/https). During development, you may choose to use your app's URL or external mock server sites like [webhook.site](https://webhook.site/) and [Beeceptor](https://beeceptor.com/). These are not recommended for production.

### Requirements

#### Use the latest version of Shopify CLI

Ensure you have the [latest version of Shopify CLI](https://shopify.dev/docs/api/shopify-cli#upgrade) installed to configure app-specific webhook subscriptions.

#### Set up a Google Cloud console project

[Set up your Google Cloud account to use Pub/Sub.](https://cloud.google.com/pubsub/docs/quickstart-console)

#### Development tools

For development, you can use mock servers like [Hookdeck Console](https://console.hookdeck.com/) or [webhook.site](https://webhook.site/).

### Project

[View on GitHub](https://github.com/Shopify/shopify-app-template-react-router/blob/webhooks-subscribe-example-pubSub/shopify.app.toml)

### Set your app up to receive webhooks from Google Pub/Sub

To receive webhooks via a cloud-based event bus like Pub/Sub from Google Cloud, you must first set up a connection between your app and Pub/Sub.

#### Grant Shopify access to publish webhooks to your Google Pub/Sub topic

1. Click on **Topics** in the left panel.
2. Click on the **Create a topic** button. Enter in a name, keep the remaining defaults and click on **Create**.
3. Next to the Google Pub/Sub topic you just created, click `⋮` and then click **View permissions**.
4. Click on **ADD PRINCIPAL**.
5. Paste `delivery@shopify-pubsub-webhooks.iam.gserviceaccount.com` (the Shopify service account address) into the **New principals** text box.
6. In the **Role** drop-down list, select **Pub/Sub** as the type, and specify the role as **Pub/Sub Publisher**.
7. Click **Save**.

### Configure your webhook subscription

#### Update your access scopes

Some webhook topics require scopes in order to be used. Because we want to know when an order is created, we need to include the `read_orders` scope in the configuration file.

- To determine which scopes are required for each topic, use the [Webhooks reference](https://shopify.dev/docs/api/webhooks).
- See the [complete list of access scopes](https://shopify.dev/docs/api/usage/access-scopes).

**Info:** Scopes that access private customer data, such as `read_orders`, require manual steps in your Partner Dashboard. Go to your app > **API access requests** > **Protected customer data access**, fill out only the first step, and then save. Reinstall your app in the Shopify admin to register the granted scope.

#### shopify.app.toml

```toml
# This file stores configurations for your Shopify app.
name = "Example App"
client_id = "a61950a2cbd5f32876b0b55587ec7a27"
application_url = "https://www.app.example.com/"
embedded = true
handle = "example-app"


[access_scopes]
scopes = "write_products, read_orders"


[webhooks]
api_version = "2024-07"


  # Handled by: /app/routes/webhooks.app.uninstalled.tsx
  [[webhooks.subscriptions]]
  uri = "/webhooks/app/uninstalled"
  topics = ["app/uninstalled"]


  # Handled by: /app/routes/webhooks.app.scopes_update.tsx
  [[webhooks.subscriptions]]
  topics = [ "app/scopes_update" ]
  uri = "/webhooks/app/scopes_update"


  # Webhooks can have filters
  # Only receive webhooks for product updates with a product price >= 10.00
  # See: https://shopify.dev/docs/apps/build/webhooks/customize/filters
  # [[webhooks.subscriptions]]
  # topics = ["products/update"]
  # uri = "/webhooks/products/update"
  # filter = "variants.price:>=10.00"


  # Webhooks can have names as identifiers
  # This field is optional
  # Must be unique; alphanumeric characters, underscores, and hyphens only
  # [[webhooks.subscriptions]]
  # name = "products-create"
  # topics = [ "products/create" ]
  # uri = "/webhooks/products/create"


  # Mandatory compliance topic for public apps only
  # See: https://shopify.dev/docs/apps/build/privacy-law-compliance
  # [[webhooks.subscriptions]]
  # uri = "/webhooks/customers/data_request"
  # compliance_topics = ["customers/data_request"]


  # [[webhooks.subscriptions]]
  # uri = "/webhooks/customers/redact"
  # compliance_topics = ["customers/redact"]


  # [[webhooks.subscriptions]]
  # uri = "/webhooks/shop/redact"
  # compliance_topics = ["shop/redact"]


  [[webhooks.subscriptions]]
  topics = ["orders/create"]
  uri = "pubsub://<PROJECT-ID>:<PUBSUB-TOPIC-ID>"


  [[webhooks.subscriptions]]
  topics = ["orders/create"]
  uri = "/webhooks/app/orders-create"


  [[webhooks.subscriptions]]
  topics = ["orders/create"]
  uri = "arn:aws:events:<AWS-REGION>::event-source/aws.partner/shopify.com/<APP-ID>/<EVENT-SOURCE-NAME>"
```

#### Select the API version

The API version impacts which topics are available to subscribe to. The React Router template defaults to the latest version in your app configuration file. However, you can [update the API version](https://shopify.dev/docs/apps/webhooks/versioning) as needed.

#### Configure topics to subscribe to

To determine which topic to subscribe to, use the [Webhooks reference](https://shopify.dev/docs/api/webhooks).

In this example, your topic name will be in a list and formatted as:

```
topics = ["orders/create"]
```

Your endpoint address should follow the following format:

```
pubsub://{project-id}:{topic-id}
```

### Process your webhooks

Follow the [Google PubSub docs](https://www.npmjs.com/package/@google-cloud/pubsub#using-the-client-library) to subscribe to event data and process events.

#### Confirm the subscription has been added to this version of your app

When working in development mode, webhook subscriptions are automatically updated when you save your TOML file.

1. Save your TOML file.
2. If `app dev` is running, the webhook subscription will be automatically created or updated.
3. The webhook subscription is now active in your dev store.

**Info:** This step abstracts away calls to the [`webhookSubscriptionCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/webhookSubscriptionCreate) GraphQL mutation. Learn more about [subscribing to webhook topics using the GraphQL Admin API](https://shopify.dev/docs/apps/build/webhooks/subscribe#shop-specific-subscriptions).

### Test your subscription

#### Manually trigger an event in your test shop

Most webhook topics fire immediately when you trigger the corresponding event in your dev store.

1. Navigate to your test shop and create a new order.
2. The webhook payload should print to your Google Pub/Sub console.

**Info:** A small number of webhook topics will not fire immediately if you trigger an event in your test shop. They include:

- The [customers/redact topic](https://shopify.dev/docs/apps/build/privacy-law-compliance#customers-redact)
- The [shop/redact topic](https://shopify.dev/docs/apps/build/privacy-law-compliance#shop-redact)

#### Simulate an event using the command line

You can use the CLI to simulate specific events occurring on a shop. This lets you test your processing logic by sending a POST request to your endpoint with a synthetic webhook. It doesn't test your subscription configuration.

[`shopify app webhook trigger`](https://shopify.dev/docs/api/shopify-cli/app/app-webhook-trigger)

The address inputted for the `--address` flag should follow the following format:

```
pubsub://{project-id}:{topic-id}
```

### Deploy your app

When you're ready to release your webhook subscriptions to production, you can create and release an [app version](https://shopify.dev/docs/apps/launch/deployment/app-versions). An app version is a snapshot of your app configuration and all extensions.

1. Navigate to your app directory.
2. Run the following command. Optionally, you can provide a name or message for the version using the `--version` and `--message` flags.

```terminal
shopify app deploy
```

Releasing an app version replaces the current active version that's served to stores that have your app installed. It might take several minutes for app users to be upgraded to the new version.

**Tip:** If you want to create a version, but avoid releasing it to users, then run the `deploy` command with a `--no-release` flag. You can release the unreleased app version using Shopify CLI's [`release`](https://shopify.dev/docs/api/shopify-cli/app/app-release) command, or through the Dev Dashboard.

### Tutorial complete!

Congratulations! You subscribed your app to a webhook topic using React Router, Google PubSub, and Shopify webhooks. Keep the momentum going with these related tutorials and resources.

#### Next steps

- [Deploy your app](https://shopify.dev/docs/apps/deployment/web) — Follow the guide to deploy your React Router app to a testing or production environment.
- [Explore the Shopify Webhooks reference](https://shopify.dev/docs/api/webhooks) — Learn about the full list of topics Shopify offers, required access and approval scopes, and sample payloads.
- [Manage subscriptions](https://shopify.dev/docs/apps/build/webhooks/subscribe) — Add, update, and delete webhook subscriptions for your app.
- [Events and classic webhooks](https://shopify.dev/docs/apps/build/events-webhooks) — Events is Shopify's next-generation subscription mechanism. Compare Events and webhooks to understand when to use each.

---

## Manage webhook subscriptions

> Fonte: https://shopify.dev/docs/apps/build/webhooks/subscribe

A webhook subscription tells Shopify which events your app is interested in and where to deliver them.

This page covers the subscription configuration options, including how to choose between subscription types and delivery methods. To shape the content of each delivery, see [Delivery structure](https://shopify.dev/docs/apps/build/webhooks/delivery-structure) and [Delivery filtering](https://shopify.dev/docs/apps/build/webhooks/delivery-filtering).

### Requirements

Each topic you subscribe to requires a corresponding [access scope](https://shopify.dev/docs/apps/build/authentication-authorization/app-installation/manage-access-scopes). See the [Webhooks reference](https://shopify.dev/docs/api/webhooks) for the full list of topics and their required scopes.

If your app is distributed through the Shopify App Store, it must be subscribed to Shopify's [mandatory compliance topics](https://shopify.dev/docs/apps/build/privacy-law-compliance). You can create mandatory compliance webhook subscriptions in Dev Dashboard or by updating your [app configuration file](https://shopify.dev/docs/apps/build/cli-for-apps/app-configuration#app-configuration-file-example).

### Versioning

Like most Shopify APIs, webhooks are [versioned](https://shopify.dev/docs/api/usage/versioning). Shopify recommends updating to the latest stable API version each quarter. The `api_version` field in `[webhooks]` controls the GraphQL Admin API version used to serialize payloads for all app-specific subscriptions:

#### shopify.app.toml

```toml
[webhooks]
api_version = "2026-04"
```

For shop-specific subscriptions created using the GraphQL Admin API, the version is determined by the request URL.

Each delivery includes the API version that serialized its payload. For HTTPS deliveries, check the [`X-Shopify-API-Version` header](https://shopify.dev/docs/apps/build/webhooks/delivery-structure#headers). For Google Cloud Pub/Sub or Amazon EventBridge, the version appears in the message payload instead.

Before updating `api_version`, test the new version against your handler code using the CLI:

```shell
shopify app webhook trigger --api-version=<new-version> --address=<destination> --topic=<topic-name>
```

Pass with the flags shown above, or run the command with no parameters and follow the prompts. Your existing subscriptions will continue using the earlier version until you update and deploy.

#### Update the API version

**App configuration file**

1. Set `webhooks.api_version` to the new version in `shopify.app.toml`.
2. Save the file. If `app dev` is running, the version updates automatically for your dev store.
3. Run `shopify app deploy` to release the change to production.

**Dev Dashboard**

1. From your [Dev Dashboard](https://dev.shopify.com/dashboard), go to **Apps**.
2. Click on your app.
3. Click **Versions** → **Create a version**.
4. In the **Webhooks API Version** field, select the newer API version.
5. Click **Release**.

### Subscription types

Shopify supports two ways to configure webhook subscriptions:

- **App-specific subscriptions**: (Recommended) Defined in `shopify.app.toml` and applied uniformly across every shop that installs your app.
- **Shop-specific subscriptions**: Created using GraphQL Admin API; configuration can differ per shop.

Choose app-specific subscriptions unless your topics, delivery URIs, or filters need to vary between shops. Use the table below to compare the capabilities and behavior of these two options:

| | App-specific | Shop-specific |
| - | - | - |
| **Compliance topics** | Supported. See [Privacy law compliance](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance#subscribe-to-compliance-webhooks). | Can be configured in your app configuration file. **Cannot** be subscribed to using the Admin API. |
| **Differentiating between methods** | Available in the **Subscription Method** field in **Logs** | Available in the **Subscription Method** field in **Logs** |
| **Identifying your subscriptions** | No ID, denoted **config-managed** | Available as the **Subscription ID** field in **Logs**. [Query by subscription ID](https://shopify.dev/docs/api/admin-graphql/latest/queries/webhookSubscription). |
| **Interface for management** | Your app configuration file | GraphQL Admin API |
| **Metafield namespaces** | Does not support `metafieldNamespaces` | `metafieldNamespaces` can be used as an input field ([example](https://shopify.dev/docs/api/admin-graphql/latest/mutations/webhookSubscriptionCreate#argument-webhooksubscription)). |
| **Scopes** | Requires scopes in your app configuration file | Scopes can be configured in your app configuration file or in your Dev Dashboard. They **cannot** be set using the Admin API. |
| **[Topics](https://shopify.dev/docs/api/webhooks)** | Supports every topic except `product_feeds/full_sync`, `product_feeds/full_sync_finish`, and `product_feeds/incremental_sync`. | Supports every topic. |
| **[Troubleshooting](https://shopify.dev/docs/apps/build/webhooks/troubleshoot)** | Failing subscriptions will **not** be deleted by Shopify. | Failing subscriptions will be deleted by Shopify. |
| **Viewing subscriptions** | Available under **Subscriptions** in your app's Dev Dashboard > **Versions** > **Configuration** | Query the GraphQL Admin API ([example](https://shopify.dev/docs/api/admin-graphql/latest/queries/webhookSubscriptions)). |

Shopify recommends using Google Pub/Sub as a cloud-based solution for delivering webhooks. You can also use Amazon EventBridge. If you prefer to build your own webhooks infrastructure, you can deliver through HTTPS, but there are [extra considerations to take into account](https://shopify.dev/docs/apps/build/webhooks/verify-deliveries#https-delivery-considerations).

If you have shop-specific subscriptions and are migrating to app-specific subscriptions, remove existing subscriptions to the same topics first to avoid conflicts and duplicate notifications. See Migrate to app-specific subscriptions.

### App-specific subscriptions

You can subscribe your app to webhook topics using your app configuration file, rather than using the Admin API. Use this to configure and manage your subscriptions across all shops where your app is installed. Shopify recommends subscribing to webhooks using this approach.

#### App-specific subscription — shopify.app.toml

```toml
[webhooks]
api_version = "2026-04"

[[webhooks.subscriptions]]
topics = ["products/create"]
uri = "https://your-app.example.com/webhooks/products"
```

#### Response

```json
{
  "id": 9554194432293,
  "title": "T-Shirt",
  "status": "active",
  "vendor": "My Store",
  "product_type": "Shirts",
  "variants": [
    {
      "id": 123456789,
      "title": "Default Title",
      "price": "29.99",
      "sku": "TSHIRT-001"
    }
  ],
  "tags": "cotton, comfortable"
}
```

#### Subscription fields

Each webhook subscription is defined by a `[[webhooks.subscriptions]]` entry in your `shopify.app.toml` file. Every subscription requires the following fields:

| Field | Purpose |
| - | - |
| `topics` | One or more topic names to subscribe to (for example `products/create`). |
| `uri` | Delivery destination. HTTPS URL, AWS EventBridge ARN, or Google Pub/Sub URI. |

Additional optional fields are available for [filtering deliveries](https://shopify.dev/docs/apps/build/webhooks/delivery-filtering), [defining their response structure](https://shopify.dev/docs/apps/build/webhooks/delivery-structure), and identifying subscriptions:

| Field | Purpose |
| - | - |
| `include_fields` | Fields to include in the payload. If omitted, the full payload is sent. See [Delivery filtering](https://shopify.dev/docs/apps/build/webhooks/delivery-filtering). |
| `filter` | Filter expression to gate deliveries. See [Delivery filtering](https://shopify.dev/docs/apps/build/webhooks/delivery-filtering). |
| `name` | Subscription name. Shopify echoes this in the [`X-Shopify-Name` header](https://shopify.dev/docs/apps/build/webhooks/delivery-structure#headers). Use to label and differentiate subscriptions to the same topic. Alphanumeric, `-`, `_`, up to 50 characters. |

#### Migrate to app-specific subscriptions

If you have shop-specific subscriptions already, and are migrating your app to app-specific subscriptions, then make sure you first remove any existing webhook subscriptions to the same topics. This avoids potential conflicts and duplicate notifications.

1. Check the list of existing shop-specific webhook topics your app is subscribed to by using the [GraphQL Admin API `webhookSubscriptions` query](https://shopify.dev/docs/api/admin-graphql/latest/queries/webhookSubscriptions).
2. Delete the relevant queries, subscription, and handler code from your app.
3. Deploy a new version of your app by running `shopify app deploy`. You can check that your subscriptions have been deleted by checking the **Versions** page for your app in the Dev Dashboard.
4. Configure your app to subscribe to app-specific subscriptions. Refer to the [create a subscription](https://shopify.dev/docs/apps/build/webhooks/get-started) tutorial to get started.

### Shop-specific subscriptions

To subscribe to webhook topics where the configuration depends on the shop your app is installed on, use the GraphQL Admin API. For the available input fields, see [`WebhookSubscriptionInput`](https://shopify.dev/docs/api/admin-graphql/latest/input-objects/WebhookSubscriptionInput).

#### React Router template

Shopify recommends that you use the Shopify CLI and React Router template when subscribing to webhooks using the GraphQL Admin API. The template abstracts away the actual GraphQL mutation you would otherwise have to write.

In `app/shopify.server.ts`, add your subscription to the `webhooks` config and register it in the `afterAuth` hook:

**app/shopify.server.ts — Google Pub/Sub**

```js
const shopify = shopifyApp({
  webhooks: {
    ORDERS_CREATED: {
      deliveryMethod: DeliveryMethod.PubSub,
      pubSubProject: "<GCP-PROJECT>",
      pubSubTopic: "<PUB_SUB_TOPIC>",
    },
  },
  hooks: {
    afterAuth: async ({ session }) => {
      shopify.registerWebhooks({ session });
    },
  },
});
```

**app/shopify.server.ts — Amazon EventBridge**

```js
const shopify = shopifyApp({
  webhooks: {
    ORDERS_CREATED: {
      deliveryMethod: DeliveryMethod.EventBridge,
      arn: "<ARN>",
    },
  },
  hooks: {
    afterAuth: async ({ session }) => {
      shopify.registerWebhooks({ session });
    },
  },
});
```

If you're using Amazon EventBridge, set `arn` to the ARN that you retrieved when you associated your event bus during setup.

#### GraphQL Admin API

Use the [`webhookSubscriptionCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/webhookSubscriptionCreate) mutation. Specify the topic using GraphQL enum screaming case syntax (for example, `ORDERS_CREATE`).

**Request**: `POST /admin/api/2026-04/graphql.json`

```graphql
mutation webhookSubscriptionCreate($topic: WebhookSubscriptionTopic!, $webhookSubscription: WebhookSubscriptionInput!) {
  webhookSubscriptionCreate(topic: $topic, webhookSubscription: $webhookSubscription) {
    userErrors {
      field
      message
    }
    webhookSubscription {
      id
      format
      includeFields
      metafieldNamespaces
      topic
      uri
    }
  }
}
```

For Google Pub/Sub, set `uri` to `pubsub://{project-id}:{topic-id}`. For Amazon EventBridge, set `uri` to the ARN from your EventBridge console under **Partner Event Sources**.

Add this code wherever you process your after-authentication hooks. This is the equivalent of `app/shopify.server.ts` in the React Router template.

You can also test with [example GraphQL queries](https://shopify.dev/docs/api/admin-graphql/latest/queries/webhookSubscriptions#section-examples) using the [GraphiQL](https://shopify.dev/docs/api/usage/api-exploration/admin-graphiql-explorer) interface by pressing `g` in the console where your app is running. You must include values for the variables to execute the mutation.

When using Google Cloud Pub/Sub or Amazon EventBridge, deliveries include additional fields beyond the sample payloads in the [Webhooks reference](https://shopify.dev/docs/api/webhooks). HMAC verification is not required for cloud event bus deliveries.

#### Custom apps

Webhooks are available for all custom apps to use. However, custom apps created in the Shopify admin cannot take advantage of the tooling available through the Shopify CLI, including subscribing to webhook topics using the app configuration file.

This means that webhook subscriptions must be set up and configured using the GraphQL Admin API.

1. Create an app in the Shopify Admin and install it on your test shop to get your Admin API Access token.
2. Configure your Admin API scopes by selecting the scopes that you'll need for each webhook topic that you intend to subscribe to. Learn more about which topics require which Shopify scopes in the [Webhooks reference](https://shopify.dev/docs/api/webhooks).
3. Subscribe to webhook topics using the Admin API and your Admin API access token.

### Topics

A topic identifies both the resource and the action that qualifies a delivery. For example, `products/update` fires when an existing product changes; `products/create` fires when a new one is created. You can list multiple topics in a single subscription to route qualifying events from each to the same `uri`.

See the [Webhooks reference](https://shopify.dev/docs/api/webhooks) for the full list of supported topics and their required scopes.

**Try Events:** Events is in developer preview for a subset of topics. If your topic is supported, you can run an Events subscription alongside this webhook in the same `shopify.app.toml`. Check the [Events reference](https://shopify.dev/docs/api/events) for supported topics.

### Test your subscriptions

Use the Shopify CLI [`webhook trigger`](https://shopify.dev/docs/api/shopify-cli/app/app-webhook-trigger) command to test delivery. Pass flags directly or run with no parameters and follow the prompts:

```shell
shopify app webhook trigger --api-version=<version> --address=<destination> --topic=<topic-name>
```

For the `--address` flag, use the appropriate format for your delivery method:

| Delivery method | `--address` value |
| - | - |
| Amazon EventBridge | Your ARN from the EventBridge console under **Partner Event Sources** > **Select your event source** > **Partner event source ARN** |
| HTTPS | Your endpoint URL |
| Google Pub/Sub | `pubsub://{project-id}:{topic-id}` — your GCP project ID and Pub/Sub topic ID |

### Example

The following subscription listens for new product creations and delivers to a single endpoint. It uses no `filter` or `include_fields`, so every qualifying creation fires a delivery with the full product payload.

**Products subscription — shopify.app.toml**

```toml
[webhooks]
api_version = "2026-04"

[[webhooks.subscriptions]]
topics = ["products/create"]
uri = "https://your-app.example.com/webhooks/products"
```

**Response**

```json
{
  "id": 9554194432293,
  "title": "T-Shirt",
  "status": "active",
  "vendor": "My Store",
  "product_type": "Shirts",
  "variants": [
    {
      "id": 123456789,
      "title": "Default Title",
      "price": "29.99",
      "sku": "TSHIRT-001"
    }
  ],
  "tags": "cotton, comfortable"
}
```

### Next steps

- [Delivery filtering](https://shopify.dev/docs/apps/build/webhooks/delivery-filtering): Gate deliveries with `filter` expressions.
- [Delivery structure](https://shopify.dev/docs/apps/build/webhooks/delivery-structure): Shape the payload with `include_fields`.

---

## Filter webhook deliveries

> Fonte: https://shopify.dev/docs/apps/build/webhooks/delivery-filtering

By default, a subscription fires for every event that matches its topic. Delivery filtering lets you narrow that without changing your topic or subscription configuration.

`filter` is an optional expression on a webhook subscription that evaluates against the payload and suppresses the delivery if the expression resolves to false.

### Filters

Shopify evaluates the expression against the payload after the event occurs, using current field values at the time of delivery. Without it, every matching event fires a delivery regardless of its payload values.

**Without filter — shopify.app.toml**

```toml
[webhooks]
api_version = "2026-04"

[[webhooks.subscriptions]]
topics = ["products/update"]
uri = "https://example.com/webhooks"
```

**Response**

```json
{
  "id": 9554194432293,
  "title": "T-Shirt",
  "status": "active",
  "vendor": "My Store",
  "product_type": "Shirts",
  "variants": [
    {
      "id": 123456789,
      "title": "Default Title",
      "price": "29.99",
      "taxable": true,
      "weight": 0.2
    }
  ],
  "tags": "cotton"
}
```

Adding `filter` suppresses deliveries where the expression evaluates to false. You can set it in your app configuration file using the `filter` argument, or with the `filter` input field in the `webhookSubscription` argument using the GraphQL Admin API.

**Filter products/update webhooks — filter definition (shopify.app.toml)**

```toml
[webhooks]
api_version = "2026-04"

[[webhooks.subscriptions]]
topics = ["products/update"]
uri = "https://example.com/webhooks"
filter = "id:* AND status:active AND (product_type:Music OR product_type:Movies) AND variants.taxable:true AND variants.weight:<5 AND variants.price:>=100 AND variants.title:Album*"
```

**GraphQL**

```graphql
mutation subscribeToWebhook {
  webhookSubscriptionCreate(
    topic: PRODUCTS_UPDATE,
    webhookSubscription: {
      uri: "https://example.com/webhooks"
      filter: "id:* AND status:active AND (product_type:Music OR product_type:Movies) AND variants.taxable:true AND variants.weight:<5 AND variants.price:>=100 AND variants.title:Album*"
    }
  ) {
    webhookSubscription {
      id
      createdAt
      uri
      filter
    }
    userErrors {
      field
      message
    }
  }
}
```

**Response**

```json
{
  "id": 9554194432293,
  "title": "Greatest Hits Collection",
  "status": "active",
  "product_type": "Music",
  "vendor": "My Store",
  "variants": [
    {
      "id": 123456789,
      "title": "Album Edition",
      "price": "129.99",
      "taxable": true,
      "weight": 0.2,
      "sku": "GHC-001"
    }
  ],
  "tags": "music, vinyl"
}
```

#### Syntax

`filter` uses Shopify API search syntax. You can combine conditions with `AND`, `OR`, and parentheses:

```toml
filter = "status:active AND (product_type:Music OR product_type:Movies) AND variants.price:>=100"
```

You denote nested fields using a period:

```json
"variants.price:>=10.00"
```

#### Differences from search

`filter` shares Shopify's search syntax but behaves differently in several cases:

| | `filter` | Search |
|---|---|---|
| **Invalid field** | No deliveries sent | All documents returned |
| **`:` operator** | Equality | Fuzzy match when fields are tokenized |
| **Field specification** | Must be explicit | Term searches supported |
| **Case sensitivity** | Case-sensitive | Case-insensitive |

### Array fields

For fields that contain arrays of objects, the filter matches if at least one object in the array meets the condition. For example, given a payload with a `line_items` array:

**Example payload**

```json
"line_items": [
  {
    "product_exists": true,
    "product_id": 9554194432293,
    "properties": []
  },
  {
    "product_exists": true,
    "product_id": 9554194465061,
    "properties": [
      { "name": "_your_custom_property", "value": "some-value" }
    ]
  }
]
```

The following delivers because at least one item in `line_items` contains a property where `name` is `_your_custom_property`:

```json
"line_items.properties.name:_your_custom_property"
```

This means that if any `line_items` has at least one matching object in its `properties` array, Shopify delivers the webhook.

#### Tag fields

Tags are arrays in the data model but are serialized as a string in the webhook payload for topics like `products/update` and `orders/updated`. Treat each tag as a keyword in a string rather than a distinct array value.

#### Variant fields

`variants` is a top-level payload field. If any one variant satisfies the filter condition, the webhook fires on any product update, including unrelated changes like a title edit.

**Filter products/update webhooks — filter definition (shopify.app.config-name.toml)**

```toml
[webhooks]
api_version = "2026-04"

[[webhooks.subscriptions]]
topics = ["products/update"]
uri = "https://example.com/webhooks"
filter = "id:* AND status:active AND (product_type:Music OR product_type:Movies) AND -invalid_field:* AND variants.taxable:true AND variants.weight:<5 AND variants.price:>=100 AND variants.title:Album*"
```

**GraphQL**

```graphql
mutation subscribeToWebhook {
  webhookSubscriptionCreate(
    topic: PRODUCTS_UPDATE,
    webhookSubscription: {
      uri: "https://example.com/webhooks"
      filter: "id:* AND status:active AND (product_type:Music OR product_type:Movies) AND -invalid_field:* AND variants.taxable:true AND variants.weight:<5 AND variants.price:>=100 AND variants.title:Album*"
    }
  ) {
    webhookSubscription {
      id
      createdAt
      uri
      filter
    }
    userErrors {
      field
      message
    }
  }
}
```

**Response**

```json
{
  "id": 9554194432293,
  "title": "Greatest Hits Collection",
  "status": "active",
  "product_type": "Music",
  "vendor": "My Store",
  "variants": [
    {
      "id": 123456789,
      "title": "Album Edition",
      "price": "129.99",
      "taxable": true,
      "weight": 0.2,
      "sku": "GHC-001"
    }
  ],
  "tags": "music, vinyl"
}
```

### Constraints

Filters are available as of the `2024-07` API version.

`filter` expressions are validated when the subscription is created or updated, and must reference valid payload fields:

- **Validation**: An invalid field or type mismatch allows the subscription to be created but suppresses all deliveries. Incorrect syntax prevents the subscription from being created entirely.
- **`include_fields` dependency**: If `include_fields` is set, all fields referenced in the filter must also appear in `include_fields`. See Delivery structure.

Some topics require a filter. The `metaobjects/create`, `metaobjects/update`, and `metaobjects/delete` topics require a filter using `type:{type}` where `{type}` is the metaobject definition's type:

```toml
[[webhooks.subscriptions]]
topics = ["metaobjects/create"]
uri = "https://example.com/webhooks"
filter = "type:my-metaobject-type"
```

To subscribe to multiple types, specify each explicitly:

```toml
filter = "type:banana OR type:apple"
```

Wildcards like `type:*` aren't supported.

For app-owned definitions, use the full type value (`app--{your-app-id}--{some-namespace}`); the `$app:{some-namespace}` shorthand isn't supported.

### Example

Suppose you want your app notified only when a `products/update` event includes a variant priced at or above $10.00. Without filtering, your subscription fires for every product update regardless of price.

The following subscription adds a filter to gate deliveries to that condition:

**Filter by variant price — shopify.app.toml**

```toml
[[webhooks.subscriptions]]
topics = ["products/update"]
uri = "https://example.com/webhooks"
filter = "variants.price:>=10.00"
```

**Response**

```json
{
  "id": 9554194432293,
  "title": "Widget",
  "status": "active",
  "vendor": "My Store",
  "product_type": "Gadgets",
  "variants": [
    {
      "id": 123456789,
      "title": "Default Title",
      "price": "29.99",
      "sku": "WIDGET-001"
    }
  ]
}
```

After you apply this filter, your app receives `products/update` webhooks for updates to products where at least one variant's price is at least $10.00.

### Next steps

- Delivery structure: Payload fields, `include_fields`, and how `filter` and `include_fields` interact.
- Verify deliveries: HMAC validation and deduplication.

---

## Webhooks delivery structure

> Fonte: https://shopify.dev/docs/apps/build/webhooks/delivery-structure

Each qualifying change sends a delivery to your `uri` as an HTTP POST with a JSON body and a set of headers. By default, the body is the full REST resource payload for the topic.

Add `include_fields` to receive only the specific fields your app needs.

### Payload

Every delivery includes a JSON body containing the full REST resource for the subscribed topic. The shape and fields depend on the topic. See the [Webhooks reference](https://shopify.dev/docs/api/webhooks) for the payload structure of each topic.

**Example payload (products/update)**

```json
{
  "id": 9554194432293,
  "title": "T-Shirt",
  "status": "active",
  "vendor": "My Store",
  "product_type": "Shirts",
  "updated_at": "2025-04-22T14:30:00-05:00",
  "variants": [
    {
      "id": 123456789,
      "title": "Default Title",
      "price": "29.99",
      "sku": "TSHIRT-001",
      "taxable": true,
      "updated_at": "2025-04-22T14:30:00-05:00"
    }
  ],
  "tags": "cotton, comfortable"
}
```

### Headers

Every delivery includes the following headers. Treat header names as case-insensitive in your code, as HTTP/2 often lowercases them.

| Header | Description |
| - | - |
| `X-Shopify-Topic` | The topic name (for example, `products/update`). |
| `X-Shopify-Hmac-Sha256` | Base64-encoded HMAC signature for verifying the delivery came from Shopify. HTTPS only. |
| `X-Shopify-Shop-Domain` | The `myshopify.com` domain of the store that triggered the event. |
| `X-Shopify-API-Version` | The API version used to serialize the payload. |
| `X-Shopify-Webhook-Id` | A unique composite key per delivery. Use to identify and deduplicate individual deliveries. |
| `X-Shopify-Triggered-At` | Timestamp of when Shopify triggered the delivery. |
| `X-Shopify-Event-Id` | A unique ID shared across all deliveries produced by the same merchant action. |
| `X-Shopify-Name` (optional) | Developer-supplied subscription name, set via the `name` field in your subscription. |

### `include_fields`

`include_fields` is an optional array of field paths on a webhook subscription. When set, the delivery payload includes only the specified fields instead of the full resource.

Without `include_fields`, every delivery includes the complete resource payload:

**Without include_fields — shopify.app.toml**

```toml
[webhooks]
api_version = "2026-04"

[[webhooks.subscriptions]]
topics = ["products/update"]
uri = "https://your-app.example.com/webhooks/products"
```

**Response**

```json
{
  "id": 9554194432293,
  "title": "T-Shirt",
  "status": "active",
  "vendor": "My Store",
  "product_type": "Shirts",
  "updated_at": "2025-04-22T14:30:00-05:00",
  "variants": [
    {
      "id": 123456789,
      "title": "Default Title",
      "price": "29.99",
      "sku": "TSHIRT-001",
      "taxable": true,
      "updated_at": "2025-04-22T14:30:00-05:00"
    }
  ],
  "tags": "cotton, comfortable"
}
```

Adding `include_fields` narrows the payload to only the specified fields. You denote nested fields using a period (for example, `variants.price`). You can also set `include_fields` using the `includeFields` input in the [`webhookSubscriptionCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/webhookSubscriptionCreate) mutation.

**With include_fields — shopify.app.toml**

```toml
[webhooks]
api_version = "2026-04"

[[webhooks.subscriptions]]
topics = ["products/update"]
uri = "https://your-app.example.com/webhooks/products"
include_fields = ["id", "variants.id", "variants.price", "updated_at"]
```

**Response**

```json
{
  "id": 9554194432293,
  "variants": [
    {
      "id": 123456789,
      "price": "29.99"
    }
  ],
  "updated_at": "2025-04-22T14:30:00-05:00"
}
```

#### Debouncing

When `include_fields` reduces the payload to a small set of fields, multiple qualifying events might produce identical payloads. Shopify debounces deliveries with identical payloads that arrive within a short time window, dropping the later one. For example, a subscription to `orders/updated` with `include_fields = ["id", "line_items.title"]` would debounce consecutive price changes, since neither the order ID nor line item titles change between them.

To prevent debouncing, include a field that always has a unique value. For example, `updated_at` changes with every update, ensuring no two consecutive deliveries are identical.

#### Combining with `filter`

When both `filter` and `include_fields` are set, all fields referenced in the filter expression must also appear in `include_fields`.

```toml
[webhooks]
api_version = "2026-04"


[[webhooks.subscriptions]]
topics = ["products/update"]
uri = "https://example.com/webhooks"
include_fields = ["id", "status", "product_type", "variants.taxable", "variants.price", "variants.title", "updated_at"]
filter = "id:* AND status:active AND (product_type:Music OR product_type:Movies) AND variants.taxable:true AND variants.price:>=100 AND variants.title:'The Miseducation of'"
```

See [Delivery filtering](https://shopify.dev/docs/apps/build/webhooks/delivery-filtering) for filter syntax and examples.

### Example

Suppose you want deliveries only when an active product in the Music or Movies category has a variant priced above $100. The following subscription combines `include_fields` to narrow the payload and `filter` to gate delivery:

**Active high-price music or movies product — shopify.app.toml**

```toml
[webhooks]
api_version = "2026-04"

[[webhooks.subscriptions]]
topics = ["products/update"]
uri = "https://your-app.example.com/webhooks/products"
include_fields = ["id", "status", "product_type", "variants.id", "variants.price", "updated_at"]
filter = "status:active AND (product_type:Music OR product_type:Movies) AND variants.price:>=100"
```

**Response**

```json
{
  "id": 9554194432293,
  "status": "active",
  "product_type": "Music",
  "variants": [
    {
      "id": 123456789,
      "price": "129.99"
    }
  ],
  "updated_at": "2025-04-22T15:00:00-05:00"
}
```

### Next steps

- [Delivery filtering](https://shopify.dev/docs/apps/build/webhooks/delivery-filtering): Gate deliveries with `filter` expressions.
- [Verify deliveries](https://shopify.dev/docs/apps/build/webhooks/verify-deliveries): HMAC verification and deduplication.

---

## Verify webhook deliveries

> Fonte: https://shopify.dev/docs/apps/build/webhooks/verify-deliveries

Each delivery includes an HMAC signature to confirm it came from Shopify, and a delivery ID you can use to detect duplicates. Verify both before processing. If you're delivering over HTTPS, see HTTPS delivery considerations for additional requirements.

### HMAC verification

Each HTTPS delivery includes a base64-encoded HMAC signature in the [`X-Shopify-Hmac-SHA256` header](https://shopify.dev/docs/apps/build/webhooks/delivery-structure#headers), generated using your app's client secret and the raw request body. Verify this signature before processing to confirm the delivery came from Shopify. HMAC verification applies to HTTPS deliveries only. Google Cloud Pub/Sub and Amazon EventBridge deliveries don't require it.

If you're using the [React Router template](https://shopify.dev/docs/api/shopify-app-react-router/latest/guide-webhooks#endpoints), verification is handled automatically before your handler runs:

**app/routes/webhooks.jsx**

```javascript
import { authenticate } from "../shopify.server";

export const action = async ({ request }) => {
  const { shop, session, topic } = await authenticate.webhook(request);

  console.log(`Received ${topic} webhook for ${shop}`);

  return new Response();
};
```

Always verify HMAC before trusting payload contents. Skip verification only in development with mock tools. If you [rotate your app's client secret](https://shopify.dev/docs/apps/build/authentication-authorization/client-secrets/rotate-revoke-client-credentials), it can take up to an hour for the HMAC digest to be generated using the new secret.

#### Manual verification

To validate manually, compute HMAC-SHA256 of the raw request body using your app's client secret as the key, then compare it to the decoded header value. Reject any delivery where the signatures don't match.

**Compute HMAC digest**

```javascript
const express = require('express');
const crypto = require('crypto');
const app = express();

const appClientSecret = process.env.CLIENT_SECRET;

app.use(express.raw({ type: '*/*' }));

app.post('*', (req, res) => {
  const shopifyHmac = req.headers['x-shopify-hmac-sha256'];
  const calculatedHmacDigest = crypto.createHmac('sha256', appClientSecret).update(req.body).digest('base64');
  const hmacValid = crypto.timingSafeEqual(Buffer.from(calculatedHmacDigest, 'base64'), Buffer.from(shopifyHmac, 'base64'));

  if (hmacValid) {
    res.send('HMAC validation successful.');
  } else {
    res.status(401).send('HMAC validation failed.');
  }
});
```

Or use the [ShopifyApp library](https://shopify.dev/docs/api/shopify-app-react-router/latest/entrypoints/shopifyapp) to handle header processing, stringifying, and payload parsing:

**Validate HMAC digest**

```javascript
app.post('/webhooks', express.text({type: '*/*'}), async (req, res) => {
  const {valid, topic, domain} = await shopify.webhooks.validate({
    rawBody: req.body, // is a string
    rawRequest: req,
    rawResponse: res,
  });

  if (!valid) {
    // This is not a valid request!
    res.send(400); // Bad Request
  }

  // Run my webhook-processing code here
});
```

For more details, refer to the library documentation for [webhooks](https://github.com/Shopify/shopify-app-js/blob/main/packages/apps/shopify-api/docs/guides/webhooks.md) and [validation](https://github.com/Shopify/shopify-app-js/blob/main/packages/apps/shopify-api/docs/reference/webhooks/validate.md).

When validating manually, watch for these common issues:

- **Raw body parsing**: HMAC verification requires the raw request body. If you're using a body parser middleware like `express.json()`, it parses the body before your verification code runs. Capture the raw body before it's parsed.
- **Middleware order**: Place your webhook verification middleware before any body parsing middleware in your app.
- **Encoding**: Ensure your encoding is set correctly.

### Ignoring duplicates

Shopify minimizes duplicate deliveries, but your app might receive the same webhook more than once, for example after a network timeout or a retry.

Process webhooks using idempotent operations so that receiving the same webhook twice doesn't produce a different outcome. If your processing isn't idempotent, use the `X-Shopify-Webhook-Id` header to detect and skip duplicates:

1. Extract `X-Shopify-Webhook-Id` from the request headers.
2. Check your persistent store for that ID.
3. If it exists, skip processing and return a success response.
4. If it's new, process the delivery and save the ID.

**Note:** If you have more than one subscription for the same topic, you'll receive a separate delivery per subscription. Each has a different `X-Shopify-Webhook-Id` but shares the same `X-Shopify-Event-Id`. Use `X-Shopify-Webhook-Id` to deduplicate individual deliveries. Use `X-Shopify-Event-Id` to correlate deliveries that originated from the same merchant action.

### HTTPS delivery considerations

The following applies when using HTTPS delivery. Cloud-based event buses (Google Pub/Sub and Amazon EventBridge) handle these concerns for you. Shopify sends an HTTP POST request to your URI and verifies SSL certificates on delivery.

During development, your CloudFlare tunnel URL changes each time you run `shopify app dev`. Use a relative path for your URI to avoid updating your subscription on each restart: `uri = "/webhooks"`.

#### Respond with a 200 OK quickly

Your system acknowledges receipt by sending Shopify a `200 OK` response. Any response outside the 200 range, including 3XX codes, is treated as an error. Shopify has a one-second connection timeout and a five-second timeout for the entire request.

Shopify's delivery system uses [HTTP Keep-Alive](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Keep-Alive) to reuse connections to the same host. Ensure `Keep-Alive` is enabled on your endpoint to reduce overhead from concurrent requests.

#### Queue webhooks to handle traffic bursts

Queuing is a useful pattern for handling bursts of traffic and for ensuring you respond within five seconds. Install a package like [Better Queue](https://www.npmjs.com/package/better-queue) to store payloads and process them asynchronously. A common practice is to also build a reconciliation job that periodically retrieves data you might have missed using Shopify APIs.

#### Retries and failures

If Shopify receives no response or an error, it retries 8 times over the next 4 hours. After 8 consecutive failures, the subscription is automatically deleted if it was configured using the Admin API. Warning emails are sent to the app's emergency developer email address. See [Troubleshoot webhooks](https://shopify.dev/docs/apps/build/webhooks/troubleshoot) for more information.

### Next steps

- [Troubleshoot webhooks](https://shopify.dev/docs/apps/build/webhooks/troubleshoot): Diagnose delivery failures and inspect logs.
- [Webhooks reference](https://shopify.dev/docs/api/webhooks): Full list of topics, payloads, and required scopes.

---

## Troubleshoot webhooks

> Fonte: https://shopify.dev/docs/apps/build/webhooks/troubleshoot

If your app uses webhooks, monitor for and respond to failed delivery notifications. Shopify retries failed webhook calls up to eight times in a four-hour period, but if failures persist, the subscription is removed.

If your app was created in the Dev Dashboard or using Shopify CLI, you can use the delivery metrics report to troubleshoot delivery failures and view performance data.

This guide shows you how to use the delivery metrics report to track failed deliveries and fix them before they affect app users.

### Monitor performance

The **Monitoring** page shows delivery counts and response time for each topic over the past 7 days. For an overview of all monitoring tools in the Dev Dashboard, see [Monitoring and logs](https://shopify.dev/docs/apps/build/dev-dashboard/monitoring-and-logs).

1. From your [Dev Dashboard](https://dev.shopify.com/dashboard), click **Apps**.
2. Click the name of your app.
3. In the sidebar, click **Monitoring**.

**Tip:** You can manually trigger a webhook to check delivery metrics by updating your dev store. For example, create a product to trigger `products/create`.

You can focus on Events and webhooks from the **Webhooks** tab, change the delivery window for the dashboard using the dropdown, and filter on specific delivery types using the **Topic +** selector.

From this view you can inspect the following plots:

- **Deliveries:** Successful deliveries and errors over the course of the selected delivery window and topic filters.
- **Response time:** Average response time for your app within the window.

The monitoring table lists the following information for each topic:

| Metric | Description |
| - | - |
| Removed webhooks | The number of removed webhook subscriptions. Webhooks are retried up to 8 times. After multiple failures in a 24-hour period, the webhook subscription is removed. |
| Failed delivery rate | The percentage of unsuccessful delivery attempts out of the total number of delivery attempts. |
| Total deliveries | The total number of delivery attempts across all subscriptions for the topic. |
| Response time | The 90th percentile of your app's response time. 90% of responses were equal to or faster than the listed time. |

From the **Monitoring** page, you can also view your app's delivery logs and delivery details.

### View delivery logs

The **Logs** page shows individual deliveries filterable by topic, status, and destination shop over the past 7 days.

1. From your [Dev Dashboard](https://dev.shopify.com/dashboard), click **Apps**.
2. Click the name of your app.
3. In the sidebar, click **Logs**.

**Note:** The delivery logs dashboard doesn't provide real-time updates. Data could be delayed up to several minutes.

You can focus on Events and webhooks from the **Webhooks** tab, change the delivery window for the dashboard using the dropdown, and filter on specific delivery types using the **Topics +**, **Shops +** and **Status +** selectors.

After clicking on an individual delivery, you can investigate the following:

| Field | Description |
| - | - |
| Response | The response code your app sent when it received the webhook. |
| Topic | The topic the subscription is listening to. |
| Shop | The URL of the Shopify store associated with the delivery. |
| Time | The date and time of the most recent delivery attempt. |

#### Responses and retries

A `200` series status response is considered successful. If your app has a high rate of successful responses, then the logs display a sample of successful responses.

If your app doesn't respond with a `200` series status code, the delivery has failed. Shopify retries failed deliveries up to 8 times.

#### Prioritize fixes

Use the response code and retry count to decide which webhooks to fix first. Prioritize webhooks with any of the following:

- **Removed response**: Removed webhook subscriptions won't receive any deliveries unless you create them again.
- **Delivery failed after retries**: After 8 failed delivery attempts, Shopify stops attempting delivery. You might need to recover missing data.
- **High failure rates on a single webhook**: A high rate on one webhook may indicate a handler-specific or payload-specific error.
- **High failure rates across all webhooks**: If all your webhooks have a high failure rate, your backend may not be responding. Use your monitoring tools to investigate.

#### View delivery details

When you click a delivery from the **Logs** page, a panel opens with the following information.

The details panel lists the following information for each delivery:

| Field | Description |
| - | - |
| Topic | The topic the subscription is listening to. |
| URI | The endpoint the delivery was sent to. |
| Subscription method | How the subscription was created, for example App specific. |
| API version | The API version used for the delivery. |
| Subscription ID | The ID of the webhook subscription. |
| Webhook ID | The unique ID of this delivery. |
| Response | The HTTP status code your app returned. |
| Time | The timestamp of the delivery attempt in EDT, UTC, and relative time. |
| Shop | The domain of the store that triggered the delivery. |
| Shop ID | The ID of the store that triggered the delivery. |
| Payload size | The size of the delivery payload. |
| Response time | The time between the delivery request and your app's response. If your app doesn't respond within five seconds, the delivery fails. |
| Delivery attempt | The attempt number for this delivery. |
| Delivery method | The method used to deliver the webhook, for example `http`. |
| HMAC SHA-256 | The HMAC signature sent with the delivery. Use this to verify the delivery came from Shopify. See [Verify deliveries](https://shopify.dev/docs/apps/build/webhooks/verify-deliveries). |
| HTTP headers | The HTTP headers sent with the delivery. |

### Troubleshoot delivery failures

Delays caused by webhook failures can affect app users. Each time a delivery fails, the interval before the next retry increases. This can cause your data to become out of sync, especially if you process many events or time-sensitive data.

To identify and resolve failed deliveries, look for the following issues:

| Issue | Description |
| - | - |
| Failed delivery rates over 0.5% | This is a higher-than-average failure rate and might mean your webhook is failing across multiple stores, or has failed multiple times in a row. A high failure rate on one topic might indicate a store-specific or payload-specific error. |
| Removed webhooks | Your app isn't receiving data for subscriptions removed after multiple failed delivery attempts. Fix the issue, then recreate the webhook subscriptions. |
| Response times between four and five seconds | Your app must respond to the webhook within five seconds. To resolve timeout failures, delay processing until after you've sent a response. |
| Same failure rates across all topics | If all your topics have a high failure rate, your backend might not be responding. Use your monitoring tools to investigate. |

### Manage delays

You might experience delays receiving webhooks. If receiving webhooks up to a day late might cause issues in your app, then compare the timestamp of the webhook to the current date and time.

### Recover from a downtime event

If your app goes offline for an extended period of time, then you can recover by re-subscribing to your webhook topics (if applicable) and importing the missing data.

You don't need to re-subscribe if your app uses [app-specific webhook subscriptions](https://shopify.dev/docs/apps/build/webhooks/subscribe#app-specific-vs-shop-specific-subscriptions). For [shop-specific webhook subscriptions](https://shopify.dev/docs/apps/build/webhooks/subscribe#app-specific-vs-shop-specific-subscriptions), consult the app's code that initially created the subscriptions. You can add a check that fetches all the existing subscriptions and creates only the ones that you need.

To import the missing data, you can fetch data from the outage period and feed it into your webhook processing code.

### Next steps

- [Webhooks reference](https://shopify.dev/docs/api/webhooks): Browse supported webhook topics and payload structures.
- [Verify deliveries](https://shopify.dev/docs/apps/build/webhooks/verify-deliveries): Verify HMAC signatures and handle duplicate webhook deliveries.

---

# Billing

Mini-indice della sezione:

- [About billing for your app](#about-billing-for-your-app)
- [Shopify App Pricing](#shopify-app-pricing)
- [Setup subscription charges (Shopify App Pricing)](#setup-subscription-charges-shopify-app-pricing)
- [Setup usage charges (Shopify App Pricing)](#setup-usage-charges-shopify-app-pricing)
- [Offer free trials](#offer-free-trials)
- [About manual pricing (legacy Billing API)](#about-manual-pricing-legacy-billing-api)
- [Create time-based subscriptions (manual pricing)](#create-time-based-subscriptions-manual-pricing)
- [Create usage-based subscriptions (manual pricing)](#create-usage-based-subscriptions-manual-pricing)
- [Support one-time app purchases (manual pricing)](#support-one-time-app-purchases-manual-pricing)

---

## About billing for your app

> Fonte: https://shopify.dev/docs/apps/launch/billing

Shopify App Pricing enables you to monetize apps distributed through the Shopify App Store. It creates a predictable, trustworthy, and standardized experience for merchants, and an easy way to setup pricing for public app developers.

### How Shopify App Pricing helps

Shopify App Pricing provides the following benefits:

- **Simplified payment process**: Charges are directly added to the merchant's Shopify invoice.
- **Increased conversion rates**: Apps that use Shopify App Pricing experience higher rates of customers transitioning from free to paid versions, because of higher trust and charges originating directly from Shopify.
- **Revenue sharing**: You automatically receive a share of the revenue that Shopify collects.
- **Chargeback handling**: Shopify handles all chargeback-related processes.
- **Flexible pricing models**: Shopify supports a wide range of common pricing models that merchants have come to expect.

### Shopify App Pricing

Shopify App Pricing is the default and recommended approach for all apps published on the Shopify App Store. Define plans in the app submission form and let Shopify host your plan selection page and automate billing, trials, proration, upgrades, and downgrades. Shopify App Pricing supports recurring and usage charges, enabling you to send billable usage events via the App Events API.

**Important:** All apps published on the Shopify App Store are required to use a Shopify provided billing solution and adhere to the terms and conditions of the Shopify Partner Program Agreement.

Shopify App Pricing is available for free, monthly and annual recurring, and various usage-based plan types.

### Manual Pricing (Legacy)

Manual pricing is still supported but is the legacy method for handling app billing. With manual pricing, you build your own billing logic and pricing page using the Billing API to create recurring, usage, or one-time charges.

This option remains available for apps that have specific requirements not covered by Shopify App Pricing yet, and for existing app developers who are using it.

### Supported currencies

You can match your app charges to a merchant's local billing currency if they use one of the supported currencies.

Retrieve the merchant's local billing currency with the GraphQL Admin API's `shopBillingPreferences` query, passing the currency value as input.

### Best practices

Consider the following best practices when developing your app's pricing model:

| Practice | Benefit | Example |
| - | - | - |
| **Provide simple and intuitive pricing** | Makes it easier for merchants to understand the pricing model and encourages adoption. | If your app provides a single set of features for all merchants, then consider setting up time-based subscriptions at 30 or 365-day intervals. |
| **Limit the number of plans** | Makes it easier for merchants to compare plans and identify which plan works best for them. | If your app provides tiered features, then consider setting up a basic plan and a pro plan. Use usage based pricing where appropriate to differentiate plans. |
| **Offer free trials** | Encourages merchants and Partners that develop stores for merchants to try your app before they pay for it. | Align with Shopify's free trial or $1 plan to encourage merchants to fully try your apps. |
| **Create charges in the merchant's local billing currency** | Enables merchants to better budget their app spend, which prevents confusion and provides a better app experience. | If a merchant is in India, then bill them in Indian Rupees (INR). If they're in Canada, then bill them in Canadian Dollars (CAD). |

---

## Shopify App Pricing

> Fonte: https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing

**Info:** Managed Pricing has been renamed to **Shopify App Pricing** and expanded with new features, including App Events, App Billing Events, and the Active Subscription and Historical Events APIs in the Partner API. If your app was using Managed Pricing, it is now part of Shopify App Pricing. See [Migrating to Shopify App Pricing](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/migrating-to-shopify-app-pricing) for what's changed and what you may need to update.

Shopify App Pricing lets you define your app's pricing plans directly in the app submission form, without needing to use the Billing API. Shopify hosts your app's plan selection page, and automates most common billing tasks, such as recurring charges, usage-based pricing, free trials, proration, test charges, and price updates.

For most developers, Shopify App Pricing is simpler and more consistent than coding your own billing logic using the Billing API.

### Pricing models

Shopify App Pricing supports the following billing models:

- **Recurring charges**: Bill merchants on a regular schedule with free, monthly, yearly, or monthly-with-yearly-discount plans. Learn more about [setting up subscription charges](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/subscription-billing/setup-subscription-charges).
- **Usage-based pricing**: Charge merchants based on actual usage using fixed, graduated, or volume pricing structures. Learn more about [setting up usage charges](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/subscription-billing/setup-usage-charges).
- **Combined pricing**: Combine recurring fees with usage-based charges for hybrid plans. Learn more about [combined subscription and usage](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/subscription-billing/combined-subscription-and-usage).

You can also configure [free trials](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/subscription-billing/offer-free-trials), [public and private plans](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/plans), and welcome links for each plan.

### Set up Shopify App Pricing

Shopify App Pricing is the default option when you submit a new public app for approval. Existing apps without active paid merchants can opt into Shopify App Pricing by selecting the option. This will be available for all developers soon. Learn more about [migrating](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/migrating-to-shopify-app-pricing).

#### Opt in to Shopify App Pricing

If you've already created plans with the Billing API that aren't compatible with Shopify App Pricing, then you'll need to remove them before you can switch.

1. From your Partner Dashboard, click **Apps > All Apps** and click the name of the app you want to update pricing for.
2. Click **Distribution**.
3. Beside **Shopify App Store listing**, click **Manage listing**.
4. Under **Published languages**, click **Edit** for the locale you want to update.
5. Under **Pricing content**, click **Manage** to open the Pricing index page.
6. Click **Settings**.
7. Select **Shopify App Pricing**.
8. In the confirmation dialog, click **Switch**.

### Plan selection page

When using Shopify App Pricing, Shopify hosts your plan selection page. It's visible in the Shopify admin, and allows merchants to view and select their plan.

Your app's plan selection page URL follows this pattern:

```text
https://admin.shopify.com/store/:store_handle/charges/:app_handle/pricing_plans
```

Learn how to [redirect merchants to the plan selection page](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/redirect-plan-selection-page) in your app.

### Redirection URL

The redirection URL is where merchants are redirected after approving your app plan charge. You can configure welcome links on a per-plan basis to customize your app onboarding experience.

- **Apps with a landing page in [App Home](https://shopify.dev/docs/api/app-home)**: Specify a relative path to your app root, such as `/welcome`. Your `plan_handle` URL parameter is appended to all redirect URLs which is a plan that merchant is subscribed to.
- **Apps without a landing page in App Home**: Redirect to a valid URL (including the `http` or `https` protocol). URL parameters for the `plan_handle` and the merchant shop domain are appended to redirect URLs.

After a merchant approves a charge, query the Partner API to confirm the subscription status. See query subscription data for details. If you enrolled before April 2026, refer to legacy Billing API queries.

### Testing

#### Test plan

Shopify App Pricing includes a $0 private test plan that you can use to configure and test your billing integration without charging merchants. The test plan is available in the **Private plans** section of your app's pricing configuration in the Partner Dashboard. Use it to verify that your usage meters, welcome links, and billing events work correctly before publishing a public plan.

#### Testing your plan selection UI

You can validate that plan selection works as expected by following the [test charge documentation](https://shopify.dev/docs/apps/launch/app-store-review/pass-app-review#test-your-app-s-billing-system).

### Query subscription data

With Shopify App Pricing, you use the [Partner API](https://shopify.dev/docs/api/partner) to retrieve both a merchant's current subscription status and their subscription history. This is different from the [Billing API](https://shopify.dev/docs/apps/launch/billing/manual-pricing), where subscription status comes from the GraphQL Admin API.

For Partner API setup — including [authentication](https://shopify.dev/docs/api/partner#authentication), [creating a Partner API client](https://shopify.dev/docs/api/partner#create-a-partner-api-client), [rate limits](https://shopify.dev/docs/api/partner#rate-limits), and [error handling](https://shopify.dev/docs/api/partner#error-handling) — see the [Partner API technical reference](https://shopify.dev/docs/api/partner).

#### Subscription status

Query `activeSubscription(appId:, shopId:)` on the [Partner API](https://shopify.dev/docs/api/partner/active-subscription) to get a merchant's current subscription, including the active plan, billing period, current billing cycle, subscription items (with pricing and usage), discounts, and any pending updates. This is the canonical way to check "what is this merchant subscribed to right now?" — the query returns the live contract state, not a derived view of historical events.

**Partner API — GraphQL query**

```graphql
query ActiveSubscription($appId: ID!, $shopId: ID!) {
  activeSubscription(appId: $appId, shopId: $shopId) {
    billingPeriod
    cancelAtEndOfCycle
    trialEndsAt
    currentBillingCycle {
      startTime
      endTime
    }
    items {
      handle
      description
      price {
        __typename
        active
        currency
        ... on FlatRatePrice {
          amount
        }
        ... on TieredPrice {
          tiersMode
          tiers {
            upTo
            amountPerUnit
            amount
          }
        }
      }
      discount {
        amount
        percentage
        remainingDiscountCycles
      }
      usage {
        quantity
        cost {
          amount
          currencyCode
        }
      }
    }
    pendingUpdate {
      billingPeriod
      items {
        handle
      }
    }
  }
}
```

**Variables**

```json
{
  "appId": "gid://shopify/App/1234",
  "shopId": "gid://shopify/Shop/5678"
}
```

`activeSubscription` returns `null` when the shop doesn't have an active Shopify App Pricing contract for the app. It only works for public apps.

For full field reference, including trial behavior, pending updates, and legacy subscription IDs, see [Active Subscription](https://shopify.dev/docs/api/partner/active-subscription) in the Partner API docs.

#### App / subscription history

Use the root `events` query on the [Partner API](https://shopify.dev/docs/api/partner/historical-events) to retrieve your app's event history across all merchants — installs, uninstalls, plan changes, cancellations, freezes, charges, earnings, and credits. The query returns events in reverse chronological order by default. Filter by `subjectId` and `shopId` to scope results to a specific app and merchant.

Filter by event types to get just the information you need:

**Partner API — Subscription events**

```graphql
{
  events(
    filter: {
      eventTypes: [
        SUBSCRIPTION_CREATED,
        SUBSCRIPTION_UPDATED,
        SUBSCRIPTION_CANCELLATION_SCHEDULED,
        SUBSCRIPTION_CANCELED,
        SUBSCRIPTION_FROZEN,
        SUBSCRIPTION_UNFROZEN
      ]
    }
    first: 10
  ) {
    edges {
      node {
        id
        eventType
        ... on SubscriptionStatus {
          state
          cancelEffectiveOn
          plan {
            handle
            billingPeriod
            trialDays
            trialDaysRemaining
            prices {
              currencyCode
              ... on FlatRatePlanPrice {
                amount
              }
              ... on TieredPlanPrice {
                tiersMode
                tiers {
                  upTo
                  amountPerUnit
                  amount
                }
              }
            }
          }
        }
      }
    }
  }
}
```

**Filter by app and shop**

```graphql
{
  events(
    filter: {
      subjectId: "gid://shopify/App/1234"
      shopId: "gid://shopify/Shop/5678"
    }
    first: 10
  ) {
    edges {
      node {
        id
        occurredAt
        eventType
        shop {
          id
          myshopifyDomain
        }
      }
    }
  }
}
```

The following event types track subscription lifecycle changes:

| Event type | Description |
| - | - |
| `SUBSCRIPTION_CREATED` | A merchant subscribed to a plan |
| `SUBSCRIPTION_UPDATED` | A merchant changed their plan |
| `SUBSCRIPTION_CANCELLATION_SCHEDULED` | A cancellation has been scheduled (for example, a downgrade to a free plan that takes effect at the end of the billing cycle) |
| `SUBSCRIPTION_CANCELED` | The subscription was canceled |
| `SUBSCRIPTION_FROZEN` | The subscription was frozen due to a store billing issue |
| `SUBSCRIPTION_UNFROZEN` | A previously frozen subscription was reactivated |

To get a merchant's complete app event history, omit `eventTypes` from the filter — all event types are returned. To restrict to app events only, set `subjectType: APP` in the filter. If you filter by `shopId`, you must also provide `subjectId` (the app GID). By default the `events` query returns the last 30 days — use `occurredAtMin` and `occurredAtMax` to widen the window (maximum range is 365 days). The page size limit is 250; use cursor-based pagination with `first` and `after` to page through results. See [Historical Events](https://shopify.dev/docs/api/partner/historical-events) for the full filter reference.

**Info:** The Active Subscription and Historical Events APIs are available in the 2026-07 release candidate of the Partner API.

### Subscription change notifications

Shopify App Pricing doesn't use webhooks to notify your app of subscription changes. Instead, Shopify passes subscription details as URL parameters when a merchant is redirected from the plan selection or charge confirmation page to your app's redirection URL.

This replaces the following webhook topics used by the [Billing API](https://shopify.dev/docs/apps/launch/billing/manual-pricing):

| Billing API webhook | Shopify App Pricing equivalent |
| - | - |
| `APP_SUBSCRIPTIONS_UPDATE` — triggered when a subscription's status or capped amount changes | Subscription status is passed as URL parameters on redirect. For status changes that happen outside of a redirect (such as cancellations or freezes), query the Partner API. |
| `APP_PURCHASES_ONE_TIME_UPDATE` — triggered when a one-time purchase status changes | Not applicable. Shopify App Pricing doesn't support one-time purchases. |
| `APP_SUBSCRIPTIONS_APPROACHING_CAPPED_AMOUNT` — triggered when usage reaches 90% of the capped amount | Not applicable. Shopify App Pricing doesn't use capped amounts for usage-based pricing. |

#### URL redirect parameters

When a merchant selects or confirms a plan, Shopify redirects them to your configured redirection URL with the following parameters appended:

| Parameter | Description |
| - | - |
| `plan_handle` | The plan that the merchant is subscribed to |
| `shop` | The merchant's shop domain (for external redirection links) |

Use these parameters to confirm the subscription status by querying the Partner API when your app handles the redirect.

For subscription lifecycle events that don't involve a merchant redirect — such as cancellations, freezes, or plan expirations — query the Partner API to check the current subscription state.

### Limitations

- Shopify App Pricing currently supports the following pricing models:
  - Fixed recurring charges (for example, $10/month or $100/year)
  - Usage-based pricing with fixed, graduated, or volume pricing
  - Combinations of monthly recurring charges with usage-based pricing
- Once you opt in to Shopify App Pricing, you can't create new recurring application charges using the Billing API. Charges created before opting into Shopify App Pricing continue to process as expected.
- Usage-based pricing has the following limitations:
  - You can create up to five active usage meters per plan
  - You can define up to six pricing tiers per usage meter
  - Usage charges must be billed monthly (can't be combined with yearly-only plans)
  - Usage caps aren't currently supported
- When testing a draft app during development, its plan selection page might return a 404 error if the development store and the app listing are set to different locales. This issue doesn't affect production stores or published apps.

### Partner API event types

The Partner API has two separate event type systems with different naming conventions. Make sure you're using the correct one for your query.

#### `EventType` — used by `QueryRoot.events` (recommended)

The `events` query at the query root uses the `EventType` enum. This is the recommended approach for Shopify App Pricing and provides subscription lifecycle tracking, charge events, and earning events.

| Event type | Description |
| - | - |
| `SUBSCRIPTION_CREATED` | A merchant subscribed to a plan |
| `SUBSCRIPTION_UPDATED` | A merchant changed their plan |
| `SUBSCRIPTION_CANCELLATION_SCHEDULED` | A cancellation has been scheduled |
| `SUBSCRIPTION_CANCELED` | The subscription was canceled |
| `SUBSCRIPTION_FROZEN` | The subscription was frozen due to a store billing issue |
| `SUBSCRIPTION_UNFROZEN` | A previously frozen subscription was reactivated |
| `CHARGE_RECURRING` | A recurring charge event |
| `CHARGE_ONE_TIME` | A one-time charge event |
| `CHARGE_USAGE` | A usage-based charge event |
| `CREDIT_APPLIED` | A credit was applied |
| `CREDIT_FAILED` | A credit application failed |
| `CREDIT_PENDING` | A credit is pending |
| `EARNING_CHARGE_RECURRING` | A recurring earning event |
| `EARNING_CHARGE_ONE_TIME` | A one-time earning event |
| `EARNING_CHARGE_USAGE` | A usage-based earning event |
| `EARNING_CREDIT` | A credit earning event |
| `EARNING_REFUND` | A refund earning event |
| `EARNING_ADJUSTMENT` | An adjustment earning event |
| `RELATIONSHIP_INSTALLED` | A merchant installed the app |
| `RELATIONSHIP_UNINSTALLED` | A merchant uninstalled the app |
| `RELATIONSHIP_REACTIVATED` | A previously deactivated relationship was reactivated |
| `RELATIONSHIP_DEACTIVATED` | The relationship was deactivated |

Use the `events` query with the `EventFilterInput` `eventTypes` field to filter by specific event types, as shown in query subscription data.

#### `AppEventTypes` — used by `App.events` (legacy)

The older `App.events` field uses the `AppEventTypes` enum with a different naming convention. These event types use a more granular naming pattern for charge lifecycle states (accepted, activated, declined, expired).

| Event type | Description |
| - | - |
| `SUBSCRIPTION_CHARGE_ACCEPTED` | A subscription charge was accepted |
| `SUBSCRIPTION_CHARGE_ACTIVATED` | A subscription charge was activated |
| `SUBSCRIPTION_CHARGE_CANCELED` | A subscription charge was canceled |
| `SUBSCRIPTION_CHARGE_DECLINED` | A subscription charge was declined |
| `SUBSCRIPTION_CHARGE_EXPIRED` | A subscription charge expired |
| `SUBSCRIPTION_CHARGE_FROZEN` | A subscription charge was frozen |
| `SUBSCRIPTION_CHARGE_UNFROZEN` | A subscription charge was unfrozen |
| `SUBSCRIPTION_CAPPED_AMOUNT_UPDATED` | The subscription's capped amount was updated |
| `SUBSCRIPTION_APPROACHING_CAPPED_AMOUNT` | The subscription is approaching its capped amount |
| `ONE_TIME_CHARGE_ACCEPTED` | A one-time charge was accepted |
| `ONE_TIME_CHARGE_ACTIVATED` | A one-time charge was activated |
| `ONE_TIME_CHARGE_DECLINED` | A one-time charge was declined |
| `ONE_TIME_CHARGE_EXPIRED` | A one-time charge expired |
| `USAGE_CHARGE_APPLIED` | A usage charge was applied |
| `CREDIT_APPLIED` | A credit was applied |
| `CREDIT_FAILED` | A credit application failed |
| `CREDIT_PENDING` | A credit is pending |
| `RELATIONSHIP_INSTALLED` | A merchant installed the app |
| `RELATIONSHIP_UNINSTALLED` | A merchant uninstalled the app |
| `RELATIONSHIP_REACTIVATED` | A previously deactivated relationship was reactivated |
| `RELATIONSHIP_DEACTIVATED` | The relationship was deactivated |

**Info:** If you're building new billing integrations with Shopify App Pricing, use the `QueryRoot.events` query with the `EventType` enum. The `App.events` query with `AppEventTypes` is available in the unstable Partner API version but uses an older naming convention that predates Shopify App Pricing.

### For apps enrolled before April 2026

**Legacy features:** If you set up Shopify App Pricing (formally known as managed pricing) before April 2026, the following features still apply to your app. New apps should use the current system documented above.

#### Webhook-based subscription notifications

Before April 28, 2026, you can receive a webhook when a subscription is updated by registering for the [`APP_SUBSCRIPTIONS_UPDATE`](https://shopify.dev/docs/api/admin-graphql/unstable/enums/WebhookSubscriptionTopic#value-appsubscriptionsupdate) topic. Note that webhooks can take several minutes to deliver. Make sure your app can handle [webhook delays](https://shopify.dev/docs/apps/build/webhooks/best-practices#manage-delays) and follow Shopify's [best practices for webhooks](https://shopify.dev/docs/apps/build/webhooks/best-practices).

After April 28, 2026, Shopify App Pricing no longer sends webhooks for subscription changes. Use the Partner API and URL redirect parameters instead.

#### Billing API subscription status queries

Before April 28, 2026, a `charge_id` URL parameter with a transaction ID is appended to your redirect URL when a merchant approves a plan charge. For apps rendered in the Shopify admin, `charge_id` is appended to the relative path. For external redirect URLs, both `charge_id` and the merchant shop domain are appended. You can use `charge_id` with the [Billing API](https://shopify.dev/docs/api/admin-graphql/current/enums/AppSubscriptionStatus) to query subscription status.

After April 28, 2026, Shopify App Pricing no longer appends `charge_id` to your redirect URL. Use the Partner API and `plan_handle` URL redirect parameters instead.

#### Test charges

Before April 28, 2026, Shopify App Pricing supports [free testing for dev stores](https://shopify.dev/docs/apps/launch/billing/offer-free-trials#set-up-free-testing). When a development store subscribes to a plan, Shopify creates a test subscription for that store. Your account isn't charged for test subscriptions.

**Note:** Test subscriptions don't convert to paid when you transfer a store. After transferring, you'll need to create a new plan.

After April 28, 2026, use the $0 private test plan to test your billing integration instead.

---

## Setup subscription charges (Shopify App Pricing)

> Fonte: https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/subscription-billing/setup-subscription-charges

Time-based subscriptions let you bill merchants on a regular schedule with fixed fees. You can offer free plans, monthly recurring charges, yearly recurring charges, or a combination of monthly and yearly options.

### Recurring charge options

Shopify App Pricing supports the following recurring charge types:

- **Free plans**: No charge to the merchant
- **Monthly recurring**: Fixed monthly subscription fee
- **Yearly recurring**: Fixed annual subscription fee
- **Monthly with yearly discount**: Offer both monthly and yearly options, with a discounted rate for annual commitments

You can also configure [free trial periods](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/subscription-billing/offer-free-trials) and welcome links for each plan.

### Add a recurring subscription plan

#### Step 1: Add the plan

1. From your Partner Dashboard, click **Apps > All Apps** and click the name of the app you want to update pricing for.
2. Click **Distribution**.
3. Beside **Shopify App Store listing**, click **Manage listing**.
4. Under **Published languages**, click **Edit** for the locale you want to update.
5. Under **Pricing content**, click **Manage** to open the Pricing index page.
6. Under **Public plans**, click **Add** to open the plan editor.
7. Under **Billing**, select whether the plan is free, monthly, yearly, or monthly with a yearly option.
8. (If required) Under **Monthly charge**, enter a price.
9. (If required) Under **Yearly charge**, enter a price.
10. (Optional) Under **Free trial duration**, enter the number of days you want to offer.
11. (Optional) Under **Welcome link**, add a path or URL where the merchant will be redirected after approving the plan charge.
12. Click **Save**.

#### Step 2: Add plan descriptions for each language

Public plans share the same billing model and price details across all your app listings. But plan descriptions are localized, so that you can translate the plan name and its list of top features for each locale.

1. From your Partner Dashboard, click **Apps > All Apps** and click the name of the app you want to update pricing for.
2. Click **Distribution**.
3. Beside **Shopify App Store listing**, click **Manage listing**.
4. Under **Published languages**, click **Edit** for the locale you want to update.
5. Under **Pricing content**, find your recently added or updated plan.
6. Under **Display name**, give the plan a name.
7. Under **Top features**, describe the app features available under this plan.
8. Click **Save**.

Make sure to add plan descriptions for each translated app listing. A plan will only display to merchants if it has a description for the current language.

### Proration logic

#### Plan downgrading

Downgrading from a paid plan to a free plan is deferred, meaning it's effective at the end of the paid plan's current cycle.

### Next steps

- Learn about [usage-based subscriptions](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/subscription-billing/setup-usage-charges)
- [Combine time and usage](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/subscription-billing/combined-subscription-and-usage) for hybrid pricing
- Offer [free trials](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/subscription-billing/offer-free-trials) to increase conversions

---

## Setup usage charges (Shopify App Pricing)

> Fonte: https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/subscription-billing/setup-usage-charges

Usage-based pricing lets you charge merchants based on their actual usage of your app's features. This pricing model is ideal for apps where costs scale with usage, such as messaging apps, email marketing tools, or apps that process transactions.

Usage-based pricing accounts for over 60% of revenue from top-earning apps on the Shopify App Store.

### When to use usage-based pricing

Consider usage-based pricing if your app:

- **Sends messages or emails**: Charge per SMS sent, email delivered, or notification pushed
- **Processes transactions**: Charge based on order volume, revenue generated, or items sold
- **Uses external APIs**: Pass through costs for third-party services like shipping carriers or payment processors
- **Provides compute-intensive features**: Charge for AI processing, image optimization, or data analysis
- **Offers variable-value features**: Align costs with the value merchants receive

### Pricing structures

You can choose from three usage-based pricing structures:

#### Fixed pricing

Charge a uniform price for each billing event. For example, charge $0.01 per SMS sent or $0.50 per order processed.

#### Graduated pricing

Price tiers based on cumulative usage. As merchants use more, they pay different rates for usage in each tier. The final charge is the sum of all tiers.

For example, with tiers set as:

- 1-100 units at $10 per unit
- 101-200 units at $9 per unit
- 201+ units at $8 per unit

If a merchant uses 150 units, they pay: (100 × $10) + (50 × $9) = $1,450

#### Volume pricing

Price tiers based on total usage volume. The rate for the entire quantity is determined by which tier the total usage falls into.

For example, with the same tier structure:

- 1-100 units at $10 per unit
- 101-200 units at $9 per unit
- 201+ units at $8 per unit

If a merchant uses 150 units, they pay: 150 × $9 = $1,350 (using the 101-200 tier rate)

### How usage-based pricing works

Usage-based pricing requires you to configure meters in the Partner Dashboard and then send billing events to Shopify using the [App Events API](https://shopify.dev/docs/api/app-events).

#### Step 1: Configure meters in the Partner Dashboard

In your app's submission page, define the usage meters you want to track:

1. Navigate to your app in the Partner Dashboard
2. Go to the **Pricing** section
3. Create a usage meter and give it an `event_handle` (for example, `sms_sent`, `email_delivered`, `order_processed`)
4. Configure your pricing structure (fixed, graduated, or volume) for each meter
5. Set your pricing tiers and rates

You can create up to five usage meters per plan to track different types of usage.

#### Step 2: Send events using the App Events API

Once your meters are configured, use the [App Events API](https://shopify.dev/docs/api/app-events) to send billing events to Shopify as they occur in your app. The `event_handle` in each request must match the meter handle you defined in the Partner Dashboard.

```bash
curl -X POST "https://api.shopify.com/app/unstable/events" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer {access_token}" \
  -d '{
    "shop_id": "gid://shopify/Shop/12345678",
    "event_handle": "sms_sent",
    "timestamp": "2026-01-27T14:30:00Z",
    "idempotency_key": "sms_12345_1706365800",
    "attributes": {
      "value": 1
    }
  }'
```

The `event_handle` must match the meter handle you configured in the Partner Dashboard. The `value` in the attributes represents the quantity of usage and must be greater than 0 (for example, 1 SMS sent or 5 orders processed). Billing events have a 24-hour idempotency window — requests with a previously seen `idempotency_key` within that window are ignored.

**Caution:** Don't include any data that, alone or in combination with other data, could identify an individual. This includes any merchant or buyer information, such as name, email address, phone number, and other identifiable data points. Use anonymized identifiers and aggregated metrics instead.

For detailed implementation instructions, see [Build a billing event](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/subscription-billing/build-billing-event).

#### Step 3: Validate events in the Dev Dashboard

After sending events, verify they're being received and classified correctly in the [Dev Dashboard](https://shopify.dev/docs/apps/build/dev-dashboard/monitoring-and-logs):

1. Open the [Dev Dashboard](https://dev.shopify.com) and navigate to your app
2. Go to the **Logs** section
3. Under the **Type** filter, select **App Billing Event** to see only events tied to your pricing meters
4. Verify that your events appear as billable and are associated with the correct meters

If an event doesn't appear under **App Billing Event**, the `event_handle` in your API request doesn't match the meter handle configured in the Partner Dashboard **Pricing** section. The handle must match exactly between your [App Events API](https://shopify.dev/docs/api/app-events) request and your pricing configuration. If an event fails validation, review the error details and update your implementation accordingly.

**Info:** The Dev Dashboard is the only place to see billing errors for your events. The App Events API always returns a `202` response when it receives your request, even if the event fails billing validation. There is no synchronous billing error response and no webhooks for billing validation failures. In the dashboard, events are marked as successful or failed, and labeled as billable or non-billable.

##### Billing error states

The following errors can occur when processing billing events. These errors appear in the Dev Dashboard:

| Error | Description |
| - | - |
| `INVALID_ACCOUNT` | The app or partner account is invalid or not authorized. |
| `ACCOUNT_FROZEN` | The partner account is frozen and can't process billing events. |
| `NO_SUBSCRIPTION` | The merchant doesn't have an active subscription to your app. |
| `SUBSCRIPTION_NOT_METERED` | The merchant's subscription doesn't include usage-based pricing. |
| `PERIOD_CLOSED` | The billing period for this event has already closed. The timestamp must fall within the merchant's current billing cycle. |
| `INVALID_TIMESTAMP` | The timestamp is missing, malformed, or outside the acceptable range. The timestamp can't be more than 5 minutes in the future, and for billing events it must fall within the merchant's current billing cycle. |
| `IDEMPOTENCY_KEY_ERROR` | The idempotency key is missing, already used, or invalid. |
| `INVALID_VALUE` | The `value` in the attributes is invalid (for example, zero, negative, or non-numeric). The value must be greater than 0. |
| `MISSING_VALUE_KEY` | The `value` key is missing from the attributes. |

#### Step 4: Automated billing

Once events are validated and accepted, Shopify automatically:

1. Aggregates usage for each merchant based on your configured meters
2. Applies your pricing structure (fixed, graduated, or volume)
3. Adds the calculated charges to the merchant's monthly bill

**Info:** After a merchant uninstalls your app, you have 24 hours to submit any remaining billing events for usage that occurred before the uninstall. After 24 hours, the billing period closes and new events are rejected with a `PERIOD_CLOSED` error. Make sure your app sends any pending billing events promptly when you receive an [app uninstalled webhook](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance).

### Combining pricing models

You can combine recurring charges with usage-based pricing to create hybrid pricing plans:

- **Base fee + usage**: Charge a monthly subscription fee plus usage-based charges (for example, $29/month + $0.01 per SMS)
- **Usage only**: Uncheck the subscription fee and charge only for usage
- **Tiered plans with usage**: Offer different base tiers with varying usage rates or included usage allowances

You can't currently combine usage-based pricing with yearly-only plans. Usage charges must be tied to a monthly billing cycle.

Learn more about [combining time and usage](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/subscription-billing/combined-subscription-and-usage).

### Limitations

Usage-based pricing has the following limitations:

- You can create up to five active usage meters per plan
- You can define up to six pricing tiers per usage meter
- Usage charges must be billed monthly (can't be combined with yearly-only plans)
- Usage caps aren't currently supported
- After a merchant uninstalls your app, you have 24 hours to submit any remaining billing events. After 24 hours, the billing period is closed and new events are rejected.

### Next steps

- [Build a billing event](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/subscription-billing/build-billing-event) to start sending usage data
- Explore the [App Events API reference](https://shopify.dev/docs/api/app-events) for implementation details
- Learn about [time-based subscriptions](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/subscription-billing/setup-subscription-charges)
- [Combine time and usage](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/subscription-billing/combined-subscription-and-usage) for hybrid pricing
- Offer [free trials](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/subscription-billing/offer-free-trials) to increase conversions

---

## Offer free trials

> Fonte: https://shopify.dev/docs/apps/launch/billing/offer-free-trials

Free trials let merchants test your app before committing to a paid plan. You can configure free trial periods when creating any subscription plan, and extend trials for individual merchants through your Partner Dashboard.

### Configure free trials

When creating or editing a plan, you can specify the number of free trial days:

1. From your Partner Dashboard, click **Apps > All Apps** and click the name of the app you want to update pricing for.
2. Click **Distribution**.
3. Beside **Shopify App Store listing**, click **Manage listing**.
4. Under **Published languages**, click **Edit** for the locale you want to update.
5. Under **Pricing content**, click **Manage** to open the Pricing index page.
6. Click on an existing plan or create a new one.
7. Under **Free trial duration**, enter the number of days you want to offer.
8. Click **Save**.

### Trial proration

Shopify App Pricing tracks trial days over a 180-day period to prevent users from repeatedly reinstalling apps to exploit free trial periods.

For example, if a merchant uses 12 out of 15 trial days on a Pro Plan, uninstalls, then reinstalls the app 90 days later, they'll still have 3 trial days left for the Pro Plan.

If you update your trial periods, then previously consumed trial days are subtracted from the new totals.

### Extend a trial period

You can extend trial periods for individual merchants through your Partner Dashboard. Staff members need the [**Manage credits and refunds**](https://help.shopify.com/partners/dashboard/account-access#sensitive-permissions) permission to manage trial extensions.

1. From your partner dashboard, search for the name of the merchant whose trial you want to extend. Click the merchant name in the **Store** column of the search results.
2. Beside **Trial extension**, click **Create**.
3. Under **App**, search for your app by name and select it.
4. Under **Extra trial days**, enter the number of days to extend the merchant's trial.
5. Click **Create**.
6. In the confirmation dialog, click **Apply** to confirm the trial extension.

Shopify sends an email to the merchant on your behalf confirming the change. The merchant doesn't need to re-subscribe to the plan. The extension is applied to their subscription automatically.

### Discounts

In addition to trial extensions, you can issue discounts to merchants:

1. From your partner dashboard, search for the name of the merchant you want to offer a discount. Click the merchant name in the **Store** column of the search results.
2. Beside **Discount**, click **Create**.
3. Under **App**, search for your app by name and select it.
4. Select the type, value, and duration of the discount.
5. Click **Create**.
6. In the confirmation dialog, click **Apply** to confirm the discount.

The discount is applied to their subscription automatically, starting on the next billing cycle.

### Test charges

**Caution:** Test subscriptions on development stores are changing. Every subscription now requires a billing contract, and Shopify doesn't support "test" subscriptions with the new billing system. Use the [$0 private test plan](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing#test-plan) to test your billing integration on development stores instead.

To simplify testing your app's pricing, Shopify App Pricing supports free testing for dev stores via the $0 private test plan. Your account isn't charged for test subscriptions on development stores.

**Note:** Test subscriptions don't convert to paid when you transfer a store. After transferring, you'll need to create a new plan.

### Next steps

- Learn about [time-based subscriptions](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/subscription-billing/setup-subscription-charges)
- Learn about [usage-based subscriptions](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/subscription-billing/setup-usage-charges)

---

## About manual pricing (legacy Billing API)

> Fonte: https://shopify.dev/docs/apps/launch/billing/manual-pricing

For advanced use cases or custom billing flows that aren't supported by [Shopify App Pricing](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing), you can use manual pricing to build your own billing logic.

**Preferred approach:** For public apps, use [Shopify App Pricing](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing). The Billing API is still supported for existing apps and outlier pricing models Shopify App Pricing doesn't cover.

### Billing process

The following diagram describes the app billing process and the roles taken by merchants, your app, and Shopify when using the Billing API.

1. A merchant starts an action that includes a charge, such as an app installation, a service plan upgrade, or an individual purchase.
2. Your app creates a charge for the merchant, using either the [`appPurchaseOneTimeCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/apppurchaseonetimecreate) or the [`appSubscriptionCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/appsubscriptioncreate) mutation.
3. Shopify verifies the charge and returns a [`confirmationUrl`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/appsubscriptioncreate#field-appsubscriptioncreatepayload-confirmationurl), which is a page that Shopify hosts for the merchant to approve charges.
4. The app should redirect the merchant to the `confirmationUrl`, where the merchant either approves or declines the charge.
5. If the merchant accepts the charge, then they're redirected to a [`returnUrl`](https://shopify.dev/docs/api/admin-graphql/latest/objects/appsubscription#field-appsubscription-returnurl) that your app specified when it issued the charge. If the charge is declined, then Shopify redirects the merchant to the Shopify admin, and provides a notification message about the app charge being declined.

**Note:** Subscription upgrades and downgrades, for example going from a basic tier to a premium tier, or a premium tier to a basic tier, go through this flow.

#### App actions to set up purchases

The app billing process requires your app to perform actions that set up purchases.

**React Router:** Shopify provides an app package for React Router to help you configure charges for your app and make calls to the GraphQL Admin API's billing resources. If your app isn't React Router based, then you can use [the code examples in the reference](https://shopify.dev/docs/api/shopify-app-react-router/latest/apis/billing) as a general guide to your app's configuration.

##### Configure a pricing model

A pricing model is how you monetize your app. Each pricing model configuration must contain an `amount`, a `currencyCode`, and an `interval`. You can also set the parameters that are allowed by the GraphQL Admin API's [`appSubscriptionCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/appSubscriptionCreate) and [`appPurchaseOneTimeCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/appPurchaseOneTimeCreate) mutations that are used for the charges.

React Router apps can set up plans by passing in the `billing` configuration when `shopifyApp` is called.

##### Gate requests

Gating requests require merchants to pay for the app before they can access specific routes. To gate requests, you can verify whether there's an active payment and require one if there isn't. The following is an example for the process:

- Indicate which plans enable access to a specific route.
- Pass a check to determine if there's a purchase for any of the plans.
- Require a purchase if one isn't detected. React Router apps can use the `admin.billing.require` function. The function verifies that there's an active payment and requires one if there isn't. You can send multiple plans to `require`. It passes if there's a purchase for any of the plans and returns information on the active purchase.

**Tip:** Call the function in loaders and actions to avoid ungated requests. If you want to gate multiple routes, then use a layout [like this example](https://github.com/Shopify/shopify-app-template-react-router/blob/main/app/routes/app.tsx) in the React Router template.

##### Request payment

If your billing check doesn't find a purchase, then you can decide where to take the merchant. The following are examples:

- Request payment right away for one of the purchase configurations.
- Redirect the merchant to a page where they can select a plan.
  - In the plan selection page, you'll need to authenticate with the [GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql) for access. React Router apps can call `authenticate.admin`.

### Pricing models

Your pricing model determines the charges that are collected for your app from merchants by Shopify.

You can use Shopify's manual pricing resources to implement one or more of the following models:

| Type | Description | Use cases | Learn how |
| - | - | - | - |
| **Subscription fee** | Charge either an annual or 30-day recurring fee to use the app, charge a capped fee based on usage, or employ both. Note, usage charges can only be paired with a 30-day recurring fee. | Charge merchants a fee every 30 days to use review features. Charge merchants a fee every 30 days and a fee per SMS message sent on their behalf. | [Time-based](https://shopify.dev/docs/apps/launch/billing/manual-pricing/subscription-billing/create-time-based-subscriptions), [Usage-based](https://shopify.dev/docs/apps/launch/billing/manual-pricing/subscription-billing/create-usage-based-subscriptions), [Combination](https://shopify.dev/docs/apps/launch/billing/manual-pricing/subscription-billing/combine-time-and-usage), [Additional use cases](https://shopify.dev/docs/apps/launch/billing/manual-pricing/subscription-billing/complex-pricing-models) |
| **One-time purchase** | Charge once for the app, or charge once to enable limited use. | Charge merchants a flat fee for translating their storefront. Enable merchants to purchase credits to use in your app. | [One-time charges and multiple one-time charges](https://shopify.dev/docs/apps/launch/billing/manual-pricing/support-one-time-purchases) |

### Pricing adjustments

A pricing adjustment modifies an app's subscription fee or price. App billing API resources support the following price adjustments:

| Type | Description | Eligibility |
| - | - | - |
| **[App credits](https://shopify.dev/docs/apps/launch/billing/billing-adjustments/award-app-credits)** | Grant a sum that merchants can put towards future purchases, subscriptions, or usage charges. | Merchants who have the app installed |
| **[Subscription discounts](https://shopify.dev/docs/apps/launch/billing/manual-pricing/subscription-billing/offer-subscription-discounts)** | Offer a percentage or fixed-price discount on an app subscription for a set number of billing cycles. | New subscribers, Merchants with existing subscriptions |
| **[Free trials](https://shopify.dev/docs/apps/launch/billing/manual-pricing/subscription-billing/offer-free-trials)** | Delay the start of an app's billing cycle by a number of days. This enables merchants to experiment with apps before they commit to paying. Available only to merchants that agree to a new subscription. Can't be added to existing subscriptions. | New subscriptions only. Can't be added to existing subscriptions |
| **[Refunds](https://shopify.dev/docs/apps/launch/billing/billing-adjustments/refund-app-charges)** | Issue a full or partial refunds for a specific app charge. | All users |

### Webhook topics

In addition to the [mandatory webhook topics](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance), Shopify provides the following webhook topics for billing:

- [`APP_PURCHASES_ONE_TIME_UPDATE`](https://shopify.dev/docs/api/admin-graphql/latest/enums/webhooksubscriptiontopic#value-apppurchasesonetimeupdate): Triggered when the status of an `AppPurchaseOneTime` object is changed.
- [`APP_SUBSCRIPTIONS_UPDATE`](https://shopify.dev/docs/api/admin-graphql/latest/enums/webhooksubscriptiontopic#value-appsubscriptionsupdate): Triggered when the status, or capped amount, of an `AppSubscription` object is changed, and when a subscription's status changes.
- [`APP_SUBSCRIPTIONS_APPROACHING_CAPPED_AMOUNT`](https://shopify.dev/docs/api/admin-graphql/latest/enums/webhooksubscriptiontopic#value-appsubscriptionsapproachingcappedamount): Triggered when the balance used on an app subscription crosses 90% of the capped amount.

### Developer tools and resources

Explore the developer tools and resources available for app billing:

- [GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql/latest/mutations/appSubscriptionCreate) — Review the GraphQL Admin API resources for app billing.
- [Partner API](https://shopify.dev/docs/api/partner) — Use the Partner API to create app credits.
- [React Router billing functions](https://shopify.dev/docs/api/shopify-app-react-router/latest/apis/billing) — Learn about the functions that React Router apps can use to bill merchants.

---

## Create time-based subscriptions (manual pricing)

> Fonte: https://shopify.dev/docs/apps/launch/billing/manual-pricing/subscription-billing/create-time-based-subscriptions

**Preferred approach:** For public apps, use [Shopify App Pricing](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing). The Billing API is still supported for existing apps and outlier pricing models Shopify App Pricing doesn't cover.

A time-based subscription is a pricing model that charges a consistent, recurring amount for a service. Shopify offers billing intervals for every 30 days and every 365 days.

Merchants must approve the pricing plan. After accepting the charges, the merchant is redirected to a URL that you provide.

### Requirements

- Your app can make [authenticated requests](https://shopify.dev/docs/api/admin-graphql#authentication) to the GraphQL Admin API.

### Step 1: Create the subscription

1. [Refer to an example](https://shopify.dev/docs/api/admin-graphql/latest/mutations/appSubscriptionCreate#examples-Create_a_subscription_for_an_app_on_a_recurring_pricing_plan_only_) of creating an app subscription.
2. Make a request to the `appSubscriptionCreate` mutation with the following information:
   - [`name`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/appSubscriptionCreate#argument-name)
   - [`returnURL`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/appSubscriptionCreate#argument-returnurl)
3. Use the [`appRecurringPricingDetails`](https://shopify.dev/docs/api/admin-graphql/latest/input-objects/AppPlanInput#field-appplaninput-apprecurringpricingdetails) field on the line item's plan to provide the following information:
   - [`currencyCode`](https://shopify.dev/docs/apps/launch/billing#supported-currencies)
   - `price`
   - `interval`

     **Note:** The `interval` field accepts `ANNUAL` or `EVERY_30_DAYS`. If not provided, then the default of `EVERY_30_DAYS` is applied.

### Step 2: Monitor subscription updates

To receive a notification when a subscription status changes, such as when a charge is successful, subscribe to the GraphQL Admin API's [`APP_SUBSCRIPTIONS_UPDATE`](https://shopify.dev/docs/api/admin-graphql/latest/enums/webhooksubscriptiontopic#value-appsubscriptionsupdate) webhook topic.

### Next steps

- [Discounts](https://shopify.dev/docs/apps/launch/billing/subscription-billing/offer-subscription-discounts) — Learn about offering subscription discounts.
- [Prorated and deferred charges](https://shopify.dev/docs/apps/launch/billing/subscription-billing) — Learn how Shopify handles prorating and deferring app subscription charges.

---

## Create usage-based subscriptions (manual pricing)

> Fonte: https://shopify.dev/docs/apps/launch/billing/manual-pricing/subscription-billing/create-usage-based-subscriptions

**Preferred approach:** For public apps, use [Shopify App Pricing](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing). The Billing API is still supported for existing apps and outlier pricing models Shopify App Pricing doesn't cover.

A usage-based subscription is a pricing model that charges merchants continuously based on app use during Shopify's 30-day billing cycle.

Merchants must approve the pricing plan. After accepting the charges, the merchant is redirected to a URL that you provide.

### Requirements

- Your app can make [authenticated requests](https://shopify.dev/docs/api/admin-graphql#authentication) to the GraphQL Admin API.

### Step 1: Create the subscription

Make a request to the [`appSubscriptionCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/appsubscriptioncreate) mutation with the following information:

- [`name`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/appSubscriptionCreate#argument-name)
- [`returnURL`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/appSubscriptionCreate#argument-returnurl)
- `terms` - Merchants review the terms of the subscription when they accept the pricing plan.
- `cappedAmount` - The maximum that a merchant is billed for during the 30-day billing cycle. The `currencyCode` must be one of the [supported currencies](https://shopify.dev/docs/apps/launch/billing#supported-currencies).

The following mutation is an example:

**POST https://{shop}.myshopify.com/api/{api_version}/graphql.json — JSON response**

```json
{
  "data": {
    "appSubscriptionCreate": {
      "userErrors": [],
      "confirmationUrl": "https://{shop}.myshopify.com/admin/charges/4028497976/confirm_recurring_application_charge?signature=BAh7BzoHaWRsKwc4AB7wOhJhdXRvX2FjdGl2YXRlVA%3D%3D--987b3537018fdd69c50f13d6cbd3fba468e0e9a6",
      "appSubscription": {
        "id": "gid://shopify/AppSubscription/4028497976",
        "lineItems": [
          {
            "id": "gid://shopify/AppSubscriptionLineItem/4028497976?v=1&index=0",
            "plan": {
              "pricingDetails": {
                "__typename": "AppRecurringPricing"
              }
            }
          },
          {
            "id": "gid://shopify/AppSubscriptionLineItem/4028497976?v=1&index=1",
            "plan": {
              "pricingDetails": {
                "__typename": "AppUsagePricing"
              }
            }
          }
        ]
      }
    }
  },
  ...
}
```

Shopify uses the payload's `AppSubscription.id` and the `AppSubscriptionLineItem.id` to generate data for app usage records.

### Step 2: Create an app usage record

After you've created the usage pricing plan and the merchant has accepted the plan, you can create a usage record with the [`appUsageRecordCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/appUsageRecordCreate) mutation. The usage record needs to include the `AppSubscriptionLineItem.id` of the `AppSubscription` object that the `appSubscriptionCreate` mutation returns.

The following mutation is an example:

**POST https://{shop}.myshopify.com/api/{api_version}/graphql.json — GraphQL mutation**

```graphql
mutation {
  appUsageRecordCreate(
    subscriptionLineItemId: "gid://shopify/AppSubscriptionLineItem/4019585080?v=1&index=0",
    description: "Super Mega Plan 1000 emails",
    price: {
      amount: 1.00,
      currencyCode: USD
    }
  ) {
    userErrors {
      field,
      message
    },
    appUsageRecord {
      id
    }
  }
}
```

**JSON response**

```json
{
  "data": {
    "appUsageRecordCreate": {
      "userErrors": [],
      "appUsageRecord": {
        "id": "gid://shopify/AppUsageRecord/14518231"
      }
    }
  },
  ...
}
```

### Step 3: Monitor app usage limits

Merchants can use the Shopify admin to change their subscription's capped amount. The capped amount is the maximum amount of usage to bill for within the 30-day billing cycle.

To receive a notification when merchants change the capped amount, subscribe to the GraphQL Admin API's [`APP_SUBSCRIPTIONS_UPDATE`](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#value-appsubscriptionsupdate) webhook topic.

To receive a notification when merchants reach or exceed 90% of their capped amount, subscribe to the GraphQL Admin API's [`APP_SUBSCRIPTIONS_APPROACHING_CAPPED_AMOUNT`](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#value-appsubscriptionsapproachingcappedamount) webhook topic.

### Step 4: Monitor subscription status changes

To receive a notification when a subscription status changes, such as when a charge is successful, subscribe to the GraphQL Admin API's [`APP_SUBSCRIPTIONS_UPDATE`](https://shopify.dev/docs/api/admin-graphql/latest/enums/webhooksubscriptiontopic#value-appsubscriptionsupdate) webhook topic.

### Next steps

- [Discounts](https://shopify.dev/docs/apps/launch/billing/subscription-billing/offer-subscription-discounts) — Learn about offering subscription discounts.
- [Capped amount](https://shopify.dev/docs/apps/launch/billing/subscription-billing/update-max-charge) — Learn how to update the maximum amount that merchants can be charged for a subscription.

---

## Support one-time app purchases (manual pricing)

> Fonte: https://shopify.dev/docs/apps/launch/billing/manual-pricing/support-one-time-purchases

**Preferred approach:** For public apps, use [Shopify App Pricing](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing). The Billing API is still supported for existing apps and outlier pricing models Shopify App Pricing doesn't cover.

A single one-time app charge uses a pricing model similar to purchasing a product, where you make a one-time payment at the time of purchase. Multiple app charges follow a pay-as-you-go pricing model, meaning that when use of a service or product has reached a certain limit, another payment is made to continue using it. In this case, the one time charge represents multiple charges that your app creates.

Merchants must approve the pricing plan. After accepting the charges, the merchant is redirected to a URL that you provide.

### Requirements

- Your app can make [authenticated requests](https://shopify.dev/docs/api/admin-graphql#authentication) to the GraphQL Admin API.

### Step 1: Create the charge

1. [Refer to an example](https://shopify.dev/docs/api/admin-graphql/latest/mutations/appPurchaseOneTimeCreate#examples-Create_a_app_one_time_purchase_app_) of creating a one-time app charge.
2. Make a request to the `appPurchaseOneTimeCreate` mutation with the following information:
   - [`name`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/appPurchaseOneTimeCreate#argument-name)
   - [`price`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/appPurchaseOneTimeCreate#argument-price)
   - [`returnUrl`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/appPurchaseOneTimeCreate#argument-returnurl)
   - [`currencyCode`](https://shopify.dev/docs/apps/launch/billing#supported-currencies)

### Step 2: Monitor updates to one-time app purchases

To receive notifications when merchants update their one-time app purchases, subscribe to the GraphQL Admin API's [`APP_PURCHASES_ONE_TIME_UPDATE`](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#value-apppurchasesonetimeupdate) webhook topic.

### Next steps

- [Viewing charges](https://shopify.dev/docs/apps/launch/billing/view-charges-earnings) — Learn about viewing app charges and earnings.
- [Best practices](https://shopify.dev/docs/apps/launch/billing/manual-pricing/subscription-billing) — Learn about app billing best practices.

---

# App configuration

Mini-indice della sezione:

- [App Configuration (shopify.app.toml reference)](#app-configuration-shopifyapptoml-reference)
- [Manage access scopes](#manage-access-scopes)

---

## App Configuration (shopify.app.toml reference)

> Fonte: https://shopify.dev/docs/apps/build/cli-for-apps/app-configuration

You can configure your apps locally with TOML files, then [deploy your changes](https://shopify.dev/docs/api/shopify-cli/app/app-deploy) using Shopify CLI. You can also configure many of these values through the [Dev Dashboard](https://shopify.dev/docs/apps/build/dev-dashboard).

**Note:** Changes to the `shopify.app.toml` are applied automatically during [`app dev`](https://shopify.dev/docs/api/shopify-cli/app/app-dev) for your chosen development store. For app configuration changes to take effect for all stores in production, you need to run the [`deploy` command](https://shopify.dev/docs/api/shopify-cli/app/app-deploy).

Learn more about [managing app configuration files](https://shopify.dev/docs/apps/build/cli-for-apps/manage-app-config-files).

### App configuration file example

**shopify.app.config-name.toml**

```toml
name = "Example App"
client_id = "a61950a2cbd5f32876b0b55587ec7a27"
application_url = "https://www.app.example.com/"
embedded = true
handle = "example-app"


[access_scopes]
scopes = "read_products"


[access.admin]
direct_api_mode = "online"


[auth]
redirect_urls = [
  "https://app.example.com/api/auth/callback",
  "https://app.example.com/api/auth/oauth/callback",
]


[customer_authentication]
redirect_uris = [
  "https://app.example.com/api/customer/auth/callback"
]
javascript_origins = [
  "https://app.example.com"
]
logout_urls = [
  "https://app.example.com/api/customer/logout"
]


[webhooks]
api_version = "2024-01"


[[webhooks.subscriptions]]
topics = [ "app/uninstalled" ]
compliance_topics = [ "customers/redact", "customers/data_request", "shop/redact" ]
uri = "/webhooks"


[events]
api_version = "unstable"


[[events.subscription]]
handle = "product-updates"
topic = "Product"
actions = ["create", "update", "delete"]
uri = "/events/products"


[app_proxy]
url = "https://app.example.com/api/proxy"
subpath = "store-pickup"
prefix = "apps"


[pos]
embedded = false


[app_preferences]
url = "https://www.app.example.com/preferences"


[build]
automatically_update_urls_on_dev = false
```

### Reference

#### Global

**Note:** Changes to the `shopify.app.toml` are applied automatically during [`app dev`](https://shopify.dev/docs/api/shopify-cli/app/app-dev) for your chosen development store. For app configuration changes to take effect for all stores in production, you need to run the [`deploy` command](https://shopify.dev/docs/api/shopify-cli/app/app-deploy).

| Property | Required? | Value | Description |
| - | - | - | - |
| `name` | Yes | `string` | The name of your app. |
| `handle` | No | `string` | The URL slug of your App Home, for example `https://admin.shopify.com/store/your-store-name/apps/your-app-handle/app`. **Warning**: Updating the handle changes the Shopify admin URL that appears when you access your app from the side menu. As a result, any app admin links will be broken. |
| `client_id` | Yes | `string` | The app's public identifier. |
| `application_url` | Yes | `string` matching a valid URL | The URL of your app. **Note:** If you're building an [extension-only app](https://shopify.dev/docs/apps/build/app-extensions/build-extension-only-app), then your `application_url` will be set to `https://shopify.dev/apps/default-app-home` by default. |
| `embedded` | Yes | `boolean` | When `true`, your app renders in the Shopify admin, letting users interact with it without leaving Shopify. |
| `extension_directories` | No | `array` of `string` paths or glob patterns | The paths that Shopify CLI will search for app [extensions](https://shopify.dev/docs/apps/build/cli-for-apps/app-structure#extensions). When omitted, defaults to `["extensions/"]`. |
| `web_directories` | No | `array` of `string` paths or glob patterns | The paths that Shopify CLI will search for the [web files](https://shopify.dev/docs/apps/build/cli-for-apps/app-structure#web-files) of your app. When omitted, defaults to the app root directory. |

#### access_scopes

Define the permissions your app requests, as well as how the permissions are requested.

| Property | Required? | Value | Description |
| - | - | - | - |
| `scopes` | Yes | `string` matching a comma-separated list of scopes | Any [access scopes](https://shopify.dev/docs/api/usage/access-scopes) that your app will request access to during the authorization process. When a merchant installs your app with [Shopify managed install](https://shopify.dev/docs/apps/build/authentication-authorization/app-installation), they're prompted to grant permission to all the access scopes that you defined in this field. Learn how to [manage access scopes](https://shopify.dev/docs/apps/build/authentication-authorization/app-installation/manage-access-scopes) for your app. |
| `optional_scopes` | No | `array` of `string` access scopes | Any [access scopes](https://shopify.dev/docs/api/usage/access-scopes) that your app can [request dynamically](https://shopify.dev/docs/apps/build/authentication-authorization/app-installation/manage-access-scopes#request-new-access-scopes-dynamically) after installation. Learn how to [manage access scopes](https://shopify.dev/docs/apps/build/authentication-authorization/app-installation/manage-access-scopes) for your app. |
| `use_legacy_install_flow` | No | boolean | When omitted or `false`, scopes are saved in your app's configuration, and are automatically requested when the app is installed on a store or when you update the `scopes` value. This is referred to as [Shopify managed installation](https://shopify.dev/docs/apps/build/authentication-authorization/app-installation). When `true`, the legacy installation flow requests scopes through a URL parameter during the [OAuth flow](https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/authorization-code-grant). The legacy installation flow is still supported, but isn't recommended because your app can end up with different scopes for each installation. |

#### access

Settings for defining the ways that your app can access Shopify APIs.

**admin**

| Property | Required? | Value | Description |
| - | - | - | - |
| `direct_api_mode` | No | `string` matching `online` or `offline` | The access mode that [Direct API access](https://shopify.dev/docs/api/admin-extensions#direct-api-access) will use. When `online`, Direct API access is enabled and uses an [online access token](https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/online-access-tokens). When `offline`, Direct API access is enabled and uses an [offline access token](https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/offline-access-tokens). When omitted, defaults to `online`. |
| `embedded_app_direct_api_access` | No | `boolean` | Whether your app has access to [Direct API access](https://shopify.dev/docs/api/app-home#direct-api-access) for calling types in the GraphQL Admin API. When omitted or `false`, Direct API access is disabled. When `true`, Direct API is enabled and uses the mode defined by `direct_api_mode`. |

#### auth

| Property | Required? | Value | Description |
| - | - | - | - |
| `redirect_urls` | Yes | `array` of `string`s matching a valid URL | Users are redirected to these URLs as part of [authorization code grant](https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/authorization-code-grant). You must include at least one redirect URL before making your app public. Learn more about [redirection URLs.](https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/authorization-code-grant) |

#### customer_authentication

Configure authentication for Customer Account API access. Your app uses these settings for OAuth 2.0 authentication flows with customers. The authentication endpoints are discovered dynamically using [discovery endpoints](https://shopify.dev/docs/api/customer#discovery-endpoints).

| Property | Required? | Value | Description |
| - | - | - | - |
| `redirect_uris` | Yes | An array of strings matching a valid URL | The URIs where customers are redirected after authentication. Supports HTTPS URLs for web applications (for example, `https://app.example.com/api/customer/auth/callback`). These URIs are used with the `authorization_endpoint` discovered from `/.well-known/openid-configuration`. |
| `javascript_origins` | No | An array of string matching a valid origin | The allowed origins for CORS when making requests to authentication endpoints from JavaScript. Required for web applications using the authorization code flow with PKCE. Origins must include protocol and domain (for example, `https://app.example.com`). |
| `logout_urls` | No | An array of strings matching a valid URL | The URLs where customers are redirected after logout. Used with the `end_session_endpoint` discovered from `/.well-known/openid-configuration` for OpenID Connect RP-initiated logout. |

#### webhooks

| Property | Required? | Value | Description |
| - | - | - | - |
| `api_version` | Yes | `string` matching a valid Shopify version (example: `2022-10`) | The API version used to serialize webhooks and cloud service events. |

**subscriptions**

Subscribe your app to Shopify webhook topics so that your app is alerted when an event occurs on a merchant's store. [Learn more about webhook subscriptions](https://shopify.dev/docs/apps/build/webhooks/get-started).

| Property | Required? | Value | Description |
| - | - | - | - |
| `topics` | Yes | `array` of `string`s matching a valid topic | The topics that your app subscribes to. Refer to a complete list of topics in the [webhooks reference](https://shopify.dev/docs/api/webhooks). |
| `compliance_topics` | No | `array` of `string`s matching a valid compliance topic | The topics to manage the requests to view or erase customer personal information. Valid options: `customers/redact`, `customers/data_request` or `shop/redact`. These are required [topics to subscribe to for all apps distributed in the Shopify App Store](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance). |
| `uri` | Yes | `string` matching a valid URI | Your app's endpoint to handle the events. It can be a HTTPS URL, a relative path starting with a slash, a Google Pub/Sub URI or an Amazon EventBridge Amazon Resource Name (ARN). |
| `filter` | No | `string` | A set of rules specified using Shopify API's Search Syntax. Ensures only webhooks that match the filter are delivered. [Learn more](https://shopify.dev/docs/apps/build/webhooks/delivery-filtering). |
| `include_fields` | No | `array` of `string`s | Specifies the fields that will be sent in a webhook's event message. If `null`, then all fields will be sent. [Learn more](https://shopify.dev/docs/apps/build/webhooks/delivery-structure#include_fields). |

**Info:** The following is the structure of the URL you should use for the URI when working with **Google Cloud Pub/Sub**: `pubsub://{project-id}:{topic-id}` — where `{project-id}` is the ID of your Google Cloud Platform project, and `{topic-id}` is the ID of the topic that you set up in Google Cloud Pub/Sub. For **Amazon EventBridge**, your URL will be similar to the following example: `arn:aws:events:<aws_region>::event-source/aws.partner/shopify.com/<app_id>/<event_source_name>`

#### events

| Property | Required? | Value | Description |
| - | - | - | - |
| `api_version` | Yes | `string` matching a valid Shopify version | The API version used to validate and run subscription `query` operations. |

**subscription**

Subscribe your app to Events topics to receive deliveries when qualifying changes occur in a merchant's store. [Learn more about Events subscriptions](https://shopify.dev/docs/apps/build/events/subscribe).

| Property | Required? | Value | Description |
| - | - | - | - |
| `handle` | Yes | `string` | Unique identifier for this subscription. Alphanumeric, `_`, `-`, max 50 characters. Included in the delivery payload and headers. |
| `topic` | Yes | `string` matching a valid Events topic | The resource your subscription listens to (for example, `Product`). See the [Events reference](https://shopify.dev/docs/api/events) for supported topics. |
| `actions` | Yes | `array` of `create`, `update`, and/or `delete` | The lifecycle transitions that can produce a delivery. |
| `uri` | Yes | `string` matching a valid URI | Your app's endpoint to handle deliveries. It can be a HTTPS URL, a relative path starting with a slash, a Google Pub/Sub URI, or an Amazon EventBridge ARN. |
| `triggers` | No | `array` of `string`s | Field paths that narrow `update` deliveries to specific field changes. Learn more about [Filtering deliveries with `triggers`](https://shopify.dev/docs/apps/build/events/delivery-filtering#triggers). |
| `query` | No | `string` | GraphQL Admin API operation whose result appears in the delivery `data` field. Learn more about [defining custom queries](https://shopify.dev/docs/apps/build/events/delivery-structure#custom-queries). |
| `query_filter` | No | `string` | Expression evaluated on the query result to suppress deliveries. Learn more about [Filtering deliveries with `query_filter`](https://shopify.dev/docs/apps/build/events/delivery-filtering#query-filters). |

#### app_proxy

Let Shopify act as a proxy when sending requests to your app. Learn more about [app proxy](https://shopify.dev/docs/apps/build/online-store/display-dynamic-data).

| Property | Required? | Value | Description |
| - | - | - | - |
| `url` | Yes if `app_proxy` defined | `string` matching a valid URL | URL of your app proxy server |
| `subpath` | Yes if `app_proxy` defined | `string` containing letters, numbers, underscores, and hyphens up to 30 characters. The value may not be `admin`, `services`, `password`, or `login`. | The combination of `prefix` and `subpath` defines where the app proxy is accessed from a merchant's shop. |
| `prefix` | Yes if `app_proxy` defined | `string` matching `a`, `apps`, `community`, or `tools` | The combination of `prefix` and `subpath` defines where the app proxy is accessed from a merchant's shop. |

#### pos

| Property | Required? | Value | Description |
| - | - | - | - |
| `embedded` | No | `boolean` | Load your [POS UI extension](https://shopify.dev/docs/api/pos-ui-extensions) or [App Home](https://shopify.dev/docs/api/app-home) app in Shopify POS. |

#### app_preferences

| Property | Required? | Value | Description |
| - | - | - | - |
| `url` | No | `string` matching a valid URL | URL for your app's preferences page |

#### build

Settings for running your app through Shopify CLI.

| Property | Required? | Value | Description |
| - | - | - | - |
| `automatically_update_urls_on_dev` | No | `boolean` | When `true`, your app URL and redirect URLs will be automatically updated on `dev`. This is useful when using the built-in tunnel for development. When `false`, your URLs won't be updated on `dev`. Recommended for production apps. When omitted, you will be prompted to choose an option on `dev`. |
| `dev_store_url` | No | `string` matching a valid store URL | The name of the dev store used to preview your app. |

### Migrate from config push

The `shopify app config push` Shopify CLI command is no longer supported. Instead, you can release your app configuration and extensions together with the [`deploy`](https://shopify.dev/docs/api/shopify-cli/app/app-deploy) command.

#### Migrate interactively

If you use the `shopify app config push` command without the `--force` flag, then follow these steps to migrate to the `deploy` command:

1. [Upgrade Shopify CLI](https://shopify.dev/docs/api/shopify-cli#upgrade) to the latest version.
2. Remove all references to the `shopify app config push` command in any scripts or aliases.
3. When you're ready to deploy both app configuration and all extensions, run the `deploy` command.

```terminal
shopify app deploy
```

4. Shopify CLI will ask if you want to start including app configuration on `deploy`. Answer `Yes, always`, and your choice will be saved in your app configuration file.
5. Continue the rest of the `deploy` flow to release a new app version to users.
6. Push your app configuration file to source control, so all contributors use the same app configuration. This ensures that the app and Shopify CLI commands behave the same way in each contributor's environment.

#### Update your CI/CD workflow

If you use the `shopify app config push` with the `--force` flag, follow these steps to migrate to the `deploy` command:

1. [Upgrade Shopify CLI](https://shopify.dev/docs/api/shopify-cli#upgrade) to the latest version.
2. Remove all references to the `shopify app config push` command.
3. Add the `deploy` command with the `--force` flag to your workflow, if it's not there already. Refer to the [example workflows](https://shopify.dev/docs/apps/launch/deployment/deploy-in-ci-cd-pipeline#examples) for more details.

---

## Manage access scopes

> Fonte: https://shopify.dev/docs/apps/build/authentication-authorization/app-installation/manage-access-scopes

After you've enabled [Shopify managed install](https://shopify.dev/docs/apps/build/authentication-authorization/app-installation), you can manage your app's [access scopes](https://shopify.dev/docs/api/usage/access-scopes).

**Note:** If you're still using the legacy installation and OAuth authorization code grant flow, then refer to the [authorization code grant](https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/authorization-code-grant#manage-access-scopes) guide on managing access scopes instead.

### Access scope configurations

There are two ways you can [configure your access scopes](https://shopify.dev/docs/apps/build/cli-for-apps/app-configuration#access_scopes):

| Configuration | Description |
| --- | --- |
| `scopes` | These configured access scopes are mandatory when merchants install your app with [Shopify managed install](https://shopify.dev/docs/apps/build/authentication-authorization/app-installation). Merchants **must** grant access before your app can be installed. Your app is guaranteed to have these access scopes after it's installed on the merchant's store. |
| `optional_scopes` | Unlike required scopes, optional scopes can only be requested by the app post-installation. When requested, merchants have the option to grant access to these scopes, or to decline them. Merchants can also revoke previously granted optional scopes. Optional scopes are useful if you want to provide certain features to different stores, without forcing every app install to provide the same data access. |

#### Scopes

The required access scopes are defined in the `scopes` field of your app's TOML file:

```toml
name = "Example App"
client_id = "a61950a2cbd5f32876b0b55587ec7a27"
application_url = "https://www.app.example.com/"
embedded = true

[access_scopes]
scopes = "read_discounts,write_products"
```

When a merchant installs your app, they're prompted to grant permission to **all** the access scopes that you've defined in the `scopes` field. After the app is installed, it's guaranteed to have the required access scopes.

#### Optional scopes

The access scopes that can be [requested dynamically](#request-new-access-scopes-dynamically) are defined in the `optional_scopes` field of the app's TOML file:

```toml
name = "Example App"
client_id = "a61950a2cbd5f32876b0b55587ec7a27"
application_url = "https://www.app.example.com/"
embedded = true

[access_scopes]
scopes = "" # The `scopes` field is still necessary, but can be empty.
optional_scopes = ["read_discounts", "write_products"]
```

When a merchant installs your app, they're not prompted during installation to grant permission to the access scopes that you've defined in the `optional_scopes` field.

The [app initiates the request](#request-new-access-scopes-dynamically) to gain access to these scopes after the installation is complete, if necessary.

### Modify declared scopes

To declare more or fewer access scopes for your app, update your app's [configuration TOML file](https://shopify.dev/docs/apps/build/cli-for-apps/app-configuration#access_scopes) and deploy the changes.

1. Modify the `scopes` or `optional_scopes` fields in your app's TOML file to include the desired set of access scopes.
2. Deploy the access scope changes by running the following Shopify CLI command:

```terminal
shopify app deploy
```

3. (Optional). Subscribe to the [app/scopes_update](https://shopify.dev/docs/api/webhooks/latest?reference=toml#list-of-topics-app/scopes_update) topic to receive webhooks when the granted scopes are updated.

#### Modifying the `scopes` field

If you modified the `scopes` field, then the following behavior occurs:

- Merchants will be prompted to approve the updated access scopes when they open your app.
  - The `app/scopes_update` webhook will be triggered when the merchant approves the access scope changes.
- If the change is a reduction of scopes, the merchant won't be prompted and the app will lose access to the scopes automatically when the merchant opens the app.
  - The `app/scopes_update` webhook will be triggered when the user opens the app.

#### Modifying the `optional_scopes` field

If you modify the `optional_scopes` field, then the following behavior occurs:

- Your app can now start [requesting the new access scopes](#request-new-access-scopes-dynamically).
- The granted access scopes for your app installation won't change until your app requests for the new access scopes dynamically and the merchant grants your app access to the newly updated scopes.
  - The `app/scopes_update` webhook will be triggered when the merchant approves the access scope changes.

#### Moving a scope between `scopes` and `optional_scopes`

You can change whether a scope is required or optional by moving its handle between the `scopes` and `optional_scopes` fields, and then deploying the change.

If you move a scope from `scopes` to `optional_scopes`, then the following behavior occurs:

- Stores that already granted the scope while it was required keep it. The scope is retained as an approved optional scope, so the merchant isn't re-prompted and the scope isn't revoked when they open your app. You don't need to request the scope again for existing installations.
- New installations don't receive the scope until your app [requests it dynamically](#request-new-access-scopes-dynamically), the same as any other optional scope.

A required scope can't implicitly grant an optional one. For example, `write_products` grants `read_products`, so if you declare `read_products` as optional while `write_products` is still required, then deploying fails with the following error:

```text
Declared optional_scopes [read_products] cannot be implicit required scopes.
```

To resolve this, move or remove the scope that grants it implicitly. In this example, you'd move or remove `write_products`.

### Query currently granted scopes

You can use [GraphQL queries](https://shopify.dev/docs/api/admin-graphql/latest/queries/currentAppInstallation) to get the currently granted access scopes for your app installation.

**Example request to retrieve currently granted access scopes using currentAppInstallation**

```graphql
query {
  currentAppInstallation {
    accessScopes {
      description
      handle
    }
  }
}
```

**Response**

```json
{
  "data": {
    "currentAppInstallation": {
      "accessScopes": [
        {
          "description": "Modify products, variants, and collections",
          "handle": "write_products"
        },
        {
          "description": "Read products, variants, and collections",
          "handle": "read_products"
        }
      ]
    }
  }
}
```

**Shopify API libraries**

You can also use the following helper methods in Shopify's API libraries to query for the currently granted access scopes:

| Library | Method |
| --- | --- |
| App Bridge API | [shopify.scopes.query()](https://shopify.dev/docs/api/app-home/apis/scopes#scopes-propertydetail-query) |
| React Router API | [scopes.query()](https://shopify.dev/docs/api/shopify-app-react-router/latest/apis/scopes#scopes-propertydetail-query) |

### Request new access scopes dynamically

**Note:** You can only request additional access scopes dynamically if they are configured as `optional_scopes` in your app's TOML file, and if the configuration changes have been deployed. Access scopes configured in the `scopes` field can't be requested dynamically.

#### Request access scopes using the App Bridge API

If your app is rendered in the Shopify admin, you should use the [App Bridge scopes API](https://shopify.dev/docs/api/app-home/apis/scopes#scopes-propertydetail-request) to request new access scopes dynamically.

```javascript
shopify.scopes.request(['read_discounts', 'write_products']);
```

This method doesn't require a browser redirect and can be performed on the client side of your app. This asynchronous, client-side method displays a permission grant modal for the access scopes requested, on top of your running app.

#### Request access scopes using a request URL for standalone apps

To request optional scopes dynamically for a standalone app, you can direct the merchant to the request URL so they can grant approval to the new access scopes.

**Browser redirect URL**

```text
https://admin.shopify.com/store/{STORE_NAME}/oauth/install?client_id={CLIENT_ID}&optional_scopes={REQUESTED_SCOPES}
```

| Query parameter | Description |
| --- | --- |
| `STORE_NAME` | The name of the merchant's store |
| `CLIENT_ID` | The app's client ID |
| `REQUESTED_SCOPES` | A comma separated list of access scopes to request. This must be a subset of the declared `optional_scopes` in your TOML file. |

**Example request URL**

```text
https://admin.shopify.com/store/my-cool-store/oauth/install?client_id=a61950a2cbd5f32876b0b55587ec7a27&optional_scopes=read_discounts,write_products
```

**Shopify API libraries**

You can use the following helper methods in Shopify's API libraries to request for new access scopes dynamically:

| Library | Method | Description |
| --- | --- | --- |
| App Bridge API | [shopify.scopes.request()](https://shopify.dev/docs/api/app-home/apis/scopes#scopes-propertydetail-request) | This asynchronous, client-side method displays a permission grant modal for the access scopes requested, on top of your running app. |
| React Router API | [scopes.request()](https://shopify.dev/docs/api/shopify-app-react-router/latest/apis/scopes#scopes-propertydetail-request) | This is recommended for standalone apps and server side handling from a React Router app. |

### Revoke granted scopes dynamically

**Note:** Only scopes configured as `optional_scopes` and that were [dynamically granted](#request-new-access-scopes-dynamically) can be revoked. Access scopes configured in the `scopes` field can't be revoked dynamically.

If your app no longer requires certain access scopes from a merchant's store, we recommend revoking the access scopes. This helps to avoid a potential data leak, if the access token is ever compromised.

You can revoke access scopes by making a [GraphQL mutation](https://shopify.dev/docs/api/admin-graphql/latest/mutations/appRevokeAccessScopes).

**Example request to revoke granted optional access scopes**

```graphql
mutation {
  appRevokeAccessScopes(scopes: ["read_discounts","write_products"]) {
    revoked {
      handle
    }
    userErrors {
      field
      message
    }
  }
}
```

**Response**

```json
{
  "data": {
    "appRevokeAccessScopes": {
      "revoked": [
        {
          "handle": "write_discounts"
        },
        {
          "handle": "write_products"
        }
      ],
      "userErrors": []
    }
  }
}
```

**Shopify API libraries**

You can use the following helper methods in Shopify's API libraries to revoke granted access scopes:

| Library | Method |
| --- | --- |
| App Bridge API | [shopify.scopes.revoke()](https://shopify.dev/docs/api/app-home/apis/scopes#scopes-propertydetail-revoke) |
| React Router API | [scopes.revoke()](https://shopify.dev/docs/api/shopify-app-react-router/latest/apis/scopes#scopes-propertydetail-revoke) |

### Developer tools and resources

- [App Bridge scopes API](https://shopify.dev/docs/api/app-home/apis/scopes) – Learn how to use the `scopes` API in the App Bridge library.
- [React Router scopes API](https://shopify.dev/docs/api/shopify-app-react-router/latest/apis/scopes) – Learn how to use the `scopes` API in the React Router library.
- [Token exchange](https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/token-exchange) – Learn how to acquire access tokens for apps through token exchange.
- [Shopify API access scopes](https://shopify.dev/docs/api/usage/access-scopes) – Learn more about access scopes.
- [Shopify CLI configuration file](https://shopify.dev/docs/apps/build/cli-for-apps/app-configuration#access_scopes) – Learn more about Shopify CLI configuration file.

---

# Distribution & launch

Mini-indice della sezione:

- [About App Distribution](#about-app-distribution)
- [Select a distribution method](#select-a-distribution-method)
- [About the Shopify App Store](#about-the-shopify-app-store)
- [About the app review process](#about-the-app-review-process)
- [Best practices / App requirements checklist](#best-practices--app-requirements-checklist)
- [Built for Shopify requirements](#built-for-shopify-requirements)

---

## About App Distribution

> Fonte: https://shopify.dev/docs/apps/launch/distribution

After you've added features to your app, you need to decide how to distribute it to merchants.

The way you choose to distribute your app depends on its purpose and your audience. You can't change the distribution method after you select it, so make sure that you understand the different capabilities and requirements of each type.

### Capabilities and requirements

The following table shows the capabilities and requirements that are associated with each distribution method:

| Distribution model | Number of stores | App type | Authorization or authentication method | Approval required | Limitations |
| - | - | - | - | - | - |
| Public distribution | Can be installed on multiple Shopify stores | Public | If embedded, token exchange and session tokens; If not embedded, authorization code grant | Yes | Must sync certain data with Shopify |
| Custom distribution | Installed on a single Shopify store, on multiple stores that belong to the same Plus organization or any transfer-disabled development stores | Custom | If embedded, token exchange and session tokens; If not embedded, authorization code grant | No | Can't use the Billing API to charge merchants |
| Shopify admin | Installed on a single Shopify store | Custom | Authenticate in the Shopify admin | No | Can't use Shopify App Bridge to display in the Shopify admin; Can't use app extensions; Can't use the Billing API to charge merchants |

**Note:** Checkout apps and extensions have design requirements that apply to custom apps as well as public apps. Be sure that your app meets all requirements for its functionality and distribution type.

#### Requesting a content size limit exception

Theme app extensions are subject to file and content size limits. If your app uses custom distribution, or your app has been granted Built for Shopify status in the Shopify App Store, then you can request an exception to the 100 KB Liquid size limit for a theme app extension. File an exemption request using the provided form.

Increasing your app's Liquid size could potentially impact its performance. Regular monitoring and optimization is advised.

### Deprecated app types

The following app types can no longer be created:

- **Private apps**: Deprecated as of January 2022. A private app was a type of app that one merchant could install directly on their store. If you want to create an app specifically for one merchant's store, then you can create a custom app instead. As of January 20, 2023, all private apps have been automatically migrated and converted to custom apps.
- **Unpublished apps**: Deprecated as of December 9, 2019. An unpublished app was a type of public app that one or many merchants could install and had all the same functionality as other public apps. However, the app didn't require any approval from Shopify.

### Next steps

Learn how to select a distribution method.

---

## Select a distribution method

> Fonte: https://shopify.dev/docs/apps/launch/distribution/select-distribution-method

Before sharing your app with merchants, you need to select a distribution method in the Partner Dashboard.

The distribution method you choose depends on your app's purpose and target audience. This selection cannot be changed afterward, so ensure you understand the different capabilities and requirements of each type.

When creating an app through the Dev Dashboard or using Shopify CLI, you can select from these distribution methods:

- **Public distribution**: Make your app public and distribute or sell it to many merchants through the Shopify App Store.
- **Custom distribution**: Distribute a custom app to one store or multiple stores within the same Plus organization using a link.

If you have separate apps for development and production, select the distribution method in your production app.

**Note:** Custom apps created through the Shopify admin cannot have their distribution method changed.

For more information, see the [features and limitations of app types](https://shopify.dev/docs/apps/launch/distribution#capabilities-and-requirements).

### Select a distribution method

1. From the Partner Dashboard, go to **App distribution**.
2. Select your app from the list.
3. Click **Choose distribution**.
4. Select a distribution method, and then click **Select**.

With **Public distribution**, you can create your Shopify App Store listing and submit your app for review when ready.

With **Custom distribution**, you can install your custom app on one or multiple stores within the same Plus organization.

### Install a custom app on multiple stores

**Note:** Custom apps created before July 26, 2023 require contacting Partner Support to enable multi-store installation.

For custom apps created after July 26, 2023, follow these steps:

1. After selecting **Custom distribution**, enter the store's myshopify.com or admin.shopify.com domain.
2. Optional: Uncheck **Allow multi-store installs for one Plus organization** to limit installs to one store.
3. Click **Generate link** to create the app install link.
4. Copy the install link.

Share the install link with users so they can install your app, such as by emailing it to the store owner.

---

## About the Shopify App Store

> Fonte: https://shopify.dev/docs/apps/launch/app-store-review

With targeted recommendations and relevant categories, the [Shopify App Store](https://apps.shopify.com) is the best place for Shopify merchants to find apps that they can use to build their business. As an app developer, you can create apps for the Shopify App Store to reach millions of entrepreneurs around the world, and use Shopify's Billing API to create pricing models that let you grow your own app development business.

Your App Store listing is the foundation for all app discovery. Whether merchants find your app through browsing the App Store, receiving recommendations in their admin workflow, or asking Sidekick for help, all these experiences draw from your public App Store listing information including your description, features, pricing, and reviews.

### Getting your app approved

When you're ready to [distribute your app on the Shopify App Store](https://shopify.dev/docs/apps/launch/distribution), you need to submit it to Shopify's App Approval team and make sure it meets all requirements.

- View the complete list of [app requirements](https://shopify.dev/docs/apps/launch/app-requirements-checklist).
- Learn more about the [app review process](https://shopify.dev/docs/apps/launch/app-store-review/review-process).
- Find out if your app needs to meet the [protected customer data requirements](https://shopify.dev/docs/apps/launch/protected-customer-data).
- Learn more about our [support requirements](https://shopify.dev/docs/apps/launch/distribution/support-your-customers) for app developers.

### Charging for your app

Shopify's Billing API lets you charge merchants a one-time fee for your public app, or you can charge them for an ongoing subscription.

Apply for our reduced revenue share plan to pay only 15% revenue share on all app revenue, reduced from 20%. [Eligible developers](https://shopify.dev/docs/apps/launch/distribution/revenue-share#calculating-shopify-app-store-revenue) pay 0% revenue share on the first $1,000,000 USD earned.

- Learn more about [using the Billing API](https://shopify.dev/docs/apps/launch/billing).
- Learn more about [app revenue share](https://shopify.dev/docs/apps/launch/distribution/revenue-share).

### Marketing and supporting your app

After your app is [listed](https://shopify.dev/docs/apps/launch/distribution/visibility) on the Shopify App Store, you can market and support your app to make it more successful. Successful developers market their app both through Shopify and externally, offer great customer service to merchants, and manage their app reviews.

Get advice on [being successful in the Shopify App Store](https://shopify.dev/docs/apps/launch/distribution/go-to-market-success).

### Improving quality and getting promoted

Merchants want apps that are easy to use, safe, and performant, and that solve their problems. To help merchants to find apps that meet their needs, Shopify adds indicators of quality to apps, and promotes high quality apps on various surfaces, including the Shopify App Store, in-admin, and Sidekick. Apps that meet all of our criteria are given Built for Shopify status, our highest level of recognition and achievement.

To learn about our quality standards, and how you can earn achievements that grant you quality indicators and promotion opportunities, refer to [Built for Shopify](https://shopify.dev/docs/apps/launch/built-for-shopify).

### Shopify App Store ads

As an app developer, you can create search ads to help merchants discover your apps in the Shopify App Store. Ads are shown to merchants on the search results page above the organic search results.

- Learn more about [Shopify App Store ads](https://shopify.dev/docs/apps/launch/marketing/advertising).

---

## About the app review process

> Fonte: https://shopify.dev/docs/apps/launch/app-store-review/review-process

When you submit an app, it goes through an app review process to ensure it meets Shopify's [requirements for safe, quality apps](https://shopify.dev/docs/apps/launch/app-requirements-checklist). Shopify's app requirements are identical for both fully visible and limited visibility public apps. If you plan to list your app on the Shopify App Store, Shopify also reviews your listing page content.

To reduce review time and ensure smooth processing, follow the tips in the sections below as you develop your app and prepare your submission. For common rejection reasons, see [Common review problems](https://shopify.dev/docs/apps/launch/app-store-review/pass-app-review#common-app-review-problems).

### Review process

Your app must satisfy all requirements on the App Store review page before evaluation begins. During review, your app progresses through statuses: Draft, Submitted, Reviewed, and Published. Track your app's status on your App Store review page.

#### Preliminary steps

Public apps start in **Draft** status. You must resolve any issues flagged on the Shopify App Store review page before [submitting your app](https://shopify.dev/docs/apps/launch/app-store-review/submit-app-for-review) for review. After making corrections, click **Submit your app** to send it for evaluation.

#### App review

After submission, your app enters **Submitted** status and you receive a confirmation email. You can withdraw anytime by clicking **Withdraw** in the status banner.

If your app fails core requirements preventing reviewer evaluation, it moves to **Paused** status with an email outlining required changes. After corrections, click **Submit fixes** in the status banner to resubmit.

Once core requirements are met, a reviewer is assigned. If additional fixes requiring discussion arise, your app moves to **Reviewed** status with an email detailing next steps—you must reply to continue.

Upon approval, you receive confirmation that your app has reached **Published** status and now appears on the Shopify App Store.

**Note:** By default, all approved app listings display in the Shopify App Store. Learn more about [listing visibility](https://shopify.dev/docs/apps/launch/distribution/visibility).

### Next step

[Prepare your app for review](https://shopify.dev/docs/apps/launch/app-store-review/pass-app-review): Test your app on a development store before submission to identify any bugs or errors.

---

## Best practices / App requirements checklist

> Fonte: https://shopify.dev/docs/apps/launch/app-requirements-checklist

> Nota: questa URL reindirizza a "Best practices for apps in the Shopify App Store". L'elenco numerato dei requisiti vincolanti è disponibile su `https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements` (vedi Pagine aggiuntive).

These best practices are intended to provide the best experience across the entire app lifecycle, from branding, to installation, to onboarding, functionality, and quality. For a list of all the requirements that need to be met to be eligible for the Shopify App Store, refer to the [App Store requirements](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements).

### General best practices for all apps

The best practices in this section apply to [all apps distributed through the Shopify App Store](https://shopify.dev/docs/apps/launch/distribution). Additional category-specific best practices are presented in the section below.

### 1. Prohibited and restricted app configurations

Some types of apps aren't permitted on the Shopify App Store and others must have their visibility set to limited visibility. See [App Store requirement 1.1](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements#build-and-operate-within-shopifys-platform) for more information.

### 2. Installation and setup

Merchants should be able to quickly set up and start using your app. This section describes the correct flows for authentication, app install charges, and any sign-up steps (if required). These best practices make sure that you provide merchants with the guidance they need when they start learning to use your app.

#### A. Authentication

Your app should immediately authorize using [OAuth](https://shopify.dev/docs/apps/build/authentication-authorization) before any other steps occur, even if the merchant has previously installed and then uninstalled your app. See [App Store requirement 2.3](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements#provide-seamless-and-secure-installation) for more information.

#### B. Permissions

[Permissions](https://shopify.dev/docs/api/usage/access-scopes) are the levels of access that your app has to a merchant's store through the API. The permissions that you request are shown to the merchant on the OAuth grant page, where the merchant can either grant or decline them. See [App Store requirement 3.2](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements#request-only-necessary-access-scopes) for more information.

#### C. Setup and merchant workflows

For merchant security, your app shouldn't use pop-up windows for essential app functionality, like running OAuth or approving app charges. Avoiding the use of pop-up windows also protects your app from being compromised by pop-up blockers.

If your app adds secondary payments to orders because of post-purchase upsells or other order edits, then you consider telling merchants that orders might have multiple payments associated with them. We recommend including a note in your Shopify App Store listing and the app setup instructions to tell merchants that if they're capturing payments manually, then they might need to capture more than one payment for a single order.

See [App Store requirement 2.3](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements#provide-seamless-and-secure-installation) for more information.

### 3. Functionality and quality

For your app to be successful, it should offer a consistent and positive experience for the merchants who use it. The following functionality and quality best practices apply to the core features of your app, such as its user interface, performance, and billing.

#### A. User interface

By offering a great user interface, you can make it easier for merchants to use your app to grow their businesses. See the [App Design Guidelines](https://shopify.dev/docs/apps/design) to learn more about how to design and build your app's user interface. Additionally, see the [Functionality](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements#functionality) section of the App Store requirements to understand what specific conditions must be met for your app to be eligible for the Shopify App Store.

#### B. Billing

Shopify offers managed pricing as well as an API-based billing system to support different types of app charges. It bills merchants through the same system that's used for their Shopify subscription, and makes it easier for them to keep track of their payments.

Your app should allow merchants to upgrade and downgrade their pricing plan without having to contact your support team or having to reinstall the app. This includes ensuring that the charges are successfully processed in the application charge history page in the merchant admin.

Enterprise-level pricing plans should be referenced in the **Description of additional charges** section of the pricing section of the app's listing.

See [App Store requirement 1.2](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements#bill-through-the-shopify-billing-api-or-managed-pricing) for more information.

#### C. State of the app

**Caution:** Make sure your app is compliant with the latest [Google Chrome cookie behavior](https://www.chromium.org/updates/same-site) and [compatible with the SameSite cookie attribute](https://shopify.dev/docs/apps/build/authentication-authorization/session-tokens).

Merchants are busy, and every minute matters when running their businesses. By making sure that your app performs well, you can help merchants achieve their goals faster and spend more time on the problems that need their attention the most.

Apps that no longer reflect the original core functionality submitted to the App Store will be re-evaluated and will need to be resubmitted for a full App review.

See [App Store requirement 2.1](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements#create-reliable-and-user-friendly-apps) for more information.

### 4. App performance

For merchants to be successful, their online stores should have best-in-class speed and user experience. Apps can easily slow down performance, and we require apps to keep performance top-of-mind while helping merchants, to follow our performance requirements and best practices, and to test that their products continue to meet our minimum requirements for speed.

**Tip:** For best practices and recommendations on app performance, refer to our [app performance recommendations](https://shopify.dev/docs/apps/build/performance).

#### A. Performance score

Your app shouldn't reduce Lighthouse performance scores by more than 10 points. Test your app's impact on Lighthouse performance scores using the steps outlined in [Testing storefront performance](https://shopify.dev/docs/apps/best-practices/performance/storefront#testing-storefront-performance).

#### B. Testing methodology

For apps that affect storefronts directly, Shopify tests the app's effect on store performance by measuring the Lighthouse score before and after the app is installed. We calculate a weighted average of score from the following pages:

| Page | Weight |
| - | - |
| Home | 17% |
| Product details | 40% |
| Collection | 43% |

The difference in the score before and after the app is installed and configured on the above pages indicates whether the app improves or worsens store performance. Your app should consistently demonstrate low or no negative impact on the performance of real merchant stores over time.

**Note:** Lighthouse scores can vary between runs. Consider running these tests frequently during your development, and averaging your scores across a few consecutive Lighthouse tests before submission.

### 5. App listing

Your app listing is often your biggest marketing tool—an effective listing helps merchants understand how it can help them run their business. Make sure your listing is clear, includes pricing, and showcases your app's benefits.

To create a listing, select [Shopify App Store as the distribution method](https://shopify.dev/docs/apps/launch/distribution/select-distribution-method). All approved public apps have a listing on the Shopify App Store, regardless of whether you choose to make it [full or limited visibility](https://shopify.dev/docs/apps/launch/distribution/visibility)

See [App Store requirements section 4](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements#app-store-listing) for more information.

The listing fields shown in an example listing are: Feature media, Demo store URL, Screenshots, App introduction, App details, Feature list, Integrations.

#### A. Branding your app

Your app name should be unique and start with your brand name (not a generic descriptor). Lead with your distinctive brand to differentiate from similar apps. For example, "QTeck - Announcement Bar" rather than "Announcement Bar - QTeck". Keep names to 30 characters or fewer. Your app name in the TOML configuration should align with your App Store listing name.

For your app icon, use bold colors and simple, recognizable patterns. Avoid text, screenshots, and Shopify trademarks. Keep corners square (they're automatically rounded) and include padding so your logo doesn't touch the edges. Use JPEG or PNG format at 1200px by 1200px.

[Download image templates](https://shopify.dev/zip/SubmissionTemplates.zip)

See [App Store requirement 4.1](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements#brand-your-app-uniquely-and-present-it-consistently-) for more information.

#### B. App store listing content

**1. Feature media** — A short video (2-3 minutes) is the best way to showcase your app's impact. Keep it promotional rather than instructional and limit screencasts to 25% of the video. If you don't have a video, use a static image that conveys your app's benefit or unique value. When creating feature images (1600px by 900px, 16:9), keep them simple with one focal point, use solid backgrounds with good contrast (4.5:1 ratio recommended), and always include alt text. Don't use Shopify logos or repeat your app card subtitle in the image.

**2. Demo store URL** — Provide a link to a [development store](https://shopify.dev/docs/api/development-stores) that showcases your app. Link directly to the page that best demonstrates your app's functionality and add contextual instructions to guide merchants through the experience. A thoughtfully designed demo helps merchants visualize your app's value.

**3. Screenshots** — Screenshots should be 1600px by 900px (16:9). Include 3-6 desktop screenshots, including at least one of your app's UI. Ensure images are clear and focused on your app's functionality. Crop out browser chrome and sensitive information. Provide alt text, avoid PII, and don't include pricing, reviews, or outcome guarantees. If your app is mobile-responsive or works with POS, include screenshots showing those experiences.

**4. App introduction** — Your app introduction (100 characters) should clearly highlight the benefits merchants can expect. Tie your unique offering to measurable business outcomes. Avoid keyword stuffing, data claims, and incomplete sentences.

| Examples | Reason |
| - | - |
| **Do**: We package and ship your orders. Fast, simple fulfillment can boost sales and delight customers. **Don't**: Get your products shipped fast. We'll take care of all the busy work for you. | Show specific benefits that drive value for merchants. Avoid generic marketing language. |
| **Do**: Create print-on-demand custom puzzles. More customization options can help increase product sales. **Don't**: Custom puzzles. A creative solution to your print-on-demand needs. | Tie your unique app offering to a measurable business outcome. |
| **Do**: Easily create personalized email campaigns. Buyer targeting can increase customer lifetime value. **Don't**: App Name is a best in class customer platform. Email marketing, text automation, Facebook custom audiences. | Show a clear merchant benefit and value proposition. Avoid unsubstantiated claims, keyword stuffing, and incomplete sentences. |

**5. App details** — In your app details (500 characters), describe functional elements and what makes your app unique. Avoid excessive marketing language, keyword stuffing, and outcome guarantees. Keep support info, links, and testimonials in their designated fields.

**6. Feature list** — Describe the functionality, not the technical mechanics. Keep features short and scannable (up to 80 characters per feature)—focus on what merchants care about, not how it's built.

| Examples | Reason |
| - | - |
| **Do**: Reports that show you sales data in real time. **Don't**: Reports that use the latest push technology to offer you sales data with only 250ms of latency. | Describe functionality that is meaningful to merchants. Avoid focusing on the technical aspects of a feature. |
| **Do**: Drag and drop page builder. **Don't**: Page builder built on the latest React Native technology to ensure the most efficient page building experience. | Be concise and informative. Avoid including feature mechanics that aren't relevant to merchants. |
| **Do**: Customize details like shape and difficulty level in a full-screen experience. **Don't**: Print-on-demand, product customization, sales analytics, puzzles. | Describe a specific, unique feature. Avoid keyword stuffing and incomplete sentences. |

**7. Integrations** — List up to six integrations that merchants will be most interested in. Don't include Shopify itself, other shopping carts (unless you provide synchronization), or other Shopify apps (unless you directly integrate with them).

#### C. Pricing

Choose your primary billing method (Free to install, Recurring charge, or One-time payment) and provide clear pricing information in the designated section only. If you have paid plans, consider offering a free trial (we recommend 14 days). Plans display from lowest to highest price automatically.

For apps with free and paid plans, select **Recurring charge** and mark one plan as **Free**—this shows "Free plan available" in search results.

See [App Store requirement 4.2](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements#keep-pricing-accurate-and-in-designated-areas) for more information.

#### D. Translate your app listing

Translated listings help your app reach a wider audience—they convert up to 4x better in non-English markets. List all languages your app's UI supports in your app store listing. To learn more about app translation, refer to [Internationalization](https://shopify.dev/docs/apps/build/localize-your-app).

English listings set as primary are automatically translated to: Brazilian Portuguese, Danish, Dutch, French, German, Simplified Chinese, Spanish, Swedish.

You can also add your own custom translations in the [Partner Dashboard](https://partners.shopify.com/organizations).

**Note:** Automated translation covers: App card subtitle, App introduction, App details, Features, Pricing details, Search terms, and image alt text. Adding a custom translation overwrites the automated one for that language.

Adding your own translated listing for an automatically translated language overwrites and disables automatic translation for that language. Deleting your translated listing resumes automated translation for that language.

To add a translated listing, go to **Apps** > your app > **Distribution** > **Manage listing** > **Add translated listing**. To delete a custom translation (which re-enables automation), use **More actions** > **Delete listing**.

#### E. App discovery

Choose accurate [categories and tags](https://shopify.dev/docs/apps/launch/app-store-review/app-listing-categories) that reflect your app's core functionality—this impacts discoverability. You can select up to 25 structured features per category to help merchants compare relevant app features.

If your app capabilities change and you want to change how your app is categorized, then you can submit an appeal to change the app categorization by using the link in the app submission form. After the Shopify app review team completes their review, they'll send a response, whether it's approved or rejected.

Include a privacy policy (required) and consider adding other helpful links to your developer website such as FAQ page, changelog, support portal, tutorial, and additional documentation. These resources help merchants understand and get the most value from your app. Link to dedicated pages rather than promotional landing pages or cloud documents.

Your app card subtitle should highlight benefits to merchants rather than just describing functions. For search terms, enter up to five relevant terms using complete words (not partial) and limit to one idea per term—for example, "email marketing" works, but "email marketing for leads" doesn't.

| Examples | Reason |
| - | - |
| **Do**: Avoid lost sales by making pages load faster and improving SEO. **Don't**: Boost Pagespeed in 1 click. Increase conversions, SEO & Sales. | Highlight the benefit to merchants instead of the function. Avoid incomplete sentences. |
| **Do**: Pick products to sell from vetted manufacturers and suppliers. **Don't**: Dropship via Wholesale Distributors, Manufacturers & Suppliers | Highlight the benefit to merchants instead of the function. |
| **Do**: Control which customers access different parts of your store. **Don't**: Access control, for anything in your online store :) | Highlight the benefit to merchants instead of the name of the feature. |

Optimize your title tag and meta description for search engines. Follow [Google's title tag best practices](https://developers.google.com/search/docs/advanced/appearance/title-link) and [write effective meta descriptions](https://www.shopify.com/blog/how-to-write-meta-descriptions) to improve click-through rates from search results.

#### F. Merchant install eligibility

Set install eligibility criteria in the app submission form to reduce uninstalls and negative reviews from ineligible merchants. Specify which sales channels your app needs (Online Store or POS) and geography criteria (country, shipping, currency) to target the right merchants. If a merchant changes their store settings after installation, use endpoints and webhooks to detect changes and notify them.

See [App Store requirement 4.3](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements#provide-accurate-and-truthful-listing-information) for more information.

#### G. App review preparation

Provide clear instructions and a complete screencast showing your app's setup process and functionality. If your app integrates with third-party platforms, include valid test credentials that grant full access. Make screencasts in English or with English subtitles, and demonstrate the expected outcome for each test case.

See [App Store requirement 4.5](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements#ensure-your-submission-is-complete-and-accurate) for more information.

### 6. Security and merchant risk

Before you submit your app, make sure it's secure so the merchants who use it won't be at risk. See [App Store requirements section 3](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements#security) for more information.

### 7. Data and user privacy

Merchants trust you with their customers' sensitive data. Proper data handling protects merchants from privacy violations, legal liability, and loss of customer trust. Include a privacy policy in your listing to build transparency and confidence with merchants.

See [App Store requirements section 3](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements#security) for more information.

**Tip:** Your app should use supported APIs only—apps using APIs that will be deprecated within 90 days can't be submitted. Review [API versioning policies](https://shopify.dev/docs/api/usage/versioning) for details.

### 8. Support

Strong support helps merchants succeed with your app and reduces negative reviews from frustrated users. Provide clear, Shopify-specific instructions in your help documentation and in-app context so merchants can quickly resolve issues themselves. Refer to Polaris [Help documentation](https://polaris.shopify.com/content/help-documentation) guidelines for writing effective support content. Keep your [emergency developer contact information](https://shopify.dev/docs/api/usage/versioning/updates#update-your-developer-contact-details) up to date in your Partner Dashboard.

See [App Store requirement 4.5](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements#ensure-your-submission-is-complete-and-accurate) for more information.

### Category-specific best practices

Certain app types have unique impacts on merchant operations and require different APIs, extensions, and implementations. These category-specific best practices ensure these apps properly serve their use cases. Note that some apps may fall into multiple categories.

#### 9. Online store

Online store apps help merchants customize their storefront experience. Use [theme app extensions](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions) to modify merchant themes—avoid requiring manual code changes. For vintage theme support, provide clear instructions for manual integration. Use [app proxies](https://shopify.dev/docs/apps/build/online-store/display-dynamic-data) to forward requests and display data. Ensure your app works properly in both the Theme Editor and theme editor environment, and provide detailed setup instructions with deep links. Keep app branding minimal—use standard attribution (24x24 pixels) unless customers directly interact with branded elements as part of their experience (like payment methods or loyalty programs). Let merchants preview edits before publishing storefront changes.

**App Name Branding** in storefront visual components is permitted only when (1) customers directly interact with the custom branding elements as a key aspect of their buying experience (e.g. part of a payment method or loyalty program), or (2) removing the custom branding elements would cause confusion or harm to customers. If neither criterion is met, the app must use the standard app attribution pattern. No app is permitted to request app reviews/ratings or promote other apps or services. App Name Branding includes logos/icons/watermarks/imagery, the company or app name displayed as text in any form, and custom design elements containing the name or logo. Standard app attribution is limited to a 24x24 pixel width and height on any image or text. See [App Store requirement 5.1](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements#online-store).

#### 10. Apps rendered in the Shopify admin

Use [Shopify App Bridge](https://shopify.dev/docs/api/app-home) to ensure OAuth redirects to your app, and provide a consistent experience by integrating off-platform features into the Shopify admin. Use session tokens for authentication and avoid third-party cookies or local storage, as they may not work in all browsers. Ensure your app functions in Chrome's incognito mode. If using max modal (full screen mode), launch it only from merchant interactions (not from the navigation menu) and use it for complex editors or workflows where it improves the user experience. For POS apps, ensure all POS actions are complete and your UI is accessible from the POS Apps Admin Dashboard. See [App Store requirement 2.2](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements#use-shopifys-apis-and-platform-tools).

#### 11. Product sourcing

Use a PCI-compliant gateway for goods sold to merchants, but charge other app costs through the [Billing API](https://shopify.dev/docs/apps/launch/billing). Don't automatically fulfill orders in pending payment state—this protects you from fraud risk. Add cost of goods to the Cost field in the merchant's product page, and avoid selling high-risk products that violate Shopify's [Acceptable Use Policy](https://www.shopify.com/legal/aup). Use the [`fulfillmentOrderSubmitFulfillmentRequest`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/fulfillmentOrderSubmitFulfillmentRequest) mutation for fulfillment requests. See [App Store requirement 5.5](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements#product-sourcing).

#### 12. Mobile app builders

Convert your mobile app builder into a Sales Channel to enable checkout creation. Provide either a customizable theme builder or preset themes, and include detailed instructions for creating developer accounts and submitting to the Apple App Store or Google Play. Apps built by your builder should not make direct requests to the authenticated GraphQL Admin API—store client secrets and access tokens on a secure web server, not on mobile devices. See [App Store requirement 5.9](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements#mobile-app-builders).

#### 13. Sales channels

Build your sales channel using [Polaris components](https://polaris.shopify.com/getting-started) and [cart permalinks](https://shopify.dev/docs/apps/build/checkout/create-cart-permalinks) that take customers directly to Shopify's checkout. After OAuth installation, redirect merchants to the [account connection](https://polaris.shopify.com/components/actions/account-connection) component and allow them to connect and disconnect their account. Use [banner](https://polaris.shopify.com/components/feedback-indicators/banner) components to communicate approval status. In your publishing section, show the number of published products with links to the bulk editor, and use the [GraphQL Admin API products query](https://shopify.dev/docs/api/admin-graphql/latest/queries/products#argument-query-filter-published_status) to retrieve products. Communicate product issues using [ResourceFeedback](https://shopify.dev/docs/api/admin-graphql/latest/objects/ResourceFeedback) and banner components. Include a [help footer](https://polaris.shopify.com/components/navigation/footer-help) on every page linking to your support resources. For sales attribution, use a storefront access token. See [App Store requirement 5.7](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements#sales-channel).

#### 14. Purchase option apps

Ensure your customer flow works properly on desktop and mobile across [all supported browsers](https://shopify.dev/docs/storefronts/themes/store/requirements). Automate theme modifications and support [multi-currency](https://shopify.dev/docs/api/admin-rest/latest/resources/transaction) with correct currency and price rounding rules. Assign the correct purchase option category for each selling plan. Display pricing clearly and show when customers will be charged. Use standalone widgets following the subscription UX guidelines and deferred purchase option UX guidelines. In cart pages, display the selling plan name—but check if the theme already includes it first. Provide a [customer portal](https://shopify.dev/docs/apps/build/purchase-options/customer-portal) accessible from the order status page and post-purchase emails; it should display all subscriptions with details (products, delivery frequency, price, schedule) and let customers cancel subscriptions or modify payment methods. Use [app extensions](https://shopify.dev/docs/apps/build/purchase-options/product-subscription-app-extensions) on product pages in the Shopify admin, and ensure changes sync between the admin and your app. See [App Store requirement 5.4](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements#purchase-option).

#### 15. Donation distribution apps

Use the [Billing API](https://shopify.dev/docs/apps/launch/billing/support-one-time-purchases) or a PCI-compliant gateway for donations. Provide proof of charitable status in your UI and show merchants proof that funds reach registered charities (not tax receipts). Collect customer donations only through Shopify checkout using [Theme App Extensions](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions) or [Checkout UI Extensions](https://shopify.dev/docs/api/checkout-ui-extensions), and include instructions for hiding add-to-cart buttons on donation products. Clearly indicate operating costs in your UI and listing. See [App Store requirement 5.10](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements#donation).

#### 16. Payments apps

Your payments app should meet the [minimum product requirements](https://shopify.dev/docs/apps/build/payments/requirements) and use only the [Payments Apps API](https://shopify.dev/docs/api/payments-apps). Submit screencasts for all [supported browsers](https://help.shopify.com/en/manual/shopify-admin/supported-browsers) showing your payment flow. Allow buyers to cancel payments and redirect properly between checkout, your payment flow, and the order confirmation page. Present identical payment information to what's shown at checkout, and don't upsell products in the payment flow. Name your payments app using your legal business name without marketing text. If using [checkout UI extensions](https://shopify.dev/docs/apps/build/payments/credit-card/with-extensibility), avoid banners, logos, or graphics as decorative elements, and use only permitted targets. Provide a test store, credentials, payment/refund instructions, and descriptions of specific scenarios (installments, 3D Secure). Cryptocurrency payments apps must be accepted into the blockchain app program. See [App Store requirement 5.2](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements#payment).

#### 17. Post Purchase apps

Redirect customers to the order confirmation page after they respond to post-purchase requests. Limit consecutive requests to 3 and ensure customers can accept or decline offers. Make upsell offers transparent with accurate pricing that dynamically updates when customers adjust quantity or variants. Display the same product price as in the merchant's store, and for limited-time offer details, clearly disclose them. Don't display order tracking, status functionality, or third-party promotions. See [App Store requirement 5.8](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements#post-purchase).

#### 18. Checkout apps

**Note:** Checkout apps and extensions have [design requirements](https://shopify.dev/docs/apps/launch/app-requirements-checklist#design-requirements-for-checkout-apps) that apply to custom apps as well as public apps.

Use only [documented APIs](https://shopify.dev/docs/api/checkout-ui-extensions/latest/targets) for customizing checkout. Don't request payment information, add countdown timers, or collect information already captured by standard checkout fields. For network access, keep response times under one second and render [skeleton components](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components) initially to avoid blocking checkout. Extensions should be feature-complete, provide novel functionality, and avoid self-promotion.

**Design guidelines** — All apps that extend Shopify checkout (both public and custom) should follow these design guidelines, ensuring buyers receive the lowest checkout total by default, that all additional charges are clearly disclosed, and buyers give explicit consent to any optional charges. Avoid deceptive "dark patterns."

- **Optional charges must be off by default** — If your app adds optional charges to the storefront or checkout, those charges should be turned off by default. Buyers must be able to clearly see the optional charge and actively choose to opt in (e.g. by checking a box). Automatically adding an optional item, disguising a charge as a "gift," or forcing buyers to opt out is unacceptable.
- **Optional charges must be clearly disclosed and itemized** — Itemize charges so buyers can clearly see them on the storefront, in the cart, and at checkout. Simply showing a higher total is not enough disclosure.
- **Shipping must default to the lowest-priced option** — When multiple shipping options are available at different prices, the cheapest option must be selected by default.

See [App Store requirement 5.6](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements#checkout-customization).

#### 19. Blockchain apps

Ensure no personal data is written or stored on-chain. Support only primary NFT sales on Shopify—secondary sales should occur on third-party platforms. Don't facilitate NFTs that could be classified as securities or have transferrable royalties.

**Caution:** Royalties should never be dispersed to buyers or recipients of NFTs.

NFT distribution apps should identify NFT variants by [populating product metafields](https://shopify.dev/docs/apps/build/blockchain/nft-distribution#nft-distribution-product-metafields-requirements) and write blockchain transaction IDs to fulfillment tracking fields. Provide wallet acquisition options for customers and ensure they can receive full self-custody without post-purchase fees (unless using permissioned blockchains—disclose this before purchase). Block NFT features while Shopify Payments is active until shops are approved using the [NFT Sales Eligibility API](https://shopify.dev/docs/apps/build/blockchain/nft-distribution/check-nft-sales-eligibility). Tokengating apps should identify gated orders using order metafields and gated products using product metafields. See [App Store requirement 5.11](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements#blockchain).

### Next steps

- [Review the App Store requirements](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements) - Review the App Store requirements before submitting your app for review.
- [Prepare your app before submitting](https://shopify.dev/docs/apps/launch/app-store-review/pass-app-review) - Learn our recommended best practices for preparing and testing your app before submitting it for review.

---

## Built for Shopify Requirements

> Fonte: https://shopify.dev/docs/apps/launch/built-for-shopify/requirements

To qualify for Built for Shopify status, your app must meet the requirements listed below. Each requirement in this list helps your app meet quality standards. Some requirements apply to all apps, while others apply to specific categories.

Along the way, you'll qualify for smaller achievements that grant unique benefits. For details about the benefits of each achievement, refer to the [Built for Shopify overview](https://shopify.dev/docs/apps/launch/built-for-shopify#other-achievements).

**Changelog:** For details about changes to the Built for Shopify requirements, refer to the [Built for Shopify changelog](https://shopify.dev/changelog?filter=built_for_shopify).

### 1. Prerequisites

Some prerequisites are automatically evaluated while others require manual validation. Visit your app's **Distribution** page in your [Partner Dashboard](https://www.shopify.com/partners) for a comprehensive breakdown.

#### 1.1 General

**1.1.1 Meet App Store requirements** — The app needs to continue to meet the [requirements for distributing apps on the Shopify App Store](https://shopify.dev/docs/apps/launch/app-requirements-checklist). Your app will be audited for these requirements when you apply for Built for Shopify status.

**1.1.2 Have a good Partner standing** — The app needs to comply with the [Partner Program Agreement](https://www.shopify.com/partners/terms) and [Shopify API License and Terms of Use](https://www.shopify.com/legal/api-terms). Your Partner Account must have no active or outstanding infractions. Resolving an outstanding infraction is the first step in getting your account back into Good Partner standing, however, even after resolving issues, previous violations can still temporarily impact your BFS status depending on their severity and frequency. Read more about [Enforcement of Shopify's Partner Program Policies](https://help.shopify.com/en/partners/faq/removal).

#### 1.2 Merchant utility

**1.2.1 Have a minimum number of installs** — Your app must have a minimum of 50 net installs from active shops on paid plans.

**1.2.2 Have a minimum number of reviews** — Your app must have a minimum of five reviews.

**1.2.3 Have a minimum app rating** — Your app must meet a minimum recent app rating threshold in the Shopify App Store.

### 2. Performance

[Optimizing your app for performance](https://shopify.dev/docs/apps/build/performance) directly influences conversion rates, repeat business, and search engine rankings.

#### 2.1 Admin performance

Shopify uses [Web Vitals](https://web.dev/articles/vitals) to determine the performance of your app in the Shopify admin. To enable Shopify to gather Web Vitals metrics, your app needs to use the [latest version of App Bridge](https://shopify.dev/docs/api/app-bridge-library#getting-started).

When your app loads in the Shopify admin, it needs to meet Web Vitals targets for the following metrics, at the 75th percentile of page loads:

- **2.1.1 Minimize Largest Contentful Paint (LCP)** — Your app's LCP is 2.5 seconds or less. Minimum of 100 calls for LCP over the last 28 days to be assessed.
- **2.1.2 Minimize Cumulative Layout Shift (CLS)** — Your app's CLS is 0.1 or less. Minimum of 100 calls for CLS over the last 28 days to be assessed.
- **2.1.3 Minimize Interaction to Next Paint (INP)** — Your app's INP is 200 milliseconds or less. Minimum of 100 calls for INP over the last 28 days to be assessed.

#### 2.2 Storefront performance

**2.2.1 Minimize the impact on store speed** — Your app must not reduce the storefront Lighthouse performance score by more than ten points.

#### 2.3 Checkout performance

**2.3.1 Minimize the impact on checkout speed** — You need to [optimize how your app fetches and stores carrier rates](https://shopify.dev/docs/apps/build/performance/checkout) to minimize impact on checkout speed. For Shopify to assess your impact on checkout speed, your app must make a minimum of 1000 requests over the last 28 days. Your requests must have a p95 value of 500ms or less, with a 0.1% failure rate.

### 3. Integration

Design your app so that all of its primary functionality is available within the Shopify admin.

#### 3.1 Embedded apps

- **3.1.1 Embed the app in the Shopify admin** — Apps should be embedded using the latest version of [Shopify App Bridge](https://shopify.dev/docs/api/app-bridge) by adding the `app-bridge.js` script tag to the `<head>` of every document. Use [session token authentication](https://shopify.dev/docs/apps/build/authentication-authorization/session-tokens). Apps should not embed external web pages.
- **3.1.2 Keep primary app workflows within Shopify** — Merchants should be able to complete primary app workflows inside the Shopify admin without accessing an external website. Exceptions apply for apps needing a standalone site for complex features (e.g. messaging apps).
- **3.1.3 Enable seamless sign up based on Shopify credentials** — Apps should make sign up seamless, without requiring an additional login or sign-up. Exceptions apply for apps requiring complex business-to-business sign-up; in those cases onboarding must first ask merchants to connect their store to existing credentials.
- **3.1.4 Include simplified monitoring or reporting** — Expose key metrics on the app's home page. If monitoring/reports can only exist externally, include a simplified version in the Shopify admin.
- **3.1.5 Keep third-party connection settings within Shopify** — Any settings/configurations controlling the connection between Shopify and a third-party system must be available inside the Shopify embedded app interface (e.g. connect/disconnect a social media account).

#### 3.2 Installation and asset management

- **3.2.1 Provide a clean uninstallation process** — Use [theme app extensions](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions) to build elements included in the theme. When merchants uninstall apps, associated blocks are automatically and entirely removed from online store themes.
- **3.2.2 Doesn't use the Asset API to create, modify, or delete files** — Your app shouldn't add, remove, or edit a merchant's theme files. Exceptions: (1) page builder apps that add or replace all layout/template files; (2) apps that back up all theme files and restore from backup; (3) apps primarily providing SEO, content locking, or developer tooling (these can still use the Asset API to read theme files). Audited when you apply for BFS status.

### 4. Design

Your app should be designed to feel familiar, helpful, and user-friendly.

#### 4.1 Familiar

Your app generally looks and behaves like the Shopify admin, leveraging Shopify [App Bridge](https://shopify.dev/docs/api/app-bridge) where appropriate.

**4.1.1 Follow UX best practices.** Reasons for rejection: (1) UI is generally buggy/unpolished (content flickers, repeatedly loads in/out, excessive shifting); (2) most content does not reside in card-like containers similar to Shopify admin cards; (3) button styles don't match the Shopify admin (e.g. primary buttons green or purple); (4) serif/script font for the majority of content; (5) body text size significantly different from the admin; (6) background color significantly different (e.g. black); (7) interacting with tabs modifies content above the tabs; (8) in a group/list, some items feature icons while others don't; (9) layout spacing significantly different from the admin; (10) text doesn't meet basic [WCAG 2.1 AA](https://www.w3.org/WAI/WCAG21/quickref/?showtechniques=141#contrast-minimum) contrast; (11) a sub-page does not offer a back button to the parent page.

**4.1.2 Mobile-friendly.** Reasons for rejection: (1) an entire page requires horizontal scrolling on mobile; (2) some content is entirely inaccessible on mobile (collapsed with no way to expand, or no horizontal scroll mechanism); (3) content appears unreasonably condensed (e.g. a two-column desktop layout remains two columns on mobile instead of stacking).

**4.1.3 Concise app name.** Reason for rejection: on desktop, when pinned, the app name is truncated with ellipsis in the Shopify navigation menu.

**4.1.4 Use the nav menu.** Use the App Bridge [s-app-nav](https://shopify.dev/docs/api/app-home/app-bridge-web-components/s-app-nav). Reasons for rejection: (1) an app has its own navigation menu instead of the Shopify admin one; (2) navigating to a sub-page fails to highlight the relevant parent nav item; (3) a separate nav item in addition to the app name redirects to the homepage (the app name should point at the homepage); (4) an app renders emojis in the nav menu.

**4.1.5 Use the contextual save bar.** Form inputs should generally be saved using the App Bridge [Contextual Save Bar](https://shopify.dev/docs/api/app-home/apis/save-bar) (CSB). Reasons for rejection: (1) a form doesn't integrate with the CSB when reasonable; (2) when CSB is present, a merchant can navigate away without first interacting with Save/Discard.

**4.1.6 Use modals appropriately.** In a [s-modal](https://shopify.dev/docs/api/app-home/polaris-web-components/overlays/modal), use the heading attribute and the primary-action/secondary-actions slots. Reasons for rejection: (1) action buttons appear outside the component slots; (2) a modal uses the deprecated Polaris Fullscreen bar component instead of `s-app-window` and `s-page`.

#### 4.2 Helpful

**4.2.1 Spelling, grammar and phrasing.** Rejection: (1) prominent spelling/grammatical errors in headings, nav items, or CTAs; (2) phrases/headings/labels/CTAs difficult to understand or lacking context.

**4.2.2 Helpful onboarding.** Rejection: (1) onboarding doesn't sufficiently guide merchants to completion; (2) onboarding not concise; (3) onboarding difficult to locate; (4) implying installing an additional app is a required step; (5) asking for merchant info without justification; (6) no mechanism to remove onboarding UI after completion.

**4.2.3 Helpful homepage.** Rejection: (1) app has an app block/embed to activate but fails to communicate status via [app.extensions()](https://shopify.dev/docs/api/app-home/apis/app#extensions); (2) no metrics/analytics on the homepage when obvious ones would help; (3) after dismissing dismissible elements, homepage only contains static content.

**4.2.4 Helpful error messages.** Errors should be red, guide to solutions, and appear next to relevant fields. Rejection: (1) error auto-disappears after a set time (e.g. toast); (2) error in a color other than red; (3) a field highlighted red without a corresponding message; (4) a contextual error not displayed contextually; (5) form fields display an error prior to any merchant interaction.

**4.2.5 Guide merchants to logical actions.** Rejection: (1) in a button group, all buttons have the same visual treatment; (2) the most visually prominent button doesn't represent the most logical next action.

**4.2.6 Visible previews.** Rejection: (1) app allows visual customization but fails to provide a live preview; (2) on desktop, a merchant can't simultaneously view editor controls and the preview.

#### 4.3 User-friendly

Your app shouldn't implement [dark patterns](https://en.wikipedia.org/wiki/Dark_pattern).

**4.3.1 Don't make false claims.** Rejection: (1) language stating a merchant outcome (e.g. "increase your sales by 18%"); (2) promoting another app with an average rating that differs significantly from its actual App Store rating.

**4.3.2 Don't pressure merchants.** Rejection: (1) animated countdown timer on a free trial encouraging upgrade; (2) CTAs that could induce guilt/shame (e.g. "No thanks, I prefer less sales").

**4.3.3 Don't distract merchants.** Rejection: (1) a modal/popover auto-appears on page load/after a delay/from an unrelated action; (2) a large element animates into view on load/after delay/from unrelated action; (3) animation used to draw attention unrelated to a merchant action; (4) red used for a purpose unrelated to errors or destructive actions.

**4.3.4 Don't overwhelm merchants.** Rejection: (1) a single large complex form instead of logically grouped fields; (2) two or more banners in close proximity; (3) large amounts of text instead of concise, scannable copy.

**4.3.5 Don't impersonate Shopify.** Rejection: (1) an icon that could be mistaken for a first-party Shopify app icon; (2) using the [Shopify Sidekick icon](https://www.shopify.com/ca/magic) and/or a color similar to [Shopify's magic purple](https://polaris.shopify.com/tokens/color#color-bg-fill-magic) for an AI feature.

**4.3.6 Dismissible ads.** Rejection: (1) promotional content not dismissible; (2) dismissed content later reappears.

**4.3.7 Label and disable premium features.** Plan-gated features must be disabled (visually and functionally) and clearly indicated; Shopify Plus-exclusive features must be hidden for non-Plus merchants. Rejection: (1) a plan-gated feature appears interactive/enabled and only later reveals it requires a more expensive plan; (2) a plan-gated feature is interactive but appears disabled; (3) a plan-gated feature is non-interactive but appears enabled; (4) a Plus-exclusive feature visible to non-Plus merchants; (5) when offering multiple tiers, it's not obvious which tier unlocks a feature.

### 5. Category-specific

If your app belongs to one of the categories below, it must meet all of the criteria listed for that category.

**5.1 Ads apps** — 5.1.1 Use [Web Pixel extensions](https://shopify.dev/docs/apps/build/marketing-analytics/build-web-pixels) for ads (no script tags / no merchant-pasted JS) for ad attribution, audience creation, segmentation, analytics, pixels, retargeting, or lookalike targeting. 5.1.2 Use Shopify segments — allow merchants to use any segment defined in the Shopify admin and provide a [customer segment action extension](https://shopify.dev/docs/apps/build/marketing-analytics/customer-segments/build-an-action-extension).

**5.2 Affiliate program apps** — 5.2.1 Use Web Pixel extensions (no script tags / no merchant-pasted JS).

**5.3 Analytics apps** — 5.3.1 Use Web Pixel extensions (no script tags / no merchant-pasted JS).

**5.4 Carrier services apps** — 5.4.1 Respond to rate requests in under 500ms for 95% of calls over the last 28 days. 5.4.2 Successfully respond to 99.9% of requests over the last 28 days. (Minimum 1000 requests in the last 28 days to assess.)

**5.5 Discount apps** — 5.5.1 Use [discount functions](https://shopify.dev/docs/apps/build/discounts#build-with-shopify-functions) or native [discount APIs](https://shopify.dev/docs/apps/build/discounts#build-with-the-graphql-admin-api). 5.5.2 Don't use draft orders with custom discounts. 5.5.3 Use [`discountRedeemCodeBulkAdd`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountRedeemCodeBulkAdd) for multiple redeem codes. 5.5.4 Create high-quality links from the Create discount button to a page in your embedded app following the [App Design Guidelines](https://shopify.dev/docs/apps/design).

**5.6 Email marketing apps** — 5.6.1 Use Web Pixel extensions. 5.6.2 Sync customer data to/from Shopify. 5.6.3 Use Shopify segments + customer segment action extension. 5.6.4 Use the [visitors API](https://shopify.dev/docs/api/web-pixels-api/emitting-data#visitor-api) to log identifying info for customers who provide it on the Online Store.

**5.7 Forms apps** — 5.7.1 Use Shopify segments + customer segment action extension. 5.7.2 Use the visitors API. 5.7.3 Sync customer data.

**5.8 Fulfillment services apps** — 5.8.1 Actively fulfill orders (100+ fulfillment orders in the last 28 days). 5.8.2 Complete 99% of assigned fulfillment orders in the last 28 days (new orders from the last 7 days excluded; incomplete states listed: `open/submitted`, `in_progress/accepted`, `in_progress/rejected`, `in_progress/cancellation_rejected`, `in_progress/cancellation_requested`). 5.8.3 Respond successfully to 99% of Shopify callback requests. 5.8.4 Only fulfill after a merchant requests fulfillment. 5.8.5 Add tracking info to 80% of fulfillments within one hour. 5.8.6 Respond to 99% of fulfillment requests within four hours (accept/reject). 5.8.7 Respond to 99% of cancellation requests within one hour (accept/reject).

**5.9 Invoices and receipts apps** — 5.9.1 Use an [admin print action extension](https://shopify.dev/docs/apps/build/admin/actions-blocks) to print invoices/packing slips from the order detail page and the orders index page.

**5.10 Product bundles apps** — 5.10.1 Use bundles primitives: GraphQL Admin API for [static bundles](https://shopify.dev/docs/apps/build/product-merchandising/bundles/add-fixed-bundle) or a `cartTransform` function for [customized bundles](https://shopify.dev/docs/apps/build/product-merchandising/bundles/add-customized-bundle). Other methods allowed for unsupported use cases (unsupported sales channels, subscriptions, post-purchase order edits).

**5.11 Product reviews apps** — 5.11.1 Provide a [Flow trigger](https://shopify.dev/docs/apps/build/flow/triggers/create) when a new review is collected. 5.11.2 Provide an [admin block extension](https://shopify.dev/docs/apps/build/admin/actions-blocks#admin-blocks) on customer detail pages.

**5.12 Returns and exchanges apps** — 5.12.1 Sync all return lifecycle events (creating returns, shipping creation, restocking, removing items, cancelling, closing, refunds). 5.12.2 Include [exchange line items](https://shopify.dev/docs/api/admin-graphql/latest/input-objects/ExchangeLineItemInput) (and remove when no longer needed). 5.12.3 Include shipping and restocking fees when applicable.

**5.13 SMS marketing apps** — 5.13.1 Use Web Pixel extensions. 5.13.2 Sync customer data. 5.13.3 Use Shopify segments + customer segment action extension. 5.13.4 Use the visitors API.

**5.14 Subscription apps** — 5.14.1 Use subscriptions objects/APIs: [Selling plan API](https://shopify.dev/docs/api/admin-graphql/latest/objects/sellingplan), [Subscription contract API](https://shopify.dev/docs/api/admin-graphql/latest/objects/subscriptioncontract), [Customer payment method API](https://shopify.dev/docs/api/admin-graphql/latest/objects/customerpaymentmethod). 5.14.2 Add subscriptions on product detail pages using a theme [app block](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions/configuration#app-blocks-for-themes) compatible with [Online Store 2.0](https://shopify.dev/docs/storefronts/themes/os20). 5.14.3 Follow [subscriptions UX guidelines](https://shopify.dev/docs/storefronts/themes/pricing-payments/subscriptions/subscription-ux-guidelines) (selling plan name, price, and savings clearly displayed on product/cart/order detail pages; automatically match the store theme's palette/font by default). 5.14.4 Use [Customer Account UI extensions](https://shopify.dev/docs/api/customer-account-ui-extensions) for customers to view/manage subscriptions.

---

# Design / UX

Mini-indice della sezione:

- [App Design Guidelines](#app-design-guidelines)
- [App structure (design)](#app-structure-design)
- [Apps in admin (Polaris & admin UI extensions)](#apps-in-admin-polaris--admin-ui-extensions)

---

## App Design Guidelines

> Fonte: https://shopify.dev/docs/apps/design

Shopify's App Design Guidelines show you what great Shopify apps look like and how they're crafted. These guidelines remove the guesswork, so you can build apps that are predictable and easy to use.

### Why you should use these guidelines

We base our design guidelines on some basic principles, which we communicate through clear directives. Following these directives helps provide a better app experience for merchants.

**Built for Shopify** — Following these guidelines should help your app meet the Built for Shopify design requirements. Achieving Built for Shopify status gives your app preferential treatment in the Shopify App Store and signals to merchants that you meet our standards for quality and trust.

**Adaptive** — With the majority of online store traffic happening on mobile, designing for mobile devices should be at the forefront of the app building process.

**A better merchant experience** — Merchants expect a predictable user experience that works like the rest of the Shopify admin. Prioritize merchant needs and context ahead of trying to make your app unique just for the sake of being different.

**Accessible** — To provide a great experience for all Shopify merchants and their customers, apps should be built using accessibility best practices.

### Apps and the Shopify admin

Apps are a crucial part of the Shopify ecosystem. They enable merchants to add functionality to their stores without leaving the familiar environment of the Shopify admin.

Using Shopify App Bridge, you can create apps directly inside the Shopify admin. A single frontend that's written with Shopify App Bridge can power point-of-sale, desktop, and mobile experiences. Apps built with Shopify App Bridge are more performant, flexible, and have more features.

By building with Shopify App Bridge and following these App Design Guidelines, you'll create a streamlined experience with the rest of the Shopify admin.

### Best practices

The best apps provide merchants with a user experience that matches the appearance and behaviors of the Shopify host surface. This consistency builds merchant trust, because merchant workflows often cross between apps and native pages of the Shopify admin.

For apps embedded into the Shopify admin, we recommend using the components and best practices of Polaris, Shopify's unified system for building app interfaces.

We're constantly innovating and evolving the Shopify admin. By using Polaris, your app can evolve with us.

Your app's UI should demonstrate a good faith effort to leverage common UX best practices and meet a high bar for design quality.

---

## App structure (design)

> Fonte: https://shopify.dev/docs/apps/design/app-structure

Apps are structured to work seamlessly with the Shopify admin and to provide an intuitive experience for merchants.

### Anatomy

1. The Shopify admin
2. App nav
3. App header
4. Page header
5. Overflow menu
6. App body

Apps consist of a few navigation elements and the app body, which is the center of your app's experience.

App navigation is strictly configured, and it's an important part of providing a great merchant experience. For more details, refer to the [navigation guidelines](https://shopify.dev/apps/design-guidelines/navigation).

### App body

The app body is where your app's main experience lives.

Be sure to follow the [layout guidelines](https://shopify.dev/apps/design-guidelines/layout) when you choose a layout for the app body.

### App window

[App window](https://shopify.dev/docs/api/app-home/app-bridge-web-components/app-window) is a focused environment for specific immersive tasks.

The app window utilizes the following areas of the app interface:

1. **App window header**: The app window can contain a top bar element to render a primary and a secondary action.
2. **App body**: The app window body is where you can add all the content for a full-screen experience.

#### When to use app window

Use app window when merchants need to complete a focused task, where leveraging the full viewport improves the user experience.

The following are some example use cases:

- Complex editing experiences, such as an editor for creating newsletter content
- Immersive experiences, such as an editor for cropping and modifying images
- Previews, such as an app that adds elements to a product page and enables merchants to preview changes

#### Behavior

App window launches only after merchants interact with a button that indicates the entire canvas will be used.

Primary navigation for the app should be shown in the top bar of the app window and the primary actions should not be duplicated.

If there are unsaved changes, prompt merchants to save before exiting full-screen mode.

Avoid unnecessarily interrupting a merchant's workflow when exiting app window.

Your app should not launch full-screen or the app window from the app nav. Instead, they should launch from the app body. This is an app store requirement.

Avoid using the [FullscreenBar](https://polaris.shopify.com/components/deprecated/fullscreen-bar) within an app window, as it results in redundant mechanisms to dismiss the app window.

### Admin UI extensions

Use admin UI extensions to integrate more deeply with the Shopify admin and create seamless merchant workflows.

Choose from the following extensions:

1. `Admin block`
2. `Admin action`
3. `Admin link`
4. `Bulk action`

[Additional admin extensions](https://shopify.dev/docs/apps/structure/app-extensions/list) are available for more specific use cases.

The extension can't be used to display promotions or advertisements. This includes promoting your app, related apps, or requesting app reviews. This is an app store requirement.

#### App attribution

Shopify will badge all admin UI extensions with the app icon, name, and a link to your app URL.

The app attribution component displays your app's logo and extension name as it displays in the Shopify App Store.

#### When to use admin blocks

Use admin block extensions to offer your app's functionality or data in the context of a resource detail page. Merchants have the option to add your app block to a page, and arrange it in the page layout.

App blocks can be embedded into Product, Order, or Customer detail pages using these [targets](https://shopify.dev/docs/api/admin-extensions/latest/targets).

[Learn more about admin blocks](https://shopify.dev/docs/apps/admin/admin-actions-and-blocks#admin-blocks).

Contents should be less than 600px in height, to avoid overly tall app blocks. If necessary, implement pagination to ensure that this requirement is met.

Input fields should be visible at all times. If necessary, app blocks should trigger app actions to ensure that this requirement is met.

Your block should have an empty state that informs merchants about what your app block does. For example, it should tell merchants what data will display in the block.

Inputs in your block can work with the contextual save bar by using the [form](https://shopify.dev/docs/api/admin-extensions/latest/web-components/forms/form) component, which provides merchants with a familiar save and validation experience.

#### When to use admin actions

Use admin action extensions to offer merchants quick access to common actions that they might do with your app. Because apps can add an unlimited number of admin actions, use discrete actions for discrete purposes.

App actions can be targeted to these [targets](https://shopify.dev/docs/api/admin-extensions/latest/targets).

[Learn more about admin actions](https://shopify.dev/docs/apps/admin/admin-actions-and-blocks#admin-actions).

Apps can have multiple admin action extensions, which display in the More actions menus.

Avoid action content that exceeds 1200px and avoid using more than two steps of pagination. Otherwise, your app can be difficult to navigate.

#### When to use admin links and bulk actions

If your content doesn't fit well within the format of the block or action, then use an admin link or bulk action instead. If an interaction is complex, such as one that requires more screen space, then routing merchants into your app is a better experience.

Examples include a multi-step process, a very long form with multiple dynamic sections, or a complex editor with several columns.

Admin links show up in the More actions menus.

Bulk actions show up in the More actions menu of bulk actions controls.

#### Combining extensions

Use app actions and blocks together to provide a more focused merchant experience.

An admin block can trigger an admin action. For more information, refer to the extension [custom protocol](https://shopify.dev/docs/api/admin-extensions#custom-protocols-extension).

Avoid duplicating the content of your admin blocks and admin actions. Differentiating the functionality and value of your blocks and actions helps merchants understand which extensions to use and when.

---

## Apps in admin (Polaris & admin UI extensions)

> Fonte: https://shopify.dev/docs/apps/tools/polaris

Your app can extend the Shopify admin beyond [App Home](https://shopify.dev/docs/apps/build/app-home) by adding functionality directly to resource pages like **Products**, **Customers**, and **Orders**. You can embed transactional workflows, display contextual information, launch native Shopify editors, and link to your app's pages.

There are two primary ways to extend the admin:

- **Admin UI extensions** add custom actions, blocks, and print functionality to resource pages.
- **Admin intents** launch Shopify's native resource editors directly from your app.

**Note:** [Admin link extensions](https://shopify.dev/docs/apps/build/admin/admin-links) are also available but are recommended only when you need to navigate merchants to a page in your app. In most cases, admin UI extensions are a better choice.

### Admin UI extensions

Admin UI extensions let you embed your app's functionality on core admin pages. They automatically match the Shopify admin's look and feel, so merchants can interact with your app without navigating away from their current task.

Each UI extension is made up of three parts:

- **[Targets](https://shopify.dev/docs/api/admin-extensions/latest/targets)** define where your extension appears in the admin, such as a product details page or an order index table.
- **[Target APIs](https://shopify.dev/docs/api/admin-extensions/latest/target-apis)** provide data and methods specific to each target, like the current resource or the ability to close a modal.
- **[Web components](https://shopify.dev/docs/api/admin-extensions/latest/web-components)** are the UI building blocks you use to render your extension's interface.

#### Admin actions

Admin actions display as modals that merchants launch from the **More actions** menu on resource pages, or from an index table's bulk action menu when one or more resources are selected. Use them for transactional workflows like creating, editing, or resolving records.

#### Admin blocks

Admin blocks display as cards inline with existing resource information on admin pages. Merchants add and pin blocks to their pages. Use them to persistently display contextual information or let merchants edit data. You can also launch admin actions directly from blocks.

#### Admin print actions

Admin print actions appear under the **Print** menu on orders and product pages. They include special APIs for previewing and printing documents like invoices and packing slips.

### Admin intents

[Admin intents](https://shopify.dev/docs/apps/build/admin/admin-intents) let you launch Shopify's native resource editors directly from your app. With a single API call, you can open the same editors merchants already use to create and edit products, collections, and other resources. When merchants complete their action, they return directly to your app.

```js
shopify.intents.invoke('create:shopify/Collection');
```

Admin intents work in [App Home](https://shopify.dev/docs/api/app-home/apis/user-interface-and-interactions/intents-api), [admin UI extensions](https://shopify.dev/docs/api/admin-extensions/2026-01/target-apis/utility-apis/intents-api), and [App Home UI extensions](https://shopify.dev/docs/api/app-home-ui-extension/2026-07-rc/target-apis/utility-apis/intents-api).

### Build for admin

The following guides walk through common use cases for admin UI extensions. For the full reference, see [admin UI extensions](https://shopify.dev/docs/api/admin-extensions).

**Extension types**

- [Build an admin action](https://shopify.dev/docs/apps/build/admin/actions-blocks/build-admin-action) — Create a modal workflow that merchants launch from a resource page's **More actions** menu.
- [Build an admin block](https://shopify.dev/docs/apps/build/admin/actions-blocks/build-admin-block) — Display persistent contextual information or editable data inline on resource pages.
- [Build an admin print action](https://shopify.dev/docs/apps/build/admin/actions-blocks/build-admin-print-action) — Add printable documents like invoices or packing slips to the **Print** menu on orders and product pages.

**Discounts** — Add configuration UIs that let merchants set up custom discount types. See all [discounts guides](https://shopify.dev/docs/apps/build/discounts).

- [Build a UI extension for discounts](https://shopify.dev/docs/apps/build/discounts/build-ui-extension)
- [Build a discounts UI with React Router](https://shopify.dev/docs/apps/build/discounts/build-ui-with-react-router)

**Bundles** — Let merchants configure product bundles from within the admin. See all [product bundles guides](https://shopify.dev/docs/apps/build/product-merchandising/bundles).

- [Add a merchant configuration UI](https://shopify.dev/docs/apps/build/product-merchandising/bundles/product-configuration-extension/add-merchant-config-ui)

**Purchase options** — Let merchants create and manage selling plans for subscriptions and deferred purchases. See all [purchase options guides](https://shopify.dev/docs/apps/build/purchase-options).

- [Build a purchase options extension](https://shopify.dev/docs/apps/build/purchase-options/purchase-options-extensions/start-building)
- [Build a product subscription extension](https://shopify.dev/docs/apps/build/purchase-options/product-subscription-app-extensions/start-building)

**Orders and fulfillment** — Automate inventory, order routing, fulfillment, and returns workflows. See all [orders and fulfillment guides](https://shopify.dev/docs/apps/build/orders-fulfillment).

- [Inventory management apps](https://shopify.dev/docs/apps/build/orders-fulfillment/inventory-management-apps)
- [Order management apps](https://shopify.dev/docs/apps/build/orders-fulfillment/order-management-apps)
- [Order routing apps](https://shopify.dev/docs/apps/build/orders-fulfillment/order-routing-apps)
- [Returns apps](https://shopify.dev/docs/apps/build/orders-fulfillment/returns-apps)

**Marketing and analytics** — Help merchants segment customers and run marketing automations from the admin. See all [marketing and analytics guides](https://shopify.dev/docs/apps/build/marketing-analytics).

- [Build a customer segment action extension](https://shopify.dev/docs/apps/build/marketing-analytics/customer-segments/build-an-action-extension)

### Next steps

- [Build an admin action](https://shopify.dev/docs/apps/build/admin/actions-blocks/build-admin-action) to extend a resource page.
- Explore the [admin UI extensions reference](https://shopify.dev/docs/api/admin-extensions) for available targets, target APIs, and web components.

---

# Compliance & data protection

Mini-indice della sezione:

- [Privacy law compliance (mandatory compliance/GDPR webhooks)](#privacy-law-compliance-mandatory-compliancegdpr-webhooks)
- [Work with protected customer data](#work-with-protected-customer-data)
- [Privacy requirements](#privacy-requirements)

---

## Privacy law compliance (mandatory compliance/GDPR webhooks)

> Fonte: https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance

Data privacy rules and regulations, such as the General Data Protection Regulation (GDPR) and California Privacy Rights Act (CPRA), set requirements for parties that collect, store, or process personal data of individuals. However, Shopify takes a standardized approach and requires public apps to provide the same privacy rights for all personal data, regardless of where an individual is located.

### Mandatory compliance webhooks

Mandatory compliance webhooks are callback methods that Shopify requires for apps listed on the Shopify App Store. Shopify requires mandatory compliance webhooks as a way to manage the personal data that an app collects.

Any app that you distribute through the Shopify App Store must respond to data subject requests, regardless of whether the app collects personal data. Shopify provides mandatory compliance webhooks to help.

**Related resources:**

- [Webhooks](https://shopify.dev/docs/apps/build/webhooks)
- [Checklist of requirements](https://shopify.dev/docs/apps/launch/app-requirements-checklist)

#### How it works

You must ensure that your app is subscribed to and verifies all mandatory compliance webhooks before you submit your app to be reviewed by Shopify.

Apps must meet the following webhook requirements:

- The app must implement the mandatory compliance webhooks.
- The app must handle `POST` requests with a JSON body and `Content-Type` header set to `application/json` sent to mandatory compliance webhooks.
- If a mandatory compliance webhook sends a request with an invalid Shopify `HMAC` header, then the app must return a `401 Unauthorized` HTTP status. Learn more about [Verifying webhook deliveries](https://shopify.dev/docs/apps/build/webhooks/verify-deliveries#hmac-verification).

If you don't provide URLs for the mandatory compliance webhooks, or your app doesn't respond to these webhooks as required, then your app will be rejected and you'll need to fix the identified problem before submitting your app for another review.

**Caution:** This page isn't intended to provide you with legal advice. It sets out Shopify's privacy requirements for app developers and items that you need to consider if you're handling personal data.

#### Compliance webhook topics

Every app that's distributed through the Shopify App Store must subscribe to the following compliance webhook topics:

| Topic | Event |
| - | - |
| `customers/data_request` | Requests to view stored customer data |
| `customers/redact` | Requests to delete customer data |
| `shop/redact` | Requests to delete shop data |

#### Subscribe to compliance webhooks

You must subscribe to compliance webhooks before publishing your app. To subscribe to compliance webhooks, you need to register endpoints and then configure them in your app config TOML.

1. Register an endpoint for each compliance webhook. For HTTPS urls, this will require a valid SSL certificate that can correctly process webhook event notifications. For more information, refer to [register an endpoint](https://shopify.dev/docs/apps/build/webhooks/verify-deliveries#https-delivery-considerations) for HTTPS, [set up an event source](https://shopify.dev/docs/apps/build/webhooks/get-started) for AWS EventBridge, or [retrieve your Shopify service account address](https://shopify.dev/docs/apps/build/webhooks/get-started) for Google Pub/Sub.

2. You can subscribe to the compliance webhook topics by making the following changes to your app's `shopify.app.toml` file in the app's root folder. Learn more about [configuring your app with the TOML file](https://shopify.dev/docs/apps/build/cli-for-apps/app-configuration).

```toml
[webhooks]
api_version = "2024-07"

[[webhooks.subscriptions]]
compliance_topics = ["customers/data_request", "customers/redact", "shop/redact"]
uri = "https://app.example.com/webhooks"
```

**Info:** The following is the structure of the URL you should use for the URI when working with **Google Cloud Pub/Sub**: `pubsub://{project-id}:{topic-id}` — where `{project-id}` is the ID of your Google Cloud Platform project, and `{topic-id}` is the ID of the topic that you set up in Google Cloud Pub/Sub. For **Amazon EventBridge**, your URL will be similar to the following example: `arn:aws:events:<aws_region>::event-source/aws.partner/shopify.com/<app_id>/<event_source_name>`

#### Respond to compliance webhooks

When you receive one of the compliance webhooks, you need to take the following actions:

- Confirm that you've received the request by responding with a `200` series status code.
- Complete the action within 30 days of receiving the request. However, if you're unable to comply with a redaction request because you're legally required to retain data, then you shouldn't complete the action. Learn more about how to [receive and respond](https://shopify.dev/docs/apps/build/webhooks/subscribe) to webhooks.

### customers/data_request

Customers can request their data from a store owner. When this happens, Shopify sends a payload on the `customers/data_request` topic to the apps that are installed on that store.

If your app has been granted access to customer or order data, then it will receive a data request webhook. The webhook contains the resource IDs of the customer data that you need to provide to the store owner directly. In some cases, a customer record contains only the customer's email address.

**`customers/data_request` payload**

```json
{
  "shop_id": 954889,
  "shop_domain": "{shop}.myshopify.com",
  "orders_requested": [299938, 280263, 220458],
  "customer": {
    "id": 191167,
    "email": "john@example.com",
    "phone":  "555-625-1199"
  },
  "data_request": {
    "id": 9999
  }
}
```

### customers/redact

Store owners can request that data is deleted on behalf of a customer. When this happens, Shopify sends a payload on the `customers/redact` topic to the apps installed on that store.

If your app has been granted access to the store's customer or order data, then it will receive a redaction request webhook with the resource IDs that you need to redact or delete. In some cases, a customer record contains only the customer's email address.

If a customer hasn't placed an order in the past six months, then Shopify sends the payload 10 days after the deletion request. Otherwise, the request is withheld until six months have passed.

**`customers/redact` payload**

```json
{
  "shop_id": 954889,
  "shop_domain": "{shop}.myshopify.com",
  "customer": {
    "id": 191167,
    "email": "john@example.com",
    "phone": "555-625-1199"
  },
  "orders_to_redact": [299938, 280263, 220458]
}
```

### shop/redact

48 hours after a store owner uninstalls your app, Shopify sends a payload on the `shop/redact` topic. This webhook provides the store's `shop_id` and `shop_domain` so that you can erase data for that store from your database.

**`shop/redact` payload**

```json
{
  "shop_id": 954889,
  "shop_domain": "{shop}.myshopify.com"
}
```

### Next steps

- Test your configuration by manually triggering a webhook delivery using the Shopify CLI [`webhook trigger`](https://shopify.dev/docs/api/shopify-cli/app/app-webhook-trigger) command. Manually triggering webhooks doesn't test your webhook subscriptions.
- Learn how to [manage webhooks for different API versions](https://shopify.dev/docs/apps/build/webhooks/subscribe#versioning).
- Learn about the available topics for [REST Admin API webhooks](https://shopify.dev/docs/api/admin-rest/latest/resources/webhook).
- Learn about the available topics for [GraphQL Admin API webhooks](https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic).
- Familiarize yourself with [data privacy concepts](https://shopify.dev/docs/apps/launch/privacy-requirements) for apps including privacy policies, data rights, and consent for marketing services.

---

## Work with protected customer data

> Fonte: https://shopify.dev/docs/apps/launch/protected-customer-data

Privacy and data protection are critical foundations for ecommerce and are important to merchants and their customers. The protected customer data requirements focus on data minimization, transparency, and security so that you can better support a merchant's path towards compliance with privacy and data protection rules.

When your app uses the [Admin API](https://shopify.dev/docs/api/admin-graphql) or the [Customer Account API](https://shopify.dev/docs/api/customer), the review process for your public, published app might require action as described in the following table:

| Level | Data use | Partner actions |
| - | - | - |
| 0 | No customer data | No action required |
| 1 | [Customer data](#protected-customer-data-api-types-and-resources) **excluding** name, address, phone, and email fields | [Request access to protected customer data](#request-access-to-protected-customer-data) in the Partner Dashboard; Implement level 1 protected customer data requirements |
| 2 | [Customer data](#protected-customer-data-api-types-and-resources) **including** name, address, phone, or email fields | Request access to protected customer data and fields in the Partner Dashboard; Implement level 1 and level 2 protected customer data requirements; Participate in data protection reviews |

Shopify will approve your app to use protected customer data if the requested data is the minimum amount required by your app to provide the merchant with the app functionality. If you're approved to access the data that you requested, then code updates aren't required. If you aren't approved to access the data that you requested, then you might need to update your app to handle errors or redacted data. For more information, refer to the example API requests for protected customer data.

While we encourage all apps to meet protected customer data requirements, access to the different levels can vary based on app types. See below:

| Level | Public app | Custom app | Admin created custom app |
| - | - | - | - |
| 1 | Requires review | Always available | Always available |
| 2 | Requires review | Always available | [Varies by plan](https://help.shopify.com/en/manual/apps/app-types/custom-apps#custom-level2-pii-app) |

To access customer data in development, select the data and fields you're using in the Partner Dashboard. You don't need to submit a request for review for apps that are installed only on development stores.

**Important:** Partners are legally bound by the terms and conditions of the [Shopify Partner Program Agreement](https://www.shopify.com/partners/terms) and the [Shopify API License and Terms of Use](https://www.shopify.com/legal/api-terms), regardless of the API version that they're using. Protected customer data requirements aren't intended to replace the terms and conditions that you agree to as a Shopify Partner.

### Request access to protected customer data

**Note:** Before you can request access to protected customer data, including on development stores, you need to [select a distribution method](https://shopify.dev/docs/apps/launch/distribution/select-distribution-method) for your app.

Public apps request access to protected customer data and protected customer fields through the Partner Dashboard.

Protected customer data includes any data that directly relates to a customer or prospective customer, as represented in the API types and resources. Types and resources that don't refer to a single customer, such as the [product](https://shopify.dev/docs/api/admin-graphql/latest/queries/product) query, aren't included.

In addition to requesting access to protected customer data, you'll need to request access to the following protected customer fields individually because they directly identify customers:

- Name: first and last names
- Address: address line 1, address line 2, geolocation, and zip codes in both billing and shipping addresses
- Email
- Phone

If your access is approved, these fields will appear in the protected customer API types and resources.

To request access:

1. From the Partner Dashboard, go to [**Apps**](https://partners.shopify.com/current/apps), and then select your app.
2. In the sidebar, click **API access requests**.
3. Find **Protected customer data access** and click **Request access**.
4. Select **Protected customer data**, provide your reasons for using it, and click **Save**.
5. If your app needs access to protected customer fields, then select the relevant fields, provide your reasons for using them, and click **Save**.
6. Complete your **Data protection details**, making sure that your app meets the protected customer data requirements.
7. [Submit your app for review](https://shopify.dev/docs/apps/launch/app-store-review/submit-app-for-review).

If your app is for testing or installed only on a development store, you can access customer data in development after Step 5. You don't need to submit for review.

You'll receive updates about the status of your review by email and through your Partner Dashboard.

#### Protected customer data API types and resources

The [GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql) and [Customer Account API](https://shopify.dev/docs/api/customer) reference documentation defines what types, objects, and fields represent protected customer data.

The following table summarizes the API types that are considered protected customer data.

| API resource/type | Protected customer data |
| - | - |
| Customers ([GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql/latest/objects/Customer), [Customer Account API](https://shopify.dev/docs/api/customer/latest/objects/Customer)) | Data that defines facts about a single customer, including name, addresses, email, and phone number. |
| Shipping rates ([GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql/latest/objects/ShippingRate)) | Shipping rates that related to a single order, which relates to a single customer. |
| [Webhooks](https://shopify.dev/docs/api/webhooks), Metafields ([GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql/latest/objects/Metafield), [Customer Account API](https://shopify.dev/docs/api/customer/latest/objects/Metafield)) | Events and metafields that relate to a single customer or order. |
| Orders ([GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql/latest/objects/Order), [Customer Account API](https://shopify.dev/docs/api/customer/latest/objects/Order)) | Orders, draft orders, abandoned checkouts, refunds, transactions, and other data that relate to a single customer. |
| Checkout ([Storefront API](https://shopify.dev/docs/api/storefront/latest/objects/Checkout)) | Checkout and payments that relate to orders by a single customer. |
| Shipping and fulfillment ([GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql/latest/objects/FulfillmentOrder), [Customer Account API](https://shopify.dev/docs/api/customer/latest/objects/Fulfillment)) | Shipping and fulfillment data that relate to orders by a single customer. |
| Online store ([Storefront API](https://shopify.dev/docs/api/storefront/latest/objects/Comment)) | Comments on a store that contain data about the commenter. |
| Gift cards ([GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql/latest/objects/GiftCard)) | Gift cards that are used by a single customer. |

### Using protected customer data

After your app is approved to access protected customer data, API requests and webhooks that contain protected resources will return the data requested. Responses will include only approved fields, and unapproved fields will be redacted.

GraphQL requests to unapproved types will return an HTTP `200 Ok` response with an error message in the `errors` hash.

#### Example API requests for protected customer data

The following examples show API requests and responses for an app that is approved to access protected customer data and the `email` and `name` fields. In this scenario, the `phone` and `address` fields are redacted from the GraphQL replies. The reply also includes an `errors` message with an explanation of redacted fields.

**GraphQL Admin API request with approved fields** — `POST /admin/api/{api_version}/graphql.json`

```graphql
{
  customer(id: "gid://shopify/Customer/957611081784") {
    email
    firstName
    lastName
  }
}
```

```json
HTTP/1.1 200 OK
{
  "data": {
    "customer": {
      "email": "testcustomer@example.com",
      "firstName": "Sally",
      "lastName": "Testopherson"
    }
  }
}
```

**GraphQL Admin API request with unapproved fields** — `POST /admin/api/{api_version}/graphql.json`

```graphql
{
  customer(id: "gid://shopify/Customer/957611081784") {
    email
    phone
  }
}
```

```json
HTTP/1.1 200 OK
{
  "data": {
    "customer": {
      "email": "testcustomer@example.com",
      "phone": null
    }
  },
  "errors": [
    {
      "message": "This app is not approved to access the Customer object. See https://partners.shopify.com/123/apps/456/customer_data for more details.",
      "locations": ...,
      "path": [
        "customer",
        "phone"
      ]
    }
  ]
}
```

**Customer Account API request with approved fields** — `POST /customer/api/{api_version}/graphql.json`

```graphql
{
  customer {
    firstName
    lastName
    emailAddress {
      emailAddress
    }
  }
}
```

```json
HTTP/1.1 200 OK
{
  "data": {
    "customer": {
      "firstName": "Sally",
      "lastName": "Testopherson",
      "emailAddress": {
        "emailAddress": "testcustomer@example.com"
      }
    }
  }
}
```

**Customer Account API request with unapproved fields** — `POST /customer/api/unstable/graphql.json`

```graphql
{
  customer {
    firstName
    lastName
    phoneNumber {
      phoneNumber
    }
  }
}
```

```json
HTTP/1.1 200 OK
{
  "data": {
    "customer": {
      "firstName": "Sally",
      "lastName": "Testopherson",
      "phoneNumber": {
        "phoneNumber": null
      }
    }
  },
  "errors": [
    {
      "message": "This app is not approved to use the phoneNumber field. See https://partners.shopify.com/123/apps/456/customer_data for more details.",
      "locations": ...,
      "path": [
        "customer",
        "phoneNumber",
        "phoneNumber"
      ]
    }
  ]
}
```

### Requirements

To help apps safely process protected customer data, you must implement the following requirements in your development practices and in your apps. These requirements reflect the minimum acceptable handling of protected customer data and help apps support merchants with increasingly strict privacy and security requirements. You might need to consult with a privacy or legal professional for help applying these requirements to your business.

If you're using only protected customer data, then you must meet the level 1 requirements.

If you're using protected customer data including name, address, phone, or email fields, then you must meet all of the level 1 and 2 requirements.

#### Level 1 requirements

1. **Process only the minimum personal data required to provide app functionality to merchants.** Processing personal data comes with legal and regulatory requirements to secure, monitor, manage, and communicate about the data. Using the minimum data required helps minimize the time and effort spent complying with these requirements, and limits the potential damage of a data breach or unauthorized access.
2. **Inform merchants what personal data you process and your reason for processing it.** Transparency with merchants about what personal data is processed and why helps merchants manage what processing occurs on their behalf. This information is often included in your privacy policy or data protection agreement.
3. **Limit your processing of personal data to the stated purposes.** Processing must be limited to the stated purposes to ensure that merchants and customers are correctly informed about how their data is used.
4. **Where applicable, respect and apply customer consent decisions.** Customer consent is a critical mechanism for customers to participate in their data processing and might be required depending on the type of processing your app performs.
5. **Where applicable, respect and apply customer decisions to opt out of any data sharing such as a 'data sale' or similar concept under applicable laws or regulations.** Merchants must comply with applicable laws and regulations around sharing of personal data and this requirement helps ensure you are prepared to support them.
6. **If you use personal data for automated decision-making and those decisions might have legal or significant effects, then you must allow customers to opt out.** Automated decision-making can include personal data processing such as profiling, analyzing, predicting, or scoring algorithms. Automated decisions with legal or significant effects are those that have a material impact on people's lives and it's important to give customers the option to have their data manually processed.
7. **Make privacy and data protection agreements with your merchants.** Data protection agreements or privacy policies represent an agreement about personal data processing and are an important tool for formal and safe data privacy practices. They often include details such as data transfer mechanisms, scope of data processed, legal roles and responsibilities, retention, and definition of terms.
8. **Apply retention periods to make sure that personal data isn't kept for longer than needed.** Personal data must not be kept longer than necessary for the stated processing purposes. Retaining personal data longer than necessary increases the security risk of unauthorized access or inappropriate processing.
9. **Encrypt data at rest and in transit.** Encrypting data when stored and as it transits various networks helps to prevent bad actors from gaining access to it even if they have access to the application. It also reduces the consequences of unintentionally disclosing the data set to the general public.

#### Level 2 requirements

1. **Encrypt your data backups.** Data backups can contain personal data and should be treated with the same level of concern and consideration as production data in order to prevent unauthorized access.
2. **Keep test and production data separate.** Strict separation of environments prevents personal data from production from leaking into less secure environments where it could become exposed.
3. **Have a data loss prevention strategy.** A data loss prevention strategy is a combination of technical controls, policies, and standards that protect an organization from the possibility of a bad actor extracting data for nefarious purposes.
4. **Limit staff access to protected customer data.** Limiting staff access to protected customer data minimizes the risk that data will be improperly accessed, exfiltrated, or processed.
5. **Require strong passwords for staff accounts.** Strong password requirements often include minimum length and a mixture of numbers, letters, and special characters.
6. **Keep an access log to protected customer data.** Keeping logs and reviewing them frequently allows an organization to not only keep an audit trail of activity related to data access, but also assess whether their security controls are working effectively.
7. **Implement a security incident response policy.** A security incident response policy helps organizations respond appropriately to security incidents and/or data breaches. These policies often include incident severity scales, roles and responsibilities, escalation paths, evidence collection, and required actions.

### Data protection review

To help you meet the protected customer data requirements, we might ask for a detailed review of your practices. During this review, you'll need to provide evidence that your app and your practices meet the protected customer data requirements. If we select your app for a data protection review, then we'll contact you with instructions on how to proceed. Data protection reviews can occur after you've implemented the protected customer data requirements.

While any app might be selected, data protection reviews will likely focus on apps that have:

- High number of merchant installs
- High volume of customer records
- More protected customer fields approved
- Long retention of personal data

---

## Privacy requirements

> Fonte: https://shopify.dev/docs/apps/launch/privacy-requirements

With privacy laws in jurisdictions such as the European Economic Area, United Kingdom, and United States, it's crucial for app developers who work with merchants to disclose all data collection and usage through a privacy policy. Privacy laws such as the General Data Protection Regulation (GDPR), California Privacy Rights Act (CPRA), Colorado Privacy Act, and Virginia's Consumer Data Protection Act clarify and impose obligations on any party that collects, processes, or stores personal data of an individual.

We've [discussed data privacy legislation on our blog](https://www.shopify.com/blog/ecommerce-laws) and how it affects our [merchants](https://help.shopify.com/en/manual/privacy-and-security/privacy), but privacy laws may also apply to developers that build Shopify apps.

We want to ensure that you're setting yourself up for success by complying with any applicable privacy laws and carefully considering what, if any, personal data your app requires, by subscribing to the [mandatory webhooks](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance), and by creating a [privacy policy](#app-privacy-policies) if required.

Privacy laws are complex, and will apply differently based on how personal data is collected, processed, or stored. If you have any concerns, then we strongly recommend consulting a lawyer about which privacy laws specifically apply to you.

**Caution:** This page isn't intended to provide you with legal advice. It sets out Shopify's privacy requirements for app developers and items that you need to consider if you're handling personal data.

### App privacy policies

To help comply with privacy laws, and to gain merchant trust by clarifying exactly how merchant and buyer data is used, you must provide a privacy policy and link to it from your Shopify App Store listing. These requirements are the same for both [full and limited visibility](https://shopify.dev/docs/apps/launch/distribution/visibility) apps.

Certain privacy laws require businesses, including app businesses, to provide their customers and users with specific information about how their app or product collects and uses personal data.

We recommend that you include the following details in your app's privacy policy:

- What information do you collect through Shopify's APIs?
- What information do you collect directly from the merchant? For example, do you ask them for contact details? Do you ask them for information about the merchant's customers? Do you generate automated logs relating to the merchant's use of your app?
- What information do you collect directly from merchants' customers? For example, do you drop cookies or use other tracking technologies on their devices? Do you log information relating to how customers visit or navigate particular stores?
- How do you use the information you collect? Do you use this information for any purposes other than providing your app's services?
- For how long do you store or retain the data that you collect?
- Are you established in Europe? Are you storing or processing information outside of Europe?
- How can merchants contact you if they have additional questions? Some jurisdictions require that you also include a physical address.

**Note:** It is important to be transparent and provide clear details to individuals about how their personal data is collected, processed, and stored. If you have any concerns about how best to describe your app's data practices, then we recommend consulting with a lawyer about your specific needs.

### Data rights of individuals

In several jurisdictions, individuals have certain rights with respect to how their personal data is collected, stored, and used. To ensure that your app is legally compliant, it's crucial to consider the following:

- Individuals may have rights to access, correct, erase, and restrict how their personal data is processed. Have a process for receiving and responding to these requests.
- Privacy laws may impose restrictions on transferring data about individuals outside the country of origin, except under certain circumstances. For example, the GDPR requires that such transfers can only take place where there are adequate protections that are essentially equivalent to those in the European Economic Area (EEA). This could be through an adequacy decision, the use of standard contractual clauses, or the use of agreed transfer frameworks.
- Certain privacy laws, such as Singapore's Personal Data Protection Act (PDPA) or the EEA's GDPR, may require you to have a Data Protection Officer (DPO) or Privacy Officer to advise the company, in an independent manner, and monitor its compliance with applicable privacy laws.
- You should consider whether you're required to have a DPO/Privacy Officer, and whether you want to appoint one internally or if you want to use an outside consultant or firm. Note that there are certain requirements in order to be a DPO/Privacy Officer.

**Note:** If you have concerns about how privacy laws affect how you currently collect, process, and store personal data, then we suggest you consult with a lawyer.

### Consent for marketing apps

If your app provides marketing or advertising-related services, then you'll need to consider how privacy and marketing laws apply to you. How the laws apply to you depends on how your app uses data, but you'll need to consider the following:

- Whether you need to obtain consent, or ensure that consent has been obtained, from individuals to use their personal data for such purposes in certain jurisdictions.
- Whether you need to facilitate individuals opting out from such use of their personal data in certain jurisdictions.
- How you use personal data to generate any interest-based segments or inferences to target ads or marketing.

---

# Pagine aggiuntive

Le seguenti pagine fanno parte dello scope ma sono **riferimenti enormi o puramente di reference**: sono elencate qui anziché trascritte integralmente (regola di scala). Inoltre includo le pagine vincolanti citate ripetutamente dalla checklist.

### Webhooks — topic reference (enorme: ogni singolo topic)

- Webhooks overview & reference (tutti i topic, payload, scope richiesti): https://shopify.dev/docs/api/webhooks
- REST Admin API webhook resource: https://shopify.dev/docs/api/admin-rest/latest/resources/webhook
- GraphQL Admin API `WebhookSubscriptionTopic` enum (elenco completo dei topic): https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic
- Events (next-gen subscriptions) overview: https://shopify.dev/docs/apps/build/events-webhooks
- Events reference (topic supportati): https://shopify.dev/docs/api/events

### Billing — pagine di reference e how-to aggiuntive

- Migrating to Shopify App Pricing: https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/migrating-to-shopify-app-pricing
- Combined subscription and usage (Shopify App Pricing): https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/subscription-billing/combined-subscription-and-usage
- Public and private plans (Shopify App Pricing): https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/plans
- Redirect to the plan selection page: https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/redirect-plan-selection-page
- Offer free trials (Shopify App Pricing variant): https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/subscription-billing/offer-free-trials
- Build a billing event (App Events API): https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/subscription-billing/build-billing-event
- App Events API reference: https://shopify.dev/docs/api/app-events
- Partner API reference (Active Subscription / Historical Events): https://shopify.dev/docs/api/partner
- Manual pricing — combine time and usage: https://shopify.dev/docs/apps/launch/billing/manual-pricing/subscription-billing/combine-time-and-usage
- Manual pricing — complex pricing models: https://shopify.dev/docs/apps/launch/billing/manual-pricing/subscription-billing/complex-pricing-models
- Manual pricing — offer subscription discounts: https://shopify.dev/docs/apps/launch/billing/manual-pricing/subscription-billing/offer-subscription-discounts
- Manual pricing — offer free trials: https://shopify.dev/docs/apps/launch/billing/manual-pricing/subscription-billing/offer-free-trials
- Award app credits: https://shopify.dev/docs/apps/launch/billing/billing-adjustments/award-app-credits
- Refund app charges: https://shopify.dev/docs/apps/launch/billing/billing-adjustments/refund-app-charges
- View charges and earnings: https://shopify.dev/docs/apps/launch/billing/view-charges-earnings
- GraphQL Admin API billing mutations (`appSubscriptionCreate`, `appPurchaseOneTimeCreate`, `appUsageRecordCreate`): https://shopify.dev/docs/api/admin-graphql/latest/mutations/appSubscriptionCreate

### Distribution & launch — requisiti vincolanti e pagine correlate

- App Store requirements (elenco numerato vincolante 1.x–5.x): https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements
- Submit your app for review: https://shopify.dev/docs/apps/launch/app-store-review/submit-app-for-review
- Prepare/pass app review (test billing, common problems): https://shopify.dev/docs/apps/launch/app-store-review/pass-app-review
- App listing categories: https://shopify.dev/docs/apps/launch/app-store-review/app-listing-categories
- App listing visibility (full vs limited): https://shopify.dev/docs/apps/launch/distribution/visibility
- Revenue share: https://shopify.dev/docs/apps/launch/distribution/revenue-share
- Support your customers: https://shopify.dev/docs/apps/launch/distribution/support-your-customers
- Go-to-market success: https://shopify.dev/docs/apps/launch/distribution/go-to-market-success
- Built for Shopify (overview e achievement): https://shopify.dev/docs/apps/launch/built-for-shopify
- Built for Shopify changelog: https://shopify.dev/changelog?filter=built_for_shopify
- Shopify App Store ads / advertising: https://shopify.dev/docs/apps/launch/marketing/advertising
- Deployment — app versions & deploy in CI/CD: https://shopify.dev/docs/apps/launch/deployment/app-versions

### Design / UX — pagine di reference

- Polaris design system (componenti, token, content guidelines): https://polaris.shopify.com
- Admin UI extensions reference (targets, target APIs, web components): https://shopify.dev/docs/api/admin-extensions
- App Bridge reference: https://shopify.dev/docs/api/app-bridge
- App Home reference: https://shopify.dev/docs/api/app-home
- Navigation guidelines: https://shopify.dev/apps/design-guidelines/navigation
- Layout guidelines: https://shopify.dev/docs/apps/design/layout

### Configurazione & autenticazione — pagine correlate

- Managing app configuration files: https://shopify.dev/docs/apps/build/cli-for-apps/manage-app-config-files
- Shopify CLI `app deploy` / `app dev` reference: https://shopify.dev/docs/api/shopify-cli/app/app-deploy
- Access scopes reference (elenco completo): https://shopify.dev/docs/api/usage/access-scopes
- Authentication & authorization overview: https://shopify.dev/docs/apps/build/authentication-authorization

