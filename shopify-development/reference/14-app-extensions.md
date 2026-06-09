# 14. App Extensions

Le **app extensions** permettono a un'app di aggiungere le proprie funzionalità direttamente nelle interfacce di Shopify (admin, checkout, customer accounts, POS, online store/theme, Flow, ecc.) senza che l'utente debba abbandonare il contesto in cui sta lavorando. Questo capitolo raccoglie in modo fedele la documentazione ufficiale di Shopify sui **tipi di estensione** e sulle relative **guide** (concetti, getting-started, configurazione, targets/extension points e panoramica dei componenti).

Per ogni tipo di estensione vengono catturati per intero: la panoramica, il getting-started, la configurazione e le pagine sui targets/extension points. Le reference per-componente auto-generate (es. ogni singolo componente Checkout/Admin/POS/Customer Account UI con la sua prop table) sono enormi: per quelle, viene catturata la pagina indice/overview e gli URL delle reference per-componente vengono elencati (non estratti) nella sezione `## Pagine aggiuntive (URL elencati, non estratti)` in fondo al capitolo.

**Mini-indice del capitolo:**

- [Panoramica generale (App extensions)](#panoramica-generale)
- [Admin UI extensions](#admin-ui-extensions)
- [App Home UI extensions](#app-home-ui-extensions)
- [Checkout UI extensions](#checkout-ui-extensions)
- [Customer account UI extensions](#customer-account-ui-extensions)
- [POS UI extensions](#pos-ui-extensions)
- [Theme app extensions (il ponte verso i temi)](#theme-app-extensions)
- [Web Pixel extensions](#web-pixel-extensions)
- [Shopify Flow extensions](#shopify-flow-extensions)
- [Marketing activities extensions](#marketing-activities-extensions)
- [Pagine aggiuntive (URL elencati, non estratti)](#pagine-aggiuntive-url-elencati-non-estratti)

---

## Panoramica generale

Mini-TOC:
- [App extensions (overview)](#app-extensions-overview)
- [List of app extensions](#list-of-app-extensions)
- [Configure app extensions](#configure-app-extensions)
- [Build an extension-only app](#build-an-extension-only-app)
- [Remove an app extension](#remove-an-app-extension)

### App extensions (overview)

> Fonte: https://shopify.dev/docs/apps/build/app-extensions

# App extensions

An app extension enables you to add your app's functionality to Shopify user interfaces. This guide introduces app extensions and how they work.

---

## How it works

An app extension surfaces the functionality of your app where and when users need it most. App extensions are useful for apps that require quick, frequent actions from users.

For example, your app's actions can appear as dropdown items in Shopify admin for orders, products, customers, and other resources. You can produce interfaces that easily mimic the Shopify look-and-feel, and make your app seamlessly appear in Shopify Point of Sale (POS). Extensions can also render a main page for your app in the App Home area of Shopify admin, giving extension-only apps a Shopify-hosted landing page with no backend required.

### Without an app extension

Without an app extension, users interact directly with your app. Your app relays information to Shopify that gets surfaced back to the users through your app:

![An example of an app interacting with a users without an app extension](https://shopify.dev/assets/assets/images/api/app-extensions-overview-without-DjGHfpdv.png)

### With an app extension

With an app extension, users interact with Shopify. Shopify relays information to your app that gets surfaced back to the users through your app extension in Shopify:

![An example of an app interacting with a user with an app extension](https://shopify.dev/assets/assets/images/api/app-extensions-overview-with-LWTIK-zM.png)

**Note:**

"An app extension isn't an app. It's a mechanism that lets an app add features to certain defined parts of several Shopify user interfaces." Apps that use extensions must adhere to the same authentication requirements and rate limits as apps that don't use extensions.

---

## Creating app extensions

You can create app extensions using Shopify CLI and the `app generate extension` command.

For information about building and previewing app extensions, refer to the documentation for your extension type.

### Extension-only apps

Extension-only apps are made up entirely of extensions, so you can host them on Shopify with no developer-hosted backend. The extension-only template now includes an App Home UI extension by default, which renders the app's main page in App Home.

**Note:**

Extension-only apps can only be installed with custom distribution.

Learn about extension-only apps that don't require a web server.

---

## Configuring app extensions

When you generate an app extension, a TOML configuration file named `shopify.extension.toml` is automatically generated in your app's extension directory. The TOML file is located in the `extensions/` directory of your app project.

For information about the properties that you can configure in the TOML file, refer to Configuring app extensions.

---

## Versioning and deployment

Your app configuration and all extensions are versioned together as a single app version.

When you run the `deploy` command using Shopify CLI, an app version is created and released. You can revert to a previous app version at any time. You can also create an app version from the Dev Dashboard.

Releasing an app version replaces the current active version that's served to stores that have your app installed. It might take several minutes for app users to be upgraded to the new version.

Learn how to deploy extensions.

Polaris reference docs follow Shopify's API versioning policy. Each stable version is supported for a minimum of 12 months. Older versions continue to work, they just won't have dedicated docs on Shopify.dev. Shopify CLI already prevents deploys targeting API versions older than 12 months, so we recommend keeping your extensions on a supported version.

---

## Reviews and approvals

Some app extensions need to be reviewed and approved before they're released to users.

If an app extension needs to be reviewed, then you can't release the related app version until you submit it for review and it's been approved.

To learn whether your extension type needs to be reviewed, refer to the list of extension types.

---

## Removing app extensions

If you no longer want users to use an app extension, or you want to temporarily disable an app extension, then you can remove it.

Learn how to remove an app extension from your app.

---

## Analyzing bundle size

"UI extensions have a strict 64 KB compressed size limit." When you run `shopify app build` with Shopify CLI version 3.92.0 or higher, an esbuild metafile (`.metafile.json`) is emitted in each extension's `dist/` folder. You can use this file to analyze what's contributing to your bundle size.

To visualize the metafile, upload it to the esbuild bundle analyzer or use a local analysis tool that supports the esbuild metafile format.

---

## Next steps

- Consult the list of app extensions to find the right extension type for your use case.
- Learn about extension-only apps that don't require a web server.
- Learn how to configure app extensions in the TOML file.

---

### List of app extensions

> Fonte: https://shopify.dev/docs/apps/build/app-extensions/list-of-app-extensions

# List of app extensions

App extensions relate to specific use cases and have varying requirements. This guide describes the available app extensions that you can use to surface your app's functionality to Shopify user interfaces.

The following table lists all of the available app extensions that you can build. For each app extension listed in the table, you can review the following information:

* The area of the Shopify interface the app extension is associated with.
* Whether the app extension requires review and approval from Shopify.
* The tool to use to create the extension.
* Links to detailed documentation.

| Shopify interface area | App extension | Requires review and approval? | Description |
| - | - | - | - |
| [Shopify admin](https://help.shopify.com/manual/shopify-admin/shopify-admin-overview) | [Admin actions](https://shopify.dev/docs/apps/build/admin/actions-blocks#admin-actions) | No | Add custom modals to resource pages in the Shopify admin. |
| | [Admin blocks](https://shopify.dev/docs/apps/build/admin/actions-blocks#admin-blocks) | No | Add custom cards to resource pages in the Shopify admin. |
| | [Product configuration](https://shopify.dev/docs/apps/build/product-merchandising/bundles/product-configuration-extension/add-merchant-config-ui) | No | Allow users to interact with bundles on the product details page of the Shopify admin. |
| | [Admin link extensions](https://shopify.dev/docs/apps/build/admin/admin-links/create-admin-links) | No | Add quick links to your app from any page in the Shopify admin. |
| | [Channel config extension](https://shopify.dev/docs/apps/build/sales-channels/channel-config-extension) | No | Configure your app as a sales channel and define channel specifications for the markets, capabilities, and requirements that your app supports. |
| | [Discount function settings](https://shopify.dev/docs/apps/build/discounts/build-ui-extension?extension=javascript) | No | Allow users to configure app discounts on the discount details page in admin. |
| | [Navigation links](https://shopify.dev/docs/apps/build/admin/admin-links) | No | Add navigation links to display your app's navigation items consistently across devices. |
| | [Purchase options extensions](https://shopify.dev/docs/apps/build/purchase-options/purchase-options-extensions) | No | Add purchase options for users in the Shopify admin. |
| | [Subscription link](https://shopify.dev/docs/apps/build/purchase-options/subscriptions/contracts/subscription-link-extensions/start-building) | No | Customize the link that allows users to see the subscription details in your subscription-enabled application. |
| | [Web pixel](https://shopify.dev/docs/apps/build/marketing-analytics/pixels) | No | Run JavaScript code snippets on the **Order status** page to collect behavioral data for marketing campaign optimization and analytics. |
| [App Home](https://shopify.dev/docs/apps/build/app-home) | [App Home UI extensions](https://shopify.dev/docs/apps/build/app-home/app-home-ui-extensions) | No | Build a Shopify-hosted landing page for your app in the admin, with no backend required. |
| [Checkout](https://shopify.dev/docs/apps/build/checkout) | [Checkout UI extensions](https://shopify.dev/docs/api/checkout-ui-extensions) | No | Add custom workflows and functionality at defined points in the checkout process. |
| | [Shopify Functions](https://shopify.dev/docs/api/functions) | No | Inject custom code into key areas of the Shopify platform, such as checkout or cart. |
| | [Post-purchase](https://shopify.dev/docs/apps/build/checkout/product-offers#post-purchase-product-offers) | Yes | Help users increase sales by adding products for purchase after checkout. |
| | [Web pixel](https://shopify.dev/docs/apps/build/marketing-analytics/pixels) | No | Run JavaScript code snippets on an online store to collect behavioral data for marketing campaign optimization and analytics. |
| [Customer accounts](https://shopify.dev/docs/apps/build/customer-accounts) | [Customer account UI extensions](https://shopify.dev/docs/api/customer-account-ui-extensions) | No | Add functionality at defined points in customer accounts. |
| [Flow](https://shopify.dev/docs/apps/build/flow) | [Triggers](https://shopify.dev/docs/apps/build/flow/triggers) | No | Connect your app to Shopify Flow so that events that occur in your app can trigger workflows. |
| | [Actions](https://shopify.dev/docs/apps/build/flow/actions) | No | Connect your app to Shopify Flow so that your app receives data when a workflow action runs. |
| | [Templates](https://shopify.dev/docs/apps/build/flow/templates) | Yes | Create an example workflow that's available in Flow's template library and can be copied into a merchant's store. |
| | [Lifecycle Events](https://shopify.dev/docs/apps/build/flow/track-lifecycle-events) | No | Improve efficiency by letting Shopify Flow notify your app when your triggers are in use. |
| [Online store](https://shopify.dev/docs/apps/build/online-store) | [Theme app extensions](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions) | No | Integrate with Online Store 2.0 themes. Theme app extensions act as a replacement for using the [Script Tag or Asset resources](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy) to integrate apps with online stores. |
| | [Web pixel](https://shopify.dev/docs/apps/build/marketing-analytics/pixels) | No | Run JavaScript code snippets on an online store to collect behavioral data for marketing campaign optimization and analytics. |
| [Payments](https://shopify.dev/docs/apps/build/payments) | [Payments extension](https://shopify.dev/docs/apps/build/payments#build-options) | Yes | Allow customers to complete purchases using a payment method provided by your app. |
| [Shopify Point of Sale (POS)](https://shopify.dev/docs/apps/build/pos) | [POS UI extensions](https://shopify.dev/docs/api/pos-ui-extensions) | No | Add custom functionality at defined areas in the POS app. |

## Next steps

* Learn how to [deploy extensions](https://shopify.dev/docs/apps/launch/deployment/deploy-app-versions) to release changes to users.

---

### Configure app extensions

> Fonte: https://shopify.dev/docs/apps/build/app-extensions/configure-app-extensions

# Configure app extensions

When you [generate an app extension](https://shopify.dev/docs/api/shopify-cli/app/app-generate-extension), a TOML configuration file named `shopify.extension.toml` is automatically generated in your app's extension directory.

Some extension types use different TOML structures and are documented in other topics:

* [Post-purchase UI](https://shopify.dev/docs/api/checkout-extensions/post-purchase/configuration)
* [Product subscription](https://shopify.dev/docs/apps/build/purchase-options/product-subscription-app-extensions/start-building)
* [Shopify Functions](https://shopify.dev/docs/api/functions/latest#configuration)
* [Theme app extensions](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions/build)
* [Web pixel](https://shopify.dev/docs/apps/build/marketing-analytics/build-web-pixels)

---

## How it works

[Shopify CLI](https://shopify.dev/docs/apps/build/cli-for-apps) builds and serves app extensions using information defined in a TOML file named `shopify.extension.toml`. The TOML file is located in a directory within the [`extensions/` directory](https://shopify.dev/docs/apps/build/cli-for-apps/app-structure#directory-structure) of your app project.

The following example shows a `shopify.extension.toml` file that contains configuration settings for a [checkout UI extension](https://shopify.dev/docs/api/checkout-ui-extensions).

## shopify.extension.toml

```toml
api_version = "2025-10"


[[extensions]]
name = "My UI extension"
description = "A UI extension"
handle = "my-ui-extension"
type = "ui_extension"
uid = "1aafc25d-8448-218e-9373-b3d91ac2a0af75f73e12"


  [extensions.capabilities]
  api_access = true
  block_progress = true
  network_access = true


  [[extensions.targeting]]
  module = "./src/CheckoutDynamicRender.js"
  target = "purchase.checkout.block.render"


    [[extensions.targeting.metafields]]
    key = "my-key"
    namespace = "my-namespace"


[settings]
  [[settings.fields]]
  key = "banner_title"
  type = "single_line_text_field"
  name = "Banner title"
  description = "Enter a title for the banner"
```

---

## Extension types

Some extensions require specific configurations. To accommodate this, Shopify CLI groups extensions into different types in the TOML file:

| Extension | `type` value in the TOML file | `--template` flag value in the generate command |
| - | - | - |
| [Admin action](https://shopify.dev/docs/apps/build/admin/actions-blocks/build-admin-action) | `ui_extension` | `admin_action` |
| [Admin block](https://shopify.dev/docs/apps/build/admin/actions-blocks/build-admin-block) | `ui_extension` | `admin_block` |
| [App Home UI](https://shopify.dev/docs/api/app-home-ui-extension/2026-07-rc) | `ui_extension` | `app_home_ui` |
| [Customer Account UI](https://shopify.dev/docs/api/customer-account-ui-extensions) | `ui_extension` | `customer_account_ui` |
| [Checkout UI](https://shopify.dev/docs/api/checkout-ui-extensions) | `ui_extension` | `checkout_ui` |
| [Editor extension collection](https://shopify.dev/docs/apps/build/customer-accounts/editor-extension-collections) | `editor_extension_collection` | `editor_extension_collection` |
| [Product configuration](https://shopify.dev/docs/apps/build/product-merchandising/bundles/product-configuration-extension/add-merchant-config-ui) | `ui_extension` | `product_configuration` |
| [Shopify Flow action](https://shopify.dev/docs/apps/build/flow/actions) | `flow_action` | `flow_action` |
| [Shopify Flow template](https://shopify.dev/docs/apps/build/flow/templates) | `flow_template` | `flow_template` |
| [Shopify Flow trigger](https://shopify.dev/docs/apps/build/flow/triggers) | `flow_trigger` | `flow_trigger` |
| [POS UI](https://shopify.dev/docs/api/pos-ui-extensions) | `ui_extension` | `pos_ui` |
| [Functions](https://shopify.dev/docs/api/functions) | `function` | Varies by [Functions API](https://shopify.dev/docs/api/functions) |

---

## Targets

A target is an identifier in `shopify.extension.toml` that specifies where you're injecting code into Shopify APIs, or other parts of the Shopify platform.

Each target is composed of three to four namespaces. The name begins with a broad Shopify context and ends with the behavior of the extensible element. For example, a checkout UI extension that renders a shipping address form has a target named `purchase.checkout.delivery-address.render-before`:

* `purchase`: The broad Shopify context.
* `checkout`: The targeted page.
* `delivery-address`: The element that the extension will be positioned near.
* `render-before`: An action verb that describes the behavior of the extensible element.

### Supported targets

The following table provides links to documentation on the supported targets associated with each app extension type.

| Extension type | Documentation on supported targets |
| - | - |
| Admin UI | [Admin UI targets](https://shopify.dev/docs/api/admin-extensions/extension-targets) |
| App Home UI | [`admin.app.home.render`](https://shopify.dev/docs/api/app-home-ui-extension/latest/targets) |
| Checkout UI | [Checkout UI targets](https://shopify.dev/docs/api/checkout-ui-extensions/current/targets) |
| Customer Account UI | [Customer Account UI targets](https://shopify.dev/docs/api/customer-account-ui-extensions/targets) |
| POS UI | [POS UI targets](https://shopify.dev/docs/api/pos-ui-extensions/targets) |
| Product configuration | Product configuration app extensions use the [admin.product-details.configuration.render](https://shopify.dev/docs/api/admin-extensions/extension-targets#extensiontargets-propertydetail-adminproductdetailsconfigurationrender) or [admin.product-variant-details.configuration.render](https://shopify.dev/docs/api/admin-extensions/extension-targets#extensiontargets-propertydetail-adminproductvariantdetailsconfigurationrender) target. |
| Functions | [Functions targets](https://shopify.dev/docs/api/functions/latest#function-extension-target-types) |

---

## Common properties

This section describes the configuration settings in `shopify.extension.toml` that are common to [Checkout UI](https://shopify.dev/docs/apps/build/checkout/technologies), [Admin UI](https://shopify.dev/docs/api/admin-extensions), [product configuration](https://shopify.dev/docs/apps/build/product-merchandising/bundles/product-configuration-extension/add-merchant-config-ui), [Shopify Flow triggers](https://shopify.dev/docs/apps/build/flow/triggers), [Shopify Flow actions](https://shopify.dev/docs/apps/build/flow/actions), and [Shopify Flow templates](https://shopify.dev/docs/apps/build/flow/templates) extensions.

**Note:**

[POS UI extensions](https://shopify.dev/docs/api/pos-ui-extensions) only support the required properties listed in the table.

| Property | Description |
| - | - |
| `api_version` required | The version of the API that's being used for the extension. If provided in the `[[extensions]]` array, then the specified API version is used instead of the root level `api_version`. |
| `[[extensions]]` required | The name of the array that contains all extensions listed in the TOML file. Contains the following properties: - `name`:required The merchant-facing name of the extension. After you [generate an extension](https://shopify.dev/docs/api/shopify-cli/app/app-generate-extension), you're prompted to provide a name for your extension. The `name` property is translatable if it starts with a `t:` and uses a key defined in your translation data. For example, you might have a `t:name` key that matches a translation key called `name`. [Learn more about localization](https://shopify.dev/docs/apps/build/checkout/localized-checkout-ui-extensions#how-it-works). **Limitations:** - Supports any characters. Shopify Flow actions and Shopify Flow triggers extensions can only include alphanumeric characters and spaces. - 5 characters minimum - 30 characters maximum - `description`:required The merchant-facing description of the extension. The `description` property is translatable if it starts with a `t:` and uses a key defined in your translation data. For example, `t:description` and you have a matching translation key called `description`. [Learn more about localization](https://shopify.dev/docs/apps/build/checkout/localized-checkout-ui-extensions#how-it-works). - `handle`:required A unique reference name for the extension. Used when referencing the extension in configuration, APIs, and the Dev Dashboard. **Limitations:** - Allowed characters: `a-z`, `A-Z`, `0-9`, `-` - 100 characters maximum - Must be unique within the app - `uid`:required The extension user identifier. An app-scoped identifier used by `shopify app deploy` to determine whether an extension is being created, updated, or deleted. **Limitations:** - Must be unique within the app - `type`:required The extension type. For more information, refer to [Extension types](#extension-types). |
| `[settings]` optional | The name of the array that defines settings that a merchant can set values for. If provided in the `[[extensions]]` array, then the specified settings are used instead of the root level `settings`. |
| `[[settings.fields]]` optional | The name of the array that contains the [settings fields](#settings-fields). |
| `[[extensions.targeting]]` required | The name of the array that contains a target and path to the related extension code. Contains the following required properties: - `target`:required An identifier that specifies where you're injecting code into Shopify APIs, or other parts of the Shopify platform. For more information, refer to [Targets](#targets). - `module`:required The file that contains the extension code. |

---

## Settings fields

Settings let merchants customize your extension from the editor. All setting inputs are optional unless marked as required — code your extension so it still works if the merchant hasn't set a value.

Each field in `[[settings.fields]]` accepts the following properties:

* `key`: The identifier for the setting. The configured value is exposed under this key at runtime.
* `type`: The [setting type](#supported-setting-types). Determines what input the merchant sees and how the value is validated.
* `name`: The merchant-facing display name for the setting.
* `description`: Help text displayed to the merchant in the editor.
* `validations`: Constraints on the input. See [validation options](#validation-options).

### Supported setting types

The following setting types apply to [checkout UI extensions](#checkout-ui-extensions) and [customer account UI extensions](#customer-account-ui-extensions). Other extension types may support additional types.

The setting type determines the type of information that the setting can store. The setting types have built-in validation on the setting input.

| Type | Description | Example value |
| - | - | - |
| `boolean` | A true or false value. | `true` |
| `date` | A date in ISO 8601 format without a presumed time zone. | `2022-02-02` |
| `date_time` | A date and time in ISO 8601 format without a presumed time zone. | `2022-01-01T12:30:00` |
| `single_line_text_field` | A single line string. | `Canada` |
| `multi_line_text_field` | A multi-line string. | `Canada` |
| `number_integer` | A whole number in the range of +/-9,007,199,254,740,991. | `10` |
| `number_decimal` | A number with decimal places in the range of +/-9,999,999,999,999.999999999. | `10.4` |
| `variant_reference` | A globally-unique identifier (GID) for a product variant. | `gid://shopify/ProductVariant/1` |

### Validation options

Each setting can include validation options. Validation options enable you to apply additional constraints to the data that a setting can store, such as a minimum or maximum value, or a regular expression. The setting's `type` determines the available validation options.

You can include a validation option for a setting using the validation `name` and a corresponding `value`. The appropriate value depends on the setting type to which the validation applies.

| Validation option | Description | Supported types | Example |
| - | - | - | - |
| Minimum length | The minimum length of a text value. | `single_line_text_field`, `multi_line_text_field` | `name = "min"` `value = "8"` |
| Maximum length | The maximum length of a text value. | `single_line_text_field`, `multi_line_text_field` | `name = "max"` `value = "25"` |
| Regular expression | A regular expression. Shopify supports [RE2](https://github.com/google/re2/wiki/Syntax). | `single_line_text_field`, `multi_line_text_field` | `name = "regex"` `value = "(@)(.+)$"` |
| Choices | A list of up to 128 predefined options that limits the values allowed for the setting. | `single_line_text_field` | `name = "choices"` `value = '["red", "green", "blue"]'` |
| Minimum date | The minimum date in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. | `date` | `name = "min"` `value = "2022-01-01"` |
| Maximum date | The maximum date in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. | `date` | `name = "max"` `value = "2022-03-03"` |
| Minimum datetime | The minimum date and time in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. | `date_time` | `name = "min"` `value = "2022-01-01T00:00:00"` |
| Maximum datetime | The maximum date and time in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. | `date_time` | `name = "max"` `value = "2022-03-03T00:00:00"` |
| Minimum integer | The minimum value of an integer. | `number_integer` | `name = "min"` `value = "0"` |
| Maximum integer | The maximum value of an integer. | `number_integer` | `name = "max"` `value = "100"` |
| Minimum decimal | The minimum value of a decimal number. | `number_decimal` | `name = "min"` `value = "0.5"` |
| Maximum decimal | The maximum value of a decimal number. | `number_decimal` | `name = "max"` `value = "99.99"` |
| Maximum precision | The maximum number of decimal places to store for a decimal number. | `number_decimal` | `name = "max_precision"` `value = "2"` |

---

## Extension-specific properties

This section describes the configuration settings in `shopify.extension.toml` that are specific to the following extensions:

* [Checkout UI extensions](#checkout-ui-extensions)
* [Customer Account UI extensions](#customer-account-ui-extensions)
* [POS UI extensions](#pos-ui-extensions)
* [Editor extension collection](#editor-extension-collection)
* [Admin UI extensions](#admin-ui-extensions)
* [App Home UI extensions](#app-home-ui-extensions)
* [Product configuration extensions](#product-configuration-extensions)
* [Shopify Flow actions](#shopify-flow-actions)
* [Shopify Flow triggers](#shopify-flow-triggers)
* [Shopify Flow templates](#shopify-flow-templates)

### Checkout UI extensions

The following example TOML file contains configuration settings for a [checkout UI extension](https://shopify.dev/docs/api/checkout-ui-extensions):

## shopify.extension.toml

```toml
api_version = "2025-10"


[[extensions]]
name = "My UI extension"
description = "A UI extension"
handle = "my-ui-extension"
type = "ui_extension"
uid = "1aafc25d-8448-218e-9373-b3d91ac2a0af75f73e12"


  [extensions.capabilities]
  api_access = true
  block_progress = true
  network_access = true


  [[extensions.targeting]]
  module = "./src/CheckoutDynamicRender.js"
  target = "purchase.checkout.block.render"
  default_placement = "WALLETS1"


    [[extensions.targeting.metafields]]
    key = "my-key"
    namespace = "my-namespace"


[settings]
  [[settings.fields]]
  key = "banner_title"
  type = "single_line_text_field"
  name = "Banner title"
  description = "Enter a title for the banner"
```

The following table describes the properties in the TOML file that are specific to checkout UI extensions:

| Property | Description |
| - | - |
| `[extensions.capabilities]` optional | The name of the array that contains the checkout UI extension's capabilities: - `api_access`:optional Whether your app extension can [query the Storefront API](https://shopify.dev/docs/apps/build/checkout/capabilities#storefront-api-access). - `block_progress`:optional Whether your app extension can [block the customer's progress](https://shopify.dev/docs/apps/build/checkout/capabilities#block-progress). - `network_access`:optional Whether your app extension can make [external network calls](https://shopify.dev/docs/apps/build/checkout/capabilities#network-access). - `collect_buyer_consent`:optional Whether your app extension can [collect buyer consent](https://shopify.dev/docs/apps/build/checkout/capabilities#collect-buyer-consent) for SMS marketing (`sms_marketing`) or customer privacy (`customer_privacy`). |
| `[extensions.metafields]` optional | An array that sets the default for each `[[extensions.targeting.metafields]]`, if `[[extensions.targeting.metafields]]` isn't specified. |
| `[[extensions.targeting.metafields]]` optional | The [metafields](https://shopify.dev/docs/api/checkout-ui-extensions/latest/targets/block/purchase-thank-you-block-render#standardapi-propertydetail-metafields) that your extension target needs to read: - `key`:optional The name for the metafield. - `namespace`:optional A container for a group of metafields. Grouping metafields within a namespace prevents your metafields from conflicting with other metafields with the same key name. You can specify up to five `key` and `namespace` pairs in the configuration file. When the extension is executed, Shopify looks for the metafields in each resource and returns their contents. |
| `[[extensions.targeting.default_placement]]` optional | Defines which location of a block extension target an extension is placed in when added. After adding the extension, the merchant can move it to other locations. Value must be a checkout [block extension target](/docs/apps/build/checkout/test-checkout-ui-extensions#block-extension targets). |

### Customer account UI extensions

The following example TOML files contain configuration settings for [a static and a full page extension](https://shopify.dev/docs/api/customer-account-ui-extensions/extension-targets-overview). The properties in the TOML files are similar to [checkout UI extensions](#checkout-ui-extensions):

## shopify.extension.toml

```toml
api_version = "2025-10"


[[extensions]]
type = "ui_extension"
uid = "9ebaa5f0-a0d8-25bf-6290-c55f579e4dfac7c7fcd2"
name = "customer-account-ui"
handle = "customer-account-ui"




[[extensions.targeting]]
module = "./src/CustomerAccountOrderIndexExtension.tsx"
target = "customer-account.order-index.block.render"
default_placement = "ORDER_INDEX"


[[extensions.targeting]]
module = "./src/CustomerAccountExtensionFullPage.tsx"
target = "customer-account.page.render"
```

The following table describes the properties in the TOML file that are specific to customer account UI extensions:

| Property | Description |
| - | - |
| `[extensions.capabilities]` optional | The name of the array that contains the customer account UI extension's capabilities: - `api_access`: Whether your app extension can [query the Storefront API](https://shopify.dev/docs/apps/build/customer-accounts/capabilities#storefront-api-access). - `network_access`: Whether your app extension can make [external network calls](https://shopify.dev/docs/apps/build/customer-accounts/capabilities#network-access). Before requesting network access, consider whether [metafields](https://shopify.dev/docs/apps/build/customer-accounts/metafields-in-customer-accounts) can provide the data your extension needs. - `collect_buyer_consent`: Whether your app extension can [collect buyer consent](https://shopify.dev/docs/apps/build/customer-accounts/capabilities#collect-buyer-consent) for SMS marketing (`sms_marketing`) or customer privacy (`customer_privacy`). |
| `[extensions.metafields]` optional | An array that sets the default for each `[[extensions.targeting.metafields]]`, if `[[extensions.targeting.metafields]]` isn't specified. |
| `[[extensions.targeting.metafields]]` optional | The [metafields](https://shopify.dev/docs/apps/build/customer-accounts/metafields-in-customer-accounts) that your extension target needs to read: - `key`: The name for the metafield. - `namespace`: A container for a group of metafields. Grouping metafields within a namespace prevents your metafields from conflicting with other metafields with the same key name. You can specify up to five `key` and `namespace` pairs in the configuration file. When the extension is executed, Shopify looks for the metafields in each resource and returns their contents. |
| `[[extensions.targeting.default_placement]]` optional | Defines which location of a block extension target an extension is placed in when added. After adding the extension, the merchant can move it to other locations. Value must be one of the [customer account placements](https://shopify.dev/docs/apps/build/customer-accounts/extension-placement#define-default-placement) for the block extension target. |

#### Supported resource metafield types

Supported resource metafield types for customer account UI extensions include:

| Resource | Description |
| - | - |
| `cart` | The cart associated with the checkout. |
| `customer` | The customer associated with the order. |
| `order` | The order being viewed. |
| `company` | The company for B2B orders. |
| `companyLocation` | The company's location for B2B orders. |
| `product` | The products in the order. |
| `shop` | The shop associated with the order. |
| `variant` | The product variants in the order. |

#### App-owned metafields

[App-owned metafields](https://shopify.dev/docs/apps/build/custom-data/ownership#reserved-prefixes) are supported. You can use app-owned metafields when your app needs to control the data and visibility of the metafield.

Your extension can access app-owned metafields that are requested in its TOML using the `$app` format. Your extension can only access app-owned metafields that belong to its parent app.

**Caution:**

When accessing app-owned metafields, you must use the `$app` format. The fully qualified reserved namespace format such as `app--{your-app-id}[--{optional-namespace}]` is not supported.

### POS UI extensions

The following example TOML file contains configuration settings for a [POS UI extension](https://shopify.dev/docs/api/pos-ui-extensions) configured to run offline:

## shopify.extension.toml

```toml
api_version = "2026-01"


[[extensions]]
name = "My POS UI extension"
description = "A POS UI extension"
handle = "my-pos-ui-extension"
type = "ui_extension"
uid = "1aafc25d-8448-218e-9373-b3d91ac2a0af75f73e12"


  [extensions.supported_features]
  runs_offline = true


  [[extensions.targeting]]
  target = "pos.home.tile.render"
  module = "./src/Tile.tsx"


  [[extensions.targeting]]
  target = "pos.home.modal.render"
  module = "./src/Modal.tsx"
```

The following table describes the properties in the TOML file that are specific to POS UI extensions:

| Property | Description |
| - | - |
| `[extensions.supported_features]` optional | Declares additional features for your extension. Contains the following property: - `runs_offline`:optional When set to `true`, the extension runs even when POS is offline. Defaults to `false`. When your extension runs offline, it continues to function using locally available data and APIs that don't require network connectivity. For more information, refer to [Run extensions offline](https://shopify.dev/docs/api/pos-ui-extensions/latest#run-extensions-offline). |

### Editor extension collection

The following example TOML files contain configuration settings for an [editor extension collection](https://shopify.dev/docs/apps/build/customer-accounts/editor-extension-collections):

## shopify.extension.toml

```toml
[[extensions]]
name = "t:collection_name"
type = "editor_extension_collection"
uid = "8723da04-b91d-e812-2091-52c161b3b2892fa89479"
handle = "editor-extension-collection"
includes=["customer-account-ui", "checkout-ui-extension"]
```

The following table describes the properties in the TOML file that are specific to editor extension collections:

| Property | Required? | Description |
| - | - | - |
| `[extensions.includes]` | Yes | An array that sets the supported extensions that belong in the editor extension collection. **Limitations:** - Currently, can only contain customer account UI and checkout UI extensions. - Must contain two or more extensions. |

### Admin UI extensions

The following example TOML files contain configuration settings for [an action and a block extension](https://shopify.dev/docs/apps/build/admin/actions-blocks). The properties in the TOML files are similar to [checkout UI extensions](#checkout-ui-extensions):

## shopify.extension.toml

```toml
api_version = "2025-10"


[[extensions]]
name = "My feature"
handle = "action-extension"
type = "ui_extension"
uid = "3e9ce641-7624-b901-fdef-cc194f77a8720c5af6e5"


[[extensions.targeting]]
module = "actionExtension.jsx"
target = "admin.product.item.action.render"
```

## shopify.extension.toml

```toml
api_version = "2025-10"


[[extensions]]
name = "My block extension"
handle = "block-extension"
type = "ui_extension"
uid = "f62f100d-15e6-9866-eda9-23f99de4b5d26e347042"


[[extensions.targeting]]
module = "blockExtension.jsx"
target = "admin.product.item.block.render"
```

### App Home UI extensions

The following example TOML file contains configuration settings for an [App Home UI extension](https://shopify.dev/docs/api/app-home-ui-extension/latest). App Home UI extensions use the same properties in their TOML file as [admin UI extensions](#admin-ui-extensions), with one additional `[[extensions.targeting.assets]]` property that points to the directory containing static assets bundled with the extension.

## shopify.extension.toml

```toml
api_version = "2026-07"


[[extensions]]
name = "App Home"
handle = "app-home"
type = "ui_extension"
uid = "1aafc25d-8448-218e-9373-b3d91ac2a0af75f73e12"


  [[extensions.targeting]]
  target = "admin.app.home.render"
  module = "./src/AppHome.tsx"
  assets = "./assets"
```

The following table describes the properties in the TOML file that are specific to App Home UI extensions:

| Property | Description |
| - | - |
| `[[extensions.targeting]]` required | Must contain a single `target` entry that targets [`admin.app.home.render`](https://shopify.dev/docs/api/app-home-ui-extension/latest/targets). The `module` value points to the Preact entry file that renders the page. `assets` defines a relative path to the directory containing static assets (such as images) that the extension's bundle references at runtime. |

### Product configuration extensions

The following example TOML file contains configuration settings for a [product configuration extension](https://shopify.dev/docs/apps/build/product-merchandising/bundles/product-configuration-extension/add-merchant-config-ui). The properties in the TOML file are similar to a [checkout UI extension](#checkout-ui-extensions):

## shopify.extension.toml

```toml
api_version = "2025-10"


[[extensions]]
name = "My product config extension"
handle = "my-product-config-extension"
type = "ui_extension"
uid = "8a8e0c98-1efb-7556-dfbb-04bdcfea1662b066ab00"


[[extensions.targeting]]
module = "./src/ProductDetailsConfigurationExtension.tsx"
target = "admin.product-details.configuration.render"


[[extensions.targeting]]
module = "./src/ProductVariantDetailsConfigurationExtension.tsx"
target = "admin.product-variant-details.configuration.render"
```

### Shopify Flow actions

The following example TOML file contains configuration settings for a [Shopify Flow action](https://shopify.dev/docs/apps/build/flow/actions):

## shopify.extension.toml

```toml
[[extensions]]
name = "Send email action"
description = "Send an email to a customer."
handle = "send-email-action"
type = "flow_action"
uid = "e75268dd-a0bf-45f9-2c95-b988a06f307920b6602c"
runtime_url = "https://runtime-endpoint.com"
schema = "./schema.graphql"
return_type_ref = "EmailDelivered"
validation_url = "https://validation-url"
config_page_url = "https://url.com/config"
config_page_preview_url = "https://url.com/config/preview"


[settings]


  [[settings.fields]]
  description = "The email address to send to"
  key = "email_address"
  name = "Email address"
  type = "single_line_text_field"
  required = true


  [[settings.fields]]
  description = "The subject of the email"
  key = "subject"
  name = "Subject"
  type = "single_line_text_field"
  required = true


  [[settings.fields]]
  description = "The body of the email"
  key = "body"
  name = "Body"
  type = "multi_line_text_field"
  required = true
```

The following table describes the properties in the TOML file that are specific to a Shopify Flow action:

| Property | Description |
| - | - |
| `[[extensions]]` required | The name of the array that contains all extensions listed in the TOML file. Contains the following properties: - `runtime_url`:required The endpoint where Flow sends your action's payload when your step is being executed at runtime. [The payload](https://shopify.dev/docs/apps/build/flow/actions/endpoints#flow-action-execution) contains data that you can use to execute the action in your app. - `validation_url`:optional [An endpoint](https://shopify.dev/docs/apps/build/flow/actions/endpoints#custom-validation) that validates the contents of custom properties in an action payload when an action is saved. This endpoint is only required if you want to use a [custom configuration page](https://shopify.dev/docs/apps/build/flow/actions/build-config-ui). - `schema`:optional A relative path to a GraphQL schema definition file that contains custom types that you can use as part of your action. Only required if `return_type_ref` is also present. - `return_type_ref`:optional The name of the type to be returned by the action. This type must be present in the referenced schema file. Only required if `schema` is also present. - `config_page_url`:optional A route that renders your [custom configuration page](https://shopify.dev/docs/apps/build/flow/actions/build-config-ui). - `config_page_preview_url`:optional [An endpoint](https://shopify.dev/docs/apps/build/flow/actions/endpoints#custom-configuration-page-preview) that provides data about your custom configuration page to display in the automation tool. This endpoint is only required if you want to use a [custom configuration page](https://shopify.dev/docs/apps/build/flow/actions/build-config-ui). |
| `[[settings.fields]]` required | The name of the array that contains the settings fields. Contains the following property: - `required`:required Specifies whether a field is required (`true`) or optional (`false`). |

### Shopify Flow triggers

The following example TOML file contains configuration settings for a [Shopify Flow trigger](https://shopify.dev/docs/apps/build/flow/triggers). The properties in the TOML file are similar to a [Shopify Flow action](#shopify-flow-actions):

## shopify.extension.toml

```toml
[[extensions]]
name = "Shopify Email sent"
description = "Triggered when an email is sent from Shopify"
handle = "shopify-email-sent"
type = "flow_trigger"
uid = "1b625187-49cd-77d4-524b-5cfbb4582529885aa0fe"


[settings]


  [[settings.fields]]
  description = "The customer who received the email."
  key = "customer_id"
  name = "Customer ID"
  type = "customer_reference"


  [[settings.fields]]
  description = "The marketing campaign ID."
  key = "campaign_id"
  name = "Campaign ID"
  type = "single_line_text_field"
```

### Shopify Flow templates

The following example TOML file contains configuration settings for a [Shopify Flow template](https://shopify.dev/docs/apps/build/flow/templates).

## shopify.extension.toml

```toml
[[extensions]]
name = "t:name"
type = "flow_template"
uid = "7fec5c80-7dd4-5fbc-1eb5-203e4bd8e1bfe9ec810a"
handle = "example-handle"
description = "t:description"


[extensions.template]


categories = ["orders", "risk"]


module = "./template.flow"


require_app = false


discoverable = true


enabled = true
```

The following table describes the properties in the TOML file that are specific to a Shopify Flow template:

| Property | Description |
| - | - |
| `[extensions.template]` required | Settings related to the template. Contains the following properties: - `categories`:required The categories that best describe the function of your template. Must be an array containing only strings of valid categories. Must choose at least one category. Max 2 recommended. Valid categories are: `buyer_experience`, `customers`, `inventory_and_merch`, `loyalty`, `orders`, `promotions`, `risk`, `fulfillment`, `b2b`, `payment_reminders`, `custom_data`, and `error_monitoring`. - `module`:required The file path of the template workflow in the extension's folder. - `require_app`:optional Whether your template is visible only to merchants who have your app installed. Defaults to `false` if not provided. - `discoverable`:optional Whether your template should be displayed in the template browser. When `false`, the template is accessible only through a deep link. Defaults to `true` if not provided. - `enabled`:optional Whether your template should be made available after being approved and released. Defaults to `true` if not provided. |

---

## Differences in TOML file names

TOML file names can differ, depending on when you generated an extension:

* If you generated an extension before July 26, 2023, then your TOML file maps to one of the following names:

  * **Checkout UI**: `shopify.ui.extension.toml`
  * **Bundles UI extension**: `shopify.ui.extension.toml` (maps to a [product configuration extension](https://shopify.dev/docs/apps/build/product-merchandising/bundles/product-configuration-extension/add-merchant-config-ui))
  * **Post-purchase UI**: `shopify.ui.extension.toml`
  * **Product subscription**: `shopify.ui.extension.toml`
  * **Web pixel**: `shopify.ui.extension.toml`
  * **Shopify POS UI**: `shopify.ui.extension.toml`
  * **Theme app extensions**: `shopify.theme.extension.toml`

* If you generated an extension after July 26, 2023, then the TOML file is named `shopify.extension.toml`.

---

### Build an extension-only app

> Fonte: https://shopify.dev/docs/apps/build/app-extensions/build-extension-only-app

# Build an extension-only app

Extension-only apps are made up entirely of extensions, so you can host them on Shopify with no developer-hosted backend. The extension-only template now includes an [App Home UI extension](https://shopify.dev/docs/apps/build/app-home/app-home-ui-extensions) by default, which renders the app's main page in App Home.

**Note:**

Extension-only apps can only be installed with [custom distribution](https://shopify.dev/docs/apps/launch/distribution/select-distribution-method).

---

## Create an extension-only app

Create a new app, give it a name, and choose **Build an extension-only app**.

### Terminal

```terminal
shopify app init
```

After you've created your app, you can [configure your app](https://shopify.dev/docs/apps/build/cli-for-apps/app-configuration), [generate additional extensions](https://shopify.dev/docs/api/shopify-cli/app/app-generate-extension), and [deploy your app](https://shopify.dev/docs/apps/launch/deployment/app-versions).

---

## App extensions that can be included in an extension-only app

The following table lists the app extensions that are compatible with extension-only apps.

| Domain | Extension type | Merchant experience | Description |
| - | - | - | - |
| [Admin](https://shopify.dev/docs/apps/build/admin) | [UI extension](https://shopify.dev/docs/apps/build/admin/actions-blocks) | [actions](https://shopify.dev/docs/apps/build/admin/actions-blocks#admin-actions) and/or [blocks](https://shopify.dev/docs/apps/build/admin/actions-blocks#admin-blocks) | Add custom cards or modals to resource pages in the Shopify admin. |
| [App Home](https://shopify.dev/docs/apps/build/app-home) | [App Home UI extension](https://shopify.dev/docs/api/app-home-ui-extension/2026-07-rc) | App's main page in the Shopify admin | Build a Shopify-hosted landing page for your app, with no backend required. |
| [Checkout](https://shopify.dev/docs/apps/build/checkout) | [UI extension](https://shopify.dev/docs/api/checkout-ui-extensions) | blocks | Add custom workflows and functionality at defined points in the checkout flow. |
| [Shopify Functions](https://shopify.dev/docs/api/functions) | functions | Inject custom code into key areas of the Shopify platform, such as checkout or cart. | |
| [Post-purchase UI extension](https://shopify.dev/docs/apps/build/checkout/product-offers#post-purchase-product-offers) | blocks | Help users increase sales by adding products for purchase after checkout. | |
| [Customer accounts](https://shopify.dev/docs/apps/build/customer-accounts) | [UI extension](https://shopify.dev/docs/api/customer-account-ui-extensions) | actions and/or blocks | Add functionality at defined points in customer accounts. |
| [Flow](https://shopify.dev/docs/apps/build/flow) | [Flow actions](https://shopify.dev/docs/apps/build/flow/actions) | actions | Connect your app to Shopify Flow so that your app receives data when a workflow action runs. |
| [Flow lifecycle events](https://shopify.dev/docs/apps/build/flow/track-lifecycle-events) | Not used for merchants | Notifications from Shopify Flow about stores using triggers in enabled workflows. | |
| [Flow templates](https://shopify.dev/docs/apps/build/flow/templates) | templates | Create an example workflow that's available in Flow's template library and can be copied into a merchant's store. | |
| [Flow triggers](https://shopify.dev/docs/apps/build/flow/triggers) | triggers | Connect your app to Shopify Flow so that events that occur in your app can trigger workflows. | |
| [POS]() | [UI extensions](https://shopify.dev/docs/api/pos-ui-extensions) | actions, blocks, and/or smart grid tiles | Add custom functionality at defined areas in the POS app. |

---

## Adding App Home pages

You can add an App Home page to an existing extension-only app through one of two routes: developer-hosted or Shopify-hosted.

### Option 1: Developer-hosted App Home page

If you need [public distribution](https://shopify.dev/docs/apps/launch/distribution/select-distribution-method) or anything beyond the UI extension runtime, then host your app yourself and update the `application_url` in your [app configuration](https://shopify.dev/docs/apps/build/cli-for-apps/app-configuration) to your hosted URL.

### Option 2: Shopify-hosted UI extension

Extension-only apps can include a Shopify-hosted App Home page by using an [App Home UI extension](https://shopify.dev/docs/api/app-home-ui-extension/latest). The extension targets `admin.app.home.render` and runs in the admin extension runtime. There's no backend to host. This option is restricted to [custom distribution](https://shopify.dev/docs/apps/launch/distribution/select-distribution-method).

To learn how to build with this option, see [App Home UI extensions](https://shopify.dev/docs/apps/build/app-home/app-home-ui-extensions).

---

## Next steps

* Learn how to [deploy your extensions](https://shopify.dev/docs/apps/launch/deployment/app-versions) that you built using Shopify CLI.

---

### Remove an app extension

> Fonte: https://shopify.dev/docs/apps/build/app-extensions/remove-app-extension

# Remove an app extension

If you no longer want users to use an app extension, or you want to temporarily disable an app extension, then you can remove it.

---

## Remove an app extension

The contents of each app version reflect the extensions available in your local development environment.

To remove an extension from your app, you need to remove the extension from your local environment.

1. Remove the relevant files from your app's `/extensions` directory.

   If you're using custom extension directories, then remove the files from the path specified in your [`shopify.app.toml`](https://shopify.dev/docs/apps/build/cli-for-apps/app-structure#root-configuration-files) `extension_directories` property, or remove the path from your `extension_directories` property.

2. Release a new app version by running the following command.

   Optionally, you can provide a name or message for the version using the `--version` and `--message` flags.

   ```terminal
   shopify app deploy
   ```

   You're prompted to confirm that you want to release a new app version. Shopify CLI lists the extensions that are being removed in the new app version.

3. Select **Yes, release this new version** to confirm.

---

## Restore a removed app extension

You can [roll back to a previous app version](https://shopify.dev/docs/apps/launch/deployment/deploy-app-versions#release-an-existing-app-version) to restore a removed app extension.

If you're rolling back to a previous app version to restore an extension, and you want to include the extension in subsequent app releases, then you need to make the extension code available in your local environment before you deploy again using Shopify CLI. For example, you might revert to a previous iteration of your project using your version control tool.

---

## Admin UI extensions

Mini-TOC:
- [Apps in Admin (overview)](#apps-in-admin-overview)
- [Admin UI extensions (reference index)](#admin-ui-extensions-reference-index)
- [Build an admin action UI extension (tutorial)](#build-an-admin-action-ui-extension-tutorial)
- [Build an admin block UI extension (tutorial)](#build-an-admin-block-ui-extension-tutorial)

### Apps in Admin (overview)

> Fonte: https://shopify.dev/docs/apps/build/admin/actions-blocks

# Apps in Admin

Your app can extend the Shopify admin beyond [App Home](https://shopify.dev/docs/apps/build/app-home) by adding functionality directly to resource pages like **Products**, **Customers**, and **Orders**. You can embed transactional workflows, display contextual information, launch native Shopify editors, and link to your app's pages.

There are two primary ways to extend the admin:

* **[Admin UI extensions](#admin-ui-extensions)** add custom actions, blocks, and print functionality to resource pages.
* **[Admin intents](#admin-intents)** launch Shopify's native resource editors directly from your app.

**Note:**

[Admin link extensions](https://shopify.dev/docs/apps/build/admin/admin-links) are also available but are recommended only when you need to navigate merchants to a page in your app. In most cases, admin UI extensions are a better choice.

---

## Admin UI Extensions

Admin UI extensions let you embed your app's functionality on core admin pages. They automatically match the Shopify admin's look and feel, so merchants can interact with your app without navigating away from their current task.

Each UI extension is made up of three parts:

* **[Targets](https://shopify.dev/docs/api/admin-extensions/latest/targets)** define where your extension appears in the admin, such as a product details page or an order index table.
* **[Target APIs](https://shopify.dev/docs/api/admin-extensions/latest/target-apis)** provide data and methods specific to each target, like the current resource or the ability to close a modal.
* **[Web components](https://shopify.dev/docs/api/admin-extensions/latest/web-components)** are the UI building blocks you use to render your extension's interface.

### Admin Actions

Admin actions display as modals that merchants launch from the **More actions** menu on resource pages, or from an index table's bulk action menu when one or more resources are selected. Use them for transactional workflows like creating, editing, or resolving records.

![An example admin action UI extension.](https://shopify.dev/assets/assets/images/admin/admin-actions-and-block/action-extension-example-D8t2Eqpr.gif)

### Admin Blocks

Admin blocks display as cards inline with existing resource information on admin pages. Merchants add and pin blocks to their pages. Use them to persistently display contextual information or let merchants edit data. You can also launch admin actions directly from blocks.

![An example admin block UI extension on the product page showing created issues.](https://shopify.dev/assets/assets/images/admin/admin-actions-and-block/block-extension-example-BvFjr72B.gif)

### Admin Print Actions

Admin print actions appear under the **Print** menu on orders and product pages. They include special APIs for previewing and printing documents like invoices and packing slips.

![An example admin print action UI extension.](https://shopify.dev/assets/assets/images/admin/admin-actions-and-block/build-an-admin-print-action/print-action-extension-Db_30ybn.gif)

---

## Admin Intents

[Admin intents](https://shopify.dev/docs/apps/build/admin/admin-intents) let you launch Shopify's native resource editors directly from your app. With a single API call, you can open the same editors merchants already use to create and edit products, collections, and other resources. When merchants complete their action, they return directly to your app.

```js
shopify.intents.invoke('create:shopify/Collection');
```

Admin intents work in [App Home](https://shopify.dev/docs/api/app-home/apis/user-interface-and-interactions/intents-api), [admin UI extensions](https://shopify.dev/docs/api/admin-extensions/2026-01/target-apis/utility-apis/intents-api), and [App Home UI extensions](https://shopify.dev/docs/api/app-home-ui-extension/2026-07-rc/target-apis/utility-apis/intents-api).

---

## Build for Admin

The following guides walk through common use cases for admin UI extensions. For the full reference, see [admin UI extensions](https://shopify.dev/docs/api/admin-extensions).

### Extension Types

[Build an admin action](https://shopify.dev/docs/apps/build/admin/actions-blocks/build-admin-action)

Create a modal workflow that merchants launch from a resource page's **More actions** menu.

[Build an admin block](https://shopify.dev/docs/apps/build/admin/actions-blocks/build-admin-block)

Display persistent contextual information or editable data inline on resource pages.

[Build an admin print action](https://shopify.dev/docs/apps/build/admin/actions-blocks/build-admin-print-action)

Add printable documents like invoices or packing slips to the **Print** menu on orders and product pages.

### Discounts

Add configuration UIs that let merchants set up custom discount types. See all [discounts guides](https://shopify.dev/docs/apps/build/discounts).

[Build a UI extension for discounts](https://shopify.dev/docs/apps/build/discounts/build-ui-extension)

Add configuration to your discounts experience with metafields and a UI extension.

[Build a discounts UI with React Router](https://shopify.dev/docs/apps/build/discounts/build-ui-with-react-router)

Build a configuration experience for your discount type using a React Router app UI.

### Bundles

Let merchants configure product bundles from within the admin. See all [product bundles guides](https://shopify.dev/docs/apps/build/product-merchandising/bundles).

[Add a merchant configuration UI](https://shopify.dev/docs/apps/build/product-merchandising/bundles/product-configuration-extension/add-merchant-config-ui)

Build a product configuration extension that surfaces bundle settings on the product details page.

### Purchase Options

Let merchants create and manage selling plans for subscriptions and deferred purchases. See all [purchase options guides](https://shopify.dev/docs/apps/build/purchase-options).

[Build a purchase options extension](https://shopify.dev/docs/apps/build/purchase-options/purchase-options-extensions/start-building)

Surface your app's purchase options in the Shopify admin with a purchase options extension.

[Build a product subscription extension](https://shopify.dev/docs/apps/build/purchase-options/product-subscription-app-extensions/start-building)

Let merchants create and manage subscription selling plans on the product details page.

### Orders and Fulfillment

Automate inventory, order routing, fulfillment, and returns workflows. See all [orders and fulfillment guides](https://shopify.dev/docs/apps/build/orders-fulfillment).

[Inventory management apps](https://shopify.dev/docs/apps/build/orders-fulfillment/inventory-management-apps)

Query and adjust inventory quantities on behalf of merchants.

[Order management apps](https://shopify.dev/docs/apps/build/orders-fulfillment/order-management-apps)

Fulfill orders on behalf of merchants or let merchants fulfill orders through your app.

[Order routing apps](https://shopify.dev/docs/apps/build/orders-fulfillment/order-routing-apps)

Customize fulfillment and delivery strategies with Shopify Functions.

[Returns apps](https://shopify.dev/docs/apps/build/orders-fulfillment/returns-apps)

Capture the financial, logistical, and business intent of a return.

### Marketing and Analytics

Help merchants segment customers and run marketing automations from the admin. See all [marketing and analytics guides](https://shopify.dev/docs/apps/build/marketing-analytics).

[Build a customer segment action extension](https://shopify.dev/docs/apps/build/marketing-analytics/customer-segments/build-an-action-extension)

Let merchants trigger marketing actions on a customer segment from the admin.

---

## Next Steps

* [Build an admin action](https://shopify.dev/docs/apps/build/admin/actions-blocks/build-admin-action) to extend a resource page.
* Explore the [admin UI extensions reference](https://shopify.dev/docs/api/admin-extensions) for available targets, target APIs, and web components.

---

### Admin UI extensions (reference index)

> Fonte: https://shopify.dev/docs/api/admin-extensions

# Admin UI extensions

Build extensions that integrate into the [Shopify admin interface](https://shopify.dev/docs/apps/admin). For example, you can add custom content blocks to product or order detail pages, create action modals that launch from context menus, or build custom settings interfaces for [Shopify Functions](https://shopify.dev/docs/apps/functions).

Extensions run in the context of key merchant workflows, so always prioritize performance.

## Getting started

Admin UI extensions require a TOML configuration file and TSX (or JSX) files containing your Preact-based extension code.

Use [Shopify CLI](https://shopify.dev/docs/api/shopify-cli) to scaffold your extension with the essential configuration and files. You can alter the default configuration later to customize the way your admin UI extension operates.

### Generate scaffold

```terminal
cd my-app
shopify app generate extension
```

[Tutorial - Build an admin action UI extension](https://shopify.dev/docs/apps/build/admin/actions-blocks/build-admin-action)

---

## Building your extension

Admin UI extensions are made up of three interconnected parts: targets that determine where your extension appears in the Shopify admin interface, target APIs that provide access to data and functionality based on your chosen target, and web components that define which interface elements you can use.

### Targets: Choose where your extension appears

Targets define where your extensions appear within Shopify's admin interface and what capabilities they have. There are six types of targets:

| Target type | Description |
| - | - |
| Action | Add menu items to the **More actions** menu on details and index pages. When triggered, your UI extension displays in a modal. This target has two varieties that can be used together: - **Render:** Displays the action menu item and renders your UI extension content in the modal. - **Should render:** Controls whether the action appears in the menu based on conditions. |
| Selection action | Add menu items to the **More actions** menu on index pages when merchants select multiple resources. Use for bulk operations on selected items, such as batch exports, bulk tagging, or multi-item processing. This target has two varieties that can be used together: - **Render:** Displays the action menu item and renders your UI extension content in the modal when resources are selected. - **Should render:** Controls whether the selection action appears based on conditions. |
| Block | Render inline cards on resource pages like product details, order details, or customer details. Merchants must [add and pin](https://help.shopify.com/manual/apps/working-with-apps#add-app-blocks-to-your-shopify-admin) blocks to their pages before they can use them. You can launch action targets from block targets for complex interactions. |
| Configuration | Provide configuration interfaces for various admin features. This target has two varieties: - **Product and variant configuration:** Render configuration settings for [product bundles](https://shopify.dev/docs/apps/build/product-merchandising/bundles/product-configuration-extension/add-merchant-config-ui) and customizable products on product and product variant pages. - **Function settings:** Provide configuration interfaces for [Shopify Functions](https://shopify.dev/docs/apps/build/functions), including [discount](https://shopify.dev/docs/api/functions/latest/discount), [validation](https://shopify.dev/docs/api/functions/latest/cart-and-checkout-validation), and [order routing](https://shopify.dev/docs/api/functions/latest/order-routing-location-rule) functions. |
| Print action | Add menu items to the **Print** menu on order and product pages. This target has two varieties that can be used together: - **Render:** Displays the print action menu item and opens a print interface when triggered. - **Should render:** Controls whether the print action appears in the menu based on conditions. |
| Runnable | Execute code and return data to Shopify without rendering UI. Used for extensions that supply data to Shopify features, such as [Sidekick](https://shopify.dev/docs/apps/build/sidekick/build-app-data) and [customer segment templates](https://shopify.dev/docs/apps/build/marketing-analytics/customer-segments/build-a-template-extension). |

[Reference - Explore all targets](https://shopify.dev/docs/api/admin-extensions/2026-04/targets)

### Target APIs: Define what your extension does

Your extension can display inventory alerts, add shipping label actions, or configure discount functions. Use target APIs to access the data and functionality for each scenario.

When your extension runs, Shopify provides a `shopify` global object that you use to access data and features. Most target APIs are properties on this object. For example, `shopify.data` gives you contextual resource data, `shopify.query()` runs GraphQL Admin API queries, and `shopify.navigation.navigate()` moves between pages.

If your app uses ESLint, update your configuration to include the global `shopify` object to prevent linting errors.

[Reference - Explore all target APIs](https://shopify.dev/docs/api/admin-extensions/2026-04/target-apis)

### Block Extension API: Access product data

```tsx
import {render} from 'preact';


export default () => {
  const productId = shopify.data.selected?.[0]?.id;


  render(
    <s-admin-block heading="Product information">
      <s-text>Product ID: {productId}</s-text>
    </s-admin-block>,
    document.body
  );
};
```

### ESLint configuration

```javascript
module.exports = {
  globals: {
    shopify: 'readonly',
  },
};
```

### Web components: Design your interface

Web components are the UI building blocks that you use to display data and trigger API functions. These components are native UI elements that follow [Shopify's design system](https://shopify.dev/docs/apps/design) and are built with [remote-dom](https://github.com/Shopify/remote-dom), Shopify's library for building cross-platform user interfaces.

Use web components to build interfaces that integrate with Shopify's admin design system.

[Reference - Explore all web components](https://shopify.dev/docs/api/admin-extensions/2026-04/web-components)

### Admin action component: Configure an admin action modal

```html
<s-admin-action heading="Extension title">
  Modal content
  <s-button slot="primary-action">Save</s-button>
  <s-button slot="secondary-actions">Cancel</s-button>
</s-admin-action>
```

---

## Configuration

Admin UI extensions rely on a `shopify.extension.toml` file that contains the extension's configuration. This includes the extension name, type, API version, and targeting definitions.

The `name` value is what displays in the admin interface to merchants, so consider this value carefully. We recommend that the `api_version` reflects the latest supported API version.

### Properties

Admin UI extensions use the following configuration properties:

#### `api_version` required

The version of the API that's being used for the extension. If provided in the `[[extensions]]` array, then the specified API version is used instead of the root level `api_version`.

#### `[[extensions]]` required

The name of the array that contains all extensions listed in the TOML file. Contains the following properties:

* `type`: required The extension type. For admin UI extensions, use `ui_extension`.

* `name`: required The merchant-facing name of the extension. After you [generate an extension](https://shopify.dev/docs/api/shopify-cli/app/app-generate-extension), you're prompted to provide a name for your extension. The `name` property is translatable if it starts with a `t:` and uses a key defined in your translation data.

  **Limitations**:

  * 5 characters minimum
  * 30 characters maximum

* `handle`: required The unique internal identifier for the extension. After you create a draft version of the extension, or deploy an extension, you can't change the `handle` value.

  **Limitations**:

  * Allowed characters: `a-z`, `A-Z`, `0-9`, `-`
  * 100 characters maximum
  * Must be unique within the app

* `uid`: required The extension user identifier that must be unique within the app. An app-scoped identifier used by `shopify app deploy` to determine whether an extension is being created, updated, or deleted.

* `description`: optional The merchant-facing description of the extension.

#### `[[extensions.targeting]]` required

The name of the array that contains a target and its associated module. Contains the following properties:

* `target`: required

  An identifier that specifies where you're injecting your extension into the admin interface.

* `module`: required

  The path to the JavaScript or TypeScript file that contains your extension code. This file exports the extension function that renders your UI or handles events.

### shopify.extension.toml

```toml
api_version = "2026-04"


[[extensions]]
type = "ui_extension"
name = "My Admin UI extension"
handle = "my-admin-ui-extension"
uid = "f62f100d-15e6-9866-eda9-23f99de4b5d26e347042"
description = "Custom product details extension"


    [[extensions.targeting]]
    target = "admin.product-details.block.render"
    module = "./src/ProductBlock.tsx"


    [[extensions.targeting]]
    target = "admin.product-details.action.render"
    module = "./src/ProductAction.tsx"
```

---

## App authentication

Use authenticated requests when your extension needs to fetch data or trigger actions on your own backend service. For example, you might need to display external analytics data, sync inventory with a warehouse system, or validate custom business rules.

Admin UI extensions can make authenticated calls to your app's backend. When you use `fetch()` to make a request to your app's configured auth domain or any of its subdomains, an `Authorization` header is automatically added with a Shopify [OpenID Connect ID Token](https://shopify.dev/docs/api/app-home/apis/id-token). There's no need to manually manage ID tokens.

Relative URLs passed to `fetch()` are resolved against your app's `app_url`. This means if your app's backend is on the same domain as your `app_url`, you can make requests to it using `fetch('/path')`.

If you need to make requests to a different domain, you can use the [`auth.idToken()`](https://shopify.dev/docs/api/admin-extensions/latest/api/standard-api#standardapi-propertydetail-auth) method to retrieve the ID token and manually add it to your request headers.

### Make requests to your app's backend

#### Get product data

```tsx
import {render} from 'preact';
import {useEffect, useState} from 'preact/hooks';

export default async () => {
  render(<Extension />, document.body);
}

// Get product info from app backend
async function getProductInfo(id) {
  const res = await fetch(`/api/products/${id}`);
  return res.json();
}

function Extension() {
  // Contextual "input" data passed to this extension:
  const {data} = shopify;
  const productId = data.selected?.[0]?.id;

  const [productInfo, setProductInfo] = useState();
  useEffect(() => {
    getProductInfo(productId).then(setProductInfo);
  }, [productId]);

  return (
    <s-admin-block heading="Product Info">
      <s-text>Info: {productInfo?.title}</s-text>
    </s-admin-block>
  );
}
```

#### Get data from a different domain

```tsx
import {render} from 'preact';
import {useEffect, useState} from 'preact/hooks';

export default async () => {
  render(<Extension />, document.body);
}

// Get product info from a different app backend
async function getProductInfo(id, auth) {
  const token = await auth.idToken();
  const res = await fetch(`https://app.example.com/api/products/${id}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return res.json();
}

function Extension() {
  // Contextual "input" data passed to this extension:
  const {data, auth} = shopify;
  const productId = data.selected?.[0]?.id;

  const [productInfo, setProductInfo] = useState();
  useEffect(() => {
    getProductInfo(productId, auth).then(setProductInfo);
  }, [productId, auth]);

  return (
    <s-admin-block heading="Product Info">
      <s-text>Info: {productInfo?.title}</s-text>
    </s-admin-block>
  );
}
```

**Note:**

Your server must support [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) for `https://extensions.shopifycdn.com`. Include this origin in your [`Access-Control-Allow-Origin`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin) header. The [Shopify App Remix template](https://github.com/Shopify/shopify-app-template-remix) handles this automatically.

---

## Direct API access

Use direct API access when your extension needs to query or modify Shopify data in real-time. For example, you might want to update product metafields, fetch detailed order information, or modify inventory levels.

You can make [GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql) requests directly from your extension using the [`query`](https://shopify.dev/docs/api/admin-extensions/latest/api/standard-api#standardapi-propertydetail-query) method in the Standard API or the standard [web fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Window/fetch). Any `fetch()` calls from your extension to the GraphQL Admin API are automatically authenticated by default. These requests are fast because Shopify handles them directly without requiring a round trip to your backend.

Direct API requests use [online access mode](https://shopify.dev/docs/apps/build/authentication-authorization/access-token-types/online-access-tokens) by default. If you want to use [offline access mode](https://shopify.dev/docs/apps/build/authentication-authorization/access-token-types/offline-access-tokens), you can set the `direct_api_mode` property to `offline` in your [app TOML file](https://shopify.dev/docs/apps/tools/cli/configuration#admin).

You must declare all required [access scopes](https://shopify.dev/docs/api/usage/access-scopes) in your app's TOML file.

**Note:**

Direct API can't be used to manage storefront access tokens.

### Query Shopify data directly

#### Fetch product data

```tsx
import {render} from 'preact';

export default async () => {
  const productId = shopify.data.selected?.[0]?.id;
  const product = await getProduct(productId);
  render(<Extension product={product} />, document.body);
};

async function getProduct(id) {
  const res = await fetch('shopify:admin/api/graphql.json', {
    method: 'POST',
    body: JSON.stringify({
      query: `
        query GetProduct($id: ID!) {
          product(id: $id) {
            title
          }
        }
      `,
      variables: {id},
    }),
  });
  const {data} = await res.json();
  return data.product;
}

function Extension({product}) {
  return (
    <s-admin-block heading="Product Info">
      <s-text>The selected product title is {product.title}</s-text>
    </s-admin-block>
  );
}
```

#### Query product data

```tsx
import {render} from 'preact';

export default async () => {
  const productId = shopify.data.selected?.[0]?.id;
  const {
    data: {product},
  } = await shopify.query(
    `
    query GetProduct($id: ID!) {
      product(id: $id) {
        title
      }
    }
  `,
    {variables: {id: productId}},
  );
  render(<Extension product={product} />, document.body);
};

function Extension({product}) {
  return (
    <s-admin-block heading="Product Info">
      <s-text>The selected product title is {product.title}</s-text>
    </s-admin-block>
  );
}
```

---

## Custom protocols

Custom protocols make it easier to navigate to common locations and construct URLs within your extensions.

### Shopify protocol

Use the `shopify:admin` protocol when you want to construct a URL with a root of the Shopify admin.

#### shopify:admin

##### Link to product page

```tsx
<s-link href="shopify:admin/products/1234567890">Link to Product Page</s-link>;
```

##### Fetch data

```typescript
fetch('shopify:admin/api/graphql.json', {
  method: 'POST',
  body: JSON.stringify(simpleProductQuery),
});
```

### App protocol

Use the `app:` protocol to construct a URL for your app. Shopify will handle constructing the base URL for your app. This works for both apps rendered in the Shopify admin and standalone apps.

#### app:

```tsx
<s-link href="app:settings/advanced">App settings</s-link>;
```

### Extension protocol

Trigger an action extension from a block extension using the `extension:` protocol. The `extensionTarget` is the target of the action extension. The handle is the handle of the action extension that will be opened.

#### extension:

```tsx
<s-link href={`extension:${extension.handle}/${extensionTarget}`}>Open extension</s-link>;
```

### Relative URLs

Relative urls are relative to your app and are useful when you want to link to a route within your app. This works for both apps rendered in the Shopify admin and standalone apps.

#### /relative/urls

```tsx
<s-link href={`/reviews/${product.id}`}>View reviews</s-link>;
```

---

## Testing and deployment

After you've built your extension, test it thoroughly and deploy it to production.

### Local testing

**Info:**

As of API version `2026-04`, you can write unit tests for admin UI extensions using [`@shopify/ui-extensions-tester`](https://github.com/Shopify/ui-extensions/blob/2026-04/packages/ui-extensions-tester/README.md). Check out the [example test suite](https://github.com/Shopify/ui-extensions/tree/2026-04/examples/testing/admin-testing-example) to get started.

To run your extension locally during development, start a dev server using [Shopify CLI](https://shopify.dev/docs/api/shopify-cli). The `dev` command creates a preview of your extension on your chosen [dev store](https://shopify.dev/docs/apps/build/dev-dashboard/development-stores). If your extension is built on an app with a backend, then this command also serves your backend locally using a Cloudflare tunnel.

The dev server automatically reloads your extension when you make changes to your code, so you can test updates in real-time.

### Start development server

```terminal
shopify app dev
```

### Deployment

When you're ready to go live, deploy your extension to production using [Shopify CLI](https://shopify.dev/docs/api/shopify-cli).

The Shopify CLI `deploy` command builds your extension bundle and uploads everything to Shopify. If your extension is built on an app with a backend, then you need to deploy your app to a hosting service first. Shopify hosts only your extension's code.

**Note:**

Your compiled UI extension bundle can't exceed 64 KB. Shopify enforces this limit at deployment to ensure fast loading times and optimal performance. Learn how to [analyze your bundle size](https://shopify.dev/docs/apps/build/app-extensions#analyzing-bundle-size).

### Deploy your extension

```terminal
shopify app deploy
```

### Versioning

Polaris reference docs follow [Shopify's API versioning policy](https://shopify.dev/docs/api/usage/versioning). Each stable version is supported for a minimum of 12 months. Older versions continue to work, they just won't have dedicated docs on Shopify.dev. [Shopify CLI](https://shopify.dev/docs/api/shopify-cli) already prevents deploys targeting API versions older than 12 months, so we recommend keeping your extensions on a supported version.

---

## Tutorials and resources

Deepen your understanding of admin UI extensions with these tutorials and community resources.

### Tutorials

[Tutorial - Build an admin action UI extension](https://shopify.dev/docs/apps/build/admin/actions-blocks/build-admin-action)

[Tutorial - Build an admin block UI extension](https://shopify.dev/docs/apps/build/admin/actions-blocks/build-admin-block)

[Tutorial - Connect admin UI extensions](https://shopify.dev/docs/apps/build/admin/actions-blocks/connect-admin-extensions)

[Tutorial - Connect UI extensions to your app's backend](https://shopify.dev/docs/apps/build/admin/actions-blocks/connect-app-backend)

[Tutorial - Hide admin UI extensions](https://shopify.dev/docs/apps/build/admin/actions-blocks/hide-extensions)

[Tutorial - Build an admin print action UI extension](https://shopify.dev/docs/apps/build/admin/actions-blocks/build-admin-print-action)

[Tutorial - Build a discounts UI with admin UI extensions](https://shopify.dev/docs/apps/build/discounts/build-ui-extension)

[Tutorial - Add a product configuration extension](https://shopify.dev/docs/apps/build/product-merchandising/bundles/product-configuration-extension/add-merchant-config-ui)

[Tutorial - Build a customer segment template extension](https://shopify.dev/docs/apps/build/marketing-analytics/customer-segments/build-a-template-extension)

[Tutorial - Build a customer segment action extension](https://shopify.dev/docs/apps/build/marketing-analytics/customer-segments/build-an-action-extension)

[Tutorial - Use extensions to surface app data](https://shopify.dev/docs/apps/build/sidekick/build-app-data)

### Community resources

[Reference - Developer changelog](https://shopify.dev/changelog)

[Community - Community forum for admin UI extensions](https://community.shopify.dev/tag/admin-ui-extensions)

---

### Build an admin action UI extension (tutorial)

> Fonte: https://shopify.dev/docs/apps/build/admin/actions-blocks/build-admin-action

# Build an admin action UI extension

This guide is the first part of a five-part tutorial series that describes how to build UI extensions that display as actions and blocks in Shopify admin. It demonstrates how to build a UI extension for an action that enables users to log trackable, resolvable issues on products.

![The issue tracker action over a modal. The action has input fields for a title and description.](https://shopify.dev/assets/assets/admin/admin-actions-and-block/build-an-admin-action/opened-action-BgrhvQ6k.png)

## What you'll learn

In this tutorial, you'll learn how to do the following tasks:

* Create a UI extension for an action that displays on the product details page in Shopify admin.
* Configure metafield definitions using TOML declarative custom data definitions.
* Fetch information to populate the UI extension's initial state.
* Create an interface for the UI extension, allowing it to gather input from merchants.
* Update the data using GraphQL based on merchant input.
* Run the UI extension locally and test it on a dev store.

## Requirements

[Create a Partner account](https://www.shopify.com/partners)

[Create a dev store](https://shopify.dev/docs/apps/tools/development-stores#create-a-development-store-to-test-your-app)

[Scaffold an app](https://shopify.dev/docs/apps/build/scaffold-app)

Scaffold an app with the `write_products` access scope that uses [Shopify CLI 3.78 or higher](https://shopify.dev/docs/api/shopify-cli#upgrade).

* If you created a React Router app, then the `write_products` access scope is automatically granted to your app.
* If you created an extension-only app, then you need to explicitly grant the `write_products` access scope to your [custom app](https://shopify.dev/docs/apps/auth/access-token-types/admin-app-access-tokens#changing-api-scopes).
* Add a product to your dev store. The product shouldn't have any custom variants at the start of this tutorial.

## Project

[View on GitHub](https://github.com/Shopify/example-admin-action-and-block-preact)

## Create a new UI extension

Use Shopify CLI to [generate starter code](https://shopify.dev/docs/api/shopify-cli/app/app-generate-extension) for your UI extension.

Navigate to your app directory:

### Terminal

```bash
cd <directory>
```

Run the following command to create a new admin action UI extension:

### Terminal

```bash
shopify app generate extension --template admin_action --name issue-tracker-action
```

The command creates a new UI extension template in your app's `extensions` directory with the following structure:

### Admin action structure

```text
extensions/issue-tracker-action
  ├── README.md
  ├── locales
  │   ├── en.default.json // The default locale for the extension
  │   └── fr.json // The French language translations for the extension
  ├── package.json
  ├── shopify.extension.toml // The config file for the extension
  ├── tsconfig.json
  ├── shopify.d.ts // Provides types for components and APIs available to the extension
  └── src
      └── AdminAction.jsx // The code that defines the action's UI and behavior
```

## Configure the metafield definition

Add a [declarative custom data definition](https://shopify.dev/docs/apps/build/custom-data/declarative-custom-data-definitions) to define the metafield that will store issue tracker data. This allows your extension to persistently store issue tracking data for products.

### /shopify.app.toml

```toml
# Learn more about configuring your app at https://shopify.dev/docs/apps/tools/cli/configuration


client_id = "1a07dcc482fc60f45a4cc669a88438ea"
name = "2025-04-09-app-ui-project"
handle = "2025-04-09-app-ui-project"
application_url = "https://example.com/"
embedded = true


[build]
include_config_on_deploy = true
automatically_update_urls_on_dev = true


[webhooks]
api_version = "2025-04"


  [[webhooks.subscriptions]]
  topics = [ "app/uninstalled" ]
  uri = "/webhooks/app/uninstalled"


  [[webhooks.subscriptions]]
  topics = [ "app/scopes_update" ]
  uri = "/webhooks/app/scopes_update"


[access_scopes]
# Learn more at https://shopify.dev/docs/apps/tools/cli/configuration#access_scopes
scopes = "write_products,read_orders"


[auth]
redirect_urls = [ "https://example.com/api/auth" ]


[pos]
embedded = false


[product.metafields.app.issues]
type = "json"
name = "Issue Tracker"
description = "Tracks issues logged for this product"
access.admin = "merchant_read_write"
```

## Create an interface for the UI extension

To create an interface for the UI extension, complete the following steps:

### Review the configuration

The UI extension's static configuration is stored in its `.toml` file. To display the issue tracker on product detail pages, validate that the `target` is set to `admin.product-details.action.render`.

[admin.product-details.action.render](https://shopify.dev/docs/api/admin-extensions/latest/targets)

### /extensions/issue-tracker-action/shopify.extension.toml

```toml
api_version = "2026-04"


[[extensions]]
# Change the merchant-facing name of the extension in locales/en.default.json
name = "t:name"
handle = "issue-tracker-action"
uid = "799a1dec-3979-a563-117b-d4e5cd6b9808fbc17d0d"
type = "ui_extension"


# Only 1 target can be specified for each Admin action extension
[[extensions.targeting]]
module = "./src/ActionExtension.jsx"
target = "admin.product-details.action.render"
```

### Update title

To update the name that displays when merchants select the action from the menu, edit the `name` value in the locale files. To localize strings, an admin action UI extension uses the [i18n API](https://shopify.dev/docs/api/admin-extensions/api/action-extension-api#actionextensionapi-propertydetail-i18n). This API gives you access to strings stored in locale files, and automatically chooses the correct string for the current user's locale.

### Translate title

Optionally translate your title to French.

### Note the export

You can view the source of your extension in the `src/ActionExtension.jsx` file. This file defines an `extension` function that calls the `render` method from Preact. You can create the extension's body by using the web components that are automatically provided.

Admin UI extensions are rendered using [Remote DOM](https://github.com/Shopify/remote-dom/tree/remote-dom), which is a fast and secure remote-rendering framework. Because Shopify renders the UI remotely, components used in the extensions must comply with a contract in the Shopify host. We provide these components automatically to the extension.

### /extensions/issue-tracker-action/src/ActionExtension.jsx

```jsx
import { render } from "preact";
import { useCallback, useEffect, useState } from "preact/hooks";
import { getIssues, updateIssues } from "./utils";


export default async () => {
  {
    render(<Extension />, document.body);
  }


  function generateId(allIssues) {
    return !allIssues?.length ? 0 : allIssues[allIssues.length - 1].id + 1;
  }


  function validateForm({ title, description }) {
    return {
      isValid: Boolean(title) && Boolean(description),
      errors: {
        title: !title,
        description: !description,
      },
    };
  }


  function Extension() {
    const { close, data, i18n } = shopify;
    const [issue, setIssue] = useState({ title: "", description: "" });
    const [allIssues, setAllIssues] = useState([]);
    const [formErrors, setFormErrors] = useState(null);
    const { title, description } = issue;


    useEffect(() => {
      getIssues(data.selected[0].id).then((issues) =>
        setAllIssues(issues || []),
      );
      // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);


    const onSubmit = useCallback(async () => {
      const { isValid, errors } = validateForm(issue);
      setFormErrors(errors);


      if (isValid) {
        // Commit changes to the database
        await updateIssues(data.selected[0].id, [
          ...allIssues,
          {
            id: generateId(allIssues),
            completed: false,
            ...issue,
          },
        ]);
        // Close the modal using the 'close' API
        close();
      }
    }, [issue, data.selected, allIssues, close]);


    return (
      <s-admin-action heading={i18n.translate("name")}>
        <s-button slot="primary-action" onClick={onSubmit}>
          {i18n.translate("issue-create-button")}
        </s-button>
        <s-button slot="secondary-actions" onClick={close}>
          {i18n.translate("issue-cancel-button")}
        </s-button>
        <s-text-field
          value={title}
          error={
            formErrors?.title ? i18n.translate("issue-title-error") : undefined
          }
          onChange={(event) =>
            setIssue((prev) => ({ ...prev, title: (/** @type {HTMLInputElement} */ (event.target)).value }))
          }
          label={i18n.translate("issue-title-label")}
          maxLength={50}
        />
        <s-box padding-block-start="large">
          <s-text-area
            value={description}
            error={
              formErrors?.description
                ? i18n.translate("issue-description-error")
                : undefined
            }
            onChange={(event) =>
              setIssue((prev) => ({ ...prev, description: (/** @type {HTMLInputElement} */ (event.target)).value }))
            }
            label={i18n.translate("issue-description-label")}
            max-length={300}
          />
        </s-box>
      </s-admin-action>
    );
  }
};
```

### Render a UI

To build your action's UX, return some components from `src/ActionExtension.jsx`.

_(Il codice del componente `ActionExtension.jsx` è identico al blocco mostrato sopra: vengono renderizzati `s-admin-action`, `s-button` (primary/secondary), `s-text-field` e `s-text-area`.)_

**Tip:**

At this point, you can use the Dev Console to [run your app's server and preview your UI extension](#test-the-ui-extension). As you preview the UI extension, changes to its code automatically cause it to reload.

## Write the UI extension's logic and connect to the GraphQL Admin API

After you've configured the metafield definition and defined the extension's UI, use standard Preact tooling to write the logic that controls it.

When you're writing UI extensions, you don't need proxy calls to the [GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql) through your app's backend. Instead, your UI extension can use [direct API access](https://shopify.dev/docs/api/admin-extensions#directapiaccess) to create requests directly using `fetch`. For merchants, this makes UI extensions more performant and responsive.

In this step, you'll create a utility file to contain GraphQL queries that the UI extension uses to read and write data to the metafield API.

Your app can also get data from the extension APIs, which includes data on the current resource from the `data` API.

Add new file at `./src/utils.js`. This file contains the GraphQL queries that the extension uses to read and write metafield data (the metafield definition is handled by TOML).

[metafieldsSet](https://shopify.dev/docs/api/admin-graphql/latest/mutations/metafieldsSet)

Import the `getIssues` utility method and use it to update the extension state. Call the `updateIssues` utility method when the form is submitted. _(Il componente importato è quello mostrato sopra; le utility sono definite in `./src/utils.js`, riportato qui sotto.)_

## Test the UI extension

After you've built the UI extension, test it with the following steps:

1. Navigate to your app directory:

   ### Terminal

   ```bash
   cd <directory>
   ```

2. To build and preview your app, either start or restart your server with the following command:

   ### Terminal

   ```bash
   shopify app dev
   ```

3. Press `p` to open the Dev Console.

4. In the Dev Console, click on the preview link for the issue tracker extension.

5. The product details page opens. If you don't have a product in your store, then you need to create one.

6. To launch your extension, select it from the **More actions** menu found at the top-right of the page.

7. Fill out the modal and click **Create**.

8. Validate that the metafield is created and populated with your issue text, by navigating to the metafields card at the bottom of the page, and select **Show all**.

Update your code to the control the form and write the data to the admin metafield API using the methods from `./src/utils.js`.

### /extensions/issue-tracker-action/locales/en.default.json

```json
{
  "name": "Create an issue",
  "create-issue-heading": "Create an issue",
  "edit-issue-heading": "Edit your issue",
  "issue-description-label": "Description",
  "issue-description-error": "Please enter a description",
  "issue-title-label": "Title",
  "issue-title-error": "Please enter a title",
  "issue-create-button": "Create",
  "issue-cancel-button": "Cancel",
  "issue-save-button": "Save",
  "issue-edit-button": "Edit",
  "issue-generate-button": "Generate issue",
  "issue-generate-banner-text": "Automatically fill the issue based on past customer feedback"
}
```

### /extensions/issue-tracker-action/locales/fr.json

```json
{
  "name": "Créer un problème",
  "create-issue-heading": "Créer un problème",
  "edit-issue-heading": "Modifier votre problème",
  "issue-description-label": "Description",
  "issue-description-error": "Veuillez entrer une description",
  "issue-title-label": "Titre",
  "issue-title-error": "Veuillez entrer un titre",
  "issue-create-button": "Create",
  "issue-cancel-button": "Annuler",
  "issue-save-button": "Enregistrer",
  "issue-edit-button": "Modifier",
  "issue-generate-button": "Générer un problème",
  "issue-generate-banner-text": "Remplir automatiquement le problème en fonction des retours clients passés"
}
```

### /extensions/issue-tracker-action/src/utils.js

```javascript
export async function updateIssues(id, newIssues) {
  // This example uses metafields to store the data. For more information, refer to https://shopify.dev/docs/apps/custom-data/metafields.
  return await makeGraphQLQuery(
    `mutation SetMetafield($ownerId: ID!, $namespace: String!, $key: String!, $type: String!, $value: String!) {
      metafieldsSet(metafields: [{ownerId: $ownerId, namespace: $namespace, key: $key, type: $type, value: $value}]) {
        metafields {
          id
          namespace
          key
          jsonValue
        }
        userErrors {
          field
          message
          code
        }
      }
    }`,
    {
      ownerId: id,
      namespace: "$app",
      key: "issues", 
      type: "json",
      value: JSON.stringify(newIssues),
    },
  );
}


export async function getIssues(productId) {
  // This example uses metafields to store the data. For more information, refer to https://shopify.dev/docs/apps/custom-data/metafields.
  const res = await makeGraphQLQuery(
    `query Product($id: ID!) {
      product(id: $id) {
        metafield(namespace: "$app", key: "issues") {
          value
        }
      }
    }`,
    { id: productId },
  );


  if (res?.data?.product?.metafield?.value) {
    return JSON.parse(res.data.product.metafield.value);
  }
}


async function makeGraphQLQuery(query, variables) {
  const graphQLQuery = {
    query,
    variables,
  };


  const res = await fetch("shopify:admin/api/graphql.json", {
    method: "POST",
    body: JSON.stringify(graphQLQuery),
  });


  if (!res.ok) {
    console.error("Network error");
  }


  return await res.json();
}
```

## Next steps

[Admin block UI extension](https://shopify.dev/docs/apps/admin/admin-actions-and-blocks/build-an-admin-block)

In the next tutorial in this series, you'll build a UI extension that lists the issues created by your action extension. This new extension will display as a block in Shopify admin.

[Targets](https://shopify.dev/docs/api/admin-extensions/latest/targets) — Learn about the various places in Shopify admin where UI extensions can be displayed.

[Web components](https://shopify.dev/docs/api/admin-extensions/latest/web-components) — Learn about the full set of available web components for writing admin UI extensions.

---

### Build an admin block UI extension (tutorial)

> Fonte: https://shopify.dev/docs/apps/build/admin/actions-blocks/build-admin-block

# Build an admin block UI extension

This guide is the second part of a five-part tutorial series that describes how to build UI extensions that display as actions and blocks in Shopify admin. Before starting this guide, you'll need to build or copy the admin action UI extension from the [Build a UI extension for an admin action](https://shopify.dev/docs/apps/build/admin/actions-blocks/build-admin-action) tutorial.

So far, you've created a UI extension for an action that enables buyers to create issues for a product. However, merchants need an easy way to see them. This guide demonstrates how to create a UI extension for a block in Shopify admin that displays buyer-created issues for a product.

![The new block UI extension, at the bottom of the page. Two issues, created with the action, display.](https://shopify.dev/assets/assets/admin/admin-actions-and-block/build-an-admin-block/block-on-page-csb-BneaXTRv.png)

## What you'll learn

In this tutorial, you'll learn how to do the following tasks:

* Create a UI extension for a block that displays on the product details page.
* Configure metafield definitions using TOML declarative custom data definitions.
* Fetch information to populate the UI extension's initial state.
* Connect the UI extension to Shopify admin's contextual save bar, when gathering input, for seamless page editing.
* Run the UI extension locally and test it on a dev store.

## Requirements

* [Create a Partner account](https://www.shopify.com/partners)
* [Create a dev store](https://shopify.dev/docs/apps/tools/development-stores#create-a-development-store-to-test-your-app)
* [Scaffold an app](https://shopify.dev/docs/apps/build/scaffold-app)
* Scaffold an app with the `write_products` access scope that uses [Shopify CLI 3.78 or higher](https://shopify.dev/docs/api/shopify-cli#upgrade).
  * If you created a React Router app, then the `write_products` access scope is automatically granted to your app.
  * If you created an extension-only app, then you need to explicitly grant the `write_products` access scope to your [custom app](https://shopify.dev/docs/apps/auth/access-token-types/admin-app-access-tokens#changing-api-scopes).
  * Add a product to your dev store. The product should not have any custom variants at the start of this tutorial.
* [Build an admin action UI extension](https://shopify.dev/docs/apps/admin/admin-actions-and-blocks/build-an-admin-action)
* Complete or copy the code from the [Build an admin action UI extension](https://shopify.dev/docs/apps/build/admin/actions-blocks/build-admin-action) tutorial.

## Project

[View on GitHub](https://github.com/Shopify/example-admin-action-and-block-preact)

## Create an admin block UI extension

Use Shopify CLI to [generate starter code](https://shopify.dev/docs/api/shopify-cli/app/app-generate-extension) for your UI extension.

Navigate to your app directory:

```bash
cd <directory>
```

Run the following command to create a new admin block UI extension:

```bash
shopify app generate extension --template admin_block --name issue-tracker-block
```

The command creates a new extension template in your app's `extensions` directory with the following structure:

```text
extensions/issue-tracker-block
  ├── README.md
  ├── locales
  │   ├── en.default.json // The default locale for the extension
  │   └── fr.json // The French language translations for the extension
  ├── package.json
  ├── shopify.extension.toml // The config file for the extension
  ├── tsconfig.json
  ├── shopify.d.ts // Provides types for components and APIs available to the extension
  └── src
      └── BlockExtension.jsx // The code that defines the block's UI and behavior
```

## Configure the metafield definition

Use [declarative custom data definitions](https://shopify.dev/docs/apps/build/custom-data/declarative-custom-data-definitions) to define the metafield that will store issue tracker data.

> **Note**: If your `shopify.app.toml` file already contains this metafield definition (for example, from completing the [Build an admin action](https://shopify.dev/docs/apps/build/admin/actions-blocks/build-admin-action) tutorial), you can skip this step.

_(Il file `shopify.app.toml` è identico a quello del tutorial admin action: stesso blocco `[product.metafields.app.issues]` con `type = "json"`, `access.admin = "merchant_read_write"`.)_

## Create an interface for the UI extension

### Review the configuration

The UI extension's static configuration is stored in its `.toml` file. To display the issue tracker on product detail pages, set the target to `admin.product-details.block.render`.

[admin.product-details.block.render](https://shopify.dev/docs/api/admin-extensions/latest/targets)

### /extensions/issue-tracker-block/shopify.extension.toml

```toml
api_version = "2026-04"

[[extensions]]
# Change the merchant-facing name of the extension in locales/en.default.json
name = "t:name"
handle = "issue-tracker-block"
uid = "5c534720-d393-1436-d4d2-438d615062be6175f52d"
type = "ui_extension"

# Only 1 target can be specified for each Admin block extension
[[extensions.targeting]]
module = "./src/BlockExtension.jsx"
target = "admin.product-details.block.render"
```

### Update title

To update the name that displays when merchants select the action from the menu, edit the `name` value in the locale files. To localize strings, a UI extension for an admin block uses the [i18n API](https://shopify.dev/docs/api/admin-extensions/api/block-extension-api#blockextensionapi-propertydetail-i18n). This API gives you access to strings stored in locale files, and automatically chooses the correct string for the current user's locale.

### Note the export

You can view the source of your extension in the `src/BlockExtension.jsx` file. This file defines a functional Preact component that's exported to run at the extension's target. You can create the extension's body by using the web components that are automatically provided.

Admin UI extensions are rendered using [Remote DOM](https://github.com/Shopify/remote-dom/tree/remote-dom), which is a fast and secure remote-rendering framework. Because Shopify renders the UI remotely, components used in the extensions must comply with a contract in the Shopify host. We provide these components automatically to the extension.

### /extensions/issue-tracker-block/src/BlockExtension.jsx

```jsx
import { render } from "preact";
import { useEffect, useMemo, useState } from "preact/hooks";

import { updateIssues, getIssues } from "./utils";

export default async () => {
  {
    render(<Extension />, document.body);
  }
  const PAGE_SIZE = 3;

  function Extension() {
    const { data, i18n } = shopify;

    const [loading, setLoading] = useState(true);
    const [_, setInitialValues] = useState([]);
    const [issues, setIssues] = useState([]);
    const [currentPage, setCurrentPage] = useState(1);

    const productId = data.selected[0].id;
    const issuesCount = issues.length;
    const totalPages = issuesCount / PAGE_SIZE;

    useEffect(() => {
      (async function getProductInfo() {
        // Load the product's metafield of type issues
        const productData = await getIssues(productId);

        setLoading(false);
        if (productData?.data?.product?.metafield?.value) {
          const parsedIssues = JSON.parse(
            productData.data.product.metafield.value,
          );
          setInitialValues(
            parsedIssues.map(({ completed }) => Boolean(completed)),
          );
```

> **Note:** Il codice sorgente del componente `BlockExtension.jsx` riportato nella documentazione è troncato allo stesso punto (caricamento dati e impostazione della paginazione `PAGE_SIZE = 3`). Il file completo è disponibile nel repository di esempio: https://github.com/Shopify/example-admin-action-and-block-preact

### Render a UI

To build your block's UX, return some components from `src/BlockExtension.jsx`. You'll create a simple UI to list out your product issues.

## Write the UI extension's logic and connect to the GraphQL Admin API

After defining the extension's UI, use standard Preact tooling to write the logic that controls it.

When you're writing UI extensions, you don't need proxy calls to the [GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql) through your app's backend. Instead, your UI extension can use [direct API access](https://shopify.dev/docs/api/admin-extensions#directapiaccess) to create requests directly using `fetch`. For merchants, this makes UI extensions more performant and responsive. This guide includes a utility file for GraphQL queries.

Your app can also get data from the extension APIs, which includes data on the current resource from the `data` API.

First, you'll need to populate the UI extension's interface with existing issue data. To do this, use direct API calls to query the Issue Tracker metafield configured in the previous step, and use the metafield data to populate a paginated list in the UI extension's block. Paginate issues to prevent the block from becoming too tall and difficult for users to use.

Create a new file at `./src/utils.js` and add the GraphQL queries that the extension uses to read and write metafield data (the metafield definition is handled by TOML).

[metafieldsSet](https://shopify.dev/docs/api/admin-graphql/latest/mutations/metafieldsSet)

### Get initial data and set up pagination

Use the `getIssues` utility method to fetch the initial data for the UI extension. Add a function to manage pagination.

> **Tip:** At this point, you can use the Dev Console to [run your app's server and preview your UI extension](#test-the-ui-extension). As you preview the UI extension, changes to its code automatically cause it to reload.

## Update data and integrate with the page's contextual save bar

Next, you'll create a status dropdown and a delete button that enables users to either mark issues as completed or remove them entirely. When you create the status dropdown, you'll integrate it with the page's contextual save bar. This enables users to save changes to your block using the same controls that they would use to save changes to other fields in the Shopify admin.

Import the `updateIssues` utility method and use it to update the UI extension state.

### Handle status changes and deleting issues

Add the functions to handle deleting and changing the status. Call the `updateIssues` utility method when the issue is deleted and when the form is submitted.

> **Tip:** For more information on how to integrate with the contextual save bar, refer to this [reference](https://shopify.dev/docs/api/admin-extensions/latest#using-forms).

## Test the UI extension

After you've built the UI extension, test it with the following steps:

1. Navigate to your app directory:

   ```bash
   cd <directory>
   ```

2. To build and preview your app, either start or restart your server with the following command:

   ```bash
   shopify app dev
   ```

3. Press `p` to open the Dev Console

4. In the extension list for your app, click on the preview link for the issue tracker UI extension. The product details page opens. If you don't have a product in your store, then you need to create one.

5. To find your block, scroll to the bottom of the page. It should display the issues that you've created so far.

6. When you change the status of an issue, the contextual save bar should display. The change is saved when you click the Save button.

![The new block UI extension, at the bottom of the page. Issues that have been created with the action display.](https://shopify.dev/assets/assets/admin/admin-actions-and-block/build-an-admin-block/block-on-page-csb-BneaXTRv.png)

## Configuration files

### /extensions/issue-tracker-block/locales/en.default.json

```json
{
  "name": "Product Issues",
  "issue-column-heading": "Issue",
  "status-column-heading": "Status",
  "select-label": "Status",
  "option-todo": "Todo",
  "option-completed": "Completed",
  "delete-issue-button": "Delete issue",
  "edit-issue-button": "Edit issue",
  "add-issue-button": "Add issue",
  "collapsed-summary": "Not enough product variants",
  "no-issues-text": "No issues for this product",
  "add-first-issue-button": "Add your first issue"
}
```

### /extensions/issue-tracker-block/locales/fr.json

```json
{
  "name": "Problèmes de produit",
  "issue-column-heading": "Problème",
  "status-column-heading": "Statut",
  "select-label": "Statut",
  "option-todo": "À faire",
  "option-completed": "Terminé",
  "delete-issue-button": "Supprimer le problème",
  "edit-issue-button": "Modifier le problème",
  "add-issue-button": "Ajouter un problème",
  "collapsed-summary": "Pas assez de variantes de produit",
  "no-issues-text": "Aucun problème pour ce produit",
  "add-first-issue-button": "Ajouter votre premier problème"
}
```

### /extensions/issue-tracker-block/src/utils.js

```javascript
export async function updateIssues(id, newIssues) {
  // This example uses metafields to store the data. For more information, refer to https://shopify.dev/docs/apps/custom-data/metafields.
  return await makeGraphQLQuery(
    `mutation SetMetafield($ownerId: ID!, $namespace: String!, $key: String!, $type: String!, $value: String!) {
      metafieldsSet(metafields: [{ownerId: $ownerId, namespace: $namespace, key: $key, type: $type, value: $value}]) {
        metafields {
          id
          namespace
          key
          jsonValue
        }
        userErrors {
          field
          message
          code
        }
      }
    }`,
    {
      ownerId: id,
      namespace: "$app",
      key: "issues", 
      type: "json",
      value: JSON.stringify(newIssues),
    },
  );
}

export async function getIssues(productId) {
  // This example uses metafields to store the data. For more information, refer to https://shopify.dev/docs/apps/custom-data/metafields.
  const res = await makeGraphQLQuery(
    `query Product($id: ID!) {
      product(id: $id) {
        metafield(namespace: "$app", key: "issues") {
          value
        }
      }
    }`,
    { id: productId },
  );

  if (res?.data?.product?.metafield?.value) {
    return JSON.parse(res.data.product.metafield.value);
  }
}

async function makeGraphQLQuery(query, variables) {
  const graphQLQuery = {
    query,
    variables,
  };

  const res = await fetch("shopify:admin/api/graphql.json", {
    method: "POST",
    body: JSON.stringify(graphQLQuery),
  });

  if (!res.ok) {
    console.error("Network error");
  }

  return await res.json();
}
```

## Next steps

- [Connect admin and block UI extensions](https://shopify.dev/docs/apps/admin/admin-actions-and-blocks/connect-action-and-block) — In the next tutorial in this series, you'll connect your admin action UI extension to your admin block UI extension, to enable issue editing.
- [Hide UI extensions](https://shopify.dev/docs/apps/build/admin/actions-blocks/hide-extensions) — Learn how to hide action UI extensions when they're not useful or relevant.
- [Targets](https://shopify.dev/docs/api/admin-extensions/latest/targets) — Learn about the various places that Shopify admin can display UI extensions.
- [Web components](https://shopify.dev/docs/api/admin-extensions/latest/web-components) — Learn about the full set of available web components for writing admin UI extensions.
- [Deploy](https://shopify.dev/docs/apps/deployment/app-versions) — Learn how to deploy your UI extensions to merchants.

---

## App Home UI extensions

Mini-TOC:
- [App Home UI extensions (tutorial)](#app-home-ui-extensions-tutorial)

### App Home UI extensions (tutorial)

> Fonte: https://shopify.dev/docs/apps/build/app-home/app-home-ui-extensions

# App Home UI extensions

App Home UI extensions are a Shopify-hosted alternative to the developer-hosted iframe model. You build your app's main page as a Preact UI extension that renders in the App Home area of Shopify admin, with no backend server to host or maintain. This path is for custom-distribution apps that don't need server-side logic. For most apps, the iframe model with React Router is still the recommended path.

To learn more about which option is right for your use case, see the Apps in App Home page.

---

## What you'll learn

In this tutorial, you'll learn how to do the following tasks:

* Scaffold an extension-only app with an App Home UI extension using Shopify CLI.
* Run your extension in a dev store and preview your changes.
* Deploy the extension as part of an app version.

---

## Requirements

* You're a user with app development permissions and have created a dev store.
* You're using the latest version of Shopify CLI.
* You're using the latest version of Chrome or Firefox.

---

## Step 1: Scaffold an extension-only app

Scaffold a new app and select the extension-only template. The template includes an App Home UI extension by default, so the scaffolded app already has a templated app with a landing page.

1. Navigate to the directory where you want to create your app.

2. Run the following command:

```terminal
shopify app init
```

3. When prompted, enter a name for your app and select **Build an extension-only app**.

   Shopify CLI creates a new app with an `extensions/app-home/` folder containing the configuration and source files for your App Home UI extension.

---

## Step 2: Examine the generated extension

Open the new app in your editor and look at the files that Shopify CLI generated for the extension.

1. Open `extensions/app-home/shopify.extension.toml`.

   The file declares a UI extension that targets `admin.app.home.render`. The `module` property points to the Preact entry file that renders the page.

```toml
api_version = "2026-07"


[[extensions]]
# Change the merchant-facing name of the extension in locales/en.default.json
name = "t:name"
handle = "app-home"
uid = "83247469-d4a8-2612-c903-5468f6914aaa918849e8"
type = "ui_extension"


  # Only 1 target can be specified for each Admin block extension
  [[extensions.targeting]]
  module = "./src/AppHome.jsx"
  target = "admin.app.home.render"


  [access_scopes]
  # Learn more at https://shopify.dev/docs/apps/tools/cli/configuration#access_scopes
  scopes = "write_metaobject_definitions,write_metaobjects,write_products"
```

   For the full set of configurable properties, see Configuring app extensions.

2. Open `extensions/app-home/src/AppHome.jsx`.

   This is the entry module for the extension. It provides a single-page app skeleton that uses client-side routing to serve multiple pages in the Shopify admin.

```tsx
import {render} from 'preact';
import {LocationProvider, ErrorBoundary, Router, Route} from 'preact-iso';


import HomePage from './pages/HomePage.jsx';
import FaqPage from './pages/FaqPage.jsx';
import NotFoundPage from './pages/NotFoundPage.jsx';


export default async () => {
  render(<App />, document.body);
};


function App() {
  return (
    <LocationProvider>
      <ErrorBoundary>
        <Router>
          <Route path="/" component={HomePage} />
          <Route path="/faq/:id" component={FaqPage} />
          <Route default component={NotFoundPage} />
        </Router>
      </ErrorBoundary>
    </LocationProvider>
  );
}
```

   The home page for your app is defined in `extensions/app-home/src/pages/HomePage.jsx`. The HomePage serves as the index view for an FAQ-manager app and displays either an empty state or a table listing all the app's FAQs. `FaqPage.jsx` handles both creation (`/faq/new`) and editing (`/faq/:id`) in a single form-based detail view. The two pages are connected through client-side routing using the `preact-iso` library.

---

## Step 3: Run your app

Start a local development server and preview the extension in your dev store's admin.

1. From the app's root directory, run the following command:

```terminal
shopify app dev
```

2. When prompted, select your dev store.

3. Press `p` to open the preview URL.

Your dev store opens at your app's home page. To open the FAQ editor, click **Create FAQ**.

---

## Step 4: Deploy your extension

App Home UI extensions deploy as part of an app version. There's no separate hosting step.

1. From the app's root directory, run `shopify app deploy` to release a new app version.

2. Install the released version on your dev store with custom distribution. For details, see Select a distribution method and Deploy app versions.

---

## Next steps

* **App Home UI extension reference** — Explore the target, target APIs, and web components available to App Home UI extensions.
* **Configure app extensions** — See the full list of configurable properties for the `shopify.extension.toml` file.
* **Build an extension-only app** — Learn what other extensions you can include in an extension-only app.
* **Apps in App Home** — Compare the iframe and UI extension models, and decide which is right for your app.

---

## Checkout UI extensions

Mini-TOC:
- [Apps in Checkout (overview)](#apps-in-checkout-overview)
- [Technologies for customizing Shopify checkout](#technologies-for-customizing-shopify-checkout)
- [Start building for checkout](#start-building-for-checkout)
- [Checkout UI extensions (reference index)](#checkout-ui-extensions-reference-index)

### Apps in Checkout (overview)

> Fonte: https://shopify.dev/docs/apps/build/checkout

# Apps in Checkout

Merchants use [Shopify checkout](https://help.shopify.com/manual/checkout-settings) to accept orders and receive payments wherever they sell online. To augment Shopify checkout with new functionality, build an app with extensions.

---

## How it Works

After a customer adds products to a cart, they use Shopify checkout to enter their customer, shipping, and payment information before placing the order.

To extend checkout, apps can use extensions. For example, apps can use extensions to offer a customer free shipping or other discounts, depending on the contents of their cart.

To install apps on their store, merchants can use the Shopify admin. There, they can use the [checkout editor](https://shopify.dev/docs/apps/build/checkout/test-checkout-ui-extensions#test-the-extension-in-the-checkout-editor) to place a block for a [checkout UI extension](https://shopify.dev/api/checkout-ui-extensions) in the checkout experience.

![Actions that a developer, customer, and merchant take in connection to Shopify checkout](https://shopify.dev/assets/assets/images/apps/checkout/what-is-checkout-BFffD-s0.png)

---

## Customization Options

There are various types of Shopify Extensions that you can use to customize checkout:

* UI extensions
* Functions
* Web pixel extensions
* Payments extensions

All customization options are easy to install and upgrade-safe, enabling merchants to benefit from Shopify releases new products such as [Shop Pay](https://shopify.dev/docs/apps/build/checkout/test-checkout-ui-extensions#test-with-shop-pay), or features such as [One-page checkout](https://shopify.dev/docs/apps/build/checkout/test-checkout-ui-extensions#one-page-checkout).

For a detailed breakdown of the technologies that can be used to customize checkout, and the ways that you can extend checkout, refer to the [options for customizing Shopify checkout](https://shopify.dev/docs/apps/build/checkout/technologies).

**Note:**

Checkout apps and extensions have [design requirements](https://shopify.dev/docs/apps/launch/app-requirements-checklist#design-requirements-for-checkout-apps) that apply to custom apps as well as public apps. Be sure that your app meets [all requirements](https://shopify.dev/docs/apps/launch/app-requirements-checklist) for its functionality and distribution type.

---

## Getting Started

To learn how to customize and extend checkout, read the following tutorials.

### Checkout UI Extensions Tutorials

**[Pre-purchase product offers](https://shopify.dev/docs/apps/build/checkout/product-offers/build-a-pre-purchase-offer)** — Build a pre-purchase upsell offer that prompts the customer to add a product to their order.

**[Post-purchase checkout extensions](https://shopify.dev/docs/apps/build/checkout/product-offers/build-a-post-purchase-offer)** — Create a basic example of a post-purchase checkout extension.

**[Thank you and order status extensions](https://shopify.dev/docs/apps/build/checkout/thank-you-order-status/add-survey)** — Build a survey that asks customers how they heard about the store after they made a purchase.

**[Custom banners](https://shopify.dev/docs/apps/build/checkout/fields-banners/add-banner)** — Learn how to add a custom banner to checkout.

**[Custom fields](https://shopify.dev/docs/apps/build/checkout/fields-banners/add-field)** — Learn how to add custom fields to checkout that customers can use to add delivery instructions to their order.

**[Client-side validation](https://shopify.dev/docs/apps/build/checkout/cart-checkout-validation/create-client-side-validation)** — Use a checkout UI extension to validate fields at checkout and block customer progress.

**[Header](https://shopify.dev/docs/apps/build/checkout/customize-header)** — Use a checkout UI extension and the GraphQL Admin API's checkout branding types to customize the checkout header with custom images, including the back to cart link.

**[Footer](https://shopify.dev/docs/apps/build/checkout/customize-footer)** — Use a checkout UI extension and the GraphQL Admin API's checkout branding types to customize the checkout footer with store policies.

**[Address autocomplete](https://shopify.dev/docs/apps/build/checkout/delivery-shipping/address-autocomplete/build-autocomplete)** — Build an extension to customize the address autocomplete provider for the delivery and billing address forms in checkout.

### Shopify Functions Tutorials

**[Build a discount function](https://shopify.dev/docs/apps/build/discounts/build-discount-function)** — Use Shopify Functions to create a new discount type for users.

**[Create a payments function](https://shopify.dev/docs/apps/build/checkout/payments/create-payments-function)** — Use Shopify Functions to hide a payment option offered to customers at checkout.

**[Build a delivery options function](https://shopify.dev/docs/apps/build/checkout/delivery-shipping/delivery-options/build-function)** — Use Shopify Functions to rename a delivery option offered to customers at checkout.

**[Create a server-side validation function](https://shopify.dev/docs/apps/build/checkout/cart-checkout-validation/create-server-side-validation-function)** — Use Shopify Functions to block progress on a checkout when the cart line quantities exceed a limit.

**[Build a location rule function](https://shopify.dev/docs/apps/build/orders-fulfillment/order-routing-apps/location-rules/build-location-rule-function)** — Use Shopify Functions to choose a different order location during checkout.

**[Add a customized bundle function](https://shopify.dev/docs/apps/build/product-merchandising/bundles/add-customized-bundle-function)** — Use Shopify Functions to group products together and sell them as a single unit.

**[Build a fulfillment constraints function](https://shopify.dev/docs/apps/build/orders-fulfillment/order-routing-apps/build-fulfillment-constraints-function)** — Use Shopify Functions to customize fulfillment and delivery strategies.

**[Build a local pickup options function](https://shopify.dev/docs/apps/build/orders-fulfillment/order-routing-apps/build-local-pickup-options-function)** — Use Shopify Functions to generate local pickup delivery options at checkout.

**[Create a local pickup charges function](https://shopify.dev/docs/apps/build/checkout/delivery-shipping/delivery-methods/create-local-pickup-charges-function)** — Use Shopify Functions to create local pickup charges at checkout.

**[Generate a pickup points function](https://shopify.dev/docs/apps/build/checkout/delivery-shipping/delivery-methods/generate-pickup-points)** — Use Shopify Functions to generate pickup point delivery options at checkout.

---

## Build for Checkout

Checkout is where merchants solve a range of cross-cutting problems. Explore the hubs below for guides grouped by topic.

**[Discounts](https://shopify.dev/docs/apps/build/discounts)** — Build custom discount types with Shopify Functions and configure them from the admin or customer accounts.

**[Payments](https://shopify.dev/docs/apps/build/payments)** — Provide customized payment processing for merchants on checkout.

**[Product bundles](https://shopify.dev/docs/apps/build/product-merchandising/bundles)** — Group products together and sell them as a single unit.

**[Purchase options](https://shopify.dev/docs/apps/build/purchase-options)** — Offer subscriptions, pre-orders, and Try Before You Buy.

---

## Upgrade

**Deprecated:**

"`checkout.liquid` is now unsupported for the Information, Shipping, and Payment checkout steps." It and "additional scripts, and script tags are deprecated for the Thank you and Order status pages" with a sunset date of August 28, 2025.

Stores currently using `checkout.liquid` for the **Thank you** and **Order status** pages must [upgrade to Shopify Extensions in Checkout](https://www.shopify.com/checkout#advanced-customizations) before the deadline.

[Shopify Scripts](https://shopify.dev/docs/api/liquid/objects#script) will continue to work alongside Shopify Extensions in checkout until June 30, 2026.

A report identifying your current checkout customizations is available in the Shopify admin. The report provides high-level guidance to map customizations to Shopify Extensions in Checkout. Use this report to simplify your review of your existing customizations and to help you upgrade to Shopify Extensions in Checkout faster. [Learn more](https://help.shopify.com/en/manual/checkout-settings/checkout-extensibility/checkout-upgrade).

To upgrade a `checkout.liquid` customization to Shopify Extensions in Checkout, take one or more of the following actions:

1. Use a public app that's built using extensions.

   We're adding new checkout apps to the Shopify App Store on a regular basis. If there currently isn't a suitable public app for your customization, then consider simplifying your checkout temporarily and adding new apps to your store as they become available.

2. Build a custom app using extensions, or [hire a service partner](https://www.shopify.com/plus/partners/service?type=service&services%5B%5D=141) to build one for you.

In some cases, after you've upgraded you can [revert to `checkout.liquid`](https://help.shopify.com/manual/checkout-settings/checkout-extensibility/checkout-upgrade#revert-to-checkout-liquid) until its sunset dates.

If you're upgrading a store to Shopify Extensions in Checkout, we recommend planning your in-checkout, **Thank you** page, and **Order status** page upgrades together, when possible, for the following benefits:

* Avoid maintaining multiple tech stacks, like UI extensions and `checkout.liquid`.
* Apply styling once to the entire experience.
* Manage one sunset date for `checkout.liquid` rather than one date for pre-purchase pages and another for **Thank you** and **Order status** pages.

  If this isn't possible, then we recommend prioritizing the upgrade for in-checkout pages first and upgrading after-purchase pages after that.

---

## Best Practices

To optimize your app development experience, Shopify has established a set of best practices that you can refer to when developing an app that extends checkout.

**Tip:**

We also recommend getting familiar with Polaris [accessibility](https://polaris.shopify.com/foundations/accessibility) and [content](https://polaris.shopify.com/content/merchant-to-customer) guidelines.

**[Create multi-page extensions](https://shopify.dev/docs/apps/build/checkout/create-multi-page-extensions)** — Learn more about building extensions that can render on any checkout page.

**[UX for checkout](https://shopify.dev/docs/apps/build/checkout/ux-for-checkout)** — Learn how to improve the quality of checkout experiences by following UX guidelines for checkout.

**[Network requests from extensions](https://shopify.dev/docs/api/checkout-ui-extensions/latest/configuration#network-access)** — Learn about Cross-Origin Resource Sharing (CORS) and other security considerations when making network requests to your own server.

**[App Design Guidelines](https://shopify.dev/docs/apps/design-guidelines/)** — Get practical guidance on how to design a user interface for the Shopify admin.

---

## Product Roadmap

Some checkout customization features are in development and will be released later this year. The following are the features on our roadmap and our estimated launch dates:

**Note:**

This roadmap is being shared for informational purposes and is subject to change. Bug fixes and improvements will be added as we hear from the community. Share your feedback or request new features by creating a new issue in the [Shopify developer community forum](https://community.shopify.dev/).

### Shopify Functions

We'll continue to add new Shopify Functions APIs to further customize checkout business logic.

| Milestone | Target |
| - | - |
| Introduced a new [Discount API](https://shopify.dev/docs/api/functions/reference/discount) that supports any combination of product, order, and shipping savings from a single function extension | April 2025 (shipped) |
| Support for cart metafields on function input queries | July 2025 (shipped) |
| Optionally reject discount codes and return custom messages when discounts shouldn't be applied [(Discount API)](https://shopify.dev/docs/api/functions/latest/discount) | Q4 2025 (shipped) |
| Support complex conditions for "Buy X Get Y" discounts [(Discount API)](https://shopify.dev/docs/api/functions/latest/discount) | Q1 2026 |
| Changes to the [Discount API](https://shopify.dev/docs/api/functions/reference/discount) to stack multiple discounts on the same product line item | Q1 2026 |

---

### Technologies for customizing Shopify checkout

> Fonte: https://shopify.dev/docs/apps/build/checkout/technologies

# Technologies for customizing Shopify checkout

This guide describes the various technologies that you can use to customize Shopify checkout. The primary technology for adding custom UI is checkout UI extensions, which are built with [Polaris](https://shopify.dev/docs/api/polaris) — Shopify's unified system for building app interfaces. Polaris provides [targets](https://shopify.dev/docs/api/checkout-ui-extensions/latest/targets) that define where your extension appears in the checkout flow, [target APIs](https://shopify.dev/docs/api/checkout-ui-extensions/latest/target-apis) that give your extension access to checkout data and functionality, and [web components](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components) that render the UI.

---

## Technologies

You can customize Shopify checkout using the following technologies:

| Technology | Customization type | Availability |
| - | - | - |
| [Checkout UI extensions](https://shopify.dev/docs/api/checkout-ui-extensions) | Add custom UI or content to the checkout process and **Order status** page | Shopify Plus. Thank you and Order status extensions are available to all plans except Shopify Starter. Market overrides are available to Advanced. |
| [Checkout UI extensions: post-purchase](https://shopify.dev/docs/apps/build/checkout/product-offers#post-purchase-product-offers) | Add new content to the post-purchase page | All plans except Shopify Starter. Currently in beta. Can be used without restrictions in a [dev store](https://shopify.dev/docs/apps/build/dev-dashboard/development-stores). To use post-purchase extensions on a live store, you need to [request access](https://shopify.dev/docs/apps/build/checkout/product-offers/build-a-post-purchase-offer#step-6-request-access). |
| [GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql/unstable/mutations/checkoutBrandingUpsert) | Customize the look and feel of checkout | Shopify Plus |
| [Shopify Functions](https://shopify.dev/docs/apps/build/functions) | Extend or replace key parts of Shopify's backend with custom logic | All plans except Shopify Starter. Some Function APIs are only available in [feature preview](https://shopify.dev/docs/api/feature-previews). Merchants that have [checkout.liquid](https://shopify.dev/docs/storefronts/themes/architecture/layouts/checkout-liquid) customizations need to [upgrade to Shopify Extensions in Checkout](https://help.shopify.com/manual/checkout-settings/checkout-extensibility/checkout-upgrade) to use Function APIs. |
| [Web pixel extensions](https://shopify.dev/docs/api/pixels) | Track customer behavior | All plans except Shopify Starter. |

The following diagram provides a decision tree for choosing a technology:

![A decision diagram for choosing a specific checkout technology](https://shopify.dev/assets/assets/images/apps/checkout/checkout-decision-tree-CBr55-4f.png)

---

## Use cases

There are a variety of ways that you can customize Shopify checkout. The following table describes some common use cases that you can build:

| Technology | Customization type | Use cases |
| - | - | - |
| [Checkout UI extensions](https://shopify.dev/docs/api/checkout-ui-extensions) | Add custom UI or content to the checkout process and **Order status** page | Show a product offer before a customer completes checkout; capture additional input from customers; build a custom banner; capture a survey or reviews; provide a referral code; add a field validation that blocks customers from progressing. |
| [Checkout UI extensions: post-purchase](https://shopify.dev/docs/apps/build/checkout/product-offers#post-purchase-product-offers) | Add new content to the post-purchase page | Show a product offer after customers have checked out (before the order confirmation page); capture additional information after checkout. |
| [GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql/unstable/mutations/checkoutBrandingUpsert) | Customize the look and feel of checkout | Apply branding changes such as changing the colors and corner radius settings on checkout form fields. |
| [Shopify Functions](https://shopify.dev/docs/apps/build/functions) | Extend or replace key parts of Shopify's backend with custom logic | Create a new type of discount; rename/reorder/sort payment options; rename/reorder/sort delivery options; enforce an order maximum and prevent proceeding; use location rules to rank locations; use fulfillment constraints; generate pickup point options. |
| [Web pixel extensions](https://shopify.dev/docs/api/pixels) | Track customer behavior | Collect customer behavioral data to measure and optimize marketing campaign performance and the conversion funnel. |

---

## Market overrides

Merchants on Advanced or Plus who use [markets](https://shopify.dev/docs/apps/build/markets) can tailor their checkout and customer accounts experience for regional and company location markets.

In the checkout and accounts editor, merchants can create market-specific overrides in either their published or draft configurations. Overrides inherit from their parent market override or from the store's default experience when no parent override exists. A market override can include changes to branding and settings, and can add, reorder, or remove extensions.

If the buyer's resolved markets change while they're in checkout or customer accounts (for example, due to a delivery address change), updated settings are dynamically reloaded. Extensions might also be added or removed as a result. If an extension is moved to a different target for a market, it's treated as a new activation and will be unmounted and remounted.

To ensure the best merchant and buyer experience:

* Prefer native market overrides in the editor over re-implementing your custom market contextualization for market types already supported by Shopify.
* Don't rely on `useLocalizationMarket()` for market-specific conditions. Market definitions are merchant-defined and this API returns only the most precise regional market. Use delivery address or company location information for regional/B2B logic.
* Use local storage to persist state across extension activations and target changes.

---

## Next steps

* [Get started building for checkout](https://shopify.dev/docs/apps/build/checkout/start-building) to scaffold your first checkout UI extension.
* Explore the [checkout UI extensions reference](https://shopify.dev/docs/api/checkout-ui-extensions) for available targets, target APIs, and web components.

---

### Start building for checkout

> Fonte: https://shopify.dev/docs/apps/build/checkout/start-building

# Start building for checkout

To get started with checkout UI extensions, Shopify Functions or web pixel extensions, you can use Shopify CLI, which generates starter code for building your extension and automates common development tasks.

The following is a lightweight guide for getting started to build. You can alternatively learn how to use the GraphQL Admin API to [style checkout for a brand](https://shopify.dev/docs/apps/build/checkout/styling), such as changing the colors and corner radius settings on checkout form fields.

**Shopify Plus:**

Checkout UI extensions are available only to [Shopify Plus](https://www.shopify.com/plus) merchants. To build and test checkout UI extensions, use a [development store with Shopify Plus enabled](https://shopify.dev/docs/apps/build/dev-dashboard/development-stores#create-a-dev-store).

---

## Requirements

* You're a [user with app development permissions](https://shopify.dev/docs/apps/build/dev-dashboard/user-permissions) and have created a [dev store](https://shopify.dev/docs/apps/build/dev-dashboard/development-stores).
* You're using the latest version of [Shopify CLI](https://shopify.dev/docs/api/shopify-cli).
* You're using the latest version of [Chrome](https://www.google.com/chrome/) or [Firefox](https://www.mozilla.org/).

### Language-specific requirements for writing Shopify Functions in Rust

* You've installed [Rust](https://www.rust-lang.org/tools/install).

  On Windows, Rust requires the [Microsoft C++ Build Tools](https://docs.microsoft.com/en-us/windows/dev-environment/rust/setup). Make sure to select the **Desktop development with C++** workload when installing the tools.

* You've installed the [`wasm32-unknown-unknown`](https://doc.rust-lang.org/rustc/platform-support/wasm32-unknown-unknown.html) build target.

```terminal
rustup target add wasm32-unknown-unknown
```

---

## Get started

1. Scaffold an app:

   ```terminal
   shopify app init
   ```

2. Navigate to your app directory:

   ```terminal
   cd <directory>
   ```

3. Run the following command to create a new extension:

   ```terminal
   shopify app generate extension --name my-extension
   ```

4. Choose from one of the following extension types:

   * **Checkout UI**
   * **Function** (any of the sub-types)
   * **Post-purchase UI**
   * **Web Pixel**

5. Select a language for your extension.

   For this quickstart, if you chose a `Function` extension type, then select either **Rust** or **JavaScript**.

6. Complete one of the following steps:

   * If you chose a `Checkout UI`, `Post-purchase UI` or `Web Pixel` extension type, then start your development server to build and preview your app:

     ```terminal
     shopify app dev
     ```

     Press `p` to open the Dev Console. In the extension list for your app, click on the preview link for your extension.

   * If you chose a `Function` extension type, then navigate to `extensions/my-extension` and build the function's Wasm module:

     ```terminal
     cd extensions/my-extension
     cargo build --target=wasm32-unknown-unknown --release
     ```

     To test your function, you need to make it available to your dev store. [Learn more](https://shopify.dev/docs/apps/build/functions/test-debug-functions#testing-on-your-development-store).

---

## Next steps

* Learn how to use checkout UI and post-purchase extensions by following [one of our use case tutorials](https://shopify.dev/docs/api/checkout-extensions#getting-started).

---

### Checkout UI extensions (reference index)

> Fonte: https://shopify.dev/docs/api/checkout-ui-extensions

# Checkout UI extensions

Extensions add custom UI and logic into any step of the [Shopify checkout](https://shopify.dev/docs/apps/checkout) experience. For example, you can display personalized messages during cart review, integrate custom payment options at checkout, or add a survey to the thank-you page.

By using extension target APIs and web components from Shopify's Polaris design system, you can build performant customizations that look and feel familiar while tailoring the checkout experience to a store's specific needs.

**Shopify Plus:**

Checkout UI extensions for the information, shipping, and payment steps are available only to stores on a [Shopify Plus plan](https://www.shopify.com/plus).

## Getting started

To get started customizing your store's checkout, scaffold an app extension using [Shopify CLI](https://shopify.dev/docs/api/shopify-cli).

Scaffolding the extension creates a file framework that includes your extension's [TOML configuration file](https://shopify.dev/docs/apps/build/app-extensions/configure-app-extensions) and a templated `Checkout.jsx` file where you add your extension's code.

### Generate scaffold

```bash
cd my-app
shopify app generate extension --template checkout_ui
```

[Tutorial - Getting started with checkout UI extensions](https://shopify.dev/docs/apps/build/checkout/start-building)

---

## Upgrading your extension

The latest version of checkout UI extensions adds new components and target APIs, and updates how extensions read and write metafields. Check out the [migration guide](https://shopify.dev/docs/apps/build/checkout/migrate-to-web-components) for the steps to upgrade your extension.

---

## Building your extension

Checkout UI extensions are made up of three interconnected parts: targets that determine where your custom UI appears in the checkout interface, target APIs that provide access to checkout data and functionality, and web components that render UI elements like buttons and menus.

### Targets: Choose where your custom UI appears

Targets define where your custom UI appears within Shopify's checkout interface. There are three types of targets:

| Target type | Description |
| - | - |
| Block | Flexible placement targets that merchants can position using the [checkout and accounts editor](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-editor). Merchants can place block targets in various locations throughout the checkout flow and on the Thank you page. |
| Runnable | Targets that provide data or functionality without rendering UI components. These targets run in response to specific events, such as when a customer types in an address field, and return data like autocomplete suggestions or formatted address information. |
| Static | Targets that appear at fixed locations in checkout, such as before actions, after contact fields, or after cart line items. These targets render automatically when the checkout page loads and can't be moved or repositioned. |

[Reference - Explore all targets](https://shopify.dev/docs/api/checkout-ui-extensions/2026-04/targets)

![Checkout UI targets overview](https://shopify.dev/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-07/building.your.extension-BobGcef1.png)

### Target APIs: Define what your extension does

Target APIs provide access to data and functionality within the checkout flow. Use them to add custom logic to your extension.

When your extension runs, Shopify provides a `shopify` global object that you use to access data and features. Most target APIs are properties on this object. For example, `shopify.buyerIdentity` gives you information about the buyer who's interacting with the checkout, and `shopify.cost` provides the cost breakdown for the current checkout.

If your app uses ESLint, update your configuration to include the global `shopify` object to prevent linting errors.

[Reference - Explore all target APIs](https://shopify.dev/docs/api/checkout-ui-extensions/2026-04/target-apis)

### Cost API: Display checkout subtotal

```tsx
import '@shopify/ui-extensions/preact';
import {render} from 'preact';


export default function extension() {
  render(<Extension />, document.body);
}


function Extension() {
  const subtotal = shopify.cost.subtotalAmount.value;
  return (
    <s-stack>
      <s-text>
        Subtotal: {subtotal.amount}{' '}
        {subtotal.currencyCode}
      </s-text>
    </s-stack>
  );
}
```

### ESLint configuration

```javascript
module.exports = {
  globals: {
    shopify: 'readonly',
  },
};
```

### Web components: Design your interface

Web components are the UI building blocks that you use to display data and trigger API functions. These components are native UI elements that follow [Shopify's design system](https://shopify.dev/docs/apps/design) and are built with [remote-dom](https://github.com/Shopify/remote-dom), Shopify's library for building cross-platform user interfaces.

The component library includes options like form inputs, buttons, overlays, and feedback indicators. You can use these components individually for simple displays, or combine them with layout primitives like stack, grid, and section to build more complex interfaces.

[Reference - Explore all web components](https://shopify.dev/docs/api/checkout-ui-extensions/2026-04/web-components)

### Using web components

```typescript
import '@shopify/ui-extensions/preact';
import {render} from 'preact';


export default function extension() {
  render(<Extension />, document.body);
}


function Extension() {
  return (
    <s-stack direction="inline">
      <s-image src="https://cdn.shopify.com/YOUR_IMAGE_HERE" />
      <s-stack>
        <s-heading>Heading</s-heading>
        <s-text type="small">Description</s-text>
      </s-stack>
      <s-button
        onClick={() => {
          console.log('button was pressed');
        }}
      >
        Button
      </s-button>
    </s-stack>
  );
}
```

![Checkout UI extension web components example](https://shopify.dev/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-07/web.components-BVHhzg7k.png)

### Apply changes: Update the cart and checkout

Some target APIs include methods that update the cart and checkout. For example:

* [`applyAttributeChange`](https://shopify.dev/docs/api/checkout-ui-extensions/latest/target-apis/checkout-apis/attributes-api) sets a cart attribute.
* [`applyMetafieldChange`](https://shopify.dev/docs/api/checkout-ui-extensions/latest/target-apis/platform-apis/metafields-api) writes a cart metafield.

Each method returns a promise that resolves after Shopify applies the change and the corresponding API property updates with the new state.

**Rate limits may apply:**

Rate limits may apply to extensions that make too many changes during a checkout. After an extension is rate limited, it can't make further changes during the buyer's session.

Batch multiple changes with `Promise.all`. Only apply the changes your extension needs.

### Single change

```tsx
import '@shopify/ui-extensions/preact';
import {render} from 'preact';

async function onCheckboxChange(event) {
  const isChecked = event.target.checked;

  await shopify.applyAttributeChange({
    type: 'updateAttribute',
    key: 'includeGift',
    value: isChecked ? 'yes' : 'no',
  });
}

function Extension() {
  return (
    <s-checkbox
      onChange={onCheckboxChange}
      label="Include a complimentary gift"
    />
  );
}

export default function extension() {
  render(<Extension />, document.body);
}
```

### Multiple changes

```tsx
import '@shopify/ui-extensions/preact';
import {render} from 'preact';

async function saveGiftPreferences() {
  // Shopify batches these into a single request.
  await Promise.all([
    shopify.applyAttributeChange({
      type: 'updateAttribute',
      key: 'includeGift',
      value: 'yes',
    }),
    shopify.applyMetafieldChange({
      type: 'updateCartMetafield',
      metafield: {
        namespace: '$app:gift',
        key: 'message',
        type: 'single_line_text_field',
        value: 'Happy birthday!',
      },
    }),
  ]);
}

function Extension() {
  return (
    <s-button onClick={saveGiftPreferences}>
      Save gift preferences
    </s-button>
  );
}

export default function extension() {
  render(<Extension />, document.body);
}
```

---

## Configuration

You define your extension's configuration in a `shopify.extension.toml` file. This file contains the extension's name, targeting definitions, API version, and other settings. We recommend that you always set the latest supported `api_version` in your configuration file.

When you scaffold your extension using Shopify CLI, a `shopify.extension.toml` file with a default configuration is created for you. As you build your extension, you define the targets you want to use and their corresponding code modules in this file.

### Properties

Checkout UI extensions use the following configuration properties:

#### `api_version` required

The version of the API that's being used for the extension. If provided in the `[[extensions]]` array, then the specified API version is used instead of the root level `api_version`.

#### `[[extensions]]` required

The name of the array that contains all extensions listed in the TOML file. Contains the following properties:

* `type`: required The extension type. For checkout UI extensions, use `ui_extension`.
* `name`: required The customer-facing name of the extension. **Limitations**: 5 characters minimum; 30 characters maximum.
* `handle`: required The unique internal identifier for the extension. After you create a draft version of the extension, or deploy an extension, you can't change the `handle` value. **Limitations**: Allowed characters: `a-z`, `A-Z`, `0-9`, `-`; 50 characters maximum; Must be unique within the app.
* `uid`: required The extension user identifier that must be unique within the app. An app-scoped identifier used by `shopify app deploy` to determine whether an extension is being created, updated, or deleted. This identifier is generated automatically when you scaffold your extension using Shopify CLI.
* `description`: optional The merchant-facing description of the extension.

#### `[[extensions.targeting]]` required

The name of the array that contains a target and its associated module. Contains the following properties:

* `target`: required An identifier that specifies where you're injecting your extension into the checkout interface.
* `module`: required The path to the JavaScript or TypeScript file that contains your extension code.

You can define multiple targets in a single configuration file, but each target must point to a separate module file. For block targets, you can also define the default placement. See the [targets overview](https://shopify.dev/docs/api/checkout-ui-extensions/latest/targets#block-extension-targets) for more details.

#### `[extensions.capabilities]` optional

Defines the capabilities associated with your extension.

| Capability | Description |
| - | - |
| [`api_access`](https://shopify.dev/docs/apps/build/checkout/capabilities#storefront-api-access) | Allows your extension to query the Storefront API. |
| [`network_access`](https://shopify.dev/docs/apps/build/checkout/capabilities#network-access) | Allows your extension to make external network calls. |
| [`collect_buyer_consent`](https://shopify.dev/docs/apps/build/checkout/capabilities#collect-buyer-consent) | Allows your extension to collect buyer consent for policies like SMS marketing. |
| [`block_progress`](https://shopify.dev/docs/apps/build/checkout/capabilities#block-progress) | Allows your extension to block the buyer's progress. |

#### `[[extensions.metafields]]` optional

Define [metafields](https://shopify.dev/docs/apps/build/metafields) your extension needs access to. Use `[[extensions.metafields]]` for metafields needed by all targets, or `[[extensions.targeting.metafields]]` for target-specific metafields.

Checkout targets can use the [Metafields API](https://shopify.dev/docs/api/checkout-ui-extensions/latest/target-apis/platform-apis/metafields-api) to read metafields you request in the TOML, and to write cart metafields with `applyMetafieldChange` (`updateCartMetafield` and `removeCartMetafield`). Thank you page targets can read metafields through the Metafields API, but don't have write access.

See which [resources support metafields](https://shopify.dev/docs/apps/build/app-extensions/configure-app-extensions#resources-that-support-metafields) and the available [metafield data types](https://shopify.dev/docs/apps/build/metafields/list-of-data-types).

Learn more in the [Metafields API](https://shopify.dev/docs/api/checkout-ui-extensions/latest/target-apis/platform-apis/metafields-api) reference.

#### `[extensions.settings]` optional

Settings let merchants configure your extension from the [checkout editor](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-editor). Each settings definition can include up to 20 settings. All setting inputs are optional. Build your extension so it still works if the merchant hasn't set a value.

Each field in `[[extensions.settings.fields]]` accepts the following properties:

* `key`: required The identifier for the setting. The configured value is exposed under this key at runtime.
* `type`: required The setting type. Determines what input the merchant sees and how the value is validated. Supported types: `boolean`, `single_line_text_field`, `multi_line_text_field`, `number_integer`, `number_decimal`, `date`, `date_time`, and `variant_reference`.
* `name`: required The display name shown to the merchant in the checkout editor.
* `description`: optional Help text displayed to the merchant in the checkout editor.
* `validations`: optional Constraints on the input that Shopify validates, such as min/max length or a regex pattern. Learn more about [validation options](https://shopify.dev/docs/apps/build/app-extensions/configure-app-extensions#settings-fields).

### shopify.extension.toml

```toml
api_version = "2026-04"


[[extensions]]
type = "ui_extension"
name = "My checkout UI extension"
handle = "my-checkout-extension"
uid = "fddfc370-27c7-c30f-4ee0-a927194e2accadefd40c"


    [[extensions.targeting]]
    target = "purchase.checkout.block.render"
    module = "./src/Checkout.tsx"


    [[extensions.targeting]]
    target = "purchase.thank-you.block.render"
    module = "./src/ThankYou.tsx"
```

[Reference - Configuring app extensions](https://shopify.dev/docs/apps/build/app-extensions/configure-app-extensions)

---

## Testing and deployment

[Shopify CLI](https://shopify.dev/docs/api/shopify-cli) provides a set of tools to help you test and deploy your extension.

### Local testing

**Info:**

As of API version `2026-04`, you can write unit tests for checkout UI extensions using [`@shopify/ui-extensions-tester`](https://github.com/Shopify/ui-extensions/blob/2026-04/packages/ui-extensions-tester/README.md). Check out the [example test suite](https://github.com/Shopify/ui-extensions/tree/2026-04/examples/testing/checkout-basic-testing-example) to get started.

To run your extension locally during development, start a dev server using [Shopify CLI](https://shopify.dev/docs/api/shopify-cli). The `dev` command creates a preview of your extension on your chosen [dev store](https://shopify.dev/docs/apps/build/dev-dashboard/development-stores). If your extension is built on an app with a backend, then this command also serves your backend locally using a Cloudflare tunnel.

The dev server automatically reloads your extension when you make changes to your code, so you can test updates in real-time.

### Start development server

```terminal
shopify app dev
```

### Deployment

When you're ready to go live, deploy your extension to production using [Shopify CLI](https://shopify.dev/docs/api/shopify-cli).

The Shopify CLI `deploy` command builds your extension bundle and uploads everything to Shopify. If your extension is built on an app with a backend, then you need to deploy your app to a hosting service first. Shopify hosts only your extension's code.

**Note:**

Your compiled UI extension bundle can't exceed 64 KB. Shopify enforces this limit at deployment to ensure fast loading times and optimal performance. Learn how to [analyze your bundle size](https://shopify.dev/docs/apps/build/app-extensions#analyzing-bundle-size).

### Deploy your extension

```terminal
shopify app deploy
```

[Tutorial - Testing checkout UI extensions](https://shopify.dev/docs/apps/checkout/test-ui-extensions#test-the-extension-in-the-checkout-editor)

[Reference - Deploy app versions](https://shopify.dev/docs/apps/launch/deployment/deploy-app-versions)

### Versioning

Polaris reference docs follow [Shopify's API versioning policy](https://shopify.dev/docs/api/usage/versioning). Each stable version is supported for a minimum of 12 months. Older versions continue to work, they just won't have dedicated docs on Shopify.dev. [Shopify CLI](https://shopify.dev/docs/api/shopify-cli) already prevents deploys targeting API versions older than 12 months, so we recommend keeping your extensions on a supported version.

---

## Security

Checkout UI extensions are a safe and secure way to customize the appearance and functionality of checkout without compromising the security of customer data.

* They run in an isolated sandbox, separate from the checkout page and other UI extensions.
* They don't have access to sensitive payment information or the checkout page itself (HTML or other assets).
* They are limited to specific UI components and APIs that are exposed by the platform.
* They have limited access to [global web APIs](https://github.com/Shopify/ui-extensions/blob/unstable/documentation/runtime-environment.md).
* Apps that wish to access [protected customer data](https://shopify.dev/docs/apps/store/data-protection/protected-customer-data) must submit an application and are subject to strict security guidelines and review processes by Shopify.

---

## Error handling

To handle errors in your extension, add an `unhandledrejection` listener for promise rejections or an `error` listener for other exceptions like Javascript runtime errors or failures to load a resource.

You can also use third party error-reporting libraries. However, these libraries might require extra configuration because UI extensions run inside of a [Web Worker](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API) which doesn't have access to `window` or the DOM. You'll typically need to disable default integrations and manually attach error listeners to `self`.

The third-party tool example shown uses [Sentry](https://sentry.io/). To install and initialize this tool, follow their [Browser JavaScript guide](https://docs.sentry.io/platforms/javascript/). We recommend disabling the default integrations to be sure the tool will run within a Web Worker. You'll need to add event listeners manually.

**Note:**

You must request [network access](https://shopify.dev/docs/apps/build/checkout/capabilities#network-access) to transmit errors to a third party service.

### Using a listener

```ts
// For unhandled promise rejections
self.addEventListener('unhandledrejection', (event) => {
  console.warn('event unhandledrejection', event.reason);
});

// For other exceptions
self.addEventListener('error', (event) => {
  console.warn('event error', event.error);
});
```

### Using Sentry

```ts
import '@shopify/ui-extensions/preact';
import {render} from 'preact';
import {
  BrowserClient,
  captureException,
  defaultStackParser,
  getCurrentScope,
  makeFetchTransport,
} from '@sentry/browser';

const sentryClient = new BrowserClient({
  dsn: 'https://examplePublicKey@o0.ingest.sentry.io/0',
  transport: makeFetchTransport,
  stackParser: defaultStackParser,
  integrations: [],
});
getCurrentScope().setClient(sentryClient);
sentryClient.init();

self.addEventListener('unhandledrejection', (event) => {
  captureException(event.reason);
});

self.addEventListener('error', (event) => {
  captureException(event.error);
});

// Your normal extension code.
export default function extension() {
  render(<Extension />, document.body);
}

function Extension() {
  return <s-banner>Your extension</s-banner>;
}
```

---

## Tutorials and resources

### Tutorials

[Tutorial - Customizing Shopify checkout](https://shopify.dev/docs/apps/checkout/build-options)

[Tutorial - Start building for checkout](https://shopify.dev/docs/apps/build/checkout/start-building)

[Tutorial - Display custom data at checkout](https://shopify.dev/docs/apps/build/checkout/display-custom-data?extension=polaris)

[Tutorial - Customize the checkout header](https://shopify.dev/docs/apps/build/checkout/customize-header?extension=polaris)

### Design resources

[Guidelines - App design guidelines](https://shopify.dev/docs/apps/design)

### Community resources

[Reference - Developer changelog](https://shopify.dev/changelog)

[Community - Developer community](https://community.shopify.dev)
