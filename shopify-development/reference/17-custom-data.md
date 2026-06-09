# 17. Custom Data (Metafields & Metaobjects)

Shopify ships with built-in data models — products, customers, orders, collections, and more — but real businesses always need to store information that doesn't fit those native shapes. **Custom data** is Shopify's answer: two complementary primitives, **metafields** and **metaobjects**, that let you extend the platform's data model without leaving it.

- **Metafields** add individual custom fields (think: new *columns*) to existing Shopify resources, like a "Warranty" field on a product or a "Lifetime value" field on a customer.
- **Metaobjects** define entirely new structured entities (think: new *tables*) with multiple related fields, such as an "Author" profile, a "Size chart", or a reusable "Product highlight" — entries that can be referenced and reused across the store.

Both share the same set of **data types**, the same **validation** system, the same **ownership** model (app-owned vs merchant-owned), and the same **access controls** (Admin API, Storefront API, Customer Account API, and Liquid). This chapter captures the conceptual overview, the complete type and validation references, the how-to guides for creating and managing definitions and values via TOML / GraphQL Admin API / Storefront API, querying, capabilities, limits, and how to read and display custom data in themes through Liquid.

## Indice del capitolo

**Overview**
- [About metafields (Custom data overview)](#about-metafields-custom-data-overview)
- [Data modeling with metafields and metaobjects](#data-modeling-with-metafields-and-metaobjects)

**Metafields**
- [List of data types (metafield TYPES reference)](#list-of-data-types-metafield-types-reference)
- [List of validation options](#list-of-validation-options)
- [Manage metafield definitions](#manage-metafield-definitions)
- [Manage values (metafield values)](#manage-values-metafield-values)
- [List of standard metafield definitions](#list-of-standard-metafield-definitions)
- [Use metafield capabilities](#use-metafield-capabilities)
- [Query using metafields](#query-using-metafields)
- [Conditional metafield definitions](#conditional-metafield-definitions)
- [Working with custom IDs](#working-with-custom-ids)
- [Metafield limits](#metafield-limits)

**Metaobjects**
- [About metaobjects](#about-metaobjects)
- [Manage metaobject definitions](#manage-metaobject-definitions)
- [Manage entries (metaobject entries)](#manage-entries-metaobject-entries)
- [Query metaobjects](#query-metaobjects)
- [Use metaobject capabilities](#use-metaobject-capabilities)
- [Standard metaobject definitions](#standard-metaobject-definitions)
- [Metaobject limits](#metaobject-limits)

**Reading & displaying in themes (Liquid)**
- [Liquid object: `metafield`](#liquid-object-metafield)
- [Liquid object: `metaobject`](#liquid-object-metaobject)

---

# Overview

---

## About metafields (Custom data overview)

> Fonte: https://shopify.dev/docs/apps/build/custom-data

Shopify includes built-in data models like products, customers, and orders. Metafields extend these models by letting you add custom data to any [Shopify resource](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).

You can use metafields to add warranty information to products, track customer lifetime value, store fulfillment notes on orders, link related products, trigger Shopify Flow automations, or power backend processes. This flexibility lets you extend Shopify's data model for specialized features and business logic.

**Info:**

Metafields add individual custom fields to specific Shopify resources.

* Need to create standalone objects with multiple related fields? Use [metaobjects](https://shopify.dev/docs/apps/build/metaobjects) instead.
* For a deep dive on how to structure your data using both tools, see [Data modeling with metafields and metaobjects](https://shopify.dev/docs/apps/build/metaobjects/data-modeling-with-metafields-and-metaobjects).

Want to skip ahead? Choose a path based on what you're building:

* **Building an app**: Use [app-owned metafields](#app-owned-metafields) with TOML configuration.
* **Extending existing store data**: Use [merchant-owned metafields](#merchant-owned-metafields) with GraphQL.

### What are metafields?

Metafields are key-value pairs with the following components:

* **Identifier**: A combination of namespace and key (for example, `custom.warranty_info`). Namespaces are logical containers that not only provide organization and prevent naming conflicts, they establish [ownership](#metafield-ownership).
* **Value**: The data being stored.
* **Type**: Defines the kind of value (such as text, number, date, or reference) and how the value is interpreted. [See available types](https://shopify.dev/docs/apps/build/metafields/list-of-data-types).

#### Metafield definitions

Before creating a metafield, you will create a metafield definition. Metafield definitions establish data schemas that enable type validation, Shopify admin integration, query filtering, access control, and performance optimization.

**Note:**

Shopify provides pre-built "standard" definitions for common use cases like ISBN numbers, product ingredients, and care instructions. Using standard definitions helps ensure interoperability across the Shopify ecosystem and saves you from defining schemas for well-known data types. Explore [standard metafield definitions](https://shopify.dev/docs/apps/build/metafields/list-of-standard-definitions).

#### Metafield ownership

Ownership determines access and control. When creating metafields, you choose between two ownership models:

| **Ownership Type** | **Purpose** | **Namespace** |
| --- | --- | --- |
| App-owned | App-managed data for internal logic, configuration, and workflows | Use reserved namespace `$app` (GraphQL) or `app` (TOML) |
| Merchant-owned | Merchant-managed data shared across all apps | Use any non-reserved namespace, such as `custom` |

**Additional ownership types:**

* **Shopify-reserved**: Metafields with Shopify-controlled namespaces and structures, including those typically prefixed with reserved namespace `shopify--` and [standard definitions](https://shopify.dev/docs/apps/build/metafields/list-of-standard-definitions). Shopify controls the structure, but the metafields are typically [merchant-owned](#merchant-owned-metafields).
* **App-data**: A special type of app-owned metafield tied to your app installation (not to products, customers, or orders) and completely hidden from the Shopify admin. See [App-data metafields](#app-data-metafields) for details.

### App-owned metafields

App-owned metafields are custom data entries controlled by your app. Your app manages both the structure and values, which are view only in the Shopify admin (by default).

App-ownership is defined using the `app` reserved namespace.

**Info:**

App-owned data is viewable by default in the Shopify admin. If you need to store data that is not visible, consider [App-data metafields](#app-data-metafields).

#### Example

You want to track internal SKU codes for products. Because your app manages inventory tracking, you create an app-owned metafield.

##### Step 1: Create the metafield definition

Create the metafield definition using your app's `shopify.app.toml` file. The following creates the definition with app-owned namespace `app` and key `internal_sku`:

```toml
[product.metafields.app.internal_sku]
name = "Internal SKU"
description = "Internal inventory tracking code"
type = "single_line_text_field"
```

Deploy it with your app:

```bash
shopify app deploy
```

##### Step 2: Create the metafield

After you create the metafield definition, add the metafield (value) using the GraphQL Admin API. Use the same namespace, key, and type from the definition:

```graphql
mutation AddInternalSKU {
  productUpdate(
    input: {
      id: "gid://shopify/Product/123456789"
      metafields: [
        {
          namespace: "$app"
          key: "internal_sku"
          value: "INV-2024-COTTON-001"
          type: "single_line_text_field"
        }
      ]
    }
  ) {
    product {
      id
      metafield(namespace: "$app", key: "internal_sku") {
        id
        value
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

**Note:**

Get a product ID by querying `products(first: 1)` in GraphiQL, or find it in the Shopify admin URL when viewing a product: `/admin/products/123456789`.

### Merchant-owned metafields

Merchant-owned metafields are custom data entries that merchants and all installed apps can modify. Both the structure and values are editable, making them ideal for shared data across multiple apps.

Create merchant-owned metafields using any [non-reserved namespace](#metafield-ownership) (such as `custom`, `specs`, or `inventory`).

**Info:**

Merchant-owned definitions can't be created in `shopify.app.toml`.

#### Example

You want to add warranty information to products. Because this type of field should be managed in the Shopify admin, you use a merchant-owned metafield.

##### Step 1: Create the metafield definition

First, create the metafield definition using the GraphQL Admin API. The following example doesn't use namespace `$app`, so the definition will be merchant-owned:

```graphql
mutation {
  metafieldDefinitionCreate(definition: {
    name: "Warranty Information",
    namespace: "custom",
    key: "warranty_info",
    description: "Product warranty details and coverage information",
    type: "multi_line_text_field",
    ownerType: PRODUCT,
    access: {
      storefront: PUBLIC_READ,
    },
  }) {
    createdDefinition {
      name
      namespace
      key
      type
      access
    }
  }
}
```

##### Step 2: Create the metafield

After you create the metafield definition, add the metafield (value). Use the same namespace, key, and type from the definition:

```graphql
mutation AddWarrantyInfo {
  productUpdate(
    input: {
      id: "gid://shopify/Product/123456789"
      metafields: [
        {
          namespace: "custom"
          key: "warranty_info"
          value: "2-year manufacturer warranty. Covers defects in materials and workmanship."
          type: "multi_line_text_field"
        }
      ]
    }
  ) {
    product {
      id
      metafield(namespace: "custom", key: "warranty_info") {
        id
        value
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

### App-data metafields

App-data metafields are tied to a specific app installation and are completely hidden from the Shopify admin. They're stored on the `AppInstallation` resource and can only be accessed by the owning app via GraphQL or through the [`app` object in Liquid](https://shopify.dev/docs/api/liquid/objects/app). They can't be created using `shopify.app.toml`.

Unlike [app-owned metafields](#app-owned-metafields) on shared resources, the `$app` reserved namespace isn't required because the `AppInstallation` owner provides isolation — only your app can access its own installation's metafields.

**Caution:**

Generally, private app data should be stored in an app-specific, secure database. App-data metafields can be used for per-installation configuration values, but sensitive credentials should be stored in environment variables or a dedicated secret management system.

#### Example

You want to store a feature tier configuration for each app installation. Because this data should be completely hidden from merchants and specific to each installation, you use app-data metafields.

##### Step 1: Retrieve the app installation ID

Get the app installation ID using the [`currentAppInstallation`](https://shopify.dev/docs/api/admin-graphql/latest/queries/currentAppInstallation) query:

```graphql
query {
  currentAppInstallation {
    id
  }
}
```

Response:

```json
{
  "data": {
    "currentAppInstallation": {
      "id": "gid://shopify/AppInstallation/123456"
    }
  }
}
```

##### Step 2: Create the app-data metafield

Create the app-data metafield using the [`metafieldsSet`](https://shopify.dev/docs/api/admin-graphql/current/mutations/metafieldsSet) mutation:

```graphql
mutation CreateAppDataMetafield($metafieldsSetInput: [MetafieldsSetInput!]!) {
  metafieldsSet(metafields: $metafieldsSetInput) {
    metafields {
      id
      namespace
      key
    }
    userErrors {
      field
      message
    }
  }
}
```

Variables:

```json
{
  "metafieldsSetInput": [
    {
      "namespace": "app_config",
      "key": "feature_tier",
      "type": "single_line_text_field",
      "value": "premium",
      "ownerId": "gid://shopify/AppInstallation/123456"
    }
  ]
}
```

### Permissions

Configure who can read and write your metafields using the `access` settings on your definition.

#### Shopify admin permissions

`admin` controls permissions for both the Shopify admin and the GraphQL Admin API.

**For app-owned metafields:**

TOML:

```toml
# Merchants can view but not edit (default)
access.admin = "merchant_read"

# Merchants can view and edit
access.admin = "merchant_read_write"
```

GraphQL:

```graphql
access: {
  admin: MERCHANT_READ  # view only (default)
}

access: {
  admin: MERCHANT_READ_WRITE  # view and edit
}
```

**For merchant-owned metafields:**

* Always full access - readable and writable by merchants and all apps with appropriate scopes. No configuration needed.

#### Storefront permissions

`storefront` controls permissions for the Storefront API (used by headless and custom storefronts). This setting doesn't affect Liquid templates - metafields are always accessible in Liquid regardless of this setting.

**Available settings:**

TOML:

```toml
# Hidden from Storefront API (default)
access.storefront = "none"

# Accessible in Storefront API
access.storefront = "public_read"
```

GraphQL:

```graphql
access: {
  storefront: NONE  # hidden (default)
}

access: {
  storefront: PUBLIC_READ  # accessible
}
```

**Note:**

Metafield access depends on its owning resource.

#### Customer accounts permissions

`customer_accounts` controls permissions for the Customer Accounts API.

**Available settings:**

TOML:

```toml
# Hidden from Customer Accounts API (default)
access.customer_account = "none"

# Readable in Customer Accounts API
access.customer_account = "read"

# Readable and writable in Customer Accounts API
access.customer_account = "read_write"
```

GraphQL:

```graphql
access: {
  customerAccount: NONE  # hidden (default)
}

access: {
  customerAccount: READ  # readable
}

access: {
  customerAccount: READ_WRITE  # readable and writable
}
```

**Note:**

Customer Account API access levels can only be adjusted via GraphQL Admin API mutation for app-owned metafields (namespace `app--`). For merchant-owned metafields, Customer Account API access can only be configured through the Shopify admin.

### Next steps

* Learn how to [model your data structure](https://shopify.dev/docs/apps/build/metaobjects/data-modeling-with-metafields-and-metaobjects).
* Learn how to [work with metafield definitions](https://shopify.dev/docs/apps/build/metafields/definitions).
* Learn how to [work with metafield values](https://shopify.dev/docs/apps/build/metafields/manage-metafields).
* Learn how to use metafields to [query resources](https://shopify.dev/docs/apps/build/metafields/query-using-metafields).
* Learn how to [enable filtering and other advanced features](https://shopify.dev/docs/apps/build/metafields/use-metafield-capabilities).

---

## Data modeling with metafields and metaobjects

> Fonte: https://shopify.dev/docs/apps/build/metaobjects/data-modeling-with-metafields-and-metaobjects

In this guide, you'll learn how to design Shopify-native data models using metafields and metaobjects. If you're familiar with relational databases, you'll learn how to translate concepts like tables, columns, foreign keys, and constraints into Shopify's architecture.

### Requirements

* Familiarity with SQL and relational database concepts (tables, columns, foreign keys, constraints).
* A basic understanding of app configuration with `shopify.app.toml`.
* A basic understanding of metafields and metaobjects.

### Mapping SQL concepts

When building an app, you often need to store data that doesn't fit into standard Shopify resources like products or orders.

In a relational database, you'd usually solve this by updating your database structure:

* You add a new column to an existing table to track new information (for example, an "estimated delivery date" on an orders table).
* You create brand-new tables to store new types of data (like a separate vendors table).

In Shopify, you achieve this using metafields and metaobjects:

* **Metafields** let you add extra fields (think: new columns) to existing Shopify resources, like products, orders, or customers.
* **Metaobjects** let you define totally new kinds of data (like custom tables), which you can relate to other resources or use in new ways.

Use the following table to map your database knowledge to Shopify concepts:

| Relational database concept | Shopify equivalent | Practical application |
| - | - | - |
| Table (built-in) | Resource | Standard objects like `Product`, `Customer`, and `Order`. |
| Table (custom) | Metaobject definition | A custom entity you define, for example, `Manufacturer` or `SizeChart`. |
| Column (on built-in table) | Metafield definition | A field added to a standard resource, such as a "Fabric" field on a `Product`. |
| Column (on custom table) | Metaobject field | A field on a metaobject, such as a "Website" field on a `Manufacturer` metaobject. |
| Row | Metaobject entry | A specific record of a metaobject, for example, "Nike". |
| Primary key (PK) | `GID` | The global ID, for example, `gid://shopify/Metaobject/123`. Always use this for relationships. |
| Foreign key (FK) | Reference type | A field typed as `metaobject_reference` or `product_reference`. |
| Constraints | Validations | Rules like `required`, `min`, `max`, or regex patterns applied to fields. |
| Migration file | `shopify.app.toml` | The declarative file where you define your schema. |

### Designing your model

Follow this workflow to translate your requirements into a Shopify schema. When planning your schema, keep metafield limits and metaobject limits in mind.

#### Step 1: Classify your data

Decide where your data belongs based on its relationship to the core commerce model:

| Data classification | Use this | Example |
| - | - | - |
| Attribute of a standard resource | Metafield definition | "Delivery Date" on an order |
| Reusable, standalone entity | Metaobject definition | "Designer Profile" shared across products |
| Relationship with extra metadata | Metaobject as join table | Ingredient list with quantities per recipe |

#### Step 2: Define relationships using types

In a relational database, you might store an ID as an integer or string. In Shopify, you must use reference types:

* **One-to-one relationship**: Use a single reference type such as a `metaobject_reference` or `product_reference`.
* **One-to-many relationship**: Use a multiple reference type such as a `list.metaobject_reference` or `list.product_reference`.

Don't store handles or IDs in plain text fields (`single_line_text_field`) to create relationships. This breaks the connection between related data and prevents Shopify from retrieving it efficiently in Liquid or the Storefront API.

#### Step 3: Configure access controls

You must explicitly define who can read and write your data. This is similar to defining database user permissions or row-level security.

* `access.admin`: Controls the Shopify admin and GraphQL Admin API.
  * Set to `merchant_read_write` if merchants need to edit this data in the Shopify admin.
* `access.storefront`: Controls the Storefront API (Headless/Hydrogen).
  * Set to `public_read` only if your data is consumed by a headless storefront. Liquid themes can access your data regardless of this setting.

### Example: Product highlights

This example shows how to create reusable "Product Highlights" (like "Eco-Friendly" or "Lifetime Warranty") that can be assigned to products.

#### The database view

In a SQL database, you might design it like this:

1. **Table**: `product_highlights` (columns: `id`, `title`, `icon`, `description`).
2. **Column**: Add a foreign key to `products`.

#### The Shopify view

Create a metaobject for the highlight entity and a metafield on the `Product` resource to store the references.

#### 1. Define the table (metaobject)

Add the following to your `shopify.app.toml` (located in your app's project root). When you deploy your app with `shopify app deploy`, Shopify creates these definitions on the store:

```toml
[metaobjects.app.product_highlight]
name = "Product Highlight"
display_name_field = "title"
description = "A reusable badge or highlight for product pages"


# Allow merchants to edit these in the Shopify admin
access.admin = "merchant_read_write"


# Fields (Columns)
[metaobjects.app.product_highlight.fields.title]
name = "Title"
type = "single_line_text_field"
required = true
validations.max = 50


[metaobjects.app.product_highlight.fields.icon]
name = "Icon"
type = "file_reference" # Strongly typed file storage


[metaobjects.app.product_highlight.fields.description]
name = "Description"
type = "multi_line_text_field"
```

#### 2. Define the foreign key (metafield)

Add the following to `shopify.app.toml`. This adds a "column" to the built-in `Product` table that points to our custom table:

```toml
[product.metafields.app.active_highlights]
name = "Active Highlights"
description = "Select the highlights to display on this product"


# This is a One-to-Many relationship (List of FKs)
type = "list.metaobject_reference<$app:product_highlight>"


# Merchants select the highlights on the product page
access.admin = "merchant_read_write"


# Expose to Headless channels (Liquid works automatically)
access.storefront = "public_read"
```

**Note:**

Enable `access.storefront = "public_read"` only if you're building a headless storefront. Liquid themes can access your data regardless of this setting.

#### How to use this data

Using specific data types unlocks built-in functionality. For example, the `file_reference` type gives you access to Liquid's image filters, and `metaobject_reference` automatically resolves related objects without extra queries.

Liquid (theme) access:

```liquid
{% for highlight in product.metafields.app.active_highlights.value %}
  <div class="highlight">
    {{ highlight.icon.value | image_url: width: 64 | image_tag }}
    <h3>{{ highlight.title.value }}</h3>
    <p>{{ highlight.description.value }}</p>
  </div>
{% endfor %}
```

### Common patterns

These patterns address scenarios you'll likely encounter when working with metafields and metaobjects.

#### Filtering (WHERE clauses)

In a database, you add an index to columns you want to query. In Shopify, you must enable capabilities.

First, enable filtering on the metafield definition:

```toml
[product.metafields.app.color]
name = "Color"
type = "single_line_text_field"
# Enables filtering in API queries
capabilities.admin_filterable = true
```

Then you can filter products using the GraphQL Admin API:

```graphql
query ProductsByColor {
  products(first: 10, query: "metafields.$app.color:\"blue\"") {
    edges {
      node {
        id
        title
      }
    }
  }
}
```

For more filtering patterns including numeric ranges and multiple conditions, refer to the Shopify documentation on querying using metafields.

#### Uniqueness and handles

Shopify resources and metaobjects have two identifiers:

| Identifier | Format | Use case |
| - | - | - |
| `GID` | `gid://shopify/Metaobject/123` | Internal references, relationships, API operations. Always unique and immutable. |
| `handle` | `eco-friendly-badge` | Human-readable URLs, Liquid lookups, importing/exporting data. |

**When to use each:**

* Use `GID` in your code for relationships and API calls. Reference types (`metaobject_reference`, `product_reference`) store GIDs automatically.
* Use handles when you need stable, readable identifiers for URLs or cross-store data migration.

Handles are auto-generated from the `display_name_field` but can be customized. To look up a metaobject by handle in Liquid:

```liquid
{% assign badge = shop.metaobjects.product_highlight.eco-friendly-badge %}
```

To enforce uniqueness on other fields, use the `unique_values` capability.

#### Modeling many-to-many relationships

In SQL, many-to-many relationships often require a join table. In Shopify, you have two options:

**Option A: List of references (recommended)**

Store a list of references on the parent object (as shown in the Product highlights example).

* **Best for**: Simple relationships where you just need to link object A to object B.
* **Pros**: Easy to query in Liquid and Storefront API, and simpler admin UI.

**Option B: The intermediate metaobject**

Create a third metaobject that has two reference fields (`product_reference` and `highlight_reference`) plus extra fields, for example, `sort_order`.

* **Best for**: When the relationship itself has data, for example, "Quantity" in a recipe ingredient list.
* **Cons**: Complex to query. Fetching the "grandchild" data in Storefront API can hit nesting limits.

### Next steps

**Manage metafield definitions** — Learn how to create and manage metafield definitions using TOML or GraphQL.

**Manage metaobject definitions** — Learn how to create and manage metaobject schemas using TOML or GraphQL.

**Data types reference** — Explore all available metafield and metaobject field types.

---

# Metafields

---

## List of data types (metafield TYPES reference)

> Fonte: https://shopify.dev/docs/apps/build/metafields/list-of-data-types

Each [metafield](https://shopify.dev/docs/apps/build/metafields) has a data type that determines what information it can store. All types have built-in validation and [Liquid](https://shopify.dev/docs/api/liquid/objects/metafield) support. Use this page to explore available types and their expected value formats.

**Note:** [Metaobjects](https://shopify.dev/docs/apps/build/metaobjects) use the same data types.

### How it works

When you create a metafield definition, the type applies to every instance of that resource. For example, if you create a definition called "Ingredients" with type `multi_line_text_field` for products, then every product enforces that type for its "Ingredients" metafield.

#### shopify.app.toml

**TOML**

```toml
[product.metafields.app.ingredients]
name = "Ingredients"
type = "multi_line_text_field"
```

**GraphQL Admin API response**

```json
{
  "data": {
    "product": {
      "metafield": {
        "namespace": "$app",
        "key": "ingredients",
        "value": "oat milk,\nsugar,\nchia seeds",
        "type": "multi_line_text_field",
        "definition": {
          "name": "Ingredients",
          "ownerType": "PRODUCT"
        }
      }
    }
  }
}
```

When using the GraphQL Admin API to read and write metafields, "the value is always entered and stored as a string, regardless of type."

For information about limits for each metafield type, refer to [metafield limits](https://shopify.dev/docs/apps/build/metafields/metafield-limits).

### Metafield type migration

You can change the type of a metafield, with some important considerations:

* Metafields cannot be migrated to type `id`.
* When migrating a metafield between incompatible types (for example, from `date_time` to `money`), the existing values become invalid. To fix this, use the Shopify admin to clear the invalid value, or use the API to clear the value or change the invalid definition to a compatible one.

### Basic types

Basic types store values like text, numbers, dates, and measurements paired with a unit. See [code samples](#basic-type-code-samples).

| Type | Description | Value type | Translatable | Market localizable |
| - | - | - | - | - |
| `antenna_gain` | A value and a unit of antenna gain. Valid unit values: `decibels_isotropic`, `decibels_dipole` | JSON object | no | no |
| `area` | A value and a unit of area. Valid unit values: `square_centimeters`, `square_feet`, `square_inches`, `square_meters`, `square_yards` | JSON object | no | no |
| `battery_charge_capacity` | A value and a unit of battery charge capacity. Valid unit values: `milliamp_hours` | JSON object | no | no |
| `battery_energy_capacity` | A value and a unit of battery energy capacity. Valid unit values: `watt_hours` | JSON object | no | no |
| `boolean` | A true or false value. | boolean | no | no |
| `capacitance` | A value and a unit of capacitance. Valid unit values: `picofarads`, `nanofarads`, `microfarads`, `farads` | JSON object | no | no |
| `color` | The hexadecimal code for a color. | string | no | no |
| `concentration` | A value and a unit of concentration. Valid unit values: `milligrams_per_gram`, `milligrams_per_milliliter` | JSON object | no | no |
| `data_storage_capacity` | A value and a unit of data storage capacity. Valid unit values: `bytes`, `kilobytes`, `megabytes`, `gigabytes`, `terabytes` | JSON object | no | no |
| `data_transfer_rate` | A value and a unit of data transfer rate. Valid unit values: `bits_per_second`, `kilobits_per_second`, `megabits_per_second`, `gigabits_per_second` | JSON object | no | no |
| `date` | A date in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format without a presumed timezone. | string | no | no |
| `date_time` | A date and time in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format without a presumed timezone. Defaults to Greenwich Mean Time (GMT). | string | no | no |
| `dimension` | A value and a unit of length. Valid unit values: `inches`, `feet`, `yards`, `millimeters`, `centimeters`, `meters` | JSON object | no | no |
| `display_density` | A value and a unit of display density. Valid unit values: `pixels_per_inch`, `dots_per_inch` | JSON object | no | no |
| `distance` | A value and a unit of distance. Valid unit values: `kilometers`, `miles` | JSON object | no | no |
| `duration` | A value and a unit of time duration. Valid unit values: `nanoseconds`, `microseconds`, `milliseconds`, `seconds`, `minutes`, `hours`, `days`, `months`, `years` | JSON object | no | no |
| `electric_current` | A value and a unit of electric current. Valid unit values: `milliamperes`, `amperes`, `kiloamperes` | JSON object | no | no |
| `electrical_resistance` | A value and a unit of electrical resistance. Valid unit values: `ohms`, `kiloohms` | JSON object | no | no |
| `energy` | A value and a unit of energy. Valid unit values: `joules`, `calories`, `kilojoules`, `kilocalories` | JSON object | no | no |
| `frequency` | A value and a unit of frequency. Valid unit values: `hertz`, `kilohertz`, `megahertz`, `gigahertz` | JSON object | no | no |
| `id` | A unique single-line text field. You can add [validations](https://shopify.dev/docs/apps/build/metafields/list-of-validation-options) for `min`, `max`, and `regex`. | string | no | no |
| `illuminance` | A value and a unit of illuminance. Valid unit values: `lux`, `foot_candles` | JSON object | no | no |
| `inductance` | A value and a unit of inductance. Valid unit values: `microhenries`, `millihenries`, `henries` | JSON object | no | no |
| `json` | A JSON-serializable value. This can be an object, an array, a string, a number, a boolean, or a null value. | JSON data | yes | no |
| `link` | A text and URL pairing that can be used to store link content. | JSON data | yes | no |
| `luminous_flux` | A value and a unit of luminous flux. Valid unit values: `lumens` | JSON object | no | no |
| `mass_flow_rate` | A value and a unit of mass flow rate. Valid unit values: `grams_per_day`, `grams_per_hour`, `grams_per_minute`, `grams_per_second`, `ounces_per_day`, `ounces_per_hour`, `ounces_per_minute`, `ounces_per_second`, `pounds_per_day`, `pounds_per_hour`, `pounds_per_minute`, `pounds_per_second`, `kilograms_per_day`, `kilograms_per_hour`, `kilograms_per_minute`, `kilograms_per_second`, `tons_per_day`, `tons_per_hour`, `tons_per_minute`, `tons_per_second`, `tonnes_per_day`, `tonnes_per_hour`, `tonnes_per_minute`, `tonnes_per_second` | JSON object | no | no |
| `money` | A numeric amount, with a currency code that matches the store's currency. You can [localize money metafields to a market](https://help.shopify.com/manual/markets/languages/translate-adapt-app#create-custom-content-for-a-market), but you can't translate them to a different language or locale. | JSON object | no | yes |
| `multi_line_text_field` | A multi-line text field. | string | yes | no |
| `number_decimal` | A number with decimal places in the range of +/-9999999999999.999999999. | string | no | no |
| `number_integer` | A whole number in the range of +/-9,007,199,254,740,991. | integer | no | no |
| `power` | A value and a unit of power. Valid unit values: `milliwatts`, `watts`, `horsepower`, `kilowatts` | JSON object | no | no |
| `pressure` | A value and a unit of pressure. Valid unit values: `pounds_per_square_inch`, `bars` | JSON object | no | no |
| `rating` | A rating measured on a specified scale. [Validations](https://shopify.dev/docs/apps/build/metafields/list-of-validation-options) are required for ratings and support `min` and `max`. | JSON object | no | no |
| `resolution` | A value and a unit of resolution. Valid unit values: `pixels`, `megapixels` | JSON object | no | no |
| `rich_text_field` | A rich text field supporting headings, lists, links, bold, and italics. Learn more about [rich text formatting](#rich-text-formatting-details). | JSON object | yes | no |
| `rotational_speed` | A value and a unit of rotational speed. Valid unit values: `revolutions_per_minute` | JSON object | no | no |
| `single_line_text_field` | A single-line text field. | string | yes | no |
| `sound_level` | A value and a unit of sound level. Valid unit values: `decibels` | JSON object | no | no |
| `speed` | A value and a unit of speed. Valid unit values: `kilometers_per_hour`, `feet_per_second`, `miles_per_hour`, `meters_per_second` | JSON object | no | no |
| `temperature` | A value and a unit of temperature. Valid unit values: `celsius`, `fahrenheit`, `kelvin` | JSON object | no | no |
| `thermal_power` | A value and a unit of thermal power. Valid unit values: `british_thermal_units_per_hour`, `kilowatts`, `tons_of_refrigeration` | JSON object | no | no |
| `url` | A URL with one of the allowed schemes: `https`, `http`, `mailto`, `sms`, `tel`. | string | yes | no |
| `voltage` | A value and a unit of voltage. Valid unit values: `volts` | JSON object | no | no |
| `volume` | A value and a unit of volume. Valid unit values: `milliliters`, `centiliters`, `liters`, `cubic_meters`, `us_fluid_ounces`, `us_pints`, `us_quarts`, `us_gallons`, `imperial_fluid_ounces`, `imperial_pints`, `imperial_quarts`, `imperial_gallons`. | JSON object | no | no |
| `volumetric_flow_rate` | A value and a unit of volumetric flow rate. Valid unit values: `liters_per_hour`, `liters_per_minute`, `liters_per_second`, `gallons_per_hour`, `gallons_per_minute`, `gallons_per_second`, `cubic_feet_per_hour`, `cubic_feet_per_minute`, `cubic_feet_per_second`, `cubic_meters_per_hour`, `cubic_meters_per_minute`, `cubic_meters_per_second` | JSON object | no | no |
| `weight` | A value and a unit of weight. Valid unit values: `ounces`, `pounds`, `grams`, `kilograms` | JSON object | no | no |

### Basic type code samples

The following examples demonstrate the expected value format for each basic type:

| Type | Sample |
| - | - |
| `antenna_gain` | `{"value": 5.0, "unit": "decibels_isotropic"}` |
| `area` | `{"value": 100.0, "unit": "square_meters"}` |
| `battery_charge_capacity` | `{"value": 3000.0, "unit": "milliamp_hours"}` |
| `battery_energy_capacity` | `{"value": 50.0, "unit": "watt_hours"}` |
| `boolean` | `true` |
| `capacitance` | `{"value": 100.0, "unit": "microfarads"}` |
| `color` | `#fff123` |
| `concentration` | `{"value": 5.0, "unit": "milligrams_per_milliliter"}` |
| `data_storage_capacity` | `{"value": 256.0, "unit": "gigabytes"}` |
| `data_transfer_rate` | `{"value": 100.0, "unit": "megabits_per_second"}` |
| `date` | `2022-02-02` |
| `date_time` | `2024-01-01T12:30:00` |
| `dimension` | `{"value": 25.0, "unit": "centimeters"}` |
| `display_density` | `{"value": 326.0, "unit": "pixels_per_inch"}` |
| `distance` | `{"value": 42.0, "unit": "kilometers"}` |
| `duration` | `{"value": 30.0, "unit": "seconds"}` |
| `electric_current` | `{"value": 2.5, "unit": "amperes"}` |
| `electrical_resistance` | `{"value": 100.0, "unit": "ohms"}` |
| `energy` | `{"value": 250.0, "unit": "kilocalories"}` |
| `frequency` | `{"value": 2.4, "unit": "gigahertz"}` |
| `id` | `1234` |
| `illuminance` | `{"value": 500.0, "unit": "lux"}` |
| `inductance` | `{"value": 10.0, "unit": "millihenries"}` |
| `json` | `{"ingredient": "flour", "amount": 0.3}` |
| `link` | `{"text": "Learn more", "url": "https://shopify.com"}` |
| `luminous_flux` | `{"value": 800.0, "unit": "lumens"}` |
| `mass_flow_rate` | `{"value": 5.0, "unit": "kilograms_per_hour"}` |
| `money` | `{"amount": "5.99", "currency_code": "CAD"}` |
| `multi_line_text_field` | `Ingredients\nFlour\nWater\nMilk\nEggs` |
| `number_decimal` | `10.4` |
| `number_integer` | `10` |
| `power` | `{"value": 100.0, "unit": "watts"}` |
| `pressure` | `{"value": 14.7, "unit": "pounds_per_square_inch"}` |
| `rating` | `{"value": "3.5", "scale_min": "1.0", "scale_max": "5.0"}` |
| `resolution` | `{"value": 12.0, "unit": "megapixels"}` |
| `rich_text_field` | `{"type": "root", "children": [{"type": "paragraph", "children": [{"type": "text", "value": "Bold text.", "bold": true}]}]}` |
| `rotational_speed` | `{"value": 3000.0, "unit": "revolutions_per_minute"}` |
| `single_line_text_field` | `VIP shipping method` |
| `sound_level` | `{"value": 85.0, "unit": "decibels"}` |
| `speed` | `{"value": 60.0, "unit": "kilometers_per_hour"}` |
| `temperature` | `{"value": 22.5, "unit": "celsius"}` |
| `thermal_power` | `{"value": 12000.0, "unit": "british_thermal_units_per_hour"}` |
| `url` | `https://www.shopify.com` |
| `voltage` | `{"value": 120.0, "unit": "volts"}` |
| `volume` | `{"value": 20.0, "unit": "milliliters"}` |
| `volumetric_flow_rate` | `{"value": 5.0, "unit": "liters_per_minute"}` |
| `weight` | `{"value": 2.5, "unit": "kilograms"}` |

### Reference types

Reference metafields store references to Shopify resources. See [code samples](#reference-type-code-samples).

| Type | Description | Value type | Translatable | Market localizable |
| - | - | - | - | - |
| `article_reference` | A reference to a [blog post](https://help.shopify.com/en/manual/online-store/blogs). | string | no | yes |
| `collection_reference` | A reference to a collection. | string | no | yes |
| `company_reference` | A reference to a company. | string | no | no |
| `customer_reference` | A reference to a customer. | string | no | no |
| `file_reference` | A reference to a file. The default value is `GenericFile`. You can use [validations](https://shopify.dev/docs/apps/build/metafields/list-of-validation-options) to add other file types (for example, `Image`). | string | yes | no |
| `metaobject_reference` | A reference to a metaobject entry. You can use [validations](https://shopify.dev/docs/apps/build/metafields/list-of-validation-options) to set which metaobject definition the metaobject must be. In TOML, use the [type shorthand](#declarative-toml-type-syntax): `type = "metaobject_reference<$app:author>"`. | string | no | yes |
| `mixed_reference` | A reference that can point to metaobjects from different definitions, unlike `metaobject_reference` which only allows metaobjects from one definition. In TOML, use the [type shorthand](#declarative-toml-type-syntax): `type = "mixed_reference<$app:author, $app:publisher>"`. | string | no | no |
| `page_reference` | A reference to a page. | string | no | yes |
| `product_reference` | A reference to a product. | string | no | yes |
| `product_taxonomy_value_reference` | A reference to a product taxonomy value. You can add [validations](https://shopify.dev/docs/apps/build/metafields/list-of-validation-options) to limit which taxonomy values can be selected. Refer to [Shopify Standard Product Taxonomy](https://shopify.github.io/product-taxonomy) for available values. | string | no | no |
| `variant_reference` | A reference to a product variant. | string | no | yes |

### Reference type code samples

The following examples demonstrate the expected value format for each reference type:

| Type | Sample |
| - | - |
| `article_reference` | `gid://shopify/Article/1` |
| `collection_reference` | `gid://shopify/Collection/1` |
| `company_reference` | `gid://shopify/Company/1` |
| `customer_reference` | `gid://shopify/Customer/1` |
| `file_reference` | `gid://shopify/MediaImage/123` |
| `metaobject_reference` | `gid://shopify/Metaobject/123` |
| `mixed_reference` | `gid://shopify/Metaobject/123` |
| `page_reference` | `gid://shopify/Page/1` |
| `product_reference` | `gid://shopify/Product/1` |
| `product_taxonomy_value_reference` | `gid://shopify/TaxonomyValue/1` |
| `variant_reference` | `gid://shopify/ProductVariant/1` |

### List types

List metafields store multiple values in a single metafield as a JSON array. See [code samples](#list-type-code-samples).

You can implement list metafields on the online store [using sections and blocks](https://shopify.dev/docs/storefronts/themes/best-practices/templates-sections-blocks#metafields). The type of list determines the implementation. For example, you could add a list of product references as a dynamic source to a custom block, or you could add a list of single line text fields to a text or rich text section.

**Info:** If you delete a product or variant from a store, then the product or variant is automatically removed from all list metafields that reference it.

| Type | Description | Translatable | Market localizable |
| - | - | - | - |
| `list.antenna_gain` | A list of values and a unit of antenna gain. Valid unit values: `decibels_isotropic`, `decibels_dipole` | no | no |
| `list.area` | A list of values and a unit of area. Valid unit values: `square_centimeters`, `square_feet`, `square_inches`, `square_meters`, `square_yards` | no | no |
| `list.article_reference` | A list of references to [blog posts](https://help.shopify.com/en/manual/online-store/blogs). | no | no |
| `list.battery_charge_capacity` | A list of values and a unit of battery charge capacity. Valid unit values: `milliamp_hours` | no | no |
| `list.battery_energy_capacity` | A list of values and a unit of battery energy capacity. Valid unit values: `watt_hours` | no | no |
| `list.capacitance` | A list of values and a unit of capacitance. Valid unit values: `picofarads`, `nanofarads`, `microfarads`, `farads` | no | no |
| `list.collection_reference` | A list of collection references. | no | no |
| `list.color` | A list of hexadecimal color codes. | no | no |
| `list.concentration` | A list of values and a unit of concentration. Valid unit values: `milligrams_per_gram`, `milligrams_per_milliliter` | no | no |
| `list.customer_reference` | A list of references to customers. | no | no |
| `list.data_storage_capacity` | A list of values and a unit of data storage capacity. Valid unit values: `bytes`, `kilobytes`, `megabytes`, `gigabytes`, `terabytes` | no | no |
| `list.data_transfer_rate` | A list of values and a unit of data transfer rate. Valid unit values: `bits_per_second`, `kilobits_per_second`, `megabits_per_second`, `gigabits_per_second` | no | no |
| `list.date` | A list of dates in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format without presumed timezones. | no | no |
| `list.date_time` | A list of dates and times in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format without presumed timezones. Defaults to Greenwich Mean Time (GMT). | no | no |
| `list.dimension` | A list of values and a unit of length. Valid unit values: `inches`, `feet`, `yards`, `millimeters`, `centimeters`, `meters`. | no | no |
| `list.display_density` | A list of values and a unit of display density. Valid unit values: `pixels_per_inch`, `dots_per_inch` | no | no |
| `list.distance` | A list of values and a unit of distance. Valid unit values: `kilometers`, `miles` | no | no |
| `list.duration` | A list of values and a unit of time duration. Valid unit values: `nanoseconds`, `microseconds`, `milliseconds`, `seconds`, `minutes`, `hours`, `days`, `months`, `years` | no | no |
| `list.electric_current` | A list of values and a unit of electric current. Valid unit values: `milliamperes`, `amperes`, `kiloamperes` | no | no |
| `list.electrical_resistance` | A list of values and a unit of electrical resistance. Valid unit values: `ohms`, `kiloohms` | no | no |
| `list.energy` | A list of values and a unit of energy. Valid unit values: `joules`, `calories`, `kilojoules`, `kilocalories` | no | no |
| `list.file_reference` | A list of references to files. The default value is `GenericFile`. You can use [validations](https://shopify.dev/docs/apps/build/metafields/list-of-validation-options) to add other file types (for example, `Image`). | yes | no |
| `list.frequency` | A list of values and a unit of frequency. Valid unit values: `hertz`, `kilohertz`, `megahertz`, `gigahertz` | no | no |
| `list.id` | A list of unique single-line text fields. You can add [validations](https://shopify.dev/docs/apps/build/metafields/list-of-validation-options) for `min`, `max`, and `regex`. | no | no |
| `list.illuminance` | A list of values and a unit of illuminance. Valid unit values: `lux`, `foot_candles` | no | no |
| `list.inductance` | A list of values and a unit of inductance. Valid unit values: `microhenries`, `millihenries`, `henries` | no | no |
| `list.link` | A list of text and URL pairings that can be used to store a collection of links. | yes | no |
| `list.luminous_flux` | A list of values and a unit of luminous flux. Valid unit values: `lumens` | no | no |
| `list.mass_flow_rate` | A list of values and a unit of mass flow rate. Valid unit values: `grams_per_day`, `grams_per_hour`, `grams_per_minute`, `grams_per_second`, `ounces_per_day`, `ounces_per_hour`, `ounces_per_minute`, `ounces_per_second`, `pounds_per_day`, `pounds_per_hour`, `pounds_per_minute`, `pounds_per_second`, `kilograms_per_day`, `kilograms_per_hour`, `kilograms_per_minute`, `kilograms_per_second`, `tons_per_day`, `tons_per_hour`, `tons_per_minute`, `tons_per_second`, `tonnes_per_day`, `tonnes_per_hour`, `tonnes_per_minute`, `tonnes_per_second` | no | no |
| `list.metaobject_reference` | A list reference to one or more metaobject entries that belong to a single metaobject definition. Unlike `list.mixed_reference`, all metaobject entries referenced must be of the same definition. In TOML, use the [type shorthand](#declarative-toml-type-syntax): `type = "list.metaobject_reference<$app:author>"`. | no | no |
| `list.mixed_reference` | A list reference to one or more metaobject entries that may belong to different metaobject definitions. In TOML, use the [type shorthand](#declarative-toml-type-syntax): `type = "list.mixed_reference<$app:author, $app:publisher>"`. | no | no |
| `list.number_decimal` | A list of numbers with decimal places in the range of +/-9999999999999.999999999. | no | no |
| `list.number_integer` | A list of whole numbers in the range of +/-9,007,199,254,740,991. | no | no |
| `list.page_reference` | A list of references to pages. | no | no |
| `list.power` | A list of values and a unit of power. Valid unit values: `milliwatts`, `watts`, `horsepower`, `kilowatts` | no | no |
| `list.pressure` | A list of values and a unit of pressure. Valid unit values: `pounds_per_square_inch`, `bars` | no | no |
| `list.product_reference` | A list of product references. | no | no |
| `list.product_taxonomy_value_reference` | A list of references to product taxonomy values. You can add [validations](https://shopify.dev/docs/apps/build/metafields/list-of-validation-options) to limit which taxonomy values can be selected. Refer to [Shopify Standard Product Taxonomy](https://shopify.github.io/product-taxonomy) for available values. | no | no |
| `list.rating` | A list of ratings measured on a specified scale. [Validations](https://shopify.dev/docs/apps/build/metafields/list-of-validation-options) are required for ratings and support `min` and `max`. | no | no |
| `list.resolution` | A list of values and a unit of resolution. Valid unit values: `pixels`, `megapixels` | no | no |
| `list.rotational_speed` | A list of values and a unit of rotational speed. Valid unit values: `revolutions_per_minute` | no | no |
| `list.single_line_text_field` | A list of single-line text fields. | yes | no |
| `list.sound_level` | A list of values and a unit of sound level. Valid unit values: `decibels` | no | no |
| `list.speed` | A list of values and a unit of speed. Valid unit values: `kilometers_per_hour`, `feet_per_second`, `miles_per_hour`, `meters_per_second` | no | no |
| `list.temperature` | A list of values and a unit of temperature. Valid unit values: `celsius`, `fahrenheit`, `kelvin` | no | no |
| `list.thermal_power` | A list of values and a unit of thermal power. Valid unit values: `british_thermal_units_per_hour`, `kilowatts`, `tons_of_refrigeration` | no | no |
| `list.url` | A list of URLs with one of the allowed schemes: `https`, `http`, `mailto`, `sms`, `tel`. | yes | no |
| `list.variant_reference` | A list of references to product variants. | no | no |
| `list.voltage` | A list of values and a unit of voltage. Valid unit values: `volts` | no | no |
| `list.volume` | A list of values and a unit of volume. Valid unit values: `milliliters`, `centiliters`, `liters`, `cubic_meters`, `us_fluid_ounces`, `us_pints`, `us_quarts`, `us_gallons`, `imperial_fluid_ounces`, `imperial_pints`, `imperial_quarts`, `imperial_gallons`. | no | no |
| `list.volumetric_flow_rate` | A list of values and a unit of volumetric flow rate. Valid unit values: `liters_per_hour`, `liters_per_minute`, `liters_per_second`, `gallons_per_hour`, `gallons_per_minute`, `gallons_per_second`, `cubic_feet_per_hour`, `cubic_feet_per_minute`, `cubic_feet_per_second`, `cubic_meters_per_hour`, `cubic_meters_per_minute`, `cubic_meters_per_second` | no | no |
| `list.weight` | A list of values and a unit of weight. Valid unit values: `ounces`, `pounds`, `grams`, `kilograms` | no | no |

### List type code samples

The following examples demonstrate the expected value format for each list type (representative samples — all list types follow the same `[ {...}, {...} ]` array shape):

| Type | Sample |
| - | - |
| `list.antenna_gain` | `[{"value": 5.0, "unit": "decibels_isotropic"}, {"value": 3.0, "unit": "decibels_isotropic"}]` |
| `list.article_reference` | `["gid://shopify/Article/1", "gid://shopify/Article/2"]` |
| `list.collection_reference` | `["gid://shopify/Collection/1", "gid://shopify/Collection/2"]` |
| `list.color` | `["#FFF123", "#E6E6FA", "#00FF00"]` |
| `list.customer_reference` | `["gid://shopify/Customer/1", "gid://shopify/Customer/2"]` |
| `list.date` | `["2022-01-01", "2022-05-05"]` |
| `list.date_time` | `["2024-01-01T12:30:00", "2024-05-01T12:30:00"]` |
| `list.dimension` | `[{"value": 25.0, "unit": "centimeters"}, {"value": 35.0, "unit": "centimeters"}]` |
| `list.file_reference` | `["gid://shopify/MediaImage/123", "gid://shopify/MediaImage/456"]` |
| `list.id` | `["1234", "5678"]` |
| `list.link` | `[{"text": "Start a business", "url": "https://shopify.com"}, {"text": "Read the docs", "url": "https://shopify.dev/docs"}]` |
| `list.metaobject_reference` | `["gid://shopify/Metaobject/123", "gid://shopify/Metaobject/456"]` |
| `list.mixed_reference` | `["gid://shopify/Metaobject/123", "gid://shopify/Metaobject/456"]` |
| `list.number_decimal` | `["10.4", "20.5", "30.6"]` |
| `list.number_integer` | `["10", "20", "30"]` |
| `list.page_reference` | `["gid://shopify/Page/1", "gid://shopify/Page/2"]` |
| `list.product_reference` | `["gid://shopify/Product/1", "gid://shopify/Product/2"]` |
| `list.product_taxonomy_value_reference` | `["gid://shopify/TaxonomyValue/1", "gid://shopify/TaxonomyValue/2"]` |
| `list.rating` | `[{"value": "3.5", "scale_min": "1.0", "scale_max": "5.0"}, {"value": "4.5", "scale_min": "1.0", "scale_max": "5.0"}]` |
| `list.single_line_text_field` | `["VIP shipping method", "Standard shipping method"]` |
| `list.url` | `["https://www.shopify.com", "https://www.shopify.dev"]` |
| `list.variant_reference` | `["gid://shopify/ProductVariant/1", "gid://shopify/ProductVariant/2"]` |
| `list.weight` | `[{"value": 2.5, "unit": "kilograms"}, {"value": 4.5, "unit": "kilograms"}]` |

> Note: Every measurement list type (`list.area`, `list.volume`, `list.power`, `list.temperature`, `list.speed`, `list.frequency`, etc.) follows the same `[{"value": ..., "unit": ...}, ...]` shape as `list.dimension` above, using the unit values documented in the corresponding basic type.

### Declarative (TOML) type syntax

When defining metafields or metaobject fields in `shopify.app.toml`, most types use the type name directly:

```toml
[product.metafields.app.ingredients]
type = "multi_line_text_field"
```

However, reference types that point to metaobjects require a special shorthand syntax that embeds the target definition in the type. This replaces the `metaobject_definition_id` and `metaobject_definition_ids` [validations](https://shopify.dev/docs/apps/build/metafields/list-of-validation-options) used in the GraphQL Admin API.

* **`metaobject_reference` and `list.metaobject_reference`**: Use angle brackets to specify which metaobject definition the reference must point to:

```toml
[product.metafields.app.author]
type = "metaobject_reference<$app:author>"

[product.metafields.app.related_authors]
type = "list.metaobject_reference<$app:author>"
```

* **`mixed_reference` and `list.mixed_reference`**: Use a comma-separated list inside the angle brackets to specify which metaobject definitions are allowed:

```toml
[product.metafields.app.content_block]
type = "mixed_reference<$app:author, $app:publisher>"

[product.metafields.app.content_blocks]
type = "list.mixed_reference<$app:author, $app:publisher>"
```

#### Metaobject field example

The same syntax applies when defining fields on metaobject definitions:

```toml
[metaobjects.app.book.fields.author]
type = "metaobject_reference<$app:author>"

[metaobjects.app.book.fields.related_content]
type = "list.mixed_reference<$app:author, $app:publisher>"
```

**Info:** You don't need to add `metaobject_definition_id` or `metaobject_definition_ids` validations in TOML. The type shorthand syntax above handles this automatically.

### Rich text formatting details

The `rich_text_field` metafield type accepts a JSON object that uses the following general structure:

```json
{
  "type": "root",
  "children": [
    {
      "type": "paragraph",
      "children": [
        {
          "type": "text",
          "value": "This is italicized text and ",
          "italic": true
        },
        {
          "url": "https://example.com",
          "title": "Link to example.com",
          "type": "link",
          "children": [
            {
              "type": "text",
              "value": "a bolded hyperlink",
              "bold": true
            }
          ]
        }
      ]
    }
  ]
}
```

Refer to the following code samples for examples of the objects that can be used to represent fragments of rich text:

#### Bold and italics

```json
{
  "type": "root",
  "children": [
    {
      "type": "paragraph",
      "children": [
        {
          "type": "text",
          "value": "This text is bolded and italicized.",
          "bold": true,
          "italic": true
        }
      ]
    }
  ]
}
```

#### Heading

```json
{
  "type": "root",
  "children": [
    {
      "type": "paragraph",
      "children": [
        {
          "type": "heading",
          "children": [{
            "type": "text",
            "value": "This is an H1 heading"
          }],
          "level": 1
        }
      ]
    }
  ]
}
```

#### Hyperlink

```json
{
  "type": "root",
  "children": [
    {
      "type": "paragraph",
      "children": [
        {
          "url": "https://example.com",
          "title": "Link to example.com",
          "type": "link",
          "children": [{
            "type": "text",
            "value": "This is a hyperlink"
          }]
        }
      ]
    }
  ]
}
```

#### Lists

```json
{
  "type": "root",
  "children": [
    {
      "listType": "ordered",
      "type": "list",
      "children": [
        {
          "type": "list-item",
          "children": [{
            "type": "text",
            "value": "This is the first list item."
          }]
        },
        {
          "type": "list-item",
          "children": [{
            "type": "text",
            "value": "This is the second list item."
          }]
        }
      ]
    }
  ]
}
```

### Next steps

* Learn how to [work with metafield values](https://shopify.dev/docs/apps/build/metafields/manage-metafields).
* Learn how to [work with metafield definitions](https://shopify.dev/docs/apps/build/metafields/definitions).
* Learn about [standard definitions](https://shopify.dev/docs/apps/build/metafields/list-of-standard-definitions).
* Learn about [validation options](https://shopify.dev/docs/apps/build/metafields/list-of-validation-options).

---

## List of validation options

> Fonte: https://shopify.dev/docs/apps/build/metafields/list-of-validation-options

Metafield definitions can have validation options. Validation options enable you to apply additional constraints to the data that a metafield can store, such as a minimum or maximum value, or a regular expression. The type of the metafield definition determines which validation options are available.

### How it works

In `shopify.app.toml`, validations use dot notation under the metafield definition. Set properties directly under `validations`:

```toml
[product.metafields.app.summary]
type = "single_line_text_field"
validations.min = 8
validations.max = 100
```

For struct values like weight or dimension constraints, use inline TOML tables:

```toml
[product.metafields.app.package_weight]
type = "weight"
validations.min = { unit = "g", value = 10 }
validations.max = { unit = "g", value = 500 }
```

For validations that accept list values, use TOML arrays:

```toml
[product.metafields.app.flavor]
type = "single_line_text_field"
validations.choices = ["Floral", "Sweet", "Nutty", "Other"]
```

#### GraphQL Admin API syntax

When using the GraphQL Admin API, you include a validation option using a `name` and a corresponding `value` string. The appropriate value depends on the metafield type that the validation applies to. For more information about supported formats and units of measurement available for each type, refer to [metafield types](https://shopify.dev/docs/apps/build/metafields/list-of-data-types).

### Supported validation options

The following table describes the validation options available for metafield definitions. Refer to the [examples](#examples) for validation option code snippets.

| Validation option | Description | Supported types | Use cases |
| --- | --- | --- | --- |
| Minimum length | Sets the minimum length of a text value | `single_line_text_field`, `multi_line_text_field` | A blog summary needs to be at least 100 characters to provide sufficient detail. A zip code needs an exact character length, so set minimum and maximum to the same value. |
| Maximum length | Sets the maximum length of a text value | `single_line_text_field`, `multi_line_text_field` | A blog summary or product description needs a maximum length of 150 characters to fit a designated page area. A phone number needs an exact length of ten, so set both minimum and maximum to `10`. |
| Regular expression | Sets a regular expression. Shopify supports [RE2](https://github.com/google/re2/wiki/Syntax). | `single_line_text_field`, `multi_line_text_field` | An email field requires an `@` symbol followed by a `.` and text. A serial number must start with specific characters. |
| Allowed domains | A list of allowed domains. | `url` | Allow links to specific social media sites. Allow links to other pages within your site for related products. |
| Choices | A list of up to 128 predefined options limiting allowed values. Maximum 300,000 characters. | `single_line_text_field` | A flavor profile field for coffee allows: Floral, Sweet, Nutty, Other. A sizing field allows: True to size, Runs large, Runs small. |
| File type options | Sets a list of file type options. Empty allows all files. Valid values: `Image`, `Video`. | `file_reference` | A blog author photo must be an image. A demonstration video in MP4 format. Product instructions in PDF format. |
| Maximum precision | Sets the maximum decimal places for a decimal number | `number_decimal` | A version number field accepts one decimal place. A product specification field has a maximum of three decimal places. |
| Minimum date | Sets the minimum date in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format | `date` | The expiry or release date must be after a specific date. |
| Maximum date | Sets the maximum date in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format | `date` | Future product availability cannot be later than a specific date. |
| Minimum datetime | Sets the minimum date and time in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format | `date_time` | A product release occurs on a specific date at midnight and won't display before that date and time. |
| Maximum datetime | Sets the maximum date and time in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format | `date_time` | A customer loyalty reward expires on a specific date and time. The reward cannot be used after that date and time. |
| Minimum weight | Sets the minimum weight | `weight` | A bundled product weight field needs maximum allowed weight. |
| Maximum weight | Sets the maximum weight | `weight` | An order requires minimum weight for shipping. |
| Minimum volume | Sets the minimum volume | `volume` | A product volume field needs specific minimum volume. A product needs exact volume, so set minimum and maximum to the same value. |
| Maximum volume | Sets the maximum volume | `volume` | A product volume field needs certain maximum volume. Set minimum and maximum to the same value for exact volume. |
| Minimum dimension | Sets the minimum dimension | `dimension` | A product needs minimum length, width, or height. |
| Maximum dimension | Sets the maximum dimension | `dimension` | A product needs maximum length, width, or height. |
| Minimum integer | Sets the minimum integer number | `number_integer` | A product number must be within a specific range. Set minimum and maximum validations to create the range. |
| Maximum integer | Sets the maximum integer number | `number_integer` | A product number must be within a specific range. Set minimum and maximum validations to create the range. |
| Minimum decimal | Sets the minimum decimal number | `number_decimal` | A product version field accepts a version number greater than a specific decimal, such as `0.5`. |
| Maximum decimal | Sets the maximum decimal number | `number_decimal` | A product version field accepts a version number less than a specific decimal, such as `1.99`. |
| Metaobject definition | Sets the metaobject definition that a reference must point to | `metaobject_reference`, `list.metaobject_reference` | A product refers to a `Designer` metaobject. |
| Multiple metaobject definitions | Sets permitted metaobject definitions that can be referred to | `mixed_reference`, `list.mixed_reference` | A product referencing a list of different `Material` metaobjects. A dynamic placeholder supporting a union set of metaobject definitions. |
| JSON schema | Sets permitted JSON format. Maximum 300,000 characters. | `json` | Data from a third-party app must match a specific JSON schema. |
| Product taxonomy attribute | Sets the product taxonomy attribute that a reference must point to | `product_taxonomy_value_reference`, `list.product_taxonomy_value_reference` | A product referencing a `Color` taxonomy value. A product referencing a list of `Material` taxonomy values. |
| List minimum | Sets the minimum number of items in a list | Any list type | A product must have at least two related products. A blog post must have at least one tag. |
| List maximum | Sets the maximum number of items in a list | Any list type | A product can have up to five related products. A blog post can have up to 10 tags. |

### Examples

This section provides examples of each validation option, in both TOML and GraphQL Admin API formats.

#### Minimum length

The following example validates the minimum length of a text value to eight characters.

TOML:
```toml
validations.min = 8
```
GraphQL Admin API:
```yml
validations: [{
  name: "min",
  value: "8"
}]
```

#### Maximum length

The following example validates the maximum length of a text value to 25 characters.

TOML:
```toml
validations.max = 25
```
GraphQL Admin API:
```yml
validations: [{
  name: "max",
  value: "25"
}]
```

#### Regular expression

The following example validates a regular expression that matches the pattern `(@)(.+)$`.

TOML:
```toml
validations.regex = "(@)(.+)$"
```
GraphQL Admin API:
```yml
validations: [{
  name: "regex",
  value: "(@)(.+)$"
}]
```

#### Allowed domains

The following example validates `shopify.com` against a list of allowed domains.

TOML:
```toml
validations.allowed_domains = ["shopify.com"]
```
GraphQL Admin API:
```yml
validations: [{
  name: "allowed_domains",
  value: "[\"shopify.com\"]"
}]
```

#### Choices

The following example validates the values allowed for the metafield: `red`, `green`, `blue`.

TOML:
```toml
validations.choices = ["red", "green", "blue"]
```
GraphQL Admin API:
```yml
validations: [{
  name: "choices",
  value: "[\"red\", \"green\", \"blue\"]"
}]
```

#### File type options

The following example validates the allowed file type options: `Image`, `Video`.

TOML:
```toml
validations.file_type_options = ["Image", "Video"]
```
GraphQL Admin API:
```yml
validations: [{
  name: "file_type_options",
  value: "[\"Image\",\"Video\"]"
}]
```

#### Maximum precision

The following example validates that the maximum number of decimal places to store for a floating-point number is two.

TOML:
```toml
validations.max_precision = 2
```
GraphQL Admin API:
```yml
validations: [{
  name: "max_precision",
  value: "2"
}]
```

#### Minimum date

The following example validates the setting for the minimum date in ISO 8601 format.

TOML:
```toml
validations.min = "2022-01-01"
```
GraphQL Admin API:
```yml
validations: [{
  name: "min",
  value: "2022-01-01"
}]
```

#### Maximum date

The following example validates the setting for the maximum date in ISO 8601 format.

TOML:
```toml
validations.max = "2022-03-03"
```
GraphQL Admin API:
```yml
validations: [{
  name: "max",
  value: "2022-03-03"
}]
```

#### Minimum datetime

The following example validates the setting for the minimum date and time in ISO 8601 format.

TOML:
```toml
validations.min = "2022-03-03T16:30:00"
```
GraphQL Admin API:
```yml
validations: [{
  name: "min",
  value: "2022-03-03T16:30:00"
}]
```

#### Maximum datetime

The following example validates the setting for the maximum date and time in ISO 8601 format.

TOML:
```toml
validations.max = "2022-03-03T16:30:00"
```
GraphQL Admin API:
```yml
validations: [{
  name: "max",
  value: "2022-03-03T16:30:00"
}]
```

#### Minimum weight

The following example validates a setting for the minimum weight to be ten grams.

TOML:
```toml
validations.min = { unit = "g", value = 10 }
```
GraphQL Admin API:
```yml
validations: [{
  name: "min",
  value: "{\"unit\":\"g\",\"value\":10}"
}]
```

#### Maximum weight

The following example validates a setting for the maximum weight to be 50 grams.

TOML:
```toml
validations.max = { unit = "g", value = 50 }
```
GraphQL Admin API:
```yml
validations: [{
  name: "max",
  value: "{\"unit\":\"g\",\"value\":50}"
}]
```

#### Minimum volume

The following example validates a setting for the minimum volume to be five milliliters.

TOML:
```toml
validations.min = { unit = "ml", value = 5 }
```
GraphQL Admin API:
```yml
validations: [{
  name: "min",
  value: "{\"unit\":\"ml\",\"value\":5}"
}]
```

#### Maximum volume

The following example validates a setting for the maximum volume to be 50 milliliters.

TOML:
```toml
validations.max = { unit = "ml", value = 50 }
```
GraphQL Admin API:
```yml
validations: [{
  name: "max",
  value: "{\"unit\":\"ml\",\"value\":50}"
}]
```

#### Minimum dimension

The following example validates a setting for the minimum dimension to be five centimeters.

TOML:
```toml
validations.min = { unit = "cm", value = 5 }
```
GraphQL Admin API:
```yml
validations: [{
  name: "min",
  value: "{\"unit\":\"cm\",\"value\":5}"
}]
```

#### Maximum dimension

The following example validates a setting for the maximum dimension to be 50 centimeters.

TOML:
```toml
validations.max = { unit = "cm", value = 50 }
```
GraphQL Admin API:
```yml
validations: [{
  name: "max",
  value: "{\"unit\":\"cm\",\"value\":50}"
}]
```

#### Minimum integer

The following example validates a setting for the minimum integer number to be nine.

TOML:
```toml
validations.min = 9
```
GraphQL Admin API:
```yml
validations: [{
  name: "min",
  value: "9"
}]
```

#### Maximum integer

The following example validates a setting for the maximum integer number to be 15.

TOML:
```toml
validations.max = 15
```
GraphQL Admin API:
```yml
validations: [{
  name: "max",
  value: "15"
}]
```

#### Minimum decimal

The following example validates a setting for the minimum decimal number to be 0.5.

TOML:
```toml
validations.min = 0.5
```
GraphQL Admin API:
```yml
validations: [{
  name: "min",
  value: "0.5"
}]
```

#### Maximum decimal

The following example validates a setting for the maximum decimal number to be 1.99.

TOML:
```toml
validations.max = 1.99
```
GraphQL Admin API:
```yml
validations: [{
  name: "max",
  value: "1.99"
}]
```

#### Metaobject definition

In TOML, this validation isn't needed because the target definition is specified directly in the `type` field using the [type shorthand syntax](https://shopify.dev/docs/apps/build/metafields/list-of-data-types#declarative-toml-type-syntax). For example:

```toml
[product.metafields.app.designer]
type = "metaobject_reference<$app:designer>"
```

When using the GraphQL Admin API, set the metaobject definition that a reference must point to:

```yml
validations: [{
  name: "metaobject_definition_id",
  value: "gid://shopify/MetaobjectDefinition/123"
}]
```

#### Multiple metaobject definitions

In TOML, this validation isn't needed because the permitted definitions are specified directly in the `type` field using the type shorthand syntax. For example:

```toml
[product.metafields.app.content_block]
type = "mixed_reference<$app:author, $app:publisher>"
```

When using the GraphQL Admin API, set the permitted metaobject definitions that can be referred to:

```yml
validations: [{
  name: "metaobject_definition_ids",
  value: "[\"gid://shopify/MetaobjectDefinition/123\",\"gid://shopify/MetaobjectDefinition/456\"]"
}]
```

#### JSON schema

The following example validates a setting for the permitted JSON format.

TOML:
```toml
validations.schema = '{"$id":"https://example.com/person.schema.json","$schema":"https://json-schema.org/draft/2020-12/schema","title":"Person","type":"object","properties":{"firstName":{"type":"string"},"lastName":{"type":"string"},"age":{"type":"integer","minimum":0}}}'
```
GraphQL Admin API:
```yml
validations: [{
  name: "schema",
  value: "{ ... escaped JSON schema with $id, $schema, title, type, properties (firstName, lastName, age) ... }"
}]
```

#### Product taxonomy attribute

The following example validates a setting for the product taxonomy attribute that a reference must point to.

TOML:
```toml
validations.product_taxonomy_attribute_handle = "style"
```
GraphQL Admin API:
```yml
validations: [{
  name: "product_taxonomy_attribute_handle",
  value: "style"
}]
```

#### List minimum

The following example validates that a list must contain at least two items.

TOML:
```toml
[product.metafields.app.tags.validations]
"list.min" = 2
```
GraphQL Admin API:
```yml
validations: [{
  name: "list.min",
  value: "2"
}]
```

#### List maximum

The following example validates that a list can contain up to five items.

TOML:
```toml
[product.metafields.app.tags.validations]
"list.max" = 5
```
GraphQL Admin API:
```yml
validations: [{
  name: "list.max",
  value: "5"
}]
```

### Next steps

- Learn how to [work with metafield definitions](https://shopify.dev/docs/apps/build/metafields/definitions).
- Learn about [metafield data types](https://shopify.dev/docs/apps/build/metafields/list-of-data-types).
- Learn how to [enable filtering and other advanced features](https://shopify.dev/docs/apps/build/metafields/use-metafield-capabilities).

---

## Manage metafield definitions

> Fonte: https://shopify.dev/docs/apps/build/metafields/definitions

Metafield definitions are schemas that specify the structure, type, and rules for metafields. Without definitions, metafields are untyped strings that can't be edited in the Shopify admin or validated.

This guide shows you how to create, read, update, and delete metafield definitions using TOML configuration or the GraphQL Admin API.

**Note:** Not sure how to structure your data? See [Data modeling with metafields and metaobjects](https://shopify.dev/docs/apps/build/metaobjects/data-modeling-with-metafields-and-metaobjects) for a translation guide from SQL concepts to Shopify's architecture.

### Requirements

* Your app can make [authenticated requests](https://shopify.dev/docs/api/usage/authentication) to the GraphQL Admin API.
* Your app has the appropriate access scopes for the [owner type](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType) that you want to associate with the metafield definition. For example, `write_products` for product metafields, or `write_customers` for customer metafields.

### Creating definitions

There are two ways to create metafield definitions:

* **TOML**: TOML configurations in `shopify.app.toml` create app-owned definitions. Your app maintains control over the schema while optionally allowing metafield (value) edits in the Shopify admin.
* **GraphQL**: The GraphQL Admin API provides programmatic control for creating merchant-owned definitions (editable in the Shopify admin by merchants and all installed apps) and dynamically generating definitions based on user configuration.

**Tip:** Creating merchant-owned metafields for common use cases (like ISBN or ingredients)? Use Shopify's pre-defined [standard definitions](#standard-definitions) instead.

#### TOML (app-owned) example

This example creates an app-owned definition that tracks when products were last synchronized. The definition grants merchants write access to metafield values through `access.admin = "merchant_read_write"`, while the definition schema remains app-controlled.

```toml
[product.metafields.app.last_synced]
name = "Last Synced"
description = "When this product was last synchronized with external system"
type = "date_time"
access.admin = "merchant_read_write"
```

Once you've updated the file, deploy the changes with your app:

```bash
shopify app deploy
```

**Benefits of TOML:**

* Definitions are version-controlled as part of your app.
* Automatic creation and updates on deploy.
* Works with `shopify app dev` to safely test out changes.
* Consistent across all shops - when you update your app's data structure, it deploys to every installation automatically.
* The app maintains ownership.

#### GraphQL Admin API example

These examples show how to create metafield definitions using GraphQL. The first creates a merchant-owned definition that all apps can access. The second creates an app-owned definition that only your app controls.

##### Merchant-owned (editable in Shopify admin)

```graphql
# POST https://{shop}.myshopify.com/api/{api_version}/graphql.json
# Headers: X-Shopify-Access-Token: {merchant_token}

mutation CreateMerchantOwnedDefinition {
  metafieldDefinitionCreate(
    definition: {
      namespace: "product_details"
      key: "warranty_info"
      name: "Warranty Information"
      description: "Product warranty details and coverage"
      type: "multi_line_text_field"
      ownerType: PRODUCT
      access: {
        storefront: PUBLIC_READ
      }
    }
  ) {
    createdDefinition {
      id
      namespace
      key
    }
    userErrors {
      field
      message
    }
  }
}
```

##### App-owned (app controlled)

```graphql
# POST https://{shop}.myshopify.com/api/{api_version}/graphql.json
# Headers: X-Shopify-Access-Token: {app_token}

mutation CreateAppOwnedDefinition {
  metafieldDefinitionCreate(
    definition: {
      namespace: "$app" # app-reserved namespace
      key: "warranty_info"
      name: "Warranty Information"
      description: "Product warranty details and coverage"
      type: "multi_line_text_field"
      ownerType: PRODUCT
      access: {
        admin: MERCHANT_READ_WRITE
        storefront: PUBLIC_READ
      }
    }
  ) {
    createdDefinition {
      id
      namespace
      key
    }
    userErrors {
      field
      message
    }
  }
}
```

Key differences:

* **Merchant-owned**: Use any non-reserved namespace (like `product_details`). This provides full control in the Shopify admin—no `access.admin` needed. Only `access.storefront` is used to control customer visibility.
* **App-owned**: Use the reserved `$app` namespace. The app controls the definition. Use `access.admin` to grant merchant write permissions.

#### When to use GraphQL vs TOML

**Use TOML when:**

* Your app needs fixed, known fields (for example, tracking numbers, warranty dates).
* The structure is consistent across all installations.
* Fields are core to your app's functionality.
* You want a version-controlled, declarative configuration.

**Use GraphQL when:**

* Merchants define their own custom fields through your app's UI.
* Field structure varies per merchant or changes frequently.
* Building form builders, CMS-like tools, or field managers.
* You're creating merchant-owned fields that other apps can access.

#### Dynamic definition creation example

This example shows how to programmatically create definitions based on user input, such as in a field manager app where custom fields are configured through your app's UI.

Your app would collect field configuration (via a form or UI), validate the input, construct the variables object, and then execute the mutation. This enables the creation of custom fields through your app's interface without editing code or configuration files.

```graphql
mutation CreateDynamicField($input: MetafieldDefinitionInput!) {
  metafieldDefinitionCreate(definition: $input) {
    createdDefinition {
      id
      name
      namespace
      key
      type { name }
    }
    userErrors {
      field
      message
      code
    }
  }
}
```

Variables:

```json
{
  "input": {
    "name": "Return Policy",
    "namespace": "custom",
    "key": "return_policy",
    "description": "Store's return policy for this product",
    "type": "multi_line_text_field",
    "ownerType": "PRODUCT",
    "validations": [
      {
        "name": "max_length",
        "value": "1000"
      }
    ],
    "access": {
      "storefront": "PUBLIC_READ"
    }
  }
}
```

### Reading definitions

Use GraphQL to find existing definitions and check their capabilities.

Query all definitions by resource type:

```graphql
query {
  metafieldDefinitions(first: 100, ownerType: PRODUCT) {
    edges {
      node {
        id
        namespace
        key
        name
        type { name }
        access { admin storefront }
      }
    }
  }
}
```

Search definitions by name or namespace:

```graphql
query {
  metafieldDefinitions(
    first: 20
    ownerType: PRODUCT
    query: "warranty"
  ) {
    edges {
      node {
        id
        name
        namespace
        key
        type { name }
      }
    }
  }
}
```

Find a specific definition by namespace and key:

```graphql
query {
  metafieldDefinitions(
    first: 1
    ownerType: PRODUCT
    namespace: "product_details"
    key: "warranty_info"
  ) {
    edges {
      node {
        id
        name
        namespace
        key
        type { name }
        access { admin storefront }
      }
    }
  }
}
```

**Tip:** Query the [`metafieldDefinitionTypes`](https://shopify.dev/docs/api/admin-graphql/latest/queries/metafieldDefinitionTypes) field to see which validations each type supports, or check the [`supportedValidations`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-supportedvalidations) field when querying existing definitions.

### Updating definitions

Only specific fields can be updated after creation:

| Field | Can update | Method |
| --- | --- | --- |
| Name and description | Yes | TOML or GraphQL |
| Validations | Yes (with limits) | TOML or GraphQL |
| Access permissions | Yes | TOML or GraphQL |
| Type | No | Can't change |
| Namespace/key | No | Immutable |
| Owner type | No | Can't migrate |

The following example shows how to update a definition's name, description, and access permissions using the [`metafieldDefinitionUpdate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/metafieldDefinitionUpdate) mutation:

```graphql
mutation {
  metafieldDefinitionUpdate(
    definition: {
      id: "gid://shopify/MetafieldDefinition/1234567890"
      name: "Updated Name"
      description: "Updated description"
      access: { storefront: PUBLIC_READ }
    }
  ) {
    updatedDefinition { id name }
    userErrors { field message }
  }
}
```

**Caution:** Tightening validations may fail if existing metafields violate the new constraint.

To change a namespace/key:

1. Create a new definition with the desired namespace/key.
2. Copy the existing metafield values to the new namespace/key.
3. Update your app code, extensions, and integrations to reference the new namespace/key.
4. Test thoroughly with both definitions active to ensure everything works.
5. Delete the old definition once migration is complete.

This approach enables safe, zero-downtime migration by allowing you to test with both the old and new metafields active before removing the old one.

### Deleting definitions

For TOML definitions:

1. Remove the definition from your `shopify.app.toml` file.
2. Deploy the change:

```bash
shopify app deploy
```

For GraphQL definitions, use the [`metafieldDefinitionDelete`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/metafieldDefinitionDelete) mutation:

```graphql
mutation {
  metafieldDefinitionDelete(
    id: "gid://shopify/MetafieldDefinition/1234567890"
    deleteAllAssociatedMetafields: true
  ) {
    deletedDefinitionId
    userErrors { field message }
  }
}
```

Set `deleteAllAssociatedMetafields` to `true` to delete all metafield values along with the definition, or `false` to only delete the definition while preserving existing values.

### Access control

Control who can read and write metafield values using settings on your definition. For comprehensive details, see [Permissions](https://shopify.dev/docs/apps/build/metafields#permissions).

**For app-owned metafields (using the `app` namespace):**

* Merchants can always read all metafields and definitions in their store.
* Only the app can make changes to the definition.
* Use `access.admin = "merchant_read_write"` to allow value edits in the Shopify admin.

**For merchant-owned metafields:**

* Merchants always have full control of both the definition and the values.
* The `access.storefront` setting controls customer visibility.

### Standard definitions

Shopify provides pre-defined standard metafield definitions for common use cases like product descriptions, ISBN numbers, and care instructions. These definitions use reserved namespace/key combinations (such as `descriptors.subtitle` or `facts.isbn`) that ensure interoperability across themes, apps, and the Shopify ecosystem.

Standard definitions are Shopify-owned with predefined access controls that vary by definition. Values are readable and writable across apps and in the Shopify admin.

Query available standard definitions using the [`standardMetafieldDefinitionTemplates`](https://shopify.dev/docs/api/admin-graphql/latest/queries/standardMetafieldDefinitionTemplates) query:

```graphql
query {
  standardMetafieldDefinitionTemplates(first: 50) {
    edges {
      node {
        id
        name
        namespace
        key
        type { name }
        ownerTypes
      }
    }
  }
}
```

Enable standard definitions using TOML configuration or the [`standardMetafieldDefinitionEnable`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/standardMetafieldDefinitionEnable) mutation. This example enables the subtitle and ISBN standard definitions for products:

**TOML:**

```toml
[product.metafields]
standard_metafields = ["descriptors.subtitle", "facts.isbn"]

[product_variant.metafields]
standard_metafields = ["descriptors.subtitle"]
```

**GraphQL:**

```graphql
# Enable subtitle standard metafield on product
mutation {
  standardMetafieldDefinitionEnable(
    id: "gid://shopify/StandardMetafieldDefinitionTemplate/1",
    ownerType: PRODUCT
  ) {
    createdDefinition {
      name
      key
      namespace
      description
    }
  }
}

# Enable ISBN standard metafield on product
mutation {
  standardMetafieldDefinitionEnable(
    id: "gid://shopify/StandardMetafieldDefinitionTemplate/3",
    ownerType: PRODUCT
  ) {
    createdDefinition {
      name
      key
      namespace
      description
    }
  }
}

# Enable subtitle standard metafield on product variant
mutation {
  standardMetafieldDefinitionEnable(
    id: "gid://shopify/StandardMetafieldDefinitionTemplate/1",
    ownerType: PRODUCTVARIANT
  ) {
    createdDefinition {
      name
      key
      namespace
      description
    }
  }
}
```

**Note:** Standard definitions auto-enable when your app [creates metafield values](https://shopify.dev/docs/apps/build/metafields/manage-metafields#using-standard-definitions) for them. Manually enable them to make the definition available in the Shopify admin for populating values.

For more about standard definitions, see the [standard definitions list](https://shopify.dev/docs/apps/build/metafields/list-of-standard-definitions).

### Error handling

Understanding common errors helps you implement proper error handling and provide better user experiences. Most errors occur during definition creation or updates when validations, permissions, or naming conflicts arise.

| Error | Cause | Solution |
| --- | --- | --- |
| `TAKEN` | Namespace/key is already in use | Query existing definitions first or use a different namespace/key |
| "Type <invalid_type> is not a valid type" | Invalid type name | Check [available types](https://shopify.dev/docs/apps/build/metafields/list-of-data-types) |
| "Validation <validation_name> is not supported for type <type_name>" | Wrong validation for type | Query [`supportedValidations`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-supportedvalidations) or check [validations guide](https://shopify.dev/docs/apps/build/metafields/list-of-validation-options) |
| "App does not have permission to modify this definition" | Not app-owned | Only app-owned definitions can be modified by apps |

### Best practices

Following these practices helps ensure maintainable, scalable metafield implementations that work well across development, staging, and production environments. Good naming and planning prevent migration headaches and help make your metafields easier for teams to understand and use.

* Use descriptive namespaces: `shipping_settings` rather than `custom`.
* Organize with sub-namespaces: For app-owned metafields, use sub-namespaces to group related fields. In TOML, `[product.metafields.analytics.lifetime_value]` creates namespace `app--{id}--analytics`. In GraphQL, use `namespace: "$app:analytics"`.
* Add validations gradually: Start loose, tighten as needed.
* Test in development first: Verify before production.
* Document for your team: Maintain a schema reference.
* Cache definition IDs: Avoid repeated queries.
* Batch related operations: Create multiple definitions together.

### TOML reference

Metafields are declared in `shopify.app.toml` using the format `[<owner_type>.metafields.app.<key>]`. For example, `[product.metafields.app.page_count]` declares a product metafield with namespace `$app` and key `page_count`.

Metafields can be defined on many different resource types. For a full list, see [MetafieldOwnerType](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).

| Property | Description |
| --- | --- |
| `type` | [Data type](https://shopify.dev/docs/apps/build/metafields/list-of-data-types) for the metafield. For `metaobject_reference` and `mixed_reference` types, use the [shorthand syntax](https://shopify.dev/docs/apps/build/metafields/list-of-data-types#declarative-toml-type-syntax) to embed the target definition (for example, `type = "metaobject_reference<$app:author>"`). |
| `name` | Human-readable name displayed in the Shopify admin. |
| `description` | Descriptive text that explains the purpose of the metafield. |
| `access.admin` | Admin UI access control: `merchant_read` or `merchant_read_write`. |
| `access.storefront` | Storefront access control: `public_read` or `none`. |
| `access.customer_account` | Customer API access control: `read`, `read_write`, or `none`. |
| `capabilities.admin_filterable` | When `true`, enables filtering by this metafield in the Shopify admin UI and Admin API. |
| `capabilities.unique_values` | When `true`, enforces uniqueness on metafield values. |
| `capabilities.cart_to_order_copyable` | When `true`, automatically copies the cart metafield value to the corresponding order metafield when an order is created. Only available for order metafield definitions. |
| `validations` | Rules to [validate field values](https://shopify.dev/docs/apps/build/metafields/list-of-validation-options#toml-syntax) (for example, min/max values, regex patterns). In TOML, use dot notation like `validations.min = "8"` or `validations.choices = ["red", "green"]`. |

### TOML limitations

When using TOML-based declarative definitions, be aware of these constraints:

#### App-reserved namespace

You can only declare metafield definitions in the app-reserved namespace (`$app`) to ensure that only the owning app can make changes to definitions. This constraint allows Shopify to guarantee a consistent state between all shops your app is installed on.

#### App-scoped limits

| Limit | Value |
| --- | --- |
| Metafield definitions per owner type | 128 |
| Changes per deploy | 25 |

To ensure Shopify can quickly and reliably distribute definitions across shops, you can't make more than 25 metafield changes (creation, update, or deletion) in a single deploy. If you need to make more than 25 changes, do so over multiple deploys.

#### Read-only through Admin API

Declarative definitions are read-only through the Admin API, and can only be updated or deleted through the TOML configuration file. You can query declarative definitions through the Admin API, but mutations will return an error.

#### Capability support

| Capability | Supported in TOML |
| --- | --- |
| [Smart collections](https://shopify.dev/docs/apps/build/metafields/use-metafield-capabilities#smart-collection) | No |
| [Admin filterable](https://shopify.dev/docs/apps/build/metafields/use-metafield-capabilities#admin-filterable) | Yes |
| [Unique values](https://shopify.dev/docs/apps/build/metafields/use-metafield-capabilities#unique-values) | Yes |
| [Cart to order copyable](https://shopify.dev/docs/apps/build/metafields/use-metafield-capabilities#cart-to-order-copyable) | Yes |
| [Pinning](https://help.shopify.com/en/manual/custom-data/metafields/pinning-metafield-definitions) | No |

### Next steps

* Learn how to [work with metafield values](https://shopify.dev/docs/apps/build/metafields/manage-metafields).
* Learn about [validation options](https://shopify.dev/docs/apps/build/metafields/list-of-validation-options).
* Learn how to [enable filtering and other advanced features](https://shopify.dev/docs/apps/build/metafields/use-metafield-capabilities).

---

## Manage values (metafield values)

> Fonte: https://shopify.dev/docs/apps/build/metafields/manage-metafields

Metafields are key-value pairs that let you store custom data on Shopify resources like products, customers, and orders. This guide shows you how to create, read, update, and delete metafield values using the GraphQL Admin API.

### Requirements

* Your app can make [authenticated requests](https://shopify.dev/docs/api/admin-graphql#authentication) to the GraphQL Admin API.
* You have the appropriate scopes, such as `write_products` and `write_customers`, based on owner type.
* You've created a [metafield definition](https://shopify.dev/docs/apps/build/metafields/definitions) for your metafield. The definition establishes the schemas (structure and rules) for metafields. If you're creating metafields for common use cases, you can [skip this step](#using-standard-definitions).

### Creating metafields

Create metafields by including them when creating or updating resources (like [`productCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productcreate) or [`productUpdate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productupdate)). Alternatively, use [`metafieldsSet`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/metafieldsSet) for standalone metafield operations.

**Note:** The metafield's namespace, key, and type must match its corresponding [metafield definition](https://shopify.dev/docs/apps/build/metafields/definitions).

#### App-owned metafield example

Create app-owned metafields for your app-owned definitions. This gives your app exclusive control over both the definition (schema) and the metafield (value). App ownership is established using the namespace `$app`.

This example uses `productCreate` to create a product along with an app-owned metafield:

```graphql
mutation CreateProductWithAppMetafield {
  productCreate(
    input: {
      title: "Analytics-Tracked Product"
      metafields: [
        {
          namespace: "$app"
          key: "internal_analytics"
          value: "{\"views\": 0, \"lastViewed\": null}"
          type: "json"
        }
      ]
    }
  ) {
    product {
      id
      title
      metafield(namespace: "$app", key: "internal_analytics") {
        id
        value
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

#### Merchant-owned metafields

Create merchant-owned metafields for your merchant-owned definitions. Merchant-ownership ensures shared management access across apps and in the Shopify admin. Merchant ownership is established using any namespace that isn't reserved for apps or Shopify (see [Metafield ownership](https://shopify.dev/docs/apps/build/metafields#metafield-ownership)).

This example uses `productCreate` to create a product along with a merchant-owned metafield.

```graphql
mutation CreateProductWithMetafield {
  productCreate(
    input: {
      title: "Premium Laptop"
      metafields: [
        {
          namespace: "product_details"
          key: "warranty_info"
          value: "2 year limited warranty"
          type: "multi_line_text_field"
        }
      ]
    }
  ) {
    product {
      id
      title
      metafield(namespace: "product_details", key: "warranty_info") {
        id
        value
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

#### Creating multiple metafields

Set multiple metafields at once by passing an array. This is more efficient than making separate requests for each metafield. See [metafield limits](https://shopify.dev/docs/apps/build/metafields/metafield-limits) for maximum batch sizes.

```graphql
mutation CreateProductWithMultipleMetafields {
  productCreate(
    input: {
      title: "Cotton T-Shirt"
      metafields: [
        {
          namespace: "specs"
          key: "weight"
          value: "{\"value\": 2.5, \"unit\": \"KILOGRAMS\"}"
          type: "weight"
        },
        {
          namespace: "specs"
          key: "material"
          value: "Cotton blend"
          type: "single_line_text_field"
        }
      ]
    }
  ) {
    product {
      id
      title
      metafields(first: 10, namespace: "specs") {
        edges {
          node {
            key
            value
          }
        }
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

#### Using standard definitions

Shopify provides pre-defined metafield schemas for common use cases like ISBN numbers, ingredients, and product specifications. Using these standard definitions saves you from creating custom definitions and ensures compatibility across themes and apps.

Standard definitions auto-enable when you create metafield values using their namespace and key (like `facts` and `isbn`):

```graphql
mutation AddISBNToProduct {
  productUpdate(
    input: {
      id: "gid://shopify/Product/123456789"
      metafields: [
        {
          namespace: "facts"
          key: "isbn"
          value: "978-3-16-148410-0"
          type: "single_line_text_field"
        }
      ]
    }
  ) {
    product {
      id
      metafield(namespace: "facts", key: "isbn") {
        id
        value
        definition {
          standardTemplate {
            id
            name
          }
        }
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

Once enabled, Shopify owns the schema, but the metafields (values) created are merchant-owned. See the [standard definitions list](https://shopify.dev/docs/apps/build/metafields/list-of-standard-definitions) for available standard namespaces and keys.

### Reading metafields

Query metafields through their parent resource using GraphQL. This example retrieves a product along with its metafields, demonstrating three common patterns: fetching metafields (with pagination), getting a specific metafield by namespace/key, and filtering by namespace.

```graphql
query GetProductWithMetafields {
  product(id: "gid://shopify/Product/1234567890") {
    id
    title
    metafields(first: 10) {
      edges {
        node {
          namespace
          key
          value
          type
        }
      }
    }
    warranty: metafield(namespace: "product_details", key: "warranty_info") {
      value
    }
    productDetails: metafields(namespace: "product_details", first: 20) {
      edges {
        node {
          key
          value
        }
      }
    }
  }
}
```

For advanced querying techniques, see [Query using metafields](https://shopify.dev/docs/apps/build/metafields/query-using-metafields).

### Updating metafields

Update metafields using the resource mutation approach. Metafields automatically update if the namespace/key combination already exists.

```graphql
mutation UpdateProductMetafield {
  productUpdate(
    input: {
      id: "gid://shopify/Product/1234567890"
      metafields: [
        {
          namespace: "product_details"
          key: "warranty_info"
          value: "Extended 3 year warranty available"
          type: "multi_line_text_field"
        }
      ]
    }
  ) {
    product {
      metafield(namespace: "product_details", key: "warranty_info") {
        value
        updatedAt
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

**Note:** The [type](https://shopify.dev/docs/apps/build/metafields/list-of-data-types) must match the original definition. You can't change a metafield's type by updating its value.

### Deleting metafields

Delete metafields using the [`metafieldsDelete`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/metafieldsDelete) mutation with their namespace, key, and owner ID.

```graphql
mutation DeleteMetafield {
  metafieldsDelete(metafields: [
    {
      ownerId: "gid://shopify/Product/1234567890"
      namespace: "product_details"
      key: "warranty_info"
    }
  ]) {
    deletedMetafields {
      key
      namespace
      ownerId
    }
    userErrors {
      field
      message
    }
  }
}
```

**Note:** Deleting a resource (using `productDelete` or `customerDelete` for example) automatically deletes all associated metafields. Use `metafieldsDelete` when you want to remove specific metafields while keeping the resource.

### Error handling

Common errors and their solutions when working with metafields.

| Error | Cause | Solution |
| - | - | - |
| "Value is invalid for type" | Wrong format for type | Check [type formats](https://shopify.dev/docs/apps/build/metafields/list-of-data-types) |
| "Validation failed" | Value doesn't meet validation rules | Check definition's [validation constraints](https://shopify.dev/docs/apps/build/metafields/list-of-validation-options) |
| "Type mismatch" | Type doesn't match definition | Use the exact type from definition |
| "JSON parse error" | Invalid JSON format | Validate JSON and escape properly |

### Best practices

Following these practices helps ensure efficient, reliable metafield management and prevents common issues:

* Batch operations: Set multiple metafields in one request by passing an array (see [limits](https://shopify.dev/docs/apps/build/metafields/metafield-limits)).
* Validate before saving: Check value format matches type requirements
* Use consistent formatting: Maintain consistent JSON structures and date formats
* Handle references carefully: Verify referenced resources exist
* Escape JSON properly: Use JSON.stringify() for complex values
* Query efficiently: Use specific namespaces/keys instead of fetching all
* Cache metafield IDs: Store IDs for frequently accessed metafields

### Next steps

* Learn how to [work with metafield definitions](https://shopify.dev/docs/apps/build/metafields/definitions).
* Learn how to use metafields to [query resources](https://shopify.dev/docs/apps/build/metafields/query-using-metafields).
* Learn how to [enable filtering and other advanced features](https://shopify.dev/docs/apps/build/metafields/use-metafield-capabilities).

---

## List of standard metafield definitions

> Fonte: https://shopify.dev/docs/apps/build/metafields/list-of-standard-definitions

Standard metafield definitions are [metafield definitions](https://shopify.dev/docs/apps/build/metafields/definitions) that we've created for some common use cases. If you need to store data for one of these use cases, then we recommend using the standard metafield definitions, because they're interoperable across the entire Shopify platform and connect more seamlessly to themes. Standards ensure interoperability across the Shopify ecosystem.

[Standard metafield definition templates](https://shopify.dev/docs/api/admin-graphql/latest/objects/StandardMetafieldDefinitionTemplate) provide preset configurations to create metafield definitions. Each template has a specific namespace and key that we've reserved to have specific meanings for common use cases.

**Tip:** For more information about the types of information that metafield definitions can store, refer to [Metafield types](https://shopify.dev/docs/apps/build/metafields/list-of-data-types).

The following table describes the standard metafield definitions:

| Name and ID | Type | Details |
| --- | --- | --- |
| Product subtitle (ID: `1`) | `single_line_text_field` | Stores a concise description of a product. All apps should use this metafield instead of the product's full description when a brief product summary is needed. For example, SMS apps can use the product subtitle for short text messages about a product. **Maximum length:** 70 characters. **Allowed resources:** `PRODUCT`, `PRODUCTVARIANT`. **Reserved namespace and key:** `descriptors.subtitle` |
| Care guide (ID: `2`) | `multi_line_text_field` | Stores detailed instructions on how to take care of clothing. Themes aimed at users selling apparel can use this metafield for display on product detail pages. **Maximum length:** 500 characters. **Allowed resources:** `PRODUCT`, `PRODUCTVARIANT`. **Reserved namespace and key:** `descriptors.care_guide` |
| ISBN (ID: `3`) | `single_line_text_field` | Stores an ISBN book identifier. Themes supporting booksellers can use this metafield to identify books to customers. Apps helping to merchandise books should write to this metafield for optimal theme integration. **Value:** Must be a 10-digit or 13-digit number, with optional hyphens. **Allowed resources:** `PRODUCT`, `PRODUCTVARIANT`. **Reserved namespace and key:** `facts.isbn` |
| UPC (ID: `4`) | `single_line_text_field` | Stores a Universal Product Code (UPC). Apps reading or writing UPCs should integrate this standard metafield for display purposes, or for integration with ERP systems. **Value:** Must be a 12-digit number with at least one zero. **Allowed resources:** `PRODUCT`, `PRODUCTVARIANT`. **Reserved namespace and key:** `facts.upc` |
| EAN (ID: `5`) | `single_line_text_field` | Stores a European Article Number (EAN). Similar to UPCs, apps reading or writing EANs should integrate this standard metafield for display in online stores, or for integration with ERP systems. **Value:** Must be a 13-digit number. **Allowed resources:** `PRODUCT`, `PRODUCTVARIANT`. **Reserved namespace and key:** `facts.ean` |
| Product rating (ID: `6`) | `rating` | Stores the average rating for a product or variant. Product rating apps should write to this standard metafield and update it whenever a product's rating has changed. Themes that display product ratings should reference this metafield for the aggregated average rating. **Allowed resources:** `PRODUCT`, `PRODUCTVARIANT`. **Reserved namespace and key:** `reviews.rating` |
| Product rating count (ID: `7`) | `number_integer` | Stores the total number of ratings for a product or variant. Product rating apps should write to this standard metafield and update it whenever a product's rating has changed. Themes that display product ratings should reference this metafield. **Allowed resources:** `PRODUCT`, `PRODUCTVARIANT`. **Reserved namespace and key:** `reviews.rating_count` |
| Related products (ID: `14`) | `list.product_reference` | Stores products that are similar to a selected product. You can display potential substitutes to help customers discover other similar products that they might like. **Allowed resources:** `PRODUCT`. **Reserved namespace and key:** `shopify--discovery--product_recommendation.related_products` |
| Related products setting (ID: `15`) | `single_line_text_field` | Stores a setting value that controls how manual product recommendations are displayed. `only manual` displays only manual recommendations. `ahead` displays manual recommendations before auto-generated recommendations. **Allowed resources:** `PRODUCT`. **Reserved namespace and key:** `shopify--discovery--product_recommendation.related_products_display` |
| Search product boosts (ID: `16`) | `list.single_line_text_field` | Stores search terms that are associated to a product. When a customer searches a store using the search terms, the product ranks higher in the search results. **Allowed resources:** `PRODUCT`. **Reserved namespace and key:** `shopify--discovery--product_search_boost.queries` |
| Complementary products (ID: `17`) | `list.product_reference` | Stores products that are often bought in addition to a selected product. You can display complementary products to help customers discover new products and to increase sales. **Allowed resources:** `PRODUCT`. **Reserved namespace and key:** `shopify--discovery--product_recommendation.complementary_products` |
| Birth date (ID: `19`) | `date` | Stores the customer's date of birth in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601). You can use this metafield to [create a filter](https://help.shopify.com/en/manual/customers/customer-segmentation/customer-segments/customer-segmentation-reference/customer-segment-metafield) that segments customers by birthday to automatically send a discount. **Allowed resources:** `CUSTOMER`. **Reserved namespace and key:** `facts.birth_date` |
| Trade item description (ID: `20`) | `multi_line_text_field` | Stores a precise product description that describes specific attributes of the product for customs and import. **Allowed resources:** `PRODUCT`, `PRODUCTVARIANT`. **Reserved namespace and key:** `import_information.trade_item_description` |
| Product transport declaration (ID: `21`) | `list.single_line_text_field` | Stores public transport declarations, such as batteries, hazardous materials, creams, liquids, or powders. **Allowed resources:** `PRODUCT`, `PRODUCTVARIANT`. **Reserved namespace and key:** `import_information.product_transport_declaration` |
| External URL (ID: `27`) | `url` | Stores a product URL at the product variant level for merchants that host their storefronts outside of Shopify. This URL populates the global Catalog. **Allowed resources:** `PRODUCTVARIANT`. **Reserved namespace and key:** `shopify.external_url` |

### Interacting with standard metafield definitions

You can interact with standard metafield definitions using GraphQL queries or mutations:

| Action | Query or mutation |
| --- | --- |
| Access standard metafield definition templates | Use the [standardMetafieldDefinitionTemplates](https://shopify.dev/docs/api/admin-graphql/current/queries/standardMetafieldDefinitionTemplates) query to access standard metafield definition templates. |
| Access metafield definition | Use the [metafieldDefinition](https://shopify.dev/docs/api/admin-graphql/current/queries/metafieldDefinition) query to access a standard metafield definition. |
| Create a metafield definition | Use the [`standardMetafieldDefinitionEnable`](https://shopify.dev/docs/api/admin-graphql/current/mutations/standardMetafieldDefinitionEnable) mutation to create a metafield definition using one of the standard metafield definition templates. To specify the template you want to use, provide the ID for the template in the format `gid://shopify/StandardMetafieldDefinitionTemplate/<id>`, where `id` is the corresponding ID value from the table. |
| Delete a metafield definition | Use the [metafieldDefinitionDelete](https://shopify.dev/docs/api/admin-graphql/current/mutations/metafieldDefinitionDelete) mutation to delete a metafield definition. |

### Next steps

* Learn how to [manage metafield definitions](https://shopify.dev/docs/apps/build/metafields/definitions).
* Learn how to [manage validation options](https://shopify.dev/docs/apps/build/metafields/list-of-validation-options).

---

## Use metafield capabilities

> Fonte: https://shopify.dev/docs/apps/build/metafields/use-metafield-capabilities

Capabilities enable optional features for metafield definitions. You can enable the following `capabilities`:

* **`smartCollectionCondition`**: Create an automated collection based on metafield values for a given definition.
* **`adminFilterable`**: Filter supported owner types based on metafield values for a definition in the Shopify admin and GraphQL Admin API.
* **`uniqueValues`**: Enforce unique metafield values for a definition.
* **`cartToOrderCopyable`**: Automatically copy cart metafield values to corresponding order metafields when an order is created.

**Capability support in TOML configuration:** Currently, only the `adminFilterable`, `uniqueValues`, and `cartToOrderCopyable` capabilities are supported in TOML configuration.

### Smart collection

An automated collection, also known as a smart collection, is a grouping of products that's defined by a set of rules. Shopify automatically changes the contents of an automated collection based on the configured rules. You can create rules with metafield definitions to automatically update the contents of an automated collection based on product or variant metafields.

Smart collections are available for the following metafield types:

| Metafield definition type | Supported conditions |
| --- | --- |
| True or false | equals |
| Integer | equals, greater than, less than |
| Decimal | equals, greater than, less than |
| Rating | equals, greater than, less than |
| Single line text | equals |
| Metaobject reference | equals |

#### Enabling the smart collection capability

Enable this capability using either `metafieldDefinitionUpdate` or `metafieldDefinitionCreate`.

The following example shows how to update a metafield definition with the `smartCollectionCondition` set to `true` to enable the smart collection capability:

```graphql
mutation metafieldDefinitionUpdate($definition: MetafieldDefinitionUpdateInput!) {
  metafieldDefinitionUpdate(definition: $definition) {
    userErrors {
      field
      message
    }
    updatedDefinition {
      key
      name
      namespace
      ownerType
      id
      capabilities {
        smartCollectionCondition {
          enabled
        }
      }
    }
  }
}
```

Variables:

```json
{
  "definition": {
    "namespace": "custom",
    "key": "material",
    "ownerType": "PRODUCT",
    "capabilities": {
      "smartCollectionCondition": {
        "enabled": true
      }
    }
  }
}
```

#### Using metafields in a smart collection

After the capability is enabled, you can create a smart collection either in the Shopify admin or with the following mutations:

* To create a smart collection, you can use the `collectionCreate` mutation.
* To update an existing collection, you can use the `collectionUpdate` mutation.

The following example creates a smart collection that includes products with a `color` metaobject reference set to `blue`:

```graphql
mutation CreateCollection($collection: CollectionInput!) {
  collectionCreate(input: $collection) {
    collection {
      id
      title
      descriptionHtml
      sortOrder
      handle
      templateSuffix
      ruleSet {
        appliedDisjunctively
        rules {
          column
          relation
          condition
        }
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

Variables:

```json
{
  "collection": {
    "title": "Blue products collection",
    "metafields": [],
    "ruleSet": {
      "appliedDisjunctively": false,
      "rules": [
        {
          "column": "PRODUCT_METAFIELD_DEFINITION",
          "relation": "EQUALS",
          "condition": "gid://shopify/Metaobject/112030056537",
          "conditionObjectId": "gid://shopify/MetafieldDefinition/23417389145"
        }
      ]
    }
  }
}
```

### Admin filterable

The Shopify admin filterable capability allows you to use a metafield definition and its values to filter resource lists in the Shopify admin. This capability makes it easier for developers to find and manage resources, such as products, based on their specific metafield values.

Admin filterable is available for the following resources:

| Resource Type |
| --- |
| Products |
| Companies* |
| Company Locations* |
| Metaobjects |
| Orders |

*Does not support numeric and date searches at this time.

**Info:** Admin Filterable is available for all metafield types EXCEPT JSON and rich text.

To enable this capability, you can use TOML configuration or the `metafieldDefinitionUpdate` mutation.

The following example shows how to enable the admin filterable capability:

TOML:
```toml
[product.metafields.custom.material]
name = "material"
type = "single_line_text_field"
capabilities.admin_filterable = true
```

GraphQL:
```graphql
mutation metafieldDefinitionUpdate {
  metafieldDefinitionUpdate(definition: {
    namespace: "custom"
    key: "material"
    ownerType: PRODUCT
    capabilities: {
      adminFilterable: {
        enabled: true
      }
    }
  }) {
    userErrors {
      field
      message
    }
    updatedDefinition {
      key
      name
      namespace
      ownerType
      id
      capabilities {
        adminFilterable {
          enabled
        }
      }
    }
  }
}
```

### Unique values

The unique values capability ensures all values of a metafield definition are unique. This is commonly used when storing external identifiers that must not duplicate, like ERP or PIM IDs.

| Metafield Type |
| --- |
| Single line text |
| URL |
| Integer |

The following example shows how to create a metafield definition with `uniqueValues` set to `true` to enable the unique values capability:

TOML:
```toml
[product.metafields.custom.external_id]
name = "External ID"
type = "single_line_text_field"
capabilities.unique_values = true
```

GraphQL:
```graphql
mutation {
  metafieldDefinitionCreate(definition: {
    name: "External ID"
    namespace: "custom"
    key: "external_id"
    type: "single_line_text_field"
    ownerType: PRODUCT
    capabilities: {
      uniqueValues: {
        enabled: true
      }
    }
  }) {
    createdDefinition {
      id
      name
      namespace
      key
      capabilities {
        uniqueValues {
          enabled
        }
      }
    }
    userErrors {
      field
      message
      code
    }
  }
}
```

### Cart to order copyable

You can automatically copy the value from a cart metafield to the corresponding order metafield when an order is created. The namespace and key must match between the cart and order metafields.

You can set cart metafields with the Storefront API or with Checkout UI Extensions.

**Info:** Only available for order metafield definitions.

The following example shows how to enable the cart to order copyable capability:

TOML:
```toml
[order.metafields.custom.gift_message]
name = "Gift Message"
type = "single_line_text_field"
capabilities.cart_to_order_copyable = true
```

GraphQL:
```graphql
mutation {
  metafieldDefinitionCreate(definition: {
    name: "Gift Message"
    namespace: "custom"
    key: "gift_message"
    type: "single_line_text_field"
    ownerType: ORDER
    capabilities: {
      cartToOrderCopyable: {
        enabled: true
      }
    }
  }) {
    createdDefinition {
      id
      name
      namespace
      key
      capabilities {
        cartToOrderCopyable {
          enabled
        }
      }
    }
    userErrors {
      field
      message
      code
    }
  }
}
```

---

## Query using metafields

> Fonte: https://shopify.dev/docs/apps/build/metafields/query-using-metafields

Use metafield values to find products, create automated collections, or search resources by specific criteria. This powerful querying capability turns your custom data into searchable, filterable attributes.

### Requirements

Before using metafields to query, filtering must be enabled on the metafield definition. Without filtering enabled, queries return unfiltered results.

* [Enable filtering](https://shopify.dev/docs/apps/build/metafields/use-metafield-capabilities#admin-filterable) through the API or in the Shopify admin.
* Not all metafield types or resources support filtering - see the [complete list](https://shopify.dev/docs/apps/build/metafields/use-metafield-capabilities#admin-filterable).

### Query syntax overview

The following query patterns are available, depending on the metafield [data type](https://shopify.dev/docs/apps/build/metafields/list-of-data-types):

| Pattern | Description |
| - | - |
| **Exact match** | Works for all types. Case-sensitive for text. Example: `color:"blue"` |
| **Prefix match** | Text types only. Use `*` wildcard. Example: `lapel_style:notch*` |
| **Exists** | Use `*` alone to match resources where the metafield has any value. Example: `color:*` |
| **NOT** | Use `-` or `NOT` to exclude matches. Use `-field:*` to find resources where a metafield has no value. Example: `-color:"blue"` |
| **Range** | Numeric and date types. Use `>`, `<`, `>=`, `<=`. Example: `price:>100` |
| **Boolean** | Use `true` or `false` without quotes. Example: `eco_friendly:true` |
| **Reference** | Use full GID format. Example: `collection:"gid://shopify/Collection/123"` |
| **List values** | Matches if ANY value in the list matches. Example: `tags:"organic"` |

Products, companies, and other core Shopify resources can be filtered by their metafield values using the GraphQL Admin API's [`query` parameter](https://shopify.dev/docs/api/usage/search-syntax).

The query format is `metafields.{namespace}.{key}:{query_value}`.

> **Info:** **Querying metaobjects:** These query patterns also work for metaobjects — just swap `metafields.namespace.key:` for `fields.field_name:`. See [Query metaobjects](https://shopify.dev/docs/apps/build/metaobjects/query-metaobjects) for examples.

### Query examples

The following examples demonstrate each query method with practical use cases. All requests are `POST https://{shop}.myshopify.com/api/{api_version}/graphql.json`.

#### Filter by text value

Finds all products with a color metafield set to "blue".

```graphql
query ProductsByColor {
  products(first: 10, query: "metafields.custom.color:\"blue\"") {
    edges {
      node {
        id
        title
        metafield(namespace: "custom", key: "color") {
          value
        }
      }
    }
  }
}
```

#### Filter by prefix match

Use the `*` wildcard to find resources where a string metafield starts with specific characters. Finds all products that start with "notch" as their lapel type on a custom suit.

```graphql
query NotchLapelProducts {
      products(first: 20, query: "metafields.custom.lapel_style:notch*") {
        edges {
          node {
            id
            title
            metafield(namespace: "custom", key: "lapel_style") {
              value
            }
          }
        }
      }
    }
```

#### Filter by numeric value

Numeric metafields support range queries using comparison operators. Finds companies with a minimum order value greater than $100.

```graphql
query CompaniesWithHighMinOrderValue {
      companies(
        first: 50
        query: "metafields.b2b.min_order_value:>100"
      ) {
        pageInfo {
          hasNextPage
        }
        edges {
          node {
            id
            name
            metafield(namespace: "b2b", key: "min_order_value") {
              id
              type
              value
            }
          }
        }
      }
    }
```

#### Filter by weight

Numeric metafields support range queries using comparison operators (`>`, `<`, `>=`, `<=`). For measurement types like weight, Shopify automatically converts between units. Queries products by weight using different units (kilograms, grams, pounds).

```graphql
query searchByWeightValue {
      weight_match_kg: products(first: 5, query: "metafields.$app.weight_field:>=1kg") {
        nodes {
          id
          metafield(namespace: "$app", key: "weight_field") { jsonValue }
        }
      }
      weight_match_g: products(first: 5, query: "metafields.$app.weight_field:<2000g") {
        nodes {
          id
          metafield(namespace: "$app", key: "weight_field") { jsonValue }
        }
      }
      weight_match_lb: products(first: 5, query: "metafields.$app.weight_field:>=4lb") {
        nodes {
          id
          metafield(namespace: "$app", key: "weight_field") { jsonValue }
        }
      }
    }
```

#### Filter by date range

Date metafields support range queries using comparison operators and can be combined with `AND` to filter within a specific date range. Finds all vintages of wines bottled between 2015 and 2018.

```graphql
query WinesBottledBetween2015And2018 {
      products(
        first: 10
        query: "metafields.custom.bottled_date:>=2015-01-01 AND metafields.custom.bottled_date:<=2018-12-31"
      ) {
        nodes {
          id
          title
          metafield(namespace: "custom", key: "bottled_date") {
            value
          }
        }
      }
    }
```

#### Filter by boolean value

Find all products that are marked as eco-friendly.

```graphql
query EcoFriendlyProducts {
  products(first: 50, query: "metafields.custom.eco_friendly:true") {
    edges {
      node {
        id
        title
        metafield(namespace: "custom", key: "eco_friendly") {
          value
        }
      }
    }
  }
}
```

#### Filter by date value

Date metafields support comparison operators for range queries. Finds products released after January 1, 2024.

```graphql
query ProductsByReleaseDate {
  products(first: 20, query: "metafields.custom.release_date:>2024-01-01") {
    edges {
      node {
        id
        title
        metafield(namespace: "custom", key: "release_date") {
          value
          type
        }
      }
    }
  }
}
```

#### Filter by reference

Reference metafields can be queried using the full Global ID (GID) of the referenced resource. Finds products that reference a specific collection.

```graphql
query ProductsByCollectionRef {
  products(first: 20, 
    query: "metafields.custom.featured_collection:\"gid://shopify/Collection/123456789\"") {
    edges {
      node {
        id
        title
        metafield(namespace: "custom", key: "featured_collection") {
          value
          reference {
            ... on Collection {
              id
              title
            }
          }
        }
      }
    }
  }
}
```

### Query list metafields

When querying list fields, the search matches if ANY value in the list equals the search term. This applies to all list types including text lists, reference lists, and multi-select fields.

#### Filter by list values

Find products that have a specific tag in a list of tags.

```graphql
query ProductsByTag {
  products(first: 20, 
    query: "metafields.custom.product_tags:\"sustainable\"") {
    edges {
      node {
        id
        title
        metafield(namespace: "custom", key: "product_tags") {
          value
          type
        }
      }
    }
  }
}
```

> **Important:** When querying multi-value metafields, the query matches if ANY value in the list matches the search term.

#### Filter by list references

Find products that reference a specific related product.

```graphql
query RelatedProducts {
  products(first: 20, 
    query: "metafields.custom.related_products:\"gid://shopify/Product/987654321\"") {
    edges {
      node {
        id
        title
        metafield(namespace: "custom", key: "related_products") {
          value
          references(first: 10) {
            edges {
              node {
                ... on Product {
                  id
                  title
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

### Combining multiple metafield queries

Build complex queries by combining multiple metafield conditions using AND/OR operators.

#### Combine multiple conditions

Find products that match multiple metafield criteria.

```graphql
query ComplexProductQuery {
  products(first: 20, 
    query: "metafields.custom.material:\"leather\" AND metafields.custom.eco_friendly:true") {
    edges {
      node {
        id
        title
        material: metafield(namespace: "custom", key: "material") {
          value
        }
        ecoFriendly: metafield(namespace: "custom", key: "eco_friendly") {
          value
        }
      }
    }
  }
}
```

#### Use range queries

Use multiple conditions with `AND` to filter within a value range. Finds products with sizes between 4 and 8.

```graphql
query ProductsWithOptions {
  products(first: 20, 
    query: "metafields.custom.dress_size:>4 AND metafields.custom.dress_size:<8") {
    edges {
      node {
        id
        title
        metafield(namespace: "custom", key: "size") {
          value
        }
      }
    }
  }
}
```

### Troubleshooting common query issues

If your metafield queries aren't working as expected, check these common issues and their solutions. Most problems stem from missing configuration, incorrect syntax, or misunderstanding how different metafield types handle query values.

#### Issue: Query returns all products/metaobjects instead of filtered results

**Problem:** Your query isn't filtering results as expected, returning all items instead of just those matching your metafield criteria.

**Solution:** Ensure the metafield has filtering enabled.

```graphql
mutation EnableFiltering {
  metafieldDefinitionUpdate(
    definition: {
      namespace: "custom"  # Replace with your namespace
      key: "material"      # Replace with your metafield key
      ownerType: PRODUCT   # Replace with appropriate owner type
      capabilities: {
        adminFilterable: {
          enabled: true
        }
      }
    }
  ) {
    updatedDefinition {
      id
      namespace
      key
      capabilities {
        adminFilterable {
          enabled
        }
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

#### Issue: "Invalid query" or syntax errors

**Problem:** Your query string may have incorrect syntax.

**Common mistakes and fixes:**

1. **Missing quotes around values:**
   * Wrong: `metafields.custom.color:blue`
   * Correct: `metafields.custom.color:\"blue\"`
2. **Incorrect namespace/key separator:**
   * Wrong: `metafields.custom:material:\"cotton\"`
   * Correct: `metafields.custom.material:\"cotton\"`
3. **Wrong syntax for metaobjects:**
   * Wrong: `metafields.color:\"blue\"`
   * Correct: `fields.color:\"blue\"`

#### Issue: Multi-value metafield queries not working

**Problem:** Queries against list fields return unexpected results.

**Solution:** Remember that multi-value queries match if ANY value in the list matches:

```graphql
# If a product has tags: ["sustainable", "organic", "cotton"]
# This query will match:
query {
  products(first: 10, query: "metafields.custom.tags:\"organic\"") {
    # Returns products with "organic" anywhere in the tags list
  }
}
```

#### Issue: Boolean metafield queries not working

**Solution:** Try using lowercase `true` or `false` without quotes:

```graphql
query {
  products(first: 10, query: "metafields.custom.is_featured:true") {
    # Note: no quotes around true/false
  }
}
```

#### Issue: Reference field queries failing

**Solution:** Try using the full GID (Global ID) format:

```graphql
query {
  products(first: 10, 
    query: "metafields.custom.related_collection:\"gid://shopify/Collection/123456789\"") {
    # Must use full GID format
  }
}
```

#### Issue: Case sensitivity problems

**Solution:** Metafield queries are case-sensitive. Ensure exact matching:

```graphql
query CaseSensitive {
  # Won't match "Cotton" or "COTTON"
  lowercase_only: products(first: 10, query: "metafields.custom.material:\"cotton\"") { nodes { id } }
  
  # To handle case variations, use multiple OR conditions:
  case_variants: products(first: 10, query: "metafields.custom.material:\"cotton\" OR metafields.custom.material:\"Cotton\"") { nodes { id } }
}
```

#### Issue: Special characters in query values

**Solution:** Escape special characters properly:

```graphql
# For values with quotes, escape them:
query SpecialChars {
  products(first: 10, 
    query: "metafields.custom.description:\"24\\\" monitor\"") {
    # Note the escaped quote: \\\"
  }
}
```

### Best Practices for Metafield Queries

1. **Always enable filtering first:** Before attempting queries, ensure the metafield definition has `adminFilterable` enabled.
2. **Test with simple queries:** Start with basic single-field queries before combining multiple conditions.
3. **Use GraphiQL for testing:** Test your queries in the GraphiQL explorer before implementing in code.
4. **Paginate large result sets:** Use cursor-based pagination for better performance:

```graphql
query PaginatedQuery($cursor: String) {
  products(first: 50, after: $cursor, 
    query: "metafields.custom.category:\"electronics\"") {
    edges {
      node {
        id
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

5. **Monitor query performance:** Complex metafield queries can be slower than standard field queries. Consider caching results when appropriate.

### Next steps

* Learn how to [enable filtering and other advanced features](https://shopify.dev/docs/apps/build/metafields/use-metafield-capabilities).
* Learn how to [query metaobjects](https://shopify.dev/docs/apps/build/metaobjects/query-metaobjects).
* Learn how to [work with metafield definitions](https://shopify.dev/docs/apps/build/metafields/definitions).

---

## Conditional metafield definitions

> Fonte: https://shopify.dev/docs/apps/build/metafields/conditional-metafield-definitions

Constraints allow metafield definitions to be applied to a subset of resources.

### How it works

By default, metafield definitions apply to every resource on their owner type. For example, `Product` metafield definitions apply to all products and appear on all product detail pages in the Shopify admin.

However, some metafield definitions should only apply to a subset of resources. For example, `Shoe size` is a valid metafield for `Shoes` products but wouldn't apply to `Sweaters`.

Metafield definition constraints provide a way to conditionally apply definitions based on the characteristics of a resource. For example, each standard [category metafield](https://help.shopify.com/manual/custom-data/metafields/category-metafields) comes with a set of constraints, which determine what product categories the metafield applies to.

At the core of the conditional metafields system are constraint subtypes. Constraint subtypes are `key | value` pairs that identify a "subtype" of a metafield owner type.

For example, because `gid://shopify/TaxonomyCategory/aa-8` is the ID of the `Shoes` product category, the `Shoes` constraint subtype is identified by:

```text
{
key: "category",
value: "gid://shopify/TaxonomyCategory/aa-8,
}
```

Currently, Shopify only supports constraint subtypes that correspond to product categories on `Product` metafield definitions. These constraint subtypes all have a `key` equal to `category`.

### Examples

#### Find product category IDs for constraints inputs

You might want to create a custom `Shoelace material` conditional metafield that applies to `Shoes` and the children categories of `Shoes`, such as `Boots` and `Sneakers`.

You need to determine the IDs of the `Shoes` category and its children. This data can be extracted directly from our [product-taxonomy repository](https://shopify.github.io/product-taxonomy/releases/latest/).

Alternatively, you can determine taxonomy category IDs using the GraphQL Admin API. For example, if you know that the ID for `Shoes` is `gid://shopify/TaxonomyCategory/aa-8`, then you can find the IDs for the children of `Shoes` using the following query:

```graphql
query ShoesChildrenIds {
  taxonomy {
    categories(first: 250, childrenOf: "gid://shopify/TaxonomyCategory/aa-8") {
      nodes {
        name
        id
      }
    }
  }
}
```

JSON response:

```json
{
  "taxonomy": {
    "categories": {
      "nodes": [
          { "name": "Athletic Shoes", "id": "gid://shopify/TaxonomyCategory/aa-8-1" },
          { "name": "Heels", "id": "gid://shopify/TaxonomyCategory/aa-8-10" },
          { "name": "Baby & Toddler Shoes", "id": "gid://shopify/TaxonomyCategory/aa-8-2" },
          { "name": "Boots", "id": "gid://shopify/TaxonomyCategory/aa-8-3" },
          { "name": "Sandals", "id": "gid://shopify/TaxonomyCategory/aa-8-6" },
          { "name": "Slippers", "id": "gid://shopify/TaxonomyCategory/aa-8-7" },
          { "name": "Sneakers", "id": "gid://shopify/TaxonomyCategory/aa-8-8" },
          { "name": "Flats", "id": "gid://shopify/TaxonomyCategory/aa-8-9" }
        ]
      }
    }
  }
}
```

#### Create a custom conditional metafield definition

You can then use the `constraints` field on `metafieldDefinitionCreate` to create the conditional metafield.

```graphql
mutation CreateMetafieldDefinition($definition: MetafieldDefinitionInput!) {
  metafieldDefinitionCreate(definition: $definition) {
    createdDefinition {
      name
      ownerType
      namespace
      key
      constraints {
        key
        values(first: 10) {
          nodes {
            value
          }
        }
      }
    }
  }
}
```

Variables:

```json
{
  "definition": {
    "name": "Shoelace material",
    "namespace": "custom",
    "key": "shoelace_material",
    "type": "single_line_text_field",
    "ownerType": "PRODUCT",
    "constraints": {
      "key": "category",
      "values": [
        "gid://shopify/TaxonomyCategory/aa-8",
        "gid://shopify/TaxonomyCategory/aa-8-1",
        "gid://shopify/TaxonomyCategory/aa-8-2",
        "gid://shopify/TaxonomyCategory/aa-8-3",
        "gid://shopify/TaxonomyCategory/aa-8-6",
        "gid://shopify/TaxonomyCategory/aa-8-7",
        "gid://shopify/TaxonomyCategory/aa-8-8",
        "gid://shopify/TaxonomyCategory/aa-8-9",
        "gid://shopify/TaxonomyCategory/aa-8-10"
      ]
    }
  }
}
```

#### Add & remove constraints on a metafield definition

If you would like to edit the constraints of a metafield definition, you can use the `constraintsUpdates` field on `metafieldDefinitionUpdate`.

The `constraintsUpdates` field handles both the creation and deletion of constraints. For example, you might realize that `Shoelace material` doesn't make sense on your `Flats` products because `Flats` don't have shoelaces. You might have also started selling a line of `Shoelaces` products and would like to track the `Shoelace material` of these new products.

The following example shows how you could update the `Shoelace material` metafield so that it is no longer constrained to `Flats` but is added to `Shoelaces`.

**Note:** If constraints already exist on the definition, then the `key` field is optional. If you're adding constraints to a definition that was previously unconstrained, then `key` must be included.

```graphql
mutation UpdateMetafieldDefinition($definition: MetafieldDefinitionUpdateInput!) {
  metafieldDefinitionUpdate(definition: $definition) {
    updatedDefinition {
      name
      ownerType
      namespace
      key
      constraints {
        key
        values(first: 10) {
          nodes {
            value
          }
        }
      }
    }
  }
}
```

Variables:

```json
{
  "definition": {
    "namespace": "custom",
    "key": "shoelace_material",
    "ownerType": "PRODUCT",
    "constraintsUpdates": {
      "values": [
        { "delete": "gid://shopify/TaxonomyCategory/aa-8-9" },
        { "create": "gid://shopify/TaxonomyCategory/aa-7-6" }
      ]
    }
  }
}
```

#### Unconstrain a metafield definition

If you no longer want a definition to be constrained, then you can also use the `constraintsUpdates` field to remove all of the definition's constraints. The constraints can be identified individually or you can set both the `key` and `values` fields to `null` to delete all constraints.

If a definition is unconstrained, then the definition applies to all resources and appears on all resource pages in the Shopify admin.

```graphql
mutation UpdateMetafieldDefinition($definition: MetafieldDefinitionUpdateInput!) {
  metafieldDefinitionUpdate(definition: $definition) {
    updatedDefinition {
      name
      ownerType
      namespace
      key
      constraints {
        key
        values(first: 10) {
          nodes {
            value
          }
        }
      }
    }
  }
}
```

Variables:

```json
{
  "definition": {
    "namespace": "custom",
    "key": "shoelace_material",
    "ownerType": "PRODUCT",
    "constraintsUpdates": {
      "key": null,
      "values": null
    }
  }
}
```

#### Query for metafield definitions based on constraints

The `constraintSubtype` and `constraintStatus` arguments can be used to filter metafield definitions queries based on constraints.

The `constraintSubtype` argument returns only metafield definitions that apply to the identified subtype. Metafield definitions are applicable to a constraint subtype if one of the following criteria is met:

* The metafield definition has a constraint matching the `constraintSubtype`.
* The metafield definition does not have any constraints, which means the definition applies to all constraint subtypes.

The `constraintStatus` argument filters metafields based on whether they are constrained or unconstrained. `constraintStatus` accepts the following values:

* `CONSTRAINED_ONLY`
* `UNCONSTRAINED_ONLY`
* `CONSTRAINED_AND_UNCONSTRAINED`

`constraintSubtype` and `constraintStatus` can also be used on the `standardMetafieldDefinitionTemplates` query in order to query metafield standard templates based on their constraints.

```graphql
query NecklaceMetafieldDefinitions {
  metafieldDefinitions(
    first: 5,
    ownerType: PRODUCT,
    constraintSubtype: {
      key: "category",
      value: "gid://shopify/TaxonomyCategory/aa-6-8"
    },
    constraintStatus: CONSTRAINED_ONLY
  ) {
    edges {
      node {
        name
        namespace
        key
      }
    }
  }
}
```

JSON response:

```json
{
  "metafieldDefinitions": {
    "edges": [
      { "node": { "name": "Color", "namespace": "shopify", "key": "color-pattern" } },
      { "node": { "name": "Target gender", "namespace": "shopify", "key": "target-gender" } },
      { "node": { "name": "Age group", "namespace": "shopify", "key": "age-group" } },
      { "node": { "name": "Jewelry material", "namespace": "shopify", "key": "jewelry-material" } },
      { "node": { "name": "Jewelry type", "namespace": "shopify", "key": "jewelry-type" } }
    ]
  }
}
```

---

## Working with custom IDs

> Fonte: https://shopify.dev/docs/apps/build/metafields/working-with-custom-ids

You can create custom IDs when you need a reliable unique identifier to match resources across multiple shops and/or systems (e.g. ERPs, CRMs, PIMs). This guide shows you how to create and manage custom IDs using Metafields in the GraphQL Admin API.

### Who is this for

Any developer who uses external systems (e.g., PIM, ERP) and wants to create a mapping of identifiers to manage data migration and synchronization with Shopify.

### Requirements

* Your app can make [authenticated requests](https://shopify.dev/docs/api/admin-graphql#authentication) to the GraphQL Admin API.
* You have access to the type of resource that you want to add the metafield on. For example, setting a metafield on a `PRODUCT` requires the same access as mutating a product.

### Limitations

* ID metafield types are automatically configured to have unique values.
* Look up by custom ID is not available for all resource types. It is currently supported for: Products, Product Variants, Collections, Customers, Orders, Locations.
* Create or update by custom ID is not available for all reference types. It is currently supported for:
  * Products (with `productSet` or `productUpdate`)
  * Customers (with `customerSet`)

  **Note:** Look up by custom ID is only available using the GraphQL Admin API.

### Step 1: Create an id metafield definition

You can create an ID metafield definition using the GraphQL Admin API's `createMetafieldDefinition` mutation.

The following example creates a pinned `id` metafield definition for the product owner type:

```graphql
mutation CreateMetafieldDefinition($definition: MetafieldDefinitionInput!) {
  metafieldDefinitionCreate(definition: $definition) {
    createdDefinition {
      id
      name
      namespace
      key
    }
    userErrors {
      field
      message
      code
    }
  }
}
```

Variables:

```json
{
  "definition": {
    "name": "My Custom ID",
    "namespace": "custom",
    "key": "id",
    "description": "An custom ID field",
    "type": "id",
    "ownerType": "PRODUCT",
    "pin": true
  }
}
```

### Step 2: Add an `id` metafield to a new resource

Add a metafield to the corresponding resource type using the id type with the namespace and key for your definition.

```graphql
mutation createProductMetafields($input: ProductInput!) {
  productCreate(input: $input) {
    product {
      id
      metafields(first: 3) {
        edges {
          node {
            namespace
            key
            value
          }
        }
      }
    }
    userErrors {
      message
      field
    }
  }
}
```

Variables:

```json
{
  "input": {
    "metafields": [
      { "namespace": "custom", "key": "id", "value": "1234" }
    ],
    "title": "Nike shoes"
  }
}
```

### Step 3 (Optional): Add an `id` metafield to an existing resource

Add a metafield to the corresponding resource type using the `id` type with the namespace and key from your definition.

```graphql
mutation updateProductMetafields($input: ProductInput!) {
  productUpdate(input: $input) {
    product {
      id
      metafields(first: 3) {
        edges {
          node {
            id
            namespace
            key
            value
          }
        }
      }
    }
    userErrors {
      message
      field
    }
  }
}
```

Variables:

```json
{
  "input": {
    "metafields": [
      { "namespace": "custom", "key": "id", "value": "1234" }
    ],
    "title": "Nike shoes"
  }
}
```

### Step 4: Look up the resource by the Custom ID

After you've added the Custom ID metafield to a resource, you can look up that resource by its custom ID. Here are some examples of available GraphQL Admin API queries:

* If you've created a product metafield definition, then use the [`productByIdentifier`](https://shopify.dev/docs/api/admin-graphql/latest/queries/productByIdentifier) query.
* If you've created a customer metafield definition, then use the [`customerByIdentifier`](https://shopify.dev/docs/api/admin-graphql/latest/queries/customerByIdentifier) query.
* If you've created an order metafield definition, then use the [`orderByIdentifier`](https://shopify.dev/docs/api/admin-graphql/latest/queries/orderByIdentifier) query.

Similar `ByIdentifier` queries are available for other supported resource types like collections and product variants.

The following example looks up a product by the Custom ID:

```graphql
query findProduct {
  productByIdentifier(identifier: {customId: {
    namespace:"custom", key:"id", value:"1234"
  }}) {
    title
    handle
  }
}
```

### Step 5: Mutate a resource with a Custom ID

You can also update or create some resources by referencing their custom ID. This is available for products via the `productSet` and `productUpdate` mutations, and customers via `customerSet`.

* **`productSet`**: When the `identifier` argument includes a custom ID, it first looks up a matching record. If one exists, the mutation updates it. Otherwise, it attempts to create a new record with the provided inputs.
* **`productUpdate`**: When the `identifier` argument includes a custom ID, it looks up a matching record and updates it. Unlike `productSet`, it doesn't create a new product if no match is found.

The following example looks up a product using the custom ID format from Step 4 and updates its title using `productSet`:

```graphql
mutation updateProduct {
  productSet(input: {title: "Nike running shoes"},
    identifier: {
      customId: {
        namespace: "custom",
        key: "id",
        value: "1234"
      }
    }
  ) {
    product {
      title
      handle
    }
  }
}
```

The following example demonstrates how `productUpdate` updates a product when it's identified by its custom ID:

```graphql
mutation updateProductByCustomId {
  productUpdate(
    product: {title: "Nike running shoes"},
    identifier: {
      customId: {
        namespace: "custom",
        key: "id",
        value: "1234"
      }
    }
  ) {
    product {
      title
      handle
    }
    userErrors {
      field
      message
    }
  }
}
```

The following example demonstrates how `productSet` creates a new product when the Custom ID doesn't match existing products:

```graphql
mutation createProduct {
  productSet(input: {title: "Nike sweatshirt"},
    identifier: {
      customId: {
        namespace: "custom",
        key: "id",
        value: "5678"
      }
    }
  ) {
    product {
      title
      handle
    }
  }
}
```

---

## Metafield limits

> Fonte: https://shopify.dev/docs/apps/build/metafields/metafield-limits

This document outlines the various limits for metafields and their definitions per shop, including apps.

### Metafield definition limits

**Note:** Standard metafield definitions don't count towards limits unless specified.

#### App definitions

Each app installed on a shop can create up to 256 metafield definitions per resource type.

#### Merchant definitions

Merchants can create up to 256 metafield definitions per resource type.

#### Other limits

| Limit type | Limit |
| - | - |
| Pinned definitions limit per resource type | 20 |

### Metafield type size limits

**Info:** Apps using JSON fields before April 1, 2026 will be grandfathered at the current 2MB limit. New apps requiring >128KB JSON fields may request an exception via a Shopify form.

Most metafield types have a 64KB (65,536 bytes) size limit, with the following exceptions:

| Type | Size limit |
| - | - |
| `id` | 2KB |
| `json` | 128KB |
| `url` | 2KB |

**Note:** Single line text metafield predefined choices are limited to 128 values.

### Lists type limits

All [list types](https://shopify.dev/docs/apps/build/metafields/list-of-data-types#list-types) have a maximum of 128 items except metaobject references, which support up to 256 items.

**Note:**

* Each item in the list has the same size limits as its corresponding single value type. For example, each text field in a `list.single_line_text_field` can store up to 64KB (65,536 bytes).
* You can use the `list.min` and `list.max` validations through the GraphQL Admin API to set custom minimum and maximum limits for the number of items in a list, as long as they don't exceed the maximum size limits.

### Metafield definition capability limits

| Limit type | Limit |
| - | - |
| Used to power smart collections | 128 |
| Use as admin filter on Products, Companies, Company Locations, or Metaobjects | 50 |
| Use as admin filter on Orders | 5 |

**Note:** Metafield definition capabilities extend metafield functionality. Learn more about [metafield capabilities](https://shopify.dev/docs/apps/build/metafields/use-metafield-capabilities).

---

# Metaobjects

---

## About metaobjects

> Fonte: https://shopify.dev/docs/apps/build/metaobjects (canonical: https://shopify.dev/docs/apps/build/custom-data/metaobjects)

Metaobjects enable you to define custom data structures with multiple related fields. While metafields add individual custom fields to existing Shopify resources, metaobjects let you create entirely new types of structured data that can be referenced and reused across your store.

You can use metaobjects to, for example, create product size charts with multiple measurements, author profiles with biographical information and contact details, ingredient lists with nutritional data, or warranty information with terms and conditions. This flexibility allows you to model complex data relationships and create rich content structures.

**Info:**

Metaobjects create complex data structures with multiple related fields.

* Need to add a single custom field to an existing Shopify resource? Use [metafields](https://shopify.dev/docs/apps/build/metafields) instead.
* For a deep dive on how to structure your data using both tools, see [Data modeling with metafields and metaobjects](https://shopify.dev/docs/apps/build/metaobjects/data-modeling-with-metafields-and-metaobjects).

Want to skip ahead? Choose a path based on what you're building:

* **Building an app**: Use [app-owned metaobjects](#app-owned-metaobjects) with TOML configuration.
* **Extending store content**: Use [merchant-owned metaobjects](#merchant-owned-metaobjects) with GraphQL.

### What is a metaobject?

A metaobject is an instance of structured data with multiple related field values. Unlike [metafields](https://shopify.dev/docs/apps/build/metafields) that attach single values to existing resources, metaobjects are standalone entities that can be referenced from multiple resources.

Each metaobject contains:

* **ID**: Unique identifier assigned by Shopify.
* **Handle**: URL-friendly identifier (auto-generated from display name, or custom).
* **Display name**: Human-readable name (auto-generated from a specified field).
* **Field values**: Data defined by its metaobject definition.
* **Capability states**: Optional states like published/unpublished (if enabled).

For example, an author metaobject might include a name, biography, email, and profile photo - all stored together as a single reusable entity.

#### Metaobject definitions

Before creating metaobjects, you create a metaobject definition. Metaobject definitions are schemas that specify the structure, fields, and rules for a metaobject type.

A definition establishes:

* **Type identifier**: The category name for your custom object (for example, `$app:author` or `size_chart`). This identifies what kind of metaobject entries you'll create.
* **Fields**: What data the metaobject stores (name, key, data type, validation rules).
* **Access permissions**: Who can edit and where entries can be accessed (Shopify admin, storefront).
* **Capabilities**: Optional features like publishable or renderable.
* **Display configuration**: How entries appear (field order, display name field).

The relationship is: one definition can have many metaobject instances (entries). For example, one "author" definition can have metaobjects for Jane Smith, John Doe, and other individual authors.

#### Metaobject ownership

Ownership determines access and control. When creating metaobjects, you choose between two ownership models:

| **Ownership Type** | **Purpose** | **Type prefix** |
| - | - | - |
| App-owned | App-managed entries for features, configurations, and content | Use reserved prefix `$app` (GraphQL) or `app` (TOML) |
| Merchant-owned | Merchant-managed content shared across all apps | Use any non-reserved prefix, such as `custom` |

**Additional ownership types:**

* **Shopify-reserved**: Standard metaobject definitions for platform features. Shopify controls the structure, but merchants typically own and manage the entries. Developers don't create these but can enable [standard definitions](https://shopify.dev/docs/apps/build/metaobjects/list-of-standard-definitions) for certain use cases like product reviews.

### App-owned metaobjects

App-owned metaobjects are custom data structures that are managed by your app. These metaobject entries are used for features requiring multiple related fields, such as configuration panels, content templates, or complex product attributes.

App-ownership is defined using the `app` reserved type prefix and can be created using your app's `shopify.app.toml` file.

**Info:** App-owned metaobject entries are viewable by default in the Shopify admin. Edit access can be configured using the [`access.admin`](#shopify-admin-permissions) setting.

#### Example

You want to create author profiles with biographical information that can be referenced from blog posts. Because you want your app to own and control the structure, you create an app-owned metaobject.

##### Step 1: Create a metaobject definition

Create the metaobject definition using your app's `shopify.app.toml` file. The following creates the definition with app-owned prefix `app` and type identifier `author`:

```toml
[metaobjects.app.author]
name = "Author"
access.admin = "merchant_read_write"
access.storefront = "public_read"


[metaobjects.app.author.fields.full_name]
name = "Full Name"
type = "single_line_text_field"


[metaobjects.app.author.fields.bio]
name = "Biography"
type = "multi_line_text_field"


[metaobjects.app.author.fields.email]
name = "Email"
type = "single_line_text_field"


[metaobjects.app.author.fields.photo]
name = "Profile Photo"
type = "file_reference"
```

Deploy it with your app:

```bash
shopify app deploy
```

##### Step 2: Create the metaobjects

After you create the metaobject definition, create metaobjects (entries) using the GraphQL Admin API. Use the same type identifier and field keys as your definition:

```graphql
mutation CreateAuthor {
  metaobjectCreate(metaobject: {
    type: "$app:author"
    fields: [
      { key: "full_name", value: "Jane Smith" }
      { key: "bio", value: "Award-winning author with 20 years of experience..." }
      { key: "email", value: "jane@example.com" }
      { key: "photo", value: "gid://shopify/MediaImage/123" }
    ]
  }) {
    metaobject {
      id
      handle
      displayName
      fields {
        key
        value
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

### Merchant-owned metaobjects

Merchant-owned metaobjects are custom data structures that can be managed in the Shopify admin or through any installed app. These metaobject entries are ideal for content that should be accessible and editable through the admin interface or multiple apps.

Merchant-ownership is defined by using any [non-reserved type](#metaobject-ownership) and can be created using the GraphQL Admin API.

**Info:** Merchant-owned metaobjects must be created using GraphQL. TOML configuration only creates app-owned metaobjects.

#### Example

You want to add size chart information to products. Because this type of structured data should be managed in the Shopify admin and accessible to all apps, you use a merchant-owned metaobject.

##### Step 1: Create the metaobject definition

Create the metaobject definition using GraphQL. The following creates the definition with type identifier `size_chart` (no prefix makes it merchant-owned):

```graphql
mutation CreateSizeChartDefinition {
  metaobjectDefinitionCreate(definition: {
    type: "size_chart"
    name: "Size Chart"
    description: "Product sizing information"
    access: {
      storefront: PUBLIC_READ
    }
    fieldDefinitions: [
      { key: "size", name: "Size", type: "single_line_text_field" }
      { key: "chest_inches", name: "Chest (inches)", type: "number_decimal" }
      { key: "waist_inches", name: "Waist (inches)", type: "number_decimal" }
      { key: "length_inches", name: "Length (inches)", type: "number_decimal" }
    ]
  }) {
    metaobjectDefinition {
      id
      type
      name
      fieldDefinitions {
        key
        name
        type { name }
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

##### Step 2: Create the metaobjects

Create metaobjects (entries) for specific size charts:

```graphql
mutation CreateSizeChartEntry {
  metaobjectCreate(metaobject: {
    type: "size_chart"
    fields: [
      { key: "size", value: "Medium" }
      { key: "chest_inches", value: "38" }
      { key: "waist_inches", value: "32" }
      { key: "length_inches", value: "29" }
    ]
  }) {
    metaobject {
      id
      handle
      displayName
      fields {
        key
        value
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

### Permissions

Configure who can read and write your metaobjects using the `access` settings on your definition.

#### Shopify admin permissions

`admin` controls permissions for both the Shopify admin and the GraphQL Admin API.

**For app-owned metaobjects:**

```toml
# Merchants can view but not edit (default)
access.admin = "merchant_read"

# Merchants can view and edit
access.admin = "merchant_read_write"
```

```graphql
access: {
  admin: MERCHANT_READ  # view only (default)
}

access: {
  admin: MERCHANT_READ_WRITE  # view and edit
}
```

**For merchant-owned metaobjects:**

* Always full access - readable and writable by merchants and all apps with appropriate scopes. No configuration needed.

#### Storefront permissions

`storefront` controls permissions for the Storefront API (used by headless and custom storefronts).

**Available settings:**

```toml
# Not accessible on storefront (default)
access.storefront = "none"

# Accessible via Storefront API
access.storefront = "public_read"
```

```graphql
access: {
  storefront: NONE  # not accessible (default)
}

access: {
  storefront: PUBLIC_READ  # accessible via Storefront API
}
```

> **Note (Liquid access):** All metaobjects are always available in Liquid templates and the online store editor, regardless of the `access.storefront` setting. The storefront access setting only governs the Storefront API (used by headless and custom storefronts).

### Use in Shopify Functions

You can query app-owned metaobjects directly in [function input queries](https://shopify.dev/docs/apps/build/functions/input-queries/metafields-for-input-queries). This works across all function types, including discounts, cart transforms, delivery customization, and fulfillment constraints.

The type must use the `$app` reserved prefix (for example, `$app:pricing-config`). Merchant-owned types don't work in function input queries.

Each `metaobject` root costs 1 complexity point, and each `field(key:)` call costs 3 points. A query with one metaobject and three fields costs 10 points total. The input query budget is 30 points. For the full cost breakdown, refer to [input query limits](https://shopify.dev/docs/api/functions/latest#input-query-limits).

### Next steps

* Learn how to [model your data structure](https://shopify.dev/docs/apps/build/metaobjects/data-modeling-with-metafields-and-metaobjects).
* Learn how to [work with metaobject definitions](https://shopify.dev/docs/apps/build/metaobjects/manage-metaobject-definitions).
* Learn how to [work with metaobject entries](https://shopify.dev/docs/apps/build/metaobjects/manage-metaobjects).
* Learn how to use metaobjects to [query entries](https://shopify.dev/docs/apps/build/metaobjects/query-metaobjects).
* Learn how to [enable advanced features](https://shopify.dev/docs/apps/build/metaobjects/use-metaobject-capabilities).
* Learn how to use app-owned metaobjects in [function input queries](https://shopify.dev/docs/apps/build/functions/input-queries/metafields-for-input-queries).

---

## Manage metaobject definitions

> Fonte: https://shopify.dev/docs/apps/build/metaobjects/manage-metaobject-definitions

Metaobject definitions are schemas that specify the structure, fields, and rules for metaobject types. This guide shows you how to create, read, update, and delete metaobject definitions using TOML configuration or the GraphQL Admin API.

**Tip:** Not sure how to structure your data? See [Data modeling with metafields and metaobjects](https://shopify.dev/docs/apps/build/metaobjects/data-modeling-with-metafields-and-metaobjects) for a translation guide from SQL concepts to Shopify's architecture.

### Requirements

* Your app can make [authenticated requests](https://shopify.dev/docs/api/usage/authentication) to the GraphQL Admin API.
* Your app has the `read_metaobject_definitions` and `write_metaobject_definitions` [access scopes](https://shopify.dev/docs/api/usage/access-scopes).

### Creating definitions

There are two ways to set up metaobject definitions:

* **TOML**: TOML configurations in `shopify.app.toml` create app-owned definitions. Your app maintains control while optionally allowing edits in the Shopify admin.
* **GraphQL**: The GraphQL Admin API provides programmatic control for creating merchant-owned metaobjects (editable in the Shopify admin and accessible to all installed apps) and dynamically generating definitions based on user configuration.

#### TOML (app-owned) example

This example creates an app-owned metaobject definition for author profiles. Because the app controls the author data structure, it uses the app's TOML configuration file to ensure that the definition is consistently deployed across all installations.

```toml
[metaobjects.app.author]
name = "Author"
access.admin = "merchant_read_write"
access.storefront = "public_read"


[metaobjects.app.author.fields.full_name]
name = "Full Name"
type = "single_line_text_field"


[metaobjects.app.author.fields.bio]
name = "Biography"
type = "multi_line_text_field"


[metaobjects.app.author.fields.email]
name = "Email"
type = "single_line_text_field"


[metaobjects.app.author.fields.photo]
name = "Profile Photo"
type = "file_reference"
```

Deploy the changes with your app:

```bash
shopify app deploy
```

**Benefits of TOML:**

* Definitions are version-controlled as part of your app.
* Automatic creation and updates on deploy.
* Works with `shopify app dev` to safely test out changes.
* Consistent across all shops - when you update your app's data structure, it deploys to every installation automatically.
* The app maintains ownership.

#### GraphQL Admin API example

These examples show how to create metaobject definitions using GraphQL. The first creates a merchant-owned definition that all apps can access. The second creates an app-owned definition that only your app controls.

##### Merchant-owned (editable in Shopify admin)

```graphql
# POST https://{shop}.myshopify.com/api/{api_version}/graphql.json

mutation CreateSizeChartDefinition {
  metaobjectDefinitionCreate(definition: {
    type: "size_chart"
    name: "Size Chart"
    description: "Product sizing information"
    access: {
      storefront: PUBLIC_READ
    }
    fieldDefinitions: [
      { key: "size", name: "Size", type: "single_line_text_field", required: true }
      { key: "chest_inches", name: "Chest (inches)", type: "number_decimal" }
      { key: "waist_inches", name: "Waist (inches)", type: "number_decimal" }
    ]
  }) {
    metaobjectDefinition {
      id
      type
      name
      fieldDefinitions {
        key
        name
        type { name }
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

##### App-owned (app controlled)

```graphql
# POST https://{shop}.myshopify.com/api/{api_version}/graphql.json

mutation CreateAppOwnedDefinition {
  metaobjectDefinitionCreate(definition: {
    type: "$app:warranty_info"
    name: "Warranty Information"
    description: "Extended warranty details"
    access: {
      admin: MERCHANT_READ_WRITE
      storefront: PUBLIC_READ
    }
    fieldDefinitions: [
      { key: "coverage_period", name: "Coverage Period", type: "single_line_text_field" }
      { key: "terms", name: "Terms and Conditions", type: "multi_line_text_field" }
    ]
  }) {
    metaobjectDefinition {
      id
      type
      name
    }
    userErrors {
      field
      message
    }
  }
}
```

Key differences:

* **Merchant-owned**: Use a simple type name without any prefix (like `size_chart` or `author`). This provides full control over both the definition and entries in the Shopify admin. `access.admin` isn't required. Only `access.storefront` is used to control customer visibility.
* **App-owned**: Use the reserved `$app:` prefix in the type. The app controls the definition. Use `access.admin` to grant merchant write permissions for the entries.

**Use GraphQL when:**

* Merchants define their own custom metaobjects through your app's UI.
* Field structure varies per merchant or changes frequently.
* Building form builders, CMS-like tools, or content managers.
* You're creating merchant-owned metaobjects that other apps can access.

#### Dynamic definition creation example

This example shows how to programmatically create definitions based on user input, such as in a content manager app where custom metaobject types are configured through your app's UI.

Your app would collect metaobject configuration (using a form or UI), validate the input, construct the variables object, and then execute the mutation.

```graphql
mutation CreateDynamicMetaobject($input: MetaobjectDefinitionCreateInput!) {
  metaobjectDefinitionCreate(definition: $input) {
    metaobjectDefinition {
      id
      name
      type
      fieldDefinitions {
        key
        name
        type { name }
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

Variables:

```json
{
  "input": {
    "type": "custom_content_block",
    "name": "Custom Content Block",
    "description": "User-defined content block",
    "fieldDefinitions": [
      { "key": "title", "name": "Title", "type": "single_line_text_field" },
      { "key": "content", "name": "Content", "type": "rich_text_field" }
    ]
  }
}
```

### Reading definitions

Query metaobject definitions to retrieve their structure and configuration.

#### Querying all definitions

```graphql
query GetAllDefinitions {
  metaobjectDefinitions(first: 50) {
    edges {
      node {
        id
        type
        name
        description
        access {
          admin
          storefront
        }
        fieldDefinitions {
          key
          name
          type { name }
          required
        }
      }
    }
  }
}
```

#### Querying a specific definition by type

```graphql
query GetDefinitionByType {
  metaobjectDefinitionByType(type: "size_chart") {
    id
    type
    name
    description
    fieldDefinitions {
      key
      name
      type { name }
      required
      validations {
        name
        value
      }
    }
    access {
      admin
      storefront
    }
  }
}
```

### Updating definitions

Modify existing definitions to add fields, update access, or change configuration. To update definitions declared in TOML, simply update the configuration file, test with `shopify app dev` and deploy a new version of your app.

#### Updating name and description

```graphql
mutation UpdateDefinitionDetails {
  metaobjectDefinitionUpdate(
    id: "gid://shopify/MetaobjectDefinition/123"
    definition: {
      name: "Updated Size Chart"
      description: "Comprehensive sizing information for all products"
    }
  ) {
    metaobjectDefinition {
      id
      name
      description
    }
    userErrors {
      field
      message
    }
  }
}
```

#### Adding a new field

```graphql
mutation AddFieldToDefinition {
  metaobjectDefinitionUpdate(
    id: "gid://shopify/MetaobjectDefinition/123"
    definition: {
      fieldDefinitions: [
        { key: "hip_inches", name: "Hip (inches)", type: "number_decimal" }
      ]
    }
  ) {
    metaobjectDefinition {
      id
      fieldDefinitions {
        key
        name
        type { name }
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

#### Updating access permissions

```graphql
mutation UpdateDefinitionAccess {
  metaobjectDefinitionUpdate(
    id: "gid://shopify/MetaobjectDefinition/123"
    definition: {
      access: {
        admin: MERCHANT_READ_WRITE
        storefront: NONE
      }
    }
  ) {
    metaobjectDefinition {
      id
      access {
        admin
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

### Deleting definitions

Remove definitions that are no longer needed. Deleting the definition also deletes all related metaobjects, metafield definitions, and metafields asynchronously.

#### Deleting with TOML

For app-owned definitions created with TOML, remove the definition block from your `shopify.app.toml` file and redeploy:

```bash
shopify app deploy
```

#### Deleting with GraphQL

```graphql
mutation DeleteDefinition {
  metaobjectDefinitionDelete(
    id: "gid://shopify/MetaobjectDefinition/123"
  ) {
    deletedId
    userErrors {
      field
      message
    }
  }
}
```

### Error handling

| Error | Cause | Solution |
| - | - | - |
| `TAKEN` | Type has already been taken | Use a different type identifier or update the existing definition |
| `INVALID` | Type contains invalid characters | Use only alphanumeric characters, underscores, and dashes |
| `NOT_AUTHORIZED` | Type is reserved for another app or Shopify | For app-owned types, use `$app:`. Don't use `shopify--` or other reserved prefixes. |
| `DUPLICATE_FIELD_INPUT` | A field with this key already exists in the definition | Use a different field key for each field |

### Best practices

* **Use TOML for app-owned definitions**: Declarative configuration ensures consistency across deployments and enables version control.
* **Plan your type identifiers carefully**: Type identifiers can't be changed after creation.
* **Document field purposes**: Use clear names and descriptions to help merchants understand each field's purpose.
* **Set appropriate access levels**: Start with restrictive access and expand as needed.
* **Test definition changes**: Verify that field additions or updates work correctly before deploying to production.

### TOML reference

Metaobjects are declared in `shopify.app.toml` using the format `[metaobjects.app.<metaobject_name>]`. For example, `[metaobjects.app.author]` declares a metaobject named `author` with type `$app:author`.

#### Metaobject definition properties

| Property | Description |
| - | - |
| `name` | Human-readable name displayed in the Shopify admin. |
| `description` | Descriptive text that explains the purpose of the metaobject. |
| `display_name_field` | Key of a field to reference as the display name for each entry. |
| `access.admin` | Admin API access control: `merchant_read` or `merchant_read_write`. |
| `access.storefront` | Storefront access control: `public_read` or `none`. |
| `capabilities.publishable` | When `true`, enables draft/active status for content workflow. See [metaobject capabilities](https://shopify.dev/docs/apps/build/metaobjects/use-metaobject-capabilities). |
| `capabilities.translatable` | When `true`, enables translation support for fields. |
| `capabilities.renderable` | When `true`, enables metaobject SEO fields on Liquid and the Storefront API. |

#### Metaobject field properties

Fields are declared using the format `[metaobjects.app.<metaobject_name>.fields.<field_name>]`. For example, `[metaobjects.app.author.fields.birthday]` declares a field named `birthday` on the `author` metaobject.

| Property | Description |
| - | - |
| `type` | Data type for the field. Uses the same types as metafields. See [metafield data types](https://shopify.dev/docs/apps/build/metafields/list-of-data-types). |
| `name` | Human-readable name displayed in the Shopify admin. |
| `description` | Descriptive text that explains the purpose of the field. |
| `required` | When `true`, the field must have a value when saving the metaobject. |
| `validations` | Rules to validate field values based on the field type. See [validation options](https://shopify.dev/docs/apps/build/metafields/list-of-validation-options). |

### TOML limitations

When using TOML-based declarative definitions, be aware of these constraints:

#### App-reserved namespace

You can only declare metaobject definitions in the app-reserved namespace (`$app:`) to ensure that only the owning app can make changes to definitions. This constraint allows Shopify to guarantee a consistent state between all shops your app is installed on.

#### App-scoped limits

| Limit | Value |
| - | - |
| Metaobject definitions | 32 |
| Field definitions per metaobject | 64 |
| Changes per deploy | 25 |

To ensure Shopify can quickly and reliably distribute definitions across shops, you can't make more than 25 metaobject changes (creation, update, or deletion) in a single deploy. If you need to make more than 25 changes, do so over multiple deploys.

#### Read-only through Admin API

Declarative definitions are read-only through the Admin API, and can only be updated or deleted through the TOML configuration file. You can query declarative definitions through the Admin API, but mutations will return an error.

#### Capability support

| Capability | Supported in TOML |
| - | - |
| Publishable | Yes |
| Translatable | Yes |
| Renderable | Yes |
| Online Store | No |

### Next steps

* Learn how to [work with metaobject entries](https://shopify.dev/docs/apps/build/metaobjects/manage-metaobjects).
* Learn how to [enable advanced features](https://shopify.dev/docs/apps/build/metaobjects/use-metaobject-capabilities).

---

## Manage entries (metaobject entries)

> Fonte: https://shopify.dev/docs/apps/build/metaobjects/manage-metaobjects

Metaobjects let you store structured data with multiple related field values. This guide shows you how to create, read, update, and delete metaobject entries using the GraphQL Admin API.

### Requirements

* Your app can make [authenticated requests](https://shopify.dev/docs/api/usage/authentication) to the GraphQL Admin API.
* Your app has the `read_metaobjects` and `write_metaobjects` [access scopes](https://shopify.dev/docs/api/usage/access-scopes).
* You've created a [metaobject definition](https://shopify.dev/docs/apps/build/metaobjects/manage-metaobject-definitions) for your metaobject. The definition specifies the fields, validations, and permissions.

> All GraphQL operations below are `POST https://{shop}.myshopify.com/api/{api_version}/graphql.json`.

### Creating entries

Create metaobject entries to store instances of structured data based on your metaobject definitions.

#### Create a basic entry

This example creates a size chart metaobject entry with basic field values. Both the field keys and `type` must match the existing metaobject definition.

```graphql
mutation CreateSizeChartEntry {
  metaobjectCreate(metaobject: {
    type: "size_chart"
    fields: [
      { key: "size", value: "Medium" }
      { key: "chest_inches", value: "38" }
      { key: "waist_inches", value: "32" }
      { key: "hip_inches", value: "36" }
    ]
  }) {
    metaobject {
      id
      handle
      displayName
      fields {
        key
        value
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

#### Create an entry with capabilities

If your metaobject definition has [capabilities](https://shopify.dev/docs/apps/build/metaobjects/use-metaobject-capabilities) enabled (such as publishable), set their initial state when creating entries. This example creates an author metaobject with publishable status set to active.

```graphql
mutation CreatePublishableEntry {
  metaobjectCreate(metaobject: {
    type: "$app:author"
    capabilities: {
      publishable: {
        status: ACTIVE
      }
    }
    fields: [
      { key: "full_name", value: "Jane Smith" }
      { key: "bio", value: "Award-winning author with 20 years of experience..." }
      { key: "email", value: "jane@example.com" }
    ]
  }) {
    metaobject {
      id
      handle
      displayName
      capabilities {
        publishable {
          status
        }
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

#### Create entries in batch

When you need to create many metaobject entries, use bulk operations for better performance.

```graphql
mutation CreateBulkEntries {
  bulkOperationRunMutation(
    mutation: """
      mutation createMetaobject($input: MetaobjectCreateInput!) {
        metaobjectCreate(metaobject: $input) {
          metaobject { id }
          userErrors { field message }
        }
      }
    """
    stagedUploadPath: "bulk_ops/metaobjects_create.jsonl"
  ) {
    bulkOperation {
      id
      status
    }
    userErrors {
      field
      message
    }
  }
}
```

### Reading entries

Query metaobject entries to retrieve their data using various approaches.

#### Query entries by type

```graphql
query GetSizeCharts {
  metaobjects(type: "size_chart", first: 10) {
    edges {
      node {
        id
        handle
        displayName
        fields {
          key
          value
        }
      }
    }
  }
}
```

#### Query a specific entry by handle

```graphql
query GetMetaobjectByHandle {
  metaobjectByHandle(handle: {
    type: "size_chart"
    handle: "medium"
  }) {
    id
    handle
    displayName
    fields {
      key
      value
    }
    updatedAt
  }
}
```

#### Query a specific entry by ID

```graphql
query GetMetaobjectById {
  metaobject(id: "gid://shopify/Metaobject/123") {
    id
    handle
    displayName
    type
    fields {
      key
      value
      type
    }
    capabilities {
      publishable {
        status
      }
    }
  }
}
```

#### Query specific fields

```graphql
query GetSpecificFields {
  metaobject(id: "gid://shopify/Metaobject/123") {
    field(key: "full_name") {
      value
    }
    emailField: field(key: "email") {
      value
    }
  }
}
```

#### Query with filters

Filter metaobject entries based on field values. This is useful for finding entries that match specific criteria, such as all size charts for "Large" sizes.

```graphql
query GetFilteredMetaobjects {
  metaobjects(
    type: "size_chart"
    first: 10
    query: "size:Large"
  ) {
    edges {
      node {
        id
        displayName
        fields {
          key
          value
        }
      }
    }
  }
}
```

### Updating entries

Modify existing metaobject entries to change field values or capability states.

#### Update field values

```graphql
mutation UpdateSizeChart {
  metaobjectUpdate(
    id: "gid://shopify/Metaobject/123"
    metaobject: {
      fields: [
        { key: "chest_inches", value: "40" }
        { key: "waist_inches", value: "34" }
      ]
    }
  ) {
    metaobject {
      id
      fields {
        key
        value
      }
      updatedAt
    }
    userErrors {
      field
      message
    }
  }
}
```

**Note:** You can't change the metaobject `type` after it's created. Field keys must match those defined in the metaobject definition, and field values must match their defined types.

#### Update published status

For metaobjects with the publishable capability enabled, change their published status to control visibility on the storefront.

```graphql
mutation PublishMetaobject {
  metaobjectUpdate(
    id: "gid://shopify/Metaobject/123"
    metaobject: {
      capabilities: {
        publishable: {
          status: ACTIVE
        }
      }
    }
  ) {
    metaobject {
      id
      capabilities {
        publishable {
          status
        }
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

#### Bulk update entries

```graphql
mutation BulkUpdateMetaobjects {
  bulkOperationRunMutation(
    mutation: """
      mutation updateMetaobject($id: ID!, $metaobject: MetaobjectUpdateInput!) {
        metaobjectUpdate(id: $id, metaobject: $metaobject) {
          metaobject { id }
          userErrors { field message }
        }
      }
    """
    stagedUploadPath: "bulk_ops/metaobjects_update.jsonl"
  ) {
    bulkOperation {
      id
      status
    }
    userErrors {
      field
      message
    }
  }
}
```

### Deleting entries

#### Delete a single entry

```graphql
mutation DeleteMetaobject {
  metaobjectDelete(
    id: "gid://shopify/Metaobject/123"
  ) {
    deletedId
    userErrors {
      field
      message
    }
  }
}
```

#### Bulk delete entries

```graphql
mutation BulkDeleteMetaobjects {
  bulkOperationRunMutation(
    mutation: """
      mutation deleteMetaobject($id: ID!) {
        metaobjectDelete(id: $id) {
          deletedId
          userErrors { field message }
        }
      }
    """
    stagedUploadPath: "bulk_ops/metaobjects_delete.jsonl"
  ) {
    bulkOperation {
      id
      status
    }
    userErrors {
      field
      message
    }
  }
}
```

### Connecting metaobjects to resources

One of the most powerful patterns with metaobjects is connecting them to Shopify resources using metafields. [Reference type metafields](https://shopify.dev/docs/apps/build/metafields/list-of-data-types#reference-types) store links to metaobject entries, enabling you to create reusable structured data that can be attached to products, orders, and other resources.

**How it works:**

1. Create definitions (metaobject + metafield) in your TOML configuration and deploy
2. Create metaobject entries (such as "Waterproof", "Eco-friendly", "Durable")
3. Attach entries to products by setting the metafield value

**Why use this pattern:**

* **Reusability**: Create a feature (such as 'Waterproof') once, reference it from 100 products
* **Maintainability**: Update the feature entry, and it updates everywhere it's referenced
* **Structure**: Features have consistent fields (title, description, icon) defined by the metaobject definition

**Reference types available:**

* `metaobject_reference` - Link to a single metaobject entry
* `list.metaobject_reference` - Link to multiple entries of the same metaobject type
* `mixed_reference` - Link to entries from different metaobject types

#### Step 1: Create definitions

Define the metaobject structure and the metafield that references it:

```toml
# shopify.app.toml
# Metaobject definition
[metaobjects.app.product_feature]
name = "Product Feature"


[metaobjects.app.product_feature.fields.title]
type = "single_line_text_field"
name = "Title"


[metaobjects.app.product_feature.fields.description]
type = "multi_line_text_field"
name = "Description"


[metaobjects.app.product_feature.fields.icon]
type = "file_reference"
name = "Icon"


# Metafield definition that references the metaobject
[product.metafields.product_info.features]
type = "list.metaobject_reference<$app:product_feature>"
name = "Product Features"
```

Deploy the definitions:

```bash
shopify app deploy
```

#### Step 2: Create metaobject entries

```graphql
mutation CreateWaterproofFeature {
  metaobjectCreate(metaobject: {
    type: "product_feature"
    fields: [
      { key: "title", value: "Waterproof" }
      { key: "description", value: "Protected against water damage" }
    ]
  }) {
    metaobject {
      id  # gid://shopify/Metaobject/789
      handle
    }
    userErrors {
      field
      message
    }
  }
}
```

#### Step 3: Attach metaobject entries to a product

```graphql
mutation AttachFeaturesToProduct {
  productUpdate(input: {
    id: "gid://shopify/Product/456"
    metafields: [{
      namespace: "product_info"
      key: "features"
      type: "list.metaobject_reference"
      value: "[\"gid://shopify/Metaobject/789\", \"gid://shopify/Metaobject/790\"]"
    }]
  }) {
    product {
      metafield(namespace: "product_info", key: "features") {
        references(first: 10) {
          nodes {
            ... on Metaobject {
              handle
              fields { key value }
            }
          }
        }
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

### Handle management

Metaobject handles are URL-friendly identifiers used to reference entries.

#### Auto-generated handles

By default, Shopify generates handles from the display name:

```graphql
mutation CreateWithAutoHandle {
  metaobjectCreate(metaobject: {
    type: "size_chart"
    fields: [
      { key: "size", value: "Extra Large" }
    ]
  }) {
    metaobject {
      handle  # Will be "extra-large"
      displayName
    }
  }
}
```

#### Custom handles

Specify a custom handle for more control:

```graphql
mutation CreateWithCustomHandle {
  metaobjectCreate(metaobject: {
    type: "size_chart"
    handle: "xl-size-chart"
    fields: [
      { key: "size", value: "Extra Large" }
    ]
  }) {
    metaobject {
      handle
      displayName
    }
    userErrors {
      field
      message
    }
  }
}
```

### Error handling

| Error | Cause | Solution |
| - | - | - |
| `UNDEFINED_OBJECT_TYPE` | No metaobject definition exists for this type | Create the definition first or check the type identifier |
| `OBJECT_FIELD_REQUIRED` | A required field value is not provided | Include all required fields in the mutation |
| `UNDEFINED_OBJECT_FIELD` | Field key doesn't exist in the definition | Verify field keys match the definition |
| `CAPABILITY_NOT_ENABLED` | Trying to use a capability not enabled on the definition | Enable the capability on the definition first |

### Best practices

* Use meaningful handles: Choose handles that clearly identify the entry's purpose.
* Validate before creating: Check that all required fields are provided and values match expected types.
* Use bulk operations for scale: When creating, updating, or deleting many entries, use bulk operations for better performance.
* Query only needed fields: Optimize API usage by requesting only the fields you need.
* Handle errors gracefully: Check `userErrors` in responses and provide clear feedback.
* Consider capability states: Set appropriate published/unpublished states for publishable metaobjects.

### Troubleshooting

| Issue | Possible Causes | Solution |
| - | - | - |
| Entry not appearing on storefront | Missing storefront access, unpublished entry, or incorrect query | Verify the definition has `storefront: PUBLIC_READ` access, check if the entry is published (for publishable metaobjects), and ensure your storefront query includes the correct type |
| Unable to update entry | Missing permissions, incorrect ID, or invalid field keys | Confirm you have write access to the metaobject type, check that the entry ID is correct and the entry still exists, and verify field keys match the definition |
| Bulk operation failing | Invalid JSONL format, missing required fields, or file size issues | Validate your JSONL file format, check that all entries have required fields, ensure file size is within limits, and review bulk operation status for specific error details |

### Next steps

* Learn how to [work with metaobject definitions](https://shopify.dev/docs/apps/build/metaobjects/manage-metaobject-definitions).
* Learn how to [enable advanced features](https://shopify.dev/docs/apps/build/metaobjects/use-metaobject-capabilities).
* Learn about [metaobject limits](https://shopify.dev/docs/apps/build/metaobjects/metaobject-limits).

---

## Query metaobjects

> Fonte: https://shopify.dev/docs/apps/build/metaobjects/query-metaobjects

Query metaobjects by their field values to find entries that match specific criteria. Use this to build dynamic searches, filter content, or find metaobject entries based on their data.

### Prerequisites

Before querying by field value, you need a metaobject definition with entries created.

* [Create metaobject definitions](https://shopify.dev/docs/apps/build/metaobjects/manage-metaobject-definitions)
* [Create metaobject entries](https://shopify.dev/docs/apps/build/metaobjects/manage-metaobjects)

### Query syntax

Use the `fields.{key}:{value}` syntax to query metaobjects based on their field values:

```
metaobjects(type: "your_type", query: "fields.field_name:\"value\"")
```

### Query examples

The following examples demonstrate how to query metaobjects by different field types. All requests are `POST https://{shop}.myshopify.com/api/{api_version}/graphql.json`.

#### By text field

Filter metaobjects by exact text field matches.

```graphql
query Metaobjects {
  metaobjects(first: 20, type: "custom--product-feature",
    query: "fields.feature_name:\"waterproof\"") {
    edges {
      node {
        id
        displayName
        type
        name: field(key: "feature_name") { value }
        updatedAt
        createdAt
      }
    }
  }
}
```

#### By taxonomy reference

Find metaobjects classified with specific taxonomy values like colors or materials.

```graphql
query Metaobjects {
    metaobjects(first: 20, type: "shopify--color-pattern",
    query: "fields.taxonomy_reference:\"gid://shopify/TaxonomyValue/2\"") {
    edges {
        node {
            id
            displayName
            type
            name: field(key: "color_taxonomy_reference") { value }
            updatedAt
            createdAt
        }
     }
  }
}
```

**Note:** This example uses the GID structure for the taxonomy node for the `color` blue. You can find GIDs for taxonomy nodes in the open source [Taxonomy Explorer](https://shopify.github.io/product-taxonomy/releases/latest/).

#### By list fields

Find metaobjects that contain a specific value in a list field. The query matches if ANY value in the list matches the search term.

```graphql
query MetaobjectsByListValue {
  metaobjects(first: 20, type: "custom--product_feature",
    query: "fields.supported_devices:\"iPhone 15\"") {
    edges {
      node {
        id
        displayName
        field(key: "supported_devices") { 
          value 
        }
      }
    }
  }
}
```

### Best practices

* **Test queries in GraphiQL** before implementing in code.
* **Use pagination** for large result sets with cursor-based pagination.
* **Be case-sensitive** - metaobject field queries are case-sensitive.
* **Quote values** - always wrap query values in escaped quotes: `\"value\"`

### Next steps

* Learn how to [work with metaobject entries](https://shopify.dev/docs/apps/build/metaobjects/manage-metaobjects).
* Learn how to [work with metaobject definitions](https://shopify.dev/docs/apps/build/metaobjects/manage-metaobject-definitions).
* Learn how to use metafields to [query resources](https://shopify.dev/docs/apps/build/metafields/query-using-metafields).
