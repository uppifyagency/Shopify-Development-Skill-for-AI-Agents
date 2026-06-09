# 7. Liquid — Overview & Objects

This chapter is a faithful 1:1 extraction of the Shopify Liquid reference: the Liquid overview, the Liquid basics, and **every** object documented under `https://shopify.dev/docs/api/liquid/objects`. Each object section is introduced with its source URL and reproduces the object's description, data type, availability/deprecation notes, the full properties table, and the code examples (Liquid input and rendered output) verbatim.

Liquid is a template language created by Shopify and released as an [open source project](https://shopify.github.io/liquid/). The variation documented here extends open-source Liquid for use with [Shopify themes](https://shopify.dev/themes).

---

## Overview & basics

### Liquid Reference

> Fonte: https://shopify.dev/docs/api/liquid

Liquid is a template language created by Shopify. It's available as an [open source project](https://shopify.github.io/liquid/) on GitHub, and is used by many different software projects and companies.

This reference documents the Liquid tags, filters, and objects that you can use to build [Shopify Themes](https://shopify.dev/themes).

#### What is a template language?

A template language allows you to create a single template to host static content, and dynamically insert information depending on where the template is rendered. For example, you can create a product template that hosts all of your standard product attributes, such as the product image, title, and price. That template can then dynamically render those attributes with the appropriate content, depending on the current product being viewed.

#### Variations of Liquid

The variation of Liquid in this reference extends the open-source version of Liquid for use with [Shopify themes](https://shopify.dev/themes). It includes tags, filters, and objects that can be used to render objects specific to Shopify stores and storefront functionality.

Shopify also uses slightly different versions of Liquid to render dynamic content for the following features. These variations aren't included in this reference.

- [Notification templates](https://help.shopify.com/en/manual/orders/notifications/email-variables)
- [Shopify Flow](https://help.shopify.com/en/manual/shopify-flow/reference/variables#liquid-variables)
- [Order printer templates](https://help.shopify.com/en/manual/fulfillment/managing-orders/printing-orders/shopify-order-printer/liquid-variables-and-filters-reference)
- [Packing slip templates](https://help.shopify.com/en/manual/orders/packing-slips-variable-list)

#### Liquid basics

Liquid is used to dynamically output objects and their properties. You can further modify that output by creating logic with tags, or directly altering it with a filter. Objects and object properties are output using one of six basic data types. Liquid also includes basic logical and comparison operators for use with tags.

**Related resource:** [Basics](https://shopify.dev/docs/api/liquid/basics)

##### Example

**Code:**
```liquid
<title>
  {{ page_title }}
</title>
{% if page_description -%}
  <meta name="description" content="{{ page_description | truncate: 150 }}">
{%- endif %}
```

**Output:**
```html
<title>
  Health potion
</title>
<meta name="description" content="Are you low on health? Well we've got the potion just for you! Just need a top up? Almost dead? In between? No need to worry because we have the ...">
```

#### Defining logic with tags

Liquid tags are used to define logic that tells templates what to do.

Tags are wrapped with curly brace percentage delimiters `{% %}`. The text within the delimiters is an instruction, not content to render.

In the example below, the `if` tag defines the condition to be met. If `product.available` returns `true`, then the price is displayed. Otherwise, the "sold out" message is shown.

To nest multiple tags inside one set of delimiters, use the [`liquid`](https://shopify.dev/docs/api/liquid/tags/liquid) tag.

##### Example

**Code:**
```liquid
{% if product.available %}
  Price: $99.99
{% else %}
  Sorry, this product is sold out.
{% endif %}
```

**Data:**
```json
{
  "product": {
    "available": true
  }
}
```

**Output:**
```html
Price: $99.99
```

##### Tags with parameters

Some tags accept parameters: either required or optional. For example, the `for` tag takes an optional `limit` parameter to stop the loop at a specific index.

**Code:**
```liquid
{% assign numbers = '1,2,3,4,5' | split: ',' %}

{% for item in numbers limit:2 -%}
  {{ item }}
{% endfor %}
```

**Output:**
```html
1
2
```

#### Modifying output with filters

Liquid filters modify the output of variables and objects.

To filter the output of a tag, use the pipe character `|`, followed by the filter. In this example, `product` is the object, `title` is its property, and `upcase` is the filter.

**Code:**
```liquid
{% # product.title -> Health potion %}

{{ product.title | upcase }}
```

**Data:**
```json
{
  "product": {
    "title": "Health potion"
  }
}
```

**Output:**
```html
HEALTH POTION
```

##### Filters with parameters

Many filters accept parameters that adjust their output. Some parameters are required, others are optional.

**Code:**
```liquid
{% # product.title -> Health potion %}

{{ product.title | remove: 'Health' }}
```

**Data:**
```json
{
  "product": {
    "title": "Health potion"
  }
}
```

**Output:**
```html
potion
```

##### Using multiple filters

Multiple filters can be used on one output. They're applied from left to right.

**Code:**
```liquid
{% # product.title -> Health potion %}

{{ product.title | upcase | remove: 'HEALTH' }}
```

**Data:**
```json
{
  "product": {
    "title": "Health potion"
  }
}
```

**Output:**
```html
POTION
```

#### Referencing objects

Liquid objects represent variables that you can use to build your theme. Object types include, but aren't limited to:

- Store resources, such as a collection or product and its properties
- Standard content that is used to power Shopify themes, such as `content_for_header`
- Functional elements that can be used to build interactivity, such as `paginate` and `search`

Objects might represent a single data point, or contain multiple properties. Some objects might represent a related object, such as a product in a collection.

Double curly brace delimiters denote an output.

##### Usage

To output an object, wrap it in curly brace delimiters `{{ }}`.

To output an object's property, use dot notation. This example outputs the `product` object's `title` property.

**Code:**
```liquid
{{ product.title }}
```

**Data:**
```json
{
  "product": {
    "title": "Health potion"
  }
}
```

**Output:**
```html
Health potion
```

##### Object access

Objects can be accessed in three ways:

- **Globally**: Available in any Liquid file, excluding [checkout.liquid](https://shopify.dev/themes/architecture/layouts/checkout-liquid) and [Liquid asset files](https://shopify.dev/themes/architecture#assets)
- **In templates**: Available in specific templates and their sections or blocks. For example, the [`product`](https://shopify.dev/docs/api/liquid/objects/product) object in a [product template](https://shopify.dev/themes/architecture/templates/product)
- **Through parent objects**: Returned as properties of other objects. For example, [`article`](https://shopify.dev/docs/api/liquid/objects/article) objects through [`articles`](https://shopify.dev/docs/api/liquid/objects/articles) or [`blog`](https://shopify.dev/docs/api/liquid/objects/blog)

Check each object's documentation to see how it can be accessed.

##### Creating variables

To create your own variables, use variable tags like [`assign`](https://shopify.dev/docs/api/liquid/tags/assign) or [`capture`](https://shopify.dev/docs/api/liquid/tags/capture). Syntactically, Liquid treats variables the same as objects.

**Code:**
```liquid
{% assign my_variable = 'My custom string.' %}
{{ my_variable }}
```

**Output:**
```html
My custom string.
```

#### Resources & tools

- **[Liquid Cheat Sheet](https://www.shopify.com/partners/shopify-cheat-sheet)** — "A simple reference guide to the Liquid language."
- **[Theme Check](https://shopify.dev/themes/tools/theme-check)** — "Command line-based linter for themes. Also comes as an official Visual Studio Code extension."
- **[Shopify CLI for Themes](https://shopify.dev/themes/tools/cli)** — "A powerful command-line tool for building Shopify themes, and exploring Liquid code in a REPL interface."
- **[Open source liquid](https://github.com/Shopify/liquid)** — Liquid is an open source project on GitHub.

### Liquid Basics

> Fonte: https://shopify.dev/docs/api/liquid/basics

The following are basic concepts that you need to effectively interact with Liquid tags, filters, and objects.

#### Object Handles

Objects that represent store resources, such as products, collections, articles, and blogs, have handles for identifying an individual resource. The handle is used to build the URL for the resource, or to return properties for the resource.

Other objects like `linklists`, `links`, and `settings` also have handles.

##### Creating and Modifying Handles

Handles are automatically generated based on the resource title. They follow a set of rules:

* Handles are always lowercase
* Whitespace and special characters are replaced with a hyphen `-`
* If there are multiple consecutive whitespace or special characters, they're replaced with a single hyphen
* Whitespace or special characters at the beginning are removed

Handles need to be unique, so if a duplicate title is used, the handle is auto-incremented by one. For example, if you had two products called `Potion`, their handles would be `potion` and `potion-1`.

After a resource has been created, changing the resource title doesn't update the handle.

You can modify a resource's handle within the Shopify admin. This can be done either in the Handle or the Edit website SEO sections, depending on the resource. If you reference resources by their handle, then be sure to update those references when modifying handles.

> **Note:** Individual links from `linklists` have handles based on their titles. These handles can't be modified directly. Individual settings, from `settings_schema.json`, sections, or blocks, get their handle from their `id` property.

###### Example

```liquid
{{ product.title | handle }}
```

**Data:**
```json
{
  "product": {
    "title": "Health potion"
  }
}
```

**Output:**
```html
health-potion
```

##### Referencing Handles

All objects that have a handle have a `handle` property. For example, you can output a product's handle with `product.handle`. You can reference an object, from within its parent object, by its handle in two ways:

* Square bracket notation `[ ]`: Accepts a handle wrapped in quotes `'`, a Liquid variable, or an object reference
* Dot notation `.`: Accepts a handle without quotes

> **Note:** Referencing an object by its handle is similar to referencing array elements by their index.

###### Example

```liquid
'About us' page URL: {{ pages['about-us'].url }}
Enable product suggestions: {{ settings.predictive_search_enabled }}
```

**Data:**
```json
{
  "settings": {
    "predictive_search_enabled": true
  }
}
```

**Output:**
```html
'About us' page URL: /pages/about-us
Enable product suggestions: true
```

#### Logical and Comparison Operators

Liquid supports basic logical and comparison operators for use with conditional tags: [`case`](https://shopify.dev/docs/api/liquid/tags/case), [`else`](https://shopify.dev/docs/api/liquid/tags/conditional-else), [`if`](https://shopify.dev/docs/api/liquid/tags/if) and [`unless`](https://shopify.dev/docs/api/liquid/tags/unless).

| Operator | Function |
| - | - |
| `==` | equals |
| `!=` | does not equal |
| `>` | greater than |
| `<` | less than |
| `>=` | greater than or equal to |
| `<=` | less than or equal to |
| `or` | Condition A or Condition B |
| `and` | Condition A and Condition B |
| `contains` | Checks for strings in strings or arrays |

##### contains

You can use `contains` to check for the presence of a string within an array, or another string. You can't use `contains` to check for an object in an array of objects.

###### Example

```liquid
{% if product.tags contains 'healing' %}
  This potion contains restorative properties.
{% endif %}
```

**Data:**
```json
{
  "product": {
    "tags": [
      "healing"
    ]
  }
}
```

**Output:**
```html
This potion contains restorative properties.
```

##### Order of Operations

When using more than one operator in a tag, the operators are evaluated from right to left, and you can't change this order.

> **Caution:** Parentheses `()` aren't valid characters within Liquid tags. If you try to include them to group operators, your tag won't be rendered.

###### Example

```liquid
{% unless true and false and false or true %}
  This evaluates to false, since Liquid checks tags like this:

  true and (false and (false or true))
  true and (false and true)
  true and false
  false
{% endunless %}
```

**Output:**
```html
This evaluates to false, since Liquid checks tags like this:

  true and (false and (false or true))
  true and (false and true)
  true and false
  false
```

#### Types

Liquid output can be one of six data types.

##### string

Any series of characters, wrapped in single or double quotes.

> **Info:** You can check whether a string is empty with the `blank` object.

##### number

Numeric values, including floats and integers.

##### boolean

A binary value, either `true` or `false`.

##### nil

An undefined value.

Tags or outputs that return `nil` don't print anything to the page. They are also treated as `false`.

> **Note:** A string with the characters "nil" is not treated the same as `nil`.

##### array

A list of variables of any type.

To access all of the items in an array, you can loop through each item in the array using a [`for`](https://shopify.dev/docs/api/liquid/tags/for) or [`tablerow`](https://shopify.dev/docs/api/liquid/tags/tablerow) tag.

You can use square bracket `[ ]` notation to access a specific item in an array. Array indexing starts at zero.

You can't initialize arrays using only Liquid. You can, however, use the split filter to break a single string into an array of substrings.

##### empty

An `empty` object is returned if you try to access an object that is defined, but has no value. For example a page or product that's been deleted, or a setting with no value.

You can compare an object with `empty` to check whether an object exists before you access any of its attributes.

###### Example

```liquid
{% unless pages.about-us == empty %}
  <h1>{{ page.title }}</h1>
  <div>
    {{ page.content }}
  </div>
{% endunless %}
```

**Data:**
```json
{
  "page": {
    "content": "<p>Polina's Potent Potions was started by Polina in 1654.</p>\n<p>We use all-natural locally sourced ingredients for our potions.</p>",
    "title": "About us"
  }
}
```

**Output:**
```html
<h1>About us</h1>
  <div>
    <p>Polina's Potent Potions was started by Polina in 1654.</p>
<p>We use all-natural locally sourced ingredients for our potions.</p>
  </div>
```

#### Truthy and Falsy

All data types must return either `true` or `false`. Those which return `true` by default are called truthy. Those that return `false` by default are called falsy.

| Value | Truthy | Falsy |
| - | - | - |
| `true` | ✓ | |
| `false` | | ✓ |
| `nil` | | ✓ |
| `empty string` | | ✓ |
| `0` | ✓ | |
| `integer` | ✓ | |
| `float` | ✓ | |
| `array` | ✓ | |
| `empty array` | ✓ | |
| `page` | ✓ | |
| `empty object` | ✓ | |

##### Example

Because `nil` and `false` are the only falsy values, you need to be careful how you check values in Liquid. A value might not be in the format you expect, but still be truthy.

For example, empty strings are truthy, so you need to check whether they're empty with `blank`. `EmptyDrop` objects are also truthy, so you need to check whether the object you're referencing is `empty`.

###### Example

```liquid
{% if settings.featured_potions_title != blank -%}
  {{ settings.featured_potions_title }}
{%- else -%}
  No value for this setting has been selected.
{%- endif %}
{% unless pages.recipes == empty -%}
  {{ pages.recipes.content }}
{%- else -%}
  No page with this handle exists.
{%- endunless %}
```

**Data:**
```json
{
  "settings": {
    "featured_potions_title": null
  }
}
```

**Output:**
```html
No value for this setting has been selected.
No page with this handle exists.
```

#### Whitespace Control

Even if it doesn't output text, any line of Liquid outputs a line in your rendered content. By including hyphens in your Liquid tag, you can strip any whitespace that your Liquid generates when rendered.

If you want to remove whitespace on only one side of the Liquid tag, then you can include the hyphen on either the opening or closing tag.

###### Example

```liquid
{%- if collection.products.size > 0 -%}
The '{{ collection.title }}' collection contains the following types of products:

{% for type in collection.all_types -%}
  {% unless type == blank -%}
    - {{ type }}
  {%- endunless -%}
{%- endfor %}
{%- endif -%}
```

**Data:**
```json
{
  "collection": {
    "all_types": [
      "Health",
      "Health & Beauty",
      "Invisibility",
      "Water"
    ],
    "products": [],
    "title": "Sale potions"
  }
}
```

**Output:**
```html
The 'Sale potions' collection contains the following types of products:

- Health
- Health & Beauty
- Invisibility
- Water
```

---

## Objects

> Index: https://shopify.dev/docs/api/liquid/objects

The following are all of the Liquid objects captured from the reference, in alphabetical order. Each object below includes its source URL, description, data type, availability/deprecation notes, full properties table, and code examples.

**Table of contents:**

- [additional_checkout_buttons](#additional_checkout_buttons)
- [address](#address)
- [all_country_option_tags](#all_country_option_tags)
- [all_products](#all_products)
- [app](#app)
- [article](#article)
- [articles](#articles)
- [block](#block)
- [blog](#blog)
- [blogs](#blogs)
- [brand](#brand)
- [brand_color](#brand_color)
- [canonical_url](#canonical_url)
- [cart](#cart)
- [checkout](#checkout)
- [collection](#collection)
- [collections](#collections)
- [color](#color)
- [color_scheme](#color_scheme)
- [color_scheme_group](#color_scheme_group)
- [comment](#comment)
- [company](#company)
- [company_address](#company_address)
- [company_location](#company_location)
- [content_for_additional_checkout_buttons](#content_for_additional_checkout_buttons)
- [content_for_header](#content_for_header)
- [content_for_index](#content_for_index)
- [content_for_layout](#content_for_layout)
- [country](#country)
- [country_option_tags](#country_option_tags)
- [currency](#currency)
- [current_page](#current_page)
- [current_tags](#current_tags)
- [customer](#customer)
- [customer_payment_method](#customer_payment_method)
- [discount](#discount)
- [discount_allocation](#discount_allocation)
- [discount_application](#discount_application)
- [external_video](#external_video)
- [filter](#filter)
- [filter_value](#filter_value)
- [filter_value_display](#filter_value_display)
- [focal_point](#focal_point)
- [font](#font)
- [forloop](#forloop)
- [form](#form)
- [form_errors](#form_errors)
- [fulfillment](#fulfillment)
- [generic_file](#generic_file)
- [gift_card](#gift_card)
- [group](#group)
- [handle](#handle)
- [image](#image)
- [image_presentation](#image_presentation)
- [images](#images)
- [instructions](#instructions)
- [line_item](#line_item)
- [link](#link)
- [linklist](#linklist)
- [linklists](#linklists)
- [localization](#localization)
- [location](#location)
- [market](#market)
- [measurement](#measurement)
- [media](#media)
- [metafield](#metafield)
- [metaobject](#metaobject)
- [metaobject_definition](#metaobject_definition)
- [metaobject_system](#metaobject_system)
- [metaobjects](#metaobjects)
- [model](#model)
- [model_source](#model_source)
- [money](#money)
- [order](#order)
- [page](#page)
- [page_description](#page_description)
- [page_image](#page_image)
- [page_title](#page_title)
- [pages](#pages)
- [paginate](#paginate)
- [parent_relationship](#parent_relationship)
- [part](#part)
- [pending_payment_instruction_input](#pending_payment_instruction_input)
- [policy](#policy)
- [powered_by_link](#powered_by_link)
- [predictive_search](#predictive_search)
- [predictive_search_resources](#predictive_search_resources)
- [product](#product)
- [product_option](#product_option)
- [product_option_value](#product_option_value)
- [quantity_price_break](#quantity_price_break)
- [quantity_rule](#quantity_rule)
- [rating](#rating)
- [recipient](#recipient)
- [recommendations](#recommendations)
- [remote_details](#remote_details)
- [remote_product](#remote_product)
- [remote_shop](#remote_shop)
- [request](#request)
- [robots](#robots)
- [routes](#routes)
- [rule](#rule)
- [script](#script)
- [search](#search)
- [section](#section)
- [selling_plan](#selling_plan)
- [selling_plan_allocation](#selling_plan_allocation)
- [selling_plan_allocation_price_adjustment](#selling_plan_allocation_price_adjustment)
- [selling_plan_checkout_charge](#selling_plan_checkout_charge)
- [selling_plan_group](#selling_plan_group)
- [selling_plan_group_option](#selling_plan_group_option)
- [selling_plan_option](#selling_plan_option)
- [selling_plan_price_adjustment](#selling_plan_price_adjustment)
- [settings](#settings)
- [shipping_method](#shipping_method)
- [shop](#shop)
- [shop_locale](#shop_locale)
- [sitemap](#sitemap)
- [sort_option](#sort_option)
- [store_availability](#store_availability)
- [store_credit_account](#store_credit_account)
- [swatch](#swatch)
- [tablerowloop](#tablerowloop)
- [tax_line](#tax_line)
- [taxonomy_category](#taxonomy_category)
- [template](#template)
- [theme](#theme)
- [transaction](#transaction)
- [transaction_payment_details](#transaction_payment_details)
- [unit_price_measurement](#unit_price_measurement)
- [user](#user)
- [user_agent](#user_agent)
- [variant](#variant)
- [video](#video)
- [video_source](#video_source)

### additional_checkout_buttons

> Fonte: https://shopify.dev/docs/api/liquid/objects/additional_checkout_buttons

Returns `true` if a store has any payment providers with offsite checkouts, such as PayPal Express Checkout.

Use `additional_checkout_buttons` to check whether these payment providers exist, and [`content_for_additional_checkout_buttons`](https://shopify.dev/docs/api/liquid/objects/content_for_additional_checkout_buttons) to show the associated checkout buttons. To learn more about how to use these objects, refer to [Accelerated checkout](https://shopify.dev/themes/pricing-payments/accelerated-checkout).

#### Example

```liquid
{% if additional_checkout_buttons %}
  {{ content_for_additional_checkout_buttons }}
{% endif %}
```

#### Directly accessible in

* Global

---

### address

> Fonte: https://shopify.dev/docs/api/liquid/objects/address

An address, such as a customer address or order shipping address.

> Use the `format_address` filter to output an address according to its locale.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| address1 | string | The first line of the address. |
| address2 | string | The second line of the address. If no second line is specified, then `nil` is returned. |
| city | string | The city of the address. |
| company | string | The company of the address. If no company is specified, then `nil` is returned. |
| country | country | The country of the address. |
| country_code | string | The country of the address in ISO 3166-1 (alpha 2) format. |
| first_name | string | The first name of the address. |
| id | number | The ID of the address. |
| last_name | string | The last name of the address. |
| name | string | A combination of the first and last names of the address. |
| phone | string | The phone number of the address. If no phone number is specified, then `nil` is returned. |
| province | string | The province of the address. |
| province_code | string | The province of the address in ISO 3166-2 (alpha 2) format. Note: The value doesn't include the preceding ISO 3166-1 country code. |
| street | string | A combination of the first and second lines of the address. |
| summary | string | A summary of the address, including first and last name, first and second lines, city, province, and country. |
| url | string | The relative URL for the address. Note: This only applies to customer addresses. |
| zip | string | The zip or postal code of the address. |

#### Example

```json
{
  "address1": "150 Elgin Street",
  "address2": "8th floor",
  "city": "Ottawa",
  "company": "Polina's Potions, LLC",
  "country": {},
  "country_code": "CA",
  "first_name": null,
  "id": 56174706753,
  "last_name": null,
  "name": "",
  "phone": "416-123-1234",
  "province": "Ontario",
  "province_code": "ON",
  "street": "150 Elgin Street, 8th floor",
  "summary": "150 Elgin Street, 8th floor, Ottawa, Ontario, Canada",
  "url": "/account/addresses/56174706753",
  "zip": "K2P 1L4"
}
```

---

### all_country_option_tags

> Fonte: https://shopify.dev/docs/api/liquid/objects/all_country_option_tags

Creates an `<option>` tag for each country.

An attribute called `data-provinces` is set for each `<option>`, containing a JSON-encoded array of the country or region's subregions. If a country has no subregions, an empty array is set for its `data-provinces` attribute.

> **Tip:** To return only countries and regions in the store's shipping zones, use the `country_option_tags` object instead.

#### Directly accessible in

* Global

#### Usage

Wrap the `all_country_option_tags` object in `<select>` tags to build a country option selector.

```liquid
<select name="country">
  {{ all_country_option_tags }}
</select>
```

---

### all_products

> Fonte: https://shopify.dev/docs/api/liquid/objects/all_products

All of the products on a store.

> **Note:** The `all_products` object has a limit of 20 unique handles per page. If you want more than 20 products, consider using a collection instead.

#### Directly accessible in

* Global

You can use `all_products` to access a product by its [handle](https://shopify.dev/docs/api/liquid/basics#handles). This returns the [`product`](https://shopify.dev/docs/api/liquid/objects/product) object for the specified product. If the product isn't found, then `empty` is returned.

#### Example

**Liquid**
```liquid
{{ all_products['love-potion'].title }}
```

**Data**
```json
{
  "all_products": {
    "love-potion": {
      "title": "Love Potion"
    }
  }
}
```

**Output**
```html
Love Potion
```

---

### app

> Fonte: https://shopify.dev/docs/api/liquid/objects/app

An app. This object is usually used to access app-specific information for use with [theme app extensions](https://shopify.dev/apps/online-store/theme-app-extensions).

#### Properties

| Property | Description |
|----------|-------------|
| metafields | The [metafields](https://shopify.dev/docs/api/liquid/objects/metafield) that are [owned by the app](https://shopify.dev/apps/metafields/app-owned). |

---

### article

> Fonte: https://shopify.dev/docs/api/liquid/objects/article

An article, or [blog post](https://help.shopify.com/manual/online-store/blogs/writing-blogs), in a blog.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| author | string | The full name of the author of the article. |
| comment_post_url | string | The relative URL where POST requests are sent when creating new comments. |
| comments | array of comment | The published comments for the article. Returns an empty array if comments are disabled. **Tip:** Use the paginate tag to choose how many comments to show at once, up to a limit of 50. |
| comments_count | number | The number of published comments for the article. |
| comments_enabled? | boolean | Returns `true` if comments are enabled. Returns `false` if not. |
| content | string | The content of the article. |
| created_at | string | A timestamp for when the article was created. **Tip:** Use the date filter to format the timestamp. |
| excerpt | string | The excerpt of the article. |
| excerpt_or_content | string | Returns the article excerpt if it exists. Returns the article content if no excerpt exists. |
| handle | string | The handle of the article. |
| id | string | The ID of the article. |
| image | image | The featured image for the article. |
| metafields | metafield | The metafields applied to the article. **Tip:** To learn about creating metafields, refer to Create and manage metafields or visit the Shopify Help Center. |
| moderated? | boolean | Returns `true` if the blog is set to moderate comments. Returns `false` if not. |
| published_at | string | A timestamp for when the article was published. **Tip:** Use the date filter to format the timestamp. |
| tags | array of string | The tags applied to the article. When looping through `article.tags`, you can print how many times a tag is used with `tag.total_count`. |
| template_suffix | string | The name of the custom template assigned to the article. The name doesn't include the `article.` prefix, or the file extension. If a custom template isn't assigned, `nil` is returned. |
| title | string | The title of the article. |
| updated_at | string | A timestamp for when the article was updated. **Tip:** Use the date filter to format the timestamp. |
| url | string | The relative URL of the article. |
| user | user | The user associated with the author of the article. |

#### Example with Tags

**Code:**
```liquid
{% for tag in article.tags -%}
  {{ tag }} ({{ tag.total_count }})
{%- endfor %}
```

**Data:**
```json
{
  "article": {
    "tags": [
      "clear potions",
      "potion troubleshooting",
      "tips"
    ]
  }
}
```

**Output:**
```html
clear potions (1)potion troubleshooting (2)tips (2)
```

#### Example Article Object

```json
{
  "author": "Polina Waters",
  "comment_post_url": "/blogs/potion-notions/how-to-tell-if-you-have-run-out-of-invisibility-potion/comments",
  "comments": [],
  "comments_count": 1,
  "comments_enabled?": true,
  "content": "<p>We've all had this problem before: we peek into the potions vault to determine which potions we are running low on, and the invisibility potion bottle looks completely empty.</p>\n<p>...</p>\n<p> </p>",
  "created_at": "2022-04-14 16:56:02 -0400",
  "excerpt": "And where to buy <strong>more</strong>!",
  "excerpt_or_content": "And where to buy <strong>more</strong>!",
  "handle": "potion-notions/how-to-tell-if-you-have-run-out-of-invisibility-potion",
  "id": 556510085185,
  "image": {},
  "metafields": {},
  "moderated?": true,
  "published_at": "2022-04-14 16:56:02 -0400",
  "tags": [],
  "template_suffix": "",
  "title": "How to tell if you're out of invisibility potion",
  "updated_at": "2022-06-04 19:27:33 -0400",
  "url": {},
  "user": {}
}
```

#### Templates using article

- [Theme architecture](https://shopify.dev/themes/architecture/templates/article)
- [article template](https://shopify.dev/themes/architecture/templates/article)

---

### articles

> Fonte: https://shopify.dev/docs/api/liquid/objects/articles

All of the articles across the blogs in the store.

#### Directly accessible in

* Global

You can use `articles` to access an article by its [handle](https://shopify.dev/docs/api/liquid/basics#handles).

#### Example

**Input:**
```liquid
{% assign article = articles['potion-notions/new-potions-for-spring'] %}
{{ article.title | link_to: article.url }}
```

**Output:**
```html
<a href="/blogs/potion-notions/new-potions-for-spring" title="">New potions for spring</a>
```

---

### block

> Fonte: https://shopify.dev/docs/api/liquid/objects/block

The content and settings of a [section block](https://shopify.dev/themes/architecture/sections/section-schema#blocks).

Sections and blocks are reusable modules of content that comprise [templates](https://shopify.dev/themes/architecture/templates).

You can include a maximum of 50 blocks in a section. To learn more about using blocks, refer to [Building with sections and blocks](https://shopify.dev/docs/themes/best-practices/templates-sections-blocks).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| id | string | The ID of the block. The ID is dynamically generated by Shopify and is subject to change. You should avoid relying on a literal value of this ID. |
| settings | object | The [settings](https://shopify.dev/themes/architecture/sections/section-schema#blocks) of the block. To learn about accessing settings, refer to [Access settings](https://shopify.dev/themes/architecture/settings#access-settings). To learn which input settings can be applied to the `type` property within settings, refer to [Input settings](https://shopify.dev/themes/architecture/settings/input-settings). |
| shopify_attributes | string | The data attributes for the block for use in the theme editor. The theme editor's [JavaScript API](https://shopify.dev/themes/best-practices/editor/integrate-sections-and-blocks#section-and-block-javascript-events) uses the data attributes to identify blocks and listen for events. No value for `block.shopify_attributes` is returned outside the theme editor. |
| type | string | The type of the block. The type is a free-form string defined in the [block's schema](https://shopify.dev/themes/architecture/sections/section-schema#blocks). You can use the type as an identifier. For example, you might display different markup based on the block type. |

#### Example

```json
{
  "id": "column1",
  "settings": "array",
  "shopify_attributes": "data-shopify-editor-block=\"{\"id\":\"column1\",\"type\":\"column\"}\"",
  "type": "column"
}
```

---

### blog

> Fonte: https://shopify.dev/docs/api/liquid/objects/blog

Information about a specific [blog](https://help.shopify.com/manual/online-store/blogs/adding-a-blog) in the store.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| all_tags | array of string | All of the tags on the articles in the blog. This includes tags of articles that aren't in the current pagination view. |
| articles | array of article | The articles in the blog. Use the paginate tag to choose how many articles to show per page, up to a limit of 50. |
| articles_count | number | The total number of articles in the blog. This total doesn't include hidden articles. |
| comments_enabled? | boolean | Returns `true` if comments are enabled for the blog; returns `false` otherwise. |
| handle | string | The [handle](https://shopify.dev/docs/api/liquid/basics#handles) of the blog. |
| id | number | The ID of the blog. |
| metafields | array of metafield | The [metafields](https://shopify.dev/docs/api/liquid/objects/metafield) applied to the blog. |
| moderated? | boolean | Returns `true` if the blog is set to moderate comments; returns `false` otherwise. |
| next_article | article | The next (older) article in the blog. Returns `nil` if there is no next article. |
| previous_article | article | The previous (newer) article in the blog. Returns `nil` if there is no previous article. |
| tags | array of string | A list of all of the tags on all of the articles in the blog. Unlike `blog.all_tags`, only returns tags from filtered articles. |
| template_suffix | string | The name of the [custom template](https://shopify.dev/themes/architecture/templates#alternate-templates) assigned to the blog. Returns `nil` if none assigned. |
| title | string | The title of the blog. |
| url | string | The relative URL of the blog. |

#### Example

```json
{
  "all_tags": [],
  "articles": [],
  "articles_count": 3,
  "comments_enabled?": true,
  "handle": "potion-notions",
  "id": 78580613185,
  "metafields": {},
  "moderated?": true,
  "next_article": {},
  "previous_article": {},
  "tags": [],
  "template_suffix": "",
  "title": "Potion Notions",
  "url": "/blogs/potion-notions"
}
```

#### Templates using blog

- [blog template](https://shopify.dev/themes/architecture/templates/blog)
- [article template](https://shopify.dev/themes/architecture/templates/article)

---

### blogs

> Fonte: https://shopify.dev/docs/api/liquid/objects/blogs

All of the blogs in the store.

#### Directly accessible in

* Global

You can use `blogs` to access a blog by its [handle](https://shopify.dev/docs/api/liquid/basics#handles).

#### Example

**Input:**
```liquid
{% for article in blogs.potion-notions.articles %}
  {{- article.title | link_to: article.url }}
{% endfor %}
```

**Output:**
```html
<a href="/blogs/potion-notions/homebrew-start-making-potions-at-home" title="">Homebrew: start making potions at home</a>

<a href="/blogs/potion-notions/new-potions-for-spring" title="">New potions for spring</a>

<a href="/blogs/potion-notions/how-to-tell-if-you-have-run-out-of-invisibility-potion" title="">How to tell if you're out of invisibility potion</a>
```

---

### brand

> Fonte: https://shopify.dev/docs/api/liquid/objects/brand

The [brand assets](https://help.shopify.com/manual/promoting-marketing/managing-brand-assets) for the store.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| colors | | The brand's colors. To learn about how to access brand colors, refer to [`brand_color`](https://shopify.dev/docs/api/liquid/objects/brand_color). |
| cover_image | [image](https://shopify.dev/docs/api/liquid/objects/image) | The square logo for the brand, resized to 32x32 px. |
| favicon_url | [image](https://shopify.dev/docs/api/liquid/objects/image) | The square logo for the brand, resized to 32x32 px. |
| logo | [image](https://shopify.dev/docs/api/liquid/objects/image) | The default logo for the brand. |
| metafields | | The social links for the brand. Social links are stored in [metafields](https://shopify.dev/docs/api/liquid/objects/metafield), and can be accessed using the syntax `shop.brand.metafields.social_links.<platform>.value`. |
| short_description | [string](https://shopify.dev/docs/api/liquid/basics#string) | A short description of the brand. |
| slogan | [string](https://shopify.dev/docs/api/liquid/basics#string) | The slogan for the brand. |
| square_logo | [image](https://shopify.dev/docs/api/liquid/objects/image) | The square logo for the brand. |

##### Social Link Platforms

| Platform |
|----------|
| `facebook` |
| `pinterest` |
| `instagram` |
| `tiktok` |
| `tumblr` |
| `snapchat` |
| `vimeo` |

#### Example: Access social links

**Code**
```liquid
{{ shop.brand.metafields.social_links.twitter.value }}
{{ shop.brand.metafields.social_links.youtube.value }}
```

**Output**
```html
https://twitter.com/ShopifyDevs
https://www.youtube.com/c/shopifydevs
```

#### Example: brand object

```json
{
  "colors": {},
  "cover_image": {},
  "favicon_url": {},
  "logo": {},
  "metafields": {},
  "short_description": "Canada's foremost retailer for potions and potion accessories. Try one of our award-winning artisanal potions, or find the supplies to make your own!",
  "slogan": "Save the toil and trouble!",
  "square_logo": {}
}
```

---

### brand_color

> Fonte: https://shopify.dev/docs/api/liquid/objects/brand_color

The colors defined as part of a store's [brand assets](https://help.shopify.com/manual/promoting-marketing/managing-brand-assets).

#### Returned by

* [brand.colors](https://shopify.dev/docs/api/liquid/objects/brand#brand-colors)

#### Accessing brand colors

To access a brand color, specify the following:

* The brand color group: either `primary` or `secondary`
* The color role: Whether the color is a `background` or `foreground` (contrasting) color
* The 0-based index of the color within the group and role

##### Example

**Liquid:**
```liquid
{{ shop.brand.colors.primary[0].background }}
{{ shop.brand.colors.primary[0].foreground }}
{{ shop.brand.colors.secondary[0].background }}
{{ shop.brand.colors.secondary[1].background }}
{{ shop.brand.colors.secondary[0].foreground }}
```

**Output:**
```html
#0b101f
#DDE2F1
#101B2E
#95A7D5
#A3DFFD
```

---

### canonical_url

> Fonte: https://shopify.dev/docs/api/liquid/objects/canonical_url

The canonical URL for the current page.

To learn about canonical URLs, refer to [Google's documentation](https://support.google.com/webmasters/answer/139066?hl=en).

#### Directly accessible in

* Global

---

### cart

> Fonte: https://shopify.dev/docs/api/liquid/objects/cart

A customer's cart.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| attributes | object | Additional attributes entered by the customer with the cart. |
| cart_level_discount_applications | array of [discount_application](https://shopify.dev/docs/api/liquid/objects/discount_application) | The cart-specific discount applications for the cart. |
| checkout_charge_amount | [number](https://shopify.dev/docs/api/liquid/basics#number) | The amount that the customer will be charged at checkout in the currency's subunit. The value is output in the customer's local (presentment) currency. For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. |
| currency | object | The currency of the cart. If the store uses multi-currency, then this is the same as the customer's local (presentment) currency. Otherwise, it's the same as the store currency. |
| discount_applications | array of [discount_application](https://shopify.dev/docs/api/liquid/objects/discount_application) | The discount applications for the cart. |
| duties_included | [boolean](https://shopify.dev/docs/api/liquid/basics#boolean) | Returns `true` if duties are included in the prices of products in the cart. Returns `false` if not. |
| empty? | [boolean](https://shopify.dev/docs/api/liquid/basics#boolean) | Returns `true` if there are no items in the cart. Returns `false` if there are. |
| item_count | [number](https://shopify.dev/docs/api/liquid/basics#number) | The number of items in the cart. |
| items | array of [line_item](https://shopify.dev/docs/api/liquid/objects/line_item) | The line items in the cart. |
| items_subtotal_price | [number](https://shopify.dev/docs/api/liquid/basics#number) | The total price of all items in the cart in the currency's subunit, after line item discounts. Excludes taxes, cart discounts, and shipping costs. |
| note | [string](https://shopify.dev/docs/api/liquid/basics#string) | Additional information captured with the cart. |
| original_total_price | [number](https://shopify.dev/docs/api/liquid/basics#number) | The total price of all items in the cart in the currency's subunit, before discounts. |
| requires_shipping | [boolean](https://shopify.dev/docs/api/liquid/basics#boolean) | Returns `true` if any products in the cart require shipping. Returns `false` if not. |
| taxes_included | [boolean](https://shopify.dev/docs/api/liquid/basics#boolean) | Returns `true` if taxes are included in product prices. Returns `false` if not. |
| total_discount | [number](https://shopify.dev/docs/api/liquid/basics#number) | The total amount of all discounts (savings) for the cart in the currency's subunit. |
| total_price | [number](https://shopify.dev/docs/api/liquid/basics#number) | The total price of all items in the cart in the currency's subunit, after discounts. |
| total_weight | [number](https://shopify.dev/docs/api/liquid/basics#number) | The total weight of all items in the cart in grams. |

#### Capture cart attributes

```liquid
<label>What do you want engraved on your cauldron?</label>
<input type="text" name="attributes[cauldron-engraving]" value="{{ cart.attributes.cauldron-engraving }}" />
```

#### Display cart-level discount applications

**Code:**
```liquid
{% for discount_application in cart.cart_level_discount_applications %}
  Discount name: {{ discount_application.title }}
  Savings: -{{ discount_application.total_allocated_amount | money }}
{% endfor %}
```

**Data:**
```json
{
  "cart": {
    "cart_level_discount_applications": [
      {
        "title": "Ingredient Sale",
        "total_allocated_amount": "42.24"
      }
    ]
  }
}
```

**Output:**
```html
Discount name: Ingredient Sale
  Savings: -$42.24
```

#### Display discount applications

**Code:**
```liquid
{% for discount_application in cart.discount_applications %}
  Discount name: {{ discount_application.title }}
  Savings: -{{ discount_application.total_allocated_amount | money }}
{% endfor %}
```

**Data:**
```json
{
  "cart": {
    "discount_applications": [
      {
        "title": "Bloodroot discount!",
        "total_allocated_amount": "2.50"
      },
      {
        "title": "Ingredient Sale",
        "total_allocated_amount": "42.24"
      }
    ]
  }
}
```

**Output:**
```html
Discount name: Bloodroot discount!
  Savings: -$2.50

  Discount name: Ingredient Sale
  Savings: -$42.24
```

#### Capture cart notes

```liquid
<label>Gift note:</label>
<textarea name="note"></textarea>
```

#### Deprecated Properties

| Property | Type | Description |
|----------|------|-------------|
| discounts | array of [discount](https://shopify.dev/docs/api/liquid/objects/discount) | **Deprecated:** Use `cart.discount_applications` instead. Not all discount types and details are available. |

#### Example

```json
{
  "attributes": {},
  "cart_level_discount_applications": [],
  "checkout_charge_amount": "380.25",
  "currency": {},
  "discount_applications": [],
  "discounts": [],
  "duties_included": false,
  "empty?": false,
  "item_count": 2,
  "items": [],
  "items_subtotal_price": "422.49",
  "note": "Hello this is a note",
  "original_total_price": "424.99",
  "requires_shipping": true,
  "taxes_included": false,
  "total_discount": "44.74",
  "total_price": "380.25",
  "total_weight": 0
}
```

---

### checkout

> Fonte: https://shopify.dev/docs/api/liquid/objects/checkout

A customer's checkout.

> The `checkout` object will be deprecated for the Information, Shipping, and Payment pages on August 13, 2024. Merchants who have customized these pages using `checkout.liquid` need to upgrade to Checkout Extensibility before August 13, 2024.

You can access the `checkout` object on the **Order status** page. Shopify Plus merchants can access the `checkout` object in the `checkout.liquid` layout.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| applied_gift_cards | array of [gift_card](https://shopify.dev/docs/api/liquid/objects/gift_card) | The gift cards applied to the checkout. |
| attributes | object | Additional attributes entered by the customer with the cart. Shopify Plus merchants that have access to `checkout.liquid` can capture attributes at checkout. |
| billing_address | [address](https://shopify.dev/docs/api/liquid/objects/address) | The billing address entered at checkout. |
| buyer_accepts_marketing | [boolean](https://shopify.dev/docs/api/liquid/basics#boolean) | Returns `true` if the customer checks the email marketing subscription checkbox. Returns `false` if not. |
| cart_level_discount_applications | array of [discount_application](https://shopify.dev/docs/api/liquid/objects/discount_application) | The cart-specific discount applications for the checkout. |
| currency | [string](https://shopify.dev/docs/api/liquid/basics#string) | The ISO code of the currency of the checkout. |
| customer | [customer](https://shopify.dev/docs/api/liquid/objects/customer) | The customer associated with the checkout. The `customer` object is directly accessible globally when a customer is logged in to their account. |
| discount_applications | array of [discount_application](https://shopify.dev/docs/api/liquid/objects/discount_application) | The discount applications for the checkout. |
| discounts_amount | [number](https://shopify.dev/docs/api/liquid/basics#number) | The total amount of the discounts applied to the checkout in the currency's subunit, output in the customer's local (presentment) currency. For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. |
| discounts_savings | [number](https://shopify.dev/docs/api/liquid/basics#number) | The total amount of the discounts applied to the checkout in the currency's subunit, as a negative value, output in the customer's local (presentment) currency. For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. |
| email | [string](https://shopify.dev/docs/api/liquid/basics#string) | The email associated with the checkout. |
| gift_cards_amount | [number](https://shopify.dev/docs/api/liquid/basics#number) | The amount of the checkout price paid in gift cards, output in the customer's local (presentment) currency. |
| id | [number](https://shopify.dev/docs/api/liquid/basics#number) | The ID of the checkout. |
| item_count | [number](https://shopify.dev/docs/api/liquid/basics#number) | The number of items in the checkout. |
| line_items | array of [line_item](https://shopify.dev/docs/api/liquid/objects/line_item) | The line items of the checkout. |
| line_items_subtotal_price | [number](https://shopify.dev/docs/api/liquid/basics#number) | The sum of the prices of all line items of the checkout in the currency's subunit, after any line item discounts have been applied, output in the customer's local (presentment) currency. |
| name | [number](https://shopify.dev/docs/api/liquid/basics#number) | The name of the checkout. This value is the same as `checkout.id` with a `#` prepended to it. |
| note | [string](https://shopify.dev/docs/api/liquid/basics#string) | Additional information entered by the customer with the cart. |
| order | [order](https://shopify.dev/docs/api/liquid/objects/order) | The order created by the checkout. Depending on the payment provider, the order might not have been created when the Thank you page is first viewed. In this case, `nil` is returned. |
| order_id | [string](https://shopify.dev/docs/api/liquid/basics#string) | The ID of the order created by the checkout. The value is the same as `order.id`. Depending on the payment provider, the order might not have been created when the Order status page is first viewed. In this case, `nil` is returned. |
| order_name | [string](https://shopify.dev/docs/api/liquid/basics#string) | The name of the order created by the checkout. The value is the same as `order.name`. Depending on the payment provider, the order might not have been created when the Order status page is first viewed. In this case, `nil` is returned. |
| order_number | [string](https://shopify.dev/docs/api/liquid/basics#string) | An integer representation of the name of the order created by the checkout. The value is the same as `order.order_number`. Depending on the payment provider, the order might not have been created when the Order status page is first viewed. In this case, `nil` is returned. |
| requires_shipping | [boolean](https://shopify.dev/docs/api/liquid/basics#boolean) | Returns `true` if any of the line items of the checkout require shipping. Returns `false` if not. |
| shipping_address | [address](https://shopify.dev/docs/api/liquid/objects/address) | The shipping address of the checkout. |
| shipping_method | [shipping_method](https://shopify.dev/docs/api/liquid/objects/shipping_method) | The shipping method of the checkout. |
| shipping_price | [number](https://shopify.dev/docs/api/liquid/basics#number) | The shipping price of the checkout in the currency's subunit, output in the customer's local (presentment) currency. For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. |
| tax_lines | array of [tax_line](https://shopify.dev/docs/api/liquid/objects/tax_line) | The tax lines for the checkout. |
| tax_price | [number](https://shopify.dev/docs/api/liquid/basics#number) | The total tax amount of the checkout in the currency's subunit, output in the customer's local (presentment) currency. For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. |
| total_price | [number](https://shopify.dev/docs/api/liquid/basics#number) | The total price of the checkout in the currency's subunit, output in the customer's local (presentment) currency. For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. |
| transactions | array of [transaction](https://shopify.dev/docs/api/liquid/objects/transaction) | The transactions of the checkout. |

#### Deprecated Properties

| Property | Type | Description |
|----------|------|-------------|
| cancelled | [boolean](https://shopify.dev/docs/api/liquid/basics#boolean) | **Deprecated.** Returns `true` if the checkout has been cancelled. Returns `false` if not. Deprecated because `false` is always returned. |
| discount | [discount](https://shopify.dev/docs/api/liquid/objects/discount) | **Deprecated.** A discount applied to the checkout without being saved. Deprecated because an unsaved discount doesn't exist on the Order status page. |
| discounts | array of [discount](https://shopify.dev/docs/api/liquid/objects/discount) | **Deprecated.** The discounts applied to the checkout. Deprecated because not all discount types and details are captured. The `checkout.discounts` property has been replaced by `checkout.discount_applications`. |
| financial_status | [string](https://shopify.dev/docs/api/liquid/basics#string) | **Deprecated.** The financial status of the checkout. Deprecated because `nil` is always returned. |
| fulfilled_at | [string](https://shopify.dev/docs/api/liquid/basics#string) | **Deprecated.** A timestamp for the fulfillment of the checkout. Deprecated because `nil` is always returned. |
| fulfilled_line_items | array of [line_item](https://shopify.dev/docs/api/liquid/objects/line_item) | **Deprecated.** The fulfilled line items from the checkout. Deprecated because the array is always empty. |
| fulfillment_status | [string](https://shopify.dev/docs/api/liquid/basics#string) | **Deprecated.** The fulfillment status of the checkout. Deprecated because `unfulfilled` is always returned. |
| unavailable_line_items | array of [line_item](https://shopify.dev/docs/api/liquid/objects/line_item) | **Deprecated.** The unavailable line items of the checkout. Deprecated because the array is always empty. |
| unfulfilled_line_items | array of [line_item](https://shopify.dev/docs/api/liquid/objects/line_item) | **Deprecated.** The unfulfilled line items of the checkout. Deprecated because the array is always the same as `checkout.line_items`. |

#### Example

```json
{
  "applied_gift_cards": [],
  "attributes": {},
  "billing_address": {},
  "buyer_accepts_marketing": false,
  "cart_level_discount_applications": [],
  "currency": "CAD",
  "customer": {},
  "discount_applications": [],
  "discounts_amount": 4224,
  "discounts_savings": -4224,
  "email": "cornelius.potionmaker@gmail.com",
  "gift_cards_amount": 0,
  "id": 29944051400769,
  "line_items": [],
  "line_items_subtotal_price": 42249,
  "name": "#29944051400769",
  "note": null,
  "order": null,
  "order_id": null,
  "order_name": "#29944051400769",
  "order_number": "#29944051400769",
  "requires_shipping": true,
  "shipping_address": {},
  "shipping_method": {},
  "shipping_price": 0,
  "tax_lines": [],
  "tax_price": 0,
  "total_price": 38025,
  "transactions": []
}
```

---

### collection

> Fonte: https://shopify.dev/docs/api/liquid/objects/collection

A [collection](https://help.shopify.com/manual/products/collections) in a store.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| all_products_count | number | The total number of products in a collection. This includes products that have been filtered out of the current view. To display filtered collection product counts, use `collection.products_count`. |
| all_tags | array of string | All of the tags applied to the products in the collection. This includes tags for products that have been filtered out of the current view. Maximum of 1,000 tags returned. For currently applied tags, use `collection.tags`. |
| all_types | array of string | All of the product types in a collection. |
| all_vendors | array of string | All of the product vendors in a collection. |
| current_type | string | The product type on a product type collection page. You can query for products of a certain type at the `/collections/types` URL with a query parameter in the format of `?q=[type]`. Query values are case-insensitive. |
| current_vendor | string | The vendor name on a vendor collection page. You can query for products from a certain vendor at the `/collections/vendors` URL with a query parameter in the format of `?q=[vendor]`. Query values are case-insensitive. |
| default_sort_by | string | The default sort order of the collection. This is set on the collection's page in the Shopify admin. Possible values: manual, best-selling, title-ascending, price-ascending, price-descending, created-ascending, created-descending |
| description | string | The description of the collection. |
| featured_image | image | The featured image for the collection. The default is the collection image. If this image isn't available, then Shopify falls back to the featured image of the first product in the collection. Returns `nil` if unavailable. |
| filters | array of filter | The storefront filters that have been set up on the collection. Only filters relevant to the current collection are returned. Empty for collections over 5000 products. |
| handle | string | The handle of the collection. |
| id | number | The ID of the collection. |
| image | image | The image for the collection. This image is added on the collection's page in the Shopify admin. |
| metafields | array of metafield | The metafields applied to the collection. |
| next_product | product | The next product in the collection. Returns `nil` if there's no next product. Use on product pages for navigation links. |
| previous_product | product | The previous product in the collection. Returns `nil` if there's no previous product. Use on product pages for navigation links. |
| products | array of product | All of the products in the collection. Use the paginate tag to choose how many products to show per page, up to a limit of 50. |
| products_count | number | The total number of products in the current view of the collection. |
| published_at | string | A timestamp for when the collection was published. Use the date filter to format the timestamp. |
| sort_by | string | The sort order applied to the collection by the `sort_by` URL parameter. If there's no `sort_by` URL parameter, then the value is `nil`. |
| sort_options | array of sort_option | The available sorting options for the collection. |
| tags | array of string | The tags that are currently applied to the collection. This doesn't include tags for products that have been filtered out of the current view. Returns `nil` if no tags applied. |
| template_suffix | string | The name of the custom template assigned to the collection. The name doesn't include the `collection.` prefix, or the file extension. Returns `nil` if not assigned. |
| title | string | The title of the collection. |
| url | string | The relative URL of the collection. |

#### Examples

##### Create links to product types

**Code:**
```liquid
{% for product_type in collection.all_types -%}
  {{- product_type | link_to_type }}
{%- endfor %}
```

**Data:**
```json
{
  "collection": {
    "all_types": [
      "Animals & Pet Supplies",
      "Baking Flavors & Extracts",
      "Cooking & Baking Ingredients",
      "Dried Flowers",
      "Fruits & Vegetables",
      "Seasonings & Spices",
      "Water"
    ]
  }
}
```

**Output:**
```html
<a href="/collections/types?q=Animals%20%26%20Pet%20Supplies" title="Animals &amp; Pet Supplies">Animals & Pet Supplies</a>
<a href="/collections/types?q=Baking%20Flavors%20%26%20Extracts" title="Baking Flavors &amp; Extracts">Baking Flavors & Extracts</a>
<a href="/collections/types?q=Cooking%20%26%20Baking%20Ingredients" title="Cooking &amp; Baking Ingredients">Cooking & Baking Ingredients</a>
<a href="/collections/types?q=Dried%20Flowers" title="Dried Flowers">Dried Flowers</a>
<a href="/collections/types?q=Fruits%20%26%20Vegetables" title="Fruits &amp; Vegetables">Fruits & Vegetables</a>
<a href="/collections/types?q=Seasonings%20%26%20Spices" title="Seasonings &amp; Spices">Seasonings & Spices</a>
<a href="/collections/types?q=Water" title="Water">Water</a>
```

##### Create links to vendors

**Code:**
```liquid
{% for product_vendor in collection.all_vendors %}
  {{- product_vendor | link_to_vendor }}
{% endfor %}
```

**Data:**
```json
{
  "collection": {
    "all_vendors": [
      "Clover's Apothecary",
      "Polina's Potent Potions",
      "Ted's Apothecary Supply"
    ]
  }
}
```

**Output:**
```html
<a href="/collections/vendors?q=Clover%27s%20Apothecary" title="Clover&#39;s Apothecary">Clover's Apothecary</a>

<a href="/collections/vendors?q=Polina%27s%20Potent%20Potions" title="Polina&#39;s Potent%20Potions">Polina's Potent Potions</a>

<a href="/collections/vendors?q=Ted%27s%20Apothecary%20Supply" title="Ted&#39;s Apothecary%20Supply">Ted's Apothecary Supply</a>
```

##### Output the sort options

**Code:**
```liquid
{%- assign sort_by = collection.sort_by | default: collection.default_sort_by -%}

<select>
{%- for option in collection.sort_options %}
  <option
    value="{{ option.value }}"
    {%- if option.value == sort_by %}
      selected="selected"
    {%- endif %}
  >
    {{ option.name }}
  </option>
{% endfor -%}
</select>
```

**Data:**
```json
{
  "collection": {
    "default_sort_by": "title-ascending",
    "sort_by": "",
    "sort_options": [
      "CollectionDrop::SortOptionDrop",
      "CollectionDrop::SortOptionDrop",
      "CollectionDrop::SortOptionDrop",
      "CollectionDrop::SortOptionDrop",
      "CollectionDrop::SortOptionDrop",
      "CollectionDrop::SortOptionDrop",
      "CollectionDrop::SortOptionDrop",
      "CollectionDrop::SortOptionDrop",
      "CollectionDrop::SortOptionDrop"
    ]
  }
}
```

**Output:**
```html
<select>
  <option
    value="manual"
  >
    Featured
  </option>

  <option
    value="most-relevant"
  >
    Most relevant
  </option>

  <option
    value="best-selling"
  >
    Best selling
  </option>

  <option
    value="title-ascending"
      selected="selected"
  >
    Alphabetically, A-Z
  </option>

  <option
    value="title-descending"
  >
    Alphabetically, Z-A
  </option>

  <option
    value="price-ascending"
  >
    Price, low to high
  </option>

  <option
    value="price-descending"
  >
    Price, high to low
  </option>

  <option
    value="created-ascending"
  >
    Date, old to new
  </option>

  <option
    value="created-descending"
  >
    Date, new to old
  </option>
</select>
```

#### Full Example Data

```json
{
  "all_products_count": 10,
  "all_tags": [
    "Burning",
    "dried",
    "extracts",
    "fresh",
    "ingredients",
    "plant",
    "supplies"
  ],
  "all_types": [
    "Animals & Pet Supplies",
    "Baking Flavors & Extracts",
    "Cooking & Baking Ingredients",
    "Dried Flowers",
    "Fruits & Vegetables",
    "Seasonings & Spices",
    "Water"
  ],
  "all_vendors": [
    "Clover's Apothecary",
    "Polina's Potent Potions",
    "Ted's Apothecary Supply"
  ],
  "current_type": null,
  "current_vendor": null,
  "default_sort_by": "created-ascending",
  "description": "Brew your own potions at home using our fresh, ethically-sourced ingredients.",
  "featured_image": {},
  "filters": {},
  "handle": "ingredients",
  "id": 266168401985,
  "image": {},
  "metafields": {},
  "next_product": null,
  "previous_product": null,
  "products": {},
  "products_count": 1,
  "published_at": "2022-04-19 09:52:18 -0400",
  "sort_by": "",
  "sort_options": [],
  "tags": [
    "Burning"
  ],
  "template_suffix": "eight-products-per-page",
  "title": "Ingredients",
  "url": {}
}
```

---

### collections

> Fonte: https://shopify.dev/docs/api/liquid/objects/collections

All of the [collections](https://shopify.dev/docs/api/liquid/objects/collection) on a store.

#### Directly accessible in

* Global

#### Iterate over the collections

You can iterate over `collections` to build a collection list.

**Code:**
```liquid
{% for collection in collections %}
  {{- collection.title | link_to: collection.url }}
{% endfor %}
```

**Output:**
```html
<a href="/collections/empty" title="">Empty</a>

<a href="/collections/featured-potions" title="">Featured potions</a>

<a href="/collections/freebies" title="">Freebies</a>

<a href="/collections/frontpage" title="">Home page</a>

<a href="/collections/ingredients" title="">Ingredients</a>

<a href="/collections/potions" title="">Potions</a>

<a href="/collections/sale-potions" title="">Sale potions</a>
```

#### Access a specific collection

You can use `collections` to access a collection by its [handle](https://shopify.dev/docs/api/liquid/basics#handles).

**Code:**
```liquid
{% for product in collections['sale-potions'].products %}
  {{- product.title | link_to: product.url }}
{% endfor %}
```

**Output:**
```html
<a href="/products/draught-of-immortality" title="">Draught of Immortality</a>

<a href="/products/glacier-ice" title="">Glacier ice</a>

<a href="/products/health-potion" title="">Health potion</a>

<a href="/products/invisibility-potion" title="">Invisibility potion</a>
```

---

### color

> Fonte: https://shopify.dev/docs/api/liquid/objects/color

A color from a [`color` setting](https://shopify.dev/themes/architecture/settings/input-settings#color).

> Use color filters to modify or extract properties of a `color` object.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| alpha | number | The alpha component of the color, which is a decimal number between 0.0 and 1.0. |
| blue | number | The blue component of the color, which is a number between 0 and 255. |
| chroma | number | The chroma component of the color, which is a decimal number between 0.0 and 0.5. |
| color_space | string | The color space of the color. Returns 'srgb' or 'oklch' |
| green | number | The green component of the color, which is a number between 0 and 255. |
| hue | number | The hue component of the color, which is a number between 0 and 360. |
| lightness | number | The lightness component of the color, which is a number between 0 and 100. |
| oklch | string | The lightness, chroma, and hue values of the color, represented as a space-separated string. |
| oklcha | string | The lightness, chroma, hue and alpha values of the color, represented as a space-separated string, with a slash before the alpha channel. |
| red | number | The red component of the color, which is a number between 0 and 255. |
| rgb | string | The red, green, and blue values of the color, represented as a space-separated string. |
| rgba | string | The red, green, blue, and alpha values of the color, represented as a space-separated string, with a slash before the alpha channel. |
| saturation | number | The saturation component of the color, which is a number between 0 and 100. |

#### Example

```json
{
  "alpha": 1,
  "blue": 180,
  "chroma": 0.16,
  "color_space": "srgb",
  "green": 79,
  "hue": 227,
  "lightness": 45,
  "oklch": "47% 0.16 268",
  "oklcha": "47% 0.16 268 / 1.0",
  "red": 51,
  "rgb": "51 79 180",
  "rgba": "51 79 180 / 1.0",
  "saturation": 56
}
```

#### Referencing color settings directly

When a color setting is referenced directly, the hexidecimal color code is returned.

**Code:**
```liquid
{{ settings.colors_accent_2 }}
```

**Data:**
```json
{
  "settings": {
    "colors_accent_2": "#334fb4"
  }
}
```

**Output:**
```html
#334fb4
```

---

### color_scheme

> Fonte: https://shopify.dev/docs/api/liquid/objects/color_scheme

A color_scheme from a `color_scheme` setting.

> To learn about color scheme groups in themes, refer to `color_scheme_group` setting.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| id | string | The ID of the color_scheme |
| settings | object | The settings of the color_scheme |

#### Example

```json
{
  "id": "background-2",
  "settings": {}
}
```

#### Referencing color_scheme settings directly

When a color_scheme setting is referenced directly, the color scheme ID is returned.

**Liquid input:**
```liquid
{{ settings.card_color_scheme }}
```

**Data:**
```json
{
  "settings": {
    "card_color_scheme": {}
  }
}
```

**Output:**
```html
background-2
```

---

### color_scheme_group

> Fonte: https://shopify.dev/docs/api/liquid/objects/color_scheme_group

A color_scheme_group from a [`color_scheme_group` setting](https://shopify.dev/themes/architecture/settings/input-settings#color_scheme_group).

> To learn about color schemes in themes, refer to [color_scheme setting](https://shopify.dev/themes/architecture/settings/input-settings#color_scheme).

#### Example

```json
{}
```

#### Referencing color_scheme_group settings directly

**Code:**
```liquid
{% for scheme in settings.color_schemes %}
  .color-{{ scheme.id }} {
    --color-background: {{ scheme.settings.background }};
    --color-text: {{ scheme.settings.text }};
  }
{% endfor %}
```

**Data:**
```json
{
  "settings": {
    "color_schemes": {}
  }
}
```

**Output:**
```html
.color-background-1 {
    --color-background: #FFFFFF;
    --color-text: #121212;
  }

  .color-background-2 {
    --color-background: #F3F3F3;
    --color-text: #121212;
  }

  .color-inverse {
    --color-background: #121212;
    --color-text: #FFFFFF;
  }

  .color-accent-1 {
    --color-background: #121212;
    --color-text: #FFFFFF;
  }

  .color-accent-2 {
    --color-background: #334FB4;
    --color-text: #FFFFFF;
  }
```

---

### comment

> Fonte: https://shopify.dev/docs/api/liquid/objects/comment

An article comment.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| author | string | The full name of the author of the comment. |
| content | string | The content of the comment. |
| created_at | string | A timestamp for when the comment was created. Use the `date` filter to format the timestamp. |
| email | string | The email of the author of the comment. |
| id | number | The ID of the comment. |
| status | string | The status of the comment. Always returns `published`. Outside of the Liquid context, the status can vary based on spam detection and moderation, but only `published` comments appear in the `article.comments` array. |
| updated_at | string | A timestamp for when the comment status was last updated. Use the `date` filter to format the timestamp. |
| url | string | The relative URL of the associated article with the `comment.id` appended. |

#### Example

```json
{
  "author": "Cornelius",
  "content": "Wow, this is going to save me a fortune in invisibility potion!",
  "created_at": "2022-06-05 19:33:57 -0400",
  "email": "cornelius.potionmaker@gmail.com",
  "id": 129089273921,
  "status": "published",
  "updated_at": "2022-06-05 19:33:57 -0400",
  "url": "/blogs/potion-notions/how-to-tell-if-you-have-run-out-of-invisibility-potion#129089273921"
}
```

---

### company

> Fonte: https://shopify.dev/docs/api/liquid/objects/company

A company that a [customer](https://shopify.dev/docs/api/liquid/objects/customer) is purchasing for.

To learn about B2B in themes, refer to [Support B2B customers in your theme](https://shopify.dev/themes/pricing-payments/b2b).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| available_locations | array of [company_location](https://shopify.dev/docs/api/liquid/objects/company_location) | The company locations that the current customer has access to, or can interact with. |
| available_locations_count | [number](https://shopify.dev/docs/api/liquid/basics#number) | The number of company locations associated with the customer's company. |
| external_id | [string](https://shopify.dev/docs/api/liquid/basics#string) | The external ID of the company. |
| id | [number](https://shopify.dev/docs/api/liquid/basics#number) | The ID of the company. |
| metafields | array of [metafield](https://shopify.dev/docs/api/liquid/objects/metafield) | The [metafields](https://shopify.dev/docs/api/liquid/objects/metafield) applied to the company. |
| name | [string](https://shopify.dev/docs/api/liquid/basics#string) | The name of the company. |

**Tip:** For metafield creation guidance, refer to Create and manage metafields or the Shopify Help Center.

#### Example

```json
{
  "available_locations": [],
  "available_locations_count": 1,
  "external_id": null,
  "id": 98369,
  "metafields": {},
  "name": "Cornelius&#39; Custom Concoctions"
}
```

---

### company_address

> Fonte: https://shopify.dev/docs/api/liquid/objects/company_address

The address of a company location.

To learn about B2B in themes, refer to [Support B2B customers in your theme](https://shopify.dev/themes/pricing-payments/b2b).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| address1 | [string](https://shopify.dev/docs/api/liquid/basics#string) | The first line of the address. |
| address2 | [string](https://shopify.dev/docs/api/liquid/basics#string) | The second line of the address. If no second line is specified, then `nil` is returned. |
| attention | [string](https://shopify.dev/docs/api/liquid/basics#string) | The attention line of the address. |
| city | [string](https://shopify.dev/docs/api/liquid/basics#string) | The city of the address. |
| country | [country](https://shopify.dev/docs/api/liquid/objects/country) | The country of the address. |
| country_code | [string](https://shopify.dev/docs/api/liquid/basics#string) | The country of the address in [ISO 3166-1 (alpha 2) format](https://www.iso.org/glossary-for-iso-3166.html). |
| first_name | [string](https://shopify.dev/docs/api/liquid/basics#string) | The first name of the address. |
| id | [number](https://shopify.dev/docs/api/liquid/basics#number) | The ID of the address. |
| last_name | [string](https://shopify.dev/docs/api/liquid/basics#string) | The last name of the address. |
| province | [string](https://shopify.dev/docs/api/liquid/basics#string) | The province of the address. |
| province_code | [string](https://shopify.dev/docs/api/liquid/basics#string) | The province of the address in [ISO 3166-2 (alpha 2) format](https://www.iso.org/glossary-for-iso-3166.html). Note: The value doesn't include the preceding ISO 3166-1 country code. |
| street | [string](https://shopify.dev/docs/api/liquid/basics#string) | A combination of the first and second lines of the address. |
| zip | [string](https://shopify.dev/docs/api/liquid/basics#string) | The zip or postal code of the address. |

#### Example

```json
{
  "address1": "99 Cauldron Lane",
  "address2": "Unit 4B",
  "attention": "Cornelius' Custom Concoctions",
  "city": "Edinburgh",
  "country": {},
  "country_code": "GB",
  "first_name": "Cornelius",
  "id": 65,
  "last_name": "Potionmaker",
  "province": null,
  "province_code": null,
  "street": "99 Cauldron Lane, Unit 4B",
  "zip": "EH95 1AF"
}
```

---

### company_location

> Fonte: https://shopify.dev/docs/api/liquid/objects/company_location

A location of the [company](https://shopify.dev/docs/api/liquid/objects/company) that a [customer](https://shopify.dev/docs/api/liquid/objects/customer) is purchasing for.

To learn about B2B in themes, refer to [Support B2B customers in your theme](https://shopify.dev/themes/pricing-payments/b2b).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| company | [company](https://shopify.dev/docs/api/liquid/objects/company) | The company that the location is associated with. |
| current? | [boolean](https://shopify.dev/docs/api/liquid/basics#boolean) | Returns `true` if the location is currently selected. Returns `false` if not. |
| external_id | [string](https://shopify.dev/docs/api/liquid/basics#string) | The external ID of the location. |
| id | [number](https://shopify.dev/docs/api/liquid/basics#number) | The ID of the location. |
| metafields | array of [metafield](https://shopify.dev/docs/api/liquid/objects/metafield) | The [metafields](https://shopify.dev/docs/api/liquid/objects/metafield) applied to the company location. **Tip:** To learn about how to create metafields, refer to [Create and manage metafields](/apps/metafields/manage) or visit the [Shopify Help Center](https://help.shopify.com/manual/metafields). |
| name | [string](https://shopify.dev/docs/api/liquid/basics#string) | The name of the location. |
| shipping_address | [company_address](https://shopify.dev/docs/api/liquid/objects/company_address) | The address of the location. |
| store_credit_account | [store_credit_account](https://shopify.dev/docs/api/liquid/objects/store_credit_account) | The store credit account associated with the company location. The account shown will be in the currency associated with the company location's current context. For example, when browsing a storefront for a company location in the US market, the company location's USD store credit account will be returned. If the company location does not have a USD store credit account `nil` will be returned. |
| tax_registration_id | [number](https://shopify.dev/docs/api/liquid/basics#number) | The tax ID of the location. |
| url_to_set_as_current | [string](https://shopify.dev/docs/api/liquid/basics#string) | The URL to set the location as the current location for the customer. |

#### Example

```json
{
  "company": {},
  "current?": false,
  "external_id": null,
  "id": 98369,
  "metafields": {},
  "name": "99 Cauldron Lane",
  "shipping_address": {},
  "store_credit_account": null,
  "tax_registration_id": null,
  "url_to_set_as_current": "https://polinas-potent-potions.myshopify.com/company_location/update?location_id=98369&return_to=/resource"
}
```

---

### content_for_additional_checkout_buttons

> Fonte: https://shopify.dev/docs/api/liquid/objects/content_for_additional_checkout_buttons

Returns checkout buttons for any active payment providers with offsite checkouts.

Use [`additional_checkout_buttons`](https://shopify.dev/docs/api/liquid/objects/additional_checkout_buttons) to check whether these payment providers exist, and `content_for_additional_checkout_buttons` to display the associated checkout buttons. Refer to [Accelerated checkout](https://shopify.dev/themes/pricing-payments/accelerated-checkout) for implementation guidance.

#### Example

```liquid
{% if additional_checkout_buttons %}
  {{ content_for_additional_checkout_buttons }}
{% endif %}
```

#### Directly accessible in

- Global

---

### content_for_header

> Fonte: https://shopify.dev/docs/api/liquid/objects/content_for_header

Dynamically returns all scripts required by Shopify.

Include the `content_for_header` object in your layout files between the `<head>` and `</head>` HTML tags.

> You shouldn't try to modify or parse the `content_for_header` object because the contents are subject to change, which can change the behaviour of your code.

> **Note:** The `content_for_header` object is required in `theme.liquid`.

#### Directly accessible in

- Global

---

### content_for_index

> Fonte: https://shopify.dev/docs/api/liquid/objects/content_for_index

Dynamically returns the content of [sections](https://shopify.dev/themes/architecture/sections) to be rendered on the home page.

If you use a [Liquid index template](https://shopify.dev/themes/architecture/templates/index-template) (`templates/index.liquid`), then you must include `{{ content_for_index }}` in the template. This object can't be used in JSON index templates.

#### Directly accessible in

* Global

---

### content_for_layout

> Fonte: https://shopify.dev/docs/api/liquid/objects/content_for_layout

Dynamically returns content based on the current [template](/themes/architecture/templates).

The `content_for_layout` object should be included in your [layout files](/themes/architecture/layouts) between the `<body>` and `</body>` HTML tags.

> **Note:** The `content_for_layout` object is required in `theme.liquid`.

#### Directly accessible in

* Global

---

### country

> Fonte: https://shopify.dev/docs/api/liquid/objects/country

A country supported by the store's localization options.

To learn how to use the `country` object to offer localization options in your theme, refer to [Support multiple currencies and languages](https://shopify.dev/themes/internationalization/multiple-currencies-languages).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| available_languages | array of [shop_locale](https://shopify.dev/docs/api/liquid/objects/shop_locale) | The languages that have been added to the market that this country belongs to. |
| continent | [string](https://shopify.dev/docs/api/liquid/basics#string) | The continent that the country is in. Possible values: `Africa`, `Asia`, `Central America`, `Europe`, `North America`, `Oceania`, `South America` |
| currency | [currency](https://shopify.dev/docs/api/liquid/objects/currency) | The currency used in the country. |
| iso_code | [string](https://shopify.dev/docs/api/liquid/basics#string) | The ISO code of the country in ISO 3166-1 (alpha 2) format. |
| market | [market](https://shopify.dev/docs/api/liquid/objects/market) | The market that includes this country. |
| name | [string](https://shopify.dev/docs/api/liquid/basics#string) | The name of the country. |
| popular? | [boolean](https://shopify.dev/docs/api/liquid/basics#boolean) | Returns `true` if the country is popular for this shop; otherwise `false`. Useful for sorting countries in a selector. |
| unit_system | [string](https://shopify.dev/docs/api/liquid/basics#string) | The unit system of the country. Possible values: `imperial`, `metric` |

#### Examples

##### Basic country object

```json
{
  "available_languages": [],
  "continent": "North America",
  "currency": {},
  "iso_code": "CA",
  "market": {},
  "name": "Canada",
  "popular?": false,
  "unit_system": "metric"
}
```

##### Referencing the country object directly

When referenced directly, `country.name` is returned.

**Code:**
```liquid
{% for country in localization.available_countries -%}
  {{ country }}
{%- endfor %}
```

**Data:**
```json
{
  "localization": {
    "available_countries": [
      "Afghanistan",
      "Australia",
      "Austria",
      "Belgium",
      "Canada",
      "Czechia",
      "Denmark",
      "Finland",
      "France",
      "Germany",
      "Hong Kong SAR",
      "Ireland",
      "Israel",
      "Italy",
      "Japan",
      "Malaysia",
      "Netherlands",
      "New Zealand",
      "Norway",
      "Poland",
      "Portugal",
      "Singapore",
      "South Korea",
      "Spain",
      "Sweden",
      "Switzerland",
      "United Arab Emirates",
      "United Kingdom",
      "United States"
    ]
  }
}
```

**Output:**
```html
Afghanistan
Australia
Austria
Belgium
Canada
Czechia
Denmark
Finland
France
Germany
Hong Kong SAR
Ireland
Israel
Italy
Japan
Malaysia
Netherlands
New Zealand
Norway
Poland
Portugal
Singapore
South Korea
Spain
Sweden
Switzerland
United Arab Emirates
United Kingdom
United States
```

##### Rendering a flag image

When passed to the [`image_url`](https://shopify.dev/docs/api/liquid/filters#image_url) filter, a CDN URL for the country's flag is returned. All flags are SVGs with a 4:3 aspect ratio.

**Code:**
```liquid
{{ localization.country | image_url: width: 32 | image_tag }}
```

**Data:**
```json
{
  "localization": {
    "country": "Canada"
  }
}
```

**Output:**
```html
<img src="//cdn.shopify.com/static/images/flags/ca.svg?width=32" alt="Canada" srcset="//cdn.shopify.com/static/images/flags/ca.svg?width=32 32w" width="32" height="24">
```

---

### country_option_tags

> Fonte: https://shopify.dev/docs/api/liquid/objects/country_option_tags

Creates an `<option>` tag for each country and region that's included in a shipping zone on the [Shipping](https://www.shopify.com/admin/settings/shipping) page of the Shopify admin.

An attribute called `data-provinces` is set for each `<option>`, and contains a JSON-encoded array of the country or region's subregions. If a country doesn't have any subregions, then an empty array is set for its `data-provinces` attribute.

**Tip:** To return all countries and regions included in the store's shipping zones, use [`all_country_option_tags`](/docs/api/liquid/objects/all_country_option_tags).

#### Directly accessible in

- Global

You can wrap the `country_option_tags` object in `<select>` tags to build a country option selector.

#### Example

**Liquid input:**
```liquid
<select name="country">
  {{ country_option_tags }}
</select>
```

**Output:**
```html
<select name="country">
  <option value="---" data-provinces="[]">---</option>
<option value="Afghanistan" data-provinces="[]">Afghanistan</option>
<option value="Canada" data-provinces="[[&quot;Alberta&quot;,&quot;Alberta&quot;],[&quot;British Columbia&quot;,&quot;British Columbia&quot;],[&quot;Manitoba&quot;,&quot;Manitoba&quot;],[&quot;New Brunswick&quot;,&quot;New Brunswick&quot;],[&quot;Newfoundland and Labrador&quot;,&quot;Newfoundland and Labrador&quot;],[&quot;Northwest Territories&quot;,&quot;Northwest Territories&quot;],[&quot;Nova Scotia&quot;,&quot;Nova Scotia&quot;],[&quot;Nunavut&quot;,&quot;Nunavut&quot;],[&quot;Ontario&quot;,&quot;Ontario&quot;],[&quot;Prince Edward Island&quot;,&quot;Prince Edward Island&quot;],[&quot;Quebec&quot;,&quot;Quebec&quot;],[&quot;Saskatchewan&quot;,&quot;Saskatchewan&quot;],[&quot;Yukon&quot;,&quot;Yukon&quot;]]">Canada</option>
<option value="United States" data-provinces="[[&quot;Alabama&quot;,&quot;Alabama&quot;],[&quot;Alaska&quot;,&quot;Alaska&quot;],...]">United States</option>
</select>
```

> Nota di estrazione: l'esempio originale include l'elenco completo delle subregioni per Stati Uniti e Canada. Le province canadesi sono riportate per intero; l'array completo degli stati USA è stato troncato qui con `...` per leggibilità. Fonte integrale: https://shopify.dev/docs/api/liquid/objects/country_option_tags

---

### currency

> Fonte: https://shopify.dev/docs/api/liquid/objects/currency

Information about a currency, like the ISO code and symbol.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| iso_code | string | The [ISO code](https://www.iso.org/iso-4217-currency-codes.html) of the currency. |
| name | string | The name of the currency. |
| symbol | string | The symbol of the currency. |

#### Example

```json
{
  "iso_code": "CAD",
  "name": "Canadian Dollar",
  "symbol": "$"
}
```

---

### current_page

> Fonte: https://shopify.dev/docs/api/liquid/objects/current_page

The current page number.

The `current_page` object has a value of 1 for non-paginated resources.

#### Directly accessible in

* Global

#### Code example

**Liquid input:**
```liquid
{{ page_title }}{% unless current_page == 1 %} - Page {{ current_page }}{% endunless %}
```

**Output:**
```html
Ingredients - Page 2
```

---

### current_tags

> Fonte: https://shopify.dev/docs/api/liquid/objects/current_tags

The currently applied tags.

You can add tags to articles and products. Article tags enable filtering a blog page to display only articles with specific tags. Similarly, product tags allow filtering a collection page to show only products with specific tags.

#### Directly accessible in

* [blog](https://shopify.dev/themes/architecture/templates/blog)
* [collection](https://shopify.dev/themes/architecture/templates/collection)

#### Templates using current_tags

* [blog template](https://shopify.dev/themes/architecture/templates/blog)
* [collection template](https://shopify.dev/themes/architecture/templates/collection)

---

### customer

> Fonte: https://shopify.dev/docs/api/liquid/objects/customer

A [customer](https://help.shopify.com/manual/customers) of the store.

The `customer` object is directly accessible globally when a customer is logged in to their account. It's also defined in the following contexts:

* The [`customers/account` template](https://shopify.dev/themes/architecture/templates/customers-account)
* The [`customers/addresses` template](https://shopify.dev/themes/architecture/templates/customers-addresses)
* The [`customers/order` template](https://shopify.dev/themes/architecture/templates/customers-order)
* When accessing [`checkout.customer`](https://shopify.dev/docs/api/liquid/objects/checkout#checkout-customer)
* When accessing [`gift_card.customer`](https://shopify.dev/docs/api/liquid/objects/gift_card#gift_card-customer)
* When accessing [`order.customer`](https://shopify.dev/docs/api/liquid/objects/order#order-customer)

Outside of the above contexts, if the customer isn't logged into their account, the `customer` object returns `nil`.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| accepts_marketing | boolean | Returns `true` if the customer accepts marketing. Returns `false` if not. |
| addresses | array of address | All of the addresses associated with the customer. Use the paginate tag to choose how many addresses to show at once, up to a limit of 20. |
| addresses_count | number | The number of addresses associated with the customer. |
| b2b? | boolean | Returns `true` if the customer is a B2B customer. Returns `false` if not. |
| company_available_locations | array of company_location | The company locations that the customer has access to, or can interact with. Use the paginate tag to choose how many company locations to show at once, up to a limit of 100. |
| company_available_locations_count | number | The number of company locations associated with the customer. |
| current_company | company | The company that the customer is purchasing for. |
| current_location | company_location | The currently selected company location. |
| default_address | address | The default address of the customer. |
| email | string | The email of the customer. |
| first_name | string | The first name of the customer. |
| has_account | boolean | Returns `true` if the email is tied to a customer account. Returns `false` if not. |
| has_avatar? | boolean | Returns `true` if an avatar is associated with a customer. Returns `false` if not. |
| id | number | The ID of the customer. |
| last_name | string | The last name of the customer. |
| last_order | order | The last order placed by the customer, not including test orders. |
| name | string | The full name of the customer. |
| orders | array of order | All of the orders placed by the customer. Use the paginate tag to choose how many orders to show at once, up to a limit of 20. |
| orders_count | number | The total number of orders that the customer has placed. |
| payment_methods | array of customer_payment_method | The customer's saved payment methods. |
| phone | string | The phone number of the customer. Only populated if customer entered it during checkout, opted into SMS, or merchant entered it. |
| store_credit_account | store_credit_account | The store credit account associated with the customer in their current currency context. |
| tags | array of string | The tags associated with the customer. |
| tax_exempt | boolean | Returns `true` if the customer is exempt from taxes. Returns `false` if not. |
| total_spent | number | The total amount the customer spent on all orders in the currency's subunit. |

#### Example

```json
{
  "accepts_marketing": true,
  "addresses": [],
  "addresses_count": 5,
  "b2b?": false,
  "company_available_locations": [],
  "company_available_locations_count": 1,
  "current_company": {},
  "current_location": null,
  "default_address": {},
  "email": "cornelius.potionmaker@gmail.com",
  "first_name": "Cornelius",
  "has_account": true,
  "has_avatar?": false,
  "id": 5625411010625,
  "last_name": "Potionmaker",
  "last_order": {},
  "name": "Cornelius Potionmaker",
  "orders": [],
  "orders_count": 1,
  "payment_methods": [],
  "phone": "+441314960905",
  "store_credit_account": {},
  "tags": [
    "newsletter"
  ],
  "tax_exempt": false,
  "total_spent": "56.00"
}
```

#### Check whether the `customer` object is defined

When using the `customer` object outside of customer-specific templates or objects that specifically return a customer, you should check whether the `customer` object is defined.

**Code:**
```liquid
{% if customer %}
  Hello, {{ customer.first_name }}!
{% endif %}
```

**Data:**
```json
{
  "customer": {
    "first_name": "Cornelius"
  }
}
```

**Output:**
```html
Hello, Cornelius!
```

#### Templates using customer

* [customers/account template](https://shopify.dev/themes/architecture/templates/customers-account)
* [customers/addresses template](https://shopify.dev/themes/architecture/templates/customers-addresses)
* [customers/order template](https://shopify.dev/themes/architecture/templates/customers-order)

---

### customer_payment_method

> Fonte: https://shopify.dev/docs/api/liquid/objects/customer_payment_method

A customer's saved payment method.

A payment method that a customer has saved to their account for reuse (e.g. a credit card).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| payment_instrument_type | string | The instrument type of the payment method (e.g credit_card). |
| token | string | The identifier for the payment method. |

#### Returned by

* [`customer.payment_methods`](https://shopify.dev/docs/api/liquid/objects/customer#customer-payment_methods)

---

### discount

> Fonte: https://shopify.dev/docs/api/liquid/objects/discount

A discount applied to a cart, line item, or order.

> **Deprecated:** Deprecated because not all discount types and details are captured. The `discount` object has been replaced by the [`discount_allocation`](https://shopify.dev/docs/api/liquid/objects/discount_allocation) and [`discount_application`](https://shopify.dev/docs/api/liquid/objects/discount_application) objects.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| amount | number | The amount of the discount in the currency's subunit. Same as `total_amount`. Presented in customer's local currency. For currencies without subunits (JPY, KRW), tenths and hundredths are appended. Use money filters for formatting. |
| code | string | The customer-facing name of the discount. Same as `title`. |
| savings | number | The amount of the discount as a negative value, in the currency's subunit. Same as `total_savings`. Presented in customer's local currency. Use money filters for formatting. |
| title | string | The customer-facing name of the discount. Same as `code`. |
| total_amount | number | The amount of the discount in the currency's subunit. Same as `amount`. Presented in customer's local currency. Use money filters for formatting. |
| total_savings | number | The amount of the discount as a negative value, in the currency's subunit. Same as `savings`. Presented in customer's local currency. Use money filters for formatting. |
| type | string | The type of the discount. Possible values: `FixedAmountDiscount`, `PercentageDiscount`, `ShippingDiscount` |

#### Example

```json
{
  "amount": "40.00",
  "code": "DIY",
  "savings": "-40.00",
  "title": "DIY",
  "total_amount": "40.00",
  "total_savings": "-40.00",
  "type": "PercentageDiscount"
}
```

---

### discount_allocation

> Fonte: https://shopify.dev/docs/api/liquid/objects/discount_allocation

Information about how a discount affects an item.

To learn about displaying discounts in your theme, refer to [Discounts](https://shopify.dev/themes/pricing-payments/discounts).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| amount | [number](https://shopify.dev/docs/api/liquid/basics#number) | The amount that the item is discounted by in the currency's subunit. The value displays in the customer's local (presentment) currency. For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen outputs as 100000. **Tip:** Use [money filters](https://shopify.dev/docs/api/liquid/filters/money-filters) to output a formatted amount. |
| discount_application | [discount_application](https://shopify.dev/docs/api/liquid/objects/discount_application) | The discount application that applies the discount to the item. |

#### Example

```json
{
  "amount": "40.00",
  "discount_application": "DiscountApplicationDrop"
}
```

---

### discount_application

> Fonte: https://shopify.dev/docs/api/liquid/objects/discount_application

Information about the intent of a discount.

To learn about how to display discounts in your theme, refer to [Discounts](https://shopify.dev/themes/pricing-payments/discounts).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| target_selection | string | The selection method for line items or shipping lines to be discounted. Note: Whether the selection method applies to line items or shipping lines depends on the discount's target type. Possible values: `all` (applies to all line items or shipping lines), `entitled` (applies to a specific set based on criteria), `explicit` (applies to a specific line item or shipping line) |
| target_type | string | The type of item that the discount applies to. Possible values: `line_item`, `shipping_line` |
| title | string | The customer-facing name of the discount. |
| total_allocated_amount | number | The total amount of the discount in the currency's subunit. The value is output in the customer's local (presentment) currency. For currencies without subunits (JPY, KRW), tenths and hundredths are appended. Use money filters to format the amount. |
| type | string | The type of the discount. Possible values: `automatic`, `discount_code`, `manual`, `script` |
| value | number | The value of the discount. Interpretation depends on the value type: for `fixed_amount`, the discount amount in currency's subunit; for `percentage`, the percent amount. |
| value_type | string | The value type of the discount. Possible values: `fixed_amount`, `percentage` |

#### Example

```json
{
  "target_selection": "explicit",
  "target_type": "line_item",
  "title": "Bloodroot discount!",
  "total_allocated_amount": "2.50",
  "type": "script",
  "value": "2.5",
  "value_type": "fixed_amount"
}
```

---

### external_video

> Fonte: https://shopify.dev/docs/api/liquid/objects/external_video

Information about an external video from YouTube or Vimeo.

> **Tip:** Use the `external_video_tag` filter to output the video in an HTML `<iframe>` tag. Use the `external_video_url` filter to specify parameters for the external video player.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| alt | string | The alt text of the external video. |
| aspect_ratio | number | The aspect ratio of the video as a decimal. |
| external_id | string | The ID of the video from its external source. |
| host | string | The service that hosts the video. Possible values: `youtube`, `vimeo` |
| id | number | The ID of the external video. |
| media_type | string | The media type of the external video. Always returns `external_video`. |
| position | number | The position of the external video in the `product.media` array. |
| preview_image | image | A preview image of the media. Preview images don't have an ID attribute. |

#### Example

**Code:**
```liquid
{% assign external_videos = product.media | where: 'media_type', 'external_video' %}

{% for external_video in external_videos %}
  {{- external_video | external_video_tag }}
{% endfor %}
```

**Data:**
```json
{
  "product": {
    "media": [
      {
        "media_type": "external_video"
      },
      {
        "media_type": "video"
      }
    ]
  }
}
```

**Output:**
```html
<iframe frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen" src="https://www.youtube.com/embed/vj01PAffOac?controls=1&amp;enablejsapi=1&amp;modestbranding=1&amp;origin=https%3A%2F%2Fpolinas-potent-potions.myshopify.com&amp;playsinline=1&amp;rel=0" title="Potion beats"></iframe>
```

**Example JSON:**
```json
{
  "alt": "Potion beats",
  "aspect_ratio": "1.77",
  "external_id": "vj01PAffOac",
  "host": "youtube",
  "id": 22015756402753,
  "media_type": "external_video",
  "position": 1,
  "preview_image": {}
}
```

---

### filter

> Fonte: https://shopify.dev/docs/api/liquid/objects/filter

A [storefront filter](https://help.shopify.com/manual/online-store/themes/customizing-themes/storefront-filters).

To learn about supporting filters in your theme, refer to [Support storefront filtering](https://shopify.dev/themes/navigation-search/filtering/storefront-filtering/support-storefront-filtering).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| active_values | array of [filter_value](https://shopify.dev/docs/api/liquid/objects/filter_value) | The values of the filter that are currently active. The array can have values only for `boolean` and `list` type filters. |
| false_value | [filter_value](https://shopify.dev/docs/api/liquid/objects/filter_value) | The `false` filter value. Returns a value for `boolean` type filters if the unfiltered view has at least one result with the `false` filter value. Otherwise, it returns `nil`. |
| inactive_values | array of [filter_value](https://shopify.dev/docs/api/liquid/objects/filter_value) | The values of the filter that are currently inactive. The array can have values only for `boolean` and `list` type filters. |
| label | [string](https://shopify.dev/docs/api/liquid/basics#string) | The customer-facing label for the filter. |
| max_value | [filter_value](https://shopify.dev/docs/api/liquid/objects/filter_value) | The highest filter value. Returns a value only for `price_range` type filters. Returns `nil` for other types. |
| min_value | [filter_value](https://shopify.dev/docs/api/liquid/objects/filter_value) | The lowest filter value. Returns a value only for `price_range` type filters. Returns `nil` for other types. |
| operator | [string](https://shopify.dev/docs/api/liquid/basics#string) from a set of values | The logical operator used by the filter. Returns a value only for `boolean` and `list` type filters. Returns `nil` for other types. For a filter named `color` with values `red` and `blue`: if the operator is `AND`, it filters items that are both red and blue; if `OR`, it filters items that are either red or blue or both. Filters supporting `AND`: Product tags, Metafields of type `list.single_line_text_field` and `list.metaobject_reference`. Possible values: `AND` (includes products matching all selections), `OR` (includes products matching at least one selection). |
| param_name | [string](https://shopify.dev/docs/api/liquid/basics#string) | The URL parameter for the filter. For example, `filter.v.option.color`. |
| presentation | [string](https://shopify.dev/docs/api/liquid/basics#string) from a set of values | Describes how to present the filter values. Returns a value only for `list` type filters. Returns `nil` for other types. Possible values: `image`, `swatch`, `text`. |
| range_max | [number](https://shopify.dev/docs/api/liquid/basics#number) | The highest product price within the collection or search results. Returns a value only for `price_range` type filters. Returns `nil` for other types. |
| true_value | [filter_value](https://shopify.dev/docs/api/liquid/objects/filter_value) | The `true` filter value. Returns a value for `boolean` type filters if the unfiltered view has at least one result with the `true` filter value. Otherwise, it returns `nil`. |
| type | [string](https://shopify.dev/docs/api/liquid/basics#string) from a set of values | The type of the filter. Possible values: `boolean`, `list`, `price_range`. |
| url_to_remove | [string](https://shopify.dev/docs/api/liquid/basics#string) | The current page URL with the URL parameter related to the filter removed. |
| values | array of [filter_value](https://shopify.dev/docs/api/liquid/objects/filter_value) | The values of the filter. The array can have values only for `boolean` and `list` type filters. |

#### Returned by

* [collection.filters](https://shopify.dev/docs/api/liquid/objects/collection#collection-filters)
* [search.filters](https://shopify.dev/docs/api/liquid/objects/search#search-filters)

---

### filter_value

> Fonte: https://shopify.dev/docs/api/liquid/objects/filter_value

A specific value of a filter.

To learn about supporting filters in your theme, refer to [Support storefront filtering](https://shopify.dev/themes/navigation-search/filtering/storefront-filtering/support-storefront-filtering).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| active | [boolean](https://shopify.dev/docs/api/liquid/basics#boolean) | Returns `true` if the value is currently active. Returns `false` if not. Can only return `true` for filters of type `boolean` or `list`. |
| count | [number](https://shopify.dev/docs/api/liquid/basics#number) | The number of results related to the filter value. Returns a value only for `boolean` and `list` type filters. Returns `nil` for `price_range` type filters. |
| image | [image](https://shopify.dev/docs/api/liquid/objects/image) | The visual representation of the filter value when an image is used. Returns an image drop for the filter value. Requires the filter presentation to be `image` and for an image to be available. Otherwise, returns `nil`. |
| label | [string](https://shopify.dev/docs/api/liquid/basics#string) | The customer-facing label for the filter value. For example, `Red` or `Rouge`. Returns a value only for `boolean` and `list` type filters. Returns `nil` for `price_range` type filters. |
| param_name | [string](https://shopify.dev/docs/api/liquid/basics#string) | The URL parameter for the parent filter of the filter value. For example, `filter.v.option.color`. Filters of type `price_range` include an extra component depending on whether the filter value is for the filter's `min_value` or `max_value`. |
| swatch | [swatch](https://shopify.dev/docs/api/liquid/objects/swatch) | The visual representation of the filter value when a swatch is used. Returns a swatch drop for the filter value. Requires the filter presentation to be `swatch` and saved color or image content. Otherwise, returns `nil`. |
| url_to_add | [string](https://shopify.dev/docs/api/liquid/basics#string) | The current page URL with the filter value parameter added. Note: Any pagination URL parameters are removed. |
| url_to_remove | [string](https://shopify.dev/docs/api/liquid/basics#string) | The current page URL with the filter value parameter removed. Note: Any pagination URL parameters are also removed. |
| value | [string](https://shopify.dev/docs/api/liquid/basics#string) | The value for the URL parameter. The `value` is paired with the `param_name` property. For example, `High` will be used in the URL as `filter.v.option.strength=High`. |

#### Deprecated Properties

| Property | Type | Status | Description |
|----------|------|--------|-------------|
| display | [filter_value_display](https://shopify.dev/docs/api/liquid/objects/filter_value_display) | Deprecated | The visual representation of the filter value. Returns a visual representation for the filter value. If no visual representation is available, then `nil` is returned. Deprecated in favor of the swatch attribute. |

#### Returned by

* [filter](https://shopify.dev/docs/api/liquid/objects/filter)
* [filter.false_value](https://shopify.dev/docs/api/liquid/objects/filter#filter-false_value)
* [filter.true_value](https://shopify.dev/docs/api/liquid/objects/filter#filter-true_value)
* [filter.max_value](https://shopify.dev/docs/api/liquid/objects/filter#filter-max_value)
* [filter.min_value](https://shopify.dev/docs/api/liquid/objects/filter#filter-min_value)

---

### filter_value_display

> Fonte: https://shopify.dev/docs/api/liquid/objects/filter_value_display

The visual representation of a filter value.

> **Deprecated:** This object is deprecated in favor of the [swatch](https://shopify.dev/docs/api/liquid/objects/swatch) drop.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| type | string | The type of visual representation. Possible values: `colors`, `image` |
| value | colors or image | The visual representation. Can be a list of color objects or an image object. Refer to the `type` property to determine which. |

#### Returned by

* [filter_value.display](https://shopify.dev/docs/api/liquid/objects/filter_value#filter_value-display)

---

### focal_point

> Fonte: https://shopify.dev/docs/api/liquid/objects/focal_point

The focal point for an image.

The focal point will remain visible when the image is cropped by the theme. [Learn more about supporting focal points in your theme](https://shopify.dev/themes/architecture/settings/input-settings#image-focal-points).

> **Tip:** Use the `image_tag` filter to automatically apply focal point settings to an image on the storefront. This applies the focal point using the `object-position` CSS property.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| x | number | The horizontal position of the focal point, as a percent of the image width. Returns `50` if no focal point is set. |
| y | number | The vertical position of the focal point, as a percent of the image height. Returns `50` if no focal point is set. |

#### Returned by

* [image_presentation.focal_point](https://shopify.dev/docs/api/liquid/objects/image_presentation#image_presentation-focal_point)

#### Referencing the `focal_point` object directly

When a `focal_point` object is referenced directly, the coordinates are returned as a string, in the format `X% Y%`.

**Code:**
```liquid
{{ images['potions-header.png'].presentation.focal_point }}
```

**Output:**
```html
1.9231% 9.7917%
```

---

### font

> Fonte: https://shopify.dev/docs/api/liquid/objects/font

A font from a [`font_picker` setting](https://shopify.dev/themes/architecture/settings/input-settings#font_picker).

You can use the `font` object in Liquid [assets](https://shopify.dev/themes/architecture#assets) or inside a [`style` tag](https://shopify.dev/docs/api/liquid/tags/style) to apply font setting values to theme CSS.

> **Tip:** Use [font filters](https://shopify.dev/docs/api/liquid/filters/font-filters) to modify properties of the `font` object, load the font, or obtain font variants.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| baseline_ratio | number | The baseline ratio of the font as a decimal. |
| fallback_families | string | The fallback families of the font. |
| family | string | The family name of the font. **Tip:** If the family name contains non-alphanumeric characters (A-Z, a-z, 0-9, or '-'), then it will be wrapped in double quotes. |
| style | string | The style of the font. |
| system? | boolean | Returns `true` if the font is a system font. Returns `false` if not. **Tip:** You can use this property to determine whether you need to include a corresponding [font-face](https://shopify.dev/docs/api/liquid/filters/font_face) declaration for the font. |
| variants | array of font | The variants in the family of the font. |
| weight | number | The weight of the font. |

#### Example

```json
{
  "baseline_ratio": 0.133,
  "fallback_families": "sans-serif",
  "family": "Assistant",
  "style": "normal",
  "system?": false,
  "variants": {},
  "weight": "400"
}
```

---

### forloop

> Fonte: https://shopify.dev/docs/api/liquid/objects/forloop

Information about a parent [`for` loop](https://shopify.dev/docs/api/liquid/tags/for).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| first | [boolean](https://shopify.dev/docs/api/liquid/basics#boolean) | Returns `true` if the current iteration is the first. Returns `false` if not. |
| index | [number](https://shopify.dev/docs/api/liquid/basics#number) | The 1-based index of the current iteration. |
| index0 | [number](https://shopify.dev/docs/api/liquid/basics#number) | The 0-based index of the current iteration. |
| last | [boolean](https://shopify.dev/docs/api/liquid/basics#boolean) | Returns `true` if the current iteration is the last. Returns `false` if not. |
| length | [number](https://shopify.dev/docs/api/liquid/basics#number) | The total number of iterations in the loop. |
| parentloop | [forloop](https://shopify.dev/docs/api/liquid/objects/forloop) | The parent `forloop` object. If the current `for` loop isn't nested inside another `for` loop, then `nil` is returned. |
| rindex | [number](https://shopify.dev/docs/api/liquid/basics#number) | The 1-based index of the current iteration, in reverse order. |
| rindex0 | [number](https://shopify.dev/docs/api/liquid/basics#number) | The 0-based index of the current iteration, in reverse order. |

#### Use the `parentloop` property

**Code:**
```liquid
{% for i in (1..3) -%}
  {% for j in (1..3) -%}
    {{ forloop.parentloop.index }} - {{ forloop.index }}
  {%- endfor %}
{%- endfor %}
```

**Output:**
```html
1 - 1
1 - 2
1 - 3

2 - 1
2 - 2
2 - 3

3 - 1
3 - 2
3 - 3
```

#### Example

```json
{
  "first": true,
  "index": 1,
  "index0": 0,
  "last": false,
  "length": 4,
  "rindex": 3
}
```

#### Use the `forloop` object

**Code:**
```liquid
{% for page in pages -%}
  {%- if forloop.length > 0 -%}
    {{ page.title }}{% unless forloop.last %}, {% endunless -%}
  {%- endif -%}
{% endfor %}
```

**Output:**
```html
About us, Contact, Potion dosages
```

---

### form

> Fonte: https://shopify.dev/docs/api/liquid/objects/form

Information about a form created by a [`form` tag](https://shopify.dev/docs/api/liquid/tags/form).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| address1 | [string](https://shopify.dev/docs/api/liquid/basics#string) | The first address line associated with the address. Exclusive to the [`customer_address` form](https://shopify.dev/docs/api/liquid/tags/form#form-customer_address). |
| address2 | [string](https://shopify.dev/docs/api/liquid/basics#string) | The second address line associated with the address. Exclusive to the [`customer_address` form](https://shopify.dev/docs/api/liquid/tags/form#form-customer_address). |
| author | [string](https://shopify.dev/docs/api/liquid/basics#string) | The name of the author of the article comment. Exclusive to the [`new_comment` form](https://shopify.dev/docs/api/liquid/tags/form#form-new_comment). |
| body | [string](https://shopify.dev/docs/api/liquid/basics#string) | The content of the contact submission or article comment. Exclusive to the [`contact`](https://shopify.dev/docs/api/liquid/tags/form#form-contact) and [`new_comment`](https://shopify.dev/docs/api/liquid/tags/form#form-new_comment) forms. |
| city | [string](https://shopify.dev/docs/api/liquid/basics#string) | The city associated with the address. Exclusive to the [`customer_address` form](https://shopify.dev/docs/api/liquid/tags/form#form-customer_address). |
| company | [string](https://shopify.dev/docs/api/liquid/basics#string) | The company associated with the address. Exclusive to the [`customer_address` form](https://shopify.dev/docs/api/liquid/tags/form#form-customer_address). |
| country | [string](https://shopify.dev/docs/api/liquid/basics#string) | The country associated with the address. Exclusive to the [`customer_address` form](https://shopify.dev/docs/api/liquid/tags/form#form-customer_address). |
| email | [string](https://shopify.dev/docs/api/liquid/basics#string) | The email associated with the form. Exclusive to: [`contact`](https://shopify.dev/docs/api/liquid/tags/form#form-contact), [`create_customer`](https://shopify.dev/docs/api/liquid/tags/form#form-create_customer), [`customer`](https://shopify.dev/docs/api/liquid/tags/form#form-customer), [`customer_login`](https://shopify.dev/docs/api/liquid/tags/form#form-customer_login), [`new_comment`](https://shopify.dev/docs/api/liquid/tags/form#form-new_comment), [`recover_customer_password`](https://shopify.dev/docs/api/liquid/tags/form#form-recover_customer_password), [`product`](https://shopify.dev/docs/api/liquid/tags/form#form-product). |
| errors | [form_errors](https://shopify.dev/docs/api/liquid/objects/form_errors) | Any errors from the form. Returns `nil` if no errors exist. Tip: Apply the `default_errors` filter to `form.errors` to output default error messages. |
| first_name | [string](https://shopify.dev/docs/api/liquid/basics#string) | The first name associated with the customer or address. Exclusive to the [`create_customer`](https://shopify.dev/docs/api/liquid/tags/form#form-create_customer) and [`customer_address`](https://shopify.dev/docs/api/liquid/tags/form#form-customer_address) forms. |
| id | [string](https://shopify.dev/docs/api/liquid/basics#string) | The ID of the form. |
| last_name | [string](https://shopify.dev/docs/api/liquid/basics#string) | The last name associated with the customer or address. Exclusive to the [`create_customer`](https://shopify.dev/docs/api/liquid/tags/form#form-create_customer) and [`customer_address`](https://shopify.dev/docs/api/liquid/tags/form#form-customer_address) forms. |
| message | [string](https://shopify.dev/docs/api/liquid/basics#string) | The personalized message intended for the recipient. Exclusive to the [`product` form](https://shopify.dev/docs/api/liquid/tags/form#form-product). |
| name | [string](https://shopify.dev/docs/api/liquid/basics#string) | The nickname of the gift card recipient. Exclusive to the [`product` form](https://shopify.dev/docs/api/liquid/tags/form#form-product). |
| password_needed | [boolean](https://shopify.dev/docs/api/liquid/basics#boolean) | Returns `true`. Exclusive to the [`customer_login` form](https://shopify.dev/docs/api/liquid/tags/form#form-customer_login). |
| phone | [string](https://shopify.dev/docs/api/liquid/basics#string) | The phone number associated with the address. Exclusive to the [`customer_address` form](https://shopify.dev/docs/api/liquid/tags/form#form-customer_address). |
| posted_successfully? | [boolean](https://shopify.dev/docs/api/liquid/basics#boolean) | Returns `true` if submitted successfully; `false` if errors occurred. Note: [`customer_address` form](https://shopify.dev/docs/api/liquid/tags/form#form-customer_address) always returns `true`. |
| province | [string](https://shopify.dev/docs/api/liquid/basics#string) | The province associated with the address. Exclusive to the [`customer_address` form](https://shopify.dev/docs/api/liquid/tags/form#form-customer_address). |
| set_as_default_checkbox | [string](https://shopify.dev/docs/api/liquid/basics#string) | Renders an HTML checkbox to submit the address as the customer's default address. Exclusive to the [`customer_address` form](https://shopify.dev/docs/api/liquid/tags/form#form-customer_address). |
| zip | [string](https://shopify.dev/docs/api/liquid/basics#string) | The zip or postal code associated with the address. Exclusive to the [`customer_address` form](https://shopify.dev/docs/api/liquid/tags/form#form-customer_address). |

#### Example

```json
{
  "address1": "12 Phoenix Feather Alley",
  "address2": "1",
  "author": null,
  "body": null,
  "city": "Calgary",
  "company": null,
  "country": "Canada",
  "email": null,
  "errors": null,
  "first_name": "Cornelius",
  "id": "new",
  "last_name": "Potionmaker",
  "password_needed?": false,
  "phone": "44 131 496 0905",
  "posted_successfully?": true,
  "province": "Alberta",
  "set_as_default_checkbox": "<input type='checkbox' id='address_default_address_new' name='address[default]' value='1'>",
  "zip": "T1X 0L4"
}
```

---

### form_errors

> Fonte: https://shopify.dev/docs/api/liquid/objects/form_errors

The error category strings for errors from a form created by a [`form` tag](/docs/api/liquid/tags/form).

The following table outlines the strings that can be returned and the reason that they would be:

| Form property name | Return reason |
| - | - |
| `author` | There were issues with required name fields. |
| `body` | There were issues with required text content fields. |
| `email` | There were issues with required email fields. |
| `form` | There were general issues with the form. |
| `password` | There were issues with required password fields. |

#### Properties

| Name | Type | Description |
| - | - | - |
| messages | array of string | The translated error messages for each value in the `form_errors` array. You can access a specific message by using a specific error from the `form_errors` array as a key. |
| translated_fields | array of string | The translated names for each value in the `form_errors` array. You can access a specific field by using a specific error from the `form_errors` array as a key. |

#### Example

```json
{
  "messages": {},
  "translated_fields": {}
}
```

#### Output form errors

You can output the name of the field related to the error, and the error message, by using the error as a key to access the `translated_fields` and `messages` properties.

```liquid
<ul>
  {% for error in form.errors %}
    <li>
      {% if error == 'form' %}
        {{ form.errors.messages[error] }}
      {% else %}
        {{ form.errors.translated_fields[error] }} - {{ form.errors.messages[error] }}
      {% endif %}
    </li>
  {% endfor %}
</ul>
```

---

### fulfillment

> Fonte: https://shopify.dev/docs/api/liquid/objects/fulfillment

An order fulfillment, which includes information like the line items being fulfilled and shipment tracking.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| created_at | string | A timestamp for when the fulfillment was created. **Tip:** Use the `date` filter to format the timestamp. |
| fulfillment_line_items | array of line_item | The line items in the fulfillment. |
| item_count | number | The number of items in the fulfillment. |
| tracking_company | string | The name of the fulfillment service. |
| tracking_number | string | The fulfillment's tracking number. If there's no tracking number, then `nil` is returned. |
| tracking_numbers | array of string | An array of the fulfillment's tracking numbers. |
| tracking_url | string | The URL for the fulfillment's tracking number. If there's no tracking number, then `nil` is returned. |

#### Example

```json
{
  "created_at": "2022-06-15 17:08:30 -0400",
  "fulfillment_line_items": [
    {
      "quantity": 2,
      "line_item": "LineItemDrop"
    },
    {
      "quantity": 1,
      "line_item": "LineItemDrop"
    }
  ],
  "item_count": 3,
  "tracking_company": "Canada Post",
  "tracking_number": "01189998819991197253",
  "tracking_numbers": [
    "01189998819991197253"
  ],
  "tracking_url": "https://www.canadapost-postescanada.ca/track-reperage/en#/search?searchFor=01189998819991197253"
}
```

---

### generic_file

> Fonte: https://shopify.dev/docs/api/liquid/objects/generic_file

A file from a `file_reference` type [metafield](https://shopify.dev/docs/api/liquid/objects/metafield) that is neither an image or video.

> **Tip:** To learn about metafield types, refer to [Metafield types](/apps/metafields/types).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| alt | [string](https://shopify.dev/docs/api/liquid/basics#string) | The alt text of the media. |
| id | [number](https://shopify.dev/docs/api/liquid/basics#number) | The ID of the file. |
| media_type | [string](https://shopify.dev/docs/api/liquid/basics#string) | The media type of the model. Always returns `generic_file`. |
| position | [number](https://shopify.dev/docs/api/liquid/basics#number) | The position of the media in the [`product.media` array](https://shopify.dev/docs/api/liquid/objects/product#product-media). If the source is a [`file_reference` metafield](https://shopify.dev/apps/metafields/types), then `nil` is returned. |
| preview_image | [image](https://shopify.dev/docs/api/liquid/objects/image) | A preview image for the file. |
| url | [string](https://shopify.dev/docs/api/liquid/basics#string) | The [CDN URL](https://shopify.dev/themes/best-practices/performance/platform#shopify-cdn) for the file. |

#### Example

```json
{
  "alt": null,
  "id": 21918386454593,
  "media_type": "generic_file",
  "position": null,
  "preview_image": {},
  "url": "//polinas-potent-potions.myshopify.com/cdn/shop/files/disclaimer.pdf?v=9043651738044769859"
}
```

---

### gift_card

> Fonte: https://shopify.dev/docs/api/liquid/objects/gift_card

A [gift card](https://help.shopify.com/manual/products/gift-card-products) that's been issued to a customer or a recipient.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| balance | number | The remaining balance of the gift card in the currency's subunit. Output in presentment currency. For currencies without subunits (JPY, KRW), tenths and hundredths are appended; 1000 yen outputs as 100000. Use money filters for formatted amounts. |
| code | string | The code used to redeem the gift card. |
| currency | string | The [ISO code](https://www.iso.org/iso-4217-currency-codes.html) of the currency that the gift card was issued in. |
| customer | customer | The customer associated with the gift card. |
| enabled | boolean | Returns `true` if the gift card is enabled; `false` otherwise. |
| expired | boolean | Returns `true` if the gift card is expired; `false` otherwise. |
| expires_on | string | A timestamp for when the gift card expires. Returns `nil` if it never expires. Use the date filter to format. |
| initial_value | number | The initial balance of the gift card in the currency's subunit. Output in presentment currency with same formatting rules as balance. Use money filters for formatted amounts. |
| last_four_characters | string | The last 4 characters of the gift card redemption code. |
| message | string | The personalized message intended for the recipient. Returns `nil` if no message exists. |
| pass_url | string | The URL to download the gift card as an Apple Wallet Pass. |
| product | product | The product associated with the gift card. |
| properties | — | The [line item properties](https://shopify.dev/docs/api/liquid/objects/line_item#line_item-properties) assigned to the gift card. Returns `EmptyDrop` if none exist. |
| qr_identifier | string | A string used to generate a QR code for the gift card. |
| recipient | recipient | The recipient associated with the gift card. Returns `nil` if no recipient exists. |
| send_on | string | The scheduled date on which the gift card will be sent to the recipient. Returns `nil` if no scheduled date. Use date filter to format. |
| template_suffix | string | The name of the [custom template](https://shopify.dev/themes/architecture/templates#alternate-templates) assigned to the gift card. Excludes `gift_card.` prefix and `.liquid` extension. Returns `nil` if unassigned. |
| url | string | The URL to view the gift card. This URL is on the `checkout.shopify.com` domain. Rendered via the gift_card.liquid theme template. |
| variant | variant | The variant associated with the gift card. Returns `nil` if no variant exists. |

#### Example

```json
{
  "balance": 5000,
  "code": "WCGX 7X97 K9HJ DFR8",
  "currency": "CAD",
  "customer": {},
  "enabled": true,
  "expired": false,
  "expires_on": null,
  "initial_value": 5000,
  "last_four_characters": "DFR8",
  "message": null,
  "send_on": null,
  "pass_url": "https://polinas-potent-potions.myshopify.com/v1/passes/pass.com.shopify.giftcardnext/94af7fbe55d010130df8d8bc4a338d36/",
  "product": {},
  "variant": {},
  "properties": {},
  "qr_identifier": "shopify-giftcard-v1-3TKWJKJBM3X7PBRK",
  "recipient": null,
  "template_suffix": null,
  "url": "https://checkout.shopify.com/gift_cards/56174706753/0011c591fc720d0a51b80cdb694f969e"
}
```

#### Templates using gift_card

- [gift_card.liquid template](https://shopify.dev/themes/architecture/templates/gift-card-liquid)

---

### group

> Fonte: https://shopify.dev/docs/api/liquid/objects/group

A group of rules for the `robots.txt` file.

> You can customize the `robots.txt` file with the `robots.txt.liquid` template.

#### Properties

| Name | Type | Description |
|------|------|---|
| rules | array of [rule](https://shopify.dev/docs/api/liquid/objects/rule) | The rules in the group. |
| sitemap | [sitemap](https://shopify.dev/docs/api/liquid/objects/sitemap) | The sitemap for the group. If the group doesn't require a sitemap, then `blank` is returned. The sitemap can be accessed at `/sitemap.xml`. |
| user_agent | [user_agent](https://shopify.dev/docs/api/liquid/objects/user_agent) | The user agent for the group. |

#### Example

```json
{
  "rules": [],
  "sitemap": {},
  "user_agent": {}
}
```

---

### handle

> Fonte: https://shopify.dev/docs/api/liquid/objects/handle

The [handle](https://shopify.dev/docs/api/liquid/basics#handles) of the resource associated with the current template.

The `handle` object will return a value only when the following templates are being viewed:

* [article](https://shopify.dev/themes/architecture/templates/article)
* [blog](https://shopify.dev/themes/architecture/templates/blog)
* [collection](https://shopify.dev/themes/architecture/templates/collection)
* [page](https://shopify.dev/themes/architecture/templates/page)
* [product](https://shopify.dev/themes/architecture/templates/product)

If none of the above templates are being viewed, then `nil` is returned.

#### Directly accessible in

* Global

---

### image

> Fonte: https://shopify.dev/docs/api/liquid/objects/image

An image, such as a product or collection image.

To learn about the image formats that Shopify supports, visit the [Shopify Help Center](https://help.shopify.com/manual/online-store/images/theme-images#image-formats).

> **Tip:** Use the `image_url` and `image_tag` filters to display images on the storefront.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| alt | string | The alt text of the image. |
| aspect_ratio | number | The aspect ratio of the image as a decimal. |
| attached_to_variant? | boolean | Returns `true` if the image is associated with a variant. Returns `false` if not. Only available for images accessed through `product.featured_image` or `product.images`. Returns `nil` if referenced on an image from another source. |
| height | number | The height of the image in pixels. |
| id | number | The ID of the image. Returns `nil` if referenced for preview images of `generic_file` or `media` objects. |
| media_type | string | The media type of the image. Always returns `image`. Only available for images accessed through `product.media` or `file_reference` type metafields. Returns `nil` if referenced from another source. |
| position | number | The position of the image in the `product.images` or `product.media` array. Only available for images associated with a product. Returns `nil` if referenced from another source. |
| presentation | image_presentation | The presentation settings for the image. |
| preview_image | image | A preview image for the image. Only available for images accessed through `product.featured_media`, `product.media`, or `file_reference` type metafields. Returns `nil` if referenced from another source. |
| product_id | number | The ID of the product that the image is associated with. Only available for images associated with a product. Returns `nil` if referenced from another source. |
| src | string | The relative URL of the image. |
| variants | array of variant | The product variants that the image is associated with. Only available for images accessed through `product.featured_image` or `product.images`. Returns `nil` if referenced from another source. |
| width | number | The width of the image in pixels. |

#### Example

```json
{
  "alt": "Charcoal",
  "aspect_ratio": 1.5001681802892701,
  "attached_to_variant?": false,
  "height": 2973,
  "id": 29355706875969,
  "position": 1,
  "product_id": 6790277595201,
  "src": {},
  "variants": [],
  "width": 4460
}
```

#### Referencing the `image` object directly

When an `image` object is referenced directly, the image's relative URL path is returned.

**Code:**
```liquid
{{ product.featured_image }}
```

**Data:**
```json
{
  "product": {
    "featured_image": "products/mushrooms-on-a-table.jpg"
  }
}
```

**Output:**
```html
products/mushrooms-on-a-table.jpg
```

#### Filter for media of a specific type

You can use the `media_type` property with the `where` filter to filter the `product.media` array for all media of a desired type.

**Code:**
```liquid
{% assign images = product.media | where: 'media_type', 'image' %}

{% for image in images %}
  {{- image | image_url: width: 300 | image_tag }}
{% endfor %}
```

**Data:**
```json
{
  "product": {
    "media": [
      "products/oil-dripping-into-jar.jpg"
    ]
  }
}
```

**Output:**
```html
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/products/oil-dripping-into-jar.jpg?v=1650399519&amp;width=300" alt="Viper venom" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/products/oil-dripping-into-jar.jpg?v=1650399519&amp;width=300 300w" width="300" height="200">
```

---

### image_presentation

> Fonte: https://shopify.dev/docs/api/liquid/objects/image_presentation

The presentation settings for an image.

#### Properties

| Name | Type | Description |
|------|------|-------------|
| focal_point | [focal_point](https://shopify.dev/docs/api/liquid/objects/focal_point) | The focal point for the image. |

#### Returned by

* [image.presentation](https://shopify.dev/docs/api/liquid/objects/image#image-presentation)

---

### images

> Fonte: https://shopify.dev/docs/api/liquid/objects/images

All of the [images](https://shopify.dev/docs/api/liquid/objects/image) that have been [uploaded](https://help.shopify.com/manual/online-store/images/theme-images#upload-images) to a store.

#### Directly accessible in

* Global

You can access images from the `images` array by their filename.

#### Example

**Input:**
```liquid
{{ images['potions-header.png'] | image_url: width: 300 | image_tag }}
```

**Output:**
```html
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/potions-header.png?v=1650325393&amp;width=300" alt="" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/files/potions-header.png?v=1650325393&amp;width=300 300w" width="300" height="173" style="object-position:1.9231% 9.7917%;">
```

---

### instructions

> Fonte: https://shopify.dev/docs/api/liquid/objects/instructions

The instructions for a nested cart line item.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| can_remove | boolean | Whether the nested cart line item can be removed. |
| can_update_quantity | boolean | Whether the nested cart line item quantity can be updated. |

#### Returned by

* [line_item.instructions](https://shopify.dev/docs/api/liquid/objects/line_item#line_item-instructions)

---

### line_item

> Fonte: https://shopify.dev/docs/api/liquid/objects/line_item

A line in a cart, checkout, or order. Each line item represents a product variant.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| discount_allocations | array of [discount_allocation](https://shopify.dev/docs/api/liquid/objects/discount_allocation) | The discount allocations that apply to the line item. **Caution:** Not applicable for item component as discounts are applied to the parent line item. |
| error_message | [string](https://shopify.dev/docs/api/liquid/basics#string) | An informational error message about the status of the line item in the buyer's chosen language. **Note:** This field is applicable for cart line item only and currently available for shops using Checkout Extensibility. |
| final_line_price | [number](https://shopify.dev/docs/api/liquid/basics#number) | The combined price, in the currency's subunit, of all of the items in the line item. This includes any line-level discounts. The value is equal to `line_item.final_price` multiplied by `line_item.quantity`. It's output in the customer's local (presentment) currency. For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000. **Tip:** Use money filters to output a formatted price. |
| final_price | [number](https://shopify.dev/docs/api/liquid/basics#number) | The price of the line item in the currency's subunit. This includes any line-level discounts. The value is output in the customer's local (presentment) currency. For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000. **Tip:** Use money filters to output a formatted price. |
| fulfillment | [fulfillment](https://shopify.dev/docs/api/liquid/objects/fulfillment) | The fulfillment of the line item. |
| fulfillment_service | [string](https://shopify.dev/docs/api/liquid/basics#string) | The [fulfillment service](https://help.shopify.com/manual/shipping/understanding-shipping/dropshipping-and-fulfillment-services) for the variant associated with the line item. If there's no fulfillment service, then `manual` is returned. |
| gift_card | [boolean](https://shopify.dev/docs/api/liquid/basics#boolean) | Returns `true` if the product associated with the line item is a gift card. Returns `false` if not. |
| grams | [number](https://shopify.dev/docs/api/liquid/basics#number) | The weight of the line item in the store's [default weight unit](https://help.shopify.com/manual/intro-to-shopify/initial-setup/setup-business-settings#set-or-change-your-stores-default-weight-unit). **Tip:** Use this property with the `weight_with_unit` filter to format the weight. |
| id | [number](https://shopify.dev/docs/api/liquid/basics#number) | The ID of the line item. The ID differs depending on the context (see context table below). |
| image | [image](https://shopify.dev/docs/api/liquid/objects/image) | The image of the line item. The image can come from the variant associated with the line item or the featured image of the product associated with the line item, if there's no variant image. |
| instructions | [instructions](https://shopify.dev/docs/api/liquid/objects/instructions) | Instructions define behaviours and operations that can be performed on the nested cart line. **Note:** This field is applicable for cart line item only. |
| item_components | array of [line_item](https://shopify.dev/docs/api/liquid/objects/line_item) | The components of a line item. **Note:** This field is applicable for cart line item only. |
| key | [string](https://shopify.dev/docs/api/liquid/basics#string) | The key of the line item. Line item keys are unique identifiers consisting of the variant ID and a hash of unique characteristics, separated by a colon. Note: Line item keys are not stable identifiers and will change as characteristics change. |
| line_level_discount_allocations | array of [discount_allocation](https://shopify.dev/docs/api/liquid/objects/discount_allocation) | The discount allocations that apply directly to the line item. **Caution:** Not applicable for item component as discounts are applied to the parent line item. |
| line_level_total_discount | [number](https://shopify.dev/docs/api/liquid/basics#number) | The total amount of any discounts applied to the line item in the currency's subunit. The value is output in the customer's local (presentment) currency. For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000. **Tip:** Use money filters to output a formatted amount. |
| message | [string](https://shopify.dev/docs/api/liquid/basics#string) | Information about the discounts that have affected the line item. Returns `nil` if no discounts apply, the discount title if one discount applies, or a generated string noting the number of discounts if more than one applies. |
| options_with_values | array | The name and value pairs for each option of the variant associated with the line item. **Note:** The array is never empty because variants with no options still have a default option. Use `line_item.product.has_only_default_variant` to check whether there's any information to output. |
| original_line_price | [number](https://shopify.dev/docs/api/liquid/basics#number) | The combined price of all of the items in a line item in the currency's subunit, before any discounts have been applied. The value is equal to `line_item.original_price` multiplied by `line_item.quantity`. It's output in the customer's local (presentment) currency. For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000. **Tip:** Use money filters to output a formatted price. |
| original_price | [number](https://shopify.dev/docs/api/liquid/basics#number) | The price of the line item in the currency's subunit, before discounts have been applied. The value is output in the customer's local (presentment) currency. For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000. **Tip:** Use money filters to output a formatted price. |
| parent_relationship | [parent_relationship](https://shopify.dev/docs/api/liquid/objects/parent_relationship) | The parent relationship for a nested line item. **Note:** This field is applicable for cart line item only. |
| product | [product](https://shopify.dev/docs/api/liquid/objects/product) | The product associated with the line item. May be a regular product or a remote product. |
| product_id | [number](https://shopify.dev/docs/api/liquid/basics#number) | The [ID](https://shopify.dev/docs/api/liquid/objects/product#product-id) of the line item's product. |
| properties | object | The properties of the line item. Line item properties consist of name and value pairs and can be captured with a custom input inside a product form or the AJAX Cart API. You can add an underscore to the beginning of a property name to hide it from customers at checkout. |
| quantity | [number](https://shopify.dev/docs/api/liquid/basics#number) | The quantity of the line item. |
| requires_shipping | [boolean](https://shopify.dev/docs/api/liquid/basics#boolean) | Returns `true` if the variant associated with the line item requires shipping. Returns `false` if not. |
| selling_plan_allocation | [selling_plan_allocation](https://shopify.dev/docs/api/liquid/objects/selling_plan_allocation) | The selling plan allocation of the line item. If the line item doesn't have a selling plan allocation, then `nil` is returned. |
| sku | [string](https://shopify.dev/docs/api/liquid/basics#string) | The [sku](https://shopify.dev/docs/api/liquid/objects/variant#variant-sku) of the variant associated with the line item. |
| successfully_fulfilled_quantity | [number](https://shopify.dev/docs/api/liquid/basics#number) | The number of items from the line item that have been successfully fulfilled. |
| tax_lines | array of [tax_line](https://shopify.dev/docs/api/liquid/objects/tax_line) | The tax lines for the line item. |
| taxable | [boolean](https://shopify.dev/docs/api/liquid/basics#boolean) | Returns `true` if taxes should be charged on the line item. Returns `false` if not. |
| title | [string](https://shopify.dev/docs/api/liquid/basics#string) | The title of the line item. The title is a combination of `line_item.product.title` and `line_item.variant.title`, separated by a hyphen. In most contexts, the line item title appears in the customer's preferred language. However, in the context of an [order](https://shopify.dev/docs/api/liquid/objects/order), the line item title appears in the language that the customer checked out in. The title can receive an override value from the Cart Transform API. Overrides take precedence over translations. |
| unit_price | [number](https://shopify.dev/docs/api/liquid/basics#number) | The [unit price](https://help.shopify.com/manual/products/details/product-pricing/unit-pricing#add-unit-prices-to-your-product) of the line item in the currency's subunit. The price reflects any discounts that are applied to the line item. The value is output in the customer's local (presentment) currency. For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000. **Tip:** Use the `unit_price_with_measurement` filter with this property and the `line_item.unit_price_measurement` property to output a formatted unit price with measurement. |
| unit_price_measurement | [unit_price_measurement](https://shopify.dev/docs/api/liquid/objects/unit_price_measurement) | The unit price measurement of the line item. **Tip:** Use the `unit_price_with_measurement` filter with the `line_item.unit_price` property and this property to output a formatted unit price with measurement. |
| url | [string](https://shopify.dev/docs/api/liquid/basics#string) | The relative URL of the variant associated with the line item. |
| url_to_remove | [string](https://shopify.dev/docs/api/liquid/basics#string) | A URL to remove the line item from the cart. **Tip:** To learn more about how to use this property in your theme, refer to Remove line items from the cart. |
| variant | [variant](https://shopify.dev/docs/api/liquid/objects/variant) | The variant associated with the line item. |
| variant_id | [number](https://shopify.dev/docs/api/liquid/basics#number) | The [ID](https://shopify.dev/docs/api/liquid/objects/variant#variant-id) of the line item's variant. |
| vendor | [string](https://shopify.dev/docs/api/liquid/basics#string) | The vendor of the variant associated with the line item. |

##### ID Context Table

| Context | Value |
|---------|-------|
| [`cart.items`](https://shopify.dev/docs/api/liquid/objects/cart#cart-items) | The ID of the line item's variant. This ID isn't unique, and can be shared by multiple items with the same variant. |
| [`checkout.line_items`](https://shopify.dev/docs/api/liquid/objects/checkout#checkout-line_items) | A temporary unique hash generated for the checkout. |
| [`order.line_items`](https://shopify.dev/docs/api/liquid/objects/order#order-line_items) | A unique integer ID. |

#### Deprecated Properties

| Property | Type | Deprecation Reason |
|----------|------|-------------------|
| discounts | array of [discount](https://shopify.dev/docs/api/liquid/objects/discount) | Deprecated because not all discount types and details are available. The `line_item.discounts` property has been replaced by [`line_item.discount_allocations`](https://shopify.dev/docs/api/liquid/objects/line_item#line_item-discount_allocations). |
| line_price | [number](https://shopify.dev/docs/api/liquid/basics#number) | Deprecated because discounts from automatic discounts and discount codes aren't included. Replaced by [`line_item.final_line_price`](https://shopify.dev/docs/api/liquid/objects/line_item#line_item-final_line_price). |
| price | [number](https://shopify.dev/docs/api/liquid/basics#number) | Deprecated because discounts from automatic discounts and discount codes aren't included. Replaced by [`line_item.final_price`](https://shopify.dev/docs/api/liquid/objects/line_item#line_item-final_price). |
| total_discount | [number](https://shopify.dev/docs/api/liquid/basics#number) | Deprecated because discounts from automatic discounts and discount codes aren't included. Replaced by [`line_item.line_level_total_discount`](https://shopify.dev/docs/api/liquid/objects/line_item#line_item-line_level_total_discount). |

#### Example: Output the option values

**Code:**
```liquid
{% for item in cart.items %}
<div class="cart__item">
  <p class="cart__item-title">
    {{ item.title }}
  </p>

  {%- unless item.product.has_only_default_variant %}
  <ul>
    {% for option in item.options_with_values -%}
    <li>{{ option.name }}: {{ option.value }}</li>
    {%- endfor %}
  </ul>
  {% endunless %}
</div>
{% endfor %}
```

**Data:**
```json
{
  "cart": {
    "items": [
      {
        "product": {
          "has_only_default_variant": true
        },
        "title": "Whole bloodroot"
      },
      {
        "product": {
          "has_only_default_variant": true
        },
        "title": "Viper venom"
      }
    ]
  }
}
```

**Output:**
```html
<div class="cart__item">
  <p class="cart__item-title">
    Whole bloodroot
  </p>
</div>

<div class="cart__item">
  <p class="cart__item-title">
    Viper venom
  </p>
</div>
```

#### Example: Capture line item properties in the product form

To capture line item properties inside the [product form](https://shopify.dev/docs/api/liquid/tags/form#form-product), you need to include an input for each property. Each input needs a unique `name` attribute. Use the following format:

```
name="properties[property-name]"
```

The value of the input is captured as the value of the property.

For example, you can use the following code to capture custom engraving text for a product:

```liquid
{% form 'product', product %}
  ...
  <label for="engravingText">Engraving<label>
  <input type="text" id="engravingText" name="properties[Engraving]">
  ...
{% endform %}
```

You can add an underscore to the beginning of a property name to hide it from customers at checkout. For example, `properties[_hiddenPropertyName]`.

#### Example JSON

```json
{
  "discount_allocations": [],
  "discounts": [],
  "error_message": "",
  "final_line_price": "74.97",
  "final_price": "24.99",
  "fulfillment": {},
  "fulfillment_service": "manual",
  "gift_card": false,
  "grams": 0,
  "id": 10974183882817,
  "image": {},
  "instructions": null,
  "item_components": null,
  "key": 10974183882817,
  "line_level_discount_allocations": [],
  "line_level_total_discount": "0.00",
  "line_price": "74.97",
  "message": "",
  "options_with_values": [
    {
      "name": "Title",
      "value": "Default Title"
    }
  ],
  "original_line_price": "74.97",
  "original_price": "24.99",
  "parent_relationship": null,
  "price": "24.99",
  "product": {},
  "product_id": 6792596455489,
  "properties": {},
  "quantity": 3,
  "requires_shipping": true,
  "selling_plan_allocation": null,
  "sku": "",
  "successfully_fulfilled_quantity": 2,
  "tax_lines": [],
  "taxable": true,
  "title": "Bloodroot (whole)",
  "total_discount": "0.00",
  "unit_price": "49.98",
  "unit_price_measurement": {
    "measured_type": "weight",
    "quantity_value": "500.0",
    "quantity_unit": "g",
    "reference_value": 1,
    "reference_unit": "kg"
  },
  "url": {},
  "url_to_remove": null,
  "variant": {},
  "variant_id": 39888235757633,
  "vendor": "Clover's Apothecary"
}
```

---

### link

> Fonte: https://shopify.dev/docs/api/liquid/objects/link

A link in a [menu](https://help.shopify.com/manual/online-store/menus-and-links/drop-down-menus).

To learn about implementing navigation in a theme, refer to [Add navigation to your theme](https://shopify.dev/themes/navigation-search/navigation).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| active | boolean | Returns `true` if the link is active. Returns `false` if not. A link is considered active if the current URL path matches or contains the link's URL. |
| child_active | boolean | Returns `true` if a link's child link is active. Returns `false` if not. A child link is active if the current URL path matches or contains its URL. |
| child_current | boolean | Returns `true` if current URL path matches a link's child link URL. Returns `false` if not. URL parameters are ignored when determining a match. |
| current | boolean | Returns `true` if the current URL path matches the URL of the link. Returns `false` if not. URL parameters are ignored; product URLs within collection context equal standard product URLs. |
| handle | string | The handle of the link. |
| levels | number | The number of nested levels under the link. |
| links | array of link | The child links of the link. |
| object | object | The object associated with the link (article, blog, collection, metaobject, page, policy, or product). |
| title | string | The title of the link. |
| type | string | The type of the link. Possible values: article_link, blog_link, catalog_link, collection_link, collections_link, customer_account_page_link, frontpage_link, http_link, metaobject_link, page_link, policy_link, product_link, search_link. |
| url | string | The URL of the link. |

#### Example

**Code:**
```liquid
{% for link in linklists.main-menu.links -%}
  {% if link.links.size > 0 -%}
    - {{ link.title }} ({{ link.links.size }} children)<br>
  {%- else -%}
    - {{ link.title }}<br>
  {%- endif %}
{%- endfor %}
```

**Output:**
```html
- Home<br>
- Catalog (2 children)<br>
- Contact<br>
```

**Example JSON:**
```json
{
  "active": false,
  "child_active": false,
  "child_current": false,
  "current": false,
  "handle": {},
  "levels": 0,
  "links": [],
  "object": {},
  "title": {},
  "type": "page_link",
  "url": "/pages/contact"
}
```

---

### linklist

> Fonte: https://shopify.dev/docs/api/liquid/objects/linklist

A [menu](https://help.shopify.com/manual/online-store/menus-and-links/drop-down-menus) in a store.

To learn about implementing navigation in a theme, refer to [Add navigation to your theme](https://shopify.dev/themes/navigation-search/navigation).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| handle | [string](https://shopify.dev/docs/api/liquid/basics#string) | The [handle](https://shopify.dev/docs/api/liquid/basics#handles) of the menu. |
| levels | [number](https://shopify.dev/docs/api/liquid/basics#number) | The number of nested levels in the menu. **Note:** Maximum of 3 levels. |
| links | array of [link](https://shopify.dev/docs/api/liquid/objects/link) | The links in the menu. |
| title | [string](https://shopify.dev/docs/api/liquid/basics#string) | The title of the menu. |

#### Example

```json
{
  "handle": "main-menu",
  "levels": 2,
  "links": [],
  "title": "Main menu"
}
```

---

### linklists

> Fonte: https://shopify.dev/docs/api/liquid/objects/linklists

All of the menus in a store.

#### Directly accessible in

* Global

Access a specific menu through the `linklists` object using the menu's handle.

#### Example

```liquid
<!-- Main menu -->
{% for link in linklists.main-menu.links -%}
  {{ link.title | link_to: link.url }}
{%- endfor %}

<!-- Footer menu -->
{% for link in linklists['footer'].links -%}
  {{ link.title | link_to: link.url }}
{%- endfor %}
```

**Data structure:**
```json
{
  "linklists": {
    "footer": {
      "links": [
        "LinkDrop"
      ]
    },
    "main-menu": {
      "links": [
        "LinkDrop",
        "LinkDrop",
        "LinkDrop"
      ]
    }
  }
}
```

**Output:**
```html
<!-- Main menu -->
<a href="/" title="">Home</a>
<a href="/collections/all" title="">Catalog</a>
<a href="/pages/contact" title="">Contact</a>


<!-- Footer menu -->
<a href="/search" title="">Search</a>
```

---

### localization

> Fonte: https://shopify.dev/docs/api/liquid/objects/localization

Information pertaining to the countries and languages accessible on a store.

The `localization` object integrates with a [localization form](https://shopify.dev/docs/api/liquid/tags/form#form-localization).

For guidance on implementing localization options in your theme, see [Support multiple currencies and languages](https://shopify.dev/themes/internationalization/multiple-currencies-languages).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| available_countries | array of [country](https://shopify.dev/docs/api/liquid/objects/country) | The countries that are available on the store. |
| available_languages | array of [shop_locale](https://shopify.dev/docs/api/liquid/objects/shop_locale) | The languages that are available on the store. |
| country | [country](https://shopify.dev/docs/api/liquid/objects/country) | The currently selected country on the storefront. |
| language | [shop_locale](https://shopify.dev/docs/api/liquid/objects/shop_locale) | The currently selected language on the storefront. |
| market | [market](https://shopify.dev/docs/api/liquid/objects/market) | The currently selected market on the storefront. |

#### Example

```json
{
  "available_countries": [],
  "available_languages": [],
  "country": {},
  "language": {},
  "market": {}
}
```

---

### location

> Fonte: https://shopify.dev/docs/api/liquid/objects/location

A store [location](https://help.shopify.com/manual/locations).

> The `location` object is defined only if one or more locations has local pickup enabled.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| address | [address](https://shopify.dev/docs/api/liquid/objects/address) | The location's address. |
| id | [number](https://shopify.dev/docs/api/liquid/basics#number) | The location's ID. |
| latitude | [number](https://shopify.dev/docs/api/liquid/basics#number) | The latitude of the location's address. If the location's address isn't verified, then `nil` is returned. |
| longitude | [number](https://shopify.dev/docs/api/liquid/basics#number) | The longitude of the location's address. If the location's address isn't verified, then `nil` is returned. |
| metafields | [metafields](https://shopify.dev/docs/api/liquid/objects/metafield) | The metafields applied to the location. |
| name | [string](https://shopify.dev/docs/api/liquid/basics#string) | The location's name. |

#### Example

```json
{
  "address": {},
  "id": 62002462785,
  "latitude": 43.6556377,
  "longitude": -79.38681079999999,
  "metafields": {},
  "name": "123 Edward Street"
}
```

---

### market

> Fonte: https://shopify.dev/docs/api/liquid/objects/market

A group of one or more regions of the world that a merchant is targeting for sales.

To learn more about markets, refer to [Shopify Markets](https://shopify.dev/docs/apps/markets). To ensure visitors interact with the optimal version of a store using Shopify Markets, refer to [Detect and set a visitor's optimal localization](https://shopify.dev/docs/themes/markets/localization-discovery).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| handle | string | The handle of the market. |
| id | string | The ID of the market. |
| metafields | array of metafield | The metafields applied to the market. To learn about creating metafields, refer to Create and manage metafields or visit the Shopify Help Center. |

#### Example

```json
{
  "handle": "ca",
  "id": 6157828161,
  "metafields": {}
}
```

---

### measurement

> Fonte: https://shopify.dev/docs/api/liquid/objects/measurement

A measurement from one of the following metafield types:

* `dimension`
* `volume`
* `weight`

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| type | string | The measurement type. Possible values: `dimension`, `volume`, `weight` |
| unit | string | The measurement unit. |
| value | number | The measurement value. |

#### Example

```json
{
  "type": "volume",
  "unit": "mL",
  "value": "500.0"
}
```

---

### media

> Fonte: https://shopify.dev/docs/api/liquid/objects/media

An abstract media object that can represent the following object types:

* [`image`](https://shopify.dev/docs/api/liquid/objects/image)
* [`model`](https://shopify.dev/docs/api/liquid/objects/model)
* [`video`](https://shopify.dev/docs/api/liquid/objects/video)
* [`external_video`](https://shopify.dev/docs/api/liquid/objects/external_video)

The `media` object can be returned by the [`product.media` array](https://shopify.dev/docs/api/liquid/objects/product#product-media) or a [`file_reference` metafield](https://shopify.dev/apps/metafields/types).

You can use [media filters](https://shopify.dev/docs/api/liquid/filters/media-filters) to generate URLs and media displays. To learn about how to use media in your theme, refer to [Support product media](https://shopify.dev/themes/product-merchandising/media/support-media).

> **Note:** Each media type has unique properties in addition to the general `media` properties. To learn about these additional properties, refer to the reference for each type.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| alt | string | The alt text of the media. |
| id | number | The ID of the media. |
| media_type | string | The media type. Possible values: `image`, `model`, `video`, `external_video` |
| position | number | The position of the media in the [`product.media` array](https://shopify.dev/docs/api/liquid/objects/product#product-media). If the source is a [`file_reference` metafield](https://shopify.dev/apps/metafields/types), then `nil` is returned. |
| preview_image | image | A preview image of the media. **Note:** Preview images don't have an ID attribute. |

#### Example: Filter for media of a specific type

You can use the `media_type` property with the [`where` filter](https://shopify.dev/docs/api/liquid/filters/where) to filter the [`product.media` array](https://shopify.dev/docs/api/liquid/objects/product#product-media) for all media of a desired type.

**Liquid Input:**
```liquid
{% assign images = product.media | where: 'media_type', 'image' %}

{% for image in images %}
  {{- image | image_url: width: 300 | image_tag }}
{% endfor %}
```

**Data:**
```json
{
  "product": {
    "media": [
      "products/oil-dripping-into-jar.jpg"
    ]
  }
}
```

**Output:**
```html
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/products/oil-dripping-into-jar.jpg?v=1650399519&amp;width=300" alt="Viper venom" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/products/oil-dripping-into-jar.jpg?v=1650399519&amp;width=300 300w" width="300" height="200">
```

**Example JSON:**
```json
{
  "alt": "Dandelion milk",
  "id": 21772527435841,
  "media_type": "image",
  "position": 1,
  "preview_image": {}
}
```

---

### metafield

> Fonte: https://shopify.dev/docs/api/liquid/objects/metafield

A [metafield](https://shopify.dev/apps/metafields) attached to a parent object.

To learn about how to access a metafield on a specific object, refer to Access metafields (below).

Metafields support [multiple data types](https://shopify.dev/apps/metafields/types), which determine the kind of information that's stored in the metafield. You can also output the metafield content in a type-specific format using [metafield filters](https://shopify.dev/docs/api/liquid/filters/metafield-filters).

> **Note:** You cannot create metafields in Liquid. Metafields can be created only in the following ways:
> - [In the Shopify admin](https://help.shopify.com/manual/metafields)
> - [Through an app](https://shopify.dev/apps/metafields)

> **Note:** Metafields of type `integer`, `json_string`, and `string` are older implementations that don't have the properties noted on this page, and aren't compatible with metafield filters. To learn more, refer to Deprecated metafields (below).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| list? | boolean | Returns `true` if the metafield is a list type. Returns `false` if not. **Tip:** To learn about metafield types, refer to [Metafield types](https://shopify.dev/apps/metafields/types). |
| type | string | The [type](https://shopify.dev/apps/metafields/types) of the metafield. Possible values: `single_line_text_field`, `multi_line_text_field`, `rich_text_field`, `product_reference`, `collection_reference`, `variant_reference`, `page_reference`, `file_reference`, `number_integer`, `number_decimal`, `date`, `date_time`, `url_reference`, `json`, `boolean`, `color`, `weight`, `volume`, `dimension`, `rating`, `money` |
| value | varies | The value of the metafield. Format depends on type (see table below). |

##### Value Formats by Type

| Type | Returned format |
|------|-----------------|
| `single_line_text_field` `multi_line_text_field` | A string |
| `rich_text_field` | A field that supports headings, lists, links, bold, and italics |
| `product_reference` | A [product object](https://shopify.dev/docs/api/liquid/objects/product) |
| `collection_reference` | A [collection object](https://shopify.dev/docs/api/liquid/objects/collection) |
| `variant_reference` | A [variant object](https://shopify.dev/docs/api/liquid/objects/variant) |
| `page_reference` | A [page object](https://shopify.dev/docs/api/liquid/objects/page) |
| `file_reference` | A [generic_file object](https://shopify.dev/docs/api/liquid/objects/generic-file) or [media object](https://shopify.dev/docs/api/liquid/objects/media) (images and videos only) |
| `number_integer` `number_decimal` | A number |
| `date` `date_time` | A date string. Use the [date filter](https://shopify.dev/docs/api/liquid/filters/date) to format. |
| `url_reference` | A URL string |
| `json` | A [JSON object](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON) |
| `boolean` | A boolean |
| `color` | A [color object](https://shopify.dev/docs/api/liquid/objects/color) |
| `weight` `volume` `dimension` | A [measurement object](https://shopify.dev/docs/api/liquid/objects/measurement) |
| `rating` | A [rating object](https://shopify.dev/docs/api/liquid/objects/rating) |
| `money` | A [money object](https://shopify.dev/docs/api/liquid/objects/money), displayed in the customer's local (presentment) currency |

#### Example

```json
{
  "list?": false,
  "type": "single_line_text_field",
  "value": "Take with a meal."
}
```

#### Access metafields

The access path for metafields consists of two layers:

- **namespace** - A grouping of metafields to prevent conflicts.
- **key** - The metafield name.

You can access the metafield object with the following syntax:

```liquid
{{ resource.metafields.namespace.key }}
```

**Code:**
```liquid
Type: {{ product.metafields.information.directions.type }}
Value: {{ product.metafields.information.directions.value }}
```

**Data:**
```json
{
  "product": {
    "metafields": {}
  }
}
```

**Output:**
```html
Type: single_line_text_field
Value: Take with a meal.
```

#### Accessing metafields of type `json`

The `value` property of metafields of type `json` returns a [JSON object](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON). You can access the properties of this object directly in Liquid, either by name or 0-based index. You can also iterate through the properties.

**Code:**
```liquid
Temperature: {{ product.metafields.information.burn_temperature.value.temperature }}
Unit: {{ product.metafields.information.burn_temperature.value['unit'] }}

{% for property in product.metafields.information.burn_temperature.value -%}
  {{ property.first | capitalize }}: {{ property.last }}
{%- endfor %}
```

**Data:**
```json
{
  "product": {
    "metafields": {}
  }
}
```

**Output:**
```html
Temperature: 700
Unit: degrees

Temperature: 700
Unit: degrees
Scale: Fahrenheit
```

#### Accessing metafields of type `list`

The `value` property of metafields of type `list` returns an array. You can iterate through the array to access the values.

**Code:**
```liquid
{% for item in product.metafields.information.combine_with.value -%}
  {{ item.product.title }}
{%- endfor %}
```

**Data:**
```json
{
  "product": {
    "metafields": {}
  }
}
```

**Output:**
```html
Blue Mountain Flower
Charcoal
```

If the list is of type `single_line_text_field`, then you can access the items in the array directly in Liquid using a 0-based index.

**Code:**
```liquid
First item in list: {{ product.metafields.information.pickup_locations.value[0] }}
Last item in list: {{ product.metafields.information.pickup_locations.value.last }}
```

**Data:**
```json
{
  "product": {
    "metafields": {}
  }
}
```

**Output:**
```html
First item in list: Ottawa
Last item in list: Vancouver
```

#### Determining the length of a list metafield

The way that you determine the length of a list metafield depends on its type:

- **[Reference types](https://shopify.dev/docs/apps/custom-data/metafields/types#reference-types)**: Use the `count` property to determine the list length.
- **Non-reference types**: These lists are rendered as arrays. Use the [`size` filter](https://shopify.dev/docs/api/liquid/filters/size) to determine the number of items in the array.

**Code:**
```liquid
# list.product_reference
Number of similar products: {{ product.metafields.information.similar_products.value.count }}

# list.single_line_text_field
Number of pickup locations: {{ product.metafields.information.pickup_locations.value.size }}
```

**Data:**
```json
{
  "product": {
    "metafields": {}
  }
}
```

**Output:**
```html
# list.product_reference
Number of similar products: 2

# list.single_line_text_field
Number of pickup locations: 4
```

#### Deprecated metafields

Deprecated metafields are older metafield types with limited functionality. The following metafield types are deprecated:

- `integer`
- `json_string`
- `string`

These metafield types don't have the same metafield object properties mentioned in the previous sections. Instead, they return the metafield value directly.

| Metafield type | Value type |
|---|---|
| `integer` | An [integer](https://shopify.dev/docs/api/liquid/basics#number) |
| `json_string` | A [JSON object](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON) |
| `string` | A [string](https://shopify.dev/docs/api/liquid/basics#string) |

---

### metaobject

> Fonte: https://shopify.dev/docs/api/liquid/objects/metaobject

A metaobject entry that includes values for a set of [fields](https://shopify.dev/docs/api/liquid/objects#metafield), with the field structure defined by the parent [`metaobject_definition`](https://shopify.dev/docs/api/liquid/objects#metaobject_definition).

#### Properties

| Name | Type | Description |
|------|------|-------------|
| system | [metaobject_system](https://shopify.dev/docs/api/liquid/objects/metaobject_system) | Basic information about the metaobject. These properties are grouped under the `system` object to avoid collisions between system property names and user-defined metaobject fields. |

#### Directly accessible in

- [metaobject](https://shopify.dev/themes/architecture/templates/metaobject)

#### Returned by

- [metaobjects](https://shopify.dev/docs/api/liquid/objects/metaobjects)

#### Access metaobjects individually

The access path for a metaobject consists of two layers:

- **type** - The type of the parent metaobject definition.
- **handle** - The unique [handle](https://shopify.dev/docs/api/liquid/basics#handles) of the metaobject.

Access a metaobject with the following syntax:

```liquid
{{ metaobjects.type.handle }}
```

You can also use square bracket notation:

```liquid
{{ metaobjects['type']['handle'] }}
```

Access a metaobject's field values using the field key:

```liquid
{{ metaobjects.testimonials.homepage.title }}
{{ metaobjects['highlights']['washable'].image.value }}
```

> **Note:** When the publishable capability is enabled, a metaobject can only be accessed if its status is active. If its status is draft, then the return value is nil.

#### Usage in metaobject templates

Within a metaobject template, the `metaobject` Liquid object represents the metaobject being rendered. Access it directly as `{{ metaobject }}`.

Basic example accessing a field within the associated metaobject template:

```liquid
{{ metaobject.title.value }}
```

Replace `title` with the key of the field you want to access. This outputs the value of that field for the current metaobject.

#### Templates using metaobject

- [Theme architecture](https://shopify.dev/themes/architecture/templates/metaobject)
- [metaobject template](https://shopify.dev/themes/architecture/templates/metaobject)

---

### metaobject_definition

> Fonte: https://shopify.dev/docs/api/liquid/objects/metaobject_definition

A `metaobject_definition` defines the structure of a metaobject type for the store, consisting of a merchant-defined set of [field definitions](https://help.shopify.com/en/manual/metafields/metafield-definitions).

One or more corresponding [`metaobject`](https://shopify.dev/docs/api/liquid/objects#metaobject) objects contain values for the fields specified in the metaobject definition.

> **Note:** When looping through metaobjects by accessing them using individual handles, you're limited to 20 unique handles per page and cannot use pagination. To iterate over more metaobjects, use the `values` property instead, which supports pagination up to 250 entries per page.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| values | array of [metaobject](https://shopify.dev/docs/api/liquid/objects/metaobject) | The metaobjects that follow the definition. |
| values_count | [number](https://shopify.dev/docs/api/liquid/basics#number) | The total number of entries for the metaobject definition. |

#### Loop over entries of a metaobject definition

If a metaobject definition has multiple metaobject entries, you can loop over them using the `values` property. You can loop over a maximum of 50 entries in a metaobject definition. For example, you can display the field `author` for each metaobject:

```liquid
{% for testimonial in metaobjects.testimonials.values %}
  {{ testimonial.author.value }}
{% endfor %}
```

> **Note:** When the `publishable` capability is enabled, loops return only metaobjects with a status of `active`. Metaobjects with `draft` status are skipped.

---

### metaobject_system

> Fonte: https://shopify.dev/docs/api/liquid/objects/metaobject_system

Basic information about a [`metaobject`](https://shopify.dev/api/liquid/objects#metaobject). These properties are grouped under the `system` object to avoid collisions between system property names and user-defined metaobject fields.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| handle | string | The unique [handle](https://shopify.dev/api/liquid/basics#handles) of the metaobject. |
| id | number | The ID of the metaobject. |
| type | string | The type of the metaobject definition. This is a free-form string that's defined when the metaobject definition is created. |
| url | string | The relative URL of the metaobject. Only set for metaobjects that have the `online_store` capability. |

#### Returned by

* [metaobject.system](https://shopify.dev/docs/api/liquid/objects/metaobject#metaobject-system)

#### Using the `metaobject_system` object

You can access the `metaobject_system` object and its properties through the metaobject's `system` property.

```liquid
{{ metaobjects.testimonials["home_page"].system.id }}
```

You can also access `metaobject_system` properties when iterating over a collection:

```liquid
{% for metaobject in product.metafields.custom.mixed_metaobject_list.value %}
  {% if metaobject.system.type == "testimonial" %}
    {% render 'testimonial' with metaobject as testimonial  %}
  {% else %}
    {{ metaobject.system.handle }}
  {% endif %}
{% endfor %}
```

---

### metaobjects

> Fonte: https://shopify.dev/docs/api/liquid/objects/metaobjects

All of the [metaobjects](https://shopify.dev/docs/api/liquid/objects/metaobject) of the store.

#### Access

Individual metaobjects can be accessed by specifying their type and handle. Refer to [Access metaobjects individually](https://shopify.dev/docs/api/liquid/objects#metaobject-access-metaobjects-individually) for more details.

You can also iterate over entries from a metaobject definition. See [Loop over entries of a metaobject definition](https://shopify.dev/docs/api/liquid/objects/metaobject_definition#metaobject_definition-loop-over-entries-of-a-metaobject-definition) for additional information.

#### Creation

Metaobjects are created in the [Content](https://www.shopify.com/admin/content) page of the Shopify admin.

#### Availability

* **Directly accessible in:** Global

---

### model

> Fonte: https://shopify.dev/docs/api/liquid/objects/model

A 3D model uploaded as product media.

> Use the `model_viewer_tag` filter to output a Google model viewer component for the model.

#### Properties

| Name | Type | Description |
|------|------|---|
| alt | string | The alt text of the model. |
| id | number | The ID of the model. |
| media_type | string | The media type of the model. Always returns `model`. |
| position | number | The position of the model in the `product.media` array. |
| preview_image | image | A preview image for the model. |
| sources | array of model_source | The source files for the model. |

#### Example: Filter for media of a specific type

You can use the `media_type` property with the `where` filter to filter the `product.media` array for all media of a desired type.

**Liquid:**
```liquid
{% assign models = product.media | where: 'media_type', 'model' %}

{% for model in models %}
  {{- model | model_viewer_tag }}
{% endfor %}
```

**Data:**
```json
{
  "product": {
    "media": [
      {
        "media_type": "model"
      }
    ]
  }
}
```

**Output:**
```html
<model-viewer src="//polinas-potent-potions.myshopify.com/cdn/shop/3d/models/o/eb9388299ce0557c/WaterBottle.glb?v=0" camera-controls="true" style="--poster-color: transparent;" data-shopify-feature="1.12" alt="Potion bottle" poster="//polinas-potent-potions.myshopify.com/cdn/shop/products/WaterBottle_small.jpg?v=1655189057"></model-viewer>
```

#### Example JSON

```json
{
  "alt": "Potion bottle",
  "id": 22064203137089,
  "media_type": "model",
  "position": 1,
  "preview_image": {},
  "sources": []
}
```

---

### model_source

> Fonte: https://shopify.dev/docs/api/liquid/objects/model_source

A model source file.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| format | string | The format of the model source file. |
| mime_type | string | The MIME type of the model source file. |
| url | string | The CDN URL of the model source file. |

#### Example

```json
{
  "format": "glb",
  "mime_type": "model/gltf-binary",
  "url": "//polinas-potent-potions.myshopify.com/cdn/shop/3d/models/o/eb9388299ce0557c/WaterBottle.glb?v=0"
}
```

---

### money

> Fonte: https://shopify.dev/docs/api/liquid/objects/money

A monetary value expressed in the customer's local (presentment) currency.

> **Tip:** Use money filters to output a formatted price.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| currency | [currency](https://shopify.dev/docs/api/liquid/objects/currency) | The customer's local (presentment) currency. |

#### Referencing money objects directly

When a money object is referenced directly, the monetary value in cents is returned.

**Liquid:**
```liquid
{{ product.metafields.details.price_per_100g.value }}
```

**Output:**
```html
1796
```

---

### order

> Fonte: https://shopify.dev/docs/api/liquid/objects/order

An [order](https://help.shopify.com/manual/orders).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| attributes | object | The attributes on the order. Returns `nil` if no attributes exist. Attributes are collected with the cart. |
| billing_address | [address](https://shopify.dev/docs/api/liquid/objects/address) | The billing address of the order. |
| cancel_reason | string | The reason the order was cancelled: `customer`, `declined`, `fraud`, `inventory`, `staff`, or `other`. |
| cancel_reason_label | string | The localized version of the cancellation reason. |
| cancelled | boolean | Returns `true` if cancelled, `false` otherwise. |
| cancelled_at | string | A timestamp for when the order was cancelled. |
| cart_level_discount_applications | array of [discount_application](https://shopify.dev/docs/api/liquid/objects/discount_application) | Discount applications at the order level. |
| confirmation_number | string | A randomly generated alpha-numeric identifier (e.g., "XPAV284CT"). Not guaranteed unique. |
| created_at | string | A timestamp for when the order was created. |
| customer | [customer](https://shopify.dev/docs/api/liquid/objects/customer) | The customer that placed the order. |
| customer_order_url | string | The URL for the new order details page. |
| customer_url | string | The URL for the customer to view the order in their account. |
| discount_applications | array of [discount_application](https://shopify.dev/docs/api/liquid/objects/discount_application) | All discount applications for the order and line items. |
| email | string | The email associated with the order. Returns `nil` if none. |
| financial_status | string | The order's financial status: `authorized`, `expired`, `paid`, `partially_paid`, `partially_refunded`, `pending`, `refunded`, `unpaid`, or `voided`. |
| financial_status_label | string | The localized version of the financial status. |
| fulfillment_status | string | The fulfillment status of the order. |
| fulfillment_status_label | string | The localized version of fulfillment status: `complete`, `fulfilled`, `partial`, `restocked`, or `unfulfilled`. |
| id | number | The ID of the order. |
| item_count | number | The number of items in the order. |
| line_items | array of [line_item](https://shopify.dev/docs/api/liquid/objects/line_item) | The line items in the order. |
| line_items_subtotal_price | number | Sum of line item prices after discounts, in currency subunit. |
| metafields | object | The metafields applied to the order. |
| name | string | The name of the order. |
| note | string | The note on the order. Returns `nil` if none. |
| order_number | number | The integer representation of the order name. |
| order_status_url | string | The URL for the Order status page. |
| phone | string | The phone number associated with the order. |
| pickup_in_store? | boolean | Returns `true` if a store pickup order. |
| shipping_address | [address](https://shopify.dev/docs/api/liquid/objects/address) | The shipping address of the order. |
| shipping_methods | array of [shipping_method](https://shopify.dev/docs/api/liquid/objects/shipping_method) | The shipping methods for the order. |
| shipping_price | number | The shipping price in currency subunit. |
| subtotal_line_items | array of [line_item](https://shopify.dev/docs/api/liquid/objects/line_item) | Non-tip line items used for subtotal calculation. |
| subtotal_price | number | Sum of subtotal line item prices after discounts, in currency subunit. |
| tags | array of string | The tags on the order, returned in alphabetical order. |
| tax_lines | array of [tax_line](https://shopify.dev/docs/api/liquid/objects/tax_line) | The tax lines on the order. |
| tax_price | number | Total taxes applied to the order in currency subunit. |
| total_discounts | number | Total discount amount in currency subunit. |
| total_duties | number | Sum of all duties on line items in currency subunit. Returns `nil` if none. |
| total_net_amount | number | Net amount after refunds in currency subunit. |
| total_price | number | Total price before refunds in currency subunit. |
| total_refunded_amount | number | Total refunded amount in currency subunit. |
| transactions | array of [transaction](https://shopify.dev/docs/api/liquid/objects/transaction) | The transactions of the order. |

#### Deprecated Properties

| Property | Type | Status |
|----------|------|--------|
| discounts | [discount](https://shopify.dev/docs/api/liquid/objects/discount) | Deprecated. Not all discount types and details are captured. Use `order.discount_applications` instead. |

#### Example

```liquid
<ul>
  {% for attribute in order.attributes -%}
    <li><strong>{{ attribute.first }}:</strong> {{ attribute.last }}</li>
  {%- endfor %}
</ul>
```

#### Example JSON

```json
{
  "attributes": {},
  "billing_address": {},
  "cancel_reason": null,
  "cancel_reason_label": null,
  "cancelled": false,
  "cancelled_at": null,
  "cart_level_discount_applications": [],
  "confirmation_number": "0YMJHPM8U",
  "created_at": "2022-04-29 11:15:46 -0400",
  "customer": {},
  "customer_order_url": "https://shopify.com/56174706753/account/orders/4295688749121?locale=en&region_country=CA&buyer_flags=...",
  "customer_url": "https://polinas-potent-potions.myshopify.com/account/orders/8be02e56c658bcd1f034d28c496fddd9",
  "discount_applications": [],
  "discounts": null,
  "email": "cornelius.potionmaker@gmail.com",
  "financial_status": "paid",
  "financial_status_label": "Paid",
  "fulfillment_status": "partial",
  "fulfillment_status_label": "Partial",
  "id": 4295688749121,
  "item_count": 6,
  "line_items": [],
  "line_items_subtotal_price": "492.93",
  "metafields": {},
  "name": "#1001",
  "note": null,
  "order_number": 1001,
  "order_status_url": "https://polinas-potent-potions.myshopify.com/56174706753/orders/8be02e56c658bcd1f034d28c496fddd9/authenticate?key=4f9baf2b8ebd0f75ec73eb9bac6e4519",
  "phone": null,
  "pickup_in_store?": false,
  "shipping_address": {},
  "shipping_methods": [],
  "shipping_price": "0.00",
  "subtotal_line_items": [],
  "subtotal_price": "492.93",
  "tags": [],
  "tax_lines": [],
  "tax_price": "0.00",
  "total_discounts": "0.00",
  "total_duties": null,
  "total_net_amount": "492.93",
  "total_price": "492.93",
  "total_refunded_amount": "0.00",
  "transactions": []
}
```

#### Templates using order

- [customers/order template](https://shopify.dev/themes/architecture/templates/customers-order)

---

### page

> Fonte: https://shopify.dev/docs/api/liquid/objects/page

A [page](https://help.shopify.com/manual/online-store/themes/theme-structure/pages) on a store.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| author | string | The author of the page. |
| content | string | The content of the page. |
| handle | string | The [handle](https://shopify.dev/docs/api/liquid/basics#handles) of the page. |
| id | number | The ID of the page. |
| metafields | — | The [metafields](https://shopify.dev/docs/api/liquid/objects/metafield) applied to the page. **Tip:** To learn about creating metafields, refer to [Create and manage metafields](/apps/metafields/manage) or visit the [Shopify Help Center](https://help.shopify.com/manual/metafields). |
| published_at | string | A timestamp for when the page was published. **Tip:** Use the [date filter](/docs/api/liquid/filters/date) to format the timestamp. |
| template_suffix | string | The name of the [custom template](https://shopify.dev/themes/architecture/templates#alternate-templates) assigned to the page. The name doesn't include the `page.` prefix, or the file extension (`.json` or `.liquid`). If a custom template isn't assigned to the page, then `nil` is returned. |
| title | string | The title of the page. |
| url | string | The relative URL of the page. |

#### Example

```json
{
  "author": null,
  "content": "<p>Polina's Potent Potions was started by Polina in 1654.</p>\n<p>We use all-natural locally sourced ingredients for our potions.</p>",
  "handle": "about-us",
  "id": 83536642113,
  "metafields": {},
  "published_at": "2022-05-04 17:47:03 -0400",
  "template_suffix": "",
  "title": "About us",
  "url": {}
}
```

#### Templates using page

- [Theme architecture](https://shopify.dev/themes/architecture/templates/page)
- [page template](https://shopify.dev/themes/architecture/templates/page)

---

### page_description

> Fonte: https://shopify.dev/docs/api/liquid/objects/page_description

The `page_description` object provides a brief description of a page for search engine listings and social media previews. This Liquid object represents the meta description of the current page and can be utilized across your store's theme.

#### Directly accessible in

- Global

To edit the meta description for a page, refer to the [Shopify Help Center documentation](https://help.shopify.com/manual/promoting-marketing/seo/adding-keywords#edit-the-title-and-meta-description-for-a-page).

---

### page_image

> Fonte: https://shopify.dev/docs/api/liquid/objects/page_image

An image displayed in search engine listings and social media previews for the current page.

The featured image from product pages, collection pages, and blog posts is utilized. For all other pages, or when no featured image exists, the [social sharing image](https://help.shopify.com/manual/online-store/images/showing-social-media-thumbnail-images?#setting-the-social-sharing-image-in-your-admin) is used instead.

#### Open Graph Fallback Tags

The `page_image` object enables creation of [Open Graph](https://ogp.me/) `og:image` meta tags. When a theme lacks `og:image` tags for a page, Shopify automatically generates these tags using the `page_image` object:

* `og:image`
* `og:image:secure_url`
* `og:image:width`
* `og:image:height`

#### Directly accessible in

* Global

---

### page_title

> Fonte: https://shopify.dev/docs/api/liquid/objects/page_title

The `page_title` object represents the title of the current page and can be utilized to define page titles for search engine listings and social media previews.

#### Directly accessible in

* Global

To learn more about editing page titles, refer to the [Shopify Help Center documentation](https://help.shopify.com/manual/promoting-marketing/seo/adding-keywords#edit-the-title-and-meta-description-for-a-page).

---

### pages

> Fonte: https://shopify.dev/docs/api/liquid/objects/pages

All of the [pages](https://shopify.dev/docs/api/liquid/objects/page) on a store.

#### Directly accessible in

* Global

You can access a specific page through the `pages` object using the page's [handle](https://shopify.dev/docs/api/liquid/basics#handles).

**Code:**
```liquid
{{ pages.contact.title }}
{{ pages['about-us'].title }}
```

**Output:**
```html
Contact
About us
```

#### Paginate the `pages` object

You can [paginate](https://shopify.dev/docs/api/liquid/tags/paginate) the `pages` object, allowing you to iterate over up to 50 pages at a time.

**Code:**
```liquid
{% paginate pages by 2 -%}
  {% for page in pages -%}
    {{ page.title | link_to: page.url }}
  {%- endfor %}

  {{- paginate | default_pagination }}
{%- endpaginate %}
```

**Output:**
```html
<a href="/pages/about-us" title="">About us</a>
<a href="/pages/contact" title="">Contact</a>

<span class="page current">1</span> <span class="page"><a href="/services/liquid_rendering/resource?page=2" title="">2</a></span> <span class="next"><a href="/services/liquid_rendering/resource?page=2" title="">Next &raquo;</a></span>
```

---

### paginate

> Fonte: https://shopify.dev/docs/api/liquid/objects/paginate

Information about the pagination inside a set of [`paginate` tags](/docs/api/liquid/tags/paginate).

> **Tip:** Use the [`default_pagination`](/docs/api/liquid/filters/default_pagination) filter to output pagination links.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| current_offset | number | The total number of items on pages previous to the current page. For example, if you show 5 items per page and are on page 3, then `paginate.current_offset` is 10. Limited to 24,999—see Pagination Limits for more information. |
| current_page | number | The page number of the current page. Limited to 25,000—see Pagination Limits for more information. |
| items | number | The total number of items to be paginated. For example, if you paginate a collection of 120 products, then `paginate.items` is 120. Limited to 25,000—see Pagination Limits for more information. |
| next | part | The pagination part to go to the next page. |
| page_param | string | The URL parameter denoting the pagination. The default value is `page`. If you paginate over an array defined in a setting or a metafield list type, then a unique key is appended to page to allow independent operation from other lists on the page. For example: `page_a9e329dc`. |
| page_size | number | The number of items displayed per page. Limited to 250. |
| pages | number | The total number of pages. Limited to 25,000—see Pagination Limits for more information. |
| parts | array of part | The pagination parts used to build pagination navigation. |
| previous | part | The pagination part to go to the previous page. |

#### Example

```json
{
  "current_offset": 10,
  "current_page": 3,
  "items": 17,
  "next": {},
  "page_param": "page",
  "page_size": 5,
  "pages": 4,
  "parts": [],
  "previous": {}
}
```

---

### parent_relationship

> Fonte: https://shopify.dev/docs/api/liquid/objects/parent_relationship

Information about the parent relationship for a nested cart line item.

#### Properties

| Name | Type | Description |
|------|------|-------------|
| parent | [line_item](https://shopify.dev/docs/api/liquid/objects/line_item) | The parent line item for the nested cart line item. |

#### Returned by

* [line_item.parent_relationship](https://shopify.dev/docs/api/liquid/objects/line_item#line_item-parent_relationship)

---

### part

> Fonte: https://shopify.dev/docs/api/liquid/objects/part

A part in the navigation for pagination.

#### Properties

| Name | Type | Description |
|------|------|-------------|
| is_link | boolean | Returns `true` if the part is a link. Returns `false` if not. |
| title | string | The page number associated with the part. |
| url | string | The URL of the part. It consists of the current page URL path with the pagination parameter for the current part appended. |

#### Example

```json
{
  "is_link": true,
  "title": "2",
  "url": "/collections/all?page=2"
}
```

#### Create pagination navigation with `part`

You can create a pagination navigation by iterating over each `part` of a `paginate` object.

**Code:**
```liquid
{% paginate collection.products by 5 -%}
  {% for part in paginate.parts -%}
    {% if part.is_link -%}
      {{ part.title | link_to: part.url}}
    {%- else -%}
      <span>{{ part.title }}</span>
    {% endif %}
  {%- endfor %}
{%- endpaginate %}
```

**Data:**
```json
{
  "collection": {
    "products_count": 19
  }
}
```

**Output:**
```html
<span>1</span>
    
<a href="/services/liquid_rendering/resource?page=2" title="">2</a>

<a href="/services/liquid_rendering/resource?page=3" title="">3</a>

<a href="/services/liquid_rendering/resource?page=4" title="">4</a>
```

---

### pending_payment_instruction_input

> Fonte: https://shopify.dev/docs/api/liquid/objects/pending_payment_instruction_input

Header-value pairs that make up the list of payment information specific to the payment method. This data enables customers to finalize purchases through offline channels.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| header | string | The header of the payment instruction. These are payment method-specific. Example: 'Entity' and 'Reference' for Multibanco |
| value | string | Contains the corresponding values to the headers of the payment instruction. |

#### Returned by

* `transaction.buyer_pending_payment_instructions`

---

### policy

> Fonte: https://shopify.dev/docs/api/liquid/objects/policy

A [store policy](https://help.shopify.com/manual/checkout-settings/refund-privacy-tos), such as a privacy or return policy.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| body | string | The content of the policy. |
| id | string | The ID of the policy. |
| title | string | The title of the policy. |
| url | string | The relative URL of the policy. |

#### Example

```json
{
  "body": "<p>We have a 30-day return policy, which means you have 30 days after receiving your item to request a return. ...</p>",
  "id": 23805034561,
  "title": "Refund policy",
  "url": "/policies/refund-policy"
}
```

---

### powered_by_link

> Fonte: https://shopify.dev/docs/api/liquid/objects/powered_by_link

Creates an HTML link element that links to a localized version of `shopify.com`, based on the locale of the store.

#### Directly accessible in

* Global

#### Code

**Liquid input:**
```liquid
{{ powered_by_link }}
```

**Rendered output:**
```html
<a target="_blank" rel="nofollow" href="https://www.shopify.com?utm_campaign=poweredby&amp;utm_medium=shopify&amp;utm_source=onlinestore">Powered by Shopify</a>
```

---

### predictive_search

> Fonte: https://shopify.dev/docs/api/liquid/objects/predictive_search

Information about the results from a predictive search query through the [Predictive Search API](https://shopify.dev/api/ajax/reference/predictive-search#get-locale-search-suggest).

> The `predictive_search` object returns results only when rendered in a section using the Predictive Search API and the Section Rendering API.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| performed | boolean | Returns `true` when being referenced inside a section that's been rendered using the Predictive Search API and the Section Rendering API. Returns `false` if not. |
| resources | predictive_search_resources | The resources associated with the query. You can check whether any resources of a specific type were returned using the `size` filter. |
| terms | string | The entered search terms. Use the `highlight` filter to emphasize search terms in results. |
| types | array of string | The object types that the search was performed on. Possible values: `article`, `collection`, `page`, `product` |

#### Example

```json
{
  "performed": true,
  "resources": {},
  "terms": "potion",
  "types": []
}
```

#### Usage Example

```liquid
{% if predictive_search.resources.articles.size > 0 %}
  {% for article in predictive_search.resources.articles %}
    {{ article.title }}
  {% endfor %}
{% endif %}
```

---

### predictive_search_resources

> Fonte: https://shopify.dev/docs/api/liquid/objects/predictive_search_resources

Contains arrays of objects for each resource type that can be returned by a [predictive search query](https://shopify.dev/api/ajax/reference/predictive-search#get-locale-search-suggest).

You can check whether any resources of a specific type were returned using the [`size` filter](https://shopify.dev/docs/api/liquid/filters/size).

```liquid
{% if predictive_search.resources.articles.size > 0 %}
  {% for article in predictive_search.resources.articles %}
    {{ article.title }}
  {% endfor %}
{% endif %}
```

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| articles | array of [article](https://shopify.dev/docs/api/liquid/objects/article) | The articles associated with the query. |
| collections | array of [collection](https://shopify.dev/docs/api/liquid/objects/collection) | The collections associated with the query. |
| pages | array of [page](https://shopify.dev/docs/api/liquid/objects/page) | The pages associated with the query. |
| products | array of [product](https://shopify.dev/docs/api/liquid/objects/product) | The products associated with the query. |

#### Example

```json
{
  "articles": [],
  "collections": [],
  "pages": [],
  "products": []
}
```

---

### product

> Fonte: https://shopify.dev/docs/api/liquid/objects/product

A [product](https://help.shopify.com/manual/products) in the store.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| available | boolean | Returns `true` if at least one variant is available. For availability, a variant needs: inventory_quantity > 0, inventory_policy set to "continue", inventory_management as nil, or an associated delivery profile with valid shipping rate. |
| category | taxonomy_category | The taxonomy category for the product |
| collections | array of collection | Collections the product belongs to. Note: Collections unavailable on Online Store sales channel aren't included. |
| compare_at_price | number | Lowest compare at price of any variants in currency's subunit, in customer's local currency. |
| compare_at_price_max | number | Highest compare at price of any variants in currency's subunit, in customer's local currency. |
| compare_at_price_min | number | Lowest compare at price of any variants (same as compare_at_price), in currency's subunit. |
| compare_at_price_varies | boolean | Returns `true` if variant compare at prices vary; `false` otherwise. |
| content | string | Product description (same as product.description). |
| created_at | string | Timestamp when product was created. Use date filter to format. |
| description | string | Product description (same as product.content). |
| featured_image | image | First (featured) image attached to the product. |
| featured_media | media | First (featured) media attached to the product. In search/filtered collections, returns most relevant variant's media. |
| first_available_variant | variant | First available variant. Availability requires: inventory_quantity > 0, inventory_policy "continue", or inventory_management nil. |
| gift_card? | boolean | Returns `true` if product is a gift card; `false` otherwise. |
| handle | string | Handle of the product. |
| has_only_default_variant | boolean | Returns `true` if product has no options; `false` otherwise. |
| id | number | ID of the product. |
| images | array of image | Images attached to the product. |
| media | array of media | Media attached to the product, sorted by date added. |
| metafields | metafield | Metafields applied to the product. |
| options | array of string | Option names of the product. |
| options_by_name | product_option | Access specific product option by name (case-insensitive). |
| options_with_values | array of product_option | Options on the product. |
| price | number | Lowest price of any variants (same as price_min), in currency's subunit. |
| price_max | number | Highest price of any variants in currency's subunit. |
| price_min | number | Lowest price of any variants (same as price), in currency's subunit. |
| price_varies | boolean | Returns `true` if variant prices vary; `false` otherwise. |
| published_at | string | Timestamp when product was published. Use date filter to format. |
| quantity_price_breaks_configured? | boolean | Returns `true` if product has variant with quantity price breaks; `false` otherwise. |
| requires_selling_plan | boolean | Returns `true` if all variants require selling plan; `false` otherwise. |
| selected_or_first_available_selling_plan_allocation | selling_plan_allocation | Currently selected or first available selling plan allocation. Returns nil if no selling plans exist. |
| selected_or_first_available_variant | variant | Currently selected or first available variant. If none available, returns first variant. |
| selected_selling_plan | selling_plan | Currently selected selling plan. Returns nil if none selected. |
| selected_selling_plan_allocation | selling_plan_allocation | Currently selected selling plan allocation for selected variant. Returns nil if none selected. |
| selected_variant | variant | Currently selected variant. Returns nil if none selected. |
| selling_plan_groups | array of selling_plan_group | Selling plan groups variants are included in. |
| tags | array of string | Product tags in alphabetical order. |
| template_suffix | string | Name of custom template (without product. prefix or file extension). Returns nil if none assigned. |
| title | string | Title of the product. |
| type | string | Type of the product. |
| url | string | Relative URL of the product. May include variant parameter or tracking parameters for recommendations. |
| variants | array of variant | Product variants (max 250 unpaginated; use paginate tag for up to 50 per page). |
| variants_count | number | Total number of variants for the product. |
| vendor | string | Vendor of the product. |

#### Example

```json
{
  "available": true,
  "category": {},
  "collections": [],
  "compare_at_price": "25.00",
  "compare_at_price_max": "25.00",
  "compare_at_price_min": "25.00",
  "compare_at_price_varies": false,
  "content": "<h3>Are you low on health? Well we've got the potion just for you!</h3>\n<p>Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!</p>",
  "created_at": "2022-04-13 14:46:16 -0400",
  "description": "<h3>Are you low on health? Well we've got the potion just for you!</h3>\n<p>Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!</p>",
  "featured_image": {},
  "featured_media": {},
  "first_available_variant": {},
  "gift_card?": false,
  "handle": "health-potion",
  "has_only_default_variant": false,
  "id": 6786188247105,
  "images": [],
  "media": [],
  "metafields": {},
  "options": [
    "Size",
    "Strength"
  ],
  "options_by_name": {},
  "options_with_values": [],
  "price": "10.00",
  "price_max": "22.00",
  "price_min": "10.00",
  "price_varies": true,
  "published_at": "2022-04-13 14:53:34 -0400",
  "quantity_price_breaks_configured?": false,
  "requires_selling_plan": false,
  "selected_or_first_available_selling_plan_allocation": {},
  "selected_or_first_available_variant": {},
  "selected_selling_plan": null,
  "selected_selling_plan_allocation": null,
  "selected_variant": null,
  "selling_plan_groups": [],
  "tags": [
    "healing"
  ],
  "template_suffix": "",
  "title": "Health potion",
  "type": {},
  "url": {},
  "variants": [],
  "variants_count": 9,
  "vendor": "Polina's Potent Potions"
}
```

#### Output the options

```liquid
{% if product.options.size > 0 -%}
  {% for option in product.options -%}
    - {{ option }}
  {%- endfor %}
{%- endif %}
```

**Data:**
```json
{
  "product": {
    "options": [
      "Size",
      "Strength"
    ]
  }
}
```

**Output:**
```html
- Size
- Strength
```

#### Output the values for a specific option

```liquid
<label>
  Strength
  <select>
    {%- for value in product.options_by_name['strength'].values %}
    <option>{{ value }}</option>
    {%- endfor %}
  </select>
</label>
```

**Data:**
```json
{
  "product": {
    "options_by_name": {}
  }
}
```

**Output:**
```html
<label>
  Strength
  <select>
    <option>Low</option>
    <option>Medium</option>
    <option>High</option>
  </select>
</label>
```

---

### product_option

> Fonte: https://shopify.dev/docs/api/liquid/objects/product_option

A product option, such as size or color.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| name | string | The name of the product option. |
| position | number | The 1-based index of the product option in the `product.options_with_values` array. |
| selected_value | string | The currently selected product option value. If no value is currently selected, then the first available variant is returned. |
| values | array of product_option_value | The possible values for the product option. |

#### Example

```json
{
  "name": "Size",
  "position": 1,
  "selected_value": {},
  "values": []
}
```

---

### product_option_value

> Fonte: https://shopify.dev/docs/api/liquid/objects/product_option_value

A product option value, such as "red" for the option "color".

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| available | boolean | Whether or not the option value is available. In context of selected values for previous options, indicates whether the current option value has purchaseable combinations in subsequent options, or whether it's purchaseable if no subsequent options exist. For example, if a product has Color/Size/Material and Red/Small/Cotton is selected, `available` shows: Color - whether any variants for that Color option value are available for purchase; Size - whether any variants for Color:Red and the Size option value are available; Material - whether any variants for Color:Red, Size:Small, and Material option value are available. |
| id | number | The ID of the product option value. |
| name | string | The name of the product option value. |
| product_url | string | Returns a URL if the option value may be associated with another product, nil otherwise. |
| selected | boolean | Whether or not the option value is selected. |
| swatch | swatch | Returns a swatch drop for the product option value. If there is no saved `color` or `image` content for the swatch, then the return value is `nil`. |
| variant | variant | The variant associated with this option value combined with the other currently selected option values, if one exists. If selected, returns the `selected_or_first_available_variant`. If not selected, returns the variant associated with the current option value and other currently selected option values. Using optionValue.variant is the recommended approach for rendering product option values availability. |

#### Example

```json
{
  "available": true,
  "id": 2070385033281,
  "name": "Bronze",
  "product_url": null,
  "selected": true,
  "swatch": {},
  "variant": {}
}
```

---

### quantity_price_break

> Fonte: https://shopify.dev/docs/api/liquid/objects/quantity_price_break

The per-unit price of a variant when purchasing the minimum quantity or more.

#### Properties

| Name | Type | Description |
|------|------|-------------|
| minimum_quantity | number | The minimum quantity required to qualify for the price break. |
| price | number | The price for the quantity price break once the minimum quantity is met. The value is the price in the customer's local (presentment) currency. **Tip:** Use money filters to output a formatted price. |

#### Example

```json
{
  "minimum_quantity": "10",
  "price": "20.00"
}
```

---

### quantity_rule

> Fonte: https://shopify.dev/docs/api/liquid/objects/quantity_rule

A variant order quantity rule.

If no rule exists, then a default value is returned. This rule can be set as part of a "B2B catalog" for quantity pricing purposes.

> The default quantity rule is `min=1,max=null,increment=1`.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| increment | number | The number the order quantity can be incremented by. The default value is `1`. |
| max | number | The maximum order quantity. If there is no maximum quantity, then `nil` is returned. |
| min | number | The minimum order quantity. The default value is `1`. |

#### Example

```json
{
  "min": 5,
  "max": 100,
  "increment": 5
}
```

#### The variant order quantity rule

**Code:**
```liquid
{{ product.variants.first.quantity_rule }}
```

**Data:**
```json
{
  "product": {
    "variants": [
      {
        "quantity_rule": {
          "min": 1,
          "max": null,
          "increment": 1
        }
      }
    ]
  }
}
```

**Output:**
```html
{"min"=>1, "max"=>nil, "increment"=>1}
```

---

### rating

> Fonte: https://shopify.dev/docs/api/liquid/objects/rating

Information for a [`rating` type](https://shopify.dev/apps/metafields/types) metafield.

> To learn about metafield types, refer to [Metafield types](/apps/metafields/types).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| rating | [number](https://shopify.dev/docs/api/liquid/basics#number) | The rating value. |
| scale_max | [number](https://shopify.dev/docs/api/liquid/basics#number) | The maximum value of the rating scale. |
| scale_min | [number](https://shopify.dev/docs/api/liquid/basics#number) | The minimum value of the rating scale. |

#### Example

```json
{
  "rating": "4.5",
  "scale_max": "5.0",
  "scale_min": "0.0"
}
```

---

### recipient

> Fonte: https://shopify.dev/docs/api/liquid/objects/recipient

A recipient that is associated with a [gift card](https://help.shopify.com/manual/products/gift-card-products).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| email | string | The email of the recipient. |
| name | string | The full name of the recipient. |
| nickname | string | The nickname of the recipient. |

#### Example

```json
{
  "email": "cornelius.potionmaker@gmail.com",
  "name": "Cornelius Potionmaker",
  "nickname": "Cornelius"
}
```

#### Templates using recipient

- [Theme architecture](https://shopify.dev/themes/architecture/templates/gift-card-liquid)
- [gift_card.liquid template](https://shopify.dev/themes/architecture/templates/gift-card-liquid)

---

### recommendations

> Fonte: https://shopify.dev/docs/api/liquid/objects/recommendations

Product recommendations for a specific product based on sales data, product descriptions, and collection relationships.

Product recommendations become more accurate over time as new orders and product data become available. To learn more about how product recommendations are generated, refer to [Product recommendations](https://shopify.dev/themes/product-merchandising/recommendations).

> **Note:** The `recommendations` object returns products only when rendered in a section using the [Product Recommendations API](/api/ajax/reference/product-recommendations) and the [Section Rendering API](/api/section-rendering).

#### Properties

| Name | Type | Description |
|------|------|-------------|
| intent | [string](https://shopify.dev/docs/api/liquid/basics#string) | The recommendation intent. If `performed?` is `false`, then `nil` is returned. |
| performed? | [boolean](https://shopify.dev/docs/api/liquid/basics#boolean) | Returns `true` when being referenced inside a section that's been rendered using the Product Recommendations API and the Section Rendering API. Returns `false` if not. |
| products | array of [product](https://shopify.dev/docs/api/liquid/objects/product) | The recommended products. If `performed?` is `false`, then an [EmptyDrop](https://shopify.dev/docs/api/liquid/basics#emptydrop) is returned. |
| products_count | [number](https://shopify.dev/docs/api/liquid/basics#number) | The number of recommended products. If `performed?` is `false`, then 0 is returned. |

#### Example

```json
{
  "products": [],
  "products_count": 4,
  "performed?": true
}
```

---

### remote_details

> Fonte: https://shopify.dev/docs/api/liquid/objects/remote_details

Information about the remote source from which the object came from.

Remote details can only be accessed on an object that comes from a remote source, such as a product from another store.

#### Properties

| Name | Type | Description |
|------|------|-------------|
| shop | [remote_shop](https://shopify.dev/docs/api/liquid/objects/remote_shop) | Information about the store that the remote object came from. |
| type | [string](https://shopify.dev/docs/api/liquid/basics#string) | Provides context on how the remote object was surfaced. Currently the only supported value is "seller", but this may be expanded in the future. |

#### Returned by

* [remote_product](https://shopify.dev/docs/api/liquid/objects/remote_product)
* [remote_product.remote_details](https://shopify.dev/docs/api/liquid/objects/remote_product#remote_product-remote_details)

---

### remote_product

> Fonte: https://shopify.dev/docs/api/liquid/objects/remote_product

A product sourced remotely, inheriting all [product](https://shopify.dev/docs/api/liquid/objects/product) functionality while providing additional context about the remote source.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| available | boolean | Returns `true` if at least one product variant is available. Returns `false` otherwise. A variant qualifies as available if: the `inventory_quantity` exceeds 0, `inventory_policy` is set to `continue`, `inventory_management` is `nil`, or it has an associated delivery profile with valid shipping. |
| category | taxonomy_category | The taxonomy category for the product. |
| compare_at_price | number | Lowest compare-at price among variants in currency subunits, displayed in customer's local currency. For currencies without subunits (JPY, KRW), tenths and hundredths are appended. Use money filters for formatted output. |
| compare_at_price_max | number | Highest compare-at price among variants in currency subunits, in customer's local currency. Use money filters for formatting. |
| compare_at_price_min | number | Lowest compare-at price among variants (equivalent to `compare_at_price`) in currency subunits, in customer's local currency. Use money filters for formatting. |
| compare_at_price_varies | boolean | Returns `true` if variant compare-at prices differ. Returns `false` if uniform. |
| content | string | Product description (equivalent to `description`). |
| created_at | string | Timestamp when product was created. Use the `date` filter for formatting. |
| description | string | Product description. For remote products, this includes a link to remote store shipping and refund policies if defined. |
| featured_image | image | The first (featured) image attached to the product. |
| featured_media | media | The first (featured) media attached to the product. May include a badge highlighting the remote source depending on rendering context. Use media filters for URLs and displays. |
| first_available_variant | variant | The first available variant. A variant is available if `inventory_quantity` > 0, `inventory_policy` is `continue`, or `inventory_management` is `nil`. |
| gift_card? | boolean | Returns `true` if the product is a gift card. Returns `false` otherwise. |
| has_only_default_variant | boolean | Returns `true` if product has no options. Returns `false` otherwise. |
| id | number | The product ID. |
| images | array of image | Images attached to the product. |
| media | array of media | Product media sorted by addition date. May include remote source badges. Use media filters for output. |
| metafields | metafields | Metafields applied to the product. Only standard metafields from the remote store are included; custom metafields are excluded. |
| options | array of string | Product option names. Use `size` filter with dot notation to determine option count. |
| options_by_name | product_option | Access specific product options by name (case-insensitive). |
| options_with_values | array of product_option | Product options with their values. |
| price | number | Lowest variant price in currency subunits (equivalent to `price_min`), in customer's local currency. Use money filters for formatting. |
| price_max | number | Highest variant price in currency subunits, in customer's local currency. Use money filters for formatting. |
| price_min | number | Lowest variant price in currency subunits (equivalent to `price`), in customer's local currency. Use money filters for formatting. |
| price_varies | boolean | Returns `true` if variant prices differ. Returns `false` if uniform. |
| published_at | string | Timestamp when product was published. Use the `date` filter for formatting. |
| quantity_price_breaks_configured? | boolean | Returns `true` if at least one variant has quantity price breaks in current customer context. Returns `false` otherwise. |
| remote_details | remote_details | Information about the remote source from which the product originated. |
| requires_selling_plan | boolean | Returns `true` if all variants require a selling plan. Returns `false` otherwise. |
| selected_or_first_available_selling_plan_allocation | selling_plan_allocation | The currently selected or first available selling plan allocation. Uses specific logic to determine selection based on variant and selling plan URL parameters. |
| selected_or_first_available_variant | variant | Currently selected or first available variant. Selected variant is determined by `variant` URL parameter (product pages) or relevance (search/collections). |
| selected_selling_plan | selling_plan | Currently selected selling plan (determined by `selling_plan` URL parameter). Returns `nil` if none selected. |
| selected_selling_plan_allocation | selling_plan_allocation | Currently selected selling plan allocation for the selected variant. Returns `nil` if no variant and plan are selected. |
| selected_variant | variant | Currently selected variant (determined by `variant` URL parameter). Returns `nil` if none selected. |
| selling_plan_groups | array of selling_plan_group | Selling plan groups that product variants belong to. |
| template_suffix | string | Custom template name assigned to product. Remote products use dedicated template names prefixed with "remote." (e.g., "remote.seller"). |
| title | string | Product title. In cart or search suggestions, appended with "Sold by {store name}". |
| type | string | Product type classification. |
| url | string | Relative product URL. In search/collections, includes `variant` parameter for most relevant variant. As recommendations, includes tracking parameters. |
| variants | array of variant | Product variants (maximum 250 unpaginated). Use `paginate` tag for up to 50 per page. |
| variants_count | number | Total number of product variants. |
| vendor | string | Product vendor name. |

#### Examples

##### Output product options

```liquid
{% if product.options.size > 0 -%}
  {% for option in product.options -%}
    - {{ option }}
  {%- endfor %}
{%- endif %}
```

**Data:**
```json
{
  "product": {
    "options": [
      "Size",
      "Strength"
    ]
  }
}
```

**Output:**
```html
- Size
- Strength
```

##### Output values for a specific option

```liquid
<label>
  Strength
  <select>
    {%- for value in product.options_by_name['strength'].values %}
    <option>{{ value }}</option>
    {%- endfor %}
  </select>
</label>
```

**Output:**
```html
<label>
  Strength
  <select>
    <option>Low</option>
    <option>Medium</option>
    <option>High</option>
  </select>
</label>
```

#### Directly accessible in

- [product](https://shopify.dev/themes/architecture/templates/product)

#### Returned by

- [collection.products](https://shopify.dev/docs/api/liquid/objects/collection#collection-products)
- [line_item.product](https://shopify.dev/docs/api/liquid/objects/line_item#line_item-product)
- [search.results](https://shopify.dev/docs/api/liquid/objects/search#search-results)
- [variant.product](https://shopify.dev/docs/api/liquid/objects/variant#variant-product)

#### Templates using remote_product

- [product template](https://shopify.dev/themes/architecture/templates/product)

---

### remote_shop

> Fonte: https://shopify.dev/docs/api/liquid/objects/remote_shop

Information about a remote store.

Remote store information is only present via remote details, if the product comes from a remote source (i.e. a product from another store).

#### Properties

| Name | Type | Description |
|------|------|-------------|
| brand | [brand](https://shopify.dev/docs/api/liquid/objects/brand) | The brand assets for the remote store. |
| name | [string](https://shopify.dev/docs/api/liquid/basics#string) | The name of the remote store. |
| policies | array of [policy](https://shopify.dev/docs/api/liquid/objects/policy) | The shipping and refund policies for the remote store. Set in the remote store's Policies settings. |
| refund_policy | [policy](https://shopify.dev/docs/api/liquid/objects/policy) | The refund policy for the remote store. |
| shipping_policy | [policy](https://shopify.dev/docs/api/liquid/objects/policy) | The shipping policy for the remote store. |

#### Returned by

* [remote_product.remote_details](https://shopify.dev/docs/api/liquid/objects/remote_product#remote_product-remote_details)
* [remote_details.shop](https://shopify.dev/docs/api/liquid/objects/remote_details#remote_details-shop)

---

### request

> Fonte: https://shopify.dev/docs/api/liquid/objects/request

Information about the current URL and the associated page.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| design_mode | boolean | Returns `true` if the request is being made from within the theme editor. Returns `false` if not. You can use `request.design_mode` to control theme behavior depending on whether the theme is being viewed in the editor. For example, you can prevent session data from being tracked by tracking scripts in the theme editor. **Caution:** You shouldn't use `request.design_mode` to change customer-facing functionality. The theme editor preview should match what the merchant's customers see on the live store. |
| host | string | The domain that the request is hosted on. |
| locale | shop_locale | The locale of the request. |
| origin | string | The protocol and host of the request. |
| page_type | string | The type of page being requested. Possible values: 404, article, blog, captcha, cart, collection, list-collections, customers/account, customers/activate_account, customers/addresses, customers/login, customers/order, customers/register, customers/reset_password, gift_card, index, metaobject, page, password, policy, product, search |
| path | string | The path of the request. **Note:** If the current path is for a page that doesn't exist, then `nil` is returned. |
| visual_preview_mode | boolean | Returns `true` if the request is being made from within the theme editor's visual section preview. Returns `false` if not. You can use `request.visual_preview_mode` to control theme behavior depending on whether the theme is being viewed in the editor's visual section preview. For example, you can remove any scripts that interfere with how the section is displayed. |

#### Example: Create a context-aware absolute URL

You can use `request.origin` with any object, object property, or filter that returns a relative URL to build a context-aware absolute URL.

**Liquid:**
```liquid
{{ product.selected_variant.url | default: product.url | prepend: request.origin }}
```

**Data:**
```json
{
  "product": {
    "selected_variant": null,
    "url": "/products/health-potion"
  },
  "request": {
    "origin": "https://polinas-potent-potions.myshopify.com"
  }
}
```

**Output:**
```html
https://polinas-potent-potions.myshopify.com/products/health-potion
```

#### Example object

```json
{
  "design_mode": false,
  "host": "polinas-potent-potions.myshopify.com",
  "locale": {},
  "origin": "https://polinas-potent-potions.myshopify.com",
  "page_type": "index",
  "path": "/",
  "visual_preview_mode": false
}
```

---

### robots

> Fonte: https://shopify.dev/docs/api/liquid/objects/robots

The default rule groups for the `robots.txt` file.

> You can customize the `robots.txt` file with the `robots.txt.liquid` template.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| default_groups | array of [group](https://shopify.dev/docs/api/liquid/objects/group) | The rule groups. |

#### Example

```json
{
  "default_groups": []
}
```

#### Templates using robots

- [Theme architecture](https://shopify.dev/themes/architecture/templates/robots-txt-liquid)
- [robots.txt.liquid template](https://shopify.dev/themes/architecture/templates/robots-txt-liquid)

---

### routes

> Fonte: https://shopify.dev/docs/api/liquid/objects/routes

Allows you to generate standard URLs for the storefront.

Using the `routes` object instead of hardcoding URLs helps ensure that your theme supports multiple languages, as well as any possible changes in URL format.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| account_addresses_url | string | The account addresses page URL. Redirects to customer accounts when enabled. |
| account_login_url | string | The account login page URL. Redirects to customer accounts when enabled. |
| account_logout_url | string | The URL to log a customer out of their account. Redirects to customer accounts when enabled. |
| account_profile_url | string | The URL for the customer accounts profile page. |
| account_recover_url | string | The password recovery page URL. Redirects to customer accounts when enabled. |
| account_register_url | string | The account registration page URL. |
| account_url | string | The account page URL. Redirects to customer accounts when enabled. |
| all_products_collection_url | string | The all-products collection page URL. The all-products collection is automatically generated by Shopify and contains all products in the store. |
| cart_add_url | string | The URL for the `/cart/add` Cart API endpoint. |
| cart_change_url | string | The URL for the `/cart/change` Cart API endpoint. |
| cart_clear_url | string | The URL for the `/cart/clear` Cart API endpoint. |
| cart_update_url | string | The URL for the `/cart/update` Cart API endpoint. |
| cart_url | string | The cart page URL. |
| collections_url | string | The collection list page URL. |
| predictive_search_url | string | The Predictive Search API URL. |
| product_recommendations_url | string | The Product Recommendations API URL. |
| root_url | string | The index (home page) URL. |
| search_url | string | The search page URL. |
| storefront_login_url | string | Customer accounts login page. Redirects to the storefront page the customer was on before visiting the login page. |

#### Example

```json
{
  "account_addresses_url": "/account/addresses",
  "account_login_url": "/account/login",
  "account_logout_url": "/account/logout",
  "account_profile_url": "https://shopify.com/56174706753/account/profile?locale=en&region_country=CA&buyer_flags=...",
  "account_recover_url": "/account/recover",
  "account_register_url": "/account/register",
  "account_url": "/account",
  "all_products_collection_url": "/collections/all",
  "cart_add_url": "/cart/add",
  "cart_change_url": "/cart/change",
  "cart_clear_url": "/cart/clear",
  "cart_update_url": "/cart/update",
  "cart_url": "/cart",
  "collections_url": "/collections",
  "predictive_search_url": "/search/suggest",
  "product_recommendations_url": "/recommendations/products",
  "root_url": "/",
  "search_url": "/search",
  "storefront_login_url": "/customer_authentication/login?return_to=%2Fservices%2Fliquid_rendering%2Fresource%3Ffast_storefront_renderer%3D1&locale=en&ui_hint=full"
}
```

---

### rule

> Fonte: https://shopify.dev/docs/api/liquid/objects/rule

A rule for the `robots.txt` file, which tells crawlers which pages can, or can't, be accessed.

A rule consists of a directive, which can be either `Allow` or `Disallow`, and a value of the associated URL path. For example:

```
Disallow: /policies/
```

You can output a rule directly, instead of referencing each of its properties.

> **Tip:** You can customize the `robots.txt` file with the `robots.txt.liquid` template.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| directive | string | The directive of the rule. |
| value | string | The value of the rule. |

#### Example

```json
{
  "directive": "Disallow",
  "value": "/*preview_script_id*"
}
```

---

### script

> Fonte: https://shopify.dev/docs/api/liquid/objects/script

Information about a Shopify Script.

> **Caution:** Shopify Scripts will be sunset on August 28, 2025. Migrate your existing scripts to Shopify Functions before this date.

> **Tip:** To learn more about Shopify Scripts and the Script Editor, visit the Shopify Help Center.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| id | number | The ID of the script. |
| name | string | The name of the script. |

#### Example

```json
{
  "id": 209584193,
  "name": "10% off Whole bloodroot"
}
```

---

### search

> Fonte: https://shopify.dev/docs/api/liquid/objects/search

Information about a storefront search query.

To learn about storefront search and how to include it in your theme, refer to [Storefront search](https://shopify.dev/themes/navigation-search/search).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| default_sort_by | [string](https://shopify.dev/docs/api/liquid/basics#string) | The default sort order of the search results, which is `relevance`. |
| filters | array of [filter](https://shopify.dev/docs/api/liquid/objects/filter) | Only filters relevant to current search results are returned. If results contain more than 1000 products, the array is empty. |
| performed | [boolean](https://shopify.dev/docs/api/liquid/basics#boolean) | Returns `true` if a search was successfully performed. Returns `false` if not. |
| results | array | The search result items. An item can be an `article`, a `page`, or a `product`. |
| results_count | [number](https://shopify.dev/docs/api/liquid/basics#number) | The number of results. |
| sort_by | [string](https://shopify.dev/docs/api/liquid/basics#string) | The sort order of the search results. This is determined by the `sort_by` URL parameter. If no parameter exists, the value is `nil`. |
| sort_options | array of [sort_option](https://shopify.dev/docs/api/liquid/objects/sort_option) | The available sorting options for the search results. |
| terms | [string](https://shopify.dev/docs/api/liquid/basics#string) | The entered search terms. |
| types | array of [string](https://shopify.dev/docs/api/liquid/basics#string) | The object types that the search was performed on (article, page, product). |

#### Code Examples

##### Search result object_type

```liquid
{% for item in search.results %}
<!-- Result {{ forloop.index }}-->
<h3>
  {{ item.title | link_to: item.url }}
</h3>

{% if item.object_type == 'article' -%}
  {%- comment -%}
     'item' is an article
     All article object properties can be accessed.
  {%- endcomment -%}

  {% if item.image -%}
    <div class="result-image">
      <a href="{{ item.url }}" title="{{ item.title | escape }}">
        {{ item | image_url: width: 100 | image_tag }}
       </a>
    </div>
   {% endif %}
{%- elsif item.object_type == 'page' -%}
  {%- comment -%}
    'item' is a page.
     All page object properties can be accessed.
  {%- endcomment -%}
{%- else -%}
  {%- comment -%}
     'item' is a product.
     All product object properties can be accessed.
  {%- endcomment -%}

  {%- if item.featured_image -%}
    <div class="result-image">
       <a href="{{ item.url }}" title="{{ item.title | escape }}">
         {{ item.featured_image | image_url: width: 100 | image_tag }}
      </a>
    </div>
  {% endif %}
{%- endif -%}

<span>{{ item.content | strip_html | truncatewords: 40 | highlight: search.terms }}</span>
{% endfor %}
```

##### Output the sort options

```liquid
{%- assign sort_by = search.sort_by | default: search.default_sort_by -%}

<select>
{%- for option in search.sort_options %}
  <option
    value="{{ option.value }}"
    {%- if option.value == sort_by %}
      selected="selected"
    {%- endif %}
  >
    {{ option.name }}
  </option>
{% endfor -%}
</select>
```

#### Example JSON

```json
{
  "default_sort_by": "relevance",
  "filters": {},
  "performed": true,
  "results": [],
  "results_count": 17,
  "sort_by": "relevance",
  "sort_options": [],
  "terms": "potion",
  "types": [
    "article",
    "page",
    "product"
  ]
}
```

#### Templates using search

- [Theme architecture](https://shopify.dev/themes/architecture/templates/search)
- [search template](https://shopify.dev/themes/architecture/templates/search)

---

### section

> Fonte: https://shopify.dev/docs/api/liquid/objects/section

The properties and settings of a section.

> To learn about sections and using them in a theme, refer to Sections.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| blocks | array of [block](https://shopify.dev/docs/api/liquid/objects/block) | The blocks of the section. |
| id | [string](https://shopify.dev/docs/api/liquid/basics#string) | The ID of the section. The ID for sections included through JSON templates are dynamically generated by Shopify. The ID for static sections is the section file name without the `.liquid` extension. For example, a `header.liquid` section has an ID of `header`. |
| index | [number](https://shopify.dev/docs/api/liquid/basics#number) | The 1-based index of the current section within its location. Use this property to adjust section behavior based on its position within its location (template, section group) and on the page. The `index` starts at 1 within each location. An example use case is for programmatically setting `loading="lazy"` for images below the fold based on an index higher than, for example, 3. Note that this is now the default behavior for the `image_tag` filter. Only use this for non-display use cases like web performance. Because of various limitations, the `index` property returns `nil` in the following contexts: When rendered as a static section, While rendering in the online store editor, When using the Section Rendering API. |
| index0 | [number](https://shopify.dev/docs/api/liquid/basics#number) | The 0-based index of the current section within its location. This is the same as the `index` property except that the index starts at 0 instead of 1. |
| location | [string](https://shopify.dev/docs/api/liquid/basics#string) | The scope or context of the section (template, section group, or global). Sections can have one of four different location types. For sections rendered within a template, the location will be `template`. For sections rendered within a section group, the location will be the section group type, e.g., `header`, `footer`, `custom.<type>`. Sections rendered statically will be `static`. Finally, if you're still using `content_for_index`, then the value will be `content_for_index`. |
| settings | object | The settings of the section. To learn about how to access settings, refer to Access settings. |

#### Example

```json
{
  "blocks": [],
  "id": "template--14453298921537__cart-items",
  "settings": {}
}
```

---

### selling_plan

> Fonte: https://shopify.dev/docs/api/liquid/objects/selling_plan

Information about the intent of how a specific [selling plan](https://shopify.dev/apps/subscriptions/selling-plans) affects a line item.

To learn about how to support selling plans in your theme, refer to [Purchase options](https://shopify.dev/themes/pricing-payments/purchase-options).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| checkout_charge | [selling_plan_checkout_charge](https://shopify.dev/docs/api/liquid/objects/selling_plan_checkout_charge) | The checkout charge of the selling plan. |
| description | [string](https://shopify.dev/docs/api/liquid/basics#string) | The description of the selling plan. |
| group_id | [string](https://shopify.dev/docs/api/liquid/basics#string) | The ID of the [`selling_plan_group`](https://shopify.dev/docs/api/liquid/objects/selling_plan_group) that the selling plan belongs to. **Note:** The name is shown at checkout with the line item summary. |
| id | [number](https://shopify.dev/docs/api/liquid/basics#number) | The ID of the selling plan. |
| name | [string](https://shopify.dev/docs/api/liquid/basics#string) | The name of the selling plan. **Note:** The name is shown at checkout with the line item summary. |
| options | array of [selling_plan_option](https://shopify.dev/docs/api/liquid/objects/selling_plan_option) | The selling plan options. |
| price_adjustments | array of [selling_plan_price_adjustment](https://shopify.dev/docs/api/liquid/objects/selling_plan_price_adjustment) | The selling plan price adjustments. The maximum length of the array is two. If the selling plan doesn't create any price adjustments, then the array is empty. Each `selling_plan_price_adjustment` maps to a [`selling_plan_allocation_price_adjustment`](https://shopify.dev/docs/api/liquid/objects/selling_plan_allocation_price_adjustment) in the [`selling_plan_allocation.price_adjustments` array](https://shopify.dev/docs/api/liquid/objects/selling_plan_allocation#selling_plan_allocation-price_adjustments). The `selling_plan.price_adjustments` array contains the intent of the selling plan, and the `selling_plan_allocation.price_adjustments` contains the resulting money amounts. |
| recurring_deliveries | [boolean](https://shopify.dev/docs/api/liquid/basics#boolean) | Returns `true` if the selling plan includes multiple deliveries. Returns `false` if not. |
| selected | [boolean](https://shopify.dev/docs/api/liquid/basics#boolean) | Returns `true` if the selling plan is currently selected. Returns `false` if not. **Note:** The selected selling plan is determined by the `selling_plan` URL parameter. |

#### Example

```json
{
  "checkout_charge": {},
  "description": null,
  "group_id": "e88ff8fdb3c39c89b564859e34542e0b982076d6",
  "id": 2595487809,
  "name": "Deliver every week, 10% off",
  "options": [],
  "price_adjustments": [],
  "recurring_deliveries": true,
  "selected": true
}
```

---

### selling_plan_allocation

> Fonte: https://shopify.dev/docs/api/liquid/objects/selling_plan_allocation

Information about how a specific [selling plan](https://shopify.dev/apps/subscriptions/selling-plans) affects a line item.

To learn about how to support selling plans in your theme, refer to [Purchase options](https://shopify.dev/themes/pricing-payments/purchase-options).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| checkout_charge_amount | number | The amount that the customer will be charged at checkout in the currency's subunit. The value is output in the customer's local (presentment) currency. Use money filters to output a formatted price. |
| compare_at_price | number | The **compare at** price of the selling plan allocation in the currency's subunit. The value represents the line item's price without the selling plan applied. Output in customer's local (presentment) currency. For currencies without subunits (JPY, KRW), tenths and hundredths are appended. Use money filters for formatted price. |
| per_delivery_price | number | The price for each delivery in the selling plan in the currency's subunit. If a selling plan includes multiple deliveries, this equals the `price` divided by the number of deliveries. Output in customer's local (presentment) currency. For currencies without subunits (JPY, KRW), tenths and hundredths are appended. Use money filters for formatted price. |
| price | number | The price of the selling plan allocation in the currency's subunit. Output in customer's local (presentment) currency. Use money filters to output a formatted price. |
| price_adjustments | array of selling_plan_allocation_price_adjustment | The selling plan allocation price adjustments. Maximum array length is two. If the associated selling plan doesn't create price adjustments, the array is empty. Maps to `selling_plan.price_adjustments`. |
| remaining_balance_charge_amount | number | The remaining amount for the customer to pay, in the currency's subunit. Output in customer's local (presentment) currency. For currencies without subunits (JPY, KRW), tenths and hundredths are appended. Use money filters for formatted price. |
| selling_plan | selling_plan | The selling plan that created the allocation. |
| selling_plan_group_id | string | The ID of the `selling_plan_group` that the selling plan of the allocation belongs to. |
| unit_price | number | The unit price of the variant associated with the selling plan, in the currency's subunit. Returns `nil` if the variant doesn't have a unit price. Output in customer's local (presentment) currency. For currencies without subunits (JPY, KRW), tenths and hundredths are appended. Use money filters for formatted price. |

#### Returned by

* `line_item.selling_plan_allocation`
* `variant.selling_plan_allocations`
* `product.selected_selling_plan_allocation`
* `product.selected_or_first_available_selling_plan_allocation`
* `variant.selected_selling_plan_allocation`
* `remote_product.selected_selling_plan_allocation`
* `remote_product.selected_or_first_available_selling_plan_allocation`

---

### selling_plan_allocation_price_adjustment

> Fonte: https://shopify.dev/docs/api/liquid/objects/selling_plan_allocation_price_adjustment

The resulting price from the intent of the associated [`selling_plan_price_adjustment`](https://shopify.dev/docs/api/liquid/objects/selling_plan_price_adjustment).

To learn about supporting selling plans in your theme, refer to [Purchase options](https://shopify.dev/themes/pricing-payments/purchase-options).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| position | [number](https://shopify.dev/docs/api/liquid/basics#number) | The 1-based index of the price adjustment in the [`selling_plan_allocation.price_adjustments` array](https://shopify.dev/docs/api/liquid/objects/selling_plan_allocation#selling_plan_allocation-price_adjustments). |
| price | [number](https://shopify.dev/docs/api/liquid/basics#number) | The price that will be charged for the price adjustment's lifetime, in the currency's subunit. The value outputs in the customer's local (presentment) currency. For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen outputs as 100000. **Tip:** Use [money filters](https://shopify.dev/docs/api/liquid/filters/money-filters) to output a formatted price. |

#### Returned by

* [`selling_plan_allocation.price_adjustments`](https://shopify.dev/docs/api/liquid/objects/selling_plan_allocation#selling_plan_allocation-price_adjustments)

---

### selling_plan_checkout_charge

> Fonte: https://shopify.dev/docs/api/liquid/objects/selling_plan_checkout_charge

Information about how a specific [selling plan](https://shopify.dev/apps/subscriptions/selling-plans) affects the amount that a customer needs to pay for a line item at checkout.

To learn about how to support selling plans in your theme, refer to [Purchase options](https://shopify.dev/themes/pricing-payments/purchase-options).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| value | [number](https://shopify.dev/docs/api/liquid/basics#number) | The value of the checkout charge. How this value is interpreted depends on the [value type](https://shopify.dev/docs/api/liquid/objects/selling_plan_checkout_charge#selling_plan_checkout_charge-value_type) of the checkout charge. For `percentage` type, the value represents the percent amount of the original price (e.g., 50 = 50% of original price). For `price` type, the value represents the amount in the currency's subunit. For currencies without subunits like JPY and KRW, tenths and hundredths of a unit are appended (e.g., 1000 Japanese yen = 100000). Use [money filters](https://shopify.dev/docs/api/liquid/filters/money-filters) to output formatted prices. |
| value_type | [string](https://shopify.dev/docs/api/liquid/basics#string) | The value type of the checkout charge. Possible values: `percentage`, `price` |

#### Example

```json
{
  "value": 100,
  "value_type": "percentage"
}
```

---

### selling_plan_group

> Fonte: https://shopify.dev/docs/api/liquid/objects/selling_plan_group

Information about a specific group of [selling plans](https://shopify.dev/apps/subscriptions/selling-plans) that include any of a product's variants.

Selling plans are grouped based on shared [selling plan option names](https://shopify.dev/docs/api/liquid/objects/selling_plan_option#selling_plan_option-name).

To learn about how to support selling plans in your theme, refer to [Purchase options](https://shopify.dev/themes/pricing-payments/purchase-options).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| app_id | string | An optional string provided by an app to identify selling plan groups created by that app. If the app doesn't provide a value, then `nil` is returned. You can use this property, with the `where` filter, to filter the `product.selling_plan_groups` array for all selling plan groups from a specific app. |
| id | number | The ID of the selling plan group. |
| name | string | The name of the selling plan group. |
| options | array of `selling_plan_group_option` | The selling plan group options. |
| selling_plan_selected | boolean | Returns `true` if the currently selected selling plan is part of the selling plan group. Returns `false` if not. The selected selling plan is determined by the `selling_plan` URL parameter. |
| selling_plans | array of `selling_plan` | The selling plans in the group. |

#### Example

```json
{
  "app_id": "gid://shopify/App/66228322305",
  "id": "e88ff8fdb3c39c89b564859e34542e0b982076d6",
  "name": "1 Week(s), 4 Week(s)",
  "options": [],
  "selling_plan_selected": false,
  "selling_plans": []
}
```

---

### selling_plan_group_option

> Fonte: https://shopify.dev/docs/api/liquid/objects/selling_plan_group_option

Information about a specific option in a [selling plan group](https://shopify.dev/docs/api/liquid/objects/selling_plan_group).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| name | string | The name of the option. |
| position | number | The 1-based index of the option in the `selling_plan_group.options` array. |
| selected_value | string | The option value of the currently selected selling plan. If no selling plan is currently selected, then `nil` is returned. **Note:** The selected selling plan is determined by the `selling_plan` URL parameter. |
| values | array of string | The values of the option. |

#### Example

```json
{
  "name": "Delivery frequency",
  "position": 1,
  "selected_value": null,
  "values": [
    "Deliver every week",
    "Deliver every 4 weeks"
  ]
}
```

---

### selling_plan_option

> Fonte: https://shopify.dev/docs/api/liquid/objects/selling_plan_option

Information about a selling plan's value for a specific [`selling_plan_group_option`](https://shopify.dev/docs/api/liquid/objects/selling_plan_group_option).

To learn about how to support selling plans in your theme, refer to [Purchase options](https://shopify.dev/themes/pricing-payments/purchase-options).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| name | string | The name of the associated `selling_plan_group_option`. |
| position | number | The 1-based index of the selling plan option in the associated [`selling_plan_group.options` array](https://shopify.dev/docs/api/liquid/objects/selling_plan_group#selling_plan_group-options). |
| value | string | The value of the selling plan option. The value is one of the [`selling_plan_group_option.values`](https://shopify.dev/docs/api/liquid/objects/selling_plan_group_option#selling_plan_group_option-values). |

#### Example

```json
{
  "name": "Delivery frequency",
  "position": 1,
  "value": "Deliver every week"
}
```

---

### selling_plan_price_adjustment

> Fonte: https://shopify.dev/docs/api/liquid/objects/selling_plan_price_adjustment

Information about how a selling plan changes the price of a variant for a given period of time.

To learn about supporting selling plans in your theme, refer to [Purchase options](https://shopify.dev/themes/pricing-payments/purchase-options).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| order_count | number | The number of orders that the price adjustment applies to. |
| position | number | The 1-based index of the price adjustment in the `selling_plan.price_adjustments` array. |
| value | number | The value of the price adjustment as a decimal. Interpretation depends on the value type. For `fixed_amount`, represents the adjustment amount in currency's subunit. For `percentage`, represents the percent adjustment. For `price`, represents the adjusted amount in currency's subunit. For currencies without subunits (JPY, KRW), tenths and hundredths are appended (e.g., 1000 yen = 100000). Use money filters for formatted output. |
| value_type | string | The type of price adjustment. Possible values: `percentage`, `fixed_amount`, `price` |

#### Example

```json
{
  "order_count": null,
  "position": 1,
  "value": 10,
  "value_type": "percentage"
}
```

---

### settings

> Fonte: https://shopify.dev/docs/api/liquid/objects/settings

Allows you to access all of the theme's settings from the `settings_schema.json` file.

#### Directly accessible in

* Global

#### Reference a setting value

**Liquid example:**
```liquid
{% if settings.favicon != blank %}
  <link rel="icon" type="image/png" href="{{ settings.favicon | image_url: width: 32, height: 32 }}">
{% endif %}
```

**Data:**
```json
{
  "settings": {
    "favicon": null
  }
}
```

---

### shipping_method

> Fonte: https://shopify.dev/docs/api/liquid/objects/shipping_method

Information about the shipping method for an order.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| discount_allocations | array of [discount_allocation](https://shopify.dev/docs/api/liquid/objects/discount_allocation) | The discount allocations that apply to the shipping method. |
| handle | [string](https://shopify.dev/docs/api/liquid/basics#string) | The handle of the shipping method. Note: The price is appended to handle. |
| id | [string](https://shopify.dev/docs/api/liquid/basics#string) | The ID of the shipping method. |
| original_price | [number](https://shopify.dev/docs/api/liquid/basics#number) | Price in currency subunit before discounts, in customer's local currency. For currencies without subunits (JPY, KRW), tenths and hundredths are appended. Use money filters for formatted output. |
| price_with_discounts | [number](https://shopify.dev/docs/api/liquid/basics#number) | Price in currency subunit after discounts including order-level discounts, in customer's local currency. For currencies without subunits (JPY, KRW), tenths and hundredths are appended. Use money filters for formatted output. |
| tax_lines | array of [tax_line](https://shopify.dev/docs/api/liquid/objects/tax_line) | The tax lines for the shipping method. |
| title | [string](https://shopify.dev/docs/api/liquid/basics#string) | The shipping method title, usually in customer's preferred language. In order context, appears in checkout language. |

#### Deprecated Properties

| Property | Type | Description |
|----------|------|-------------|
| price | [number](https://shopify.dev/docs/api/liquid/basics#number) | Price in currency subunit after discounts, in customer's local currency. **Deprecated:** did not include order level discounts. Use `price_with_discounts` instead. |

#### Example

```json
{
  "handle": "shopify-Standard-0.00",
  "id": "shopify-Standard-0.00",
  "original_price": "0.00",
  "price": "0.00",
  "price_with_discounts": "0.00",
  "tax_lines": [],
  "title": "Standard"
}
```

---

### shop

> Fonte: https://shopify.dev/docs/api/liquid/objects/shop

Information about the store, such as the store address, the total number of products, and various settings.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| accepts_gift_cards | boolean | Returns `true` if the store accepts gift cards. Returns `false` if not. |
| address | address | The address of the store. |
| brand | brand | The brand assets for the store. |
| collections_count | number | The number of collections in the store. |
| currency | string | The currency of the store. |
| customer_accounts_enabled | boolean | Returns `true` if the store shows a login link. Returns `false` if not. |
| customer_accounts_optional | boolean | Returns `true` if customer accounts are optional to complete checkout. Returns `false` if not. |
| description | string | The description of the store. |
| domain | string | The primary domain of the store. |
| email | string | The sender email of the store. |
| enabled_currencies | array of currency | The currencies that the store accepts. |
| enabled_payment_types | array of string | The accepted payment types on the store. The payment types are based on the store's enabled payment providers and the customer's current region and currency. |
| id | string | The ID of the store. |
| metafields | metafield | The metafields applied to the store. |
| money_format | currency | The money format of the store. |
| money_with_currency_format | currency | The money format of the store with the currency included. |
| name | string | The name of the store. |
| password_message | string | The password page message of the store. |
| permanent_domain | string | The `.myshopify.com` domain of the store. |
| phone | string | The phone number of the store. |
| policies | array of policy | The policies for the store. |
| privacy_policy | policy | The privacy policy for the store. |
| products_count | number | The number of products in the store. |
| published_locales | array of shop_locale | The locales (languages) that are published on the store. |
| refund_policy | policy | The refund policy for the store. |
| search_types | array of string | The resource types searched for by default when no `type` parameter is specified. |
| secure_url | string | The full URL of the store, with an `https` protocol. |
| shipping_policy | policy | The shipping policy for the store. |
| subscription_policy | policy | The subscription policy for the store. |
| terms_of_service | policy | The terms of service for the store. |
| types | array of string | All of the product types in the store. |
| url | string | The full URL of the store. |
| vendors | array of string | All of the product vendors for the store. |

#### Deprecated Properties

| Property | Type | Status | Description |
|----------|------|--------|-------------|
| enabled_locales | array of shop_locale | Deprecated | The locales (languages) that are published on the store. Replaced by `shop.published_locales`. |
| locale | shop_locale | Deprecated | The currently active locale (language). Replaced by `request.locale`. |
| metaobjects | metaobject | Deprecated | All of the metaobjects of the store. Replaced by `metaobjects`. |
| taxes_included | boolean | Deprecated | Returns `true` if prices include taxes. Returns `false` if not. Replaced by `cart.taxes_included`. |

#### Policies Example

**Code:**
```liquid
<ul>
{%- for policy in shop.policies %}
  <li>{{ policy.title }}</li>
{%- endfor %}
</ul>
```

**Output:**
```html
<ul>
  <li>Refund policy</li>
  <li>Privacy policy</li>
  <li>Terms of service</li>
  <li>Shipping policy</li>
</ul>
```

#### Product Types Example

**Code:**
```liquid
{% for type in shop.types %}
  {{- type | link_to_type }}
{% endfor %}
```

**Output (excerpt):**
```html
Unknown Type

<a href="/collections/types?q=Animals%20%26%20Pet%20Supplies" title="Animals &amp; Pet Supplies">Animals & Pet Supplies</a>

<a href="/collections/types?q=Baking%20Flavors%20%26%20Extracts" title="Baking Flavors &amp; Extracts">Baking Flavors & Extracts</a>

<a href="/collections/types?q=Water" title="Water">Water</a>
```

#### Vendors Example

**Code:**
```liquid
{% for vendor in shop.vendors %}
  {{- vendor | link_to_vendor }}
{% endfor %}
```

**Output:**
```html
<a href="/collections/vendors?q=Clover%27s%20Apothecary" title="Clover&#39;s Apothecary">Clover's Apothecary</a>

<a href="/collections/vendors?q=Polina%27s%20Potent%20Potions" title="Polina&#39;s Potent Potions">Polina's Potent Potions</a>

<a href="/collections/vendors?q=Ted%27s%20Apothecary%20Supply" title="Ted&#39;s Apothecary Supply">Ted's Apothecary Supply</a>
```

#### Example

```json
{
  "accepts_gift_cards": true,
  "address": {},
  "brand": {},
  "collections_count": 7,
  "currency": "CAD",
  "customer_accounts_enabled": true,
  "customer_accounts_optional": true,
  "description": "Canada's foremost retailer for potions and potion accessories. Try one of our award-winning artisanal potions, or find the supplies to make your own!",
  "domain": "polinas-potent-potions.myshopify.com",
  "email": "polinas.potent.potions@gmail.com",
  "enabled_currencies": [],
  "enabled_locales": [],
  "enabled_payment_types": [
    "visa",
    "master",
    "american_express",
    "paypal",
    "diners_club",
    "discover"
  ],
  "id": 56174706753,
  "locale": "en",
  "metafields": {},
  "metaobjects": {},
  "money_format": "${{amount}}",
  "money_with_currency_format": "${{amount}} CAD",
  "name": "Polina's Potent Potions",
  "password_message": "Our store will be opening when the moon is in the seventh house!!",
  "permanent_domain": "polinas-potent-potions.myshopify.com",
  "phone": "416-123-1234",
  "policies": [],
  "privacy_policy": {},
  "products_count": 19,
  "published_locales": [],
  "refund_policy": {},
  "search_types": [
    "article",
    "page",
    "product"
  ],
  "secure_url": "https://polinas-potent-potions.myshopify.com",
  "shipping_policy": {},
  "subscription_policy": null,
  "taxes_included": false,
  "terms_of_service": {},
  "types": [
    "",
    "Animals & Pet Supplies",
    "Baking Flavors & Extracts",
    "Container",
    "Cooking & Baking Ingredients",
    "Dried Flowers",
    "Fruits & Vegetables",
    "Gift Cards",
    "Health",
    "Health & Beauty",
    "Invisibility",
    "Love",
    "Music & Sound Recordings",
    "Seasonings & Spices",
    "Water"
  ],
  "url": "https://polinas-potent-potions.myshopify.com",
  "vendors": [
    "Clover's Apothecary",
    "Polina's Potent Potions",
    "Ted's Apothecary Supply"
  ]
}
```

---

### shop_locale

> Fonte: https://shopify.dev/docs/api/liquid/objects/shop_locale

A language in a store.

To learn how to offer localization options in your theme, refer to [Support multiple currencies and languages](https://shopify.dev/themes/internationalization/multiple-currencies-languages).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| endonym_name | string | The name of the locale in the locale itself. |
| iso_code | string | The ISO code of the locale in [IETF language tag format](https://en.wikipedia.org/wiki/IETF_language_tag). |
| name | string | The name of the locale in the store's primary locale. |
| primary | boolean | Returns `true` if the locale is the store's primary locale. Returns `false` if not. |
| root_url | string | The relative root URL of the locale. |

#### Example

```json
{
  "endonym_name": "English",
  "iso_code": "en",
  "name": "English",
  "primary": true,
  "root_url": "/"
}
```

---

### sitemap

> Fonte: https://shopify.dev/docs/api/liquid/objects/sitemap

The sitemap for a specific group in the [`robots.txt` file](/themes/architecture/templates/robots-txt-liquid).

The sitemap provides information about the pages and content on a site, and the relationships between them, which helps crawlers crawl a site more efficiently.

> To learn more about sitemaps, refer to [Google's documentation](https://developers.google.com/search/docs/advanced/sitemaps/overview).

The `sitemap` object consists of a `Sitemap` directive, and a value of the URL that the sitemap is hosted at. For example:

```
Sitemap: https://your-store.myshopify.com/sitemap.xml
```

> You can [customize the `robots.txt` file](/themes/seo/robots-txt) with the [`robots.txt.liquid` template](/themes/architecture/templates/robots-txt-liquid).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| directive | [string](https://shopify.dev/docs/api/liquid/basics#string) | Returns `Sitemap`. |
| value | [string](https://shopify.dev/docs/api/liquid/basics#string) | The URL that the sitemap is hosted at. |

#### Example

```json
{
  "directive": "Sitemap",
  "value": "https://polinas-potent-potions.myshopify.com/sitemap.xml"
}
```

---

### sort_option

> Fonte: https://shopify.dev/docs/api/liquid/objects/sort_option

A sort option for a collection or search results page.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| name | string | The customer-facing name of the sort option. The name can be edited by merchants in the language editor. |
| value | string | The value of the sort option. This value is used when assigning the `collection.sort_by` and `search.sort_by` parameters. |

#### Example

```json
{
  "name": "Alphabetically, A-Z",
  "value": "title-ascending"
}
```

---

### store_availability

> Fonte: https://shopify.dev/docs/api/liquid/objects/store_availability

A variant's inventory information for a physical store location.

If a location doesn't stock a variant, then there won't be a `store_availability` for that variant and location.

> **Note:** The `store_availability` object is defined only if one or more locations has [local pickup](https://help.shopify.com/manual/shipping/setting-up-and-managing-your-shipping/local-methods/local-pickup) enabled.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| available | boolean | Returns `true` if the variant has available inventory at the location. Returns `false` if not. |
| location | location | The location that the variant is stocked at. |
| pick_up_enabled | boolean | Returns `true` if the location has pickup enabled. Returns `false` if not. |
| pick_up_time | string | The amount of time that it takes for pickup orders to be ready at the location. This value can be configured in the Shopify admin. |

#### Example

```json
{
  "available": true,
  "location": {},
  "pick_up_enabled": true,
  "pick_up_time": "Usually ready in 24 hours"
}
```

---

### store_credit_account

> Fonte: https://shopify.dev/docs/api/liquid/objects/store_credit_account

A [store credit account](https://help.shopify.com/en/manual/customers/store-credit) that belongs to a [customer](https://shopify.dev/docs/api/liquid/objects/customer).

#### Properties

| Name | Type | Description |
|------|------|-------------|
| balance | [money](https://shopify.dev/docs/api/liquid/objects/money) | The store credit account's balance in the currency's subunit. The value displays in the customer's local (presentment) currency. For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen displays as 100000. Use [money filters](https://shopify.dev/docs/api/liquid/filters/money-filters) to output a formatted amount. |

#### Example

```json
{
  "balance": {}
}
```

---

### swatch

> Fonte: https://shopify.dev/docs/api/liquid/objects/swatch

Color and image for visual representation. Available for [product option values](https://shopify.dev/docs/api/liquid/objects/product_option_value) and [filter values](https://shopify.dev/docs/api/liquid/objects/filter_value).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| color | [color](https://shopify.dev/docs/api/liquid/objects/color) | The swatch color. |
| image | [image](https://shopify.dev/docs/api/liquid/objects/image) | The swatch image. |

#### Example

```json
{
  "color": {},
  "image": {}
}
```

---

### tablerowloop

> Fonte: https://shopify.dev/docs/api/liquid/objects/tablerowloop

Information about a parent [`tablerow` loop](https://shopify.dev/docs/api/liquid/tags/tablerow).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| col | number | The 1-based index of the current column. |
| col_first | boolean | Returns `true` if the current column is the first in the row. Returns `false` if not. |
| col_last | boolean | Returns `true` if the current column is the last in the row. Returns `false` if not. |
| col0 | number | The 0-based index of the current column. |
| first | boolean | Returns `true` if the current iteration is the first. Returns `false` if not. |
| index | number | The 1-based index of the current iteration. |
| index0 | number | The 0-based index of the current iteration. |
| last | boolean | Returns `true` if the current iteration is the last. Returns `false` if not. |
| length | number | The total number of iterations in the loop. |
| rindex | number | The 1-based index of the current iteration, in reverse order. |
| rindex0 | number | The 0-based index of the current iteration, in reverse order. |
| row | number | The 1-based index of current row. |

#### Example

```json
{
  "col": 1,
  "col0": 0,
  "col_first": true,
  "col_last": false,
  "first": true,
  "index": 1,
  "index0": 0,
  "last": false,
  "length": 5,
  "rindex": 5,
  "rindex0": 4,
  "row": 1
}
```

---

### tax_line

> Fonte: https://shopify.dev/docs/api/liquid/objects/tax_line

Information about a tax line of a checkout or order.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| price | number | The tax amount in the currency's subunit. The value is output in the customer's local (presentment) currency. For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000. **Tip:** Use money filters to output a formatted price. |
| rate | number | The decimal value of the tax rate. |
| rate_percentage | number | The decimal value of the tax rate, as a percentage. |
| title | string | The title of the tax. |

#### Example

```json
{
  "price": 1901,
  "rate": 0.05,
  "rate_percentage": 5,
  "title": "GST"
}
```

---

### taxonomy_category

> Fonte: https://shopify.dev/docs/api/liquid/objects/taxonomy_category

The taxonomy category for a product

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| ancestors | array of [taxonomy_category](https://shopify.dev/docs/api/liquid/objects/taxonomy_category) | All parent nodes of the current taxonomy category. |
| gid | [string](https://shopify.dev/docs/api/liquid/basics#string) | The public node ID for the category, formatted as a Shopify GID. |
| id | [string](https://shopify.dev/docs/api/liquid/basics#string) | The public node ID for the category |
| name | [string](https://shopify.dev/docs/api/liquid/basics#string) | The localized category name |

#### Example

```json
{
  "ancestors": [],
  "gid": "gid://shopify/TaxonomyCategory/hb-1-9-6",
  "id": "hb-1-9-6",
  "name": "Vitamins & Supplements"
}
```

---

### template

> Fonte: https://shopify.dev/docs/api/liquid/objects/template

Information about the current [template](https://shopify.dev/docs/themes/architecture/templates).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| directory | [string](https://shopify.dev/docs/api/liquid/basics#string) | The name of the template's parent directory. Returns `nil` if the template's parent directory is `/templates`. |
| name | [string](https://shopify.dev/docs/api/liquid/basics#string) | The name of the template's [type](https://shopify.dev/docs/themes/architecture/templates#template-types). Possible values: 404, article, blog, cart, collection, list-collections, customers/account, customers/activate_account, customers/addresses, customers/login, customers/order, customers/register, customers/reset_password, gift_card, index, page, password, product, search |
| suffix | [string](https://shopify.dev/docs/api/liquid/basics#string) | The custom name of an [alternate template](https://shopify.dev/themes/architecture/templates#alternate-templates). Returns `nil` if the default template is being used. |

#### Example

```json
{
  "directory": null,
  "name": "product",
  "suffix": null
}
```

---

### theme

> Fonte: https://shopify.dev/docs/api/liquid/objects/theme

Information about the current theme.

> **Deprecated:** The values of this object's properties are subject to change and cannot be reliably used within themes. To link to the theme editor for the published theme, use the URL path `/admin/themes/current/editor`. While deprecated in Liquid, this object remains accessible through the [REST Admin API](https://shopify.dev/api/admin-rest/current/resources/theme).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| id | number | The ID of the theme. |
| name | string | The name of the theme. |
| role | string | The role of the theme. Possible values: `main` (published theme visible to customers), `unpublished` (not visible to customers), `demo` (installed as demo; requires purchase to publish), `development` (used for development; temporary and cannot be published). |

#### Example

```json
{
  "id": 124051750977,
  "name": "Dawn",
  "role": "main"
}
```

---

### transaction

> Fonte: https://shopify.dev/docs/api/liquid/objects/transaction

A transaction associated with a checkout or order.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| amount | number | The amount of the transaction in the currency's subunit. The amount is in the customer's local (presentment) currency. For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000. **Tip:** Use money filters to output a formatted amount. |
| buyer_pending_payment_instructions | array of pending_payment_instruction_input | A list of `pending_payment_instruction_input` header-value pairs, with payment method-specific details. The customer can use these details to complete their purchase offline. If the payment method doesn't support pending payment instructions, then an empty array is returned. |
| buyer_pending_payment_notice | string | A notice that contains instructions for the customer on how to complete their payment. The messages are specific to the payment method used. |
| created_at | string | A timestamp of when the transaction was created. **Tip:** Use the `date` filter to format the timestamp. |
| gateway | string | The handleized name of the payment provider used for the transaction. |
| gateway_display_name | string | The name of the payment provider used for the transaction. |
| id | number | The ID of the transaction. |
| kind | string | The type of transaction. Possible values: `authorization`, `capture`, `sale`, `void`, `refund` |
| name | string | The name of the transaction. |
| payment_details | transaction_payment_details | The transaction payment details. |
| receipt | string | Information from the payment provider about the payment receipt. This includes things like whether the payment was a test, or an authorization code if there was one. |
| show_buyer_pending_payment_instructions? | boolean | Whether the transaction is pending, and whether additional customer info is required to process the payment. |
| status | string | The status of the transaction. Possible values: `success`, `pending`, `failure`, `error` |
| status_label | string | The status of the transaction, translated based on the current locale. |

#### Example

```json
{
  "amount": "380.25",
  "created_at": "2022-06-15 19:13:14 -0400",
  "gateway": "shopify_payments",
  "gateway_display_name": "Shopify payments",
  "id": 5432242176065,
  "kind": "sale",
  "name": "c29944051400769.",
  "payment_details": {
    "credit_card_number": "•••• •••• •••• 4242",
    "credit_card_company": "Visa",
    "credit_card_last_four_digits": "4242",
    "receiver_info": null
  },
  "receipt": "...",
  "show_buyer_pending_payment_instructions?": null,
  "status": "success",
  "status_label": "Success"
}
```

> Nota di estrazione: il campo `receipt` nell'esempio originale contiene un dump YAML molto lungo del payment intent del provider; qui è abbreviato con `...`. Tutte le proprietà e gli altri valori dell'esempio sono riportati integralmente. Fonte completa: https://shopify.dev/docs/api/liquid/objects/transaction

---

### transaction_payment_details

> Fonte: https://shopify.dev/docs/api/liquid/objects/transaction_payment_details

Information about the payment methods used for a transaction.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| credit_card_company | [string](https://shopify.dev/docs/api/liquid/basics#string) | The name of the company that issued the credit card used for the transaction. |
| credit_card_last_four_digits | [string](https://shopify.dev/docs/api/liquid/basics#string) | The last four digits of the credit card number of the credit card used for the transaction. |
| credit_card_number | [string](https://shopify.dev/docs/api/liquid/basics#string) | The credit card number of the credit card used for the transaction. All but the last four digits are redacted. |
| gift_card | [gift_card](https://shopify.dev/docs/api/liquid/objects/gift_card) | The gift card used for the transaction. If no gift card was used, then `nil` is returned. |

#### Example

```json
{
  "credit_card_number": "•••• •••• •••• 4242",
  "credit_card_company": "Visa",
  "credit_card_last_four_digits": "4242"
}
```

---

### unit_price_measurement

> Fonte: https://shopify.dev/docs/api/liquid/objects/unit_price_measurement

Information about how units of a product variant are measured. It's used to calculate [unit prices](https://help.shopify.com/manual/products/details/product-pricing/unit-pricing#add-unit-prices-to-your-product).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| measured_type | string | The type of unit measurement. Possible values: volume, weight, length, area, count |
| quantity_unit | string | The unit of measurement used to measure the quantity_value. |
| quantity_value | number | The quantity of the unit. |
| reference_unit | string | The unit of measurement used to measure the reference_value. |
| reference_value | number | The quantity of the unit for the base unit price. |

#### Example

```json
{
  "measured_type": "weight",
  "quantity_value": "500.0",
  "quantity_unit": "g",
  "reference_value": 1,
  "reference_unit": "kg"
}
```

---

### user

> Fonte: https://shopify.dev/docs/api/liquid/objects/user

The author of a blog article.

> The information returned by the `user` object can be edited on the **Account page** of the Shopify admin.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| account_owner | boolean | Returns `true` if the author is the account owner of the store. Returns `false` if not. |
| bio | string | The bio associated with the author's account. If no bio is specified, then `nil` is returned. |
| email | string | The email associated with the author's account. |
| first_name | string | The first name associated with the author's account. |
| homepage | string | The URL for the personal website associated with the author's account. If no personal website is specified, then `nil` is returned. |
| image | image | The image associated with the author's account. If no image is specified, then `nil` is returned. |
| last_name | string | The last name associated with the author's account. |
| name | string | The first and last name associated with the author's account. |

#### Example

```json
{
  "account_owner": false,
  "bio": "Polina got her first cauldron at the tender age of six, and she has been passionate about potions ever since!!",
  "email": "polinas.potent.potions@gmail.com",
  "first_name": "Polina",
  "homepage": null,
  "image": {},
  "last_name": "Waters",
  "name": "Polina Waters"
}
```

---

### user_agent

> Fonte: https://shopify.dev/docs/api/liquid/objects/user_agent

The user-agent, which is the name of the crawler, for a specific group in the `robots.txt` file.

The `user_agent` object consists of a `User-agent` directive, and a value of the name of the user-agent. For example:

```
User-agent: *
```

> **Tip:** You can customize the `robots.txt` file with the `robots.txt.liquid` template.

#### Properties

| Name | Type | Description |
|------|------|-------------|
| directive | string | Returns `User-agent`. |
| value | string | The name of the user-agent. |

#### Example

```json
{
  "directive": "User-agent",
  "value": "*"
}
```

---

### variant

> Fonte: https://shopify.dev/docs/api/liquid/objects/variant

A [product variant](https://help.shopify.com/manual/products/variants).

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| available | boolean | Returns `true` if the variant is available. Returns `false` if not. |
| barcode | string | The barcode of the variant. |
| compare_at_price | number | The **compare at** price of the variant in the currency's subunit. The value is output in the customer's local (presentment) currency. For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000. **Tip:** Use money filters to output a formatted price. |
| featured_image | image | The image attached to the variant. **Note:** This is the same value as `variant.image`. |
| featured_media | media | The first media object attached to the variant. |
| id | number | The ID of the variant. |
| image | image | The image attached to the variant. **Note:** This is the same value as `variant.featured_image`. |
| incoming | boolean | Returns `true` if the variant has incoming inventory. Returns `false` if not. Incoming inventory information is populated by inventory transfers, purchase orders, and third-party apps. |
| inventory_management | string | The inventory management service of the variant. If inventory isn't tracked, then `nil` is returned. |
| inventory_policy | string | Whether the variant should continue to be sold when it's out of stock. Possible values: `continue` (Continue selling when the variant is out of stock) or `deny` (Stop selling when the variant is out of stock). |
| inventory_quantity | number | The inventory quantity of the variant. If inventory isn't tracked, then the number of items sold is returned. |
| matched | boolean | Returns `true` if the variant has been matched by a storefront filter or no filters are applied. Returns `false` if it hasn't. |
| metafields | metafield | The metafields applied to the variant. **Tip:** To learn about how to create metafields, refer to Create and manage metafields or visit the Shopify Help Center. |
| next_incoming_date | string | The arrival date for the next incoming inventory of the variant. Incoming inventory information is populated by inventory transfers, purchase orders, and third-party apps. **Tip:** Use the `date` filter to format the date. |
| options | product_option_value | The values of the variant for each product option. |
| price | number | The price of the variant in the currency's subunit. The value is output in the customer's local (presentment) currency. For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000. **Tip:** Use money filters to output a formatted price. |
| product | product | The parent product of the variant. |
| quantity_price_breaks | array of quantity_price_break | Returns `quantity_price_break` objects for the variant in the current customer context. |
| quantity_price_breaks_configured? | boolean | Returns `true` if the variant has any quantity price breaks available in the current customer context. Returns `false` if it doesn't. |
| quantity_rule | quantity_rule | The quantity rule for the variant. If no rule exists, then a default value is returned. This rule can be set as part of a B2B catalog. **Note:** The default quantity rule is `min=1,max=null,increment=1`. |
| requires_selling_plan | boolean | Returns `true` if the variant's product is set to require a `selling_plan` when being added to the cart. Returns `false` if not. |
| requires_shipping | boolean | Returns `true` if the variant requires shipping. Returns `false` if it doesn't. |
| selected | boolean | Returns `true` if the variant is currently selected. Returns `false` if it's not. **Note:** The selected variant is determined by the `variant` URL parameter. This URL parameter is available on product pages URLs only. |
| selected_selling_plan_allocation | selling_plan_allocation | The selected `selling_plan_allocation`. If no selling plan is selected, then `nil` is returned. **Note:** The selected selling plan is determined by the `selling_plan` URL parameter. |
| selling_plan_allocations | array of selling_plan_allocation | The `selling_plan_allocation` objects for the variant. |
| sku | string | The SKU of the variant. |
| store_availabilities | array of store_availability | The store availabilities for the variant. The array is defined in only the following cases: `variant.selected` is `true` or the variant is the product's first available variant. |
| taxable | boolean | Returns `true` if taxes should be charged on the variant. Returns `false` if not. |
| title | string | A concatenation of each variant option, separated by a `/`. |
| unit_price | number | The unit price of the variant in the currency's subunit. The price reflects any discounts that are applied to the line item. The value is output in the customer's local (presentment) currency. For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000. **Tip:** Use the `unit_price_with_measurement` filter with this property and the `variant.unit_price_measurement` property to output a formatted unit price with measurement. |
| unit_price_measurement | unit_price_measurement | The unit price measurement of the variant. To learn about how to display unit prices in your theme, refer to Unit pricing. **Tip:** Use the `unit_price_with_measurement` filter with the `variant.unit_price` property and this property to output a formatted unit price with measurement. |
| url | string | The URL of the variant. Variant URLs use the structure: `/products/[product-handle]?variant=[variant-id]` |
| weight | number | The weight of the variant in grams. **Tip:** Use the `weight_with_unit` filter to format the weight in the store's format. Use `variant.weight_in_unit` to output the weight in the unit configured on the variant. |
| weight_in_unit | number | The weight of the variant in the unit specified by `variant.weight_unit`. **Tip:** To output this weight, use this property and the `variant.weight_unit` property with the `weight_with_unit` filter. |
| weight_unit | string | The unit for the weight of the variant. **Tip:** To output the weight of a variant in this unit, use this property and the `variant.weight_in_unit` property with the `weight_with_unit` filter. |

#### Deprecated Properties

| Property | Type | Description |
|----------|------|-------------|
| option1 | string | The value of the variant for the first product option. If there's no first product option, then `nil` is returned. **Deprecated:** Prefer to use `variant.options` instead. |
| option2 | string | The value of the variant for the second product option. If there's no second product option, then `nil` is returned. **Deprecated:** Prefer to use `variant.options` instead. |
| option3 | string | The value of the variant for the third product option. If there's no third product option, then `nil` is returned. **Deprecated:** Prefer to use `variant.options` instead. |

#### Example: The variant options

**Code:**
```liquid
{% for variant in product.variants -%}
  {%- capture options -%}
    {% for option in variant.options -%}
      {{ option }}{%- unless forloop.last -%}/{%- endunless -%}
    {%- endfor %}
  {%- endcapture -%}
  
  {{ variant.id }}: {{ options }}
{%- endfor %}
```

**Data:**
```json
{
  "product": {
    "variants": [
      { "id": 39897499729985, "options": ["S", "Low"] },
      { "id": 39897499762753, "options": ["S", "Medium"] },
      { "id": 39897499795521, "options": ["S", "High"] },
      { "id": 39897499828289, "options": ["M", "Low"] },
      { "id": 39897499861057, "options": ["M", "Medium"] },
      { "id": 39897499893825, "options": ["M", "High"] },
      { "id": 39897499926593, "options": ["L", "Low"] },
      { "id": 39897499959361, "options": ["L", "Medium"] },
      { "id": 39897499992129, "options": ["L", "High"] }
    ]
  }
}
```

**Output:**
```html
39897499729985: S/Low

39897499762753: S/Medium

39897499795521: S/High

39897499828289: M/Low

39897499861057: M/Medium

39897499893825: M/High

39897499926593: L/Low

39897499959361: L/Medium

39897499992129: L/High
```

#### Example: The variant title

**Code:**
```liquid
{{ product.variants.first.title }}
```

**Data:**
```json
{
  "product": {
    "variants": [
      { "title": "S / Low" },
      { "title": "S / Medium" },
      { "title": "S / High" },
      { "title": "M / Low" },
      { "title": "M / Medium" },
      { "title": "M / High" },
      { "title": "L / Low" },
      { "title": "L / Medium" },
      { "title": "L / High" }
    ]
  }
}
```

**Output:**
```html
S / Low
```

#### Complete Example JSON

```json
{
  "available": true,
  "barcode": "",
  "compare_at_price": null,
  "featured_image": null,
  "featured_media": null,
  "id": 39897499729985,
  "image": null,
  "incoming": false,
  "inventory_management": "shopify",
  "inventory_policy": "deny",
  "inventory_quantity": 5,
  "matched": true,
  "metafields": {},
  "next_incoming_date": null,
  "option1": "S",
  "option2": "Low",
  "option3": null,
  "options": [],
  "price": "10.00",
  "product": {},
  "quantity_price_breaks": [],
  "quantity_rule": {},
  "requires_selling_plan": false,
  "requires_shipping": true,
  "selected": false,
  "selected_selling_plan_allocation": null,
  "selling_plan_allocations": [],
  "sku": "",
  "store_availabilities": [],
  "taxable": true,
  "title": "S / Low",
  "unit_price": null,
  "unit_price_measurement": null,
  "url": {},
  "weight": 500,
  "weight_in_unit": 500,
  "weight_unit": "g"
}
```

---

### video

> Fonte: https://shopify.dev/docs/api/liquid/objects/video

Information about a video uploaded as [product media](/docs/api/liquid/objects/product-media) or a [`file_reference` metafield](/apps/metafields/types).

> **Tip:** Use the `video_tag` filter to output the video in an HTML `<video>` tag.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| alt | string | The alt text of the video. |
| aspect_ratio | number | The aspect ratio of the video as a decimal. |
| duration | number | The duration of the video in milliseconds. |
| id | number | The ID of the video. |
| media_type | string | The media type of the model. Always returns `video`. |
| position | number | The position of the video in the `product.media` array. |
| preview_image | image | A preview image for the video. |
| sources | array of video_source | The source files for the video. |

#### Example: Filter for media of a specific type

You can use the `media_type` property with the `where` filter to filter the `product.media` array for all media of a desired type.

**Code:**
```liquid
{% assign videos = product.media | where: 'media_type', 'video' %}

{% for video in videos %}
  {{- video | video_tag }}
{% endfor %}
```

**Data:**
```json
{
  "product": {
    "media": [
      {
        "media_type": "external_video"
      },
      {
        "media_type": "video"
      }
    ]
  }
}
```

**Output:**
```html
<video playsinline="playsinline" preload="metadata" aria-label="Potion beats" poster="//polinas-potent-potions.myshopify.com/cdn/shop/products/4edc28a708b7405093a927cebe794f1a.thumbnail.0000000_small.jpg?v=1655255324"><source src="//polinas-potent-potions.myshopify.com/cdn/shop/videos/c/vp/4edc28a708b7405093a927cebe794f1a/4edc28a708b7405093a927cebe794f1a.HD-1080p-7.2Mbps.mp4?v=0" type="video/mp4"><img src="//polinas-potent-potions.myshopify.com/cdn/shop/products/4edc28a708b7405093a927cebe794f1a.thumbnail.0000000_small.jpg?v=1655255324"></video>
```

#### Example object

```json
{
  "alt": "Potion beats",
  "aspect_ratio": 1.779,
  "duration": 34801,
  "id": 22070396551233,
  "media_type": "video",
  "position": 2,
  "preview_image": {},
  "sources": []
}
```

---

### video_source

> Fonte: https://shopify.dev/docs/api/liquid/objects/video_source

Information about the source files for a video.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| format | [string](https://shopify.dev/docs/api/liquid/basics#string) | The format of the video source file. Possible values: `mov`, `mp4`, `m3u8`. **Note:** When mp4 videos are uploaded, Shopify generates an m3u8 file as an additional video source. |
| height | [number](https://shopify.dev/docs/api/liquid/basics#number) | The height of the video source file. |
| mime_type | [string](https://shopify.dev/docs/api/liquid/basics#string) | The [MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types) of the video source file. |
| url | [string](https://shopify.dev/docs/api/liquid/basics#string) | The [CDN URL](https://shopify.dev/themes/best-practices/performance/platform#shopify-cdn) of the video source file. |
| width | [number](https://shopify.dev/docs/api/liquid/basics#number) | The width of the video source file. |

#### Example

```json
{
  "format": "mp4",
  "height": 1080,
  "mime_type": "video/mp4",
  "url": "//polinas-potent-potions.myshopify.com/cdn/shop/videos/c/vp/4edc28a708b7405093a927cebe794f1a/4edc28a708b7405093a927cebe794f1a.HD-1080p-7.2Mbps.mp4?v=0",
  "width": 1920
}
```

---

## Pagine non catturate

| Pagina / URL | Motivo |
|--------------|--------|
| `https://shopify.dev/docs/api/liquid/objects/payment` | HTTP 404 Not Found. `payment` non è una pagina oggetto valida nella reference Liquid (non esiste un oggetto `payment` standalone). Tutti gli oggetti realmente documentati sono stati catturati. |

Nessun altro oggetto è stato saltato. Le uniche abbreviazioni applicate riguardano blocchi di dati estremamente lunghi (segnalate inline con nota di estrazione e URL della fonte): l'elenco completo degli stati USA in `country_option_tags`, il dump YAML del campo `receipt` in `transaction`. In entrambi i casi la tabella completa delle proprietà e gli esempi primari sono riportati integralmente.
