# 12. Custom Apps — Foundations & Auth

This chapter captures the **foundations of Shopify App development**: what apps are and how they extend Shopify, how an app is structured, how authentication and authorization work (OAuth, session tokens, token exchange, access scopes, online vs offline tokens), App Bridge and the embedded admin UI, App Home, and the build tools (Shopify CLI, the React Router template, scaffolding, local dev, deploy, distribution).

It is assembled faithfully from the official Shopify developer documentation under `shopify.dev/docs/apps` and `shopify.dev/docs/api/app-bridge-library` (which now redirects to the App Home reference). Each captured page is reproduced under its own `##` section with a `> Fonte:` source URL. Internal headings from each page have been demoted so the chapter keeps a single heading hierarchy. This chapter deliberately covers **conceptual and how-to guide pages** — the giant auto-generated API/web-component reference subtrees are listed (not extracted) at the end under *Pagine aggiuntive*.

---

## Sezioni

1. **Overview** — what apps are, getting started, the Dev Dashboard
2. **App architecture & structure** — CLI app structure, configuration (`shopify.app.toml`), app types (custom vs public)
3. **Authentication & authorization** — auth vs authz, session tokens, token exchange, access tokens (online/offline), authorization code grant, client credentials, managed installation, access scopes, custom authorization
4. **App Bridge** — overview, APIs index, web components, App Bridge web components, navigation, resource picker
5. **App Home & embedding in admin** — App Home models, integrating with the Shopify admin
6. **Build tools** — Shopify CLI for apps, scaffolding, the React Router build tutorial, deployment, distribution

---

# Section 1 — Overview

