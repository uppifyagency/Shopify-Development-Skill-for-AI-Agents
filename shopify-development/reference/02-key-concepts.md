# 2. Key Concepts (Theme Architecture)

This chapter is a faithful, 1:1 extraction of the **Theme architecture** section of the Shopify Themes documentation (the "Key Concepts" area of the developer docs). A Shopify theme controls the organization, features, and style of a merchant's online store. Theme architecture is the technical heart of theme development: it defines the standard directory structure, the markup-and-feature files (layouts, templates, sections, section groups, blocks, snippets), and the configuration and localization files (settings, config, locales) that make a theme customizable by merchants in the theme editor.

Each page below is reproduced from its source on `shopify.dev`, preserving all headings, prose, lists, tables (schema/attribute/property tables), and code examples (Liquid, JSON, JS) verbatim. Page titles (originally `H1`) have been demoted to `###` so they nest cleanly under each section's `##` heading. Source URLs are noted under each section heading.

> Note on the **Fonts** page: that page contains a very large machine-generated enumeration of every individual font handle in the Shopify font library. Per extraction rules, the conceptual prose, tables, and code examples are reproduced fully, while the giant font-handle list itself is marked with a placeholder. The full list is available at the source URL.

---

## Chapter table of contents

1. [Theme Architecture (overview)](#21-theme-architecture-overview)
2. [Layouts](#22-layouts)
   - [checkout.liquid](#221-checkoutliquid)
   - [Best practices for editing checkout.liquid](#222-best-practices-for-editing-checkoutliquid)
3. [Templates](#23-templates)
   - [JSON templates](#231-json-templates)
   - [Liquid templates](#232-liquid-templates)
   - [Alternate templates](#233-alternate-templates)
   - [Metaobject theme templates](#234-metaobject-theme-templates)
   - [404](#235-404)
   - [agents.md.liquid](#236-agentsmdliquid)
   - [article](#237-article)
   - [blog](#238-blog)
   - [cart](#239-cart)
   - [collection](#2310-collection)
   - [gift_card.liquid](#2311-gift_cardliquid)
   - [index](#2312-index)
   - [list-collections](#2313-list-collections)
   - [llms-full.txt.liquid](#2314-llms-fulltxtliquid)
   - [llms.txt.liquid](#2315-llmstxtliquid)
   - [page](#2316-page)
   - [password](#2317-password)
   - [product](#2318-product)
   - [robots.txt.liquid](#2319-robotstxtliquid)
   - [search](#2320-search)
4. [Sections](#24-sections)
   - [Section schema](#241-section-schema)
5. [Section groups](#25-section-groups)
   - [Migrate static sections to section groups](#251-migrate-static-sections-to-section-groups)
6. [Blocks](#26-blocks)
   - [Theme blocks (Quick Start)](#261-theme-blocks-quick-start)
   - [Block schema](#262-block-schema)
   - [Theme block targeting](#263-theme-block-targeting)
   - [Static blocks](#264-static-blocks)
   - [Dynamic sources (theme blocks)](#265-dynamic-sources-theme-blocks)
   - [Section blocks](#266-section-blocks)
   - [App blocks for themes](#267-app-blocks-for-themes)
   - [AI generated theme blocks](#268-ai-generated-theme-blocks)
7. [Snippets](#27-snippets)
8. [Settings](#28-settings)
   - [Input settings](#281-input-settings)
   - [Sidebar settings](#282-sidebar-settings)
   - [Dynamic data sources](#283-dynamic-data-sources)
   - [Fonts](#284-fonts)
9. [Config](#29-config)
   - [settings_schema.json](#291-settings_schemajson)
   - [settings_data.json](#292-settings_datajson)
   - [markets.json](#293-marketsjson)
10. [Locales](#210-locales)
    - [Storefront locale files](#2101-storefront-locale-files)
    - [Schema locale files](#2102-schema-locale-files)

---

## 2.1 Theme Architecture (overview)

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture

### Theme Architecture

A theme controls the organization, features, and style of a merchant's online store. Theme code is organized with a standard directory structure of files specific to Shopify themes, as well as supporting assets such as images, stylesheets, and scripts.

**Note:**

If you're building a theme for the Shopify Theme Store, then you need to meet certain requirements for the customization options that your theme offers, your theme's style, and the features that you include.

Theme files fall into the following general categories:

* **Markup and features** - These files control the layout and functionality of a theme. They use Liquid to generate the HTML markup that makes up the pages of the merchant's online store.
* **Supporting assets** - These files are assets, scripts, or locale files that are either called or consumed by other files in the theme.
* **Config files** - These files use JSON to store configuration data that can be customized by merchants using the theme editor.

---

#### Markup and Features

The following components determine the organization of each page:

| Number | Component | Description |
| - | - | - |
| 1 | The layout file | The base of the theme. Use the layout file to host repeated theme elements like headers and footers. |
| 2 | The template | The template that controls what's displayed on a page. Each theme should include different types of templates to display different types of content, such as the home page and products. You can also create multiple templates for the same resource type and associate them with your store resources, to allow for variation. JSON templates act only as a wrapper for sections, while Liquid templates contain code. |
| 3 | The section groups rendered by the layout | Containers that enable merchants to add, remove, and reorder sections in areas of the layout file such as the header and footer. |
| 4 | The sections rendered by the template | Reusable, customizable modules of content that merchants can add to JSON templates and section groups. |
| 5 | The blocks that each section contains | Reusable, customizable modules of content that can be added to sections, removed, and reordered. |
| 6 | The snippets being rendered | Reusable pieces of Liquid code that can be rendered anywhere in the theme. |

Features can be introduced into themes in Liquid template files, sections, blocks, and snippets. You can implement theme features using Liquid, CSS, and JavaScript. A theme's features determine how customers can interact with the content on an online store. For example, your theme needs to allow customers to add products to a cart by providing a Liquid `form` tag with a `product` type.

##### JSON with Comments

Theme files with JSON support comments and trailing commas. Users can add comments within `config/settings_schema.json` and within schema tags.

For example:

###### settings_schema.json

```json
[
  {
    /* context about theme schema settings */
    "name": "theme_info",
    "theme_name": "Dawn",
    "theme_author": "Shopify",
    "theme_version": "1.0.0",
    "theme_documentation_url": "https:\/\/help.shopify.com\/manual\/online-store\/themes\/os20\/themes-by-shopify\/dawn",
    "theme_support_url": "https:\/\/support.shopify.com\/",
  },
  {
  "name": "t:settings_schema.colors.name",
  "settings": [
    {
      "type": "header",
      "content": "t:settings_schema.colors.settings.header__1.content", // some useful context + see trailing comma
    },
  ...
]
```

Files that users typically don't edit won't persist comments or trailing commas. This includes the following:

```
templates/*.json
sections/*.json (section groups)
config/settings_data.json
locales/*.json
```

**Note:**

If you're using the Assets API to fetch and parse theme files, then you'll need to adopt a JSON parser that supports comments and trailing commas. The `unstable` version of the Admin API will add an autogenerated comment at the top of files that do not persist comments. This comment header will appear in files in the next stable version of the Admin API, `2024-10`.

---

#### Supporting Assets

You can add supporting assets to your theme to control the presentation of components and features, or to store reusable pieces of code that can be used across components.

For example, you need to add assets to style the theme. These resources help to define the aesthetic of the online store and how content sections are styled to express the merchant's brand. The style of a theme is defined by the CSS and JavaScript applied to layout, template, and section files. Liquid and HTML that you want to reuse across your theme can be stored in snippets. Theme CSS and JavaScript is stored in the assets directory of the theme.

In addition, you can translate your theme into different languages using locale files. Locale files contain a set of translations for text strings that are used throughout the theme, and are stored in the locales directory of the theme.

---

#### Directory Structure and Component Types

Themes must use the following directory structure:

##### Shopify Theme Directory Structure

```
.
├── assets
├── blocks
├── config
├── layout
├── locales
├── sections
├── snippets
└── templates
    └── customers
    └── metaobject
```

Subdirectories, other than the ones listed, aren't supported.

To see an example of a complete theme directory structure, and the various component types, explore the Dawn GitHub repository.

**Note:**

Only a `layout` directory containing a `theme.liquid` file is required for the theme to be uploaded to Shopify.

##### `assets`

The `assets` directory contains all of the assets used in a theme, including image, CSS, and JavaScript files.

Use the `asset_url` Liquid URL filter to reference an asset within your theme.

You can access limited Liquid functionality in non-binary asset files by appending a `.liquid` extension. Common use cases include JavaScript (`.js.liquid`) and CSS (`.css.liquid`) files. Files with this extension have access to the following features:

* The settings object
* Liquid filters

##### `config`

The `config` directory contains the config files for a theme. Config files define settings in the **Theme settings** area of the theme editor, as well as store their values.

Theme settings are a good place to host general settings such as typography and color options. Theme settings can be accessed through the settings object.

**Tip:**

You can also create settings for sections and blocks. These settings are defined as part of the parent section or block object, and appear in the theme editor with the associated object.

##### `layout`

The `layout` directory contains the layout files for a theme, through which template files are rendered.

Layouts are Liquid files that enable you to include content that should be repeated on multiple page types in a single location. For example, layouts are a good place to include any content you might want in your `<head>` element, as well as section groups for headers and footers.

A `theme.liquid` file must exist in this folder for the theme to be uploaded to Shopify.

##### `locales`

The `locales` directory contains the locale files for a theme, which are used to provide translated content. Locale files allow you to provide a translated experience in the theme editor, provide translations for the online store, and allow merchants to customize text in the online store.

##### `sections`

The `sections` directory contains a theme's sections and section groups.

Sections are Liquid files that allow you to create reusable modules of content that can be customized by merchants. They can also include blocks which allow merchants to add, remove, and reorder content within a section.

Section groups are JSON containers that allow merchants to add, remove, and reorder sections in areas of the layout file such as the header and footer.

##### `snippets`

The `snippets` directory contains Liquid snippet files that host smaller reusable snippets of code. Snippets are reusable pieces of Liquid code that can be rendered anywhere in your theme, and are invisible to merchants in the theme editor.

**Tip:**

You can provide LiquidDoc definitions which will enable additional tooling support through the Shopify VS Code Extension.

##### `templates`

The `templates` directory contains a theme's template files, which control what's rendered on each type of page.

The `templates/customers` directory contains the template files for legacy customer account pages, like login and account overview.

You can use the template to add functionality that makes sense for the page type. For example, you can add additional product recommendations to a product template, or add a comment form to an article template. You can also create multiple versions of the same template type to create custom templates for different use cases.

No templates are required. However, you need to have a matching template for any page type that you want to render. For example, to render a product page, you need at least one template of type `product`.

---

## 2.2 Layouts

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/layouts

### Layouts

Layouts are the base of the theme, through which all [templates](https://shopify.dev/docs/storefronts/themes/architecture/templates) are rendered.

Layouts are Liquid files that allow you to include content, that should be repeated on multiple page types, in a single location. For example, layouts are a good place to include any content you might want in your `<head>` element, as well as headers and footers.

You can edit the default `theme.liquid` layout, or you can create multiple custom layout files to suit your needs. You can specify which layout to use, or whether to use a layout at all, at the template level:

* In JSON templates, the layout that's used to render a page is specified using [the `layout` attribute](https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates#schema).

* In Liquid templates, the layout that's used to render a page is specified using [the `layout` Liquid tag](https://shopify.dev/api/liquid/tags/layout).

#### Location

Layout files are located in the `layout` directory of the theme:

```text
└── theme
  ├── layout
  |   ├── theme.liquid
  |   ...
  ├── templates
  ...
```

#### Subtypes

There are the following layout types:

| Type | Description |
| --- | --- |
| **General** | General layouts can apply to all non-checkout pages. The default layout file, which must be included in all themes, is `theme.liquid`. |
| **Checkout** | This layout type applies to all checkout pages. It's available to [Shopify Plus](https://www.shopify.com/plus?utm_source=shopify&utm_medium=docs&utm_campaign=checkout_liquid_layout) merchants only. To learn more about this layout, refer to [checkout.liquid](https://shopify.dev/docs/storefronts/themes/architecture/layouts/checkout-liquid). |

#### Schema

Because layout files are the base of the theme, they should follow the structure of a [standard HTML document](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Document_and_website_structure) in most cases. Most layout files also contain the following Liquid objects:

* [content_for_header](#content_for_header)
* [content_for_layout](#content_for_layout)

##### basic_layout_example.liquid

```liquid
<!DOCTYPE html>
<html>
  <head>
    ...
    {{ content_for_header }}
    ...
  </head>


  <body>
    ...
    {{ content_for_layout }}
    ...
  </body>
 </html>
```

#### Content

Layouts allow you to include content that's repeated across multiple page types in a single location. For example, layouts might include header and footer [sections](https://shopify.dev/docs/storefronts/themes/architecture/sections) and [SEO metadata](https://shopify.dev/docs/storefronts/themes/seo/metadata).

Layout files are `.liquid` files, so content can be built using standard HTML and Liquid.

Layouts can access any [global Liquid objects](https://shopify.dev/docs/api/liquid/objects) and can contain the following Liquid objects:

* [content_for_header](#content_for_header)
* [content_for_layout](#content_for_layout).

> **Caution:** These objects are required in `theme.liquid`. If references to these objects aren't included, then you can't save or update the file using the code editor or tools like Shopify CLI.

##### content_for_header

The `content_for_header` object is required in [`theme.liquid`](https://shopify.dev/docs/storefronts/themes/architecture/layouts). It must be placed inside the HTML `<head>` tag. It dynamically loads all scripts required by Shopify into the document head. These scripts are required for features like hCaptcha, Shopify apps, and more.

You shouldn't try to modify or parse the `content_for_header` object. If `content_for_header` changes, then the behavior of your Liquid will change.

##### content_for_layout

The `content_for_layout` object dynamically outputs the content for each [template](https://shopify.dev/docs/storefronts/themes/architecture/templates). You need to add a reference to this object between the `<body>` and `</body>` HTML tags.

#### Usage

When working with layout files, you should familiarize yourself with the following concepts:

* [Supporting template-specific CSS selectors](#support-template-specific-css-selectors)
* [Accessing and customizing checkout.liquid](#access-and-customize-checkoutliquid)

##### Support template-specific CSS selectors

You can help create CSS rules for specific templates by outputting data from the [`template` object](https://shopify.dev/docs/api/liquid/objects/template) in the `<body>` tag's class.

###### theme.liquid

```liquid
<body class="template-{{ template.name }}">
  ...
</body>
```

###### theme.css

```css
.template-product {
  margin-bottom: 2em;
}
```

##### Access and customize checkout.liquid

> **Deprecated:** `checkout.liquid` is now unsupported for the Information, Shipping, and Payment checkout steps. `checkout.liquid`, additional scripts, and script tags are deprecated for the **Thank you** and **Order status** pages and will be sunset on August 28, 2025.

Stores that currently use `checkout.liquid` for the **Thank you** and **Order status** pages need to [upgrade to Shopify Extensions in Checkout](https://www.shopify.com/checkout#advanced-customizations) before the deadline.

[Shopify Scripts](https://shopify.dev/docs/api/liquid/objects#script) will continue to work alongside Shopify Extensions in Checkout until June 30, 2026.

Learn [how to build checkout extensions](https://shopify.dev/docs/apps/build/checkout/technologies) that extend the functionality of Shopify checkout.

To enable or disable access to `checkout.liquid`, Shopify Plus merchants must [contact support](https://help.shopify.com/en/questions#/contact). To learn more about enabling access, refer to [Access checkout.liquid](https://shopify.dev/docs/storefronts/themes/architecture/layouts/checkout-liquid#access-checkout-liquid).

Before making any customizations, you should refer to [checkout.liquid](https://shopify.dev/docs/storefronts/themes/architecture/layouts/checkout-liquid) to familiarize yourself with the file format and contents, as well as [Best practices for editing checkout.liquid](https://shopify.dev/docs/storefronts/themes/architecture/layouts/checkout-liquid/customize-checkout).

### 2.2.1 checkout.liquid

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/layouts/checkout-liquid

#### checkout.liquid

**Deprecated:**

`checkout.liquid` is now unsupported for the Information, Shipping, and Payment checkout steps. `checkout.liquid`, additional scripts, and script tags are deprecated for the **Thank you** and **Order status** pages and will be sunset on August 28, 2025.

Stores that currently use `checkout.liquid` for the **Thank you** and **Order status** pages need to upgrade to Shopify Extensions in Checkout before the deadline.

Shopify Scripts will continue to work alongside Shopify Extensions in Checkout until June 30, 2026.

Learn how to build checkout extensions that extend the functionality of Shopify checkout.

The `checkout.liquid` layout renders the checkout and is available only to Shopify Plus merchants. If your store isn't on Shopify Plus, then you can customize your checkout pages in the theme editor.

---

##### Location

The `checkout.liquid` layout is located in the `layout` directory of the theme:

```text
└── theme
  ├── layout
  |  ├── theme.liquid
  |  └── checkout.liquid
  ├── templates
  ...
```

---

##### Schema

The `checkout.liquid` layout has the following format by default:

###### checkout.liquid

```liquid
<!DOCTYPE html>
<html lang="{{ locale }}" dir="{{ direction }}" class="{{ checkout_html_classes }}">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, height=device-height, minimum-scale=1.0, user-scalable=0" />
    <meta name="referrer" content="origin" />


    <title>{{ page_title }}</title>


    {{ content_for_header }}


    {{ checkout_stylesheets }}
    {{ checkout_scripts }}
  </head>
  <body>
    {{ skip_to_content_link }}


    <header class="banner" data-header role="banner">
      <div class="wrap">
        {{ content_for_logo }}
      </div>
    </header>


    {{ order_summary_toggle }}
    <div class="content" data-content>
      <div class="wrap">
        <div class="main">
          <header class="main__header" role="banner">
            {{ content_for_logo }}
            {{ breadcrumb }}
            {{ alternative_payment_methods }}
          </header>
          <main class="main__content" role="main">
            {{ content_for_layout }}
          </main>
          <footer class="main__footer" role="contentinfo">
            {{ content_for_footer }}
          </footer>
        </div>
        <aside class="sidebar" role="complementary">
          <div class="sidebar__header">
            {{ content_for_logo }}
          </div>
          <div class="sidebar__content">
            {{ content_for_order_summary }}
          </div>
        </aside>
      </div>
    </div>


    {{ tracking_code }}
  </body>
</html>
```

---

##### Content

The `checkout.liquid` layout has specific checkout objects to render various checkout content, depending on the checkout step.

###### Checkout steps

The checkout has the following steps:

| Step | Description |
| - | - |
| **Inventory issues** | This step is displayed if one or more of the cart items is out of stock, or the inventory level is below what the customer has requested. Customers are shown a confirmation button that will update their cart with the available item quantities. |
| **Contact information** | The customer enters their email address and will have the option to log in if customer accounts are enabled for the store. If any cart items require shipping, then the customer is shown a shipping address form. Otherwise, the customer is shown a billing address form. |
| **Shipping method** | The customer selects a shipping option or edits their shipping information. This step is skipped when none of the cart items require shipping. Skipping the shipping method is common for merchants selling digital products or services. Clicking **Edit shipping information** returns the visitor to the **Customer information** step. |
| **Payment method** | The customer chooses a payment method and, if applicable, enters payment information. Some payment providers require the customer to complete payment information on a different site. Customers can also specify a different billing address during this step. |
| **Review order** | Optional based on checkout settings. The customer confirms their order total, shipping and billing addresses, and payment details by clicking **Complete order**. This step might be required if the store is operating in the European Union. |
| **Processing/forwarding** | A temporary page shown to customers as their order is being processed, or as they are being redirected to an off-site payment provider. The message displayed during this step depends on your checkout's translation settings. |
| **Order status** | The last step of checkout. This step is displayed after an order is complete. |

On every step, an **Order summary** showing the products, price, taxes, and shipping costs is displayed in the right column. This column collapses at mobile breakpoints.

> **Tip:**
>
> You can use JavaScript to identify the current step.

###### Checkout objects

| Object | Description | Required |
| - | - | - |
| **content_for_header** | The scripts from Shopify for features like hCaptcha, Shopify apps, and more. You need to add a reference to this object between the `<head>` and `</head>` HTML tags. | Yes |
| **content_for_layout** | The form fields and content for each step of the checkout process. You need to add a reference to this object between the `<body>` and `</body>` HTML tags. | Yes |
| **locale** | The currently-selected locale. | No |
| **direction** | The CSS direction of the content. For example, `ltr` or `rtl`. | No |
| **page_title** | The page title. Commonly wrapped in `<title>` and `</title>` tags. | No |
| **skip_to_content_link** | A hidden link for accessibility that allows users to skip to the main content. | No |
| **checkout_html_classes** | A string that should be added to the `<html>` tag to benefit from Shopify's default CSS. | No |
| **checkout_stylesheets** | Shopify's checkout stylesheets. It's recommended that you don't remove this, even if you have your own stylesheets, as it requires extensive work to replace the default styling. | No |
| **checkout_scripts** | Shopify's JavaScript files. | No |
| **content_for_logo** | The store logo, as determined by the checkout settings. | No |
| **breadcrumb** | The list of steps required to complete the checkout. The breadcrumb doesn't display on the final review step during checkout. | No |
| **order_summary_toggle** | The markup necessary to show and hide the order summary on mobile devices. | No |
| **content_for_order_summary** | The content summary, including line items, discounts, taxes, and totals. | No |
| **alternative_payment_methods** | The list of available express payment methods, such as PayPal. | No |
| **content_for_footer** | The list of your store policies or, if the list is empty, a copyright notice. | No |
| **tracking_code** | The JavaScript responsible for Google Analytics and Facebook Pixel tracking. | No |
| **checkout** | The checkout object. | No |

> **Caution:**
>
> If you don't include the required objects in your `checkout.liquid` template, then you can't save or update the file using the code editor or tools like Shopify CLI.

---

##### Usage

When working with `checkout.liquid`, you should familiarize yourself with the following concepts:

* How to access `checkout.liquid`
* Considerations for customizing checkout content
* How to identify the current checkout step
* Page events
* Checkout jQuery
* How to capture checkout attributes

###### Access checkout.liquid

To enable or disable access to `checkout.liquid`, Shopify Plus merchants must contact support.

Before requesting access to `checkout.liquid`, you should be familiar with the following versions of checkout and their implications:

| Version | Description |
| - | - |
| **Standard** | The default checkout. It's used if access to `checkout.liquid` isn't enabled, and is automatically updated as Shopify releases updates and features for the checkout. |
| **Maintenance** | Used when access to `checkout.liquid` is enabled. It's a stable version of `Standard`, frozen at a specific time. This means that it's not automatically updated. If you use `Maintenance`, then you can get access to updates and features in the following ways: - Disable access to `checkout.liquid` to move back onto `Standard`. - Wait for `Maintenance` to be upgraded and follow the manual checkout upgrade process. |

###### Add checkout.liquid to your theme

If access to `checkout.liquid` has been enabled, then you can follow the steps below to add the layout to your theme through the code editor in the Shopify admin:

**Desktop**

1. From your Shopify admin, go to **Online Store** > **Themes**.
2. Find the theme that you want to edit, and then click **...** > **Edit code**.

**Mobile**

1. From the Shopify app, tap **Store**.
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage all themes**.
4. Find the theme that you want to edit, and then tap **...** > **Edit code**.

Then:

1. In the **Layout** directory, click **Add a new layout**.
2. In the drop-down list, select **checkout**, and then click **Create layout**.

You should now see `checkout.liquid` listed in the **Layout** directory.

###### Customize checkout content

You can't edit the content generated by any of the checkout objects, required or optional, before they're rendered. The only exceptions to this are for translation settings, theme editor settings, and some options made available in the Shopify admin.

If you need to customize the content output by a checkout object, then you need to use JavaScript to alter the content after it's been rendered. To learn more about customizing this content, refer to Best practices for editing checkout.liquid.

###### Step identification

The checkout is all hosted on one page, which means that the URL remains the same regardless of which step of the process a customer is on. To account for this, you can use the following JavaScript objects to identify where the customer is in the checkout process.

* Shopify.Checkout.step
* Shopify.Checkout.page
* Shopify.Checkout.OrderStatus

> **Tip:**
>
> The above JavaScript objects can be viewed using your browser's developer tools.

**Shopify.Checkout.step**

An object that shows which step of the checkout the customer is on. It returns one of the following results:

* `contact_information`
* `shipping_method`
* `payment_method`
* `processing` - This is the step between the `payment_method` step and the `thank_you` page.
* `review` - This is an optional step set in the Shopify Admin.

> **Note:**
>
> This object is defined only when the customer first visits the **Order Status** page.

**Shopify.Checkout.page**

An object that shows which type of page the customer is on. It returns one of the following results:

* `show` - A page template for various steps of the checkout process.
* `stock_problems` - A page that displays if there's an inventory issue with any cart items.
* `processing` - A page that displays while the payment is being processed.
* `forward` - A page from PayPal or another third-party gateway.
* `thank_you`

> **Note:**
>
> This object is defined only when the customer first visits the **Order Status** page.

**Shopify.Checkout.OrderStatus**

An object that can be used for adding content to the **Order status** page. It can also help determine whether the customer is on a **Thank You** page or an **Order Status** page.

The **Order Status** page is usually considered as a `checkout` page. However, the first time a customer visits the page, it's considered as a **Thank You** page, where the `Shopify.Checkout.step` and `Shopify.Checkout.page` objects are defined.

If the customer revisits or reloads the page, then this `checkout` is converted to an `order`, and the page loads as an **Order Status** page, where the `Shopify.Checkout.step` and `Shopify.Checkout.page` objects are undefined and the `Shopify.Checkout.OrderStatus` object is defined.

###### Page events

All of the checkout steps are hosted at a single URL path, where the content is loaded dynamically depending on the current step. There are two main page events that are triggered during this process:

* page:load
* page:change

**page:load**

The `page:load` event is triggered when the content of each step is loaded. This is the default event that you should use when adding content into the page on load.

```javascript
$(document).on('page:load', function() {
  // Add content
});
```

**page:change**

The `page:change` event is triggered when the customer is on the same checkout step, but part of the content has changed. For example, this event triggers when the discount form is submitted.

If you add content to the Document Object Model (DOM) with only `page:load`, then there's a risk that it could be overwritten by a `page:change` event. To avoid this issue, you should watch for both events when adding content.

```javascript
$(document).on("page:load page:change", function() {
  // Add content
});
```

###### Checkout jQuery

The checkout contains its own version of jQuery, which can be accessed using `Checkout.$`.

```javascript
(function($) {
  $(document).on("page:load page:change", function() {
    // Add your customizations
  });
})(Checkout.$);
```

> **Note:**
>
> The checkout's version of jQuery is not always the most recent version. If you need any functionality from a more recent version of jQuery, then you'll need to include it specifically.

###### Capture checkout attributes

You can capture checkout attributes in a similar way to capturing cart attributes.

To capture a checkout attribute, include an input with an attribute of `name="checkout[attributes][attribute-name]"`, where `attribute-name` is the desired name of your attribute, inside the main checkout form.

```html
<input type="text" name="checkout[attributes][custom attribute]" />
```

> **Tip:**
>
> If you're collecting attributes on the **Payment method** step, then you should populate them with a placeholder value before allowing the order to proceed. If the attribute has a blank value, then it can cause an error noting that the checkout has changed.

Note that capturing checkout attributes will remove any existing cart attributes. To learn how to avoid this issue, refer to Preserve cart attributes below.

**Preserve cart attributes**

When capturing checkout attributes, you can preserve any cart attributes with the `checkout.attributes` Liquid object, which contains the cart attribute values. You can loop through the attributes to add them as checkout attribute inputs with names and values defined by the existing attribute data.

This snippet should be included inside a JavaScript function for placing the attribute inputs inside the main form.

```liquid
{% for attribute in checkout.attributes %}
  <input type=hidden name="checkout[attributes][{{ attribute.first }}]" value="{{ attribute.last  }}" />
{% endfor %}
```

### 2.2.2 Best practices for editing checkout.liquid

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/layouts/checkout-liquid/customize-checkout

#### Best practices for editing checkout.liquid

**Deprecated:**

`checkout.liquid` is now unsupported for the Information, Shipping, and Payment checkout steps. `checkout.liquid`, additional scripts, and script tags are deprecated for the **Thank you** and **Order status** pages and will be sunset on August 28, 2025.

Stores that currently use `checkout.liquid` for the **Thank you** and **Order status** pages need to upgrade to Shopify Extensions in Checkout before the deadline.

Shopify Scripts will continue to work alongside Shopify Extensions in Checkout until June 30, 2026.

Learn how to build checkout extensions that extend the functionality of Shopify checkout.

**Caution:**

Before you make changes to your checkout, it's recommended that you back up the current version of the code in your `checkout.liquid` file. To learn more about backing up your theme, refer to Downloading themes or Duplicating themes.

If you're on Shopify Plus, then you can get access to the `checkout.liquid` layout. However, if you make changes to this layout, then you'll need to manually upgrade it whenever Shopify releases an upgrade.

---

##### Document Object Model (DOM) dependency

One of the biggest considerations to make when implementing checkout modifications is how DOM-dependent your code is. As Shopify releases checkout upgrades, the content output by the Liquid drops in `checkout.liquid`, and in some cases by the `checkout.liquid` content itself, is updated. This means that if your customizations depend on that content, then they could break with new upgrades. It's always best to minimize DOM dependency to reduce future support debt for your team.

**Tip:**

Other than adding content only outside of the Liquid drops, the most DOM-independent method for accessing elements is to reference `data` and `name` attributes, as these are less likely to be changed across upgrades.

---

##### Add custom code

When making changes, you should keep all of the relevant code for a specific customization in a single snippet. This reduces the risk of conflict with other code, and generally makes the code easier to read.

Also, any time that a change is made, it's recommended that you place a comment at the beginning of the change noting who made it, and when.

###### Example

```liquid
{% comment %} Added by Name from Company on September 21 2018 {% endcomment %}
```

---

##### Add killswitches

When customizing `checkout.liquid`, you're more likely to run into issues or conflicts in the checkout, possibly preventing sales, so it's a good idea to wrap your customizations in a killswitch (a theme setting). This allows you to temporarily disable the customization to get the checkout functioning quickly, which gives you time to troubleshoot issues.

---

##### General customization approach

In general, the approach for making customizations is the following:

* Create a killswitch theme setting
* Create a snippet to host your customization
* Include your snippet, wrapped in your killswitch, in `checkout.liquid`

The following examples show a killswitch theme setting and a snippet inclusion wrapped in a conditional based on the killswitch:

###### config/settings_schema.json

```json
{
  "type": "checkbox",
  "id": "checkout_customization",
  "label": "Enables a checkout customization"
},
```

###### layout/checkout.liquid

```liquid
{% comment %}Added by Name at Company on September 21, 2018{% endcomment %}
{% if settings.checkout_customization %}
  {% render 'checkout-customization' %}
{% endif %}
```

In your snippet, you can do the following:

* Use the checkout's version of jQuery

* Watch for the `page:load` and `page:change` events to set up your customization

* Scope your customization to the appropriate step or page by referencing the following objects:

  * `Shopify.Checkout.step`
  * `Shopify.Checkout.page`
  * `Shopify.Checkout.OrderStatus`

```javascript
(function($) {
  $(document).on("page:load page:change", function() {
    if (Shopify.Checkout.step === "contact_information") {
      // Add content
    }
  });
})(Checkout.$);
```

---

##### Form submit

Many checkout customizations require validating data before allowing the customer to move to the next step. Due to the functionality around the main form submit button, the easiest approach is watch for the `click` event on this button, rather than the `submit` field on the form. You should also watch for the use of the enter key and re-route that functionality into a `click` event on the submit button.

**Caution:**

All selectors used in the snippet below are placeholders. You'll need to decide on the selector you want to use. Try to avoid DOM dependency.

```javascript
(function($) {
  $(document).on("page:load page:change", function() {
    if (Shopify.Checkout.step === "contact_information") {
      $("DEFINE_YOUR_SUBMIT_BUTTON_SELECTOR").on("click", function(e) {
        e.preventDefault();


        if (data is valid) {
          $("DEFINE_YOUR_MAIN_FORM_SELECTOR").submit();
        } else {
          // Show an error
        }
      });


      $("DEFINE_YOUR_MAIN_FORM_SELECTOR").on("keyup", function(e) {
        if (e.keycode === 13) {
          e.preventDefault();
          $("DEFINE_YOUR_SUBMIT_BUTTON_SELECTOR").trigger("click");
        }
      });
    }
  });
})(Checkout.$);
```

---

##### Common customizations

The following examples are commonly requested customizations. They all use the general customization approach as a starting point.

###### Block the use of specific characters in address fields

To block the use of specific characters in address fields, you need to consider the following cases:

1. Updates to the associated address fields, such as the `blur` event.
2. The form submit event.

For each of these cases, execute your validation. For example, you could compare any field values with a Regular Expression (Regex). If the data isn't valid, you can show an error and prevent the default functionality.

###### Limit the number of characters in address fields

To limit the number of characters in address fields, add a `maxlength` attribute to any associated fields, as shown in the following example.

**Note:**

The selector used below is a placeholder. You'll need to decide on the selector you want to use. Try to avoid DOM dependency.

```javascript
$("DEFINE_YOUR_FIELD_SELECTOR").attr("maxlength", your_value);
```

The `maxlength` attribute only prevents additional characters from being entered. To ensure a good user experience, you should add a message that appears when a customer hits the character limit.

###### Add a required Terms of Service checkbox

To add a required checkbox for agreeing to Terms of Service, create a checkbox on the page, then follow the form submit event to check whether the checkbox has been checked before allowing the customer to proceed. It's also a good idea to use a checkout attribute to save the value of the checkbox.

---

## 2.3 Templates

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/templates

### Templates

Templates control what's rendered on each type of page in a theme.

Each page type in an online store has an associated template type. You can use the template to add functionality that makes sense for the page type. For example, to render a product page, the theme needs at least one template of type `product`. Similarly, to render a metaobject page, the theme needs at least one template of type `metaobject/{metaobject-type}`, for example: `metaobject/book` or `metaobject/author`, depending on the type of metaobject definition.

You can create multiple versions of the same template type to create custom templates for different use cases. For example, you can create a separate product template for outerwear products, or a separate page template for pages with video content.

---

#### JSON vs. Liquid

There are two different file types you can use for a theme template: JSON and Liquid. These template file types can be used to build multiple template types, each of which represents a type of content in a merchant's online store.

| Type | Description |
| - | - |
| JSON | JSON templates are data files with the `.json` file extension. These templates let you easily populate your template with content from sections. Sections can be added, removed, or rearranged by merchants using the theme editor. If you're using a JSON template, then any HTML or Liquid code needs to be included in a section that's referenced by the template. |
| Liquid | Liquid templates are Liquid markup files, with the `.liquid` file extension. You can add Liquid and HTML directly to Liquid templates. |

##### Choosing JSON vs Liquid

If you want to use sections in a template, then you should use a JSON template.

"JSON templates provide more flexibility for merchants to add, remove, and reorder sections, including app sections. Additionally, they minimize the amount of data in `settings_data.json`." Instead, data is stored directly in the template, which improves the performance of the theme editor.

---

#### Template types

Each available template type represents a type of content in a merchant's online store. No template types are required. However, you must have a matching template for any page type that you want to render. For example, to render a product page, you need at least one template of type `product`.

You can have a maximum of 1000 JSON templates in your theme, across all template types. For example, if you have 20 JSON product templates, 10 JSON page templates, and 5 JSON collection templates, then you can add up to 965 additional templates to the theme.

You can use the following template types in your theme:

| Type | Description |
| - | - |
| 404 | Renders page content that is shown to customers if they enter an invalid URL for the store. |
| agents.md.liquid | Renders the `agents.md` file, which is hosted at the `/agents.md` URL. This file is the canonical, agent-facing description of the store, telling AI agents how to discover and transact with it. This must be a Liquid template. |
| article | Renders the article page, which contains the full content of the article, as well as an optional comments section for customers. This template is used for items like individual posts in a blog. |
| blog | Renders the blog page, which lists all articles within a blog. |
| cart | Renders the `/cart` page, which provides an overview of the contents of a customer's cart. |
| collection | Renders the collection page, which lists all products within a collection. |
| gift_card.liquid | Renders the gift card page, which displays the gift card issued to a customer upon purchase. This must be a Liquid template. |
| index | Renders the home page of the store, located at the root URL (`/`). |
| list-collections | Renders the collection list page, which lists all the store's collections. This page is located at the `/collections` URL of the store. |
| llms-full.txt.liquid | Renders the `llms-full.txt` file, hosted at the `/llms-full.txt` URL. An alternate agent-discovery URL that mirrors `/agents.md` by default. This must be a Liquid template. |
| llms.txt.liquid | Renders the `llms.txt` file, hosted at the `/llms.txt` URL. An alternate agent-discovery URL that mirrors `/agents.md` by default. This must be a Liquid template. |
| page | Renders the shop's pages, such as **About us** and **Contact us**. |
| password | Renders the `/password` page, which is a landing page shown when you add password protection to your online store. This page includes a message that is editable by merchants, and the password form for customers to gain access to the store. |
| product | Renders the product page, which contains a product's media and content, as well as a form for customers to select a variant and add it to the cart. |
| robots.txt.liquid | Renders the `robots.txt` file, which is hosted at the `/robots.txt` URL. This file tells search engines which pages can, or can't, be crawled on a site. This must be a Liquid template. |
| search | Renders the `/search` page, which displays the results of a storefront search. |
| metaobject | Renders metaobject pages, such as "artists" or "authors". To render each metaobject entry as an individual page, the metaobject definition must have the web page capability. |

**Note:**

"The `gift_card`, `robots.txt`, `agents.md`, `llms.txt`, and `llms-full.txt` templates can't be JSON templates, so you must make them Liquid templates." Other template types support either template file type.

##### Legacy customer account templates

Legacy customer account templates are deprecated. Customer accounts now operate independently of themes, and the following templates no longer need to be included in your theme:

* customers/account
* customers/activate_account
* customers/login
* customers/order
* customers/register
* customers/reset_password
* customers/addresses

Publishing a theme without these templates automatically upgrades merchants to the latest customer accounts experience, which operates independently of themes.

Instead, add the `<shopify-account>` component to your theme header so customers can sign in without leaving the storefront, or navigate to account pages. It's fully integrated with customer accounts and offers styling controls to match your theme.

---

#### Location

Template files are located in the `templates` directory of the theme:

```text
└── theme
  ├── layout
  ├── templates
  |   ├── 404.json
  |   ├── article.json
  |   ...
  ...
```

---

#### Content

The content that you can include in a template depends on whether it is a JSON template or a Liquid template.

You should always keep the goal of the template type in mind when deciding what content you want to include in a template. For example, a product template, or a section in the product template, should always include the `product` object, which renders product details, and the product form tag, which lets customers add a product variant to the cart. Depending on your template type and approach, you might want to include these items in a section that you reference in the template.

### 2.3.1 JSON templates

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates

#### JSON templates

JSON templates allow you to control the look and feel of different pages of the online store using [sections](https://shopify.dev/docs/storefronts/themes/architecture/sections).

JSON templates are data files that store a list of sections to be rendered, and their associated settings. Merchants can add, remove, and reorder these sections using the theme editor.

When a page is rendered with a JSON template, the sections are rendered in the order specified by the [order attribute](#schema), with no markup between the sections. JSON templates can render up to 25 sections, and each section can have up to 50 blocks.

---

##### Supported features

Although JSON templates differ from Liquid templates in their contents, they are still template files that support the following Shopify theme features:

* All template types, except for [gift_card](https://shopify.dev/docs/storefronts/themes/architecture/templates/gift-card-liquid), [robots.txt](https://shopify.dev/docs/storefronts/themes/architecture/templates/robots-txt-liquid), [agents.md](https://shopify.dev/docs/storefronts/themes/architecture/templates/agents-md-liquid), [llms.txt](https://shopify.dev/docs/storefronts/themes/architecture/templates/llms-txt-liquid), and [llms-full.txt](https://shopify.dev/docs/storefronts/themes/architecture/templates/llms-full-txt-liquid).

* [Alternate templates](https://shopify.dev/docs/storefronts/themes/architecture/templates/alternate-templates).

  When you build a JSON template, you should also build a section that contains the core functionality for the template. For example, when you're building a [list-collections](https://shopify.dev/docs/storefronts/themes/architecture/templates/list-collections) JSON template, it should reference a section that uses the [collections object](https://shopify.dev/docs/api/liquid/objects/collections).

  A theme can contain up to 1,000 JSON templates. After the limit is reached, you can't create new JSON templates.

---

##### Schema

A JSON template accepts only a JSON file with a fixed schema and list of accepted attributes. The root should be an object with the following attributes:

| Attribute | Type | Required | Description |
| - | - | - | - |
| `layout` | String or `false` | No | The filename of the [layout](https://shopify.dev/docs/storefronts/themes/architecture/layouts) to use when rendering the template. For example, specify `"full-width"` to render `layout/full-width.liquid`. The default layout is `theme.liquid`. Use the value `false` to render the template without a layout. Templates without a layout can't be customized in the theme editor. |
| `wrapper` | String | No | The HTML wrapper element for the template's sections. To learn more, refer to [The wrapper property](https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates#the-wrapper-property). |
| `sections` | Object | Yes | An object that uses section IDs as keys, and section data as values. This attribute needs to contain at least one section. Duplicate IDs within the template aren't allowed. The format of the section data is the same as section data in [settings_data.json](https://shopify.dev/docs/storefronts/themes/architecture/config/settings-data-json). To learn more, refer to [Section data](https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates#section-data). JSON templates can render up to 25 sections, and each section can have up to 50 blocks. |
| `order` | Array | Yes | An array of section IDs, listed in the order that they should be rendered. The IDs must exist in the `sections` object. Duplicates are not allowed. |

**Tip:**

Section files must define [presets](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#presets) in their schema to support being added to JSON templates using the theme editor. Section files without presets should be included in the JSON file manually, and can't be removed using the theme editor.

###### Naming JSON templates

The filename must be a valid [theme template type](https://shopify.dev/docs/storefronts/themes/architecture/templates#template-types), with an optional suffix for an alternate template. For example, a product template can be named `product.json` or `product.alternate.json`.

A template can only exist as a JSON or Liquid template, not both. For example, if `product.liquid` already exists, then you can't create `product.json`.

###### The wrapper property

The `wrapper` property makes it possible to insert HTML tags around all of the sections in a JSON template. You can use the following HTML tags:

* `<div>`
* `<main>`
* `<section>`

For example, a JSON file with the following `wrapper` property produces the following output:

**product.json**

```json
{
  "wrapper": "div#div_id.div_class[attribute-one=value]",
  "sections": {
    "main": {
      "type": "product"
    }
  },
  "order": [
    "main"
  ]
}
```

**Output**

```html
<div id="div_id" class="div_class" attribute-one="value">
    <!-- product.json sections -->
</div>
```

###### Section data

The `sections` attribute of JSON templates holds the data for the sections to be rendered by the template. These can be either [theme sections](https://shopify.dev/docs/storefronts/themes/architecture/sections) or [app sections](https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks#app-block-wrapper). You can't share section data across JSON theme templates, so each section must have an ID that's unique within the template.

JSON templates can render up to 25 sections, and each section can have up to 50 blocks.

You can add sections to a template in code, or through the theme editor. The sections that are available to be added to a template in the theme editor might be limited by the [`enabled_on`](https://shopify.dev/docs/themes/architecture/sections/section-schema#enabled_on) or [`disabled_on`](https://shopify.dev/docs/themes/architecture/sections/section-schema#disabled_on) attribute of the section schema. If no `enabled_on` or `disabled_on` attribute is defined, then the section can be added to any template.

The following table outlines the format of section data:

| Value | Type | Required | Description |
| - | - | - | - |
| `<SectionID>` | String | - | A unique ID for the section. Accepts only alphanumeric characters. |
| `<SectionType>` | String | Yes | The filename of the section file to render, without the extension. |
| `<SectionDisabled>` | Boolean | No | When `true`, the section isn't rendered but can still be customized in the theme editor. Is `false` by default. |
| `<BlockID>` | String | - | A unique ID for the block. Accepts only alphanumeric characters. |
| `<BlockType>` | String | Yes | The type of block to render, as defined in the schema of the section file. |
| `<BlockOrder>` | Array | No | An array of block IDs, ordered as they should be rendered. The IDs must exist in the `blocks` object, and duplicate IDs aren't allowed. |
| `<SettingID>` | String | - | The ID of a setting as defined in the schema of the section or the block. |
| `<SettingValue>` | (multiple) | - | A valid value for the setting. |

For example:

```json
sections: {
<SectionID>: {
  "type": <SectionType>,
  "disabled": <SectionDisabled>,
  "settings": {
    <SettingID>: <SettingValue>
  },
  "blocks": {
    <BlockID>: {
      "type": <BlockType>,
      "settings": {
        <SettingID>: <SettingValue>
      }
    }
  },
  "block_order": <BlockOrder>
}
}
```

For example, the following template renders the `product.liquid` and `product-recommendations.liquid` section files on product pages:

**templates/product.json**

```json
{
  "sections": {
    "main": {
      "type": "product",
      "settings": {
        "show_vendor": true
      }
    },
    "recommendations": {
      "type": "product-recommendations"
    }
  },
  "order": [
    "main",
    "recommendations"
  ]
}
```

**Caution:**

Any sections that are included in a template, and aren't app sections, must exist in the theme. If they don't, then this will result in an error.

###### Platform-controlled settings

In the theme editor, Shopify exposes a [custom CSS setting](https://help.shopify.com/manual/online-store/themes/theme-structure/extend/add-css) at the theme and section level. Any custom CSS that merchants add to a section instance is stored in a `custom_css` attribute in the section data.

This setting is intended to enable users to customize the look and feel of their storefront without editing theme code. As a theme developer, you shouldn't add this setting, or edit the value of this setting after it's set. Instead, you should use dedicated [CSS assets](https://shopify.dev/docs/storefronts/themes/architecture#assets) and [`stylesheet` Liquid tags](https://shopify.dev/docs/storefronts/themes/best-practices/javascript-and-stylesheet-tags#stylesheet), and introduce customization options for CSS in these areas using [theme settings](https://shopify.dev/docs/storefronts/themes/architecture/settings).

---

##### Content

A JSON template accepts only JSON with a fixed schema and list of accepted attributes. For more information, refer to [JSON templates](https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates).

### 2.3.2 Liquid templates

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/templates/liquid-templates

#### Liquid Templates

Liquid templates enable you to manage the visual presentation of various pages in your online store. However, they cannot be combined with [sections](https://shopify.dev/docs/storefronts/themes/architecture/sections). To incorporate sections, you must use [JSON templates](https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates) instead.

A primary application involves creating distinct layouts for product pages. You can designate specific templates to individual products to create varied visual presentations. For instance, all clothing items might employ different templates, each featuring unique combinations of settings, sections, and blocks.

##### Schema

Liquid templates do not follow a predetermined schema structure.

##### Content

Liquid templates support standard HTML and Liquid syntax. They have access to any [global Liquid objects](https://shopify.dev/docs/api/liquid/objects), as well as the object connected to the template. Consult the [documentation for each template type](https://shopify.dev/docs/storefronts/themes/architecture/templates#template-types) for additional details.

### 2.3.3 Alternate templates

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/templates/alternate-templates

#### Alternate templates

When working with template files, you should familiarize yourself with alternate templates and how to use them.

In some cases, you might need to create different markup for the same template. For example, you might want to create an alternate template that includes different sections for specific products.

You can create an alternate template locally, through the theme code editor, or through the theme editor.

**Note:**

"You can't replace the default template with an alternate template." If the default template doesn't meet your needs, then you can edit the template code to customize it.

---

##### Contextual templates

When a merchant adapts a template for a specific buyer context, a new contextual template file is created. The file takes the name of the context in the following format: `index.context.<context-string>.json`

A contextual template file includes the overrides that you make to the template for a context. The context and parent template are defined at the top of the template. The `context` value can contain either `"market": "market-handle"` or `"b2b": true`. For example, the following code contextualizes the `image-banner` section for market handle `ca`:

**index.context.ca**

```json
{
  "context": {
    "market": "ca"
  },
  "parent": "index.json",
  "sections": {
    "image_banner": {
      "blocks": {
        "heading": {
          "disabled": true,
          "settings": {
            "heading_size": "h2"
          }
        },
      "settings": {
        "show_text_box": true
      }
    }
  }
}
```

---

##### Name structure

Alternate template files use the following name structure, where `template-name` is the template name, `template-suffix` is the alternate name, and `template-file-type` is the file type, which is either `json` or `liquid`:

```text
template-name.template-suffix.template-file-type
```

For example, if you create an alternate JSON product template with the name of **alternate**, then the file name would be the following:

```text
product.alternate.json
```

---

##### Use an alternate template

After you've created an alternate template, you can apply it in the following ways:

* Assign it to an associated resource in the Shopify admin.
* Preview it in the theme editor.
* Render it on the storefront with the `view` URL parameter.

**Tip:**

"You can identify which template is currently being used with the `template` object."

---

##### Render an alternate template

Alternate templates can be rendered on the storefront with the `view` URL parameter. This parameter should be in the format of `?view=[template-suffix]`, where `[template-suffix]` is the template's alternate name.

For example, given the `product.alternate.json` template from the previous section, and a product called **Example product**, you can render that product with that template using the following:

```text
/products/example-product?view=alternate
```

### 2.3.4 Metaobject theme templates

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/templates/metaobject

#### Metaobject theme templates

Metaobject theme templates enable the rendering of metaobject webpages per metaobject definition. To create a metaobject template for an Online Store, you must enable the "onlineStore capability." You should also enable the "renderable capability" to enable SEO fields management.

##### Default and alternative templates

"The first template created for a metaobject must be the default template and will be automatically used by all active metaobject entries for that definition." You might optionally create alternative templates after the default template is created.

**Tip:** "The template is empty when it's initially created in the Online Store editor. Merchants must add sections to their metaobject template to display content."

##### Location

Metaobject templates are located in the `templates` directory of the theme:

```text
└── theme
  ├── layout
  ├── templates
  |   ├── 404.json
  |   ├── article.json
  |   |── metaobject
  |   |   |── {type}.json
          ...
      ...
  ...
```

##### Content

Any sections that are available for any template or section group are included in metaobject templates by default. You can access the Liquid metaobject object to display the metaobject fields.

### 2.3.5 404

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/templates/404

#### 404

The `404` template renders page content that is shown to customers if they enter an invalid URL for the store.

**Tip:**

Refer to the [404 template](https://github.com/Shopify/dawn/blob/main/templates/404.json) and its [main section](https://github.com/Shopify/dawn/blob/main/sections/main-404.liquid) in Dawn for an example implementation.

---

##### Location

The `404` template is located in the `templates` directory of the theme:

```text
└── theme
  ├── layout
  ├── templates
  |   ...
  |   ├── 404.json
  |   ...
  ...
```

---

##### Content

There are no suggested objects for a 404 template. However, "the template should make it clear to the customer that the page they were looking for couldn't be found."

You should provide obvious options for how to proceed. For example, you can add links to popular pages, a search bar to help customers find what they're looking for, or a link that redirects customers to your home page or a collection to continue shopping:

```html
<p>
  404
</p>
<h1 class="title">
  Page not found
</h1>
<a href="{{ routes.all_products_collection_url }}" class="button">
  Continue shopping
</a>
```

**Tip:**

"If you're using a JSON template, then any HTML or Liquid code needs to be included in a section that's referenced by the template."

### 2.3.6 agents.md.liquid

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/templates/agents-md-liquid

#### agents.md.liquid

The `agents.md.liquid` template renders the `agents.md` file, which is hosted at the `/agents.md` URL.

The `agents.md` file is the canonical, agent-facing description of a store. It tells AI agents and shopping assistants how to discover the store's commerce capabilities and how to transact with it, including:

* The store's [Universal Commerce Protocol (UCP)](https://ucp.dev) discovery and Model Context Protocol (MCP) endpoints.
* Read-only browsing URLs for product, collection, and search data.
* The store's published policies.
* Guidance for personal shopping agents, such as the [Shop skill](https://shop.app/SKILL.md).

Shopify generates an `agents.md` file by default, which works for most shops, so this template isn't included in any themes by default.

**Tip:**

"The `agents.md` file is served at the bare primary domain, without a locale or Shopify Markets subfolder prefix."

---

##### Relationship to llms.txt and llms-full.txt

`agents.md` is the canonical agent-discovery document. The `/llms.txt` and `/llms-full.txt` URLs mirror the content of `/agents.md` by default on Shopify stores, so agents requesting either one still find a usable document.

Because of this, the `agents.md.liquid` template is the fallback for all three URLs. When a request is served, Shopify checks for theme templates in the following order:

| URL | Template lookup order |
| - | - |
| `/agents.md` | `agents.md.liquid` → Shopify-generated default |
| `/llms.txt` | `llms.txt.liquid` → `agents.md.liquid` → Shopify-generated default |
| `/llms-full.txt` | `llms-full.txt.liquid` → `agents.md.liquid` → Shopify-generated default |

If you add only an `agents.md.liquid` template, it serves all three URLs. To make one URL diverge, add a dedicated `llms.txt.liquid` or `llms-full.txt.liquid` template, which takes precedence for that URL only.

---

##### Location

The `agents.md.liquid` template belongs in the `templates` directory:

```text
└── theme
  ├── layout
  ├── templates
  |   ...
  |   ├── agents.md.liquid
  |   ...
  ...
```

**Adding the template (Desktop)**

1. From your Shopify admin, go to **Online Store** > **Themes**.
2. Find the theme you want to edit, then click **...** > **Edit code**.

**Adding the template (Mobile)**

1. From the Shopify app, tap **Store**.
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage all themes**.
4. Find the theme you want to edit, then tap **...** > **Edit code**.

**File creation steps**

1. In the left sidebar, locate the **Templates** folder.
2. Right-click on the **Templates** folder.
3. Click **New File** from the context menu.
4. Name the file `agents.md.liquid`.
5. Press Enter to create the file.

---

##### Content

This template cannot be a JSON template—it must be `agents.md.liquid`.

The template accepts standard Markdown and [Liquid](https://shopify.dev/docs/api/liquid). To help you build agent instructions with values that stay in sync with the store's actual commerce configuration, the template exposes an `agents` object alongside standard [global Liquid objects](https://shopify.dev/docs/api/liquid/objects) (such as `request` and `shop`).

###### The `agents` object

The `agents` object provides auto-populated UCP and agent-interaction metadata:

| Property | Type | Description |
| - | - | - |
| `agents.store_name` | string | The name of the store. |
| `agents.store_url` | string | The full URL of the store, using the bare primary domain. |
| `agents.ucp_discovery_url` | string | The UCP discovery URL for the store (`{store_url}/.well-known/ucp`). |
| `agents.mcp_endpoint_url` | string | The MCP (Model Context Protocol) endpoint URL (`{store_url}/api/ucp/mcp`). |
| `agents.ucp_versions` | array of string | The supported UCP versions, newest first. Derived from the store's UCP implementation, so it stays in sync automatically. |
| `agents.currency` | string | The store's primary currency code, such as `USD`. |
| `agents.sitemap_url` | string | The store's sitemap URL (`{store_url}/sitemap.xml`). |

###### Example template

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

**Caution:**

"Avoid outputting potentially private merchant data, such as contact email addresses or phone numbers, in this file." The Shopify-generated version deliberately omits contact details because the file is broadly cached and served to every agent requesting it.

---

##### Usage

When you provide an `agents.md.liquid` template, it replaces the Shopify-generated `agents.md` and, unless overridden, the content served at `/llms.txt` and `/llms-full.txt`.

"It's strongly recommended to keep the UCP and MCP endpoints discoverable by using the `agents` object rather than hardcoding URLs." This ensures auto-populated values stay in sync as the store's commerce configuration changes.

### 2.3.7 article

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/templates/article

#### article

The `article` template renders the article page, which contains the full content of the article, as well as an optional comments section for customers. This template is used for items like individual posts in a blog.

**Tip:**

Refer to the [article template](https://github.com/Shopify/dawn/blob/main/templates/article.json) and its [main section](https://github.com/Shopify/dawn/blob/main/sections/main-article.liquid) in Dawn for an example implementation.

---

##### Location

The `article` template is located in the `templates` directory of the theme:

```text
└── theme
  ├── layout
  ├── templates
  |   ├── 404.json
  |   ├── article.json
  |   ...
  ...
```

---

##### Content

You should include the following in your `article` template or a section inside of the template:

* The article object
* The comment form

###### The article object

You can access the Liquid [`article` object](https://shopify.dev/docs/api/liquid/objects/article) to display the article details.

###### The comment form

The comment form can be added with the Liquid [`form` tag](https://shopify.dev/docs/api/liquid/tags/form#form-new_comment) and accompanying `'new_comment', article` parameter. Within the form tag block, you need to include the following:

| Input | `type` | `name` |
| - | - | - |
| Name | `text` | `comment[author]` |
| Email | `email` | `comment[email]` |
| Comment | `textarea` | `comment[body]` |

For example:

```liquid
{% form 'new_comment', article %}
  {{ form.errors | default_errors }}


  <div class="name">
    <label for="name">Name</label>
    <input type="text" name="comment[author]" value="{{ form.author }}" />
  </div>


  <div class="email">
    <label for="email">Email</label>
    <input type="email" name="comment[email]" value="{{ form.email }}" />
  </div>


  <div class="comment">
    <label for="comment">Comment</label>
    <textarea name="comment[body]">{{ form.body }}</textarea>
  </div>


  <div class="submit">
    <input type="submit" value="Post" />
  </div>
{% endform %}
```

**Tip:**

When a customer posts a comment, your code should provide feedback indicating whether it was posted successfully, or if there were any errors.

---

##### Usage

When working with the `article` template, you should familiarize yourself with paginating article comments.

**Tip:**

If you're using a JSON template, then any HTML or Liquid code needs to be included in a [section](https://shopify.dev/docs/storefronts/themes/architecture/sections) that's referenced by the template.

###### Paginate article comments

Article comments can be accessed through the [article object](https://shopify.dev/docs/api/liquid/objects/article#article-comments), and have a limit of 50 per page. For this reason, you should [paginate](https://shopify.dev/docs/api/liquid/tags/paginate) article comments to ensure that they're all accessible:

**Example**

```liquid
{% paginate article.comments by 20 %}
  {% for comment in article.comments %}
    <!-- comment info -->
  {% endfor %}


  {{ paginate | default_pagination }}
{% endpaginate %}
```

### 2.3.8 blog

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/templates/blog

#### blog

The `blog` template renders the blog page, which lists all articles within a blog.

**Tip:**

Refer to the [blog template](https://github.com/Shopify/dawn/blob/main/templates/blog.json) and its [main section](https://github.com/Shopify/dawn/blob/main/sections/main-blog.liquid) in Dawn for an example implementation.

---

##### Location

The `blog` template is located in the `templates` directory of the theme:

```text
└── theme
  ├── layout
  ├── templates
  |   ...
  |   ├── blog.json
  |   ...
  ...
```

---

##### Content

Your blog template should contain a section that includes the `blog` object.

###### The blog object

You can access the Liquid [`blog` object](https://shopify.dev/docs/api/liquid/objects/blog) to display the blog details.

---

##### Usage

When working with the `blog` template, you should familiarize yourself with filtering articles by tag.

**Tip:**

If you're using a JSON template, then any HTML or Liquid code needs to be included in a [section](https://shopify.dev/docs/storefronts/themes/architecture/sections) that's referenced by the template.

###### Filter articles by tag

You can use [article tags](https://shopify.dev/docs/api/liquid/objects/article#article-tags) to filter a blog into smaller subsets of articles. This is done by appending `/tagged/[tag-handle]` to the blog URL, where `[tag-handle]` is the [handleized](https://shopify.dev/docs/api/liquid/filters/handleize) version of the desired article tag.

For example, if you want to show only articles from the `main` blog that are tagged with `news`, then you can use the following URL structure:

```text
https://my-store.myshopify.com/blogs/main/tagged/news
```

You can also filter by multiple tags by combining the handleized tags with a `+`:

```text
https://my-store.myshopify.com/blogs/main/tagged/news+breaking
```

**Tip:**

Instead of manually building this URL structure, you can use the [link_to_tag](https://shopify.dev/docs/api/liquid/filters/link_to_tag), [link_to_add_tag](https://shopify.dev/docs/api/liquid/filters/link_to_add_tag), and [link_to_remove_tag](https://shopify.dev/docs/api/liquid/filters/link_to_remove_tag) URL filters.

### 2.3.9 cart

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/templates/cart

#### cart

The `cart` template renders the `/cart` page, which provides an overview of the contents of a customer's cart. The overview is typically shown in a table format with a row for each line item.

**Tip:**

Refer to the [cart template](https://github.com/Shopify/dawn/blob/main/templates/cart.json), its [items section](https://github.com/Shopify/dawn/blob/main/sections/main-cart-items.liquid), and its [footer section](https://github.com/Shopify/dawn/blob/main/sections/main-cart-footer.liquid) in Dawn for an example implementation.

---

##### Location

The `cart` template is located in the `templates` directory of the theme:

```text
└── theme
  ├── layout
  ├── templates
  |   ...
  |   ├── cart.json
  |   ...
  ...
```

---

##### Content

You should include the cart object in your `cart` template or a section inside of the template.

###### The cart object

You can access the Liquid [`cart` object](https://shopify.dev/docs/api/liquid/objects/cart) to display the cart details.

---

##### Usage

When working with the `cart` template, you should familiarize yourself with the following:

* Using cart line items
* Letting customers proceed to checkout from the cart
* Providing an option to remove line items from the cart
* Updating line item quantities
* Showing discounts
* Using cart notes and attributes
* Displaying line item properties in the cart

**Tip:**

If you're using a JSON template, then any HTML or Liquid code needs to be included in a [section](https://shopify.dev/docs/storefronts/themes/architecture/sections) that's referenced by the template.

###### Cart line items

A [line_item](https://shopify.dev/docs/api/liquid/objects/line_item) is a single line in a shopping cart that records which variant of a product was added, and the associated quantity. For example, if a customer adds both a `size medium` and `size large` of the same `t-shirt` to their cart, then each t-shirt has its own line item.

The `cart` template should include a table where each line item has a row:

**Example**

```liquid
{% for item in cart.items %}
  <!-- line item info -->
{% endfor %}
```

###### Proceed to checkout

To let customers proceed to checkout from the cart, you need to output the cart line items inside a `<form>` element. The form element needs to have attributes of `action="{{ routes.cart_url }}"` and `method="post"`.

The form element also needs to include an `<input />` with attributes of `type="submit"` and `name="checkout"`. This input triggers proceeding to checkout.

**Example**

```liquid
<form action="{{ routes.cart_url }}" method="post">
  {% for item in cart.items %}
    <!-- line item info -->
  {% endfor %}


  <input type="submit" name="checkout" value="Checkout" />
</form>
```

###### Remove line items from the cart

You should give customers the option to remove a line item from their cart. You can do this by including an `<a>` element with each line item, whose `href` attribute references the `url_to_remove` attribute of the [line_item object](https://shopify.dev/docs/api/liquid/objects/line_item):

**Example**

```liquid
{% for item in cart.items %}
  <!-- line item info -->


  <a href="{{ item.url_to_remove }}">Remove</a>
{% endfor %}
```

**Tip:**

Refer to the [Cart API](https://shopify.dev/docs/api/ajax/reference/cart#post-locale-cart-change-js) to learn more about changing the cart using JavaScript.

###### Update line item quantities

You should give customers the option to update line item quantities in their cart. You can do this by including an `<input />` element with each line item that has the attributes of `name="updates[]"` and `value="{{ line_item.quantity}}"`:

**Example**

```liquid
{% for item in cart.items %}
  <!-- line item info -->


  <input type="text" name="updates[]" value="{{ item.quantity }}" />
{% endfor %}
```

To actually trigger an update when a quantity input is changed, you can include an `<input />` with an attribute of `type="submit"` in the cart `<form>`:

**Example**

```html
<input type="submit" value="Update cart" />
```

Submitting the form with this input will reload the page with updated quantities.

**Tip:**

Refer to the `/{locale}/cart/update` endpoint of the [Cart API](https://shopify.dev/docs/api/ajax/reference/cart#post-locale-cart-update-js) to learn more about updating the cart using JavaScript.

###### Show cart and line item discounts

Because discounts can apply to an entire cart or to individual line items, you should show discounts with the cart total summary and individual line item displays. To learn more about discounts and how to build discount displays, refer to [Discounts](https://shopify.dev/docs/storefronts/themes/pricing-payments/discounts).

###### Support cart notes and attributes

You can give customers the option to include additional information with their order through cart notes and attributes.

**Cart notes**

To capture a cart note, include an HTML input, commonly a `<textarea>`, with the attributes `name="note"` and `form="cart"` in the `main-cart-footer.liquid` file:

*main-cart-footer.liquid*

```html
<textarea name="note" form="cart"></textarea>
```

This value is accessible through the `note` attribute of the [cart object](https://shopify.dev/docs/api/liquid/objects/cart#cart-note).

**Cart attributes**

To capture a cart attribute, include an HTML input with the attributes `name="attributes[attribute-name]"` and `form="cart"` in the `main-cart-footer.liquid` file:

*main-cart-footer.liquid*

```liquid
<p>
  <label>Please let us know your favorite color</label>


  <input type="text" name="attributes[Favorite color]" form="cart" value="{{ cart.attributes['Favorite color'] }}" />
</p>
```

Any values are accessible through the `attributes` attribute of the [cart object](https://shopify.dev/docs/api/liquid/objects/cart#cart-attributes).

###### Display line item properties

When items are added to the cart, they can have [line item properties](https://shopify.dev/docs/api/liquid/objects/line_item#line_item-properties) included with them. You can display these properties on the cart page by looping through each property:

**Example**

```liquid
{% for item in cart.items %}
  <!-- line item info -->


  {% unless item.properties == empty %}
    {% for property in item.properties %}
      {{ property.first }}:


      {% if property.last contains '/uploads/' %}
        <a href="{{ property.last }}">{{ property.last | split: '/' | last }}</a>
      {% else %}
        {{ property.last }}
      {% endif %}
    {% endfor %}
  {% endunless %}
{% endfor %}
```

**Tip:**

If two of the same item are added to the cart, but have unique line item properties, then they'll be split into separate line items.

###### Remote products

Products from other stores may be present in the cart, if a store has opted in to displaying remote products on their storefront. No theme changes are required to support this. Remote products in the cart will contain the store name in the title to signify that they are from a different store. You can identify remote products by the presence of [`product.remote_details`](https://shopify.dev/docs/api/liquid/objects/remote_product#remote_product-remote_details) or [`remote:true`](https://shopify.dev/docs/api/ajax/reference/cart#json-of-a-cart-with-remote-products) on the cart line items.

**Caution:**

Themes must use Liquid's [`cart.items`](https://shopify.dev/docs/api/liquid/objects/cart#cart-items) or the [Cart Ajax API](https://shopify.dev/docs/api/ajax/reference/cart) to be compatible with remote products. The [Storefront API](https://shopify.dev/docs/api/storefront/latest/queries/cart) will not distinguish between remote and owned products. Support for this is coming soon.

### 2.3.10 collection

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/templates/collection

#### collection

The `collection` template renders the collection page, which lists all products within a collection.

**Tip:**

Refer to the [collection template](https://github.com/Shopify/dawn/blob/main/templates/collection.json), its [banner section](https://github.com/Shopify/dawn/blob/main/sections/main-collection-banner.liquid), and its [product grid section](https://github.com/Shopify/dawn/blob/main/sections/main-collection-product-grid.liquid) in Dawn for an example implementation.

---

##### Location

The `collection` template is located in the `templates` directory of the theme:

```text
└── theme
  ├── layout
  ├── templates
  |   ...
  |   ├── collection.json
  |   ...
  ...
```

---

##### Content

You should include the collection object in your `collection` template or a section inside of the template.

###### The collection object

You can access the Liquid [`collection` object](https://shopify.dev/docs/api/liquid/objects/collection) to display the collection details.

---

##### Usage

When working with the `collection` template, you should familiarize yourself with the following:

* Filtering collections
* Sorting products in a collection
* Paginating products

**Tip:**

If you're using a JSON template, then any HTML or Liquid code needs to be included in a [section](https://shopify.dev/docs/storefronts/themes/architecture/sections) that's referenced by the template.

###### Filter collections

You can use [storefront filtering](https://shopify.dev/docs/storefronts/themes/navigation-search/filtering) to filter collections into smaller subsets of products.

###### Sort products in a collection

You can choose the order that products are sorted in through the `sort_by` URL parameter on collection pages:

**Example**

```text
https://my-store.myshopify.com/collections/frontpage?sort_by=price-descending
```

Through the [collection object](https://shopify.dev/docs/api/liquid/objects/collection), you can access the following:

* The available options with the `sort_options` attribute.
* The currently selected option, if one is selected, with the `sort_by` attribute.
* The default option with the `default_sort_by` attribute.

You can output the available options in a `<select>` element for customers to make their selection, and you can initialize the selector based on the current and default options. When a new selection is made, you should use JavaScript to append the URL parameter and refresh the page.

The following is a simple example of a sort order selector, and accompanying JavaScript:

**Example**

```liquid
<select id="sort-by">
  {% assign sort_by = collection.sort_by | default: collection.default_sort_by %}


  {% for option in collection.sort_options %}
    <option value="{{ option.value }}" {% if option.value == sort_by %}selected="selected"{% endif %}>
      {{ option.name }}
    </option>
  {% endfor %}
</select>


<script>
  Shopify.queryParams = {};


  // Preserve existing query parameters
  if (location.search.length) {
    var params = location.search.substr(1).split('&');


    for (var i = 0; i < params.length; i++) {
      var keyValue = params[i].split('=');


      if (keyValue.length) {
        Shopify.queryParams[decodeURIComponent(keyValue[0])] = decodeURIComponent(keyValue[1]);
      }
    }
  }


  // Update sort_by query parameter on select change
  document.querySelector('#sort-by').addEventListener('change', function(e) {
    var value = e.target.value;


    Shopify.queryParams.sort_by = value;
    location.search = new URLSearchParams(Shopify.queryParams).toString();
  });
</script>
```

###### Paginate products

Products can be accessed through the `products` attribute of the [collection object](https://shopify.dev/docs/api/liquid/objects/collection#collection-products), and have a limit of 50 per page. For this reason, you should [paginate](https://shopify.dev/docs/api/liquid/tags/paginate) a collection's products to ensure that they're all accessible:

**Example**

```liquid
{% paginate collection.products by 20 %}
  {% for product in collection.products %}
    <!-- product info -->
  {% endfor %}


  {{ paginate | default_pagination }}
{% endpaginate %}
```

###### Remote products

If a store has opted in to displaying remote products on their storefront, products from other stores are surfaced automatically in collections. No theme changes are required to support this. Remote product images contain special badges to signify that they're from a different store.

**Caution:**

Remote products aren't yet supported in themes that surface collection products through APIs. Themes must be using Liquid's [`collection.products`](https://shopify.dev/docs/api/liquid/objects/collection#collection-products) to be compatible with this feature.

### 2.3.11 gift_card.liquid

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/templates/gift-card-liquid

#### gift_card.liquid

The `gift_card.liquid` template renders the gift card page, which displays the "gift card issued to a customer upon purchase."

**Tip:**

Refer to the [gift_card.liquid template](https://github.com/Shopify/dawn/blob/main/templates/gift_card.liquid) in Dawn for an example of this template.

Unlike other pages in your store, gift card pages are hosted on the `checkout.shopify.com` domain. Gift card URLs contain unique identifiers for your store and gift card:

```text
https://checkout.shopify.com/gift_cards/[store_id]/[gift_card_token]
```

---

##### Location

The `gift_card` template is located in the `templates` directory of the theme:

```text
└── theme
  ├── layout
  ├── templates
  |   ...
  |   ├── gift_card.liquid
  |   ...
  ...
```

---

##### Content

This template cannot be a JSON template.

You can include the following in your gift_card template or a section inside of the template:

* The gift_card object
  * You can also include a QR code or Apple wallet passes.

###### The gift_card object

You can access the Liquid `gift_card` object to display the gift card details.

---

##### Usage

When working with the `gift_card` template, you should familiarize yourself with the following:

* Adding a QR code link
* Including Apple Wallet passes to the template
* Displaying only the gift card details

To learn how to personalize gift card templates with a custom image, refer to the [Shopify Help Center](https://help.shopify.com/manual/online-store/themes/themes-by-shopify/vintage-themes/customizing-vintage-themes/personalize-gift-cards).

###### QR code

You can include a QR code link by adding JavaScript that generates a QR code. Add the following snippets in the `<head>` and `<body>` elements of the page, respectively. To control the content of the QR code, update the `text` property with the desired content. In this example, the QR code links to the store's URL.

**Include in `<head>`**

```liquid
{{ 'vendor/qrcode.js' | shopify_asset_url | script_tag }}
```

**Include in `<body>`**

```liquid
<div id="qr-code"></div>

<script>
  new QRCode(document.getElementById('qr-code'), {
    text: '{{ shop.url }}',
    width: 120,
    height: 120
  });
</script>
```

###### Apple Wallet passes

You can include Apple Wallet passes by adding the following snippet to the `<body>` element of the page:

```liquid
{% if gift_card.pass_url %}
<a href="{{ gift_card.pass_url }}" >
  <img id="apple-wallet-badge"
    src="/content/assets/images/{{ "gift-card/add-to-apple-wallet.svg' | shopify_asset_url }}"
    width="120"
    height="40"
    alt="Add To Apple Wallet" />
  </a>
{% endif %}
```

###### Display only the gift card details

If you don't want to include theme elements, like the header and footer, you can choose to render the `gift_card.liquid` template with no layout or with a custom layout, using the Liquid `layout` object.

For example:

*gift_card.liquid*

```liquid
{% layout none %}

<!-- template content -->
```

---

##### Preview the template

You can preview the gift card's appearance by navigating to the gift card template from the theme editor.

1. From the theme editor, open the drop-down menu at the top of the page.
2. Under **Templates**, click **Others**. Then click **Gift card**.

**Note:**

If you can't find the gift card template in the theme editor's navigation menu, then you might need to insert the `content_for_header` Liquid object in the HTML `<head>` tag of your `gift_card.liquid` template.

### 2.3.12 index

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/templates/index-template

#### index

The `index` template renders the home page of the store, located at the root URL (`/`). The home page often serves as a customer's first impression of a merchant's store, so the `index` template should include versatile options for merchants to tell their story.

**Tip:**

Refer to the [index template](https://github.com/Shopify/dawn/blob/main/templates/index.json) in Dawn for an example of this template.

---

##### Location

The `index` template is located in the `templates` directory of the theme:

```text
└── theme
  ├── layout
  ├── templates
  |   ...
  |   ├── index.json
  |   ...
  ...
```

---

##### Usage

When working with the `index` template, you should familiarize yourself with the differences between JSON and Liquid index templates.

###### JSON vs. Liquid

Both JSON and Liquid index templates allow merchants to add and remove sections using the theme editor. Although the Liquid index template has this functionality, in most cases, you should use a JSON template (`index.json`) as your index template. JSON templates have the following advantages over Liquid templates:

* JSON templates give more flexibility for merchants to add, remove, and reorder sections, including app sections.
* JSON templates store their own data, which minimizes the amount of data in `settings_data.json` and improves the performance of the theme editor.

### 2.3.13 list-collections

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/templates/list-collections

#### list-collections

The `list-collections` template renders the collection list page, which lists all the store's [collections](https://help.shopify.com/manual/products/collections). This page is located at the `/collections` URL of the store.

**Tip:**

Refer to the [list-collections template](https://github.com/Shopify/dawn/blob/main/templates/list-collections.json) and its [main section](https://github.com/Shopify/dawn/blob/main/sections/main-list-collections.liquid) in Dawn for an example implementation.

##### Location

The `list-collections` template is located in the `templates` directory of the theme:

```text
└── theme
  ├── layout
  ├── templates
  |   ...
  |   ├── list-collections.json
  |   ...
  ...
```

##### Content

You can include the following in your list-collections template or a section inside of the template:

* The collections object

###### The collections object

You can access the Liquid [`collections` object](https://shopify.dev/docs/api/liquid/objects/collections) to display the store's collections.

##### Usage

When working with the `list-collections` template, you should familiarize yourself with the following:

* Changing the order of collections
* Setting a fallback image for collection images

**Tip:**

If you're using a JSON template, then any HTML or Liquid code needs to be included in a [section](https://shopify.dev/docs/storefronts/themes/architecture/sections) that's referenced by the template.

###### Change the order of collections

Typically, this template includes the following loop through the collections to output the display, which outputs the collections in alphabetical order:

```liquid
{% for collection in collections %}
  <!-- collection info -->
{% endfor %}
```

If you want to change the order, then you can build a [menu](https://help.shopify.com/en/manual/online-store/menus-and-links/editing-menus) to host the collections in your desired order, and loop through the menu items. If you use this method, then you should build a [setting](https://shopify.dev/docs/themes/architecture/settings/input-settings#link_list) to allow merchants to select the menu that's used. You can access the menu through the Liquid [`linklist` object](https://shopify.dev/docs/api/liquid/objects/linklist), filter the menu items for collections based on [`link.type`](https://shopify.dev/docs/api/liquid/objects/link#link-type), and access the collection information through [`link.object`](https://shopify.dev/docs/api/liquid/objects/link#link-object).

For example:

```liquid
{% for link in settings.collection_list_menu.links %}
{% if link.type == 'collection_link' %}
  {% assign collection = link.object %}

  <!-- collection info -->
{% endif %}
{% endfor %}
```

###### Collection image fallback

You should have a fallback for the case that a collection doesn't have a [collection image](https://shopify.dev/docs/api/liquid/objects/collection#collection-image). For example, you might use the image of the first product within the collection:

```liquid
{% if collection.image %}
{{ collection.image | image_url: width: 450, height: 450 | image_tag: collection.image.alt }}
{% else %}
{% assign alt = collection.title | escape %}
{{ collection.products.first.image | image_url: width: 450, height: 450 | image_tag: alt }}
{% endif %}
```

### 2.3.14 llms-full.txt.liquid

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/templates/llms-full-txt-liquid

#### llms-full.txt.liquid

The `llms-full.txt.liquid` template renders the `llms-full.txt` file, which is hosted at the `/llms-full.txt` URL.

`/llms-full.txt` is an agent-discovery file and an alternate URL for [`/agents.md`](https://shopify.dev/docs/storefronts/themes/architecture/templates/agents-md-liquid), which is the canonical agent-discovery document. By default, `/llms-full.txt` mirrors the content of `/agents.md`, so agents and crawlers that request it still find a usable, agent-facing description of the store. As a result, this template isn't included in any themes by default.

**Tip:**

The `llms-full.txt` file is served at the bare primary domain, without a locale or [Shopify Markets](https://shopify.dev/docs/storefronts/themes/markets) subfolder prefix. It has no localized counterpart.

---

##### When to use this template

In most cases you don't need a separate `llms-full.txt.liquid` template. If you want to customize the agent-discovery content for every URL at once, then add an [`agents.md.liquid`](https://shopify.dev/docs/storefronts/themes/architecture/templates/agents-md-liquid) template instead — `/llms-full.txt` falls back to it automatically.

Add an `llms-full.txt.liquid` template only when you want "/llms-full.txt" to diverge from "/agents.md". The template lookup order for `/llms-full.txt` is:

1. `llms-full.txt.liquid` (if present)
2. [`agents.md.liquid`](https://shopify.dev/docs/storefronts/themes/architecture/templates/agents-md-liquid) (if present)
3. The Shopify-generated default

A dedicated `llms-full.txt.liquid` takes precedence for `/llms-full.txt` only, while `/agents.md` and `/llms.txt` are unaffected.

---

##### Location

The `llms-full.txt.liquid` template is located in the `templates` directory of the theme:

```text
└── theme
  ├── layout
  ├── templates
  |   ...
  |   ├── llms-full.txt.liquid
  |   ...
  ...
```

If your theme doesn't already contain the `llms-full.txt.liquid` template, you can add it with the following steps:

**Desktop**

1. From your Shopify admin, go to **Online Store** > **Themes**.
2. Find the theme that you want to edit, and then click **...** > **Edit code**.

**Mobile**

1. From the [Shopify app](https://www.shopify.com/install/detect), tap **Store**.
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage all themes**.
4. Find the theme that you want to edit, and then tap **...** > **Edit code**.

**Creating the file**

1. In the left sidebar, locate the **Templates** folder.
2. Right-click on the **Templates** folder.
3. Click **New File** from the context menu.
4. Name the file `llms-full.txt.liquid`.
5. Press Enter to create the file.

---

##### Content

This template cannot be a [JSON template](https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates). It must be `llms-full.txt.liquid`.

The template accepts standard text or Markdown and [Liquid](https://shopify.dev/docs/api/liquid). Like [`agents.md.liquid`](https://shopify.dev/docs/storefronts/themes/architecture/templates/agents-md-liquid#the-agents-object), it has access to the `agents` object for auto-populated UCP and agent-interaction metadata, alongside the standard [global Liquid objects](https://shopify.dev/docs/api/liquid/objects). For the full list of `agents` properties, refer to [agents.md.liquid](https://shopify.dev/docs/storefronts/themes/architecture/templates/agents-md-liquid#the-agents-object).

###### Example

```liquid
# {{ agents.store_name }} — Full agent reference


The canonical description is at {{ agents.store_url }}/agents.md.


## Commerce Protocol (UCP)
- UCP discovery: {{ agents.ucp_discovery_url }}
- MCP endpoint: {{ agents.mcp_endpoint_url }}


### Supported UCP versions
{% for version in agents.ucp_versions %}
- {{ version }}
{% endfor %}


## Read-only browsing
- All products: `GET /collections/all`
- Sitemap: {{ agents.sitemap_url }}
```

---

##### Usage

To customize agent-discovery content for `/agents.md`, `/llms.txt`, and `/llms-full.txt` together, edit [`agents.md.liquid`](https://shopify.dev/docs/storefronts/themes/architecture/templates/agents-md-liquid). Use `llms-full.txt.liquid` only when `/llms-full.txt` requires different content than `/agents.md`.

### 2.3.15 llms.txt.liquid

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/templates/llms-txt-liquid

#### llms.txt.liquid

The `llms.txt.liquid` template renders the `llms.txt` file, which is hosted at the `/llms.txt` URL.

`/llms.txt` is an agent-discovery file and an alternate URL for `/agents.md`, which is the canonical agent-discovery document. By default, `/llms.txt` mirrors the content of `/agents.md`, so agents and crawlers that request it still find a usable, agent-facing description of the store. As a result, this template isn't included in any themes by default.

**Tip:**

"The `llms.txt` file is served at the bare primary domain, without a locale or Shopify Markets subfolder prefix."

##### When to use this template

In most cases you don't need a separate `llms.txt.liquid` template. If you want to customize the agent-discovery content for every URL at once, then add an `agents.md.liquid` template instead — `/llms.txt` falls back to it automatically.

Add an `llms.txt.liquid` template only when you want `/llms.txt` to **diverge** from `/agents.md`. The template lookup order for `/llms.txt` is:

1. `llms.txt.liquid` (if present)
2. `agents.md.liquid` (if present)
3. The Shopify-generated default

A dedicated `llms.txt.liquid` takes precedence for `/llms.txt` only, while `/agents.md` and `/llms-full.txt` are unaffected.

##### Location

The `llms.txt.liquid` template is located in the `templates` directory of the theme:

```text
└── theme
  ├── layout
  ├── templates
  |   ...
  |   ├── llms.txt.liquid
  |   ...
  ...
```

**Adding the template**

*Desktop*

1. From your Shopify admin, go to **Online Store** > **Themes**.
2. Find the theme that you want to edit, and then click **...** > **Edit code**.

*Mobile*

1. From the Shopify app, tap **Store**.
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage all themes**.
4. Find the theme that you want to edit, and then tap **...** > **Edit code**.

*Creating the file*

1. In the left sidebar, locate the **Templates** folder.
2. Right-click on the **Templates** folder.
3. Click **New File** from the context menu.
4. Name the file `llms.txt.liquid`.
5. Press Enter to create the file.

##### Content

"This template can't be a JSON template. It must be `llms.txt.liquid`."

The template accepts standard text or Markdown and Liquid. Like `agents.md.liquid`, it has access to the `agents` object for auto-populated UCP and agent-interaction metadata, alongside the standard global Liquid objects. For the full list of `agents` properties, refer to `agents.md.liquid`.

###### Example

```liquid
# {{ agents.store_name }}

> Agent-discovery summary. The canonical, full description is at {{ agents.store_url }}/agents.md.

- UCP discovery: {{ agents.ucp_discovery_url }}
- MCP endpoint: {{ agents.mcp_endpoint_url }}
- Sitemap: {{ agents.sitemap_url }}
```

##### Usage

To customize the agent-discovery content for `/agents.md`, `/llms.txt`, and `/llms-full.txt` together, edit `agents.md.liquid`. Use `llms.txt.liquid` only when `/llms.txt` needs content that differs from `/agents.md`.

### 2.3.16 page

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/templates/page

#### page

The `page` template renders the store's [pages](https://help.shopify.com/manual/online-store/themes/theme-structure/pages), like **About us** or **Contact us**.

**Tip:**

Refer to the [page template](https://github.com/Shopify/dawn/blob/main/templates/page.json) and its [main section](https://github.com/Shopify/dawn/blob/main/sections/main-page.liquid) in Dawn for an example implementation.

---

##### Location

The `page` template is located in the `templates` directory of the theme:

```text
└── theme
  ├── layout
  ├── templates
  |   ...
  |   ├── page.json
  |   ...
  ...
```

---

##### Content

You can include the following in your page template or a section inside of the template:

* The page object

###### The page object

You can access the Liquid [`page` object](https://shopify.dev/docs/api/liquid/objects/page) to display the page details.

**Tip:**

"If you're using a JSON template, then any HTML or Liquid code needs to be included in a [section](https://shopify.dev/docs/storefronts/themes/architecture/sections) that's referenced by the template."

### 2.3.17 password

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/templates/password

#### password

The `password` template renders the password page, a landing page displayed when password protection is applied to a store. This page includes an editable merchant message and a password form for customer access.

**Tip:**

Refer to the password template and its sections in Dawn for an example implementation.

---

##### Location

The `password` template is located in the `templates` directory of the theme:

```text
└── theme
  ├── layout
  ├── templates
  |   ...
  |   ├── password.json
  |   ...
  ...
```

---

##### Content

You can include the following in your password template or a section inside of the template:

* A password message
* The password form
* The email sign-up form

**Tip:**

If you're using a JSON template, then any HTML or Liquid code needs to be included in a section that's referenced by the template.

###### The password message

When password protection is enabled on a store, there's also the option to include a message. This message can be shown using the `password_message` attribute of the Liquid `shop` object:

```liquid
{% unless shop.password_message == blank %}
  {{ shop.password_message }}
{% endunless %}
```

###### The password form

The password form can be added with the Liquid `form` tag and accompanying `'storefront_password'` parameter. Within the form tag block, you need to include an `<input />` with the following attributes:

* `type="password"`
* `name="password"`

For example:

```liquid
{% form 'storefront_password' %}
  {{ form.errors | default_errors }}

  <div class="password">
    <label for="password">Password</label>
    <input type="password" name="password" />
  </div>

  <div class="submit">
    <input type="submit" value="Sign in" />
  </div>
{% endform %}
```

###### The email sign-up form

You can include an email sign-up form to capture customer emails with the Liquid `form` tag and accompanying `'customer'` parameter. Within the form tag block, you need to include the following:

| Input | `type` | `name` | `value` |
| - | - | - | - |
| Tags | `hidden` | `contact[tags]` | `prospect, password page` |
| Email | `email` | `contact[email]` | - |

For example:

```liquid
{% form 'customer' %}
  {{ form.errors | default_errors }}

  <div class="tags">
    <input type="hidden" name="contact[tags]" />
  </div>

  <div class="email">
    <label for="email">Email</label>
    <input type="email" name="contact[email]" />
  </div>

  <div class="submit">
    <input type="submit" value="Sign in" />
  </div>
{% endform %}
```

**Tip:**

Shopify assists merchants in marketing to customers created with the `prospect` and `password page` tags, but you can use your own custom tags as well.

---

##### Usage

If you're working on a development store, then you can't show a custom password page on the store. A development store-specific password page is always displayed.

The customizable password page isn't used to control access to your dev store, but you can view it after you log in and edit it from the Shopify admin.

To view the customizable password page, logged-in visitors can navigate to `https://your-store-name.myshopify.com/password`, where `your-store-name` is the name of the dev store.

### 2.3.18 product

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/templates/product

#### product

The `product` template renders the product page, which contains a product's media and content, as well as a form for customers to select a variant and add it to the cart.

**Tip:**

Refer to the [product template](https://github.com/Shopify/dawn/blob/main/templates/product.json) and its [main section](https://github.com/Shopify/dawn/blob/main/sections/main-product.liquid) in Dawn for an example implementation.

---

##### Location

The `product` template is located in the `templates` directory of the theme:

```text
└── theme
  ├── layout
  ├── templates
  |   ...
  |   ├── product.json
  |     ...
  ...
```

---

##### Content

You should include the following in your `product` template or a section inside of the template:

* The product object

* The product form, with the following components:

  * A variant selector
  * A quantity input
  * Accelerated checkout buttons
  * Input elements for line item properties

  Optionally, you might want to show product recommendations on the product page.

**Tip:**

If you're using a JSON template, then any HTML or Liquid code needs to be included in a [section](https://shopify.dev/docs/storefronts/themes/architecture/sections) that's referenced by the template.

###### The product object

You can access the Liquid [`product` object](https://shopify.dev/docs/api/liquid/objects/product) to display the product details.

###### The product form

The product form is the main method for customers to add a product variant to the cart. You can include the product form with the Liquid [`form` tag](https://shopify.dev/docs/api/liquid/tags/form#form-product) and accompanying `'product'` parameter:

**Example**

```liquid
{% form 'product' %}
  <!-- form content -->


  <input type="submit" value="Add to cart" />
{% endform %}
```

**Tip:**

If you need to add custom attributes to the form, like a class or ID, then you can [modify the form's default attributes](https://shopify.dev/docs/api/liquid/tags/form#form-html-attributes).

Inside the form, you need the following:

* The variant selector
* The quantity input
* Accelerated checkout buttons

**The variant selector**

A variant selector is typically structured as one or more option value inputs that enable a buyer to specify which product variant to purchase. You can refer the [product variants section](https://shopify.dev/docs/storefronts/themes/product-merchandising/variants) for an example implementation.

**The quantity input**

You should include a quantity input to allow customers to choose the quantity of a variant that they're adding to the cart. This input needs to have an attribute of `name="quantity"`, and the value must be an integer greater than 1:

```html
<input type="text" name="quantity" min="1" value="1" />
```

**Accelerated checkout buttons**

You should include [accelerated checkout buttons](https://help.shopify.com/manual/online-store/accelerated-checkout) to allow customers to quickly buy the product they're viewing. These can be added with the `payment_button` Liquid [HTML filter](https://shopify.dev/docs/api/liquid/filters/payment_button):

```liquid
{% form 'product' %}
  <!-- form content -->


  <input type="submit" value="Add to cart" />
  {{ form | payment_button }}
{% endform %}
```

**Tip:**

To learn about styling and customizing these buttons, refer to the [accelerated checkout reference](https://shopify.dev/docs/storefronts/themes/pricing-payments/accelerated-checkout)

**Line item properties**

You can give customers the option to include additional information for a variant that's added to the cart by using line item properties. You can use line item properties to enable customers to customize orders or provide supplementary information. For example, you can capture monogram or engraving text, or let a customer upload a file.

These properties are captured through input elements with an attribute of `name="properties[property-name]"`, where `property-name` is the name of your custom property. Any property inputs need to be included inside the product form:

```liquid
{% form 'product' %}
  <!-- form content -->


  <input type="text" name="properties[Monogram]" />
  <input type="submit" value="Add to cart" />
{% endform %}
```

**Tip:**

To learn about displaying any line item properties that are collected in the cart, refer to the cart template reference for [line item properties](https://shopify.dev/docs/storefronts/themes/architecture/templates/cart#display-line-item-properties).

---

##### Usage

When working with the `product` template, you should familiarize yourself with the following:

* The Cart AJAX API
* Showing product recommendations

**Tip:**

If you're using a JSON template, then any HTML or Liquid code needs to be included in a [section](https://shopify.dev/docs/storefronts/themes/architecture/sections) that's referenced by the template.

###### The Cart AJAX API

You can use the [Cart API](https://shopify.dev/docs/api/ajax/reference/cart), which is part of the AJAX API, to allow customers to add a variant to the cart without redirecting them to the cart page afterwards.

###### Show product recommendations

You can use the [Product Recommendations API](https://shopify.dev/docs/api/ajax/reference/product-recommendations), which is part of the Ajax API, to upsell customers on related products. To learn more about how to use this API, refer to [Product recommendations](https://shopify.dev/docs/storefronts/themes/product-merchandising/recommendations).

### 2.3.19 robots.txt.liquid

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/templates/robots-txt-liquid

#### robots.txt.liquid

The `robots.txt.liquid` template renders the `robots.txt` file, which is hosted at the `/robots.txt` URL.

The `robots.txt` file tells search engines which pages can, or can't, be crawled on a site. It contains groups of rules for doing so, and each group has three main components:

* The user agent, which notes which crawler the group of rules applies to. For example, `adsbot-google`.
* The rules themselves, which note specific URLs that crawlers can, or can't, access.
* An optional sitemap URL.

Shopify generates a `robots.txt` file by default, which works for most shops, so this template isn't included in any themes by default.

> **Tip:** If you want to customize the `robots.txt.liquid` template, then refer to Customize robots.txt for more information.

##### Location

The `robots.txt.liquid` template is located in the `templates` directory of the theme:

```text
└── theme
  ├── layout
  ├── templates
  |   ...
  |   ├── robots.txt.liquid
  |   ...
  ...
```

If your theme doesn't already contain the `robots.txt.liquid` template, then you can add it with the following steps:

**Desktop**

1. From your Shopify admin, go to **Online Store** > **Themes**.
2. Find the theme that you want to edit, and then click **...** > **Edit code**.

**Mobile**

1. From the Shopify app, tap **Store**.
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage all themes**.
4. Find the theme that you want to edit, and then tap **...** > **Edit code**.

**Creating the File**

1. In the left sidebar, locate the **Templates** folder.
2. Right-click on the **Templates** folder.
3. Click **New File** from the context menu.
4. Name the file `robots.txt.liquid`.
5. Press Enter to create the file.

##### Content

This template can't be a JSON template. It must be `robots.txt.liquid`.

The rules included in the default `robots.txt` file are mirrored through the Liquid `robots` object, which the `robots.txt.liquid` template uses to output the rules.

###### Example

```liquid
{% for group in robots.default_groups %}
  {{- group.user_agent -}}


  {% for rule in group.rules %}
    {{- rule -}}
  {% endfor %}


  {%- if group.sitemap != blank -%}
    {{ group.sitemap }}
  {%- endif -%}
{% endfor %}
```

While you can replace all the template content with plain text rules, it's strongly recommended to use the provided Liquid objects whenever possible. The default rules are updated regularly to ensure that SEO best practices are always applied.

##### Usage

If you want to customize the `robots.txt.liquid` template, then you need to add it with the following steps:

1. In the code editor for the theme you want to edit, locate the **Templates** folder.
2. Right-click on the **Templates** folder.
3. Click **New File** from the context menu.
4. Name the file `robots.txt.liquid`.
5. Press Enter to create the file.

To learn about customizing this template, refer to the Customize robots.txt documentation.

### 2.3.20 search

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/templates/search

#### search

The `search` template renders the search page, which displays the results of a [storefront search](https://help.shopify.com/en/manual/online-store/storefront-search).

**Tip:**

Refer to the [search template](https://github.com/Shopify/dawn/blob/main/templates/search.json) and its [main section](https://github.com/Shopify/dawn/blob/main/sections/main-search.liquid) in Dawn for an example implementation.

---

##### Location

The `search` template is located in the `templates` directory of the theme:

```text
└── theme
  ├── layout
  ├── templates
  |   ...
  |   ├── search.json
  |     ...
  ...
```

---

##### Content

You should include the following in your `search` template or a section inside of the template:

* The search object
* The search form
* The search results

###### The search object

You can access the Liquid [`search` object](https://shopify.dev/docs/api/liquid/objects/search) to display the search details.

###### The search form

To land on the search page, customers need to perform a search through a search form. You can include a search form in your theme with a `<form>` element that has an attribute of `action="{{ routes.search_url }}"`. Inside the form, you need an input with the following attributes:

* `type="text"`
* `name="q"`.

  You should also set the value of the input to reflect the value of the `terms` attribute of the [`search` object](https://shopify.dev/docs/api/liquid/objects/search#search-terms) so that the customer's search terms are preserved:

**Example**

```liquid
<form action="{{ routes.search_url }}">
  <input type="text"
    placeholder="Search"
    name="q"
    value="{{ search.terms | escape }}"
  />
  <input type="submit" value="Search" />
</form>
```

**Tip:**

To learn more about the search form, refer to [Storefront search](https://shopify.dev/docs/storefronts/themes/navigation-search/search).

###### The search results

You can display the search results by looping through the values of the `results` attribute of the [`search` object](https://shopify.dev/docs/api/liquid/objects/search#search-results):

**Example**

```liquid
{% for item in search.results %}
  <!-- item details -->
{% endfor %}
```

###### Remote products

If a store has opted in to displaying remote products on their storefront, products from other stores are surfaced automatically in search results. No theme changes are required to support this. Remote product images contain special badges to signify that they're from a different store.

**Caution:**

"Remote products aren't yet supported in themes that surface search results through APIs." Themes must be using Liquid's [`search.results`](https://shopify.dev/docs/api/liquid/objects/search#search-results) to be compatible with this feature.

---

##### Usage

When working with the `search` template, you should familiarize yourself with highlighting search terms.

**Tip:**

If you're using a JSON template, then any HTML or Liquid code needs to be included in a [section](https://shopify.dev/docs/storefronts/themes/architecture/sections) that's referenced by the template.

###### Highlight search terms

If you output any associated content with your search results, then you can highlight the search terms within that content using the Liquid [`highlight` filter](https://shopify.dev/docs/api/liquid/filters/highlight):

**Example**

```liquid
{% for item in search.results %}
  <!-- item details -->


  {{ item.content | highlight: search.terms }}
{% endfor %}
```

**Tip:**

"This filter bolds any matching text by wrapping it in a `<strong>` element, with an attribute of `class="highlight"`" if you want to add any additional styling.

---

## 2.4 Sections

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/sections

### Sections

Sections are Liquid files that allow you to create reusable modules of content that can be customized by merchants. They can also include [blocks](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#blocks) which allow merchants to add, remove, and reorder content within a section.

For example, you can create an **Image with text** section that displays an image and text side-by-side with options for merchants to choose the image, set the text, and select the display order.

Sections can be dynamically added to pages using [JSON templates](https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates) or [section groups](https://shopify.dev/docs/storefronts/themes/architecture/section-groups), giving merchants flexibility to easily customize page layouts. Sections that are included in JSON templates or section groups can support [app blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks), which give merchants the option to include app content within a section without having to edit theme code. JSON templates and section groups can render up to 25 sections, and each section can have up to 50 [blocks](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#blocks).

Sections can also be [included statically](#statically-render-a-section), which can provide merchants with in-context customization options for static content.

By default, sections are available for any template or section group. You can limit which templates and section groups have access in the [section schema](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema).

The following diagram shows the main theme architecture components with sections highlighted in blue and blocks highlighted in red.

---

#### Location

Section files are located in the `sections` directory of the theme:

```text
└── theme
  ...
  ├── templates
  ├── sections
  ...
```

---

#### Content

Sections can contain three main types of content:

| Type | Description | Required |
| - | - | - |
| **Main content** | Any HTML or Liquid content you might want to include in the section. Sections have the same access to [global objects](https://shopify.dev/docs/api/liquid/objects), [tags](https://shopify.dev/docs/api/liquid/tags), and [filters](https://shopify.dev/docs/api/liquid/filters) as other Liquid theme files, as well as the following section-specific objects:<br><br>- **The [`section` object](https://shopify.dev/docs/api/liquid/objects/section)** - Contains the section's properties and setting values.<br>- **The [`block` object](https://shopify.dev/docs/api/liquid/objects/block)** - Contains the properties and setting values of a single section block.<br><br>Aside from global objects, variables created outside of sections aren't accessible within sections. The section and block objects, as well as variables created within sections, aren't available outside of their respective section. The only exception is when you reference section and block objects within a snippet that's rendered inside the section you're referencing. | No |
| **Assets** | Sections can bundle their own JavaScript and stylesheet assets with the following section-specific Liquid tags:<br><br>- [`{% javascript %}`](https://shopify.dev/docs/storefronts/themes/best-practices/javascript-and-stylesheet-tags#javascript)<br>- [`{% stylesheet %}`](https://shopify.dev/docs/storefronts/themes/best-practices/javascript-and-stylesheet-tags#stylesheet)<br><br>To learn more, refer to [Section assets](https://shopify.dev/docs/storefronts/themes/best-practices/javascript-and-stylesheet-tags). | No |
| **Schema** | Sections support the `{% schema %}` Liquid tag. This tag is used to define the following section attributes and settings:<br><br>- [name](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#name)<br>- [tag](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#tag)<br>- [class](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#class)<br>- [limit](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#limit)<br>- [settings](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#settings)<br>- [blocks](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#blocks)<br>- [app blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks)<br>- [max_blocks](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#max_blocks)<br>- [presets](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#presets)<br>- [defaults](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#default)<br>- [locales](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#locales)<br>- [enabled_on](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#enabled_on)<br>- [disabled_on](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#disabled_on)<br><br>To learn more, refer to [Section schema](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema). | Yes |

---

#### Usage

When working with sections, you should familiarize yourself with the following:

* How to render a section
* How to integrate sections with the theme editor
* Support app blocks

##### Render a section

You can render sections in one of the following ways:

* Reference the section in a [JSON template](https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates), or a [section group](https://shopify.dev/docs/storefronts/themes/architecture/section-groups) in a [layout](https://shopify.dev/docs/storefronts/themes/architecture/layouts) file.
* [Statically render](#statically-render-a-section) the section with the `section` Liquid tag.
* Use the [Section Rendering API](https://shopify.dev/docs/api/ajax/section-rendering).

> **Tip:** If you want to render sections inside a template, then use a JSON template. "JSON templates provide more extensive customization options for merchants, and improve the theme editor's performance."

###### Statically render a section

> **Caution:** "Whenever possible, you should avoid statically rendering sections. Instead, you should reference them in a JSON template or section group."

You can statically render a section using the Liquid [section tag](https://shopify.dev/docs/api/liquid/tags/section).

For example, to include a section in a [Liquid template](https://shopify.dev/docs/storefronts/themes/architecture/templates/liquid-templates), you can include it with a section tag:

```liquid
{% section 'featured-product' %}
```

> **Note:** "You can include a statically rendered section in multiple theme files. However, only one instance of the section exists. If you change section settings in one location, then the change will be applied to all locations where the section is rendered."

##### Integrate sections with the theme editor

When users customize sections and blocks through the theme editor, their HTML is dynamically added, removed, or re-rendered directly onto the existing DOM, without reloading the entire page. However, any associated JavaScript that runs when the page loads won't run again.

Additionally, you must make sure that when a section or block is selected, that section or block becomes, and remains, visible while it's selected. For example, a slideshow section should scroll into view when the section is selected, slide to a selected block (slide), and pause while that block is selected.

To help identify theme editor actions like section and block selection or reordering, you can use the [JavaScript events](https://shopify.dev/docs/storefronts/themes/best-practices/editor/integrate-sections-and-blocks#javascript-events) emitted by the theme editor.

You might also want to prevent specific code from running in the theme editor. To do so, you can use Liquid and JavaScript variables for [detecting the theme editor](https://shopify.dev/docs/storefronts/themes/best-practices/editor/integrate-sections-and-blocks#detect-the-theme-editor).

> **Tip:** "Section and block files must define presets in their schema to support being added to JSON templates using the theme editor."

##### Support app blocks

App blocks allow app developers to create blocks for merchants to add app content to their theme without having to directly edit theme code.

To learn more about how to make your theme compatible with app blocks, refer to [App blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks).

### 2.4.1 Section schema

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema

#### Section schema

`{% schema %}` tag for sections allows you to define the following section attributes and settings:

* [name](#name)
* [tag](#tag)
* [class](#class)
* [limit](#limit)
* [settings](#settings)
* [blocks](#blocks)
* [max_blocks](#max_blocks)
* [presets](#presets)
* [default](#default)
* [locales](#locales)
* [enabled_on](#enabled_on)
* [disabled_on](#disabled_on)

These attributes and settings enable different customization options and preconfigurations of the section inside the theme editor.

**Note:**

The `{% schema %}` tag is a Liquid tag. However, it doesn't output its contents, or render any Liquid included inside it.

The following is an example of a valid section schema for the `Slideshow` section:

**/sections/slideshow.liquid**

```json
{% schema %}
{
  "name": "Slideshow",
  "tag": "section",
  "class": "slideshow",
  "limit": 1,
  "settings": [
    {
      "type": "text",
      "id": "title",
      "label": "Slideshow"
    }
  ],
  "max_blocks": 5,
  "blocks": [
     {
       "name": "Slide",
       "type": "slide",
       "settings": [
         {
           "type": "image_picker",
           "id": "image",
           "label": "Image"
         }
       ]
     }
  ],
  "presets": [
    {
      "name": "Slideshow",
      "settings": {
        "title": "Slideshow"
      },
      "blocks": [
        {
          "type": "slide"
        },
        {
          "type": "slide"
        }
      ]
    }
  ],
  "locales": {
    "en": {
      "title": "Slideshow"
    },
    "fr": {
      "title": "Diaporama"
    }
  },
  "enabled_on": {
    "templates": ["*"],
    "groups": ["footer"]
  }
}
{% endschema %}
```

Each section can have only a single `{% schema %}` tag, which must contain only valid JSON using the attributes listed below. The tag can be placed anywhere within the section file, but it can't be nested inside another Liquid tag.

**Caution:**

Having more than one `{% schema %}` tag, or placing it inside another Liquid tag, will result in a syntax error when editing your theme code.

Consider making your section compatible with app blocks. When you create app blocks, merchants can add app content to their theme without directly editing their theme code.

---

##### name

The `name` attribute determines the section title that is shown in the theme editor. For example, the following schema returns the following output:

```json
{% schema %}
{
  "name": "Slideshow"
}
{% endschema %}
```

---

##### tag

By default, when Shopify renders a section, it's wrapped in a `<div>` element with a unique `id` attribute:

```html
<div id="shopify-section-[id]" class="shopify-section">
  // Output of the section content
</div>
```

If you don't want to use a `<div>`, then you can specify which kind of HTML element to use with the `tag` attribute. The following are the accepted values:

* `article`
* `aside`
* `div`
* `footer`
* `header`
* `section`

For example, the following schema returns the following output:

**/sections/slideshow.liquid**

```json
{% schema %}
{
  "name": "Slideshow",
  "tag": "section"
}
{% endschema %}
```

**Output**

```html
<section id="shopify-section-[id]" class="shopify-section">
  // Output of the section content
</section>
```

---

##### class

When Shopify renders a section, it's wrapped in an HTML element with a class of `shopify-section`. You can add to that class with the `class` attribute:

**/sections/slideshow.liquid**

```json
{% schema %}
{
  "name": "Slideshow",
  "tag": "section",
  "class": "slideshow"
}
{% endschema %}
```

**Output**

```html
<section id="shopify-section-[id]" class="shopify-section slideshow">
  // Output of the section content
</section>
```

---

##### limit

By default, there's no limit to how many times a section can be added to a template or section group. You can specify a limit of 1 or 2 with the `limit` attribute:

**/sections/slideshow.liquid**

```json
{% schema %}
{
  "name": "Slideshow",
  "tag": "section",
  "class": "slideshow",
  "limit": 1
}
{% endschema %}
```

---

##### settings

You can create section specific settings to allow merchants to customize the section with the `settings` object:

**/sections/slideshow.liquid**

```json
{% schema %}
{
  "name": "Slideshow",
  "tag": "section",
  "class": "slideshow",
  "settings": [
    {
      "type": "text",
      "id": "header",
      "label": "Header"
    }
  ]
}
{% endschema %}
```

**Caution:**

All section setting IDs must be unique within each section. Having duplicate IDs within a section will result in an error.

###### Access section settings

Section settings can be accessed through the `section` object. Refer to the access settings documentation to learn more.

**Tip:**

If a section is statically rendered, then there's only one instance of the section across all static renderings, as a result they all share the same section setting values.

---

##### blocks

You can create blocks for a section. Blocks are reusable modules of content that can be added, removed, and reordered within a section.

Blocks have the following attributes:

| Attribute | Description | Required |
| - | - | - |
| `type` | The block type. This is a free-form string that you can use as an identifier. You can access this value through the `type` attribute of the `block` object. | Yes |
| `name` | The block name, which will show as the block title in the theme editor. | Yes |
| `limit` | The number of blocks of this type that can be used. | No |
| `settings` | Any input or sidebar settings that you want for the block. Certain settings might be used as the title of the block in the theme editor. | No |

The following is an example of including blocks in a section:

**/sections/slideshow.liquid**

```json
{% schema %}
{
  "name": "Slideshow",
  "tag": "section",
  "class": "slideshow",
  "settings": [
    {
      "type": "text",
      "id": "title",
      "label": "Slideshow"
    }
  ],
  "blocks": [
     {
       "name": "Slide",
       "type": "slide",
       "settings": [
         {
           "type": "image_picker",
           "id": "image",
           "label": "Image"
         }
       ]
     }
   ]
}
{% endschema %}
```

**Caution:**

All block names and types must be unique within each section, and all setting IDs must be unique within each block. Having duplicates will result in an error.

###### Access block settings

Block settings can be accessed through the `block` object. Refer to the access settings documentation to learn more.

**Tip:**

If a section is statically rendered, then there's only one instance of the section across all static renderings, meaning they all share the same block setting values.

###### Render blocks

You can render a section's blocks by looping over the `blocks` attribute of the `section` object:

```liquid
{% for block in section.blocks %}
  {% case block.type %}
    {% when 'slide' %}
      <div class="slide" {{ block.shopify_attributes }}>
        {{ block.settings.image | image_url: width: 2048 | image_tag }}
      </div>
    ...
  {% endcase %}
{% endfor %}
```

In the example above, each block's content is included inside a parent container, and that container has `{{ block.shopify_attributes }}` added as an attribute. Shopify's theme editor uses that attribute to identify blocks in its JavaScript API.

If your block is a single element, then ensure that the element has this attribute.

**Caution:**

Don't rely on the literal value of a block's ID when you iterate over blocks. The ID is dynamically generated and is subject to change. The following is an example of relying on a literal value of a block's ID, which may break functionality in your theme if the ID changes:

```liquid
{% for block in section.blocks %}
{%- if block.id == 'J6d9jV' -%}
<h1>{{ block.settings.heading }}</h1>
{% endif %}
{% endfor %}
```

###### Recommended blocks

You can highlight specific theme blocks in the block picker to make them easier to find. To do this, include the `@theme` block type along with your recommended blocks in the `blocks` array.

In this example, the `text`, `button`, and `_marquee` blocks appear immediately in the picker. Other available theme blocks remain accessible by selecting **Show all**.

```json
"blocks": [
  { "type": "@theme" },
  { "type": "button" },
  { "type": "text" },
  { "type": "_marquee" }
]
```

###### Show dynamic block titles in the theme editor

In certain cases, the theme editor can display an input setting value as the title of a block in the theme editor sidebar. This can help merchants to identify and rearrange blocks in a section.

The theme editor checks the `id` values of the settings in a block to determine the best one to use for the block title.

The theme editor uses settings with the following `id` values, in order of precedence:

1. `heading`
2. `title`
3. `text`

If a setting with a matching `id` value doesn't exist, then the block name is used as the title.

For example, this block with a setting `id` of `heading` displays in the sidebar with the title `Welcome to our store`.

**File**

```json
"blocks": [
  {
    "name": "Announcement",
    "type": "announcement",
    "settings": [
      {
        "type": "text",
        "id": "heading",
        "default": "Welcome to our store",
        "label": "Heading"
      }
    ]
  }
]
```

---

##### max_blocks

There's a limit of 50 blocks per section. You can specify a lower limit with the `max_blocks` attribute.

**Note:**

Static blocks don't count toward this limit.

**/sections/slideshow.liquid**

```json
{% schema %}
{
  "name": "Slideshow",
  "tag": "section",
  "class": "slideshow",
  "max_blocks": 5,
  "settings": [
    {
      "type": "text",
      "id": "title",
      "label": "Slideshow"
    }
  ],
  "blocks": [
     {
       "name": "Slide",
       "type": "slide",
       "settings": [
         {
           "type": "image_picker",
           "id": "image",
           "label": "Image"
         }
       ]
     }
   ]
}
{% endschema %}
```

---

##### presets

Presets are predefined section configurations that merchants can select when adding sections to a JSON template. Presets help you quickly provide merchants with different layouts and use cases by adjusting section settings. For example, a "Testimonials" section might include presets for a single testimonial, a carousel, and a grid layout.

**Note:**

Section presets are different from the presets used to define theme presets in the `settings_data.json` file.

Presets appear in the **Add section** picker as follows:

| Number | Description |
| - | - |
| 1 | Presets appear alphabetically based on their `name` attribute. |
| 2 | Presets can optionally be grouped into collapsible categories using the `category` attribute. |
| 3 | Uncategorized presets are always displayed first. |
| 4 | The theme editor automatically generates a preset preview. You can further customize this preview using visual preview mode. |

Section presets have the following attributes:

| Attribute | Description | Required |
| - | - | - |
| `name` | The preset name displayed in the theme editor's **Add section** picker and sidebar, and is persisted in the JSON template when you add a section. | Yes |
| `category` | Groups related presets together in the theme editor's **Add section** picker. | No |
| `settings` | Default values for settings you want to pre-populate. Each entry includes the setting name and its value. | No |
| `blocks` | Default blocks included in the preset. Each block entry must include a `type` attribute matching the block type, and a `settings` object formatted similarly to the `settings` attribute above. Optionally, include a `name` attribute to display when merchants add the block in the editor. | No |

Here's an example of how presets are defined within a section schema:

**/sections/slideshow.liquid**

```json
{% schema %}
{
  "name": "Slideshow",
  "tag": "section",
  "class": "slideshow",
  "max_blocks": 5,
  "settings": [
    {
      "type": "text",
      "id": "title",
      "label": "Slideshow"
    }
  ],
  "blocks": [
     {
       "name": "Slide",
       "type": "slide",
       "settings": [
         {
           "type": "image_picker",
           "id": "image",
           "label": "Image"
         }
       ]
     }
   ],
  "presets": [
    {
      "name": "Slideshow",
      "category": "Banners",
      "settings": {
        "title": "Slideshow"
      },
      "blocks": [
        {
          "type": "slide"
        },
        {
          "type": "slide"
        }
      ]
    }
  ]
}
{% endschema %}
```

**Tip:**

Sections with presets shouldn't be statically rendered. If you're going to statically render a section, then you should use default settings.

---

##### default

If you statically render a section, then you can define a default configuration with the `default` object, which has the same attributes as the preset object.

The following is an example of including a default in a section:

**/sections/slideshow.liquid**

```json
{% schema %}
{
  "name": "Slideshow",
  "tag": "section",
  "class": "slideshow",
  "max_blocks": 5,
  "settings": [
    {
      "type": "text",
      "id": "title",
      "label": "Slideshow"
    }
  ],
  "blocks": [
     {
       "name": "Slide",
       "type": "slide",
       "settings": [
         {
           "type": "image_picker",
           "id": "image",
           "label": "Image"
         }
       ]
     }
   ],
  "default": {
    "settings": {
      "title": "Slideshow"
    },
    "blocks": [
      {
        "type": "slide"
      },
      {
        "type": "slide"
      }
    ]
  }
}
{% endschema %}
```

**Tip:**

You should only use the section `default` attribute for sections that will be reused, or installed on multiple themes or shops. Statically rendered sections that come pre-installed on a theme should have their default configuration defined by the `default` attribute for each individual setting.

---

##### locales

Sections can provide their own set of translated strings through the `locales` object. This is separate from the `locales` directory of the theme, which makes it a useful feature for sections that are meant to be installed on multiple themes or shops.

The `locales` object has the following general format:

**General format**

```json
{
  "locales": {
    "language": {
      "translation_key": "translation_value"
    }
  }
}
```

For example:

**/sections/slideshow.liquid**

```json
{% schema %}
{
  "name": "Slideshow",
  "tag": "section",
  "class": "slideshow",
  "max_blocks": 5,
  "settings": [
    {
      "type": "text",
      "id": "title",
      "label": "Slideshow"
    }
  ],
  "blocks": [
     {
       "name": "Slide",
       "type": "slide",
       "settings": [
         {
           "type": "image_picker",
           "id": "image",
           "label": "Image"
         }
       ]
     }
   ],
   "default": {
    "settings": {
      "title": "Slideshow"
    },
    "blocks": [
      {
        "type": "slide"
      },
      {
        "type": "slide"
      }
    ]
  },
  "locales": {
    "en": {
      "title": "Slideshow"
    },
    "fr": {
      "title": "Diaporama"
    }
  }
}
{% endschema %}
```

Any translations will show up under the **Sections** tab of the language editor for merchants to edit. When edits are made, the changes are saved directly to the applicable locale file, and the section schema is unchanged.

These translations can be accessed through the Liquid translation filter (`t` filter) where the key will be in the following format:

```text
sections.[section-name].[translation-description]
```

For example, if you want to reference the `title` translation from the example above, then use the following:

```liquid
{{ 'sections.slideshow.title' | t }}
```

---

##### enabled_on

You can restrict a section to certain template page types and section group types by specifying them through the `enabled_on` attribute.

`enabled_on`, along with `disabled_on`, replaces the `templates` attribute.

**Caution:**

You can use only one of `enabled_on` or `disabled_on`.

`enabled_on` must have at least one of the following attributes:

| Attribute | Description |
| - | - |
| `templates` | A list of the template page types where the section can be used. Accepted values: A list of page types or `["*"]` (all template page types) |
| `groups` | A list of the section groups where the section can be used. Accepted values: A list of the section group types. Accepted values: `header`, `footer`, `aside`, and custom types in the format `custom.<NAME>`, or `["*"]` (all section group types) |

In the following example, the section is available to all templates, and to the `footer` section group:

**/sections/slideshow.liquid**

```json
{% schema %}
{
  "name": "Slideshow",
  "tag": "section",
  "class": "slideshow",
  "max_blocks": 5,
  "settings": [
    {
      "type": "text",
      "id": "title",
      "label": "Slideshow"
    }
  ],
  "blocks": [
     {
       "name": "Slide",
       "type": "slide",
       "settings": [
         {
           "type": "image_picker",
           "id": "image",
           "label": "Image"
         }
       ]
     }
   ],
   "default": {
    "settings": {
      "title": "Slideshow"
    },
    "blocks": [
      {
        "type": "slide"
      },
      {
        "type": "slide"
      }
    ]
  },
  "locales": {
      "en": {
        "title": "Slideshow"
      },
      "fr": {
        "title": "Diaporama"
      }
  },
  "enabled_on": {
    "templates": ["*"],
    "groups": ["footer"]
  }
}
{% endschema %}
```

---

##### disabled_on

You can prevent a section from being used on certain template page types and section group types by setting them in the `disabled_on` attribute. When you use `disabled_on`, the section is available to all templates and section groups except the ones that you specified.

`disabled_on`, along with `enabled_on`, replaces the `templates` attribute.

**Caution:**

You can use only one of `enabled_on` or `disabled_on`.

`disabled_on` must have at least one of the following attributes:

| Attribute | Description |
| - | - |
| `templates` | A list of the template page types where the section can't be used. Accepted values: A list of page types or `["*"]` (all template page types) |
| `groups` | A list of the section groups where the section can't be used. Accepted values: A list of the section group types. Accepted values: `header`, `footer`, `aside`, and custom types in the format `custom.<NAME>`, or `["*"]` (all section group types) |

In the following example, the section is available to all templates other than `password` templates, and to all section groups other than `footer` section groups.

**/sections/slideshow.liquid**

```json
{% schema %}
{
  "name": "Slideshow",
  "tag": "section",
  "class": "slideshow",
  "max_blocks": 5,
  "settings": [
    {
      "type": "text",
      "id": "title",
      "label": "Slideshow"
    }
  ],
  "blocks": [
     {
       "name": "Slide",
       "type": "slide",
       "settings": [
         {
           "type": "image_picker",
           "id": "image",
           "label": "Image"
         }
       ]
     }
   ],
   "default": {
    "settings": {
      "title": "Slideshow"
    },
    "blocks": [
      {
        "type": "slide"
      },
      {
        "type": "slide"
      }
    ]
  },
  "locales": {
      "en": {
        "title": "Slideshow"
      },
      "fr": {
        "title": "Diaporama"
      }
  },
  "disabled_on": {
    "templates": ["password"],
    "groups": ["footer"]
  }
}
{% endschema %}
```

---

## 2.5 Section groups

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/section-groups

### Section groups

A section group is a JSON data file that stores a list of [sections](https://shopify.dev/docs/storefronts/themes/architecture/sections) and [app blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks) to be rendered, and their associated settings. Merchants can add sections to the section group, as well as remove and reorder them, in the theme editor.

You can [add a reference to a section group](#include-a-section-group-in-a-layout-file) in a [layout](https://shopify.dev/docs/storefronts/themes/architecture/layouts) file to add support for sections in areas that are controlled by the layout, such as the header or footer.

The sections and app blocks referenced in a section group are rendered in the order specified by the `order` attribute, with no markup between the sections.

Section groups can render up to 25 sections, and each section can have up to 50 blocks.

The sections and app blocks referenced in section groups are the same sections and app blocks referenced in templates, and should follow the same [guidelines](https://shopify.dev/docs/storefronts/themes/best-practices/templates-sections-blocks).

You can use section groups in place of [static sections](https://shopify.dev/docs/storefronts/themes/architecture/sections#statically-render-a-section) in layouts. [Learn how to migrate from static sections to section groups](https://shopify.dev/docs/storefronts/themes/architecture/section-groups/migrate).

> **Tip:** In most themes, you should use section groups for only the header and footer. If you create additional section groups for other areas of the theme, such as a navigation sidebar, then name the section group to reflect its intended purpose.

---

#### Location

Section group files are located in the `sections` directory of the theme:

```text
└─ theme
  ...
  ├─ layout
  │  └─ theme.liquid
  ├─ sections
  │  ├─ footer-group.json
  │  ├─ header.liquid
  │  ├─ header-group.json
  │  └─ ...
  ...
```

---

#### Schema

Section groups must be valid JSON files. The root should be an object with the following attributes:

| Attribute | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | String | Yes | The type of the section group. Accepted values: `header`, `footer`, `aside`, or a custom type in the format `custom.<name>`, where `<name>` is a unique identifier for your section group type. |
| `name` | String | Yes | A name for the section group. Maximum length: 50 characters |
| `sections` | Object | Yes | An object that uses section IDs as keys, and section data as values. You can leave this attribute empty. Duplicate IDs within the template aren't allowed. The format of the section data is the same as the section data in [settings_data.json](https://shopify.dev/docs/storefronts/themes/architecture/config/settings-data-json). JSON templates can render up to 25 sections, and each section can have up to 50 blocks. |
| `order` | Array | Yes | An array of section IDs, listed in the order that they should be rendered. The IDs must exist in the `sections` object. You can leave this attribute empty. Duplicate IDs aren't allowed. |

#### Example

```json
{
 "type": "header",
 "name": "Header Group",
 "sections": {
   "header": {
     "type": "header",
     "settings": {}
   }
 },
 "order": ["header"]
}
```

##### Section data

The `sections` attribute of section groups holds the data for the sections to be rendered by the section group. These can be either [theme sections](https://shopify.dev/docs/storefronts/themes/architecture/sections) or [app sections](https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks#app-block-wrapper). You can't share section data across section groups, so each section must have an ID that's unique within the section group.

Section groups can render up to 25 sections, and each section can have up to 50 blocks.

You can add sections to a group in code, or through the theme editor.

The following table outlines the format of section data:

| Value | Type | Required | Description |
| --- | --- | --- | --- |
| `<SectionID>` | String | — | A unique ID for the section. Accepts only alphanumeric characters. |
| `<SectionType>` | String | Yes | The filename of the section file to render, without the extension. |
| `<SectionDisabled>` | Boolean | No | When `true`, the section isn't rendered but can still be customized in the theme editor. Is `false` by default. |
| `<BlockID>` | String | — | A unique ID for the block. Accepts only alphanumeric characters. |
| `<BlockType>` | String | Yes | The type of block to render, as defined in the schema of the section file. |
| `<BlockOrder>` | Array | No | An array of block IDs, ordered as they should be rendered. The IDs must exist in the `blocks` object, and duplicate IDs aren't allowed. |
| `<SettingID>` | String | — | The ID of a setting as defined in the schema of the section or the block. |
| `<SettingValue>` | (multiple) | — | A valid value for the setting. |

For example:

```json
sections: {
<SectionID>: {
  "type": <SectionType>,
  "disabled": <SectionDisabled>,
  "settings": {
    <SettingID>: <SettingValue>
  },
  "blocks": {
    <BlockID>: {
      "type": <BlockType>,
      "settings": {
        <SettingID>: <SettingValue>
      }
    }
  },
  "block_order": <BlockOrder>
}
}
```

For example, the following section group renders the `quick-links` and `newsletter-signup` section files:

**sections/footer-group.json**

```json
{
 "type": "footer",
 "name": "Footer group",
 "sections": {
   "quick-links": {
     "type": "quick-links",
     "settings": {}
   },
   "newsletter-signup": {
     "type": "newsletter-signup",
     "settings": {}
   }
 },
 "order": [
    "newsletter-signup",
    "quick-links"
 ]
}
```

> **Caution:** Any sections that are included in a section group, and aren't app sections, must exist in the theme. If a section doesn't exist and is referenced in a section group, then it results in an error.

---

#### Usage

When working with section groups, you should familiarize yourself with the process of including a section group in a layout, and considerations for using both section groups and static sections in a layout.

You can also optionally use section groups to render your template content.

##### Contextual section groups

When a merchant [adapts a section group for a specific buyer context](https://help.shopify.com//en/manual/online-store/themes/customizing-themes/store-contextualization), a new contextual section group file is created. The file takes the name of the context in the following format: `header-group.context.<context-string>.json`.

A contextual section group file includes the overrides that you make to the section group for a context. The context and parent file are defined at the top of the template. The `context` value can contain either `"market": "market-handle"` or `"b2b": true`. For example, the following code contextualizes the `announcement-bar` section for market handle `ca`:

**header-group.context.ca**

```json
{
  "context": {
    "market": "ca"
  },
  "parent": "header-group.json",
  "sections": {
    "announcement-bar": {
      "blocks": {
        "announcement-bar-one": {
          "settings": {
            "text": "Free shipping for Canada!"
          }
        }
      },
      "settings": {
        "change_slides_speed": 5
      }
    }
  }
}
```

##### Include a section group in a layout file

Use the [`sections`](https://shopify.dev/docs/api/liquid/tags/sections) Liquid tag to render section groups as part of the theme's layout content. Place the `sections` tag where you want to render it in the layout.

The `sections` Liquid tag uses the following syntax, where `filename` is the name of the section group without its file extension:

**Syntax**

```liquid
{% sections 'filename' %}
```

For example, if you have a `/sections/header-group.json` file that contains your theme's header content, such as header section and announcement bar section, then you might want to include that section group in `theme.liquid` so that the header section group is rendered on all pages that use that layout:

**layout/theme.liquid**

```liquid
{% sections 'header-group' %}
```

##### Static section and section group coexistence

Avoid using both section groups and static sections in the same layout file. If you need to use both, then you should identify which sections are static in the section name.

### 2.5.1 Migrate static sections to section groups

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/section-groups/migrate

#### Migrate static sections to section groups

Section groups give merchants the flexibility to add, remove, and reorder sections in their theme's layout without making changes to the theme code.

If you created your theme before section groups became available, then you might render one or more sections statically in your layout file. Because section groups are more flexible and reduce the need for code changes, you should replace the statically rendered sections in your layout files with section groups that contain the sections by default.

When you migrate static sections to section groups, Shopify attempts to [migrate any applicable settings](#settings-migration-for-theme-updates) for the merchant during the theme update process.

---

##### Step 1: Create new section groups

Create a section group for each of the areas of your layout where you include static sections. In most cases, you need to create a header section group and a footer section group.

1. In the `sections` directory, create a new JSON file for the section group.

   The file name should identify the area of the layout that the section group represents. For example, you might create a file called `header-group.json` for your header section group.

2. In the file, add data for the basic section group schema, including the section group type and name.

   **sections/header-group.json**

   ```json
   {
     "type": "header",
     "name": "Header group",
     "sections": {
     },
     "order": [
     ]
   }
   ```

3. Add references to the sections that you want to include in the section group. You should include all of the static sections that the section group is replacing, so Shopify can [copy a merchant's static section settings to the section group](#settings-migration-for-theme-updates).

   For example, the header area of your layout file might contain the following sections:

   **layout/theme.liquid**

   ```liquid
   {% section 'announcement-bar' %}
   {% section 'header' %}
   ```

   You can add references to those sections in your new section group:

   **sections/header-group.json**

   ```json
   {
     "type": "header",
     "name": "Header Group",
     "sections": {
       "header": {
         "type": "header",
         "settings": {
         }
       },
       "announcement-bar": {
         "type": "announcement-bar",
         "settings": {
         }
       }
     },
     "order": [
       "announcement-bar",
       "header"
     ]
   }
   ```

---

##### Step 2: Replace static section tags with section group tags

After you create your section group JSON file, replace the static sections in your layout file with your new section group:

**layout/theme.liquid**

**Code to remove**

```liquid
{% section 'announcement-bar' %}
{% section 'header' %}
```

**Code to add**

```liquid
{% sections 'header-group' %}
```

---

##### Settings migration for theme updates

When a merchant updates their theme from a version that uses a static section to a version that includes that section in a section group, Shopify attempts to copy the static section's settings to the settings for the equivalent section in the section group. Shopify maps these settings based on the section's `type`.

For example, if a theme uses a section group that has a section of type `header`, Shopify copies any settings for a section of type `header` from the old version's `/config/settings_data.json` file.

**Old version**

```json
{
  "current": {
    "colors_solid_button_labels": "#ffffff",
    "colors_accent_1": "#121212",
    "sections": {
      "header": {
        "type": "header",
        "settings": {
          "color_scheme": "background-1",
          "logo_width": 90,
          "logo_position": "middle-left",
          "menu": "main-menu",
          "show_line_separator": true,
          "enable_sticky_header": true,
          "margin_bottom": 0
        }
      }
    }
  },
  "presets": {}
}
```

**New version**

```json
{
  "type": "header",
  "name": "Header Group",
  "sections": {
    "header": {
      "type": "header",
      "settings": {
        "color_scheme": "background-1",
        "logo_width": 90,
        "logo_position": "middle-left",
        "menu": "main-menu",
        "show_line_separator": true,
        "enable_sticky_header": true,
        "margin_bottom": 0
      }
    }
  },
  "order": [
    "header"
  ]
}
```

---

## 2.6 Blocks

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/blocks

### Blocks

Blocks enable developers to create flexible layouts by breaking down sections into smaller, reusable pieces of Liquid. Each block has its own set of settings, and can be added, removed, and reordered within a section.

There are three types of blocks:

* **Theme blocks**: Created as their own Liquid files in the `/blocks` folder, and re-usable across multiple sections with the theme.
* **Section blocks**: Created within a section's Liquid file and are limited to use within that section.
* **App blocks**: Provided by apps installed on a merchant's shop.

#### Theme blocks

Theme blocks provide the most flexibility when building sections. As a developer you can:

* Let merchants add any available block
* Restrict sections to specific block types
* Enable blocks to nest inside other blocks
* Create "static blocks" that stay in a specific part of the code, within their parent block or section. Static blocks can be hidden by merchants, but not deleted.

For example, imagine building a slideshow section. You might:

* Limit it to only accept slide blocks
* Let each Slide block contain any other block type available within the theme, or provided by an app
* Add a static "Slideshow Controls" block that stays locked in place

This gives merchants the freedom to customize slide content while keeping navigation controls consistent.

#### Section blocks

Section blocks have a number of limitations:

* They only work in the section they're defined within and can't be used elsewhere.
* They only support a single level of hierarchy, and cannot be nested.
* They cannot currently be used in the same section as Theme blocks.

Section blocks are defined directly within a section's Liquid file, and configured within the section's `{% schema %}` tag.

#### App blocks

App blocks allow merchants to add app-specific functionality to your theme, such as reviews, ratings, or custom forms; they are defined by the Shopify apps that a merchant installs on their shop. App blocks can be added to any section (or Theme Block) within a theme that has added support in its schema file. For example, in a Slideshow example, you may have `/blocks/slide.liquid`. To add support for App Blocks, you would write:

```js
{% schema %}
{
"name": "Slide",
"blocks": [{ "type": "@theme" }, { "type": "@app" }],

// Rest of your Schema code
```

#### Theme blocks vs Snippets

Theme blocks and snippets both help you reuse code, but serve different purposes.

Theme blocks:

* Show settings in the theme editor
* Let merchants customize each instance
* Access their parent section and global objects
* Cannot receive variables from parent code

Snippets:

* Handle repeatable markup without merchant customization
* Accept variables from their parent code
* Don't show in the theme editor

Often you'll use both together. For example, a product card might use:

* Theme blocks for the overall structure and settings
* Snippets for individual pieces of markup and templating logic that are re-used across many other blocks

#### AI generated theme blocks

Shopify themes can be extended with custom blocks generated using Shopify Magic, directly within the theme editor (for eligible merchants). This feature allows users to describe a desired block in plain text, and Shopify Magic generates the corresponding Liquid code, including the necessary HTML structure, potential CSS/JavaScript, and the JSON schema definition.

From a developer perspective, these AI-generated blocks are theme blocks.

* They are stored in the `/blocks` folder alongside other theme blocks.
* They can be added to any section (or theme block) within a theme that supports theme blocks.

### 2.6.1 Theme blocks (Quick Start)

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks

#### Quick Start

Learn how to build a basic theme block and add it to a section and another block file.

Theme blocks are blocks that are defined at the theme level. You can reuse theme blocks across different sections of the theme, unlike section-defined blocks that can only be used within the section where they're defined. Additionally, theme blocks can be nested within other theme blocks to create hierarchy.

##### Requirements

- [Understand Blocks at Shopify](https://shopify.dev/docs/storefronts/themes/architecture/blocks)
- [Create a Theme](https://shopify.dev/docs/storefronts/themes/getting-started/create)

##### Create a theme block

At the end of this tutorial, you should have a text block that can be reused across different sections and blocks of the theme. You will add it to a Custom Section and a Group block.

###### Add a blocks folder

Theme blocks are Liquid files that are defined in the `blocks` directory of the theme. To create a theme block, add a Liquid file in the `/blocks` folder of your theme.

If your theme doesn't have a `/blocks` folder yet, then add one at the root of your theme. Add a `text.liquid` file to the `/blocks` folder.

###### Write the markup

Theme block files contain markup.

The markup is any HTML or Liquid content that you want to include in the block.

**/blocks/text.liquid**

```liquid
<div class="text-block text-{{ block.settings.alignment }}">
  {{ block.settings.text }}
</div>


{% stylesheet %}
  .text-left {
    text-align: left;
  }


  .text-center {
    text-align: center;
  }


  .text-right {
    text-align: right;
  }
{% endstylesheet %}


{% schema %}
{
  "name": "Text",
  "settings": [
    {
      "type": "richtext",
      "id": "text",
      "label": "Text"
    },
    {
      "type": "text_alignment",
      "id": "alignment",
      "label": "Alignment"
    },
  ],
  "presets": [
    { "name": "Text" },
    {
      "name": "Content",
      "settings": {
        "text": "<p>Hello, world!</p>"
      }
    }
  ]
}
{% endschema %}
```

###### Write the schema

Theme block files contain a schema.

The schema is the `{% schema %}` Liquid tag, which is used to configure settings and attributes of the block. [Learn how to write block schema](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/schema).

**Tip:** At this step, you'll be able to reference the theme block in a section file with block targeting. To make this block display in the theme editor's block picker, you need to add a block preset.

##### Use Liquid objects in blocks

Blocks use a few key liquid objects:

* Theme blocks reference a `block` object, which contains the properties and setting values of the block.
* Theme blocks can reference the `section` object of the section that rendered the theme block.
* Theme blocks have access to global objects.

In this Text block example, this block references the settings attribute of the block object.

Theme blocks cannot access variables created outside the block and cannot be passed variables like when using a snippet.

###### Add a block preset

Presets need to be defined in order for the theme block to be available for merchants in the theme editor block picker. You can author multiple presets for the same theme block.

In this example, the text theme blocks has two presets called Text and Content.

**Block presets**

```json
"presets": [
  { "name": "Text" },
  {
    "name": "Content",
    "settings": {
      "text": "Hello, World!"
    }
  }
]
```

##### Use theme blocks in sections

After theme blocks are defined in your theme, you need to update the theme's sections to render blocks.

**Tip:** Sections can either define blocks locally or opt-in to supporting theme blocks, but they can't support both simultaneously.

###### Render the blocks in Liquid

Render the blocks in Liquid using:

```liquid
{% content_for 'blocks' %}
```

**/sections/custom-section.liquid**

```liquid
<div class="custom-section color-{{ section.settings.color_scheme }}">
  {% content_for 'blocks' %}
</div>


{% schema %}
{
  "name": "Custom section",
  "blocks": [{ "type": "@theme" }, { "type": "@app" }],
  "settings": [
    {
      "type": "header",
      "content": "Color"
    },
    {
      "type": "color_scheme",
      "id": "color_scheme",
      "label": "Color scheme",
      "default": "scheme-1"
    }
  ],
  "presets": [
    {
      "name": "Custom section"
    },
    {
      "name": "Heading and text",
      "blocks": [
        {
          "type": "group",
          "settings": {
            "color_scheme": "scheme-3"
          },
          "blocks": [
            {
              "type": "text",
              "settings": {
                "text": "<h1>Image with text</h1>"
              }
            },
            {
              "type": "text",
              "settings": {
                "text": "<p>Pair text with an image to focus on your chosen product, collection, or blog post.</p>"
              }
            }
          ]
        }
      ]
    }
  ]
}
{% endschema %}
```

###### Update the section schema

To accept all theme blocks in a section, add the type `@theme` to the blocks attribute of the schema of that section. To be more restrictive about which blocks can be use in specific sections, use block targeting.

**blocks attribute**

```json
"blocks": [{ "type": "@theme" }, { "type": "@app" }],
```

##### Nest blocks in theme blocks

Theme blocks can accept other theme and app blocks as children.

Theme blocks use the `blocks` attribute of their schema and assemble different configurations of these child blocks using the `presets` attribute.

In this example, the Group block has a preset called Column which is nesting the Text block using the `presets` attribute.

**Group block's Column preset nests Text blocks**

```json
{
  "name": "Column",
  "settings": {
    "color_scheme": "scheme-3"
  },
  "blocks": [
    {
      "type": "text",
      "settings": {
        "text": "<h3>Hello, world!</h3>"
      }
    },
    {
      "type": "text",
      "settings": {
        "text": "<p>How's it going?<\/p>"
      }
    }
  ]
}
```

**/blocks/group.liquid**

```liquid
<div
  class="group-block color-{{ block.settings.color_scheme }}"
>
  {% content_for 'blocks' %}
</div>


{% schema %}
{
  "name": "Group",
  "blocks": [{ "type": "@theme" }, { "type": "@app" }],
  "settings": [
    {
      "type": "header",
      "content": "Color"
    },
    {
      "type": "color_scheme",
      "id": "color_scheme",
      "label": "Color scheme",
      "default": "scheme-1"
    }
  ],
  "presets": [
    {
      "name": "Group"
    },
    {
      "name": "Column",
      "settings": {
        "color_scheme": "scheme-3"
      },
      "blocks": [
        {
          "type": "text",
          "settings": {
            "text": "<h3>Hello, world!</h3>"
          }
        },
        {
          "type": "text",
          "settings": {
            "text": "<p>How's it going?<\/p>"
          }
        }
      ]
    }
  ]
}
{% endschema %}
```

Each block's content is rendered by the liquid tag:

```liquid
{% content_for 'blocks' %}
```

The content is rendered in the order that's stored in the JSON template. This is the same rendering mechanism sections use for blocks.

**Tip:** Block presets can refer to other theme blocks within the theme. This example refers to the `/blocks/text.liquid` Liquid file created earlier in this tutorial.

##### Next Steps

The examples above demonstrate basic theme blocks usage. Theme blocks support several more advanced features to enhance the merchant experience as well as provide flexibility to theme developers.

* [Theme block schema](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/schema) — Learn how to configure theme block settings and attributes through their schema.
* [Theme block availability with targeting](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/targeting) — Learn how to use targeting in order to restrict which theme blocks can be added by merchants to sections and blocks that accept nested blocks.
* [Layout control with static blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/static-blocks) — Learn how to have stricter control over the layout of theme blocks and sections using static blocks.
* [Dynamic sources](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/dynamic-sources) — Learn how to enable more flexibility for merchants by connecting theme blocks to dynamic sources.

### 2.6.2 Block schema

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/schema

#### Block schema

Theme blocks support the `{% schema %}` Liquid tag. This tag is used to define the following block attributes and settings:

* [`name`](#name)
* [`settings`](#settings)
* [`blocks`](#blocks)
* [`presets`](#presets)
* [`tag`](#tag)
* [`class`](#class)

These attributes and settings enable different customization options and preconfigurations of the block inside the theme editor.

The following is an example of a block schema that opts-in to supporting nested blocks with its `block` attribute, defines some background-related `settings`, and assembles different variations of those settings with its `presets` attribute:

**/blocks/slide.liquid**

```json
{% schema %}
{
  "name": "Slide",
  "blocks": [{"type": "@app"}, {"type": "@theme"}],
  "settings": [
    {
      "type": "image_picker",
      "id": "image",
      "label": "Background image"
    },
    {
      "type": "color_background",
      "id": "background",
      "label": "Background color"
    }
  ],
  "presets": [
    {
      "name": "Slide",
      "settings": {
        "background": "#000000"
      },
      "blocks": [
        {
          "type": "text",
          "settings": {
            "text": "This is a slide!"
          }
        }
      ]
    }
  ]
}
{% endschema %}
```

Each block can have only a single `{% schema %}` tag, which must contain only valid JSON and can only use the attributes listed below. The schema tag can be placed anywhere within the block file, but it can't be nested inside another Liquid tag. It doesn't output its contents, or render any Liquid included inside it.

**Caution:**

Having more than one `{% schema %}` tag, or placing it inside another Liquid tag, will result in an error.

---

##### name

The `name` attribute determines the block title that's shown in the theme editor. For example, the following schema returns the following output:

```json
{% schema %}
{
  "name": "Slide"
}
{% endschema %}
```

###### Showing dynamic block titles in the theme editor

In specific cases, the theme editor can display an input setting value as the title of a block in the theme editor sidebar. This can help merchants to identify and rearrange blocks in a section.

The theme editor checks the `id` values of the settings in a block to determine the best one to use for the block title.

The theme editor uses settings with the following `id` values, in the following order of precedence:

1. `heading`
2. `title`
3. `text`

If a setting with a matching `id` value doesn't exist, then the block name is used as the title.

For example, the following block with a setting `id` of `text` displays in the sidebar with the title `Welcome to our store`.

**File**

```json
{
  "name": "Text",
  "settings": [
    {
      "type": "text",
      "id": "text",
      "default": "Welcome to our store",
      "label": "Content"
    }
  ]
}
```

---

##### settings

You can create block-specific settings to enable merchants to customize the block with the `settings` object:

**/blocks/slide.liquid**

```json
{% schema %}
{
  "name": "Slide",
  "settings": [
    {
      "type": "image_picker",
      "id": "image",
      "label": "Background image"
    },
    {
      "type": "color_background",
      "id": "background",
      "label": "Background color"
    }
  ]
}
{% endschema %}
```

**Caution:**

All block setting IDs must be unique within each block. Having duplicate IDs within a block throws an error.

###### Accessing block settings

Block settings can be accessed through the `block` object. Refer to the appropriate documentation to learn more about accessing settings.

---

##### blocks

Theme blocks can accept other app and theme blocks as children using the `blocks` attribute of their schema:

```json
{% schema %}
{
  "name": "Slide",
  "blocks": [{"type": "@app"}, {"type": "@theme"}]
}
{% endschema %}
```

The `"@app"` type denotes that this block accepts app blocks. App blocks enable app developers to create blocks for merchants to add app content to their theme without having to directly edit theme code.

The `"@theme"` type denotes that this block is compatible with other theme-defined blocks that live in the `/blocks` folder of the theme.

Theme blocks can also be made individually accessible by explicitly referencing them.

```json
{% schema %}
{
  "name": "Slideshow",
  "blocks": [{"type": "@app"}, {"type": "slide"}]
}
{% endschema %}
```

Unlike sections, which can define blocks locally using the blocks attribute of their schema, theme blocks can't define local blocks in the `blocks` attribute of their schema.

**Tip:**

You can feature the most relevant theme blocks in the block picker for quicker access.

###### Rendering nested blocks

You can render a block's child blocks by using the `{% content_for 'blocks' %}` Liquid tag:

```liquid
<div class="slide">
  {% content_for 'blocks' %}
</div>
```

In the example above, each block's content is outputted by the `{% content_for 'blocks' %}` tag in the order stored in the JSON template.

**Tip:**

Theme blocks can be nested up to 8 levels deep, excluding the section level.

###### Recommended blocks

You can highlight specific theme blocks in the block picker to make them easier to find. To do this, include the `@theme` block type along with your recommended blocks in the `blocks` array.

In this example, the `text`, `button`, and `_marquee` blocks appear immediately in the picker. Other available theme blocks remain accessible by selecting **Show all**.

```json
"blocks": [
  { "type": "@theme" },
  { "type": "button" },
  { "type": "text" },
  { "type": "_marquee" }
]
```

---

##### presets

Presets are predefined block configurations that merchants can select when adding blocks to a JSON template. Presets help you quickly provide merchants with different layouts and use cases by adjusting block settings. Additionally, presets of a block may reference other child blocks and assemble them in any number of configurations.

Presets appear in the **Add block** picker as follows:

| Number | Description |
| - | - |
| 1 | Presets appear alphabetically based on their `name` attribute. |
| 2 | Presets can optionally be grouped into collapsible categories using the `category` attribute. |
| 3 | Uncategorized presets are always displayed first. |
| 4 | The theme editor automatically generates a preset preview. You can further customize this preview using visual preview mode. |

Block presets have the following attributes:

| Attribute | Description | Required |
| - | - | - |
| `name` | The preset name displayed in the theme editor's **Add block** picker and sidebar, and is persisted in the JSON template when you add a block. | Yes |
| `category` | Groups related presets together in the theme editor's **Add block** picker. | No |
| `settings` | Default values for settings you want to pre-populate. Each entry includes the setting name and its value. | No |
| `blocks` | Default blocks included in the preset. Each block entry must include a `type` attribute matching the block type, and a `settings` object formatted similarly to the `settings` attribute above. Optionally, include a `name` attribute to display when merchants add the block in the editor. | No |

Here's an example of how presets are defined within a block schema, assuming that the theme also contains a text block located in the `/blocks/text.liquid` Liquid file:

**/blocks/slide.liquid**

```json
{% schema %}
{
  "name": "Slide",
  "blocks": [{"type": "@app"}, {"type": "@theme"}],
  "settings": [
    {
      "type": "image_picker",
      "id": "image",
      "label": "Background image"
    },
    {
      "type": "color_background",
      "id": "background",
      "label": "Background color"
    }
  ],
  "presets": [
    {
      "name": "Slide",
      "category": "Banners",
      "settings": {
        "background": "#000000"
      },
      "blocks": [
        {
          "type": "text",
          "settings": {
            "text": "This is a slide!"
          }
        }
      ]
    }
  ]
}
{% endschema %}
```

---

##### tag

By default, when Shopify renders a block, it's wrapped in a `<div>` element with a unique `id` attribute:

```html
<div id="shopify-block-[id]" class="shopify-block">
  // Output of the block content
</div>
```

If you don't want to use a `<div>`, then you can specify which kind of HTML element to use with the `tag` attribute.

For example, the following schema returns the following output:

```json
{% schema %}
{
  "name": "Image",
  "tag": "picture"
}
{% endschema %}
```

**Output**

```html
<picture id="shopify-block-[id]" class="shopify-block">
  // Output of the block content
</picture>
```

**Tip:**

The `tag` attribute accepts any string up to a limit of 50 characters. It can also be used to render custom HTML elements.

###### Rendering blocks without a wrapper

In some advanced use cases, you might want more control over the tag and the attributes that are passed to it. For example, dynamically setting a tag or class name based on the settings of the block. In these scenarios, you can render blocks without a wrapper by setting the `tag` attribute to `null`.

When the `tag` attribute is set to `null`, Shopify doesn't wrap the contents of the block in a wrapper element, and instead directly outputs the contents of the block.

**Warning:**

Blocks that make use of `"tag": null` should contain a single top level HTML tag within the same Liquid file. Only a single HTML element can be tagged with `{{ block.shopify_attributes }}`. This element should be the topmost HTML element in the file. This is important to allow the theme editor to move the entirety of the block's markup to a new index when merchants re-order blocks without leaving orphaned HTML elements.

```liquid
<{{ block.settings.tag }} class="heading" {{ block.shopify_attributes }}>
  ...
</{{ block.settings.tag }}>


{% schema %}
{
  "name": "Heading",
  "tag": null,
  "settings": [
    {
      "type": "select",
      "id": "heading_size",
      "label": "Heading size",
      "options": [
        {
          "value": "h3",
          "label": "Small"
        },
        {
          "value": "h2",
          "label": "Medium"
        },
        {
          "value": "h1",
          "label": "Large"
        }
      ]
    }
  ]
}
{% endschema %}
```

**Output**

```html
<h3 class="heading">
  ...
</h3>
```

For blocks to be compatible with the theme editor, the top level HTML element must be tagged with the `{{ block.shopify_attributes }}` Liquid tag. This adds the necessary data attributes for the block to be identified by the theme editor. Shopify's theme editor uses that attribute to identify blocks in its JavaScript API.

**Note:**

Shopify automatically adds this attribute for you when it renders the wrapper around blocks, but when the `tag` attribute is set to `null`, you must ensure that the top level HTML element of your block has this attribute for it to be compatible with the theme editor.

---

##### class

When Shopify renders a block, it's wrapped in an HTML element with the `shopify-block` class. You can append other classes by using the class attribute:

```json
{% schema %}
{
  "name": "Slide",
  "class": "slide"
}
{% endschema %}
```

**Output**

```html
<div id="shopify-block-[id]" class="shopify-block slide">
  // Output of the block content
</div>
```

### 2.6.3 Theme block targeting

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/targeting

#### Theme block targeting

Theme block targeting allows theme developers to specify which blocks can be used in a section. In a theme section, theme developers can choose to:

1. Accept all theme blocks for use
2. Accept specific theme blocks for use

---

##### Accept all theme blocks

To accept all theme blocks in a section by adding a generic entry of type `@theme` to the blocks attribute of the schema of that section. To be more restrictive about which blocks can be use in specific sections, use block targeting.

In the following example, the Section will have access to all theme blocks.

**/sections/section.liquid**

```liquid
{% content_for 'blocks' %}


{% schema %}
{
  "name": "Section",
  "blocks": [{"type": "@theme"}]
}
{% endschema %}
```

---

##### Accept specific theme blocks

To accept specific theme blocks, theme developers can explicitly reference blocks in their schema. In the following example, the Slideshow section will have access to only the Slide theme block. In the editor, the block picker for Slideshow will only have a single block: slide. By default, theme blocks are available in all sections and theme blocks. In this example, the slide block will be in the block picker for all sections, not just the slideshow section.

**/blocks/slide.liquid**

```liquid
{% content_for 'blocks' %}


{% schema %}
{
  "name": "Slide"
}
{% endschema %}
```

**/sections/slideshow.liquid**

```liquid
{% content_for 'blocks' %}


{% schema %}
{
  "name": "Slideshow",
  "blocks": [{"type": "slide"}]
}
{% endschema %}
```

---

##### Private blocks

There are cases where you might want to limit the blocks that are available in sections. For example, slides are a type of block that should only be available in slideshow sections. To prevent the default behavior, theme developers can name the block with an underscore prefix.

In this case, `slide.liquid` can be renamed to `_slide.liquid`. All underscore prefixed blocks would be excluded from appearing in the block picker for blocks and sections that accept blocks with type `@theme`. Those blocks and sections will need to explicitly add the block by base filename. Ex: `"blocks": [ { "type": "_slide" } ]`

**/blocks/_slide.liquid**

```liquid
{% schema %}
{
  "name": "Slide"
}
{% endschema %}
```

**/sections/slideshow.liquid**

```liquid
{% content_for 'blocks' %}


{% schema %}
{
  "name": "Slideshow",
  "blocks": [{"type": "_slide"}]
}
{% endschema %}
```

### 2.6.4 Static blocks

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/static-blocks

#### Static blocks

Static theme blocks enable a theme developer to have more control over the layout of their blocks and sections. They are called static theme blocks because they are statically rendered in Liquid instead of dynamically rendered. Static theme blocks can be used in various scenarios:

* Bring structure to the theme in cases where the theme design requires theme blocks that should not be moved or deleted by the merchant.

* [Conditionally render theme blocks](#conditional-rendering).

In all cases, static blocks maintain the flexibility to customize the settings.

---

##### Statically vs dynamically rendered theme blocks

You can render a theme block in a section or another theme block in the following ways:

* Dynamically rendered in Liquid using `{% content_for 'blocks' %}`.
* Statically rendered in Liquid, setting the `type` explicitly using `{% content_for "block", type: "<type>", id: "<id>" %}`.

| Static blocks | Dynamically rendered blocks |
| - | - |
| Can be hidden and customized | Can be hidden and customized |
| Cannot be reordered (drag and drop) | Can be reordered (drag and drop) |
| Cannot be removed or duplicated | Can be removed or duplicated |
| Can be rendered conditionally or in a for-loop | Cannot be rendered conditionally or in a for-loop |
| Will be parsed if not added as part of the block preset | Must be included in a block preset to be added as part of the block preset |
| Don't count toward the `max_blocks` limit | Count toward the `max_blocks` limit |

---

##### Render a static block

To render a theme block statically in a section or block file, the following Liquid tag must be used:

```liquid
{% content_for "block", type: "type", id: "id" %}
```

| Parameter | Definition |
| - | - |
| `type` | The type (name) of an existing theme block in your theme's `/blocks` folder. |
| `id` required | A unique identifier, and associated string literal, within the section or block that contains the static blocks. The ID can be any descriptive identifier, for the static theme block that you can reference in presets and templates. The ID is required because it's possible to have many static blocks of the same type. Shopify never generates the ID for static blocks, so theme developers must set the static ID in Liquid. |

**Note:**

Along with this feature, we have updated the unique ID constraint for blocks. Block ID no longer needs to be unique to the root section. It must only be unique to its immediate parent. This means theme developers will not need to worry about where or how many times the static block is used in a section.

---

##### Passing data to static blocks

Just like theme blocks, static blocks have access to dynamic source data coming from sections and blocks. With static blocks you can also pass arbitrary data. For example, a slideshow section can pass the color to the slide block:

```liquid
{% content_for "block", id: "slide-1", type: "slide", color: "#111" %}
```

From the slide block you can access the data by referencing the same keyword:

```liquid
<h2 style="color: {{ color | default: 'green' }};">
  Shopify
</h2>
```

---

##### Conditional rendering

A static block is conditional when rendered in a conditional statement in Liquid. Shopify detects when a static block is rendered conditionally and shows a visual cue (a dotted eye icon) next to the block in the Theme Editor sidebar for an enhanced user experience.

```liquid
<div id="slideshow-{{ section.id }}">
  <div class="slideshow__slides">
    {% content_for "blocks" %}
  </div>


  {% if section.blocks.size > 1 %}
    {% content_for "block", type: "_slideshow-controls", id: "static-slideshow-controls" %}
  {% endif %}
</div>


{% schema %}
  {
    "name": "Slideshow",
    "class": "section--group",
    "blocks": [{ "type": "_slide" }, { "type": "_slideshow-controls" }]
  }
{% endschema %}
```

---

##### Static theme blocks in presets

Optionally, you may include static blocks in theme block presets to override settings values. A static block preset requires two additional keys:

1. `id`: The ID of the static block from Liquid
2. `static: true`: Signifies the block is static

**Note:**

If a section or block contains static blocks but does not explicitly include them in the presets, the static blocks will always get added along with the container section or block preset using the default settings values.

The example below renders a collapsible row using static blocks for the summary and the icon. Summary and icon are static blocks because they have a fixed relationship with the row. A row should always have an icon and a summary at the top level, therefore a merchant should not be able to delete them or reorder them.

In this example, the static blocks are authored in the block preset.

```liquid
{% content_for "block", type: "collapsible-row-summary", id: "collapsible-row" %}


<div>
  {% content_for "blocks" %}
</div>


{% schema %}
{
  "name": "Collapsible row",
  "tag": "details",
  "class": "details",
  "blocks": [{ "type": "@theme" }, { "type": "@app" }],
  "settings": [],
  "presets": [
    {
      "name": "Collapsible row",
      "blocks": [
        {
          "type": "collapsible-row-summary",
          "static": true,
          "id": "collapsible-row",
          "blocks": [
            {
              "type": "icon",
              "id": "collapsible-row-icon",
              "static": true,
              "settings": {
                "icon": "check_mark",
                "size": {
                  "width": "22px"
                }
              }
            }
          ]
        },
        {
          "type": "group",
          "blocks": [
            {
              "type": "heading"
            },
            {
              "type": "text"
            }
          ]
        }
      ]
    }
  ]
}
{% endschema %}
```

The code above will render a collapsible row in the editor, featuring a statically rendered icon and summary.

---

##### Static theme blocks in data

Static theme blocks are persisted in the JSON data. There are two key elements to note about static blocks in JSON data:

1. The `static: true` flag indicates which blocks are statically rendered.
2. Static block IDs are not included in the `block_order` array because static blocks can not be re-ordered by merchants. Shopify determines the order of static blocks based on their arrangement in the Liquid code relative to dynamic blocks, and displays them accordingly in the Theme Editor sidebar and on the rendered page.

The following code snippet is from a template json file. The `collapsible-row-summary` and `collapsible-row-icon` block have the `static: true` flag. They are not included in the `block_order` array.

```json
{
  "sections": {
   "custom_section": {
     "type": "custom-section",
     "blocks": {
       "collapsible_row": {
         "type": "collapsible-row",
         "settings": {},
         "blocks": {
           "collapsible-row-summary": {
             "type": "collapsible-row-summary",
             "static": true,
             "settings": {
               "summary": "Collapsible row"
             },
             "blocks": {
               "collapsible-row-icon": {
                  "type": "icon",
                  "static": true,
                  "settings": {
                  "icon": "check_mark",
                  "size": {
                    "width": "22px"
                  }
                }
               }
             },
             "block_order": []
           }
         },
         "block_order": []
       }
      },
      "block_order": ["collapsible_row"],
      "settings": {
        "direction": "column",
        "justify_content": "flex-start",
        "full_width": false
      }
   }
  },
  "order": ["custom_section"]
}
```

### 2.6.5 Dynamic sources (theme blocks)

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/dynamic-sources

#### Dynamic sources

[Dynamic sources](https://shopify.dev/docs/storefronts/themes/architecture/settings/dynamic-sources) allow merchants to connect [input settings](https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings) to data coming from resources such as products, collections, blogs, and pages as well as [metafields](https://help.shopify.com/manual/custom-data/metafields) and [metaobjects](https://help.shopify.com/manual/custom-data/metaobjects).

---

##### Dynamic sources available to theme blocks

[Theme blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks) are reusable blocks which are defined at the theme level and can be nested. The settings of theme blocks can be connected to data that come from the following:

| Source | Description |
| - | - |
| Template | The resource that's associated to the template or page being rendered. |
| Section | A [resource input setting](https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings#specialized-input-settings) defined as part of the [section schema](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema), such as product setting and collection setting. |
| Block | A [resource input setting](https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings#specialized-input-settings) defined as part of any of the ancestor blocks, such as product setting and collection setting. |
| Liquid | A resource drop passed to blocks explicitly in Liquid to the `content_for` tag. |

---

##### Accessing the closest resource

Theme blocks can access dynamic sources using access paths such as:

```js
// Template resource
{{ product }}
{{ collection }}


// Section settings
{{ section.settings.featured_product }}


// Block settings
{{ block.settings.collection }}
```

Theme blocks are reusable and can be nested across various sections and blocks. As a result, it isn't always possible to determine ahead of time where the data will come from. To address this issue, you can use the `closest` access path to reference the nearest resource of a specified type.

The `closest` access path provides a way to access the closest resource of a given type, regardless of whether it is coming from the template, parent section or any ancestor block.

**Note:**

The `closest.<type>` is accessible exclusively via theme settings and can serve as a configuration value for these settings.

###### Example

In this example, the `Image banner` section has a `Product card` block with nested `Media`, `Title` and `Price` blocks. They are connected to the closest product which currently resolves to the product setting of the `Product card` which is set to `Sunglasses`.

If the `Sunglasses` product is removed from the `Product card`, the nested blocks connected to the closest product are still pointing to the `Product card` product setting, even when the setting is empty. Because no closest product is currently set, the nested blocks will display placeholders.

If the `T-shirt` product is later selected in the `Product card` block, its nested blocks will then display the new closest product: `T-shirt`.

In other words, a setting connected to the closest product will automatically go up the chain of its ancestors to grab the attributes from the closest product found, in the following order:

1. A product setting within the same block;
2. A parent block product setting;
3. The current section product setting;
4. The current template's product

---

##### Usage in theme block presets

You can connect settings to the closest resource of a specific type within their presets, which allows you to access the most relevant resource of any type (such as a product, collection or page).

You can configure [theme block preset settings](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/schema#presets) to reference the closest resource of a compatible resource type by using the following Liquid syntax: `{{closest.<type>}}`.

When a nested theme block is connected the closest resource of a specified type, the order of resolution for the closest resource is based on the following rules:

1. The closest Liquid context setter of the specified type
2. The closest ancestor block setting of the specified type
3. The section resource settings of the specified type
4. The template resource if it's of the specified type

The following table shows all possible configuration values for each resource type:

| Resource type | Configuration value |
| - | - |
| Product | `{{ closest.product }}` |
| Collection | `{{ closest.collection }}` |
| Article | `{{ closest.article }}` |
| Blog | `{{ closest.blog }}` |
| Page | `{{ closest.page }}` |
| Metaobject | `{{ closest.metaobject[<definition_type>] }}` |

The following examples shows a price block with a [product setting](https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings#product). The price block's product setting is set to `closest.product`. The closest key means it will be able to access the closest product resource from the closest ancestor possible.

**blocks/price.liquid**

```liquid
{{ block.settings.product.price | default: 1999 }}


{% schema %}
{
  "name": "Product (price)",
  "class": "price-block",
  "settings": [{
    "type": "product",
    "id": "product",
    "label": "Product"
   }],
  "presets": [{
    "name": "Product (price)",
    "settings": {
      "product": "{{ closest.product }}"
    }
  }]
}
{% endschema %}
```

You can configure theme block settings in presets to point to the closest ancestor of a specific resource type, without needing to specify where. After a resource is connected at an ancestor level, children blocks can access the available resource [properties](https://shopify.dev/docs/storefronts/themes/architecture/settings/dynamic-sources#available-shopify-resources-and-attributes) using dynamic sources from their settings.

In the following example, the text, price and product media blocks access the closest product resource using `{{ closest.product }}`:

**blocks/card.liquid**

```liquid
{% schema %}
{
  "name": "Card",
  "blocks": [{"type": "@theme"}],
  "presets": [
    {
      "name": "Product Card",
      "blocks": [
        {
          "type": "group",
          "blocks": [
            {
              "type": "text",
              "settings": {
                "text": "<p>{{ closest.product.title }}</p>"
              }
            },
            {
              "type": "price",
              "settings": {
                "product": "{{ closest.product }}"
              }
            },
            {
              "type": "product-medias",
              "settings": {
                "product": "{{ closest.product }}"
              }
            }
          ]
        }
      ]
    }
  ]
}
{% endschema %}
```

After the preset has been inserted into a section or block, then the data is stored in JSON as follows:

**index.json**

```json
{
  "sections": {
    "custom_section_1": {
      "type": "custom-section",
      "blocks": {
        "group_1": {
          "blocks": {
            "text_1": {
              "type": "text",
              "settings": {
                "text": "<p>{{ closest.product.title }}</p>"
              }
            },
            "price_1": {
              "type": "price",
              "settings": {
                "product": "{{ closest.product }}"
              }
            },
            "product_medias_1": {
              "type": "product-medias",
              "settings": {
                "product": "{{ closest.product }}"
              }
            }
          },
          "block_order": [
            "text_1",
            "price_1",
            "product_medias_1"
          ]
        }
      },
      "block_order": ["group_1"]
    }
  },
  "order": ["custom_section_1"]
}
```

---

##### Passing resources down in Liquid using closest

Theme block settings can access the closest resources set in Liquid using the [`content_for` Liquid tag](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/schema#rendering-nested-blocks) directly. A resource can be passed directly to the `content_for` tag using a parameter that specifies the type of the resource.

The table below shows which resource types can be passed to the `content_for` tag in Liquid:

| Resource type | Syntax |
| - | - |
| Product | `{% content_for "blocks", closest.product: <Product Drop> %}` |
| Collection | `{% content_for "blocks", closest.collection: <collection Drop /> %}` |
| Article | `{% content_for "blocks", closest.article: <ArticleDrop> %}` |
| Blog | `{% content_for "blocks", closest.blog: <BlogDrop> %}` |
| Page | `{% content_for "blocks", closest.page: <PageDrop> %}` |
| Metaobject | `{% content_for "blocks", closest.metaobject.<definition_type>: <metaobjectDrop /> %}` |

The `{% content_for "block" %}` tag, which is used to render [static blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/static-blocks), also supports passing context using the same syntax for all of the resource types above.

**Note:**

If the resource type doesn't match one of these parameters, then an error is returned.

###### Example

A common use-case for passing resources down to nested blocks in Liquid is when looping over the products in a collection. We need to pass down the current product that is being iterated over in the collection to the `content_for` tag so that nested blocks can access the product resource using `{{ closest.product }}`.

**blocks/product-grid.liquid**

```liquid
<ul class="product-grid">
  {% for product in block.settings.collection.products %}
    <li>
      {% content_for "block", type: "product-card", id: "card", closest.product: product %}
    </li>
  {% endfor %}
</ul>


{% schema %}
{
  "name": "Product grid",
  "settings": [{
    "type": "collection",
    "id": "collection",
    "label": "Collection"
  }],
  "presets": [{
    "name": "Product grid",
    "blocks": [
      {
        "id": "card",
        "type": "product-card",
        "static": true,
        "settings": {
          "product": "{{ closest.product }}"
        },
        "blocks": [
          {
            "type": "price",
            "settings": {
              "product": "{{ closest.product }}"
            }
          }
        ]
      }
    ]
  }]
}
{% endschema %}
```

In this example, we are rendering a [static block](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/static-blocks) named `product-card` while looping over the products in the collection setting of the `Product grid` block. This will allow the `Product card` block, and all of its nested blocks to access the current product for that card via `{{ closest.product }}`.

---

##### Using dynamic sources in the theme editor

Merchants can connect theme block settings to the closest resource of a particular type using the dynamic sources picker in the theme editor. A merchant might have access to more than one type of closest resource.

In this example, the merchant is editing a text block on a product template. The merchant is connecting a text setting for the text block to a dynamic source. The merchant can pick from different resource contexts: the closest product, the product set at the section or the product set at the template.

Once a closest resource context is selected, the merchant may select a data field. All the listed data fields are compatible with a text setting.

### 2.6.6 Section blocks

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/blocks/section-blocks

#### Section Blocks

Sections can define blocks locally within their schema. Use section blocks to create customizable content layouts within a specific section. You can only use section blocks within the section where they're defined. You can't nest other blocks in section blocks, so you can't use them to create hierarchy.

To learn more about section blocks, refer to the [blocks](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#blocks) property of the [section schema](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema).

---

##### Define blocks within sections

In your section's schema, add a `blocks` array. Each object in the array represents a block that's local to the section.

The following is an example:

```json
{
  "name": "Example section",
  "blocks": [
    {
      "type": "heading",
      "name": "Heading",
      "settings": [
        {
          "type": "text",
          "id": "heading",
          "label": "Heading",
          "default": "Hello, world!"
        }
      ]
    }
  ]
}
```

In this example, the `Example section` includes the `Heading` block. The block has the following data:

* **`type`**: A property that represents a unique identifier for the block
* **`settings`**: An array that contains the customizable options for the block.

###### Rendering the block

In your section's Liquid file, you can loop over the blocks of the section and render each block based on its type. You can access the settings of the block using the `block` Liquid tag. The following is an example:

```liquid
{% for block in section.blocks %}
  {%- case block.type -%}
    {%- when "heading" -%}
      <h1>{{ block.settings.heading }}</h1>
  {% endcase %}
{% endfor %}
```

In this example, the `for` loop iterates over each block in the section, and the `block.settings.heading` expression outputs the heading of each block.

**Caution:**

"Don't rely on the literal value of a block's ID when you iterate over blocks. The ID is dynamically generated and is subject to change." The following is an example of relying on a literal value of a block's ID, which may break functionality in your theme if the ID changes:

```liquid
{% for block in section.blocks %}
{%- if block.id == 'J6d9jV' -%}
<h1>{{ block.settings.heading }}</h1>
{% endif %}
{% endfor %}
```

### 2.6.7 App blocks for themes

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks

#### App blocks for themes

If your section is part of a [JSON template](https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates), then you should support blocks of type `@app`. These blocks enable app developers to create blocks for merchants to add app content to their theme without having to directly edit theme code. You can build app blocks using [theme app extensions](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions).

**Note:**

Blocks of type `@app` aren't supported in [statically rendered sections](https://shopify.dev/docs/storefronts/themes/architecture/sections#statically-render-a-section).

In the theme editor, merchants can choose to add app blocks to existing sections, or in a new section.

When merchants choose to add the app to a new section, Shopify automatically wraps the app block in a [wrapper section](#app-block-wrapper) called `Apps`. You can customize this wrapper section by your own `apps.liquid` section.

To add support for app blocks to your sections and theme blocks, you need take the following steps:

* Add support for app blocks to the schema
* Render the block content
* Ensure that you have valid section settings

Refer to Dawn's [main product section](https://github.com/Shopify/dawn/blob/main/sections/main-product.liquid) for an example implementation of an existing theme section that opts-in to accepting app blocks.

**Tip:**

For framework information about app blocks, including the valid schema for app blocks, refer to the [theme app extensions framework](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions/configuration) documentation.

---

##### Supporting app blocks

To allow merchants to add app blocks to a [section](https://shopify.dev/docs/storefronts/themes/architecture/sections) or a [theme block](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks), you need to include a generic block of type `@app` in the section or block schema.

For example:

```json
"blocks": [
  {
    "type": "@app"
  }
]
```

**Caution:**

"Blocks of type `@app` don't accept the `limit` parameter. Including this will result in an error."

---

##### Render app blocks

To render app blocks, the theme block must use the `{% content_for 'blocks' %}` Liquid tag. This tag handles block rendering, including app blocks.

For example:

```liquid
<div class="group">
  {% content_for 'blocks' %}
</div>
```

###### Render app blocks alongside section-defined blocks

To render an app block alongside [section-defined blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/section-blocks), you need to check for the appropriate type, and use the following code:

```liquid
{% render block %}
```

For example:

```liquid
{% for block in section.blocks %}
  {% case block.type %}
    {% when '@app' %}
      {% render block %}
    ...
  {% endcase %}
{% endfor %}
```

---

##### App blocks and section settings

To prevent ambiguity with [autofill settings](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions/configuration#autofill), sections that support app blocks can include only one resource setting of each type as a section setting. For example, a section might include only one product setting and only one collection setting.

---

##### App block wrapper

Merchants can add app blocks to a page in the following ways:

* As a block within the confines of the section that's rendering the block
* In a similar manner to sections, giving them the full width of the page to render content

Because app blocks aren't sections themselves, Shopify wraps these top-level app blocks in a platform-generated `apps.liquid` wrapper section by default. However, you can override this default wrapper section by creating your own.

###### Shopify wrapper logic

Shopify determines which wrapper to use for these top-level app blocks based on the following logic:

**Theme-provided `apps.liquid` section**

* If your theme includes a section file named `apps.liquid`, Shopify uses this section to wrap any top-level app block added by the merchant.
* This provides theme developers specific control over how only app blocks are rendered when added directly to a template.
* The `apps.liquid` section schema needs to support blocks of type `@app` and must include a preset. If either of these is missing, then an `Apps not supported` or `Apps section is invalid` error is returned in the theme editor and merchants aren't able to use the section.

**Theme-provided `_blocks.liquid` section**

* If `apps.liquid` does not exist, Shopify looks for a section file named `_blocks.liquid`.
* This section acts as a more generic wrapper, designed to handle both `@app` blocks and `@theme` blocks when added directly to a template.
* The `_blocks.liquid` section schema needs to support block types `@theme` and `@app`, and must include a preset. If either of these is missing, then an error is returned in the theme editor and merchants aren't able to use the section

**Platform-generated `apps.liquid` section**

* If neither `apps.liquid` nor `_blocks.liquid` exists in the theme, Shopify falls back to using a default, platform-generated `apps.liquid` wrapper to render the top-level app block.

###### App Wrapper Examples

**Caution:**

"The `apps.liquid` section schema can't contain the `templates` schema attribute. This also includes the `templates` attribute within the `enabled_on/disabled_on` schema attributes."

**/sections/apps.liquid**

```liquid
{% for block in section.blocks %}
  {% render block %}
{% endfor %}


{% schema %}
  {
    "name": "App wrapper",
    "settings": [],
    "blocks": [
      {
        "type": "@app"
      }
    ],
    "presets": [
      {
        "name": "App wrapper"
      }
    ]
  }
{% endschema %}
```

To enable merchants to control how the app looks inside of an app section, you can add a setting that lets merchants add margins around the app blocks. This helps make the app section margins consistent with your theme's layout.

**/sections/apps.liquid**

```liquid
<div class="{% if section.settings.include_padding %}padded{% endif %}">
  {% for block in section.blocks %}
    {% render block %}
  {% endfor %}
</div>


{% schema %}
  {
    "name": "App wrapper",
    "settings": [
      {
        "type": "checkbox",
        "id": "include_padding",
        "default": true,
        "label": "Make section margins the same as theme"
      }
    ],
    "blocks": [
      {
        "type": "@app"
      }
    ],
    "presets": [
      {
        "name": "App wrapper"
      }
    ]
  }
{% endschema %}
```

**Note:**

"The `apps.liquid` section isn't a standard theme section. It can't be manually rendered, meaning you can't include it with `{% section 'apps' %}`, and it won't show up in the theme editor for merchants to add to pages."

### 2.6.8 AI generated theme blocks

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/blocks/ai-generated-theme-blocks

#### AI generated theme blocks

In the theme editor, merchants can generate theme blocks in existing sections that support theme blocks. In order for theme developers to create themes that enable merchants to use this feature effectively, there are a few key concepts to understand.

---

##### Theme blocks

To make it possible for a section to accept AI generated blocks, it must accept theme blocks. To accept all theme blocks in a section, add the type `@theme` to the blocks attribute of the schema of that section.

---

##### Wrapper Section

Generated blocks aren't sections themselves. Therefore Shopify wraps these generated blocks in a platform-generated section by default such as when merchants choose to use Sidekick to generate a block in a new section.

Shopify automatically wraps the generated block in a wrapper section called `_blocks.liquid`. You can override and customize this wrapper section by adding your own `_blocks.liquid` section to your theme.

**Note:**

"The `_blocks.liquid section` isn't a standard theme section. It can't be manually rendered, meaning you can't include it with `{% section '_blocks' %}`, and it won't show up in the theme editor for merchants to add to pages."

###### Custom `_blocks.liquid` section

The `_blocks.liquid` section schema needs the following to be true:

1. Define `@theme` and `@app` as block types
2. Define `presets`
3. Define `{% content_for blocks %}`
4. Does not define the `templates` attribute, including within `disabled_on` and `enabled_on`

If any of these cases is not met, then an error is returned in the code editor and merchants aren't able to use the section.

Additionally, you can enable merchants to control how the block looks inside the \_blocks.liquid wrapper using settings. This ensures the wrapper is visually consistent with your theme's layout.

**\_blocks.liquid**

```liquid
{% content_for 'blocks' %}


{% schema %}
{
  "name": "Section",
  "blocks": [{ "type": "@theme" }, { "type": "@app" }],
  "settings": [
    {
      "type": "range",
      "id": "section-margin",
      "label": "",
      "min": 0,
      "max": 50,
      "default": 0,
      "unit": "px"
    },
  ],
  "presets": [
    {
      "name": "Section"
    }
  ]
}
{% endschema %}
```

---

## 2.7 Snippets

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/snippets

### Snippets

#### Overview

Snippets are "reusable pieces of Liquid code that help you maintain consistency and reduce duplication across your theme." Unlike sections and blocks, snippets remain hidden from merchants in the theme editor, making them ideal for repeated code patterns like product cards or navigation elements.

#### How to use snippets

The `render` tag references snippets in Liquid code and accepts named parameters for passing data:

```liquid
{% render 'product-card',
product: product,
show_price: true,
max_description_length: 120
%}
```

##### Variable scoping

Snippets have restricted variable access. You can access global objects such as `product`, `collection`, and `section`, plus any variables passed as parameters. Variables created within a snippet stay local to it and cannot be accessed externally.

#### Documenting snippets with LiquidDoc

LiquidDoc provides "a structured way to add documentation to your snippets" and integrates with development tools for real-time feedback and code completion.

```liquid
{% doc %}
Product card snippet


@param {string} title - The title to display
@param {number} [max_items] - Optional maximum number of items to show


@example
{% render 'example-snippet', title: 'Featured Products', max_items: 3 %}
{% enddoc %}
```

#### Next steps

- Learn more about LiquidDoc
- Learn more about the render tag

---

## 2.8 Settings

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/settings

### Settings

To make it easier for merchants to customize your theme, you can use JSON to create settings that merchants can access through the theme editor.

You can provide settings at the theme, section, or block level. Settings can be fixed (such as informational elements) or interactive (such as a drop-down menu). Setting values can be static, or use dynamic sources to render contextually appropriate values.

Exposing settings makes your theme more customizable so it can better express a merchant's brand. It also can make your theme more flexible so that you can address various use cases for merchants.

---

#### Subtypes

There are two categories of settings:

| Category | Description |
| - | - |
| Input settings | Settings that can hold a value, and are configurable by app users. |
| Sidebar settings | Settings that can't hold a value, and aren't configurable by app users. They're informational elements that can be used to provide detail and clarity for your input settings. |

---

#### Location

You can create settings in the following places:

* `config` > `settings_schema.json`
* Section files in the `sections` folder, using the section's `{% schema %}` tag

```text
└── theme
  ├── config
  |   ├── settings_schema.json
  |   ...
  ├── sections
  |   ├── main_product.liquid
  |   ├── another_section_file.liquid
  |   ...
  ...
```

##### settings_schema.json

The settings_schema.json file controls the content of the **Theme settings** area of the theme editor. Settings in this file translate to global theme settings, which can be accessed through the Liquid settings object.

##### Section schema

The section `{% schema %}` tag is where you can create section settings and block settings. Those settings can be accessed through the `settings` attribute of the section object and block object, respectively.

---

#### Schema

Settings are defined as a JSON `settings` attribute that's parented to the object that the settings apply to. This attribute accepts an array of settings. Input settings and sidebar settings both use standard schema attributes. You can find detailed descriptions of these attributes in their respective sections:

* Input Settings
* Sidebar settings

Most setting types may be conditionally set using the `visible_if` attribute.

#### Basic setting example

```json
{
  ...
  "settings": [
    {
      "type": "header",
      "content": "My settings"
    },
    {
      "type": "text",
      "id": "my_id",
      "label": "My setting label",
      "default": "Enter text here"
    },
    {
      "type": "select",
      "id": "layout_style",
      "label": "type",
      "options": [
        {
          "value": "flex",
          "label": "Stack"
        },
        {
          "value": "grid",
          "label": "Grid"
        }
      ],
      "default": "flex"
    },
    {
      "type": "select",
      "id": "content_direction",
      "label": "Direction",
      "options": [
        { "value": "row", "label": "Horizontal" },
        { "value": "column", "label": "Vertical" }
      ],
      "default": "column",
      "visible_if": "{{ block.settings.layout_style == 'flex' }}"
    }
  ],
  ...
}
```

---

#### Usage

When working with settings, you should familiarize yourself with the following:

* Accessing setting values
* Checking the setting value format
* Using dynamic sources for settings

##### Access settings

Depending on where they were created, you can access settings through the following Liquid objects:

* The global `settings` object
* The `section` object
* The `block` object

**Note:**

Settings from the `settings` object can be accessed in Liquid theme assets.

To access a specific setting, append the `id` attribute of the associated setting to the object that you want to access.

For example, if you had the following setting implemented in each Liquid object:

```json
{
  "type": "text",
  "id": "message",
  "label": "Message",
  "default": "Hello!"
}
```

Then the following Liquid would generate the following output:

**Input**

```liquid
// Settings
Message: {{ settings.message }}


// Section
Message: {{ section.settings.message }}


// Block
Message: {{ block.settings.message }}
```

**Output**

```text
// Settings
Message: Hello!


// Section
Message: Hello!


// Block
Message: Hello!
```

##### Check the format of the setting value

When referencing settings, you should always check that the value is in the format that you expect. Any setting without an automatic default value could end up with no value, which translates to an empty string.

For example, if you have a setting with an `id` of `message`, then the following Liquid would generate the following output depending on the value:

**Input**

```liquid
// No value
Setting: {{ settings.message }}


// With value
Setting: {{ settings.message }}
```

**Output**

```text
// No value
Setting:


// With value
Setting: Message value
```

You can check whether a value is an empty string with the `blank` operator. For example:

```liquid
{% unless settings.message == blank %}
  {{ settings.message }}
{% endunless %}
```

###### Resource-based settings

To avoid an empty string, check that the value is in the format that you expect. It's possible that no resource was selected, selected resource no longer exists, or the selected resource has been hidden.

For example, if you have the following `page` type setting:

```json
{
  "type": "page",
  "id": "page",
  "label": "Page"
}
```

Then you can check for emptiness like the following:

```liquid
{% if settings.page != blank %}
  {{ settings.page.title }}
  {{ settings.page.content }}
{% else %}
  No page, or invalid page, selected.
{% endif %}
```

**Tip:**

Resource-based settings didn't always return the resource object. To learn more, refer to Legacy resource-based settings.

###### Legacy resource-based settings

In the past, resource-based settings returned the handle of the associated resource, and you had to access the actual object through Liquid using that handle.

For example, if you had the following product setting, then you would need to access the product object like the following:

**Setting**

```json
{
  "type": "product",
  "id": "product",
  "label": "Product"
}
```

**Access setting**

```liquid
{% unless settings.product == blank %}
  {% assign product = all_products[settings.product] %}


  {% if product %}
    {{ product.title }} - {{ product.price }}
  {% else %}
    No product, or invalid product, selected.
  {% endif %}
{% endunless %}
```

##### Dynamic sources

Settings for sections and blocks included in a JSON template have the option for merchants to connect one or more dynamic sources to the setting, depending on the setting type.

Learn more about dynamic sources.

---

#### Conditional settings

Settings can be displayed conditionally by passing a boolean expression to the `visible_if` attribute:

```json
"visible_if": "{{ block.settings.layout_style == 'flex' }}"
```

Not all settings can be conditionally set. The following settings support conditional settings:

* All basic input settings
* All sidebar settings
* These specialized input settings:
  * color
  * color_background
  * color_scheme
  * font_picker
  * html
  * image_picker
  * inline_richtext
  * link_list
  * liquid
  * richtext
  * text_alignment
  * url
  * video
  * video_url

**Note:**

Conditional settings cannot access runtime context or resolved data source values. While you can check if a setting with a data source *has a value*, you cannot create conditions based on what that data source *resolves to*.

---

#### Platform-controlled settings

In the theme editor, Shopify exposes a custom CSS setting at the theme and section level. You can't add or hide this setting in your settings schema.

Any custom CSS that merchants add using this setting is stored in a `custom_css` attribute, either in a JSON template's section attribute, or in the settings_data.json `platform_customizations` object.

This setting is intended to enable users to customize the look and feel of their storefront without editing theme code. As a theme developer, you shouldn't add this setting, or edit the value of this setting after it's set. Instead, you should use dedicated CSS assets and `stylesheet` Liquid tags, and introduce customization options for CSS in these areas using theme settings.

---

#### Translate settings

You can translate various attributes of the settings schema depending on the online store's active language. These translations are stored in schema locale files.

### 2.8.1 Input settings

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings

#### Input settings

Input settings can hold a value and are configurable by merchants.

Input settings are generally composed of [standard attributes](#standard-attributes), and there are two categories:

* [Basic input settings](#basic-input-settings)
* [Specialized input settings](#specialized-input-settings)

To learn how to access the values of these settings for use in your theme, refer to the [settings overview](https://shopify.dev/docs/storefronts/themes/architecture/settings#access-settings).

**Tip:**

If you want to add informational elements to your settings display, like a heading, then refer to [Sidebar settings](https://shopify.dev/docs/storefronts/themes/architecture/settings/sidebar-settings).

---

##### Standard attributes

The following are standard attributes across input settings. However, depending on the input type, there might be extra attributes or some might not apply:

| Attribute | Description | Required |
| - | - | - |
| `type` | The setting type, which can be any of the [basic](#basic-input-settings) or [specialized](#specialized-input-settings) input setting types. | Yes |
| `id` | The setting ID, which is used to access the setting value. | Yes |
| `label` | The setting label, which will show in the theme editor. | Yes |
| `default` | The default value for the setting. | No |
| `info` | An option for informational text about the setting. | No |

---

##### Basic input settings

The following are the basic input setting types:

* [checkbox](#checkbox)
* [number](#number)
* [radio](#radio)
* [range](#range)
* [select](#select)
* [text](#text)
* [textarea](#textarea)

---

##### checkbox

A setting of type `checkbox` outputs a checkbox field. This setting type can be used for toggling features on and off, such as whether to show an announcement bar.

For example, the following setting generates the following output:

###### Setting

```json
{
  "type": "checkbox",
  "id": "show_announcement",
  "label": "Show announcement",
  "default": true
}
```

###### Output

![checkbox setting](https://shopify.dev/assets/assets/images/themes/settings/basic/checkbox-B9evgs1-.png)

When accessing the value of a `checkbox` type setting, data is returned as a [boolean](https://shopify.dev/docs/api/liquid/basics/types#boolean).

**Note:**

If `default` is unspecified, then the value is `false` by default.

---

##### number

A setting of type `number` outputs a single number field. In addition to the [standard attributes](#standard-attributes) of an input setting, `number` type settings have the following attribute:

| Attribute | Description | Required |
| - | - | - |
| `placeholder` | A placeholder value for the input. These values only appear for settings defined in `settings_schema.json`. They don't appear for settings defined in a section's schema. | No |

You can use this setting type to capture a varying numerical value, such as the number of products to show per page on a collection page.

For example, the following setting generates the following output:

###### Setting

```json
{
  "type": "number",
  "id": "products_per_page",
  "label": "Products per page",
  "default": 20
}
```

###### Output

![number setting](https://shopify.dev/assets/assets/images/themes/settings/basic/number-CS1t32hl.png)

When accessing the value of a `number` type setting, data is returned in one of the following formats:

* [A number](https://shopify.dev/docs/api/liquid/basics/types#number).
* [nil](https://shopify.dev/docs/api/liquid/basics/types#nil), if nothing has been entered.

**Caution:**

The `default` attribute is optional. However, the value must be a number and not a string. Failing to adhere results in an error.

---

##### radio

A setting of type `radio` outputs a radio option field. In addition to the [standard attributes](#standard-attributes) of an input setting, `radio` type settings have a required `options` attribute that accepts an array of `value` and `label` definitions.

You can use this setting type to capture a multi-option selection, such as the alignment of a header logo.

For example, the following setting generates the following output:

###### Setting

```json
{
  "type": "radio",
  "id": "logo_alignment",
  "label": "Logo alignment",
  "options": [
    {
      "value": "left",
      "label": "Left"
    },
    {
      "value": "centered",
      "label": "Centered"
    }
  ],
  "default": "left"
}
```

###### Output

![radio setting](https://shopify.dev/assets/assets/images/themes/settings/basic/radio-CCoZNBwU.png)

When accessing the value of a `radio` type setting, data is returned as a [string](https://shopify.dev/docs/api/liquid/basics/types#string).

**Note:**

If `default` is unspecified, then the first option is selected by default.

---

##### range

A setting of type `range` outputs a range slider field with an input field. In addition to the [standard attributes](#standard-attributes) of an input setting, `range` type settings have the following attributes:

| Attribute | Description | Required |
| - | - | - |
| `min` | The minimum value of the input | Yes |
| `max` | The maximum value of the input | Yes |
| `step` | The increment size between steps of the slider. Defaults to `1` when omitted. | No |
| `unit` | The unit for the input. For example, you can set `px` for a font-size slider. | No |

You can use this setting type to capture a varying numerical value, such as font size.

You can update the `range` value using the provided slider, or by typing a value into the input field:

* If you enter a value that doesn't respect the `step` definition, then the value rounds to the closest step.
* If you enter a value outside of the given `min` and `max`, then the value reverts to the `min` or `max` value accordingly.

For example, the following setting generates the following output:

###### Setting

```json
{
  "type": "range",
  "id": "font_size",
  "min": 12,
  "max": 24,
  "step": 1,
  "unit": "px",
  "label": "Font size",
  "default": 16
}
```

###### Output

![range setting](https://shopify.dev/assets/assets/images/themes/settings/basic/range-aWMy5szy.png)

When accessing the value of a `range` type setting, data is returned as a [number](https://shopify.dev/docs/api/liquid/basics/types#number).

**Caution:**

The `default` attribute is required. The `min`, `max`, `step`, and `default` attributes can't be string values. Failing to adhere results in an error.

---

##### select

A setting of type `select` outputs [different selector fields](#selector-fields), depending on certain criteria. In addition to the [standard attributes](#standard-attributes) of an input setting, `select` type settings have the following attributes:

| Attribute | Description | Required |
| - | - | - |
| `options` | Takes an array of `value`/`label` definitions for each option in the drop-down. | Yes |
| `group` | An optional attribute that you can add to each option to create option groups in the drop-down. | No |

###### Selector fields

The following criteria render selector fields as either a `DropDown` or a `SegmentedControl`:

| Field | Rendering criteria | Output |
| - | - | - |
| `Dropdown` | * The optional `group` attribute is used.
* More than five options are provided.
* The options are too long and might overflow their container. | ![Selector fields rendered as a field of type DropDown](https://shopify.dev/assets/assets/images/themes/settings/basic/select_dropdown-CUcAaqoR.png) |
| `SegmentedControl` | * The optional `group` attribute isn't used.
* Two to five options are provided.
* All options fit within their container and don't overflow. | ![Selector fields rendered as a SegmentedControl field](https://shopify.dev/assets/assets/images/themes/settings/basic/select_segmented_control-DM4rog_O.png) |

You can use this setting type to capture a multi-option selection, such as the vertical alignment of slideshow text.

For example, the following setting generates the following output:

###### Setting

```json
{
  "type": "select",
  "id": "vertical_alignment",
  "label": "Vertical alignment",
  "options": [
    {
      "value": "top",
      "label": "Top"
    },
    {
      "value": "middle",
      "label": "Middle"
    },
    {
      "value": "bottom",
      "label": "Bottom"
    }
  ],
  "default": "middle"
}
```

###### Output

![select setting](https://shopify.dev/assets/assets/images/themes/settings/basic/select_segmented_control-DM4rog_O.png)

However, if your setting matches the criteria for a drop-down field (`DropDown`) because it has more than five options, then the following output is generated:

###### Setting

```json
{
  "type": "select",
  "id": "sizes",
  "label": "Sizes",
  "options": [
    {
      "value": "xs",
      "label": "X-small"
    },
    {
      "value": "s",
      "label": "Small"
    },
    {
      "value": "m",
      "label": "Medium"
    },
    {
      "value": "l",
      "label": "Large"
    },
    {
      "value": "xl",
      "label": "X-large"
    },
    {
      "value": "xxl",
      "label": "XX-large"
    }
  ],
  "default": "m"
}
```

###### Output

![select setting](https://shopify.dev/assets/assets/images/themes/settings/basic/select_dropdown-CUcAaqoR.png)

When accessing the value of a `select` type setting, data is returned as a [string](https://shopify.dev/docs/api/liquid/basics/types#string).

**Note:**

If `default` is unspecified, then the first option is selected by default.

---

##### text

A setting of type `text` outputs a single-line text field. In addition to the [standard attributes](#standard-attributes) of an input setting, `text` type settings have the following attribute:

| Attribute | Description | Required |
| - | - | - |
| `placeholder` | A placeholder value for the input. These values only appear for settings defined in `settings_schema.json`. They don't appear for settings defined in a section's schema. | No |

You can use this setting type to capture short strings, such as titles.

For example, the following setting generates the following output:

###### Setting

```json
{
  "type": "text",
  "id": "footer_linklist_title",
  "label": "Heading",
  "default": "Quick links"
}
```

###### Output

![text setting](https://shopify.dev/assets/assets/images/themes/settings/basic/text-CAnGUyes.png)

When accessing the value of a `text` type setting, data is returned in one of the following formats:

* A [string](https://shopify.dev/docs/api/liquid/basics/types#string).
* An [`empty` object](https://shopify.dev/docs/api/liquid/basics/types#emptydrop), if nothing has been entered.

**Tip:**

Settings of type `text` are not updated when switching presets.

---

##### textarea

A setting of type `textarea` outputs a multi-line text field. In addition to the [standard attributes](#standard-attributes) of an input setting, `textarea` type settings have the following attribute:

| Attribute | Description | Required |
| - | - | - |
| `placeholder` | A placeholder value for the input. These values only appear for settings defined in `settings_schema.json`. They don't appear for settings defined in a section's schema. | No |

You can use this setting type to capture larger blocks of text, such as messages.

For example, the following setting generates the following output:

###### Setting

```json
{
  "type": "textarea",
  "id": "home_welcome_message",
  "label": "Welcome message",
  "default": "Welcome to my shop!"
}
```

###### Output

![textarea setting](https://shopify.dev/assets/assets/images/themes/settings/basic/textarea-RUfHgDDX.png)

When accessing the value of a `textarea` type setting, data is returned in one of the following formats:

* A [string](https://shopify.dev/docs/api/liquid/basics/types#string).
* An [`empty` object](https://shopify.dev/docs/api/liquid/basics/types#emptydrop), if nothing has been entered.

---

##### Specialized input settings

The following are the specialized input setting types:

* [article](#article)
* [article_list](#article_list)
* [blog](#blog)
* [collection](#collection)
* [collection_list](#collection_list)
* [color](#color)
* [color_background](#color_background)
* [color_scheme](#color_scheme)
* [color_scheme_group](#color_scheme_group)
* [font_picker](#font_picker)
* [html](#html)
* [image_picker](#image_picker)
* [inline_richtext](#inline_richtext)
* [link_list](#link_list)
* [liquid](#liquid)
* [metaobject](#metaobject)
* [metaobject_list](#metaobject_list)
* [page](#page)
* [product](#product)
* [product_list](#product_list)
* [richtext](#richtext)
* [text_alignment](#text_alignment)
* [url](#url)
* [video](#video)
* [video_url](#video_url)

---

##### article

A setting of type `article` outputs an article picker field that's automatically populated with the available articles for the store. You can use this setting type to capture an article selection, such as the article to feature on the homepage.

For example, the following setting generates the following output:

###### Setting

```json
{
  "type": "article",
  "id": "article",
  "label": "Article"
}
```

###### Output

![article setting](https://shopify.dev/assets/assets/images/themes/settings/specialized/article-CjWR9_o2.png)

When accessing the value of an `article` type setting, data is returned in one of the following formats:

* An [`article` object](https://shopify.dev/docs/api/liquid/objects/article).

To ensure backwards compatibility with [legacy resource-based settings](https://shopify.dev/docs/storefronts/themes/architecture/settings#legacy-resource-based-settings), outputting the setting directly will return the object's handle.

* `blank` if no selection has been made, the selection isn't visible, or the selection no longer exists

**Note:**

Settings of type `article` are not updated when switching presets. `article` settings also don't support the `default` attribute.

---

##### article_list

A setting of type `article_list` outputs an article picker field that's automatically populated with the available blog articles for the store. You can use this setting type to capture multiple articles, such as a group of articles to feature on the homepage.

**Note:**

You can only choose from articles that are published.

In addition to the [standard attributes](#standard-attributes) of an input setting, `article_list` type settings have the following attributes:

| Attribute | Description | Required |
| - | - | - |
| `limit` | The maximum number of articles that the merchant can select. The default limit, and the maximum limit you can set, is 50. | No |

###### Setting

```json
{
  "type": "article_list",
  "id": "featured_articles",
  "label": "Featured articles",
  "limit": 12
}
```

###### Output

![article_list setting](https://shopify.dev/assets/assets/images/themes/settings/specialized/article_list-DsF9KSDO.png)

When accessing the value of an `article_list` type setting, data is returned in one of the following formats:

* An array of [`article` objects](https://shopify.dev/docs/api/liquid/objects/article)

The array supports pagination using the [paginate](https://shopify.dev/docs/api/liquid/tags/paginate#paginate-paginating-setting-arrays) tag. You can also append `.count` to the [setting key](https://shopify.dev/docs/storefronts/themes/architecture/settings#access-settings) to return the number of articles in the array.

* `blank` if no selection has been made, the selection isn't visible, or the selection no longer exists

---

##### blog

A setting of type `blog` outputs a blog picker field that's automatically populated with the available blogs for the store. You can use this setting type to capture a blog selection, such as the blog to feature in the sidebar.

For example, the following setting generates the following output:

###### Setting

```json
{
  "type": "blog",
  "id": "blog",
  "label": "Blog"
}
```

###### Output

![blog setting](https://shopify.dev/assets/assets/images/themes/settings/specialized/blog-BVKhA-y3.png)

When accessing the value of a `blog` type setting, data is returned in one of the following formats:

* A [`blog` object](https://shopify.dev/docs/api/liquid/objects/blog).

To ensure backwards compatibility with [legacy resource-based settings](https://shopify.dev/docs/storefronts/themes/architecture/settings#legacy-resource-based-settings), outputting the setting directly will return the object's handle.

* `blank`, if either no selection has been made or the selection no longer exists.

**Note:**

Settings of type `blog` are not updated when switching presets. `blog` settings also don't support the `default` attribute.

---

##### collection

A setting of type `collection` outputs a collection picker field that's automatically populated with the available collections for the store. You can use this setting type to capture a collection selection, such as a collection for featuring products on the homepage.

For example, the following setting generates the following output:

###### Setting

```json
{
  "type": "collection",
  "id": "collection",
  "label": "Collection"
}
```

###### Output

![collection setting](https://shopify.dev/assets/assets/images/themes/settings/specialized/collection-Dbsx6Vk7.png)

When accessing the value of a `collection` type setting, data is returned in one of the following formats:

* A [`collection` object](https://shopify.dev/docs/api/liquid/objects/collection).

To ensure backwards compatibility with [legacy resource-based settings](https://shopify.dev/docs/storefronts/themes/architecture/settings#legacy-resource-based-settings), outputting the setting directly will return the object's handle.

* `blank`, if no selection has been made, the selection isn't visible, or the selection no longer exists.

**Note:**

Settings of type `collection` are not updated when switching presets. `collection` settings also don't support the `default` attribute.

---

##### collection_list

A setting of type `collection_list` outputs a collection picker field that's automatically populated with the available collections for the store. You can use this setting type to capture multiple collections, such as a group of collections to feature on the homepage.

In addition to the [standard attributes](#standard-attributes) of an input setting, `collection_list` type settings have the following attributes:

| Attribute | Description | Required |
| - | - | - |
| `limit` | The maximum number of collections that the merchant can select. The default limit, and the maximum limit you can set, is 50. | No |

###### Setting

```json
{
  "type": "collection_list",
  "id": "collection_list",
  "label": "Collections",
  "limit": 8
}
```

###### Output

![collection_list setting](https://shopify.dev/assets/assets/images/themes/settings/specialized/collection_list-DnN-pRRN.png)

###### Output

![collection_list setting selector](https://shopify.dev/assets/assets/images/themes/settings/specialized/collection_list-detail-DsUsWzFl.png)

When accessing the value of a `collection_list` type setting, data is returned in one of the following formats:

* An array of [`collection` objects](https://shopify.dev/docs/api/liquid/objects/collection)

The array supports pagination using the [paginate](https://shopify.dev/docs/api/liquid/tags/paginate#paginate-paginating-setting-arrays) tag. You can also append `.count` to the [setting key](https://shopify.dev/docs/storefronts/themes/architecture/settings#access-settings) to return the number of collections in the array.

* `blank` if no selection has been made, the selection isn't visible, or the selection no longer exists

---

##### color

A setting of type `color` outputs a color picker field. You can use this setting type to capture a color selection for various theme elements, such as the body text color.

For example, the following setting generates the following output:

###### Setting

```json
{
  "type": "color",
  "id": "body_text",
  "label": "Body text",
  "default": "#000000"
}
```

###### Output

![color setting picker](https://shopify.dev/assets/assets/images/themes/settings/specialized/color-DQX-ko7V.png)

When accessing the value of a `color` type setting, data is returned in one of the following formats:

* A [`color` object](https://shopify.dev/docs/api/liquid/objects/color).
* `blank`, if no selection has been made.

---

##### color_background

A setting of type `color_background` outputs a text field for entering [CSS background](https://developer.mozilla.org/en-US/docs/Web/CSS/background) properties. You can use this setting type to capture background settings for various theme elements, such as the store background.

**Caution:**

Settings of type `color_background` do not support image related background properties.

For example, the following setting generates the following output:

###### Setting

```json
{
  "type": "color_background",
  "id": "background",
  "label": "Background",
  "default": "linear-gradient(#ffffff, #000000)"
}
```

###### Output

![color_background setting input](https://shopify.dev/assets/assets/images/themes/settings/specialized/color-background-input-WkRtRyyo.png)

When accessing the value of a `color_background` type setting, data is returned in one of the following formats:

* A [string](https://shopify.dev/docs/api/liquid/basics/types#string).
* An empty string, if nothing has been entered.

---

##### color_scheme

A setting of type `color_scheme` outputs a picker with all of the available theme color schemes, and a preview of the selected color scheme. Theme color schemes in the picker are defined using the [`color_scheme_group`](#color_scheme_group) setting. You can apply a color scheme to sections, blocks and general theme settings. Color scheme settings aren't supported in app blocks.

For example, the following setting generates the following output:

###### Setting

```json
{
  "type": "color_scheme",
  "id": "color_scheme",
  "default": "scheme_1",
  "label": "Color scheme"
}
```

###### Output

![color scheme setting](https://shopify.dev/assets/assets/images/themes/settings/specialized/color_scheme-COyirGuy.png)

When accessing the value of a `color_scheme` type setting, Shopify returns the selected `color_scheme` object from `color_scheme_group`.

If no value was entered, or the value was invalid, then the default value from `color_scheme` is returned. If the default value is also invalid, then the first `color_scheme` from `color_scheme_group` is returned.

If the theme doesn't have `color_scheme_group` data in `settings_data.json`, then [nil](https://shopify.dev/docs/api/liquid/basics/types#nil) is returned.

---

##### color_scheme_group

A setting of type `color_scheme_group` outputs a color scheme which is composed of the following input setting types:

* `header`

* `color`

* `color_background`

Color schemes can be added only in `settings_schema.json`.

For example, the following setting generates the following output:

###### Setting

```json
{
  "type": "color_scheme_group",
  "id": "color_schemes",
  "definition": [
    {
      "type": "color",
      "id": "background",
      "label": "t:settings_schema.colors.settings.background.label",
      "default": "#FFFFFF"
    },
    {
      "type": "color_background",
      "id": "background_gradient",
      "label": "t:settings_schema.colors.settings.background_gradient.label",
      "info": "t:settings_schema.colors.settings.background_gradient.info"
    },
    {
      "type": "color",
      "id": "text",
      "label": "t:settings_schema.colors.settings.text.label",
      "default": "#121212"
    },
    {
      "type": "color",
      "id": "button",
      "label": "t:settings_schema.colors.settings.button_background.label",
      "default": "#121212"
    },
    {
      "type": "color",
      "id": "button_label",
      "label": "t:settings_schema.colors.settings.button_label.label",
      "default": "#FFFFFF"
    },
    {
      "type": "color",
      "id": "secondary_button_label",
      "label": "t:settings_schema.colors.settings.secondary_button_label.label",
      "default": "#121212"
    },
    {
      "type": "color",
      "id": "shadow",
      "label": "t:settings_schema.colors.settings.shadow.label",
      "default": "#121212"
    }
  ],
  "role": {
    "text": "text",
    "background": {
      "solid": "background",
      "gradient": "background_gradient"
    },
    "links": "secondary_button_label",
    "icons": "text",
    "primary_button": "button",
    "on_primary_button": "button_label",
    "primary_button_border": "button",
    "secondary_button": "background",
    "on_secondary_button": "secondary_button_label",
    "secondary_button_border": "secondary_button_label"
  }
}
```

###### Output

![color_scheme_group setting input](https://shopify.dev/assets/assets/images/themes/settings/specialized/color_scheme_group-COY53K7M.png)

###### role

The `role` field outputs a color scheme preview. The color scheme previews are visible to merchants anywhere in the editor where they might pick a color scheme. You can assign roles to your color scheme definitions to map the color scheme to the previews. For example you can assign `role.background` to the `Background` definition. Role uses the following standardized mapping of the `color_scheme_group` definition to the color scheme preview:

| Role | Description | Required? | Gradient? |
| - | - | - | - |
| `role.background` | Renders the background color of the preview | Yes | Optional |
| `role.text` | Renders the text color of the preview | Yes | No |
| `role.primary_button`, `role.secondary_button` | Render the 1st and 2nd pills in the preview | Yes | Optional |
| `role.primary_button_border`, `role.secondary_button_border` | Render the 1st and 2nd pills' border in the preview | Yes | No |
| `role.on_primary_button`, `role.on_secondary_button` | Aren't used in the preview | Yes | No |
| `role.links`, `role.icons` | Aren't used in the preview | Yes | No |

###### Output

![color scheme mapping](https://shopify.dev/assets/assets/images/themes/settings/specialized/color-scheme-mapping-WPDqcLK2.png)

---

##### font_picker

A setting of type `font_picker` outputs a font picker field that's automatically populated with fonts from the [Shopify font library](https://shopify.dev/docs/storefronts/themes/architecture/settings/fonts#shopify-font-library). This library includes system fonts and a selection of Google Fonts.

You can use this setting type to capture a font selection for various theme elements, such as the base heading font.

For example, the following setting generates the following output:

###### Setting

```json
{
  "type": "font_picker",
  "id": "heading_font",
  "label": "Heading font",
  "default": "helvetica_n4"
}
```

###### Output

![font setting](https://shopify.dev/assets/assets/images/themes/settings/specialized/font_picker-Dbgudqpj.png)

When accessing the value of a `font_picker` type setting, data is returned as a [`font` object](https://shopify.dev/docs/api/liquid/objects/font).

**Caution:**

The `default` attribute is required. Failing to include it will result in an error. You can find the possible values through the [available fonts](https://shopify.dev/docs/storefronts/themes/architecture/settings/fonts#available-fonts) in the Shopify font library.

---

##### html

A setting of type `html` outputs a multi-line text field that accepts HTML markup. In addition to the [standard attributes](#standard-attributes) of an input setting, `html` type settings have the following attribute:

| Attribute | Description | Required |
| - | - | - |
| `placeholder` | A placeholder value for the input | No |

You can use this setting type to capture custom blocks of HTML content, such as a video embed.

For example, the following setting generates the following output:

###### Setting

```json
{
  "type": "html",
  "id": "video_embed",
  "label": "Video embed"
}
```

###### Output

![html setting](https://shopify.dev/assets/assets/images/themes/settings/specialized/html-faprOLP2.png)

The following HTML tags will be automatically removed:

* `<html>`
* `<head>`
* `<body>`

When accessing the value of an `html` type setting, data is returned in one of the following formats:

* A [string](https://shopify.dev/docs/api/liquid/basics/types#string) that contains the entered content.
* An [`empty` object](https://shopify.dev/docs/api/liquid/basics/types#emptydrop), if nothing has been entered.

**Note:**

Unclosed HTML tags are automatically closed when the setting is saved. This may not line up with your intended formatting, so be sure to verify your input.

---

##### image_picker

A setting of type `image_picker` outputs an image picker field that's automatically populated with the available images from the [Files](https://help.shopify.com/manual/shopify-admin/productivity-tools/file-uploads) section of Shopify admin, and has the option to upload new images. Merchants also have an opportunity to enter alt text and select a [focal point](#image-focal-points) for their image.

You can use this setting type to capture an image selection, such as logos, favicons, and slideshow images.

For example, the following setting generates the following output:

###### Setting

```json
{
  "type": "image_picker",
  "id": "image_with_text_image",
  "label": "Image"
}
```

###### Output

![image setting](https://shopify.dev/assets/assets/images/themes/settings/specialized/image-C-_MRJC_.png)

###### Output (Preview and edit modal)

![image setting](https://shopify.dev/assets/assets/images/themes/settings/specialized/image_editor-DSyUvApw.png)

When accessing the value of an `image_picker` type setting, data is returned in one of the following formats:

* An [`image` object](https://shopify.dev/docs/api/liquid/objects/image).
* [nil](https://shopify.dev/docs/api/liquid/basics/types#nil), if either no selection has been made or the selection no longer exists.

**Note:**

Settings of type `image_picker` are not updated when switching presets. `image_picker` settings also don't support the `default` attribute.

###### Image focal points

Images selected using an `image_picker` setting support focal points. A focal point is a position in an image that the merchant wants to remain in view as the image is cropped and adjusted by the theme. Focal points can be set in the theme editor `image_picker` setting, or from the **Files** page.

To make sure that your theme respects the focal point of the image, do the following:

* Render your images using the [`image_tag`](https://shopify.dev/docs/api/liquid/filters/image_tag) filter.
* Consider positioning images within containers using `object-fit: cover`.

Using `image_tag`, if a focal point was provided, then an `object-position` style is added to the image tag, with the value set to the focal point.

###### Input

```liquid
{{ section.settings.image_with_text_image | image_url: width: 1500 | image_tag }}
```

###### Output

```html
<img src="/content/assets/images/octopus-tentacle.jpg?v=1&width=1500" alt="My alt text"
 srcset="octopus-tentacle.jpg?v=1&width=352 352w,
         octopus-tentacle.jpg?v=1&width=832 832w,
         octopus-tentacle.jpg?v=1&width=1200 1200w"
 width="1500" height="1875"
 style={{objectPosition: '25% 10%'}} />
```

If you need to override the `object-position` style for a specific use case, then pass a `style: object-position: inherit;` property to the `image_tag` filter.

**Tip:**

You can also access the focal point data using [`image.presentation.focal_point`](https://shopify.dev/docs/api/liquid/objects/image_presentation#image_presentation-focal_point).

---

##### inline_richtext

A setting of type `inline_richtext` outputs HTML markup that isn't wrapped in paragraph tags (`<p>`). The setting includes the following basic formatting options:

* Bold
* Italic
* Link

**Note:**

The `inline_richtext` setting doesn't support the following features:

* Line breaks (`<br />`)
* An underline option in the rich text editor. Merchants can underline text using the `Command+U` or `Control+U` keyboard shortcut.

You can use this setting type to capture formatted text content, such as introductory brand content on the homepage.

For example, the following setting generates the following output:

###### Setting

```json
{
  "type": "inline_richtext",
  "id": "inline",
  "default": "my <i>inline</i> <b>text</b>",
  "label": "Inline rich text"
}
```

###### Output

![inline_richtext setting](https://shopify.dev/assets/assets/images/themes/settings/specialized/inline_rich_text-DGwTH9yH.png)

When accessing the value of an `inline_richtext` type setting, data is returned in one of the following formats:

* A [string](https://shopify.dev/docs/api/liquid/basics/types#string) that contains the entered content.
* An [`empty` object](https://shopify.dev/docs/api/liquid/basics/types#emptydrop), if nothing has been entered.

---

##### link_list

A setting of type `link_list` outputs a menu picker field that's automatically populated with the available menus for the store. You can use this setting type to capture a menu selection, such as the menu to use for footer links.

For example, the following setting generates the following output:

###### Setting

```json
{
  "type": "link_list",
  "id": "menu",
  "label": "Menu"
}
```

###### Output

![link_list setting](https://shopify.dev/assets/assets/images/themes/settings/specialized/linklist-p6TUcGXd.png)

When accessing the value of a `link_list` type setting, data is returned in one of the following formats:

* A [`linklist` object](https://shopify.dev/docs/api/liquid/objects/linklist).
* `blank`, if either no selection has been made or the selection no longer exists.

**Note:**

Accepted values for the `default` attribute are `main-menu` and `footer`.

---

##### liquid

A setting of type `liquid` outputs a multi-line text field that accepts HTML and [limited](#limitations) Liquid markup. You can use this setting type to capture custom blocks of HTML and Liquid content, such as a product-specific message. Merchants can also use a liquid setting to add the code needed to integrate certain types of [apps](https://shopify.dev/docs/apps/build/online-store) into your theme.

For example, the following setting generates the following output:

###### Setting

```json
{
  "type": "liquid",
  "id": "battery_message",
  "label": "Battery message",
  "default": "{% if product.tags contains 'battery' %}This product can only be shipped by ground.{% else %}This product can be shipped by ground or air.{% endif %}"
}
```

###### Output

![liquid setting](https://shopify.dev/assets/assets/images/themes/settings/specialized/liquid-DT_qkQts.png)

When accessing the value of a `liquid` type setting, data is returned in one of the following formats:

* A [string](https://shopify.dev/docs/api/liquid/basics/types#string) that contains the entered content.
* An [`empty` object](https://shopify.dev/docs/api/liquid/basics/types#emptydrop), if nothing has been entered.

**Note:**

The `default` attribute is optional. However, if you use it, then its value can't be an empty string. Additionally, unclosed HTML tags are automatically closed when the setting is saved. This might not line up with your intended formatting, so be sure to verify your input.

###### Limitations

Settings of type `liquid` don't have access to the following liquid objects/tags:

* [layout](https://shopify.dev/docs/api/liquid/tags/layout)
* [content_for_header](https://shopify.dev/docs/api/liquid/objects/content_for_header)
* [content_for_layout](https://shopify.dev/docs/api/liquid/objects/content_for_layout)
* [content_for_index](https://shopify.dev/docs/api/liquid/objects/content_for_index)
* [section](https://shopify.dev/docs/api/liquid/tags/section)
* [javascript](https://shopify.dev/docs/storefronts/themes/best-practices/javascript-and-stylesheet-tags#javascript)
* [stylesheet](https://shopify.dev/docs/storefronts/themes/best-practices/javascript-and-stylesheet-tags#stylesheet)
* [schema](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema)
* [settings](https://shopify.dev/docs/api/liquid/objects/settings)

However, `liquid` settings can access the following:

* [Global Liquid objects](https://shopify.dev/docs/api/liquid/objects)
* Template specific objects like `collection`, `product`, etc. (within their respective templates)
* Standard Liquid [tags](https://shopify.dev/docs/api/liquid/tags) and [filters](https://shopify.dev/docs/api/liquid/filters)

If your content includes non-existent, or empty, Liquid tags, then they will be rendered as empty strings. For example, the following setting generates the following output:

###### Setting

```json
{
  "type": "liquid",
  "id": "message",
  "label": "Message",
  "default": "Hello {{ not_a_real_tag }}, welcome to our shop."
}
```

###### Output

```text
Hello , welcome to our shop.
```

**Caution:**

Content entered in these settings can't exceed 50kb. Saving content that either exceeds this limit or includes invalid Liquid will result in an error.

---

##### metaobject

A `metaobject` setting allows merchants to select metaobject entries of a designated type through a picker interface. This setting supports both standard and custom metaobject definitions:

1. Standard metaobject definitions: These are readily available in the theme editor and do not need to be pre-enabled on a shop. An example of a standard metaobject is the `product_review` metaobject. [Learn more](https://shopify.dev/docs/apps/build/custom-data/metaobjects/list-of-standard-definitions) about current standard metaobject definitions.
2. Custom metaobject definitions: These are designed for custom themes and require the metaobject definition to already exist. Note that custom metaobject definitions are not allowed in themes listed on the Theme Store. An example of a custom metaobject would be an `author` metaobject.

Additionally, apps can utilize `metaobject` settings with their own app-owned metaobject definitions and entries.

`metaobject` type settings have the following attributes, in addition to the [standard attributes](#standard-attributes) of an input setting:

| Attribute | Description | Required |
| - | - | - |
| `metaobject_type` | The metaobject type allowed by the picker. | Yes |

A `metaobject` setting value can be either of the following formats:

* A [`metaobject` object](https://shopify.dev/docs/api/liquid/objects/metaobject)
* `blank` if no selection has been made, the selection isn't visible, or the selection no longer exists

###### Standard metaobject example

###### Setting

```json
{
  "type": "metaobject",
  "id": "my_material_setting",
  "label": "Material",
  "metaobject_type": "shopify--material"
}
```

###### Output

![metaobject setting](https://shopify.dev/assets/assets/images/themes/settings/specialized/metaobject-DXxYCQH5.png)

###### Custom metaobject example

###### Setting

```json
{
  "type": "metaobject",
  "id": "my_artist",
  "label": "Artist",
  "metaobject_type": "artist"
}
```

###### Output

![metaobject setting](https://shopify.dev/assets/assets/images/themes/settings/specialized/custom_metaobject-BBO5BXOS.png)

###### Limitations

* Only a single `metaobject_type` is supported at a time, as defined in the setting's schema.
* In order for themes to meet [publishing guidelines](https://shopify.dev/docs/storefronts/themes/store/requirements#14-settings) for the Shopify Theme Store, only standard definitions can be used. Custom or app owned definitions cannot be used.
* When referencing a **custom** or **app created** `metaobject_type`, the definition must exist on the shop and be available to the storefront. If either condition isn't met, the setting will show an error in the theme editor.

![metaobject-missing-definition](https://shopify.dev/assets/assets/images/themes/settings/specialized/metaobject_error--DgB5sV3.png)

###### Usage in apps

Apps can leverage `metaobject` settings in their app blocks or embeds to enhance theme functionality. By creating metaobject definitions under [reserved namespaces](https://shopify.dev/docs/apps/build/custom-data/ownership#create-metaobject-definitions-with-reserved-types), apps can offer advanced configuration options for merchants while maintaining a simple user experience.

Consider an app designed to improve brand storytelling through customer testimonials. Here's a potential implementation:

1. Create a custom metaobject definition named `Customer Testimonial`
2. Use app blocks to collect customer data on a post-purchase page
3. Write this data as `Customer Testimonial` metaobject entries
4. Provide a `Testimonial` app block with a `metaobject` setting that uses the `Customer Testimonial` metaobject type
5. Access the `metaobject` setting value in Liquid to display the selected testimonials

###### Setting

```json
{
  "type": "metaobject",
  "id": "my_testimonial",
  "label": "Testimonial",
  "metaobject_type": "app--<appid>-testimonial"
}
```

---

##### metaobject_list

A `metaobject_list` setting allows merchants to select multiple metaobject entries of a designated type through a picker interface. This setting supports both standard and custom metaobject definitions:

1. Standard metaobject definitions: These are readily available in the theme editor and do not need to be pre-enabled on a shop. An example of a standard metaobject is the `product_review` metaobject. [Learn more](https://shopify.dev/docs/apps/build/custom-data/metaobjects/list-of-standard-definitions) about current standard metaobject definitions.
2. Custom metaobject definitions: These are designed for custom themes and require the metaobject definition to already exist. Note that custom metaobject definitions are not allowed in themes listed on the Theme Store. An example of a custom metaobject would be an `author` metaobject.

Additionally, apps can utilize `metaobject_list` settings with their own app-owned metaobject definitions and entries.

`metaobject_list` type settings have the following attributes, in addition to the [standard attributes](#standard-attributes) of an input setting:

| Attribute | Description | Required |
| - | - | - |
| `limit` | The maximum number of metaobject entries that the merchant can select. The default limit, and the maximum limit you can set, is 50. | No |
| `metaobject_type` | The metaobject type allowed by the picker. | Yes |

A `metaobject_list` setting value can be either of the following formats:

* An array of [`metaobject` objects](https://shopify.dev/docs/api/liquid/objects/metaobject)

  The array supports pagination using the [paginate](https://shopify.dev/docs/api/liquid/tags/paginate#paginate-paginating-setting-arrays) tag. You can also append `.count` to the [setting key](https://shopify.dev/docs/storefronts/themes/architecture/settings#access-settings) to return the number of metaobject entries in the array.

* `blank` if no selection has been made, the selection isn't visible, or the selection no longer exists

###### Standard metaobject list example

###### Setting

```json
{
  "type": "metaobject_list",
  "id": "my_material_list_setting",
  "label": "Materials",
  "metaobject_type": "shopify--material",
  "limit": 12
}
```

###### Output

![metaobject_list setting](https://shopify.dev/assets/assets/images/themes/settings/specialized/metaobject_list-BRPogIV_.png)

###### Custom metaobject list example

###### Setting

```json
{
  "type": "metaobject_list",
  "id": "my_artist_list",
  "label": "Artists",
  "metaobject_type": "artist",
  "limit": 12
}
```

###### Output

![metaobject_list setting](https://shopify.dev/assets/assets/images/themes/settings/specialized/custom_metaobject_list-D_xebCul.png)

###### Limitations

* Only a single `metaobject_type` is supported at a time, as defined in the setting's schema.
* In order for themes to meet [publishing guidelines](https://shopify.dev/docs/storefronts/themes/store/requirements#14-settings) for the Shopify Theme Store, custom or app owned definitions cannot be used.
* When referencing a **custom** or **app created** `metaobject_type`, the definition must exist on the shop and be available to the storefront. If either condition isn't met, the setting will show an error in the theme editor.

![metaobject-list-missing-definition](https://shopify.dev/assets/assets/images/themes/settings/specialized/metaobject_error--DgB5sV3.png)

###### Usage in apps

Apps can leverage `metaobject_list` settings in their app blocks or embeds to enhance theme functionality. By creating metaobject definitions under [reserved namespaces](https://shopify.dev/docs/apps/build/custom-data/ownership#create-metaobject-definitions-with-reserved-types), apps can offer advanced configuration options for merchants while maintaining a simple user experience. Using the same [example](#metaobject) as above, a `Testimonials` app-block could allow merchants to select multiple testimonial entries. The `metaobject_list` setting would make this implementation possible.

###### Setting

```json
{
  "type": "metaobject_list",
  "id": "my_testimonial_list",
  "label": "Testimonials list",
  "metaobject_type": "app--<appid>-testimonial",
  "limit": 12
}
```

---

##### page

A setting of type `page` outputs a page picker field that's automatically populated with the available pages for the store. You can use this setting type to capture a page selection, such as the page to feature content for in a size-chart display.

For example, the following setting generates the following output:

###### Setting

```json
{
  "type": "page",
  "id": "page",
  "label": "Page"
}
```

###### Output

![page setting](https://shopify.dev/assets/assets/images/themes/settings/specialized/page-DY3jU_ff.png)

When accessing the value of a `page` type setting, data is returned in one of the following formats:

* A [`page` object](https://shopify.dev/docs/api/liquid/objects/page).

To ensure backwards compatibility with [legacy resource-based settings](https://shopify.dev/docs/storefronts/themes/architecture/settings#legacy-resource-based-settings), outputting the setting directly will return the object's handle.

* `blank`, if no selection has been made, the selection isn't visible, or the selection no longer exists.

**Note:**

Settings of type `page` are not updated when switching presets. `page` settings also don't support the `default` attribute.

---

##### product

A setting of type `product` outputs a product picker field that's automatically populated with the available products for the store. You can use this setting type to capture a product selection, such as the product to feature on the homepage.

For example, the following setting generates the following output:

###### Setting

```json
{
  "type": "product",
  "id": "product",
  "label": "Product"
}
```

###### Output

![product setting](https://shopify.dev/assets/assets/images/themes/settings/specialized/product-BU89p2xJ.png)

When accessing the value of a `product` type setting, data is returned in one of the following formats:

* A [`product` object](https://shopify.dev/docs/api/liquid/objects/product).

To ensure backwards compatibility with [legacy resource-based settings](https://shopify.dev/docs/storefronts/themes/architecture/settings#legacy-resource-based-settings), outputting the setting directly will return the object's handle.

* `blank` if no selection has been made, the selection isn't visible, or the selection no longer exists

**Note:**

Settings of type `product` are not updated when switching presets. `product` settings also don't support the `default` attribute.

---

##### product_list

A setting of type `product_list` outputs a product picker field that's automatically populated with the available products for the store. You can use this setting type to capture multiple products, such as a group of products to feature on the homepage.

**Note:**

You can only choose from products that are published to the online store and have an `active` status.

In addition to the [standard attributes](#standard-attributes) of an input setting, `product_list` type settings have the following attributes:

| Attribute | Description | Required |
| - | - | - |
| `limit` | The maximum number of products that the merchant can select. The default limit, and the maximum limit you can set, is 50. | No |

###### Setting

```json
{
  "type": "product_list",
  "id": "product_list",
  "label": "Products",
  "limit": 12
}
```

###### Output

![product_list setting](https://shopify.dev/assets/assets/images/themes/settings/specialized/product_list-CLbCBDvu.png)

When accessing the value of a `product_list` type setting, data is returned in one of the following formats:

* An array of [`product` objects](https://shopify.dev/docs/api/liquid/objects/product)

The array supports pagination using the [paginate](https://shopify.dev/docs/api/liquid/tags/paginate#paginate-paginating-setting-arrays) tag. You can also append `.count` to the [setting key](https://shopify.dev/docs/storefronts/themes/architecture/settings#access-settings) to return the number of products in the array.

* `blank` if no selection has been made, the selection isn't visible, or the selection no longer exists

---

##### richtext

A setting of type `richtext` outputs a multi-line text field with the following basic formatting options:

* Bold
* Italic
* Underline
* Link
* Paragraph
* Unordered list

**Note:**

No underline option appears in the rich text component. Merchants can underline text using the `Command+U` or `Control+U` keyboard shortcut.

You can use this setting type to capture formatted text content, such as introductory brand content on the homepage.

For example, the following setting generates the following output:

###### Setting

```json
{
  "type": "richtext",
  "id": "paragraph",
  "label": "Paragraph"
}
```

###### Output

![richtext setting](https://shopify.dev/assets/assets/images/themes/settings/specialized/richtext-CdgN-WUR.png)

When accessing the value of a `richtext` type setting, data is returned in one of the following formats:

* A [string](https://shopify.dev/docs/api/liquid/basics/types#string) that contains the entered content.
* An [`empty` object](https://shopify.dev/docs/api/liquid/basics/types#emptydrop), if nothing has been entered.

###### default

The `default` attribute isn't required. However, if it's used, then only `<p>` or `<ul>` tags are supported as top-level elements.

The following HTML tags are also supported inside the parent `<p>` tag:

* `<p>`
* `<br />`
* `<strong>`
* `<b>`
* `<em>`
* `<i>`
* `<u>`
* `<span>`
* `<a>`

**Caution:**

Failing to wrap the `default` content in `<p>` or `<ul>` tags will result in an error.

---

##### text_alignment

A setting of type `text_alignment` outputs a `SegmentedControl` field with icons. In addition to the [standard attributes](#standard-attributes) of an input setting, `text_alignment` type settings support the following attribute:

| Attribute | Description | Required |
| - | - | - |
| Default | The initially selected value. Can be one of `left`, `right`, `center`. The default value is `left`. | No |

The following default values can't be changed to a different value:

| Value | Icon presentation |
| - | - |
| Left | ![](https://shopify.dev/assets/assets/images/themes/settings/specialized/text-alignment-left-AHfF-UoS.png) |
| Right | ![](https://shopify.dev/assets/assets/images/themes/settings/specialized/text-alignment-right-BKQxxcoT.png) |
| Center | ![](https://shopify.dev/assets/assets/images/themes/settings/specialized/text-alignment-center-DQNO6R-L.png) |

For example, the following setting generates the following output:

###### Setting

```json
{
   "type": "text_alignment",
   "id": "alignment",
   "label": "Text alignment",
   "default": "center"
}
```

###### Output

![text_alignment setting](https://shopify.dev/assets/assets/images/themes/settings/specialized/text-alignment-DidZPfbN.png)

When you access the value of a `text_alignment` type setting, data is returned as a [string](https://shopify.dev/docs/api/liquid/basics/types#string).

**Note:**

If you don't specify the default attribute, then the `left` option is selected by default.

---

##### url

A setting of type `url` outputs a URL entry field where you can manually enter external URLs and relative paths. It also has a picker that's automatically populated with the following available resources for the shop:

* Articles
* Blogs
* Collections
* Pages
* Products

You can use this setting type to capture a URL selection, such as the URL to use for a slideshow button link.

For example, the following setting generates the following output:

###### Setting

```json
{
  "type": "url",
  "id": "button_link",
  "label": "Button link"
}
```

###### Output

![url setting](https://shopify.dev/assets/assets/images/themes/settings/specialized/url-Cf6Ul31I.png)

When accessing the value of a `url` type setting, data is returned in one of the following formats:

* A [string](https://shopify.dev/docs/api/liquid/basics/types#string) that contains the selected URL.
* [nil](https://shopify.dev/docs/api/liquid/basics/types#nil), if nothing has been entered.

**Note:**

Accepted values for the `default` attribute are `/collections` and `/collections/all`.

---

##### video

A setting of type `video` outputs a video picker that's automatically populated with the available videos from the [Files](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads) section of the Shopify admin. The merchant also has the option to upload new videos.

For example, the following setting generates the following output:

###### Setting

```json
{
  "type": "video",
  "id": "video",
  "label": "A Shopify-hosted video"
}
```

###### Output

![video setting](https://shopify.dev/assets/assets/images/themes/settings/specialized/video-BCdU4jwk.png)

The `video` type setting also accepts metafields of type `file_reference` as a [dynamic source](https://shopify.dev/docs/storefronts/themes/architecture/settings/dynamic-sources).

When accessing the value of a `video` type setting, data is returned in one of the following formats:

* A [`video` object](https://shopify.dev/docs/api/liquid/objects#video).

* [nil](https://shopify.dev/docs/api/liquid/basics/types#nil), if:

  * no selection has been made,
  * the selection no longer exists, or
  * the selection is a `file_reference` metafield that points to a non-video file.

**Note:**

`video` settings don't support the `default` attribute.

---

##### video_url

A setting of type `video_url` outputs a URL entry field. In addition to the [standard attributes](#standard-attributes) of an input setting, `video_url` type settings have the following attributes:

| Attribute | Description | Required |
| - | - | - |
| `accept` | Takes an array of accepted video providers. Valid values are `youtube`, `vimeo`, or both. | Yes |
| `placeholder` | A placeholder value for the input. | No |

This setting type can be used to capture a video URL from YouTube and/or Vimeo, such as the URL for a static video to show in the product description.

For example, the following setting generates the following output:

###### Setting

```json
{
  "type": "video_url",
  "id": "product_description_video",
  "label": "Product description video",
  "accept": [
    "youtube",
    "vimeo"
  ]
}
```

###### Output

![video_url setting](https://shopify.dev/assets/assets/images/themes/settings/specialized/video_url-DL7LUFoz.png)

When accessing the value of a `video_url` type setting, data is returned in one of the following formats:

* A [string](https://shopify.dev/docs/api/liquid/basics/types#string) that contains the entered URL.
* [nil](https://shopify.dev/docs/api/liquid/basics/types#nil), if nothing has been entered.

Additionally, there's access to the `id` and `type` (YouTube or Vimeo) of the video.

For example, assuming you're using [this video](https://www.youtube.com/watch?v=_9VUPq3SxOc) with the above setting, the following Liquid generates the following output:

###### Setting

```liquid
ID: {{ settings.product_description_video.id }}
Type: {{ settings.product_description_video.type }}
```

###### Output

```text
ID: _9VUPq3SxOc
Type: youtube
```

---

##### Create links

You can [add links](https://www.markdownguide.org/basic-syntax/#links) to the `info` settings attribute by enclosing the link text in brackets and then following it immediately with the URL in parentheses.

For example, the following setting generates the following output:

###### Settings

```json
{
  "type": "checkbox",
  "id": "enable_payment_button",
  "label": "Show dynamic checkout button",
  "info": "Each customer will see their preferred payment method [Learn more](https://help.shopify.com/manual/online-store/dynamic-checkout)",
  "default": true
}
```

###### Output

![link setting](https://shopify.dev/assets/assets/images/themes/create_links_input-BXi7gx1l.png)

---


### 2.8.2 Sidebar settings

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/settings/sidebar-settings

#### Sidebar settings

Sidebar settings function as informational elements that "can't hold a value and aren't configurable." Their primary purpose is organizing and providing context for input settings.

##### Available Types

Two sidebar setting types exist:

* header
* paragraph

Both are composed of standard attributes and serve organizational purposes rather than collecting data.

> **Tip:** For actual input settings like checkboxes, refer to Input settings documentation.

---

##### Standard attributes

All sidebar settings share these attributes:

| Attribute | Description | Required |
|-----------|-------------|----------|
| `type` | The setting type: either `header` or `paragraph` | Yes |
| `content` | The content displayed in the theme editor | Yes |

---

##### header

The `header` type "outputs a header element to help you better organize your input settings."

Additional attribute:

| Attribute | Description | Required |
|-----------|-------------|----------|
| `info` | Optional informational text about the setting | No |

**Example**

```json
{
  "type": "header",
  "content": "Email Signup",
  "info": "Subscribers added automatically to your \"accepted marketing\" customer list. [Learn more](https://help.shopify.com/manual/customers/manage-customers)"
}
```

---

##### paragraph

The `paragraph` type "outputs a text element to help you better describe your input settings."

**Example**

```json
{
  "type": "paragraph",
  "content": "All of your collections are listed by default. To customize your list, choose 'Selected' and add collections."
}
```

---

##### Create links

Links can be added to the `info` attribute using standard markdown syntax: `[link text](URL)`.

**Example**

```json
{
  "type": "checkbox",
  "id": "enable_payment_button",
  "label": "Show dynamic checkout button",
  "info": "Each customer will see their preferred payment method [Learn more](https://help.shopify.com/manual/online-store/dynamic-checkout)",
  "default": true
}
```

### 2.8.3 Dynamic data sources

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/settings/dynamic-sources

#### Dynamic data sources

Dynamic data sources, also known as dynamic sources, allow merchants to connect input settings to data coming from resources such as products, collections, blogs, and pages as well as metafields and metaobjects.

Dynamic sources are connected using section and block settings. Merchants can make these connections in the theme editor

A dynamic source can be either:

* A resource attribute
* A metafield value

**Note:**

Dynamic sources aren't available for general theme settings.

---

##### Dynamic source type availability

Shopify determines the value of each available dynamic source type based on the following:

* The resource associated with the template that the section is in
* The resource settings in the context of the current setting
* Any metaobjects with storefront visibility and compatible fields
* Brand attributes
* Market-specific metafields and metaobjects

| Conditions | Description |
| - | - |
| The section is included as part of the product template | Metafields and attributes related to the product will be available for the following: * The section's settings * The settings for any block in the section |
| The section includes a collection type setting | Metafields and attributes related to the collection will be available for the following: * The section's settings * The settings for any block in the section |
| Theme Blocks product type setting | Theme Blocks access the closest resource which matches a resources of specified type. In this case, the nearest product type setting. |
| The section's blocks include a product type setting | Metafields and attributes for that product will be available for the block's settings. |
| Globally available metaobjects | Metaobjects with storefront visibility will be available as dynamic sources for any theme setting |

---

##### Available Shopify resources and attributes

The following table lists the available Shopify resources and their associated attributes:

| Resource | Attributes |
| - | - |
| product | `title`, `vendor`, `description`, `url`, `featured_image`, `collections` |
| collection | `title`, `image`, `description`, `url`, `products` |
| page | `title`, `url`, `content` |
| article | `title`, `url`, `author`, `content`, `excerpt`, `comments_count`, `image` |
| blog | `title`, `url` |

**Note:**

More resources and resource attributes will become available in the future.

---

##### Metafield and input setting compatibility

Metafields allow merchants to define custom data. The metafields can be connected to sections and blocks using settings in the theme editor.

The following outlines which setting and metafield types are compatible:

| Setting | Metafield(s) | Metafield validation options |
| - | - | - |
| `article` | `article_reference` | |
| `collection` | `collection_reference` | |
| `collection_list` | `list.collection_reference` | |
| `color` | `color` | |
| `image_picker` | `file_reference` | |
| `page` | `page_reference` | |
| `product` | `product_reference` | |
| `product_list` | `list.product_reference` | |
| `richtext` | `single_line_text_field`, `list.single_line_text_field`, `multi_line_text_field`, `rich_text_field`, `number_integer`, `number_decimal`, `date`, `date_time`, `weight`, `volume`, `dimension`, `rating`, `money`, `link` | |
| `inline_richtext` | `single_line_text_field`, `list.single_line_text_field`, `number_integer`, `number_decimal`, `date`, `date_time`, `weight`, `volume`, `dimension`, `rating`, `money`, `link` | |
| `text` | `single_line_text_field`, `list.single_line_text_field`, `number_integer`, `number_decimal`, `date`, `date_time`, `weight`, `volume`, `dimension`, `rating`, `money` | |
| `url` | `url` | |
| `video` | `file_reference` | Must accept video file types |
| `metaobject` | `metaobject_reference` | Must be of the same metaobject type as in the setting's schema. |
| `metaobject_list` | `list.metaobject_reference` | Must be of the same metaobject type as in the setting's schema. |

###### Referencing metaobject fields

You can use dynamic sources to connect metaobject fields to settings. Metaobjects can be referenced in two ways:

1. Directly as a dynamic source when the metaobject has storefront visibility and compatible fields (also referred to as globally available metaobjects)
2. Through a `metaobject_reference` metafield

When selecting a metaobject as a dynamic source, users can select any field that is compatible with the setting type. For example, if a metaobject has a `text` field and an image field, a `text` setting could use the `text` field as a dynamic source, while an `image_picker` setting could use the image field.

In the case of a `list.metaobject_reference`, the metaobject entries attached to the resource are iterated over, and for each metaobject, the selected field's value is displayed in a list. The values are displayed as a list of the selected field's type. For example, if the selected metaobject field is of type `single_line_text_field`, then the values are returned as `list.single_line_text_field`.

**Example**

A merchant has a `list.metaobject_reference` metafield that references a **Materials** metaobject. Each metaobject has a field called **Material name**.

You can assign the materials by name to the product in the **Metafields** section.

In the online store editor, any setting that supports `list.single_line_text_field`, such as a rich text field, can use dynamic sources to select the **Material name** field as a text source. This outputs a list of the material names associated with the current product.

---

##### Default values

You can configure a setting's default value to reference a dynamic source. However, only do this if you're rendering a section or block in a context where the dynamic source value exists. For example, don't use a product-related value in a section that:

* Can be rendered in non-product templates
* Doesn't explicitly have a `product` type setting to provide the necessary value

**Note:**

This also applies to setting values in presets.

Additional Liquid is invalid when using this method, so you can only reference the value directly. If you include additional Liquid, then you'll get an error.

The following is an example of a `default` setting that references a dynamic source:

```json
{
  "type": "text",
  "id": "featured_product_title",
  "label": "Featured product title",
  "default": "Featuring: {{ product.title }}"
}
```

---

##### Limits

Shopify limits the number of dynamic sources that you can use in different areas of your theme. These limits help to keep the theme performant.

| Description | Limit |
| - | - |
| Dynamic sources in a JSON template | 100 |
| Dynamic sources in general theme settings | 100 |
| Dynamic sources in a section group | 100 |
| Dynamic sources in a single setting | 50 |
| Dynamic sources in a static section | 50 |

### 2.8.4 Fonts

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/settings/fonts

#### Fonts

You can add fonts to your theme in the following ways:

* Use fonts from [Shopify's font library](#shopify-font-library)
* Use [custom fonts](#custom-fonts)

**Tip:**

In general, fonts are a separate resource that need to be downloaded by the browser before any text is rendered, which impacts a store's overall performance. To make the theme more performant, system fonts that are already installed on the customers computer can be used by merchants that choose fonts from the **System fonts** category of the Shopify font library.

---

##### Shopify font library

Shopify's font library is a collection of fonts that includes system fonts and a selection of Google fonts. These fonts are free to use on all Shopify online stores, and are provided in both [WOFF](https://caniuse.com/#feat=woff) and [WOFF2](https://caniuse.com/#feat=woff2) formats.

The files for each font include the following Unicode ranges, if the ranges are available for the font:

* [Basic Latin](https://www.unicode.org/charts/PDF/U0000.pdf)
* [Latin-1 Supplement](https://www.unicode.org/charts/PDF/U0080.pdf)
* [Latin Extended-A](https://www.unicode.org/charts/PDF/U0100.pdf)
* [Currency Symbols](https://www.unicode.org/charts/PDF/U20A0.pdf)

A limited number number of fonts also include the CJK Unicode ranges used in Japanese writing (e.g. [CJK Unified Ideographs](https://unicode.org/charts/PDF/U4E00.pdf)).

This selection of fonts covers a broad range of use cases. However, due to licensing restrictions, there are some fonts that Shopify can't include. If you need to use a broader range of characters, then you can use system fonts, [Typekit](https://fonts.adobe.com/typekit), and other solutions.

To learn more about using Shopify's font library, refer to Add Shopify fonts to your theme.

**Note:**

Personal access to the font files isn't currently available.

---

##### System fonts

System fonts are fonts that are already installed on a user's computer. This removes the need for browsers to download the font before rendering text and makes the theme more performant. System fonts are listed with the available fonts, noted with a `System` badge, and will show under the **System fonts** category in the theme editor font picker.

If you choose to use system fonts, then the font that's used to render text will depend on the user's operating system. There are three generic system font types. The following are examples of fonts within those types:

* `mono` - Menlo, Consolas, Monaco, Liberation Mono, and Lucida Console
* `sans-serif` - Helvetica, and Arial
* `serif` - Iowan Old Style, Apple Garamond, Baskerville, Times New Roman, Droid Serif, Times, and Source Serif Pro
* `system-ui` - San Francisco, Segoe UI, Roboto, Helvetica Neue, Noto Sans, Liberation Sans, and Arial

---

##### Custom fonts

If you want to use a font that's not included in Shopify's font library, then you can use fonts from third party solutions like [Typekit](https://fonts.adobe.com/typekit).

With most third party font solutions, you have the following options for including the font in your theme:

* Reference the font through the third party's hosting
* Upload the font files to your theme

If you include custom fonts in your theme and want to provide merchants with the ability to choose the font, then you need to create a setting for the selection, such as a [select setting](https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings#select). You can then reference the setting value in your CSS when defining which font to use for the associated elements.

###### Third party hosted fonts

If a font is hosted with the third party, then they'll usually provide a `<link>` tag to include the font in your theme:

```html
<link rel="stylesheet" href="[font-url]">
```

**Tip:**

The `<link>` tag is often included in `theme.liquid`, or your chosen [layout](https://shopify.dev/docs/storefronts/themes/architecture/layouts) file.

###### Host fonts in your theme

If you have your own font files, then follow these steps to include the font in your theme:

**Non-admin**

If you're planning on pushing your theme to a store using Shopify CLI, uploading a theme ZIP file, using the Shopify GitHub integration, or distributing the font with a theme through the Shopify Theme Store, then you should store the font in the [assets](https://shopify.dev/docs/storefronts/themes/architecture#assets) folder of the theme. These steps should be performed in a local code editor, not the Shopify admin code editor.

1. Add the font files to the [assets directory](https://shopify.dev/docs/storefronts/themes/architecture#assets).

2. Create a `@font-face` CSS rule so that you can reference the font. Use the [`asset_url` filter](https://shopify.dev/docs/api/liquid/filters/asset_url) to output the URL for the font file:

   ```liquid
   @font-face {
     font-family: "Font name";
     src: url("{{ '[font-file-name]' | asset_url }}") format("[font-format]");
   }
   ```

**Shopify admin**

If you want to add a font to an existing theme through the Shopify admin, then you should store your font in the [Files](https://help.shopify.com/manual/shopify-admin/productivity-tools/file-uploads) section of the Shopify admin. This is because uploading some types of fonts to the `assets` directory through the Shopify admin code editor might lead to file corruption.

1. Upload the font files to the **Content** > [**Files**](https://shopify.com/admin/content/files) section of the Shopify admin.

2. Create a `@font-face` CSS rule so that you can reference the font. Use the [`file_url` filter](https://shopify.dev/docs/api/liquid/filters#file_url) to output the URL for the font file:

   ```liquid
   @font-face {
     font-family: "Font name";
     src: url("{{ '[font-file-name]' | file_url }}") format("[font-format]");
   }
   ```

---

##### Add Shopify fonts to your theme

The following outlines how to use fonts from the Shopify font library in your theme:

1. Add a [font_picker](https://shopify.dev/docs/themes/architecture/settings/input-settings#font_picker) type setting to allow merchants to choose their font in the theme editor. The value of this setting is returned as a [`font` object](https://shopify.dev/docs/api/liquid/objects/font).
2. Use one of the following [font filters](https://shopify.dev/docs/api/liquid/filters/font-filters) to load the chosen font, or any of its variants:

   * Use the [font_face](https://shopify.dev/docs/api/liquid/filters/font_face) filter to insert the default `@font-face` declaration.
   * Use the [font_url](https://shopify.dev/docs/api/liquid/filters/font_url) filter to access a CDN URL, so that you can create a custom `@font-face` declaration.
   * Use the [font_modify](https://shopify.dev/docs/api/liquid/filters/font_modify) filter to access font variants of the same family. Examples are bold and italic stylings.

3. Reference the chosen font to set any specific CSS stylings, such as [font-family](https://developer.mozilla.org/en-US/Web/CSS/font-family), [font-weight](https://developer.mozilla.org/en-US/Web/CSS/font-weight), and [font-style](https://developer.mozilla.org/en-US/Web/CSS/font-style).

---

##### Available fonts

> Nota di estrazione: questa pagina contiene un elenco molto lungo e auto-generato di tutti i singoli handle dei font disponibili nella libreria Shopify (centinaia di voci come `assistant_n4`, `helvetica_n4`, ecc.). L'elenco completo non è riprodotto qui per dimensione; fa fede la fonte: https://shopify.dev/docs/storefronts/themes/architecture/settings/fonts#available-fonts

---

##### Deprecated fonts

As part of a broader move towards open-source fonts, and in an effort to refine our font offerings, we have deprecated some fonts in our library.

| Font family | Handles | Replacement |
| - | - | - |
| Agmena | `agmena_n3 agmena_i3 agmena_n4 agmena_i4 agmena_n6 agmena_i6 agmena_n7 agmena_i7` | Alegreya |
| Akko | `akko_n2 akko_i2 akko_n3 akko_i3 akko_n4 akko_i4 akko_n5 akko_i5 akko_n7 akko_i7 akko_n9 akko_i9` | Titillium Web |
| Alfie | `alfie_n4` | Handlee |
| Americana | `americana_n4 americana_i4 americana_n7 americana_n8` | Trirong |
| Antique Olive | `antique_olive_n3 antique_olive_n4 antique_olive_i4 antique_olive_n7 antique_olive_n9` | Anek Tamil |
| Armata | `armata_n4` | Titillium Web |
| Avenir Next | `avenir_next_n1 avenir_next_i1 avenir_next_n2 avenir_next_i2 avenir_next_n3 avenir_next_i3 avenir_next_n4 avenir_next_i4 avenir_next_n5 avenir_next_i5 avenir_next_n6 avenir_next_i6 avenir_next_n7 avenir_next_i7 avenir_next_n8 avenir_next_i8` | Figtree |

> Nota: la tabella dei font deprecati prosegue oltre queste voci. L'elenco completo delle famiglie deprecate, dei loro handle e dei font sostitutivi è disponibile alla fonte: https://shopify.dev/docs/storefronts/themes/architecture/settings/fonts#deprecated-fonts

---

## 2.9 Config

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/config

### Config

Config files define settings in the **Theme settings** area of the theme editor, as well as store their values.

Theme settings are a good place to host general settings such as typography and color options. Theme settings can be accessed through the settings object.

**Tip:**

You can also create settings for sections and blocks. These settings are defined as part of the parent section or block object, and appear in the theme editor with the associated object.

---

#### Location

Config files are located in the `config` directory of the theme. When the theme contains market-specific customizations, the `markets.json` file is present in this directory:

```text
└── theme
  ...
  ├── config
  |   ├── settings_data.json
  |   ├── settings_schema.json
  |   └── markets.json
  └── locales
```

---

#### Subtypes

There are up to three config files, each with their own schema and content:

| Type | Description | Required |
| - | - | - |
| **settings_schema.json** | Controls the organization and content of the **Theme settings** area of the theme editor. | Yes |
| **settings_data.json** | Contains the saved values from the settings in `settings_schema.json`. | Yes |
| **markets.json** | Sets the source of inheritance of market-specific theme customizations. | No |

---

#### Usage

When working with config files, you should familiarize yourself with the following:

* Setting types
* Accessing settings
* Theme metadata

##### Setting types

There are two categories of settings:

| Category | Description |
| - | - |
| Input settings | Settings that can hold a value, and are configurable by app users. |
| Sidebar settings | Settings that can't hold a value, and aren't configurable by app users. They're informational elements that can be used to provide detail and clarity for your input settings. |

##### Access settings

Theme settings can be accessed through the settings object. To learn more about the syntax and considerations, refer to documentation on accessing settings.

##### Theme metadata

You can add theme metadata to the **Theme actions** menu of the theme editor. This includes information like the theme name and version, where to find theme documentation, and theme developer contact details. To learn how to include this information in your theme, refer to the settings schema JSON documentation.

### 2.9.1 settings_schema.json

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/config/settings-schema-json

#### settings_schema.json

The `settings_schema.json` file controls the organization and content of the **Theme settings** area of the theme editor. All setting selections in the theme editor are saved in [settings_data.json](https://shopify.dev/docs/storefronts/themes/architecture/config/settings-data-json).

---

##### Location

The `settings_schema.json` file is located in the `config` directory of the theme:

```text
└── theme
  ...
  ├── config
  |   ├── settings_data.json
  |   ├── settings_schema.json
  |   └── markets.json
  └── locales
```

---

##### Schema

The `settings_schema.json` file is an array of objects that represent setting categories. Each object needs to have the following attributes:

| Attribute | Description | Required |
| - | - | - |
| `name` | The name of the category of settings. | Yes |
| `settings` | An array of associated [settings](https://shopify.dev/docs/storefronts/themes/architecture/settings). | Yes |

The `settings_schema.json` file should follow the following basic format:

```json
[
{
  "name": "Category",
  "settings": [
    ...
  ]
},
...
]
```

The `settings_schema.json` file is a JSON file, so all content must be valid JSON. Additionally, make sure you follow the appropriate syntax for your desired setting.

---

##### Usage

When working with the `settings_schema.json` file, familiarize yourself with the following:

* setting types
* accessing settings
* adding theme metadata

###### Setting types

There are two categories of settings:

| Category | Description |
| - | - |
| [Input settings](https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings) | Settings that can hold a value, and are configurable by app users. |
| [Sidebar settings](https://shopify.dev/docs/storefronts/themes/architecture/settings/sidebar-settings) | Settings that can't hold a value, and aren't configurable by app users. They're informational elements that can be used to provide detail and clarity for your input settings. |

###### Access settings

Theme settings can be accessed through the [settings object](https://shopify.dev/docs/api/liquid/objects/settings). To learn more about the syntax and considerations, refer to [Access settings](https://shopify.dev/docs/storefronts/themes/architecture/settings#access-settings).

###### Add theme metadata

As a theme author, you can include additional metadata for your theme in the **Theme actions** menu of the theme editor. This menu appears at the left of the theme editor top bar.

To add this metadata, you can include a `theme_info` object in the `settings_schema.json` file. This object must include the following attributes:

| Attribute | Description | Required |
| - | - | - |
| `name` | The value of this attribute must be `theme_info`. | Yes |
| `theme_name` | The name of the theme. | Yes |
| `theme_author` | The author of the theme. | Yes |
| `theme_version` | The version number of the theme. | Yes |
| `theme_documentation_url` | A URL where merchants can find documentation for the theme. | Yes |
| `theme_support_email` | An email address that merchants can contact for support for the theme. | See note |
| `theme_support_url` | A URL where merchants can find support for the theme. | See note |

**Caution:**

All of the above attributes are required. However, you need to specify only `theme_support_email` or `theme_support_url`, not both. Including both of these attributes, or excluding any other attributes, will result in an error.

For example:

```json
[
  {
    "name": "theme_info",
    "theme_name": "Dawn",
    "theme_author": "Shopify",
    "theme_version": "1.0.0",
    "theme_documentation_url": "https://help.shopify.com/manual/online-store/themes/os20/themes-by-shopify/dawn",
    "theme_support_url": "https://support.shopify.com/"
  },
  ...
]
```

### 2.9.2 settings_data.json

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/config/settings-data-json

#### settings_data.json

The `settings_data.json` file contains the setting values for a theme based on the settings included in [settings_schema.json](https://shopify.dev/docs/storefronts/themes/architecture/config/settings-schema-json).

For example, you can use the following theme setting to allow a merchant to choose a color for the page background:

**config/settings_schema.json**

```json
{
  "name": "Colors",
  "settings": [
    {
      "type": "color",
      "id": "color_page_bg",
      "label": "Page background",
      "default": "#FFFFFF"
    }
  ]
}
```

This adds an entry for `color_page_bg` in `settings_data.json`:

**config/settings_data.json**

```json
...
"color_page_bg": "#FFFFFF"
...
```

**Tip:**

In this example, the value of `color_page_bg` is `#FFFFFF` due to the [default](https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings#standard-attributes) setting attribute.

Any time that the value of `color_page_bg` is changed in the theme editor, `settings_data.json` is updated with the new value.

---

##### Location

The `settings_data.json` file is located in the `config` directory of the theme:

```text
└── theme
  ...
  ├── config
  |   ├── settings_data.json
  |   ├── settings_schema.json
  |   └── markets.json
  └── locales
```

---

##### Schema

The `settings_data.json` file has the following parent objects:

| Object | Description | Required |
| - | - | - |
| `current` | Contains all of the setting values that are currently saved in the theme editor. | Yes |
| `presets` | Contains an object for each [theme preset](#theme-presets). Each object is in the same format as `current`. | Yes |
| `platform_customizations` | Contains setting values for [platform-controlled settings](#platform-controlled-settings). | No - this object is added by Shopify if a merchant uses a platform-controlled setting. |

For example:

```json
{
"current": {
  "color_page_bg": "#FFFFFF",
  ...
},
"presets": {
  "preset name": {
    "color_page_bg": "#000000",
    ...
  }
}
}
```

---

##### Usage

When you're working with the `settings_data.json` file, you should familiarize yourself with the following concepts:

* Theme presets
* Platform-controlled settings
* Limitations

###### Theme presets

Presets enable you to create up to five pre-configured designs from the same theme code base. Each preset includes a combination of layout options, color schemes, typography, and other visual elements.

Theme presets are included under one theme package. This gives merchants multiple customization options that they can apply to their store to change the general look and feel of the theme without extensive design skills or coding knowledge. Each preset gets its own dedicated listing page on the [Theme Store](https://themes.shopify.com/) that aligns to a primary industry and catalog size to appeal to a specific merchant segment.

Selecting a theme preset updates the `current` object to use the associated theme preset values. However, only values from [presentational settings](#presentational-settings) are updated.

**Presentational settings**

Presentational settings are settings that are related to a visual aspect of the theme. Examples of presentational settings include the color and font applied to text, or whether a specific element is visible.

The following input types are presentational settings. Values for these settings are overwritten when switching theme styles.

* [checkbox](https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings#checkbox)
* [color](https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings#color)
* [color_background](https://shopify.dev/docs/themes/architecture/settings/input-settings#color_background)
* [color_scheme](https://shopify.dev/docs/themes/architecture/settings/input-settings#color_scheme)
* [color_scheme_group](https://shopify.dev/docs/themes/architecture/settings/input-settings#color_scheme_group)
* [font_picker](https://shopify.dev/docs/themes/architecture/settings/input-settings#font_picker)
* [number](https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings#number)
* [radio](https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings#radio)
* [range](https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings#range)
* [select](https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings#select)

###### Platform-controlled settings

In the theme editor, Shopify exposes a [custom CSS setting](https://help.shopify.com/manual/online-store/themes/theme-structure/extend/add-css) at the theme and section level. Any custom CSS the merchant adds at the theme level is stored in the `platform-customizations` object's `custom_css` attribute.

This setting is intended to enable users to customize the look and feel of their storefront without editing theme code. As a theme developer, you shouldn't add this setting, or edit the value of this setting after it's set. Instead, you should use dedicated [CSS assets](https://shopify.dev/docs/storefronts/themes/architecture#assets) and [`stylesheet` Liquid tags](https://shopify.dev/docs/storefronts/themes/best-practices/javascript-and-stylesheet-tags#stylesheet), and introduce customization options for CSS in these areas using [theme settings](https://shopify.dev/docs/storefronts/themes/architecture/settings).

###### Limitations

* The `settings_data.json` file size can't exceed 1.5MB.
* A theme can't contain more than five presets.

### 2.9.3 markets.json

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/config/markets-json

#### markets.json

The `markets.json` file controls how theme customizations are inherited downstream across different markets. This file only appears in your theme's config folder when you have market-specific customizations.

While Shopify's markets feature allows one market to inherit from multiple parents, theme customizations require each market to have only one parent. The `markets.json` file manages this structure and allows developers to modify it.

##### Location

When a theme contains market-specific customizations, the `markets.json` file is located in its `config` directory:

```text
└── theme
  ...
  ├── config
  |   ├── settings_data.json
  |   ├── settings_schema.json
  |   └── markets.json
  └── locales
```

##### Usage

The `markets.json` lists the markets for which the theme was customized and their source of inheritance.

Here is an example of a `markets.json` file for a theme that includes customizations for the following markets: North America, Canada, United States, and Europe.

**config/markets.json**

```json
/*
 * ------------------------------------------------------------
 * IMPORTANT: The contents of this file are auto-generated.
 *
 * This file may be updated by the Shopify admin theme editor
 * or related systems. Please exercise caution as any changes
 * made to this file may be overwritten.
 * ------------------------------------------------------------
 */
{
  "markets": {
    "europe": {
      "parent": "@default"
    },
    "north-america": {
      "parent": "@default"
    },
    "canada": {
      "parent": "north-america"
    },
    "united-states": {
      "parent": "north-america"
    }
  }
}
```

In this example, the North America and Europe markets inherit from the store default. The Canada and United States markets inherit from North America.

When you customize a theme for a new market, Shopify sets the source of inheritance automatically. To customize this inheritance, update the `parent` field for the market in `markets.json`. The value for `parent` can be set to:

* Store default (`@default`): This is the default parent for all markets.
* Any parent market handle for that given market.

---

## 2.10 Locales

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/locales

### Locales

Locale files are JSON files containing translation sets for text strings throughout the theme and theme editor.

These files provide merchants a centralized location to edit repeated words and phrases, and enable translation of storefront content and theme editor settings for international audiences.

#### Location

Locale files reside in the `locales` directory:

```text
└── theme
  ...
  └── locales
```

#### Subtypes

Two types of locale files exist:

| Type | Description |
| - | - |
| Storefront | Files with `.json` extension controlling storefront content translations, editable by merchants via Shopify Language Editor |
| Schema | Files with `.schema.json` extension controlling theme editor settings translations |

#### Schema

Locale files follow a specific naming structure and organizational hierarchy:

* **Category**: Top-level translation grouping
* **Group**: Second-level grouping within a category
* **Description**: Third level representing individual translations

##### Example

```json
{
  "my_category": {
    "my_group": {
      "my_description": "translation text",
      ...
    },
    ...
  },
  ...
}
```

**Tip:** "When naming translation descriptions, try to be descriptive enough to give the translation context. For example, `blogs.article_comment.submit_button_text` gives more context than `blogs.article_comment.submit`."

##### Name locale files

File naming must follow IETF language tag nomenclature, with lowercase language code and uppercase region code.

Examples:

| Language | Storefront | Schema |
| - | - | - |
| English - Great Britain | `en-GB.json` | `en-GB.schema.json` |
| Spanish - Spain | `es-ES.json` | `es-ES.schema.json` |
| French - Canada | `fr-CA.json` | `fr-CA.schema.json` |

For non-region-specific languages, use 2-letter lowercase language codes:

| Language | Storefront | Schema |
| - | - | - |
| Finnish - All regions | `fi.json` | `fi.schema.json` |

A default locale file must be designated in the format `*.default.json` (or `*.default.schema.json` for schema files), where `*` represents the selected language. "Only one default file is permitted." Most themes use `en.default.json`, establishing English as the default locale.

#### Requirements and limitations

* Maximum of 3400 translations allowed in a single locale file
* Translation values cannot exceed 1000 characters

#### Usage

When working with locale files, reference methods vary depending on whether you're accessing storefront or schema locale files.

### 2.10.1 Storefront locale files

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/locales/storefront-locale-files

#### Storefront locale files

Storefront locale files are JSON files with a `.json` file extension. They host translation strings for content displayed on the storefront throughout the theme. These translations can be accessed by merchants through the [Shopify Language Editor](https://help.shopify.com/manual/online-store/themes/customizing-themes/language/change-wording#overview-of-the-language-editor).

**Note:**

Shopify provides [checkout and system message translations](#checkout-and-system-messages) through the Shopify Language Editor. However, this data is stored by Shopify outside of storefront locale files.

Rather than hard-coded text strings, theme layouts, templates, snippets, and [Liquid assets](https://shopify.dev/docs/storefronts/themes/architecture#assets) can reference these translations with the Liquid [translation filter](https://shopify.dev/docs/api/liquid/filters/translate) (`t` filter). This returns the appropriate translated string from the locale file for the [active language](https://help.shopify.com/manual/online-store/themes/customizing-themes/language/translate-theme#choose-a-language-for-your-theme).

When using the `t` filter, you can [interpolate](#interpolation) and [pluralize](#pluralize-translations) translations, as well as [localize any dates and times](#date-and-time-localization).

---

##### Location

Storefront locale files are located in the `locales` directory of the theme:

```text
└── theme
  ...
  ├── config
  └── locales
    ├── en.default.json
    ...
```

---

##### Schema

Storefront locale files need to follow a specific [naming structure](#name-structure). They also follow a basic organizational structure:

* **Category**: The top-level category of your translations.
* **Group**: The second level grouping of translations within a category.
* **Description**: The third level, which represents the individual translations.

**Example**

```json
{
  "my_category": {
    "my_group": {
      "my_description": "translation text",
      ...
    },
    ...
  },
  ...
}
```

**Tip:**

When naming translation descriptions, try to be descriptive enough to give the translation context. For example, `blogs.article_comment.submit_button_text` gives more context than `blogs.article_comment.submit`.

###### Name structure

Locale file naming must follow the standard [IETF language tag nomenclature](https://en.wikipedia.org/wiki/IETF_language_tag), where the first lowercase letter code represents the language, and the second uppercase letter code represents the region.

For example:

| Language | Format |
| - | - |
| English - Great Britain | `en-GB.json` |
| Spanish - Spain | `es-ES.json` |
| French - Canada | `fr-CA.json` |

If a language isn't region specific, you can use the 2-letter lowercase language representation.

For example:

| Language | Format |
| - | - |
| Finnish - All regions | `fi.json` |

Additionally, you must designate a [default locale file](#the-default-locale-file).

**The default locale file**

You must designate a default locale file in the format of `*.default.json`, where `*` is your selected language. This file contains the translations for the default language of the theme. Only one default file is permitted.

Most themes use `en.default.json`, which sets the default locale of the theme to English.

---

##### Content

To ensure that translations are mapped correctly, and to keep the process as simple as possible for merchants, you should organize your key structure to reflect your theme structure.

For example, the first two levels of the structure might look like this:

| 1st level | 2nd level |
| - | - |
| `general` | 404, breadcrumbs, search (results page and blank slates), pagination |
| `blogs` | article, article comments, blog sidebar |
| `cart` | cart contents, updates, notes, link to checkout |
| `collection` | collection, collection loop |
| `products` | product, product loop, related products |
| `layout` | general field titles and identifiers |
| `customer` | account, orders (list and details), account activation, addresses, login, password, registration |
| `contact` | contact form, form errors |
| `home_page` | blank slate, featured, help |
| `gift_cards` | title, usage terms |

**Note:**

If you use translations in snippets, then you should group them with the category most related to the snippet's role. For example, if you have a `related-products.liquid` snippet, then any associated translations should be included in the products group.

---

##### Usage

When working with storefront locale files, be aware of the following:

* referencing storefront translations
* interpolation
* preventing translations from being escaped
* pluralizing translations
* date and time localization
* checkout and system messages

###### Reference storefront translations

To reference translations from the storefront locale file for your theme's [active language](https://help.shopify.com/manual/online-store/themes/customizing-themes/language/translate-theme#choose-a-language-for-your-theme), you can use translation keys and the Liquid [translation filter](https://shopify.dev/docs/api/liquid/filters/translate) (`t` filter).

For example, let's assume you have locale files for English, French, and Spanish. In this case, you might have the following in each associated locale file:

**/locales/en.default.json (English)**

```json
{
  "blog": {
    "comment": {
      "email": "Your email"
    }
  }
}
```

**/locales/fr.json (French)**

```json
{
  "blog": {
    "comment": {
      "email": "Votre adresse courriel"
    }
  }
}
```

**/locales/es-ES.json (Spanish)**

```json
{
  "blog": {
    "comment": {
      "email": "Su correo electrónico"
    }
  }
}
```

To reference this translation, you might use something like the following:

```liquid
<span>{{ 'blog.comment.email'  | t }}</span>
```

**Tip:**

When referencing translation keys in Liquid, they must be wrapped in single quotes (`'`).

The output is customized based on the settings in each locale file:

**Output**

```html
// English
<span>Your email</span>


// French
<span>Votre adresse courriel</span>


// Spanish
<span>Su correo electrónico</span>
```

###### Interpolation

Translation strings can be interpolated, meaning you can include variables in your strings to be dynamically populated when the string is referenced in Liquid. For example, you can include following in your locale file:

**/locales/en.default.json**

```json
{
  "layout": {
    "header": {
      "hello_user": "Hello {{ name }}!"
    }
  }
}
```

When you reference that translation in your theme, you can specify a value for the `name` variable:

**/layout/theme.liquid**

```liquid
{% if customer %}
  <h1>{{ 'layout.header.hello_user' | t: name: customer.first_name }}</h1>
{% endif %}
```

In the case of a customer named "Jane", this code outputs the following:

**Output**

```html
<h1>Hello Jane!</h1>
```

**Pass multiple arguments**

With interpolation, it's possible to pass multiple arguments, separated by a comma (`,`). For example, if you want to extend the example above to show the customer's first and last name, then you can adjust your translation string and theme reference to the following:

**/locales/en.default.json**

```json
{
  "layout": {
    "header": {
      "hello_user": "Hello {{ first_name }} {{ last_name }}!"
    }
  }
}
```

**/layout/theme.liquid**

```liquid
{% if customer %}
  <h1>
    {{ 'layout.header.hello_user' | t: first_name: customer.first_name, last_name: customer.last_name }}
  </h1>
{% endif %}
```

In the case of a customer named "Jane Doe", this code outputs the following:

**Output**

```html
<h1>Hello Jane Doe!</h1>
```

###### Prevent translations from being escaped

Translated content is escaped by default, meaning any HTML character is converted into its entity equivalent.

You can add the suffix `_html` to the description level of your translation key to prevent translated content from being escaped. For example, the content output by the following translation would be escaped, causing the `<strong>` tags to show as plain text:

**/locales/en.default.json**

```json
{
  "layout": {
    "header": {
      "announcement_bar_text": "Spend $50 and get <strong>FREE</strong> shipping",
    }
  }
}
```

Adding the `_html` suffix prevents the output content from being escaped, allowing the `<strong>` tags to render as proper HTML:

**/locales/en.default.json**

```json
{
  "layout": {
    "header": {
      "announcement_bar_text_html": "Spend $50 and get <strong>FREE</strong> shipping",
    }
  }
}
```

**Tip:**

The `_html` suffix is useful for cases like including HTML characters in translations, or using translations in JavaScript as part of a `<script>` tag or `js.liquid` asset file.

###### Pluralize translations

You can apply locale-aware pluralizations to translations by passing a `count` attribute to the [translation filter](https://shopify.dev/docs/api/liquid/filters/translate) (`t` filter).

The following pluralization keys, defined by the Unicode Consortium's [CLDR](https://github.com/unicode-org/cldr), are supported:

* `few`
* `many`
* `one`
* `other`
* `two`
* `zero`

For example, the following translation and translation reference returns the following output:

**/locales/en.default.json**

```json
{
  "customers": {
    "orders": {
      "order_count": {
        "one": "You've made {{ count }} order with us",
        "other": "You've made {{ count }} orders with us"
      }
    }
  }
}
```

**/layout/theme.liquid**

```liquid
{% if customer %}
  <h1>{{ 'customers.order.order_count' | t: count: customer.orders_count }}</h1>
{% endif %}
```

**Output**

```html
// count == 1
<h1>You've made 1 order with us</h1>


// count == 12
<h1>You've made 12 orders with us</h1>
```

For more information about pluralization rules in different languages, refer to the [Unicode language plural rules](https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html) tables.

###### Date and time localization

Dates and times can be rendered with the [date](https://shopify.dev/docs/api/liquid/filters/date) and [time_tag](https://shopify.dev/docs/api/liquid/filters/time_tag) Liquid filters. Each has default format options that will display in the appropriate format for the store's [active language](https://help.shopify.com/en/manual/checkout-settings/checkout-language):

* `date` filter [default format options](https://shopify.dev/docs/api/liquid/filters/date-format)
* `time_tag` filter [default format options](https://shopify.dev/docs/api/liquid/filters/time_tag-format)

For example, the following Liquid generates the following output:

**Input**

```liquid
{{ order.created_at | date: format: 'abbreviated_date' }}
```

**Output**

```liquid
Dec 31, 2018
```

**Custom formats**

You can include custom formats in locale files by adding a `date_formats` object:

**locales/en.json**

```json
{
  "date_formats": {
    "month_and_year": "%B %Y"
  }
}
```

These formats must use the same parameters as Ruby's `strftime` method. You can find a list of these parameters in [Ruby's documentation](https://ruby-doc.org/core-3.0.1/Time.html#method-i-strftime), or use a site like [strfti.me](https://www.strfti.me/).

**Caution:**

Ensure that custom formats are included in all locale files. If a custom format is missing in the locale file of the active language, then a Liquid error is rendered.

Using the custom format above, the following Liquid generates the following output:

**Input**

```liquid
{{ order.created_at | date: format: 'month_and_year' }}
```

**Output**

```liquid
December 2018
```

###### Checkout and system messages

Shopify provides checkout and system messages in the following languages:

* Bulgarian (Bulgaria)
* Chinese (Simplified)
* Chinese (Traditional)
* Croatian (Croatia)
* Czech
* Danish
* Dutch
* English
* Finnish
* French
* German
* Greek
* Hindi
* Hungarian
* Indonesian
* Italian
* Japanese
* Korean
* Lithunian (Lithuania)
* Malay
* Norwegian (Bokmål)
* Polish
* Portuguese (Brazil)
* Portuguese (Portugal)
* Romania (Romanian)
* Russian
* Slovak
* Slovenian
* Spanish
* Swedish
* Thai
* Turkish

**Note:**

If you're using a language that's not in the list above, then you'll need to manually enter translations for checkout and system messages through the [Shopify Language Editor](https://help.shopify.com/manual/checkout-settings/checkout-language#create-your-own-checkout-language).

### 2.10.2 Schema locale files

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/locales/schema-locale-files

#### Schema locale files

Schema locale files are JSON files with a `.schema.json` file extension. They host translation strings for various setting schema attributes so that content in the theme editor can be translated to the store's active language.

To learn which attributes can be translated, refer to Content.

---

##### Location

Schema locale files are located in the `locales` directory of the theme:

```text
└── theme
  ...
  ├── config
  └── locales
    ├── en.default.schema.json
    ├── es-ES.schema.json
    ...
```

---

##### Schema

Schema locale files need to follow a specific naming structure. They also follow a basic organizational structure:

* **Category**: The top-level category of your translations.
* **Group**: The second level grouping of translations within a category.
* **Description**: The third level, which represents the individual translations.

**Example**

```json
{
  "my_category": {
    "my_group": {
      "my_description": "translation text",
      ...
    },
    ...
  },
  ...
}
```

**Tip:**

When naming translation descriptions, try to be descriptive enough to give the translation context. For example, `blogs.article_comment.submit_button_text` gives more context than `blogs.article_comment.submit`.

###### Name structure

Locale file naming must follow the standard IETF language tag nomenclature, where the first lowercase letter code represents the language, and the second uppercase letter code represents the region.

For example:

| Language | Format |
| - | - |
| English - Great Britain | `en-GB.schema.json` |
| Spanish - Spain | `es-ES.schema.json` |
| French - Canada | `fr-CA.schema.json` |

If a language isn't region specific, you can use the 2-letter lowercase language representation.

For example:

| Language | Format |
| - | - |
| Finnish - All regions | `fi.schema.json` |

Additionally, you must designate a default locale file.

**The default locale file**

You must designate a default locale file in the format of `*.default.schema.json`, where `*` is your selected language. This file contains the translations for the default language of the theme. Only one default file is permitted.

Most themes use `en.default.schema.json`, which sets the default locale of the theme to English.

###### Content

Schema locale files allow you to create translations for the following setting attributes:

| Parent | Attribute |
| - | - |
| All settings | `info`, `label` |
| Section schema `block` | `name` |
| `select` | `group` |
| `html`, `number`, `text`, `textarea`, `video_url` | `placeholder` |
| `range` | `unit` |
| `header`, `paragraph` | `content` |
| `presets` | `name`, `category` |
| `html`, `inline_richtext`, `liquid`, `richtext`, `text`, `textarea`, `url`, `video`, `video_url` | `default` |

---

##### Usage

When working with schema locale files, you should familiarize yourself with referencing schema translations.

###### Reference schema translations

Schema translations can be accessed with code in the following format:

```text
t:translation_category.translation_group.translation_name
```

For example, to make the `name` attribute of the `product.liquid` section translatable, use the following:

**locales/en.default.schema.json**

```json
{
  "sections": {
    "product": {
      "name": "Product"
    }
  }
}
```

**sections/product.liquid**

```liquid
{% schema %}
{
  "name": "t:sections.product.name",
  ...
}
{% endschema %}
```

---

*Fine del Capitolo 2 — Key Concepts (Theme Architecture).*