Mini-TOC:
- [Build apps for Shopify (apps landing)](#build-apps-for-shopify-apps-landing)
- [Dev Dashboard](#dev-dashboard)

---

## Build apps for Shopify (apps landing)

> Fonte: https://shopify.dev/docs/apps  /  https://shopify.dev/docs/apps/build

Shopify is a commerce platform that apps extend. Build with APIs, web components, and backend logic to solve merchant problems across every surface.

### Getting Started

#### Scaffold an app

Use Shopify CLI to generate a new app project with everything you need.

#### Build an app

After scaffolding, build your first Shopify app with APIs, tools, and libraries.

### Dev Tools

#### Set up your development environment

Generate apps and extensions, manage dev stores, connect AI assistants, and deploy projects.

- **Dev MCP server** — Connect your AI assistant to Shopify docs, API schemas, and development resources.
- **Shopify CLI for apps** — Generate apps and extensions, run dev servers, and deploy projects from the command line.
- **Dev Dashboard** — Create and manage apps, stores, and collaborator access in one place.

### Extending Shopify

#### Build across every surface

Extend multiple Shopify surfaces from a single app, from pages in the admin to checkout customizations, storefront themes, and automation workflows. All UI surfaces share Polaris, Shopify's unified system for building app interfaces.

- **App Home** — Build your app's main interface in the Shopify admin with React Router and App Bridge, or as a Shopify-hosted UI extension.
- **Admin** — Add actions, blocks, and print functionality to resource pages in the Shopify admin.
- **Checkout** — Customize the checkout experience with UI extensions and backend logic.
- **Customer accounts** — Extend order status pages and the logged-in customer experience.
- **Flow** — Integrate triggers, actions, and templates into Shopify's automation platform.
- **Online store** — Add dynamic functionality to merchants' storefront themes.
- **Point of Sale** — Add custom functionality to Shopify POS on iOS and Android.
- **Sidekick** — Use app extensions to integrate your app with Sidekick.

### Building Blocks

#### Connect to data and customize backend logic

Read and write store data with APIs, react to events with webhooks, and customize Shopify's backend behavior with Functions.

- **GraphQL** — Query and mutate products, customers, orders, inventory, and more.
- **Extensions** — Add your app's functionality to Shopify user interfaces with app extensions.
- **Shopify Functions** — Customize backend logic for discounts, payments, delivery, and cart validation.
- **ShopifyQL** — Query store data with an SQL-like language built for commerce.
- **Events** — Subscribe to granular changes to GraphQL Admin objects, and shape the data you receive.
- **Webhooks** — Subscribe to store events and trigger your own logic in real time.
- **Storefront MCP** — Build AI agents that access storefront data through MCP servers.
- **Metafields** — Extend Shopify resources with custom fields and validation rules.
- **Metaobjects** — Store structured content that can be reused across the store.
- **Authentication** — Authenticate with Shopify and manage access scopes for your app.

### Use Cases

#### Build for specific commerce workflows

Integrate with dedicated APIs for discounts, payments, fulfillment, and other merchant workflows: Marketing and analytics, Discounts, Product merchandising, Purchase options, Global markets, Orders and fulfillment, Payments, Sales channels, B2B, Shopify Collective, Blockchain.

### Best Practices

#### Ship with quality

Follow Shopify's guidelines for performance, accessibility, security, and compliance to meet App Store requirements and deliver a great merchant experience: Performance, Accessibility, Localize your app, Integrating with Shopify, Mobile support, Non-deceptive code, Compliance, Security.

---

## Dev Dashboard

> Fonte: https://shopify.dev/docs/apps/build/dev-dashboard

The Dev Dashboard serves as the central hub for building on Shopify. Whether you're building apps, setting up stores for clients, or managing collaborator access to merchant stores, it all lives here.

[Go to Dev Dashboard](https://dev.shopify.com/dashboard/)

### Create apps

Build apps that extend, automate, or connect your store in countless ways. Whether you want to build fully interactive experiences or just need secure API access, getting started is straightforward and approachable for any skill level.

#### Use Shopify CLI to build feature-rich, extensible apps

"The recommended way to create a Shopify app is with Shopify CLI." The CLI quickly generates a complete project with all the structure and best practices you need to start building right away. As your requirements grow, the CLI makes it easy to add custom admin features, checkout blocks, and embedded user interfaces—all fully integrated with Shopify's platform.

Local development and deployment workflows are built in, ensuring a smooth path from your first line of code to a live app. With CLI projects, you have access to Shopify's latest extensibility options and a full suite of developer tools, supporting everything from simple customizations to advanced multi-surface apps.

[Learn how to start an app using Shopify CLI](https://shopify.dev/docs/apps/build/cli-for-apps)

#### Use the Dev Dashboard for automation or API-only apps

If your project focuses on backend automation, secure data sync, or API integration—and doesn't need an interface in the Shopify admin—you can create and configure an app directly in the Dev Dashboard.

This workflow lets you quickly set up app credentials, permissions, and connections without scaffolding app code. Apps created this way are ideal for tasks like scheduled sync jobs, webhook handling, or simple API utilities, where browser-based app configuration is all you need.

[Learn how to create an app in the Dev Dashboard](https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard)

#### Manage your apps

The Dev Dashboard lets you see every app tied to your organization, check app status, and configure your apps. You can also manage permissions, credentials, and team access.

#### Track performance

The Dev Dashboard gives you direct access to logs and health metrics for each of your apps. Use these built-in monitoring tools to track your app's performance and help identify and diagnose problems.

The dashboard also displays app events data that your app sends to Shopify, giving you a complete view of both Shopify-generated events and custom events from your app.

#### Manage your stores

The Dev Dashboard is the home for all your stores. The **Stores** tab gives you a unified view of every store connected to your organization, across three types:

* **Dev stores**: Testing environments for building and validating apps.
* **Client transfer stores**: Stores you build and hand off to merchant clients.
* **Collaborations**: Merchant-owned stores you have collaborator access to.

#### Create catalogs for agentic experiences

Saved Catalogs let you customize product discovery for your AI agents. Instead of querying all of Shopify's global product catalog, you can create filtered views scoped to specific product taxonomies, price ranges, or individual shops.

From the Dev Dashboard, you can configure catalog filters, preview search results, and generate a custom endpoint URL for your agents. This is useful when your agents consistently need the same query parameters applied to every request.

### Accessing the Dev Dashboard

Access the Dev Dashboard directly at [dev.shopify.com/dashboard](https://dev.shopify.com/dashboard/). Or, navigate to the dashboard from the Shopify Admin or the Partner Dashboard:

#### From the Shopify admin

1. Select your store name in the top, right-hand corner of the screen.
2. Select **Dev Dashboard**.

#### From the Partner Dashboard

1. Select **App distribution** from the left sidebar.
2. Select **Visit Dev Dashboard**.

### Next steps

- Build with Shopify CLI
- Build in Dev Dashboard
- Manage your stores
- Manage App Automation Tokens
- Manage your organization

---

# Section 2 — App architecture & structure

Mini-TOC:
- [Scaffold an app](#scaffold-an-app)
- [Create apps using the Dev Dashboard](#create-apps-using-the-dev-dashboard)
- [App structure (CLI directory structure)](#app-structure-cli-directory-structure)
- [App configuration (shopify.app.toml)](#app-configuration-shopifyapptoml)

---

## Scaffold an app

> Fonte: https://shopify.dev/docs/apps/build/scaffold-app

You're ready to scaffold a new app. You want to set up your development environment so that you can start coding.

In this tutorial, you'll scaffold an app that users access from the Shopify admin by using a React router template. You'll generate starter code and use Shopify CLI to develop your app. This React router template is the recommended path for most apps.

If you're building a simple custom-distribution app that doesn't need server-side logic, you can also create an app using the extension-only template with an App Home UI extension. To learn more about which option is right for your use case, see Apps in App Home.

**Info:**

* Building a simple integration? If you're connecting an existing system to Shopify and only need API credentials (no embedded UI), create an app in the Dev Dashboard instead.
* Building with your own tech stack? See Authentication and authorization.

### What you'll learn

In this tutorial, you'll learn how to do the following tasks:

* Initialize a React Router app that uses Shopify CLI
* Install your app on a dev store
* Generate a product using your new app

### Requirements

* You're a user with app development permissions and have created a dev store.
* You're using the latest version of Shopify CLI.
* You're using the latest version of Chrome or Firefox.

### Step 1: Create a new app

You can create a new Shopify app using Shopify CLI

1. Navigate to the directory where you want to create your app. Your app will be created in a new subdirectory.
2. Run the following command to create a new app:

   ```terminal
   shopify app init
   ```

3. When prompted, enter a name for your app, and then select **Build a React Router app** to use the React Router template.

   A new app is created and Shopify CLI is installed along with all the dependencies that you need to build Shopify apps.

### Step 2: Start a local development server

After your app is created, you can work with using a local development server and the Shopify CLI.

Shopify CLI uses Cloudflare to create a tunnel that enables your app to be accessed using a HTTPS URL.

1. Navigate to your newly created app directory.

   ```terminal
   cd my-new-app
   ```

2. Run the following command to start a local server for your app:

   ```terminal
   shopify app dev
   ```

Shopify CLI performs the following tasks:

* Guides you through logging into your developer account (either a Partner account or merchant account with appropriate permissions)
* Creates an app in the Dev Dashboard, and connects your local code to the app
* Creates your Prisma SQLite database
* Creates a tunnel between your local machine and the dev store

To learn more about the processes that are executed when you run `dev`, refer to the Shopify CLI command reference.

**Caution:**

To use a dev store with Shopify CLI, you need to be the store owner, or have a staff account on the store. If you create a dev store, then you're assigned as the store owner. Other staff members must be added to the store.

### Step 3: Install your app

You can install your app on your dev store, and automatically populate your dev store with products that you can use for app testing.

1. With the server running, press `p` to open your app's preview URL in a browser. When you open the URL, you're prompted to install the app on your dev store.
2. Click **Install app** to install the app on the dev store. You now have a dev store running with your new app installed.
3. From the home page of the new app, click **Generate a product** to create a product for your dev store.

### Next steps

* Follow the Build a Shopify app using React Router tutorial to learn how to add features to an app using the Shopify React Router template and key Shopify tools and libraries.
* Learn how to deploy and distribute your app.

---

## Create apps using the Dev Dashboard

> Fonte: https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard

The Dev Dashboard provides a simplified interface for creating apps and integrating them with the Shopify admin. This makes it the best choice for quick integrations, such as connecting an existing system to Shopify.

> **Info:** Creating an app for the app store? Build using Shopify CLI instead.

### What you'll learn

* Create and configure a new app using the Dev Dashboard
* Install your app on a dev store
* Authenticate your app to make API requests

### Requirements

* You're a user with app development permissions.
* You're using the latest version of Chrome or Firefox.

### Step 1: Create a new app

1. From the Dev Dashboard, be sure you're on **Apps** in the left-panel navigation and select **Create app** in the top, right corner of the screen.
2. Select **Start from Dev Dashboard**.
3. Name your app, then select **Create**.

### Step 2: Create a version

Once you've created the app, you can create a version. A version is a snapshot of your app's current configuration, URLs, and settings. Your app must have at least one version before it can be installed on a store.

From the **Versions** tab of your app in the Dev Dashboard, complete your desired fields, including:

1. Defining your app URL. If your app isn't embedded in the Shopify admin, you can use the default URL `https://shopify.dev/apps/default-app-home`.
2. Selecting a Webhooks API version (typically the newest version).
3. Entering or selecting your app scopes. These define the data and features your app can access within the Shopify platform. Note that access to protected customer data or other sensitive information requires approval.
4. Select **Release**.

Versions enable you to track changes to your app configuration over time and roll back to previous configurations if needed. When you update scopes in a new version of your app, updates are not applied automatically to the stores your apps are installed in. Merchants still need to manually approve new scopes within your Admin.

### Step 3: Install your app

1. From your app, select **Home** in the left-panel of the Dev Dashboard.
2. Scroll down and select **Install app**.
3. Select or create the store for your app.
4. Select **Install**.

Your app is now installed. To start making API calls, you'll need to authenticate your app as described in the next step.

### Step 4: Authenticate your app

To make API requests, your app needs an access token. If you're building apps for your own store, you can use the client credentials grant:

1. From your app in the Dev Dashboard, select **Settings**.
2. Copy your **Client ID** and **Client secret**.
3. Use these credentials to programmatically request an access token from Shopify's OAuth endpoint. Tokens expire after 24 hours—your code can request a new one when needed.

> **Info:** If you're building with Shopify CLI, authentication is handled automatically.

### Next steps

* Start building with the Admin API to read and write store data.
* Configure Events and webhooks to receive real-time notifications about events in your store.
* Use the Dev Dashboard to monitor your app's performance.

---

## App structure (CLI directory structure)

> Fonte: https://shopify.dev/docs/apps/build/cli-for-apps/app-structure

All apps created with Shopify CLI follow the same basic directory structure. Some elements might be included or omitted depending on your app's functionality.

### Directory Structure

```text
└── <App name>
    ├── shopify.app.toml
    ├── shopify.web.toml
    ├── package.json
    ├── node_modules/
    |   └── ...
    ├── app/
    |   ├── entry.server.[jsx|tsx]
    |   ├── root.[jsx|tsx]
    |   └── ...
    ├── extensions/
    |   ├── my-ui-extension
    |   |  ├── shopify.extension.toml
    |   |  ├── package.json
    |   |  └── ...
    |   ├── my-function-extension
    |   |  ├── shopify.extension.toml
    |   |  ├── package.json
    |   |  └── ...
    |   ├── my-theme-extension
    |   |  ├── shopify.extension.toml
    |   |  ├── package.json
    |   |  └── ...
    |   └── ...
    └── .env
```

| File/directory | Required? | Description |
| - | - | - |
| shopify.app.toml | Yes | A file containing metadata and configuration for your project. This file represents the root of the app. |
| shopify.app.{config-name}.toml | No | One or more files that contain configuration for your project. You can use TOML files to manage your apps' configuration locally and sync them with Shopify. |
| package.json | Yes | A file containing Node-specific metadata about your project. Includes project dependencies and scripts that let you run Shopify CLI commands using your package manager. Depending on your project structure or template, you might have additional `package.json` files in your project subfolders. |
| Web files directory | No | The recommended directory for the web files for your app. Use this directory if you want to build a web interface to display in the Shopify admin or Shopify POS using Shopify App Bridge. These components can be made up of one or more processes. |
| `app/` directory | Yes | The directory that contains the app's entry points, routes, and webhooks. The `entry.server.[jsx\|tsx]` file is the main application entry point. The `root.[jsx\|tsx]` file is the root route of any React Router app. You can also use `root.[jsx\|tsx]` to define any common UI for the app, such as a responsive layout. |
| `extensions/` directory | No | Any app extensions that you've generated in your app. Each directory under `extensions/` represents an extension, where the extension's local identifier is the name of the directory. Each extension's directory must contain a TOML configuration file. |
| env | No | A file containing the UUIDs for your app and each extension in the app. |

### Root Configuration Files

`shopify.app.toml` is a configuration file that contains app-level configuration and metadata. The first time you use the `app dev` or `app config link` CLI commands, the file is updated to reflect the configuration of the linked Shopify app. For more details, refer to App configuration.

#### Named Configuration Files

You can use TOML files with names matching format `shopify.app.{config-name}.toml` to link your project to multiple Shopify apps.

### Web Files

For new apps created with the React Router template, the web files are created at the root directory as a React Router app. Use this directory if you want to build a web interface to display in the Shopify admin or Shopify POS using Shopify App Bridge.

> **Tip:** In older versions of Shopify CLI, the web files were created in a directory called `/web`.

The web interface can consist of one process or multiple processes. For example, you might have one process if you have a standard Rails app with an asset pipeline, or you might have multiple processes if your web app has independent frontend and backend stacks.

> **Tip:** The default location for web files is the `web/` subdirectory. Keeping your web files in a subdirectory like `web/` helps to keep your project organized. However, Shopify CLI supports having the web file at the root of the project or any subdirectory of your choice. To use a different subdirectory or the project root for your web files, include the `shopify.web.toml` file in the directory.

#### shopify.web.toml

A configuration file where you can define properties for your app. The location of this file identifies your web file directory to Shopify CLI.

When you scaffold an app using a template that contains an app, the `shopify.web.toml` file is created in the root directory. If you choose to store your web files in a subdirectory, you need to include a `shopify.web.toml` in that directory instead.

If you need to override the `build` or `dev` command to build or preview your web app, then you can provide your own command at this level.

In projects where you want to serve the web backend and frontend through two processes, you can create a `shopify.web.toml` for each process. Shopify CLI can start the two processes, and expects the frontend web HTTP server to forward the traffic to the backend process.

To explicitly specify the folders where Shopify CLI should look for `shopify.web.toml` files, and to avoid files being loaded twice due to symlinks, use the `web_directories` variable in the `shopify.app.toml` file.

##### shopify.web.toml Example

```text
roles = ["frontend"]

auth_callback_path = ["/custom/path1", "/custom/path2"]

webhooks_path = "/api/webhooks"

[commands]
dev = "npm run dev"
build = "npm run build"
```

| Property | Required? | Description | Values |
| - | - | - | - |
| `roles` | No | List of one or more roles of the process in the directory. If your project uses only one process, then you don't need to specify a value. This property replaces the deprecated `type` property. | `["frontend", "backend", "background"]` |
| `auth_callback_path` | No | Overrides the allowed redirection URLs set in your app configuration. Use this property if your app uses a custom path to handle OAuth callbacks. You can specify a single path, or multiple paths separated by commas. | |
| `webhooks_path` | No | The root path for your app's webhook endpoints. If you run the `dev` command with a `--reset` flag, then Shopify CLI sends an `UNINSTALLED` webhook request for the selected store to this endpoint. If this value isn't set, then the default value of `/api/webhooks` is used. | |
| `port` | No | Specifies which port to use to run your frontend or backend process. If you don't specify a port, then a random one is assigned when you run `dev`. | |
| `commands.build` | No | The command to build the app. This command is run when you run the Shopify CLI `build` command. It's executed from the configuration file's directory. | |
| `commands.dev` | Yes | The command to serve the app. This command is run when you run the Shopify CLI `dev` command. This command is executed from the configuration file's directory. | |
| `type` (deprecated) | No | The role of the process in the directory. If your project uses only one process, then you don't need to specify a value. | `frontend`, `backend` |

#### Web File Conventions

Shopify CLI builds and serves the various parts of your app using the following conventions, some of which use information that is defined in configuration files.

##### Single Process or Frontend Process

The following conventions apply to apps that run on a single process, such as standard Rails apps, and to the frontend process of apps that have both a frontend and backend process.

**Configuration:** The CLI expects at least one `shopify.web.toml` configuration file, with `roles` including `frontend`, or with no type/roles specified. This file can be at the root of the project, or in a project subdirectory. In the case of a single-process app, include `backend` in the list of roles as well.

**Provided Variables** (environment variables):

* `SHOPIFY_API_KEY`: The client ID of the app.
* `SHOPIFY_API_SECRET`: The client secret of the app.
* `HOST`/`APP_URL`: The URL that stores will load.
* `PORT`/`FRONTEND_PORT`/`SERVER_PORT`: The port in which the process' server should run.
* `SCOPES`: The app's access scopes.
* `BACKEND_PORT`: The port in which the second, or backend, process will run if the app is a two-process app. The frontend uses `BACKEND_PORT` to proxy traffic to the backend process.

##### Second Process or Backend Process

The following conventions apply to the backend process of two-process apps, or to single-process apps.

**Configuration:** The CLI expects a `shopify.web.toml` configuration file in any subdirectory of the project, with `roles` including `backend`. The frontend must proxy backend requests to the backend port defined in the environment variable `BACKEND_PORT`.

**Provided Variables:**

* `SHOPIFY_API_KEY`: The client ID of the app.
* `SHOPIFY_API_SECRET`: The client secret of the app.
* `HOST`/`APP_URL`: The URL that stores will load.
* `SERVER_PORT`/`BACKEND_PORT`/`PORT`: The port in which the process's server should run.
* `SCOPES`: The app's access scopes.
* `FRONTEND_PORT`: The port in which the frontend process will run.

##### Background Process

You can also specify additional processes that will run in the background and don't require the behavior of frontend or backend processes. This can be useful for service-oriented architectures or custom file-watcher processes.

**Configuration:** The CLI accepts a `shopify.web.toml` configuration file in any subdirectory of the project, with `roles = ["background"]`.

**Provided Variables:**

* `SHOPIFY_API_KEY`: The client ID of the app.
* `SHOPIFY_API_SECRET`: The client secret of the app.
* `HOST`/`APP_URL`: The URL that stores will load.
* `SERVER_PORT`/`PORT`: The port in which the process's server should run, if the process includes a server.
* `SCOPES`: The app's access scopes.
* `FRONTEND_PORT`: The port in which the frontend process will run.
* `BACKEND_PORT`: The port in which the second, or backend, process will run, if the app has a backend.

### Extensions

The `extensions/` directory contains any app extensions that you've generated onto your app, or that were included in your app template. If your app doesn't contain any app extensions, then you don't need this directory. You can override the default directories using the `extension_directories` variable in `shopify.app.toml`.

Each extension is created in its own directory. The structure of the extension directory depends on the type of extension. Shopify CLI groups extensions into the following types in the TOML file:

| Extension | `type` value in the TOML file | `--template` flag value in the generate command |
| - | - | - |
| Admin action | `ui_extension` | `admin_action` |
| Admin block | `ui_extension` | `admin_block` |
| App Home UI | `ui_extension` | `app_home_ui` |
| Cart and checkout validation | `function` | `cart_checkout_validation` |
| Cart transform | `function` | `cart_transform` |
| Checkout UI | `ui_extension` | `checkout_ui` |
| Customer Account UI | `ui_extension` | `customer_account_ui` |
| Delivery customization | `function` | `delivery_customization` |
| Discounts allocator (developer preview) | `function` | `discounts_allocator` |
| Discount | `function` | `discount` |
| Editor extension collection (developer preview) | `editor_extension_collection` | `editor_extension_collection` |
| Fulfillment constraints | `function` | `fulfillment_constraints` |
| Order routing location rule (beta) | `function` | `order_routing_location_rule` |
| Payment customization | `function` | `payment_customization` |
| POS UI | `ui_extension` | `pos_ui` |
| Post-purchase UI (beta) | `post_purchase_ui` | `post_purchase_ui` |
| Product configuration | `ui_extension` | `product_configuration` |
| Product subscription | `subscription_ui` | `subscription_ui` |
| Shopify Flow action | `flow_action` | `flow_action` |
| Shopify Flow template | `flow_template` | `flow_template` |
| Shopify Flow trigger | `flow_trigger` | `flow_trigger` |
| Shopify POS UI | `pos_ui_extension` | `pos_ui` |
| Theme app extensions | `theme_app_extension` | `theme_app_extension` |
| Web pixel | `web_pixel` | `web_pixel` |

#### Build and Deploy Process

| Extension type | Build and deploy process |
| - | - |
| UI extensions | Shopify CLI builds UI extensions using ESBuild. It expects an extension script named `index.{ts,js,tsx,jsx}` to exist in the extension's directory or the `src/` subdirectory. Shopify CLI build process outputs the extension in `dist/index.js` when running `build`, and inside a temporary directory when running `deploy` to prevent past build artifacts from leaking into the deploy bundle. |
| Functions | Shopify CLI runs the command specified in the `build.command` attribute of the configuration file. It expects the output `wasm` file to be at `dist/index.wasm`, unless a different path is set in the `build.path` attribute. |
| Themes | When building, Shopify CLI runs Theme Check against the theme app extension. |

### Dependency Management

Shopify CLI uses workspaces to manage dependencies for various parts of your app project. For example, your app might contain:

* A `package.json` file at the root of the app project to manage all of the app dependencies and the workspace.
* A `package.json` file for each extension that you create.

We recommend including the lock files generated by the package manager (`yarn.lock`, `package-lock.json`, or `pnpm-lock.yaml`) in the repository to ensure the same version of these dependencies is used consistently across environments.

---

## App configuration (shopify.app.toml)

> Fonte: https://shopify.dev/docs/apps/build/cli-for-apps/app-configuration

You can configure your apps locally with TOML files, then deploy your changes using Shopify CLI. You can also configure many of these values through the Dev Dashboard.

**Note:** Changes to the `shopify.app.toml` are applied automatically during `app dev` for your chosen development store. For app configuration changes to take effect for all stores in production, you need to run the `deploy` command.

### App configuration file example

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

| Property | Required? | Value | Description |
| - | - | - | - |
| `name` | Yes | `string` | The name of your app. |
| `handle` | No | `string` | The URL slug of your App Home, for example `https://admin.shopify.com/store/your-store-name/apps/your-app-handle/app`. **Warning**: Updating the handle changes the Shopify admin URL that appears when you access your app from the side menu. As a result, any app admin links will be broken. |
| `client_id` | Yes | `string` | The app's public identifier. |
| `application_url` | Yes | `string` matching a valid URL | The URL of your app. **Note:** If you're building an extension-only app, then your `application_url` will be set to `https://shopify.dev/apps/default-app-home` by default. |
| `embedded` | Yes | `boolean` | When `true`, your app renders in the Shopify admin, letting users interact with it without leaving Shopify. |
| `extension_directories` | No | `array` of `string` paths or glob patterns | The paths that Shopify CLI will search for app extensions. When omitted, defaults to `["extensions/"]`. |
| `web_directories` | No | `array` of `string` paths or glob patterns | The paths that Shopify CLI will search for the web files of your app. When omitted, defaults to the app root directory. |

#### access_scopes

Define the permissions your app requests, as well as how the permissions are requested.

| Property | Required? | Value | Description |
| - | - | - | - |
| `scopes` | Yes | `string` matching a comma-separated list of scopes | Any access scopes that your app will request access to during the authorization process. When a merchant installs your app with Shopify managed install, they're prompted to grant permission to all the access scopes that you defined in this field. |
| `optional_scopes` | No | `array` of `string` access scopes | Any access scopes that your app can request dynamically after installation. |
| `use_legacy_install_flow` | No | boolean | When omitted or `false`, scopes are saved in your app's configuration, and are automatically requested when the app is installed on a store or when you update the `scopes` value. This is referred to as Shopify managed installation. When `true`, the legacy installation flow requests scopes through a URL parameter during the OAuth flow. The legacy installation flow is still supported, but isn't recommended because your app can end up with different scopes for each installation. |

#### access

Settings for defining the ways that your app can access Shopify APIs.

**admin:**

| Property | Required? | Value | Description |
| - | - | - | - |
| `direct_api_mode` | No | `string` matching `online` or `offline` | The access mode that Direct API access will use. When `online`, Direct API access is enabled and uses an online access token. When `offline`, Direct API access is enabled and uses an offline access token. When omitted, defaults to `online`. |
| `embedded_app_direct_api_access` | No | `boolean` | Whether your app has access to Direct API access for calling types in the GraphQL Admin API. When omitted or `false`, Direct API access is disabled. When `true`, Direct API is enabled and uses the mode defined by `direct_api_mode`. |

#### auth

| Property | Required? | Value | Description |
| - | - | - | - |
| `redirect_urls` | Yes | `array` of `string`s matching a valid URL | Users are redirected to these URLs as part of authorization code grant. You must include at least one redirect URL before making your app public. |

#### customer_authentication

Configure authentication for Customer Account API access. Your app uses these settings for OAuth 2.0 authentication flows with customers. The authentication endpoints are discovered dynamically using discovery endpoints.

| Property | Required? | Value | Description |
| - | - | - | - |
| `redirect_uris` | Yes | An array of strings matching a valid URL | The URIs where customers are redirected after authentication. Supports HTTPS URLs for web applications (for example, `https://app.example.com/api/customer/auth/callback`). These URIs are used with the `authorization_endpoint` discovered from `/.well-known/openid-configuration`. |
| `javascript_origins` | No | An array of string matching a valid origin | The allowed origins for CORS when making requests to authentication endpoints from JavaScript. Required for web applications using the authorization code flow with PKCE. Origins must include protocol and domain (for example, `https://app.example.com`). |
| `logout_urls` | No | An array of strings matching a valid URL | The URLs where customers are redirected after logout. Used with the `end_session_endpoint` discovered from `/.well-known/openid-configuration` for OpenID Connect RP-initiated logout. |

#### webhooks

| Property | Required? | Value | Description |
| - | - | - | - |
| `api_version` | Yes | `string` matching a valid Shopify version (example: `2022-10`) | The API version used to serialize webhooks and cloud service events. |

**subscriptions:**

| Property | Required? | Value | Description |
| - | - | - | - |
| `topics` | Yes | `array` of `string`s matching a valid topic | The topics that your app subscribes to. |
| `compliance_topics` | No | `array` of `string`s matching a valid compliance topic | The topics to manage the requests to view or erase customer personal information. Valid options: `customers/redact`, `customers/data_request` or `shop/redact`. These are required topics to subscribe to for all apps distributed in the Shopify App Store. |
| `uri` | Yes | `string` matching a valid URI | Your app's endpoint to handle the events. It can be a HTTPS URL, a relative path starting with a slash, a Google Pub/Sub URI or an Amazon EventBridge Amazon Resource Name (ARN). |
| `filter` | No | `string` | A set of rules specified using Shopify API's Search Syntax. Ensures only webhooks that match the filter are delivered. |
| `include_fields` | No | `array` of `string`s | Specifies the fields that will be sent in a webhook's event message. If `null`, then all fields will be sent. |

**Info — Google Cloud Pub/Sub URI structure:**

```
pubsub://{project-id}:{topic-id}
```

Where `{project-id}` is the ID of your Google Cloud Platform project, and `{topic-id}` is the ID of the topic that you set up in Google Cloud Pub/Sub.

**For Amazon EventBridge:**

```
arn:aws:events:<aws_region>::event-source/aws.partner/shopify.com/<app_id>/<event_source_name>
```

#### events

| Property | Required? | Value | Description |
| - | - | - | - |
| `api_version` | Yes | `string` matching a valid Shopify version | The API version used to validate and run subscription `query` operations. |

**subscription:**

| Property | Required? | Value | Description |
| - | - | - | - |
| `handle` | Yes | `string` | Unique identifier for this subscription. Alphanumeric, `_`, `-`, max 50 characters. Included in the delivery payload and headers. |
| `topic` | Yes | `string` matching a valid Events topic | The resource your subscription listens to (for example, `Product`). |
| `actions` | Yes | `array` of `create`, `update`, and/or `delete` | The lifecycle transitions that can produce a delivery. |
| `uri` | Yes | `string` matching a valid URI | Your app's endpoint to handle deliveries. |
| `triggers` | No | `array` of `string`s | Field paths that narrow `update` deliveries to specific field changes. |
| `query` | No | `string` | GraphQL Admin API operation whose result appears in the delivery `data` field. |
| `query_filter` | No | `string` | Expression evaluated on the query result to suppress deliveries. |

#### app_proxy

Let Shopify act as a proxy when sending requests to your app.

| Property | Required? | Value | Description |
| - | - | - | - |
| `url` | Yes if `app_proxy` defined | `string` matching a valid URL | URL of your app proxy server |
| `subpath` | Yes if `app_proxy` defined | `string` containing letters, numbers, underscores, and hyphens up to 30 characters. The value may not be `admin`, `services`, `password`, or `login`. | The combination of `prefix` and `subpath` defines where the app proxy is accessed from a merchant's shop. |
| `prefix` | Yes if `app_proxy` defined | `string` matching `a`, `apps`, `community`, or `tools` | The combination of `prefix` and `subpath` defines where the app proxy is accessed from a merchant's shop. |

#### pos

| Property | Required? | Value | Description |
| - | - | - | - |
| `embedded` | No | `boolean` | Load your POS UI extension or App Home app in Shopify POS. |

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

The `shopify app config push` Shopify CLI command is no longer supported. Instead, you can release your app configuration and extensions together with the `deploy` command.

**Migrate interactively** (if you use `shopify app config push` without `--force`):

1. Upgrade Shopify CLI to the latest version.
2. Remove all references to the `shopify app config push` command in any scripts or aliases.
3. When you're ready to deploy both app configuration and all extensions, run `shopify app deploy`.
4. Shopify CLI will ask if you want to start including app configuration on `deploy`. Answer `Yes, always`, and your choice will be saved in your app configuration file.
5. Continue the rest of the `deploy` flow to release a new app version to users.
6. Push your app configuration file to source control, so all contributors use the same app configuration.

**Update your CI/CD workflow** (if you use `shopify app config push` with `--force`):

1. Upgrade Shopify CLI to the latest version.
2. Remove all references to the `shopify app config push` command.
3. Add the `deploy` command with the `--force` flag to your workflow, if it's not there already.

---

# Section 3 — Authentication & authorization

Mini-TOC:
- [Authentication and authorization (overview)](#authentication-and-authorization-overview)
- [About session tokens](#about-session-tokens)
- [Set up session tokens](#set-up-session-tokens)
- [About token acquisition](#about-token-acquisition)
- [Exchange a session token for an access token (token exchange)](#exchange-a-session-token-for-an-access-token-token-exchange)
- [About online access tokens](#about-online-access-tokens)
- [About offline access tokens](#about-offline-access-tokens)
- [Implement authorization code grant manually](#implement-authorization-code-grant-manually)
- [Using the client credentials grant](#using-the-client-credentials-grant)
- [Enable Shopify-managed installations](#enable-shopify-managed-installations)
- [Manage access scopes](#manage-access-scopes)
- [Generate access tokens for custom apps in the Shopify admin](#generate-access-tokens-for-custom-apps-in-the-shopify-admin)
- [Shopify API access scopes (full list)](#shopify-api-access-scopes-full-list)
- [About client credentials (client secrets)](#about-client-credentials-client-secrets)
- [Implement custom authorization](#implement-custom-authorization)

---

## Authentication and authorization (overview)

> Fonte: https://shopify.dev/docs/apps/build/authentication-authorization

This guide introduces the different methods of authenticating and authorizing apps with Shopify's platform. Make sure that you understand the differences between the types of authentication and authorization methods before you begin your development process.

You can use Shopify CLI to generate a starter app with boilerplate code that handles authentication and authorization. The starter app includes code for an app rendered in the Shopify admin that follows best practices:

* Authorizing your app using session tokens and token exchange.
* Installing on stores using Shopify managed installation.

You should use this starter app unless you need to scaffold a standalone app.

### Authentication vs. authorization

"Authentication is the process of verifying the identity of the user or the app." To keep transactions on Shopify's platform safe and secure, all apps connecting with Shopify APIs must authenticate when making API requests.

"Authorization is the process of giving permissions to apps." When an app user installs a Shopify app they authorize the app, enabling the app to acquire an access token. For example, an app might be authorized to access orders and product data in a store.

### Types of authentication and authorization methods

The authentication and authorization methods that your app needs to use depends on the tool that you used to create your app, and the components that your app uses.

#### Authentication

* Apps rendered in the Shopify admin need to authenticate their incoming requests with session tokens.
* Standalone apps need to implement their own authentication method for incoming requests.

#### Authorization

Authorization encompasses the installation of an app and the means to acquire an access token.

To avoid unnecessary redirects and page flickers during the app installation process, you should configure your app's required access scopes using Shopify CLI. This allows Shopify to manage the installation process for you.

If you aren't able to use Shopify CLI to configure your app, then your app will install as part of the authorization code grant flow. This provides a degraded user experience.

If you're building an app for your own organization and don't require user interaction, you can use the client credentials grant to acquire access tokens.

The following table outlines the supported installation and token acquisition flows for various app configurations. Whenever possible, you should create apps rendered in the Shopify admin that use Shopify managed installation and token exchange.

| Type of app | Supported installation flows | Supported token acquisition flows |
| --- | --- | --- |
| App rendered in the Shopify admin | Shopify managed installation (recommended); Installation during authorization code grant | Token exchange (recommended); Authorization code grant |
| Standalone app | Shopify managed installation (recommended); Installation during authorization code grant | Authorization code grant |
| Admin-created custom app | Installed upon generation in the Shopify admin | Generate in the Shopify admin |

OAuth 2.0 is the industry-standard protocol for authorizing or giving permissions to apps. (Note: token exchange was introduced after some videos were created, and the term "OAuth" might be used interchangeably with "authorization code grant.")

### Getting started

* Authenticate your app using session tokens.
* Authorize your app using a session token with token exchange.
* Authorize your standalone app with authorization code grant.
* Authenticate your app created in the Shopify admin with access tokens.

### Tools

* **Shopify CLI** — A command-line tool to help you build Shopify apps faster.
* **shopify_api** — Shopify's official Ruby gem for interacting with the Admin API.
* **@shopify/shopify-api** — Shopify's official Node library for interacting with the Storefront and Admin APIs, handling OAuth, webhooks, and billing.
* **@shopify/admin-api-client** — Shopify's official lightweight Node library for interacting with the Admin API.

---

## About session tokens

> Fonte: https://shopify.dev/docs/apps/build/authentication-authorization/session-tokens

A session token is a mechanism that lets your app authenticate the requests that it makes between the client side and your app's backend.

**Note:** All apps rendered in the Shopify admin need to use session tokens because third-party cookies won't work with browsers that restrict cross-domain data access. If your app still uses cookies and could pose a risk to users, then as part of our app quality check process you might be contacted and requested to migrate your app to use session tokens. This request will require immediate action.

### How Session Tokens Work

This section describes the authentication and request flows associated with session tokens, and the lifetime of a session token.

#### Authentication Flow Using a Session Token

When your app first loads, it's unauthenticated and serves up the frontend code for your app. Your app renders a user interface skeleton or loading screen to the user.

After the frontend code has loaded, your app calls a Shopify App Bridge action to get the session token. Your app includes the session token in an authorization header when it makes any HTTPS requests to its backend.

#### Request Flow Using a Session Token

The session token is signed using the shared secret between your app and Shopify so that your backend can verify if the request is valid.

#### Lifetime of a Session Token

The lifetime of a session token is one minute. Session tokens must be fetched using Shopify App Bridge on each request to make sure that stale tokens aren't used.

#### OAuth and Session Tokens

**Tip:** You can use Shopify CLI to generate a starter app with boilerplate code that handles authentication and authorization. The starter app includes code for an app rendered in the Shopify admin that uses session tokens and token exchange.

Session tokens are for authentication, and aren't a replacement for authorization. Learn more about the difference between authentication and authorization.

Unlike API access tokens, session tokens can't be used to make authenticated requests to Shopify APIs. An API access token is what you use to send requests from your app's backend to Shopify so that you can fetch specific data from the user's shop.

For example, to make authenticated requests to the GraphQL Admin API, your app must store the access token it receives during the OAuth flow. To contrast, session tokens are used by your app's backend to verify the embedded request coming from your app's frontend.

### Anatomy of a Session Token

Session tokens use the JSON Web Token (JWT) format and contain information about the merchant that's currently using your app. A session token consists of a header, payload, and signature. For an interactive example, refer to JWT.io.

For the most part, you shouldn't have to manage the anatomical details of session tokens. In most scenarios, you'll use a library, such as `authenticated_fetch` from app-bridge, which generates and includes the session token in your requests. On the backend, you can use middleware similar to `validateAuthenticatedSession` in @shopify/shopify-app-express.

#### Header

The values in the header are constant and never change.

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

* `alg`: The algorithm used to encode the JWT.
* `typ`: The (type) header parameter used by session token to declare the media type.

#### Payload

```json
{
  "iss": "<shop-name.myshopify.com/admin>",
  "dest": "<shop-name.myshopify.com>",
  "aud": "<client ID>",
  "sub": "<user ID>",
  "exp": "<time in seconds>",
  "nbf": "<time in seconds>",
  "iat": "<time in seconds>",
  "jti": "<random UUID>",
  "sid": "<session ID>",
  "sig": "<signature>"
}
```

* `iss`: The shop's admin domain.
* `dest`: The shop's domain.
* `aud`: The client ID of the receiving app.
* `sub`: The User that the session token is intended for.
* `exp`: When the session token expires.
* `nbf`: When the session token activates.
* `iat`: When the session token was issued.
* `jti`: A secure random UUID.
* `sid`: A unique session ID per user and app.
* `sig`: Shopify signature.

#### Example Payload

```json
{
  "iss"=>"https://exampleshop.myshopify.com/admin",
  "dest"=>"https://exampleshop.myshopify.com",
  "aud"=>"client-id-123",
  "sub"=>"42",
  "exp"=>1591765058,
  "nbf"=>1591764998,
  "iat"=>1591764998,
  "jti"=>"f8912129-1af6-4cad-9ca3-76b0f7621087",
  "sid"=>"aaea182f2732d44c23057c0fea584021a4485b2bd25d3eb7fd349313ad24c685",
  "sig"=>"f07cf3740270c17fb61c700b2f0f2e7f2f4fc8cc48426221738f7a39e4c475bf"
}
```

**Note:** All times are in UNIX timestamp format.

### Limitations

Session token authentication is only fully supported for single-page apps. You can only use session tokens for a multi-page app if you convert it to behave like a single-page app. For an example, refer to the Turbolinks and JWT sample app.

**Caution:** In some cases, ad blockers can interfere with session tokens. If you're submitting your app to the Shopify App Store and the automated check for session tokens is hanging, then try disabling your ad blocker and interacting with your app to record the required session data.

### Sample Apps

* Sample single-page app using Rails and React: https://github.com/Shopify/next-gen-auth-app-demo
* Sample server-side rendered Rails app converted using Turbolinks: https://github.com/Shopify/turbolinks-jwt-sample-app

### Next Steps

* Set up your app to authenticate using session tokens.

---

## Set up session tokens

> Fonte: https://shopify.dev/docs/apps/build/authentication-authorization/session-tokens/set-up-session-tokens

This tutorial explains how to set up session token authentication for your app.

**Caution:** The below guide only applies to App Bridge 2.0. The current version of App Bridge automatically adds session tokens to requests coming from your app. If you want to set up session token authentication for a multi-page server-side rendered (SSR) app, then you need to instead set your app to use Turbolinks.

### Requirements

* You've created an app from the Dev Dashboard or Shopify CLI.
* The app is rendered in the Shopify admin.
* You've learned about how session tokens work.
* The app uses App Bridge version 2.0.
* You've created an App Bridge instance.

**Tip:** You can use Shopify CLI to generate a starter app with boilerplate code that handles authentication and authorization. The starter app includes code for an app rendered in the Shopify admin that uses session tokens and token exchange.

### Recommendations

We recommend using the Shopify App gem, or Shopify Node API library to decode and verify the authenticity of the session token.

### Step 1: Get a session token

The `getSessionToken` helper retrieves a session token from Shopify. It sets up a subscription on the Shopify App Bridge client to listen for the `APP::SESSION_TOKEN_RESPOND` action and then immediately dispatches the `APP::SESSION_TOKEN_REQUEST` action.

```js
import createApp from "@shopify/app-bridge";
import { getSessionToken } from "@shopify/app-bridge/utilities";


const app = createApp({
  apiKey: "12345", // API key from the Dev Dashboard
  host: "YWRtaW4uc2hvcGlmeS5jb20vc3RvcmUvemwtMDMwNDExMjE", // host from URL search parameter
});
```

Where your app requires a session token, specify the following code:

```js
const sessionToken = await getSessionToken(app);
```

`getSessionToken` returns a `Promise`, which either resolves with the session token, or rejects with an `APP::ERROR::FAILED_AUTHENTICATION` error when the session token is `undefined`.

### Step 2: Authenticate your requests

The `authenticatedFetch` helper function authenticates your requests using the session token. The function gets the session token from Shopify App Bridge and passes in the `Authorization` header to your subsequent `fetch` requests.

**Parameters:**

* `app`: The App Bridge instance.
* `fetchOperation`: Optional. Define a custom fetch wrapper.

```js
import ApolloClient from "apollo-client";
import { authenticatedFetch } from "@shopify/app-bridge/utilities";
import createApp from "@shopify/app-bridge";
import { HttpLink } from "apollo-link-http";
import { InMemoryCache } from "apollo-cache-inmemory";


const app = createApp({
  apiKey: "12345", // API key from the Dev Dashboard
  host: "YWRtaW4uc2hvcGlmeS5jb20vc3RvcmUvemwtMDMwNDExMjE", // host from URL search parameter
});


const client = new ApolloClient({
  link: new HttpLink({
    credentials: "same-origin",
    fetch: authenticatedFetch(app), // ensures that all requests triggered by the ApolloClient are authenticated
  }),
  cache: new InMemoryCache(),
});
```

#### Use a custom fetch wrapper

If you want to add custom headers, caching, or special treatment of requests, then you can optionally pass in a custom fetch wrapper function to the `fetchOperation` parameter. Any custom fetch function that you provide needs to append all the appropriate options, including headers:

```js
import ApolloClient from "apollo-client";
import { authenticatedFetch } from "@shopify/app-bridge/utilities";
import createApp from "@shopify/app-bridge";
import deepMerge from "@shopify/app-bridge/actions/merge";
import { HttpLink } from "apollo-link-http";
import { InMemoryCache } from "apollo-cache-inmemory";


// Sample custom fetch wrapper
const yourCustomFetchWrapper = (uri, options) => {
  const aggregateOptions = deepMerge(options, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
  });
  return fetch(uri, aggregateOptions);
};


const app = createApp({
  apiKey: "12345", // API key from the Dev Dashboard
  host: "YWRtaW4uc2hvcGlmeS5jb20vc3RvcmUvemwtMDMwNDExMjE", // host from URL search parameter
});


const client = new ApolloClient({
  link: new HttpLink({
    credentials: "same-origin",
    fetch: authenticatedFetch(app, yourCustomFetchWrapper), // ensures that your custom fetch wrapper is authenticated
  }),
  cache: new InMemoryCache(),
});
```

### Step 3: Decode session tokens for incoming requests

You need to add middleware that detects requests with a session token present, verifies that the session token's signature is correct, and then builds a session based on the shop and user information included in the token. The Shopify App gem and Shopify Node API library provide middleware and utilities for decoding session tokens.

#### Optional: Obtain session details and verify the session token manually

A session token is a JWT string with the following structure: `<header>.<payload>.<signature>`. You can obtain the session details from the payload and then verify the contents as follows:

1. Extract the `exp` value from the payload. Verify that the datetime value is in the future.
2. Extract the `nbf` value from the payload. Verify that the datetime value was in the past.
3. Extract the `iss` and `dest` fields from the payload. The top-level domains should match. The `dest` field specifies the shops that the request originated from. For example, `myshop.myshopify.com`.
4. Extract the `aud` value from the payload. Verify that the value matches the client ID of your app.
5. Extract the `sub` value from the payload. This is the ID of the user that made the request.

If any of the above steps fail, then discard the payload, stop processing the request, and respond with an error.

**Note:** Without third-party cookies, setting Cross-Site Request Forgery (CSRF) tokens in a cookie might not be possible. The session token serves as an alternative to CSRF tokens, because you can trust that the session token has been issued by Shopify to your app frontend.

#### Verify the session token's signature

To verify that the signature is correct, you need to generate a new Base64url-encoded signature using the app's shared secret. Session tokens are signed using the HS256 algorithm (symmetric). The signing key is the shared secret for your Shopify app.

1. Take the `<header>.<payload>` portion of the string and hash it with SHA-256.
2. Sign the string using the HS256 algorithm by using the app's secret as the signing key.
3. Base64url-encode the result.
4. Verify that the result is the same as the signature that was sent with the session token.

### Step 4: Allow authenticated requests

To allow authenticated requests, you need to update the route that serves the app so that it allows unauthenticated requests. You also need to add logic to the unauthenticated route to detect if this is the first time that the shop is loading your app.

**Update the route:** If the page that's rendered by the route depends on an authenticated request to the route, then remove the protected data from the response and expose the data to the frontend using an authenticated API route. The only app user information that should be available on unauthenticated routes is the shop domain, which is passed in as a query parameter in the app URL.

**Add logic to the unauthenticated route:** If your app doesn't have a valid online or offline access token, then it should get a new session token from App Bridge. The session token should be passed into the app backend to exchange for an online and offline access token using token exchange.

### Step 5: Mark shop records as uninstalled using the `app/uninstalled` webhook

To ensure OAuth continues to work with session tokens, your app must update its shop records when a shop uninstalls your app. An app can receive notifications of uninstall events by subscribing to the `app/uninstalled` webhook.

**Set up the webhook:**

```text
rails g shopify_app:add_webhook -t app/uninstalled -a {your_app_url}/webhooks/app_uninstalled
```

**Mark the shop record as uninstalled:**

```ruby
class AppUninstalledJob < ActiveJob::Base
  def perform(args)
    shop = Shop.find_by(shopify_domain: args[:shop_domain])


    mark_shop_as_uninstalled(shop)
  end


  private


  def mark_shop_as_uninstalled(shop)
    shop.uninstall! if shop
  end
end
```

**Define a background job** (to ensure shops with existing installations also have the uninstall webhook set up):

```ruby
class RegisterWebhooksForActiveShops < ApplicationJob
  queue_as :default


  def perform
    register_webhooks_for_active_shops
  end


  private


  def register_webhooks_for_active_shops
    Shop.find_each do |shop|
      ShopifyApp::WebhooksManagerJob.perform_now(
        shop_domain: shop.shopify_domain,
        shop_token: shop.shopify_token,
        webhooks: ShopifyApp.configuration.webhooks
      )
    end
  end
end
```

Enqueue the `RegisterWebhooksForActiveShops` background job to apply the webhook registration.

### Step 6: Handle the expiry of online access tokens

Apps that use online access tokens need to keep track of whether the online access token is expired. If the online access token is expired, your app can request a new one using token exchange.

### Step 7: Verify that the session token is being sent

Your app should now work using session token authentication. When any network calls are made, you should see the session token being sent in the header.

### Next steps

* Exchange your session token for an access token with token exchange.

---

## About token acquisition

> Fonte: https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens

> "You can use Shopify CLI to generate a starter app with boilerplate code that handles authorization. This is the recommended method."

The Shopify platform offers two approaches for apps to obtain access tokens: token exchange and authorization code grant. Apps embedded in the Shopify admin should use token exchange, whereas standalone apps require authorization code grant.

### Token Exchange

OAuth 2.0 token exchange enables apps to exchange a session token for an access token. The session token is restricted to apps displayed in the Shopify admin and can be obtained through App Bridge. Generating a starter app handles authentication automatically.

### Authorization Code Grant

For standalone applications, Shopify implements OAuth 2.0's authorization code grant flow to issue access tokens on behalf of merchants. This OAuth process allows merchants to grant app access to store data, such as orders and products.

1. The user initiates an app installation request.
2. The app redirects to Shopify's grant screen, requesting authorization for required scopes. For apps with API access scopes in TOML files, the grant screen may appear before redirection.
3. The user authorizes the app by accepting requested scopes.
4. The app receives an authorization grant—a temporary credential representing authorization.
5. The app requests an access token by authenticating with Shopify and presenting the authorization grant.
6. Shopify authenticates the app, validates the grant, and issues an access token. The app can now retrieve Shopify data.
7. The app uses the access token for Shopify API requests.
8. Shopify validates the access token and returns requested data.

#### Ways to Implement Authorization Code Grant

* For new apps, Shopify recommends using Shopify CLI to create your app. This starter app uses token exchange and session tokens.
* For existing apps, standalone applications, or template alternatives, consider a Shopify Admin API library. These libraries provide authorization code grant methods (except React Router, which uses token exchange) and enhance implementation speed and security.

---

## Exchange a session token for an access token (token exchange)

> Fonte: https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/token-exchange

> **Tip:** You can use Shopify CLI to generate a starter app with boilerplate code that handles authentication and authorization. The starter app includes code for an app rendered in the Shopify admin that uses session tokens and token exchange.

### Requirements

- You've created an app rendered in the Shopify admin that doesn't use a Shopify app template.
- You have your app's client credentials.
- You're familiar with session tokens in Shopify.

### Step 1: Ensure you have a valid session token

Your app's frontend must acquire a session token from App Bridge. In the current version of App Bridge, this is handled automatically using `authenticatedFetch`. You must include the token in the `AUTHORIZATION` header for all requests to the app's backend. Your app's backend is responsible for authenticating all incoming requests using the session token.

### Step 2: Get an access token

If your app doesn't have a valid access token, then it can exchange its session token for an access token using token exchange.

#### Token exchange API

```http
POST https://{shop}.myshopify.com/admin/oauth/access_token
```

| Parameter | Description |
| - | - |
| `client_id` | The API key for the app. |
| `client_secret` | The client secret for the app. |
| `grant_type` | The value `urn:ietf:params:oauth:grant-type:token-exchange` indicates that token exchange is to be performed. |
| `subject_token` | An ID token that represents the identity and active browser session of a merchant using the app. |
| `subject_token_type` | The value `urn:ietf:params:oauth:token-type:id_token` indicates that the subject token type is an ID token. |
| `requested_token_type` | `urn:shopify:params:oauth:token-type:offline-access-token` (default) for requesting offline access tokens; `urn:shopify:params:oauth:token-type:online-access-token` for requesting online access tokens |
| `expiring` | Only applicable if `requested_token_type` is set to offline-access-token. `0` (default) for a non-expiring offline token; `1` for an expiring offline token |

#### Request — Online access token

```terminal
curl -X POST \
  https://{shop}.myshopify.com/admin/oauth/access_token \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Accept: application/json' \
  -d 'client_id={client_id}' \
  -d 'client_secret={client_secret}' \
  -d 'grant_type=urn:ietf:params:oauth:grant-type:token-exchange' \
  -d 'subject_token={session_token}' \
  -d 'subject_token_type=urn:ietf:params:oauth:token-type:id_token' \
  -d 'requested_token_type=urn:shopify:params:oauth:token-type:online-access-token'
```

#### Request — Expiring offline access token

```terminal
curl -X POST \
  https://{shop}.myshopify.com/admin/oauth/access_token \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Accept: application/json' \
  -d 'client_id={client_id}' \
  -d 'client_secret={client_secret}' \
  -d 'grant_type=urn:ietf:params:oauth:grant-type:token-exchange' \
  -d 'subject_token={session_token}' \
  -d 'subject_token_type=urn:ietf:params:oauth:token-type:id_token' \
  -d 'requested_token_type=urn:shopify:params:oauth:token-type:offline-access-token' \
  -d 'expiring=1'
```

#### Request — Non-expiring offline access token

```terminal
curl -X POST \
  https://{shop}.myshopify.com/admin/oauth/access_token \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Accept: application/json' \
  -d 'client_id={client_id}' \
  -d 'client_secret={client_secret}' \
  -d 'grant_type=urn:ietf:params:oauth:grant-type:token-exchange' \
  -d 'subject_token={session_token}' \
  -d 'subject_token_type=urn:ietf:params:oauth:token-type:id_token' \
  -d 'requested_token_type=urn:shopify:params:oauth:token-type:offline-access-token'
```

#### Response — Online access token

```json
{
  "access_token": "f85632530bf277ec9ac6f649fc327f17",
  "scope": "write_orders,read_customers",
  "expires_in": 86399,
  "associated_user_scope": "write_orders",
  "associated_user": {
    "id": 902541635,
    "first_name": "John",
    "last_name": "Smith",
    "email": "john@example.com",
    "email_verified": true,
    "account_owner": true,
    "locale": "en",
    "collaborator": false
  }
}
```

#### Response — Expiring offline access token

```json
{
  "access_token": "f85632530bf277ec9ac6f649fc327f17",
  "scope": "write_orders,read_customers",
  "expires_in": 3600,
  "refresh_token": "shprt_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "refresh_token_expires_in": 7776000
}
```

#### Response — Non-expiring offline access token

```json
{
  "access_token": "f85632530bf277ec9ac6f649fc327f17",
  "scope": "write_orders,read_customers"
}
```

If your session token is expired or otherwise invalid, then the token exchange request fails with an HTTP status code of `400 Bad Request`.

#### Online access token response values

| Value | Description |
| - | - |
| `access_token` | An API access token that can be used to access the shop's data. An online access token can be used for as long as the app is installed or for the next 24 hours, whichever comes first. After 24 hours, you need to refresh the access token. |
| `scope` | The list of access scopes that were granted to your app and are associated with the access token. |
| `expires_in` | The number of seconds until the access token expires. |
| `associated_user_scope` | The list of access scopes that were granted to the app and are available for this access token, given the user's permissions. |
| `associated_user` | Information about the user who completed the authorization. The `email` field appears regardless of the email verification status; if using emails as an identification source, make sure `email_verified` is also `true`. You can use the `id` field to uniquely identify a single user. |

#### Offline access token response values

| Value | Description |
| - | - |
| `access_token` | An API access token that can be used to access the shop's data. |
| `scope` | The list of access scopes that were granted to your app and are associated with the access token. |
| `expires_in`* | The number of seconds until the access token expires. |
| `refresh_token`* | The refresh token that can be used to obtain a new access token when the current one expires. |
| `refresh_token_expires_in`* | The number of seconds until the refresh token expires. |

\* Only included when `expiring=1` is specified in the request.

### Step 3: Make authenticated requests

After your app has obtained an API access token, it can make authenticated requests to the GraphQL Admin API and fulfill incoming requests from the app frontend.

```terminal
curl -X POST \
  https://{shop}.myshopify.com/admin/api/2026-04/graphql.json \
  -H 'Content-Type: application/json' \
  -H 'X-Shopify-Access-Token: {access_token}' \
  -d '{
    "query": "{
      products(first: 5) {
        edges {
          node {
            id
            handle
          }
        }
        pageInfo {
          hasNextPage
        }
      }
    }"
  }'
```

---

## About online access tokens

> Fonte: https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/online-access-tokens

When creating an API access token for the GraphQL Admin API, you can select between offline and online access modes. Online access requires explicit request and links tokens to individual store users, with expiration matching the user's web session lifespan.

"Online access is meant to be used when a user is interacting with your app through the web, or when an app must respect an individual user's permission level."

### Example Use Cases

* Your app's security requirements specify short-lived access to a store. Tokens with online access mode expire either when the user logs out or after 24 hours.
* Your app differentiates between users that are logged in and those using the app. Tokens with online access mode have the same permissions as the user that's logged in.

### Installation

After your app is installed, requesting this access mode always returns an access token restricted to the scopes available to the user. The app can inspect `scope` and `associated_user_scope` to determine if a user is lacking certain permissions. When online access mode is requested and the app is not already installed on a store, the user installing the app must have access to all required scopes, or the installation fails.

### Authorization

"An API request made using an online mode access token is guaranteed to respect the user's individual permissions. Shopify returns a `403 Forbidden` status code when the access token is valid but the user does not have access."

App developers should make sure to handle such a response gracefully. After an access token has expired, Shopify returns a `401 Unauthorized` response code.

#### Best Practices

If your app implements caching to avoid fetching data from Shopify too often, then make sure to scope the cache to each individual user. Because online access mode is guaranteed to respect each user's permission level, not caching on a per-user basis could result in an inconsistent cache.

### Revoking Access

The access tokens created with the online access mode are temporary, and are guaranteed to expire after some time. After an access token has expired, Shopify returns a `401 Unauthorized` response code. Users can revoke their own access to your app at any time, without affecting the validity of other users' access tokens. When a user logs out of Shopify admin, all online mode access tokens created during the same web session are revoked.

---

## About offline access tokens

> Fonte: https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/offline-access-tokens

When you create an API access token for the GraphQL Admin API, you can choose between two access modes: offline and online. Offline is the default access mode when none is specified. Tokens with offline access mode are meant for service-to-service requests where no user interaction is involved. Offline access mode is ideal for background work in response to webhooks, or for maintenance work in backgrounded jobs.

### Expiring vs non-expiring offline tokens

As of December 2025, Shopify supports **expiring offline access tokens**, providing enhanced security through token rotation with a refresh token while maintaining the ability for apps to perform background operations without user interaction.

**Expiring token requirements for public apps:** Public apps must use expiring tokens for offline access. Public apps created on or after April 1, 2026 must use expiring tokens, and public apps created before April 1, 2026 must migrate to expiring tokens by January 1, 2027. Starting January 1, 2027, public apps that make REST or GraphQL Admin API requests with non-expiring tokens receive error responses. These requirements don't apply to custom apps or apps created by merchants.

#### Expiring offline tokens

Introduced in December 2025, expiring offline tokens provide enhanced security by allowing apps to regularly rotate access tokens using refresh tokens. Characteristics:

* **90-day refresh token lifetime**: A refresh token is provided in the response when obtaining new access tokens.
* **Token refresh**: Apps can refresh expired tokens without merchant intervention.
* **One refreshable expiring offline token per app and store**: When your app obtains a new expiring offline token, Shopify retires older expiring offline tokens for the same app and store. Retired access tokens remain valid until their `expires_in` duration ends, so requests in progress can complete. Their refresh tokens are invalidated immediately.

#### Non-expiring offline tokens

Prior to December 2025, non-expiring offline tokens were the default and only option for offline access. These tokens grant permanent access to a shop's data and can only be revoked through app uninstallation or secret revocation, making them less secure than expiring tokens. Characteristics:

* **No expiration**: Tokens remain valid indefinitely until app is uninstalled or secret revocation.
* **Acquiring offline tokens**: Getting offline tokens for the same shop and installation returns the same access token each time.

**Note:** Apps can migrate from non-expiring to expiring tokens using the token exchange grant. This is a one-time, irreversible migration per shop.

### Acquiring expiring offline tokens

Expiring offline tokens are supported in the different token acquisition flows.

#### Token exchange from session token

When using token exchange, include the `expiring=1` parameter:

```http
POST https://{shop}.myshopify.com/admin/oauth/access_token
```

| Parameter | Description |
| - | - |
| `client_id` (required) | The API key for the app. |
| `client_secret` (required) | The client secret for the app. |
| `grant_type` (required) | The value `urn:ietf:params:oauth:grant-type:token-exchange`. |
| `subject_token` (required) | An ID token that represents the identity and active browser session of a merchant using the app. |
| `subject_token_type` (required) | The value `urn:ietf:params:oauth:token-type:id_token`. |
| `requested_token_type` | The value `urn:shopify:params:oauth:token-type:offline-access-token` for requesting offline access tokens. |
| `expiring` | `0` (default) for a non-expiring offline token; `1` for an expiring offline token |

**Request:**

```terminal
curl -X POST \
  https://{shop}.myshopify.com/admin/oauth/access_token \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Accept: application/json' \
  -d 'client_id={client_id}' \
  -d 'client_secret={client_secret}' \
  -d 'grant_type=urn:ietf:params:oauth:grant-type:token-exchange' \
  -d 'subject_token={session_token}' \
  -d 'subject_token_type=urn:ietf:params:oauth:token-type:id_token' \
  -d 'requested_token_type=urn:shopify:params:oauth:token-type:offline-access-token' \
  -d 'expiring=1'
```

**Response:**

```json
{
  "access_token": "shpat_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "expires_in": 3600,
  "refresh_token": "shprt_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "refresh_token_expires_in": 7776000,
  "scope": "write_products,read_orders"
}
```

#### Authorization code grant

When exchanging an authorization code for an offline access token, include the `expiring=1` parameter:

```http
POST https://{shop}.myshopify.com/admin/oauth/access_token
```

| Parameter | Description |
| - | - |
| `client_id` (required) | The client ID for the app, as configured in the Dev Dashboard. |
| `client_secret` (required) | The client secret for the app, as configured in the Dev Dashboard. |
| `code` (required) | The authorization code provided in the redirect. |
| `expiring` | Only applicable if the initial authorize request was for an offline token. `0` (default) non-expiring; `1` expiring |

**Request:**

```terminal
curl -X POST \
  https://{shop}.myshopify.com/admin/oauth/access_token \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Accept: application/json' \
  -d 'client_id={client_id}' \
  -d 'client_secret={client_secret}' \
  -d 'code={authorization_code}' \
  -d 'expiring=1'
```

**Response:**

```json
{
  "access_token": "shpat_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "expires_in": 3600,
  "refresh_token": "shprt_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "refresh_token_expires_in": 7776000,
  "scope": "write_products,read_orders"
}
```

### Refreshing expiring offline tokens

When an expiring offline token expires, use the refresh token to obtain a new access token and refresh token.

```http
POST https://{shop}.myshopify.com/admin/oauth/access_token
```

| Parameter | Description |
| - | - |
| `client_id` (required) | The API key for the app. |
| `client_secret` (required) | The client secret for the app. |
| `grant_type` (required) | The value `refresh_token` indicates that a refresh token grant is being used. |
| `refresh_token` (required) | The refresh token received when the access token was issued. |

**Request:**

```terminal
curl -X POST \
  https://{shop}.myshopify.com/admin/oauth/access_token \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Accept: application/json' \
  -d 'client_id={client_id}' \
  -d 'client_secret={client_secret}' \
  -d 'grant_type=refresh_token' \
  -d 'refresh_token={refresh_token}'
```

**Response:**

```json
{
  "access_token": "shpat_yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy",
  "expires_in": 3600,
  "refresh_token": "shprt_zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",
  "refresh_token_expires_in": 7776000,
  "scope": "write_products,read_orders"
}
```

#### Refresh token behavior

* **New tokens on each refresh**: Shopify returns a new access token and a new refresh token.
* **Extended expiration**: The new refresh token has a new 90-day expiration from the refresh time.
* **Retired access token**: The previous access token remains valid until its `expires_in` duration ends, but you should use the new access token for new requests.
* **One-time use and retry behavior**: Shopify invalidates the previous refresh token after use. If your app doesn't receive a response from a refresh request, then retry the same request immediately with the same `refresh_token`. Shopify can return the same refreshed token response within a short retry window. After the short retry window, the previous `refresh_token` is invalid and can't be used again.

**Caution:** If the refresh token expires (after 90 days), then the app user needs to relaunch the app so that the app triggers the token acquisition flow.

### Migrating from non-expiring to expiring tokens

**Step 1: Update your app's session storage** — Add fields to store token expiration metadata: `expires_at`, `refresh_token`, `refresh_token_expires_at`.

**Step 2: Implement token refresh logic** — Before making API requests where no user interaction is involved, check if the offline access token has expired and refresh it if needed.

**Step 3: Start requesting expiring offline tokens** — For new installs, start acquiring expiring offline tokens, and persist the refresh token for refreshing.

**Step 4: Migrate existing tokens** — For installed shops with existing non-expiring tokens, perform the migration using token exchange. The migration can be done via a background job or during the next app launch.

**Caution:** The original non-expiring token will be revoked upon successful exchange. This migration is irreversible. To obtain a new non-expiring offline access token, the app would have to re-trigger the token acquisition flow with merchant interaction.

```http
POST https://{shop}.myshopify.com/admin/oauth/access_token
```

| Parameter | Description |
| - | - |
| `client_id` (required) | The API key for the app. |
| `client_secret` (required) | The client secret for the app. |
| `grant_type` (required) | The value `urn:ietf:params:oauth:grant-type:token-exchange`. |
| `subject_token` (required) | The non-expiring offline access token to migrate. |
| `subject_token_type` (required) | The value `urn:shopify:params:oauth:token-type:offline-access-token`. |
| `requested_token_type` (required) | The value `urn:shopify:params:oauth:token-type:offline-access-token`. |
| `expiring` (required) | Must be set to `1` to request an expiring offline token. |

**Request:**

```terminal
curl -X POST \
  https://{shop}.myshopify.com/admin/oauth/access_token \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Accept: application/json' \
  -d 'client_id={client_id}' \
  -d 'client_secret={client_secret}' \
  -d 'grant_type=urn:ietf:params:oauth:grant-type:token-exchange' \
  -d 'subject_token={non_expiring_offline_token}' \
  -d 'subject_token_type=urn:shopify:params:oauth:token-type:offline-access-token' \
  -d 'requested_token_type=urn:shopify:params:oauth:token-type:offline-access-token' \
  -d 'expiring=1'
```

**Response:**

```json
{
  "access_token": "shpat_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "expires_in": 3600,
  "refresh_token": "shprt_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "refresh_token_expires_in": 7776000,
  "scope": "write_products,read_orders"
}
```

---

## Implement authorization code grant manually

> Fonte: https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/authorization-code-grant

**Tip:** All Shopify app templates already have authorization code grant implemented. If you're using one of these templates, then you don't need to follow this tutorial.

This tutorial shows you how to install your app and acquire access tokens using authorization code grant, either using a Shopify Admin API library, or from scratch.

**Caution:** Apps rendered in the Shopify admin should use token exchange to acquire access tokens, and all apps should use Shopify managed installation. This guide is only relevant to standalone apps and legacy apps that aren't using Shopify managed installation.

### Requirements

* You've created an app that doesn't use a Shopify app template.
* You have your app's client credentials.
* You're familiar with the authorization code grant flow in Shopify.

### Step 1: Verify the installation request

When a user installs your app through the Shopify App Store or using an installation link, your app receives a `GET` request to the **App URL** path that you specify in the Dev Dashboard. The request includes the `shop`, `timestamp`, and `hmac` query parameters. You need to verify the authenticity of these requests using the provided `hmac` parameter.

To verify the request, you need to remove the `hmac` parameter from the query string and process it through an HMAC-SHA256 hash function. For a request to be valid, the `hmac` parameter must match the HMAC-SHA256 hash of the remaining parameters in the query string.

**Example query string:**

```text
"hmac=700e2dadb827fcc8609e9d5ce208b2e9cdaab9df07390d2cbca10d7c328fc4bf&shop={shop}.myshopify.com&timestamp=1337178173"
```

**Note:** The HMAC verification procedure for authorization code grant is different from the procedure for verifying webhooks.

**Before HMAC removal:**

```text
"code=0907a61c0c8d55e99db179b68161bc00&hmac=700e2dadb827fcc8609e9d5ce208b2e9cdaab9df07390d2cbca10d7c328fc4bf&shop={shop}.myshopify.com&state=0.6784241404160823&timestamp=1337178173"
```

**After HMAC removal:**

```text
"code=0907a61c0c8d55e99db179b68161bc00&shop={shop}.myshopify.com&state=0.6784241404160823&timestamp=1337178173"
```

The remaining parameters must be sorted alphabetically as strings, in the format `"parameter_name=parameter_value"`. Ruby example:

```ruby
digest = OpenSSL::Digest.new('sha256')
# The Shopify app's client secret, viewable in the Dev Dashboard. In a production environment, set the client secret as an environment variable to prevent exposing it in code
secret = 'my_client_secret'
message = 'code=0907a61c0c8d55e99db179b68161bc00&shop={shop}.myshopify.com&state=0.6784241404160823&timestamp=1337178173'


digest = OpenSSL::HMAC.hexdigest(digest, secret, message)
ActiveSupport::SecurityUtils.secure_compare(digest, "700e2dadb827fcc8609e9d5ce208b2e9cdaab9df07390d2cbca10d7c328fc4bf")
```

### Step 2: Request authorization code

Before an app can access any store data, it needs to acquire an access token. Your app begins the process by redirecting the user through the authorization code flow and retrieving an authorization code.

Your app should redirect the user through the authorization code flow if your app has verified the authenticity of the request and any of the following is true:

* Your app doesn't have a token for that shop.
* Your app uses online tokens and the token for that shop has expired.
* Your app has a token for that shop, but it was created before you rotated the app's secret.
* Your app has a token for that shop, but your app now requires scopes that differ from the scopes granted with that token.

#### Redirect to the authorization code flow

You can't perform a redirect from inside an iframe in the Shopify admin, due to `X-Frame-Options: DENY` restrictions on Shopify admin pages.

* If your app is never embedded, then perform a 3xx redirect to the grant screen.
* If your app can be embedded: check whether the app is being rendered in an iframe by checking the `embedded` parameter; if it is, escape the iframe using a Shopify App Bridge redirect action that redirects back to the same URL; then perform a 3xx redirect to the grant screen.

**Check for and escape the iframe (apps rendered in the Shopify admin only):**

1. Check your request query parameters for an `embedded` parameter. If present with a value of `1`, the request is being rendered in an iframe. If not present or `0`, use a 3xx redirect to the grant screen.
2. If `embedded=1`, then render a page that uses the Shopify App Bridge redirect action to redirect back to the same URL. This breaks your app out of the iframe so that you can redirect to the grant screen.

**Redirect using a 3xx redirect:**

```text
https://{shop}/admin/oauth/authorize?client_id={client_id}&scope={scopes}&redirect_uri={redirect_uri}&state={nonce}&grant_options[]={access_mode}
```

| Query parameter | Description |
| - | - |
| `{shop}` | The name of the user's shop. |
| `{client_id}` | The client ID for the app. |
| `{scopes}` | A comma-separated list of scopes. For example, `scope=write_products,read_shipping`. You should include every scope your app needs. Any permission to write a resource includes the permission to read it. Some data is considered protected customer data. This parameter should be omitted if you've pushed requested API access scopes with the TOML file. |
| `{redirect_uri}` | The URL to which a user is redirected after authorizing the app. The complete URL specified here must be added to your app as an allowed redirection URL, as configured in the Dev Dashboard. |
| `{nonce}` | A randomly selected value provided by your app that is unique for each authorization request. During the OAuth callback, your app must check that this value matches the one you provided during authorization. |
| `{access_mode}` | Sets the access mode. For an online access token, set to `per-user`. For an offline access token, omit this parameter. |

During the redirect, set a signed cookie with the `nonce` value from the URL.

**Note:** Most API access scopes can be requested using your app's `.env` or TOML file. However, in some cases, you must request specific permission to access data from the user in the Dev Dashboard.

### Step 3: Validate authorization code

After processing your request, Shopify redirects the user to your app's server:

```text
https://example.org/some/redirect/uri?code={authorization_code}&hmac=da9d83c171400a41f8db91a950508985&host={base64_encoded_hostname}&shop={shop_origin}&state={nonce}&timestamp=1409617544
```

**Security checks** — verify the following (if any fails, reject the request):

* The `nonce` is the same one that your app provided to Shopify, and the signed cookie value equals the `nonce` value in the `state` parameter.
* The `hmac` is valid and signed by Shopify.
* The `shop` parameter is a valid shop hostname, ends with `myshopify.com`, and doesn't contain characters other than letters (a-z), numbers (0-9), periods, and hyphens.

Regular expression to match the hostname form `https://{shop}.myshopify.com/`:

```regex
/^https?\:\/\/[a-zA-Z0-9][a-zA-Z0-9\-]*\.myshopify\.com\/?/
```

To match `{shop}.myshopify.com`:

```regex
/^[a-zA-Z0-9][a-zA-Z0-9\-]*\.myshopify\.com/
```

### Step 4: Get an access token

**Tip:** Shopify's API libraries can retrieve an access token by default.

```http
POST https://{shop}.myshopify.com/admin/oauth/access_token
```

| Parameter | Description |
| - | - |
| `client_id` (required) | The client ID for the app, as configured in the Dev Dashboard. |
| `client_secret` (required) | The client secret for the app, as configured in the Dev Dashboard. |
| `code` (required) | The authorization code provided in the redirect. |
| `expiring` | Only applicable if the initial authorize request was for an offline token. `0` (default) for an offline token without expiry; `1` for an expiring offline token. |

**Default request:**

```terminal
curl -X POST \
  https://{shop}.myshopify.com/admin/oauth/access_token \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Accept: application/json' \
  -d 'client_id={client_id}' \
  -d 'client_secret={client_secret}' \
  -d 'code={authorization_code}'
```

**Expiring offline token request:**

```terminal
# Only applicable if the initial https://{shop}/admin/oauth/authorize request was for an offline token
curl -X POST \
  https://{shop}.myshopify.com/admin/oauth/access_token \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Accept: application/json' \
  -d 'client_id={client_id}' \
  -d 'client_secret={client_secret}' \
  -d 'code={authorization_code}' \
  -d 'expiring=1'
```

**Response — Online access token:**

```json
{
  "access_token": "f85632530bf277ec9ac6f649fc327f17",
  "scope": "write_orders,read_customers",
  "expires_in": 86399,
  "associated_user_scope": "write_orders",
  "associated_user": {
    "id": 902541635,
    "first_name": "John",
    "last_name": "Smith",
    "email": "john@example.com",
    "email_verified": true,
    "account_owner": true,
    "locale": "en",
    "collaborator": false
  }
}
```

**Response — Expiring offline access token:**

```json
{
  "access_token": "f85632530bf277ec9ac6f649fc327f17",
  "scope": "write_orders,read_customers",
  "expires_in": 3600,
  "refresh_token": "shprt_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "refresh_token_expires_in": 7776000
}
```

**Response — Non-expiring offline access token:**

```json
{
  "access_token": "f85632530bf277ec9ac6f649fc327f17",
  "scope": "write_orders,read_customers"
}
```

**Confirm the requested scopes:** Due to the nature of OAuth, it's possible for an app user to change the requested scope in the URL during the authorize phase, so the app should ensure that all required scopes are granted before using the access token. If you requested both read and write for a resource, check only for the write scope (read is implied by write).

### Step 5: Redirect to your app's UI

If your app is embedded, and the `embedded` parameter isn't present or is equal to `0`, then you should `3xx` redirect to the App Home URL. If your app is never embedded, or `embedded=1`, then you should `3xx` redirect to your app URL.

**Node:**

```javascript
if (Shopify.Context.IS_EMBEDDED_APP && req.query.embedded !== "1") {
  const embeddedUrl = Shopify.Utils.getEmbeddedAppUrl(req);

  return res.redirect(embeddedUrl + req.path);
} else {
  const host = Shopify.Utils.sanitizeHost(req.query.host);

  return res.redirect(`/?shop=${session.shop}&host=${encodeURIComponent(host)}`);
}
```

**Ruby:**

```ruby
if ShopifyAPI::Context.embedded? && params[:embedded] != "1"
  embedded_url = ShopifyAPI::Auth.embedded_app_url(params[:host])

  redirect_to(embedded_url)
else
  redirect_to("/?shop=#{session.shop}&host=#{params[:host]}")
end
```

If you redirect to your app URL, then make sure to include the `shop` and `host` parameters. Without these, App Bridge can't initialize and your UI can't get a session token. Construct the App Home URL using Shopify Admin API libraries, or manually:

```url
https://{base64_decode(host)}/apps/{api_key}/
```

**Note:** The `host` variable is base64-encoded and then the padding characters (`=`) are removed. Some base64 decoders like Node.js can handle the lack of padding, and others like Python can't.

### Step 6: Make authenticated requests

```terminal
curl -X POST \
  https://{shop}.myshopify.com/admin/api/2026-04/graphql.json \
  -H 'Content-Type: application/json' \
  -H 'X-Shopify-Access-Token: {access_token}' \
  -d '{
    "query": "{
      products(first: 5) {
        edges {
          node {
            id
            handle
          }
        }
        pageInfo {
          hasNextPage
        }
      }
    }"
  }'
```

An authenticated request might fail if your app is requesting data not permitted by the scope, or the online token has expired. In these cases, redirect to the grant screen (escaping the iframe first if embedded).

### Manage Access Scopes

To change scopes, redirect the user to the app authorization link and request authorization of new permissions:

```text
https://{shop}.myshopify.com/admin/oauth/authorize
```

This URL might change in the future; construct it using a Shopify Admin API library where possible.

---

## Using the client credentials grant

> Fonte: https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/client-credentials-grant

The client credentials grant is an OAuth 2.0 flow where your app exchanges its own client ID and client secret directly with a store in which it's installed to obtain an access token, without any end-user interaction (RFC 6749, section 4.4). Use this for trusted, server-to-server integrations owned by your organization (for example, internal automation or back-office services).

Client credentials is only available for apps developed by your own organization and installed in stores that you own. Public or custom apps must use token exchange or authorization code flows.

### Requirements

* You've configured access scopes for your app (in the Dev Dashboard when creating an app version, or in your app's TOML configuration file).
* You've installed your app into a store. You need to acquire an access token for each store in which the app is installed.

### Step 1: Get your client credentials from the Dev Dashboard

Your app's client credentials are on the **Settings** page. You'll need the **Client ID** and **Secret**.

**Caution:** The client secret is sensitive information. Don't expose it in your app's frontend code or in your code repositories. If you suspect that your client secret has been compromised, you must rotate it immediately.

### Step 2: Get an access token

```text
POST https://{shop}.myshopify.com/admin/oauth/access_token
```

| Parameter | Description |
| - | - |
| `client_id` | The client ID for the app. |
| `client_secret` | The client secret for the app. |
| `grant_type` | This must always be set to `client_credentials`. |

**Request:**

```terminal
curl -X POST \
  "https://{shop}.myshopify.com/admin/oauth/access_token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials" \
  -d "client_id={client_id}" \
  -d "client_secret={client_secret}"
```

**Response:**

```json
{
  "access_token": "f85632530bf277ec9ac6f649fc327f17",
  "scope": "write_orders,read_customers",
  "expires_in": 86399
}
```

**Offline access token response values:**

| Value | Description |
| - | - |
| `access_token` | An API access token that can be used to access the shop's data as long as your app is installed. |
| `scope` | The list of access scopes that were granted to your app and are associated with the access token. |
| `expires_in` | The number of seconds until the access token expires. This is always set to 86399 (24 hours). |

### Step 3: Refresh the access token

Access tokens are valid for 24 hours, after which they must be refreshed. To refresh, your app must make the same request to the token endpoint with the client credentials as in the previous step.

---

## Enable Shopify-managed installations

> Fonte: https://shopify.dev/docs/apps/build/authentication-authorization/app-installation

Shopify managed installation is an installation method where Shopify installs an app and updates its access scopes without making any calls to the app. Advantages:

* **Improved performance**: "No browser redirects during installation or updates."
* **Less complexity**: "Apps rendered in the Shopify admin can use token exchange to acquire access tokens, and will no longer need to implement authorization code grant for installation or access scope changes."
* **Improved user experience**: "Faster installations and updates, and no screen flickering."

To enable Shopify managed installation, you need to share the scopes that your app requires in a configuration file that you push to Shopify. If you don't use this method, then your app will use authorization code grant, and call your app to determine the required access scopes before proceeding.

### Step 1: Configure your app using Shopify CLI

You can configure your app locally using a TOML file with Shopify CLI.

### Step 2: Deploy your configuration to Shopify

```toml
name = "Example App"
client_id = "a61950a2cbd5f32876b0b55587ec7a27"
application_url = "https://www.app.example.com/"
embedded = true


[access_scopes]
scopes = "read_orders"


# other fields omitted for brevity
```

Update the `scopes` field to include the access scopes that your app requires:

```toml
name = "Example App"
client_id = "a61950a2cbd5f32876b0b55587ec7a27"
application_url = "https://www.app.example.com/"
embedded = true


[access_scopes]
scopes = "read_orders,write_customers"


# other fields omitted for brevity
```

Then deploy:

```terminal
shopify app deploy
```

### Step 3: Shopify now manages installing your app and access scope changes

After you deploy your app configuration with your updated scopes, Shopify handles installation and scope updates whenever you deploy changes to your configuration.

### Step 4: Acquire access tokens to make authenticated requests to Shopify APIs

Apps rendered in the Shopify admin using Shopify managed install should acquire access tokens through token exchange. Standalone apps should use the authorization code grant flow.

---

## Manage access scopes

> Fonte: https://shopify.dev/docs/apps/build/authentication-authorization/app-installation/manage-access-scopes

After you've enabled Shopify managed install, you can manage your app's access scopes.

**Note:** If you're still using the legacy installation and OAuth authorization code grant flow, then refer to the authorization code grant guide on managing access scopes instead.

### Access scope configurations

| Configuration | Description |
| --- | --- |
| `scopes` | These configured access scopes are mandatory when merchants install your app with Shopify managed install. Merchants **must** grant access before your app can be installed. Your app is guaranteed to have these access scopes after it's installed on the merchant's store. |
| `optional_scopes` | Unlike required scopes, optional scopes can only be requested by the app post-installation. When requested, merchants have the option to grant access to these scopes, or to decline them. Merchants can also revoke previously granted optional scopes. Optional scopes are useful if you want to provide certain features to different stores, without forcing every app install to provide the same data access. |

**Scopes** (required) — defined in the `scopes` field:

```toml
name = "Example App"
client_id = "a61950a2cbd5f32876b0b55587ec7a27"
application_url = "https://www.app.example.com/"
embedded = true

[access_scopes]
scopes = "read_discounts,write_products"
```

**Optional scopes** — defined in the `optional_scopes` field:

```toml
name = "Example App"
client_id = "a61950a2cbd5f32876b0b55587ec7a27"
application_url = "https://www.app.example.com/"
embedded = true

[access_scopes]
scopes = "" # The `scopes` field is still necessary, but can be empty.
optional_scopes = ["read_discounts", "write_products"]
```

### Modify declared scopes

1. Modify the `scopes` or `optional_scopes` fields in your app's TOML file.
2. Deploy: `shopify app deploy`
3. (Optional) Subscribe to the `app/scopes_update` topic to receive webhooks when the granted scopes are updated.

**Modifying the `scopes` field:**

* Merchants will be prompted to approve the updated access scopes when they open your app. The `app/scopes_update` webhook will be triggered when the merchant approves the access scope changes.
* If the change is a reduction of scopes, the merchant won't be prompted and the app will lose access to the scopes automatically when the merchant opens the app. The `app/scopes_update` webhook will be triggered when the user opens the app.

**Modifying the `optional_scopes` field:**

* Your app can now start requesting the new access scopes.
* The granted access scopes for your app installation won't change until your app requests for the new access scopes dynamically and the merchant grants your app access. The `app/scopes_update` webhook will be triggered when the merchant approves the access scope changes.

**Moving a scope between `scopes` and `optional_scopes`:** If you move a scope from `scopes` to `optional_scopes`, stores that already granted the scope while it was required keep it (no re-prompt). New installations don't receive the scope until your app requests it dynamically. A required scope can't implicitly grant an optional one. For example, `write_products` grants `read_products`, so declaring `read_products` as optional while `write_products` is still required fails deploy with:

```text
Declared optional_scopes [read_products] cannot be implicit required scopes.
```

### Query currently granted scopes

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

**Response:**

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

Helper methods: App Bridge API `shopify.scopes.query()`; React Router API `scopes.query()`.

### Request new access scopes dynamically

**Note:** You can only request additional access scopes dynamically if they are configured as `optional_scopes` in your app's TOML file, and if the configuration changes have been deployed.

**Using the App Bridge API** (apps rendered in the Shopify admin):

```javascript
shopify.scopes.request(['read_discounts', 'write_products']);
```

This asynchronous, client-side method displays a permission grant modal for the access scopes requested, on top of your running app, with no browser redirect.

**Using a request URL for standalone apps:**

```text
https://admin.shopify.com/store/{STORE_NAME}/oauth/install?client_id={CLIENT_ID}&optional_scopes={REQUESTED_SCOPES}
```

| Query parameter | Description |
| --- | --- |
| `STORE_NAME` | The name of the merchant's store |
| `CLIENT_ID` | The app's client ID |
| `REQUESTED_SCOPES` | A comma separated list of access scopes to request. This must be a subset of the declared `optional_scopes` in your TOML file. |

Example:

```text
https://admin.shopify.com/store/my-cool-store/oauth/install?client_id=a61950a2cbd5f32876b0b55587ec7a27&optional_scopes=read_discounts,write_products
```

### Revoke granted scopes dynamically

**Note:** Only scopes configured as `optional_scopes` and that were dynamically granted can be revoked.

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

**Response:**

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

Helper methods: App Bridge API `shopify.scopes.revoke()`; React Router API `scopes.revoke()`.

---

## Generate access tokens for custom apps in the Shopify admin

> Fonte: https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/generate-app-access-tokens-admin

**Caution:** You can no longer create new custom apps in the Shopify admin. Existing admin-created custom apps continue to work. To create a new custom app, use the Dev Dashboard or Shopify CLI.

You can create a custom app for a store directly in the Shopify admin. To authenticate an admin-created custom app, you or the app user needs to install the app from the Shopify admin to generate API credentials and the necessary API access tokens.

### Step 1: Create and install the app

You or the user can create and install a custom app in the Shopify admin by following the Custom apps documentation on the Shopify Help Center.

### Step 2: Make authenticated requests

```terminal
curl -sX POST \
  https://{shop}.myshopify.com/admin/api/2026-04/graphql.json \
  -H 'Content-Type: application/json' \
  -H "X-Shopify-Access-Token: ${SHOP_TOKEN}" \
  -d @- <<EOF
{
  "query": "{
    products(first: 5) {
      edges {
        node {
          id
          handle
        }
      }
      pageInfo {
        hasNextPage
      }
    }
  }"
}
EOF
```

Using `jq` to parse:

```terminal
curl -sX POST \
  https://{shop}.myshopify.com/admin/api/2026-04/graphql.json \
  -H 'Content-Type: application/json' \
  -H "X-Shopify-Access-Token: ${SHOP_TOKEN}" \
  -d @- <<EOF | jq '.data.products.edges[].node | {id, handle}'
{
  "query": "{
    products(first: 5) {
      edges {
        node {
          id
          handle
        }
      }
      pageInfo {
        hasNextPage
      }
    }
  }"
}
EOF
```

Output:

```json
{
  "id": "gid://shopify/Product/10079467700516",
  "handle": "the-draft-snowboard"
}
{
  "id": "gid://shopify/Product/10079467733284",
  "handle": "the-archived-snowboard"
}
{
  "id": "gid://shopify/Product/10079467766052",
  "handle": "the-hidden-snowboard"
}
```

### Rotating API credentials

You can't rotate API credentials for custom apps created in the Shopify admin. You need to delete the app and create a new custom app which has new API credentials. To create new access tokens, uninstall and reinstall your app.

**Caution:** Your app's requests and webhooks are disrupted until you update your app's code with the new API credentials or access token.

### Permissions required to assign scopes to a custom app

Anyone with a staff or collaborator account can change what store resources an admin-created custom app can access, only if they have the **Manage and install apps and channels** permission, the **Develop apps** permission, and the relevant permissions for the respective store resource.

| Admin API scope name | Permissions required for the staff or collaborator account |
|---|---|
| `read_analytics` | View store metrics |
| `read_assigned_fulfillment_orders`, `write_assigned_fulfillment_orders` | View or manage fulfillment orders |
| `read_customer_merge`, `write_customer_merge` | View or manage customer profile merges |
| `read_customers`, `write_customers` | View or manage customers, customer addresses, order history, and customer groups |
| `read_discounts`, `write_discounts` | View or manage automatic discounts and discount codes |
| `read_draft_orders`, `write_draft_orders` | View or manage orders created by app users on behalf of customers |
| `read_files`, `write_files` | View or manage files |
| `read_fulfillments`, `write_fulfillments` | View or manage fulfillment services |
| `read_gdpr_data_request` | View GDPR data requests |
| `read_gift_cards`, `write_gift_cards` | View or manage gift cards (Available to Plus merchants only) |
| `read_inventory`, `write_inventory` | View or manage inventory across multiple locations |
| `read_legal_policies`, `write_legal_policies` | View or manage a shop's legal policies |
| `read_locations` | View the geographic location of stores, headquarters, and warehouses |
| `read_marketing_events`, `write_marketing_events` | View or manage marketing events and engagement data |
| `read_merchant_managed_fulfillment_orders`, `write_merchant_managed_fulfillment_orders` | View or manage fulfilment orders assigned to merchant-managed locations |
| `read_metaobject_definitions`, `write_metaobject_definitions` | View or manage metaobject definitions |
| `read_metaobjects`, `write_metaobjects` | View or manage metaobject entries |
| `read_online_store_navigation` | View menus for display on the storefront |
| `read_online_store_pages`, `write_online_store_pages` | View or manage Online Store pages |
| `read_order_edits`, `write_order_edits` | View or manage edits to orders |
| `read_orders`, `write_orders`, `read_all_orders` | View or manage orders, transactions, fulfillments, and abandoned checkouts from the last 60 days, or View all past and future orders |
| `read_price_rules`, `write_price_rules` | View or manage conditional discounts |
| `read_products`, `write_products` | View or manage products, variants, and collections |
| `read_product_listings`, `write_product_listings` | View or manage product or collection listings |
| `read_reports`, `write_reports` | View or manage reports on the **Reports** page in the Shopify admin |
| `read_resource_feedbacks`, `write_resource_feedbacks` | View or manage the status of shops and resources |
| `read_script_tags`, `write_script_tags` | View or manage the JavaScript code in storefront or orders status pages |
| `read_shipping`, `write_shipping` | View or manage shipping carriers, countries, and provinces |
| `read_shopify_payments_accounts` | View Shopify Payments accounts |
| `read_shopify_payments_bank_accounts` | View bank accounts that can receive Shopify Payments payouts |
| `read_shopify_payments_disputes` | View Shopify Payment disputes raised by buyers |
| `read_shopify_payments_payouts` | View Shopify Payments payouts and the account's current balance |
| `read_content`, `write_content` | View or manage articles, blogs, comments, pages, and redirects |
| `read_themes`, `write_themes` | View or manage theme templates and assets |
| `read_third_party_fulfillment_orders`, `write_third_party_fulfillment_orders` | View or manage fulfillment orders assigned to a location managed by any fulfillment service |
| `read_translations`, `write_translations` | View or manage content that can be translated |

---

## Shopify API access scopes (full list)

> Fonte: https://shopify.dev/docs/api/usage/access-scopes

All apps need to request access to specific store data during the app authorization process. This guide provides a list of available access scopes for the GraphQL Admin, Storefront, Payment Apps APIs, and Customer Account APIs.

### How it works

After you've generated API credentials, your app needs to "be authorized to access store data." An app can request authenticated or unauthenticated access scopes.

| Scope type | Description | Example use cases |
| - | - | - |
| Authenticated | Controls access to resources in the GraphQL Admin API, Web Pixel API, and Payments Apps API. Authenticated access is intended for interacting with a store on behalf of a user. | Creating products; Managing discount codes |
| Unauthenticated | Controls an app's access to Storefront API objects. Unauthenticated access is intended for interacting with a store on behalf of a customer. | Viewing products; Initiating a checkout |
| Customer | Controls an app's access to Customer Account API objects. Customer access is intended for interacting with data that belongs to a customer. | Viewing orders; Updating customer details |

### Authenticated access scopes

Access to some resources are marked **permissions required** — you must request specific permission to access data from the user in your Partner Dashboard.

| Scope | Access |
| - | - |
| `read_all_orders` | All relevant orders rather than the default window of orders created within the last 60 days. **permissions required**. Used in conjunction with existing order scopes (`read_orders` or `write_orders`). |
| `write_app_proxy` | Allows your app to use app proxies. |
| `read_assigned_fulfillment_orders`, `write_assigned_fulfillment_orders`, `read_merchant_managed_fulfillment_orders`, `write_merchant_managed_fulfillment_orders`, `read_third_party_fulfillment_orders`, `write_third_party_fulfillment_orders`, `read_marketplace_fulfillment_orders` | `FulfillmentOrder`. As of API version 2024-10, `write_third_party_fulfillment_orders` will no longer allow order management apps to create fulfillments for fulfillment orders assigned to a different fulfillment service app. |
| `read_cart_transforms`, `write_cart_transforms` | `CartTransform` |
| `read_checkout_branding_settings`, `write_checkout_branding_settings` | `CheckoutBranding` |
| `read_checkout_and_accounts_configurations`, `write_checkout_and_accounts_configurations` | `CheckoutAndAccountsConfiguration` |
| `read_content`, `write_content`, `read_online_store_pages` | `Article`, `Blog`, `Comment`, `Page` |
| `read_customer_events`, `write_pixels` | Web Pixels API |
| `read_customer_merge`, `write_customer_merge` | `CustomerMergePreview`, `CustomerMergeRequest` |
| `read_customer_payment_methods` | `CustomerPaymentMethod` **permissions required** |
| `read_customers`, `write_customers` | `Customer`, `Segment`, `Company`, `CompanyLocation` |
| `read_delivery_customizations`, `write_delivery_customizations` | `DeliveryCustomization` |
| `read_discounts`, `write_discounts` | Discounts features |
| `read_draft_orders`, `write_draft_orders` | `DraftOrder` |
| `read_files`, `write_files` | `GenericFile` |
| `read_fulfillments`, `write_fulfillments` | `FulfillmentService` |
| `read_gift_cards`, `write_gift_cards` | `GiftCard` |
| `read_inventory`, `write_inventory` | `InventoryLevel`, `InventoryItem` |
| `read_legal_policies` | `ShopPolicy` |
| `read_locales`, `write_locales` | `ShopLocale` |
| `read_locations`, `write_locations` | `Location` |
| `read_markets`, `write_markets` | `Market` |
| `read_marketing_events`, `write_marketing_events` | `MarketingEvent`, `MarketingActivity` |
| `read_merchant_approval_signals` | `MerchantApprovalSignals` |
| `read_metaobject_definitions`, `write_metaobject_definitions` | `MetaobjectDefinition` |
| `read_metaobjects`, `write_metaobjects` | `Metaobject` |
| `read_online_store_navigation`, `write_online_store_navigation` | `UrlRedirect` |
| `read_order_edits`, `write_order_edits` | `CalculatedOrder`, `DeliveryCarrierService` |
| `read_orders`, `write_orders` | `AbandonedCheckout`, `Fulfillment`, `Order`, `OrderTransaction`, `DeliveryCarrierService` |
| `read_own_subscription_contracts`, `write_own_subscription_contracts` | GraphQL Admin API `SubscriptionContract` **permissions required**; Customer Account API `SubscriptionContract` **permissions required** |
| `read_payment_customizations`, `write_payment_customizations` | `PaymentCustomization` |
| `read_payment_gateways`, `write_payment_gateways` | Payments Apps API `PaymentsAppConfiguration` |
| `read_payment_mandate`, `write_payment_mandate` | `PaymentMandate` |
| `write_payment_sessions` | Payments Apps API `PaymentSession`, `CaptureSession`, `RefundSession`, `VoidSession` |
| `read_payment_terms`, `write_payment_terms` | `PaymentSchedule`, `PaymentTerms` |
| `read_price_rules`, `write_price_rules` | `PriceRule` |
| `write_privacy_settings`, `read_privacy_settings` | `CookieBanner`, `PrivacySettings` |
| `read_products`, `write_products` | `Product`, `ProductVariant`, `Collection`, `ResourceFeedback`, `SellingPlan` (also requires `read_purchase_options` or `read_own_subscription_contracts` for queries, and `write_purchase_options` or `write_own_subscription_contracts` for mutations) |
| `read_reports` | Analytics and reporting data through the `shopifyqlQuery` query |
| `read_returns`, `write_returns` | `Return` |
| `read_script_tags`, `write_script_tags` | `ScriptTag` |
| `read_shipping`, `write_shipping` | `DeliveryCarrierService` |
| `read_shopify_payments_disputes` | `ShopifyPaymentsDispute` |
| `read_shopify_payments_dispute_evidences` | `ShopifyPaymentsDisputeEvidence` |
| `read_shopify_payments_payouts` | `ShopifyPaymentsPayout`, `ShopifyPaymentsBalanceTransaction` |
| `read_store_credit_accounts` | `StoreCreditAccount` |
| `read_store_credit_account_transactions`, `write_store_credit_account_transactions` | `StoreCreditAccountDebitTransaction`, `StoreCreditAccountCreditTransaction` |
| `read_themes`, `write_themes` | `OnlineStoreTheme` |
| `read_translations`, `write_translations` | `TranslatableResource`, `Translation` |
| `read_users` | `StaffMember` (Shopify Plus) |
| `read_validations`, `write_validations` | `Validation` |

#### Requesting specific permissions

**Orders permissions:** By default, you have access to the last 60 days' worth of orders. To access all orders, request the `read_all_orders` scope:

1. From the Partner Dashboard, go to **Apps**.
2. Click the name of your app.
3. Click **API access**.
4. In the **Access requests** section, on the **Read all orders scope** card, click **Request access**.
5. Describe your app and why you're applying for access.
6. Click **Request access**.

**Subscription APIs permissions:** Subscription apps let users sell subscription products that generate multiple orders on a billing frequency. Request the required protected access scopes:

1. From the Partner Dashboard, go to **Apps** → your app → **API access**.
2. In the **Access requests** section, on the **Access Subscriptions APIs** card, click **Request access**.
3. Describe why you're applying for access and click **Request access**.

If approved, you can add `read_customer_payment_methods` and `write_own_subscription_contracts` scopes (or `customer_read_own_subscription_contracts` / `customer_write_own_subscription_contracts` for the Customer Account API).

**Protected customer data permissions:** By default, apps don't have access to any protected customer data. To access it, you must meet the protected customer data requirements. You can add the relevant scopes, but the API won't return data from non-development stores until your app is configured and approved for protected customer data use.

### Unauthenticated access scopes

Unauthenticated access scopes provide apps with read-only access to the Storefront API.

| Scope | Access |
| - | - |
| `unauthenticated_read_checkouts`, `unauthenticated_write_checkouts` | `Cart` object |
| `unauthenticated_read_customers`, `unauthenticated_write_customers` | `Customer` object |
| `unauthenticated_read_customer_tags` | `tags` field on the `Customer` object |
| `unauthenticated_read_content` | Storefront content, such as `Article`, `Blog`, and `Comment` objects |
| `unauthenticated_read_metaobjects` | View metaobjects, such as `Metaobject` |
| `unauthenticated_read_product_inventory` | `quantityAvailable` field on the `ProductVariant` object and `totalAvailable` field on the `Product` object |
| `unauthenticated_read_product_listings` | `Product` and `Collection` objects |
| `unauthenticated_read_product_pickup_locations` | `Location` and `StoreAvailability` objects |
| `unauthenticated_read_product_tags` | `tags` field on the `Product` object |
| `unauthenticated_read_selling_plans` | Selling plan content on the `Product` object |

### Customer access scopes

Customer access scopes provide apps with read and write access to the Customer Account API.

| Scope | Access |
| - | - |
| `customer_read_customers`, `customer_write_customers` | `Customer` object |
| `customer_read_orders`, `customer_write_orders` | `Order` object |
| `customer_read_draft_orders` | `DraftOrder` object |
| `customer_read_markets` | `Market` object |
| `customer_read_metaobjects` | `Metaobject` object |
| `customer_read_store_credit_accounts` | `StoreCreditAccount` object |
| `customer_read_own_subscription_contracts`, `customer_write_own_subscription_contracts` | `SubscriptionContract` object for records that belong to your app |
| `customer_write_subscription_contracts` | `SubscriptionContract` object for all records. Only available for Hydrogen and Headless storefronts |
| `customer_read_companies`, `customer_write_companies` | `Company` object |
| `customer_read_locations`, `customer_write_locations` | `CompanyLocation` object |

### Checking granted access scopes

You can check your app's granted access scopes using the `appInstallation` query in the GraphQL Admin API.

### Limitations

* Apps should request only the minimum amount of data necessary. Shopify restricts access to scopes for apps that don't require legitimate use of the associated data.
* Only public or custom apps are granted access scopes. Legacy app types, such as private or unpublished, won't be granted new access scopes.

---

## About client credentials (client secrets)

> Fonte: https://shopify.dev/docs/apps/build/authentication-authorization/client-secrets

Your app's client credentials (client ID and client secret) authenticate your app when it requests access to a store's data. You can use these credentials to retrieve an access token for API requests or to verify that a webhook request is genuinely from Shopify.

### Retrieve your app's client credentials

1. Open the Dev Dashboard.
2. Click **Apps** and select your app.
3. Click **Settings**.
4. View or copy your client ID and secret.

### Use your credentials to get an access token

**Info:** If you're building apps for other merchants, use Shopify CLI, which handles authentication automatically.

```text
POST https://{shop}.myshopify.com/admin/oauth/access_token

Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials
&client_id={your_client_id}
&client_secret={your_client_secret}
```

**Response:**

```json
{
  "access_token": "shpat_xxxxx",
  "scope": "read_products,write_products",
  "expires_in": 86399
}
```

Include this token in the `X-Shopify-Access-Token` header when calling Shopify APIs. Tokens expire after 24 hours—request a new one when needed.

### Verify webhook requests

Use your client secret to verify that incoming webhook requests are genuinely from Shopify. Shopify signs each webhook request with an HMAC-SHA256 hash using your client secret. Your app should compute the same hash and compare it to the `X-Shopify-Hmac-Sha256` header.

### Rotate or revoke your app's client credentials

You should rotate the client credentials for your app on a regular basis. To learn how, refer to *Rotate or revoke client credentials*.

---

## Implement custom authorization

> Fonte: https://shopify.dev/docs/apps/build/authentication-authorization/implement-custom-authorization

This tutorial guides you through the process of implementing your own authorization flow for an app that is not created using the React Router app template. It covers:

* Configuring access scopes through the CLI for Shopify to manage your app's installation on stores.
* Retrieving and validating session tokens to authenticate a user.
* Exchanging the session token for API access tokens to make API queries.
* Post authorization tasks.

### Configure access scopes through the CLI

The Shopify CLI helps developers building new apps by providing app templates, previewing apps in a dev store, and managing app deployments and extensions.

**Shopify managed install:** After migrating your app to use Shopify CLI you would have: a `shopify.app.toml` file in your project directory; your app listed in the Dev Dashboard; and your app startable through the Shopify CLI (`shopify app dev`).

**Requesting and updating access scopes:** The access scopes configured in the app TOML file are registered on Shopify, and the installation of your app is managed by Shopify. Ensure you have `scopes` set in your TOML file, and `use_legacy_install_flow` is either removed or set to `false`. Update scopes by editing the TOML file and running `shopify app deploy`.

Example `shopify.app.toml`:

```toml
## Learn more about configuring your app at https://shopify.dev/docs/apps/tools/cli/configuration


client_id = "your-client-id"
name = "My Awesome app"
application_url = "https://this-is-not-real.yourapp"
embedded = true


[build]
automatically_update_urls_on_dev = true
dev_store_url = "your-dev-store-to-test.myshopify.com"
include_config_on_deploy = true


[access_scopes]
# Learn more at https://shopify.dev/docs/apps/tools/cli/configuration#access_scopes
scopes = "write_products, read_orders"


# Ensure that "use_legacy_install_flow" is set to false or is omitted from this TOML file to use Shopify managed installation.
use_legacy_install_flow = false


[auth]
redirect_urls = [
  "https://this-is-not-real.yourapp/auth/callback",
  "https://this-is-not-real.yourapp/auth/shopify/callback",
  "https://this-is-not-real.yourapp/api/auth/callback"
]


[webhooks]
api_version = "2024-01"


[pos]
embedded = false
```

### Authentication

Apps rendered in the Shopify admin must authenticate their incoming requests with session tokens. When the app is loaded through Shopify admin, a session token must be retrieved to validate that the user is authenticated. Session tokens are short lived (60 seconds) and must not be used for tracking session persistence. Always fetch the latest session token from the request header when handling requests.

The session token is available in 2 places: in the request header (`authorization: Bearer encoded_session_token`), and in the URL parameter (`id_token`).

Full reference implementation (`routes/auth.js`):

```javascript
var express = require('express');
var {shopifyApi, RequestedTokenType} = require('@shopify/shopify-api');


var router = express.Router();
const shopify = shopifyApi({
  apiKey: process.env.SHOPIFY_API_KEY,
  apiSecretKey: process.env.SHOPIFY_API_SECRET || '',
  apiVersion: 'unstable',
  appUrl: process.env.SHOPIFY_APP_URL || '',
  scopes: process.env.SCOPES?.split(','),
  hostScheme: process.env.HOST?.split('://')[0],
  hostName: process.env.HOST?.replace(/https?:\/\//, ''),
  isEmbeddedApp: true,
});


function getSessionTokenHeader(request) {
  return request.headers['authorization']?.replace('Bearer ', '');
}


function getSessionTokenFromUrlParam(request) {
  const searchParams = new URLSearchParams(request.url);


  return searchParams.get('id_token');
}


function redirectToSessionTokenBouncePage(req, res) {
  const searchParams = new URLSearchParams(req.query);
  // Remove `id_token` from the query string to prevent an invalid session token sent to the redirect path.
  searchParams.delete('id_token');


  // Using shopify-reload path to redirect the bounce automatically.
  searchParams.append(
    'shopify-reload',
    `${req.path}?${searchParams.toString()}`
  );
  res.redirect(`/session-token-bounce?${searchParams.toString()}`);
}


router.get('/session-token-bounce', async function (req, res, next) {
  res.setHeader("Content-Type", "text/html");
  // "process.env.SHOPIFY_API_KEY" is available if you use Shopify CLI to run your app.
  // You can also replace it with your App's Client ID manually.
  const html = `
  <head>
      <meta name="shopify-api-key" content="${process.env.SHOPIFY_API_KEY}" />
      <script src="https://cdn.shopify.com/shopifycloud/app-bridge.js"></script>
  </head>
  `;
  res.send(html);
});


router.get('/authorize', async function (req, res, next) {
  let encodedSessionToken = null;
  let decodedSessionToken = null;
  try {
    encodedSessionToken =
      getSessionTokenHeader(req) || getSessionTokenFromUrlParam(req);


    // "shopify" is an instance of the Shopify API library object,
    // You can install and configure the Shopify API library through: https://www.npmjs.com/package/@shopify/shopify-api
    decodedSessionToken = await shopify.session.decodeSessionToken(
      encodedSessionToken
    );
  } catch (e) {
    // Handle invalid session token error
    const isDocumentRequest = !request.headers.get("authorization");
    if (isDocumentRequest) {
      return redirectToSessionTokenBouncePage(req, res);
    }


    throw new Response(undefined, {
      status: 401,
      statusText: 'Unauthorized',
      headers: new Headers({
        'X-Shopify-Retry-Invalid-Session-Request': '1',
      }),
    });
  }


  const dest = new URL(decodedSessionToken.dest);
  const shop = dest.hostname;
  const accessToken = await shopify.auth.tokenExchange({
    shop,
    sessionToken: encodedSessionToken,
    requestedTokenType: RequestedTokenType.OnlineAccessToken, // or RequestedTokenType.OfflineAccessToken
  });


  res.setHeader("Content-Type", "text/html");
  const html = `
  <body>
    <h1>Retrieved access Token</h1>
    <p>${JSON.stringify(accessToken, null, 2)}</p>
  </body>`;
  res.send(html);
});


module.exports = router;
```

**Session token in the request header:** You must use App Bridge to get session tokens. If the App Bridge script is properly set up, it'll append a new header field `authorization` to your server requests automatically:

```json
{
  ...
  "authorization": "Bearer encoded_session_token",
  "accept-language": "...",
  "accept-encoding": "...",
  "accept": "*/*",
  "user-agent": "...",
  "host": "...",
  ...
}
```

**Session token in the URL parameter:** When Shopify admin loads your app path, it appends the session token to the URL:

```text
/my-app-path?embedded=1&hmac={HMAC_VALUE}&host={HOST}&id_token={ID_TOKEN}&locale=en&session={SESSION}&shop={SHOP}&timestamp={TIMESTAMP}
```

The encoded session token can be retrieved from the parameter field `id_token`.

**Critical:** There may not always be a session token in the URL because it might be lost or invalidated in server side redirects. It's recommended that you still have a fallback bounce page to get a session token from App Bridge.

**Bounce page to get a session token from App Bridge:** A bounce page loads the App Bridge script before redirecting back to your app's requested path. Add a bounce route that only renders an HTML response containing the App Bridge setup script (`/session-token-bounce`). When the session token isn't available in the request header or URL parameters, redirect to the bounce route. Use App Bridge's `shopify-reload` to reload your original route after App Bridge appends the session token. Add the `shopify-reload` parameter containing the path to reload (with original parameters minus `id_token`).

**Validate the session token:** After obtaining the session token, decode and verify that the request is made by an authenticated user. Use the Shopify API library (`session.decodeSessionToken`), which throws an error if validation fails. In cases when the session token has become invalid because app scopes have changed or it has expired, refresh in one of two ways: for a document request, redirect to the bounce page; for an XHR request, send a `401 Unauthorized` response with the `X-Shopify-Retry-Invalid-Session-Request` header. App Bridge will intercept the request, refresh the session token, and retry the request once.

**Do's and don'ts for session tokens:**

Do:
* ✅ Validate session tokens on every request.
* ✅ Only continue request operation if session token is valid and active.
* ✅ Exchange the session token for an access token for API queries.

Don't:
* ❌ Use session tokens for session persistence (60-second expiry).
* ❌ Depend on session token from the URL params as your main validation method. It's ok for the initial server side rendering request, but subsequent requests should go through App Bridge and be validated through the session token from the request header.

### Authorization

Authorization begins when the user installs the app by granting a set of permissions requested by the app. The next step is to obtain an access token to be used for making queries to Shopify APIs. There are 2 types of access tokens: online access tokens and offline access tokens.

**Token Exchange:** Use the authorization API to exchange a session token for an access token based on the access scopes granted by the user. Use the Shopify API library method `auth.tokenExchange` to avoid implementing your own token exchange method.

**Do's and don'ts for access tokens:**

Do:
* ✅ Use a storage method to persist the access token retrieved from token exchange.
* ✅ Check for access token's existence or validity in session storage before performing another token exchange.

Don't:
* ❌ Perform token exchange on every request. Access tokens may expire depending on their type.
* ❌ Share the access token with others.

### Post authorization tasks

Now that the app has a valid access token, it can use the access token to make authenticated API requests (add the access token as `X-Shopify-Access-Token` header). For a new install, perform:

1. **Subscribing to webhooks:** Webhooks notify your app when something changes in a shop. If you created a React Router app from the Shopify CLI, then your app will automatically register the default webhook `APP_UNINSTALLED` after installation, to clean up session data from the database when an app is uninstalled.
2. **Session storage:** Don't exchange tokens on every request. The access token should be persisted after the exchange. If you created a React Router app from the Shopify CLI, then your app will automatically store and load a session during the authentication/authorization process (using the `shopify-app-session-storage-prisma` library by default).

---
