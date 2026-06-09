# 9. Liquid — Filters (parte 1: categorie A–L)

Questo capitolo è una trascrizione fedele (1:1) della reference dei **filtri Liquid** di Shopify, limitata alle **categorie il cui nome inizia con una lettera da A a L (inclusa)**. Le categorie da M a Z sono trattate nella parte 2 (file complementare, senza sovrapposizioni né lacune).

> Indice di riferimento: <https://shopify.dev/docs/api/liquid/filters>

**Categorie coperte in questa parte 1 (A–L), esattamente:**

1. **array** — `compact`, `concat`, `find`, `find_index`, `first`, `has`, `join`, `last`, `map`, `reject`, `reverse`, `size`, `slice`, `sort`, `sort_natural`, `sum`, `uniq`, `where`
2. **cart** — `item_count_for_variant`, `line_items_for`
3. **collection** — `highlight_active_tag`, `link_to_type`, `link_to_vendor`, `sort_by`, `url_for_type`, `url_for_vendor`, `within`
4. **color** — `brightness_difference`, `color_brightness`, `color_contrast`, `color_darken`, `color_desaturate`, `color_difference`, `color_extract`, `color_lighten`, `color_mix`, `color_modify`, `color_saturate`, `color_to_hex`, `color_to_hsl`, `color_to_oklch`, `color_to_rgb`, `hex_to_rgba`
5. **customer** — `avatar`, `customer_login_link`, `customer_logout_link`, `customer_register_link`, `login_button`
6. **default** — `default`, `default_errors`, `default_pagination`
7. **font** — `font_face`, `font_modify`, `font_url`
8. **format** — `date`, `json`, `structured_data`, `weight_with_unit`
9. **hosted_file** — `asset_img_url`, `asset_url`, `file_img_url`, `file_url`, `global_asset_url`, `img_tag`, `script_tag`, `shopify_asset_url`, `stylesheet_tag`
10. **html** — `class_list`, `escape`, `highlight`, `newline_to_br`, `strip_html`, `time_tag`, `url_escape`, `url_param_escape`
11. **localization** — `currency_selector`, `format_address`, `translate` (alias `t`)
12. **math** — `abs`, `at_least`, `at_most`, `ceil`, `divided_by`, `floor`, `minus`, `modulo`, `plus`, `round`, `times`

> Nota sui confini di categoria (per evitare overlap con la parte 2): i filtri `escape_once`, `handleize`/`handle`, `link_to`, `strip_newlines` — pur essendo affini agli HTML — sono classificati da Shopify nella categoria **string** (M–Z) e quindi **non** sono inclusi qui. Nella categoria **html** è incluso `escape` (che svolge l'escaping dei caratteri HTML). Non esistono pagine reference autonome `html_escape`/`html_safe` su shopify.dev.

---

## Indice (per categoria)

### array
- [array — compact](#array--compact)
- [array — concat](#array--concat)
- [array — find](#array--find)
- [array — find_index](#array--find_index)
- [array — first](#array--first)
- [array — has](#array--has)
- [array — join](#array--join)
- [array — last](#array--last)
- [array — map](#array--map)
- [array — reject](#array--reject)
- [array — reverse](#array--reverse)
- [array — size](#array--size)
- [array — slice](#array--slice)
- [array — sort](#array--sort)
- [array — sort_natural](#array--sort_natural)
- [array — sum](#array--sum)
- [array — uniq](#array--uniq)
- [array — where](#array--where)

### cart
- [cart — item_count_for_variant](#cart--item_count_for_variant)
- [cart — line_items_for](#cart--line_items_for)

### collection
- [collection — highlight_active_tag](#collection--highlight_active_tag)
- [collection — link_to_type](#collection--link_to_type)
- [collection — link_to_vendor](#collection--link_to_vendor)
- [collection — sort_by](#collection--sort_by)
- [collection — url_for_type](#collection--url_for_type)
- [collection — url_for_vendor](#collection--url_for_vendor)
- [collection — within](#collection--within)

### color
- [color — brightness_difference](#color--brightness_difference)
- [color — color_brightness](#color--color_brightness)
- [color — color_contrast](#color--color_contrast)
- [color — color_darken](#color--color_darken)
- [color — color_desaturate](#color--color_desaturate)
- [color — color_difference](#color--color_difference)
- [color — color_extract](#color--color_extract)
- [color — color_lighten](#color--color_lighten)
- [color — color_mix](#color--color_mix)
- [color — color_modify](#color--color_modify)
- [color — color_saturate](#color--color_saturate)
- [color — color_to_hex](#color--color_to_hex)
- [color — color_to_hsl](#color--color_to_hsl)
- [color — color_to_oklch](#color--color_to_oklch)
- [color — color_to_rgb](#color--color_to_rgb)
- [color — hex_to_rgba](#color--hex_to_rgba)

### customer
- [customer — avatar](#customer--avatar)
- [customer — customer_login_link](#customer--customer_login_link)
- [customer — customer_logout_link](#customer--customer_logout_link)
- [customer — customer_register_link](#customer--customer_register_link)
- [customer — login_button](#customer--login_button)

### default
- [default — default](#default--default)
- [default — default_errors](#default--default_errors)
- [default — default_pagination](#default--default_pagination)

### font
- [font — font_face](#font--font_face)
- [font — font_modify](#font--font_modify)
- [font — font_url](#font--font_url)

### format
- [format — date](#format--date)
- [format — json](#format--json)
- [format — structured_data](#format--structured_data)
- [format — weight_with_unit](#format--weight_with_unit)

### hosted_file
- [hosted_file — asset_img_url](#hosted_file--asset_img_url)
- [hosted_file — asset_url](#hosted_file--asset_url)
- [hosted_file — file_img_url](#hosted_file--file_img_url)
- [hosted_file — file_url](#hosted_file--file_url)
- [hosted_file — global_asset_url](#hosted_file--global_asset_url)
- [hosted_file — img_tag](#hosted_file--img_tag)
- [hosted_file — script_tag](#hosted_file--script_tag)
- [hosted_file — shopify_asset_url](#hosted_file--shopify_asset_url)
- [hosted_file — stylesheet_tag](#hosted_file--stylesheet_tag)

### html
- [html — class_list](#html--class_list)
- [html — escape](#html--escape)
- [html — highlight](#html--highlight)
- [html — newline_to_br](#html--newline_to_br)
- [html — strip_html](#html--strip_html)
- [html — time_tag](#html--time_tag)
- [html — url_escape](#html--url_escape)
- [html — url_param_escape](#html--url_param_escape)

### localization
- [localization — currency_selector](#localization--currency_selector)
- [localization — format_address](#localization--format_address)
- [localization — translate (t)](#localization--translate-t)

### math
- [math — abs](#math--abs)
- [math — at_least](#math--at_least)
- [math — at_most](#math--at_most)
- [math — ceil](#math--ceil)
- [math — divided_by](#math--divided_by)
- [math — floor](#math--floor)
- [math — minus](#math--minus)
- [math — modulo](#math--modulo)
- [math — plus](#math--plus)
- [math — round](#math--round)
- [math — times](#math--times)

---

## array — compact

> Fonte: <https://shopify.dev/docs/api/liquid/filters/compact>

### Description

"Removes any `nil` items from an array."

### Syntax

```liquid
array | compact
```

### Parameters

None

### Returns

An array with all `nil` values removed.

### Example

#### Input

```liquid
{%- assign original_prices = collection.products | map: 'compare_at_price' -%}

Original prices:

{% for price in original_prices -%}
  - {{ price }}
{%- endfor %}

{%- assign compacted_original_prices = original_prices | compact -%}

Original prices - compacted:

{% for price in compacted_original_prices -%}
  - {{ price }}
{%- endfor %}
```

#### Data

```json
{
  "collection": {
    "products": [
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": "1000000.59"
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": "10.00"
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": "25.00"
      },
      {
        "compare_at_price": "400.00"
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
      }
    ]
  }
}
```

#### Output

```html
Original prices:

- 
- 
- 
- 
- 100000059
- 
- 
- 
- 1000
- 
- 2500
- 40000
- 
- 
- 
- 
- 
- 
- 

Original prices - compacted:

- 100000059
- 1000
- 2500
- 40000
```

---

## array — concat

> Fonte: <https://shopify.dev/docs/api/liquid/filters/concat>

### Description

"Concatenates (combines) two arrays."

### Syntax

```liquid
array | concat: array
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `array` | array | The array to combine with the input array |

### Returns

An array containing all elements from both the input array and the specified array in sequence.

### Notes

"The `concat` filter won't filter out duplicates. If you want to remove duplicates, then you need to use the `uniq` filter."

### Example

**Input:**

```liquid
{%- assign types_and_vendors = collection.all_types | concat: collection.all_vendors -%}

Types and vendors:

{% for item in types_and_vendors -%}
  {%- if item != blank -%}
    - {{ item }}
  {%- endif -%}
{%- endfor %}
```

**Data:**

```json
{
  "collection": {
    "all_types": [
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
Types and vendors:

- Animals & Pet Supplies
- Baking Flavors & Extracts
- Container
- Cooking & Baking Ingredients
- Dried Flowers
- Fruits & Vegetables
- Gift Cards
- Health
- Health & Beauty
- Invisibility
- Love
- Music & Sound Recordings
- Seasonings & Spices
- Water
- Clover's Apothecary
- Polina's Potent Potions
- Ted's Apothecary Supply
```

---

## array — find

> Fonte: <https://shopify.dev/docs/api/liquid/filters/find>

### Syntax

```liquid
array | find: string, string
```

### Description

"Returns the first item in an array with a specific property value." This filter requires you to provide both the property name and the associated value.

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| property | string | The name of the property to match |
| value | string | The value to search for |

### Returns

The first object in the array where the specified property matches the given value, or `nil` if no match is found.

### Examples

#### Example 1: Finding a product by vendor

**Liquid Input:**

```liquid
{% assign product = collection.products | find: 'vendor', "Polina's Potent Potions" %}

{{ product.title }}
```

**Data:**

```json
{
  "collection": {
    "products": [
      {
        "title": "Blue Mountain Flower",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Charcoal",
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "title": "Crocodile tears",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Dandelion milk",
        "vendor": "Clover's Apothecary"
      },
      {
        "title": "Draught of Immortality",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Dried chamomile",
        "vendor": "Clover's Apothecary"
      },
      {
        "title": "Forest mushroom",
        "vendor": "Clover's Apothecary"
      },
      {
        "title": "Gift Card",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Glacier ice",
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "title": "Ground mandrake root",
        "vendor": "Clover's Apothecary"
      },
      {
        "title": "Health potion",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Invisibility potion",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Komodo dragon scale",
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "title": "Love Potion",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Mana potion",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Potion beats",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Potion bottle",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Viper venom",
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "title": "Whole bloodroot",
        "vendor": "Clover's Apothecary"
      }
    ]
  }
}
```

**Output:**

```html
Blue Mountain Flower
```

#### Example 2: Handling no matches

**Liquid Input:**

```liquid
{% assign product = collection.products | find: 'vendor', "Polina's Potions" %}

{{ product.title | default: "No product found" }}
```

**Data:**

```json
{
  "collection": {
    "products": [
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Clover's Apothecary"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Clover's Apothecary"
      },
      {
        "vendor": "Clover's Apothecary"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "vendor": "Clover's Apothecary"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "vendor": "Clover's Apothecary"
      }
    ]
  }
}
```

**Output:**

```html
No product found
```

---

## array — find_index

> Fonte: <https://shopify.dev/docs/api/liquid/filters/find_index>

**Description:** "Returns the index of the first item in an array with a specific property value."

### Syntax

```liquid
array | find_index: string, string
```

**Returns:** number

### Overview

This filter locates the position of the first array element matching a specified property-value pair. You must supply both the property name and its corresponding value.

### Parameters

- **Property name** (string): The object property to evaluate
- **Property value** (string): The target value to match

### Examples

#### Basic Usage

**Liquid code:**

```liquid
{% assign index = collection.products | find_index: 'vendor', "Polina's Potent Potions" %}

{{ index }}
```

**Sample data:**

```json
{
  "collection": {
    "products": [
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Clover's Apothecary"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Clover's Apothecary"
      },
      {
        "vendor": "Clover's Apothecary"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "vendor": "Clover's Apothecary"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "vendor": "Clover's Apothecary"
      }
    ]
  }
}
```

**Output:**

```html
0
```

#### No Match Found

**Liquid code:**

```liquid
{% assign index = collection.products | find_index: 'vendor', "Polina's Potions" %}

{{ index | default: "No index found" }}
```

**Sample data:**

```json
{
  "collection": {
    "products": [
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Clover's Apothecary"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Clover's Apothecary"
      },
      {
        "vendor": "Clover's Apothecary"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "vendor": "Clover's Apothecary"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "vendor": "Clover's Apothecary"
      }
    ]
  }
}
```

**Output:**

```html
No index found
```

### Behavior Notes

When no items match the specified property value, the filter returns `nil`.

---

## array — first

> Fonte: <https://shopify.dev/docs/api/liquid/filters/first>

### Description

"Returns the first item in an array."

### Syntax

```liquid
array | first
```

### Examples

#### Basic Usage

**Liquid Code:**

```liquid
{%- assign first_product = collection.products | first -%}

{{ first_product.title }}
```

**Data:**

```json
{
  "collection": {
    "products": [
      {
        "title": "Blue Mountain Flower"
      },
      {
        "title": "Charcoal"
      },
      {
        "title": "Crocodile tears"
      },
      {
        "title": "Dandelion milk"
      },
      {
        "title": "Draught of Immortality"
      },
      {
        "title": "Dried chamomile"
      },
      {
        "title": "Forest mushroom"
      },
      {
        "title": "Gift Card"
      },
      {
        "title": "Glacier ice"
      },
      {
        "title": "Ground mandrake root"
      },
      {
        "title": "Health potion"
      },
      {
        "title": "Invisibility potion"
      },
      {
        "title": "Komodo dragon scale"
      },
      {
        "title": "Love Potion"
      },
      {
        "title": "Mana potion"
      },
      {
        "title": "Potion beats"
      },
      {
        "title": "Potion bottle"
      },
      {
        "title": "Viper venom"
      },
      {
        "title": "Whole bloodroot"
      }
    ]
  }
}
```

**Output:**

```html
Blue Mountain Flower
```

#### Dot Notation

"You can use the `first` filter with dot notation when you need to use it inside a tag or object output."

**Liquid Code:**

```liquid
{{ collection.products.first.title }}
```

**Data:**

```json
{
  "collection": {
    "products": [
      {
        "title": "Blue Mountain Flower"
      },
      {
        "title": "Charcoal"
      },
      {
        "title": "Crocodile tears"
      },
      {
        "title": "Dandelion milk"
      },
      {
        "title": "Draught of Immortality"
      },
      {
        "title": "Dried chamomile"
      },
      {
        "title": "Forest mushroom"
      },
      {
        "title": "Gift Card"
      },
      {
        "title": "Glacier ice"
      },
      {
        "title": "Ground mandrake root"
      },
      {
        "title": "Health potion"
      },
      {
        "title": "Invisibility potion"
      },
      {
        "title": "Komodo dragon scale"
      },
      {
        "title": "Love Potion"
      },
      {
        "title": "Mana potion"
      },
      {
        "title": "Potion beats"
      },
      {
        "title": "Potion bottle"
      },
      {
        "title": "Viper venom"
      },
      {
        "title": "Whole bloodroot"
      }
    ]
  }
}
```

**Output:**

```html
Blue Mountain Flower
```

---

## array — has

> Fonte: <https://shopify.dev/docs/api/liquid/filters/has>

### Syntax

```liquid
array | has: string, string
```

### Returns

[boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

### Description

"Tests if any item in an array has a specific property value."

This requires you to provide both the property name and the associated value.

### Examples

#### Returns `true` when items match the specified property value

**Liquid code:**

```liquid
{% assign has_potent_potions = collection.products | has: 'vendor', "Polina's Potent Potions" %}

{{ has_potent_potions }}
```

**Data:**

```json
{
  "collection": {
    "products": [
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Clover's Apothecary"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Clover's Apothecary"
      },
      {
        "vendor": "Clover's Apothecary"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "vendor": "Clover's Apothecary"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "vendor": "Clover's Apothecary"
      }
    ]
  }
}
```

**Output:**

```html
true
```

#### Returns `false` when no items match the specified property value

**Liquid code:**

```liquid
{% assign has_potent_potions = collection.products | has: 'vendor', "Polina's Potions" %}

{{ has_potent_potions }}
```

**Data:**

```json
{
  "collection": {
    "products": [
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Clover's Apothecary"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Clover's Apothecary"
      },
      {
        "vendor": "Clover's Apothecary"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "vendor": "Clover's Apothecary"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "vendor": "Clover's Apothecary"
      }
    ]
  }
}
```

**Output:**

```html
false
```

---

## array — join

> Fonte: <https://shopify.dev/docs/api/liquid/filters/join>

**Description:** "Combines all of the items in an array into a single string, separated by a space."

### Syntax

```liquid
array | join
```

```liquid
array | join: string
```

**Returns:** [string](https://shopify.dev/docs/api/liquid/basics#string)

### Basic Usage

Joins array elements with default space separator.

#### Code

```liquid
{{ collection.all_tags | join }}
```

#### Data

```json
{
  "collection": {
    "all_tags": [
      "extra-potent",
      "fresh",
      "healing",
      "ingredients"
    ]
  }
}
```

#### Output

```html
extra-potent fresh healing ingredients
```

### Custom Separator

Specify a custom separator string for the joined items.

#### Code

```liquid
{{ collection.all_tags | join: ', ' }}
```

#### Data

```json
{
  "collection": {
    "all_tags": [
      "extra-potent",
      "fresh",
      "healing",
      "ingredients"
    ]
  }
}
```

#### Output

```html
extra-potent, fresh, healing, ingredients
```

---

## array — last

> Fonte: <https://shopify.dev/docs/api/liquid/filters/last>

### Syntax

```liquid
array | last
```

### Description

"Returns the last item in an array."

### Return Value

The final element from the provided array.

### Examples

#### Basic Usage

**Liquid Code:**

```liquid
{%- assign last_product = collection.products | last -%}

{{ last_product.title }}
```

**Data:**

```json
{
  "collection": {
    "products": [
      {
        "title": "Blue Mountain Flower"
      },
      {
        "title": "Charcoal"
      },
      {
        "title": "Crocodile tears"
      },
      {
        "title": "Dandelion milk"
      },
      {
        "title": "Draught of Immortality"
      },
      {
        "title": "Dried chamomile"
      },
      {
        "title": "Forest mushroom"
      },
      {
        "title": "Gift Card"
      },
      {
        "title": "Glacier ice"
      },
      {
        "title": "Ground mandrake root"
      },
      {
        "title": "Health potion"
      },
      {
        "title": "Invisibility potion"
      },
      {
        "title": "Komodo dragon scale"
      },
      {
        "title": "Love Potion"
      },
      {
        "title": "Mana potion"
      },
      {
        "title": "Potion beats"
      },
      {
        "title": "Potion bottle"
      },
      {
        "title": "Viper venom"
      },
      {
        "title": "Whole bloodroot"
      }
    ]
  }
}
```

**Output:**

```html
Whole bloodroot
```

#### Dot Notation

You can use dot notation syntax when applying this filter inside tags or object outputs.

**Liquid Code:**

```liquid
{{ collection.products.last.title }}
```

**Data:**

```json
{
  "collection": {
    "products": [
      {
        "title": "Blue Mountain Flower"
      },
      {
        "title": "Charcoal"
      },
      {
        "title": "Crocodile tears"
      },
      {
        "title": "Dandelion milk"
      },
      {
        "title": "Draught of Immortality"
      },
      {
        "title": "Dried chamomile"
      },
      {
        "title": "Forest mushroom"
      },
      {
        "title": "Gift Card"
      },
      {
        "title": "Glacier ice"
      },
      {
        "title": "Ground mandrake root"
      },
      {
        "title": "Health potion"
      },
      {
        "title": "Invisibility potion"
      },
      {
        "title": "Komodo dragon scale"
      },
      {
        "title": "Love Potion"
      },
      {
        "title": "Mana potion"
      },
      {
        "title": "Potion beats"
      },
      {
        "title": "Potion bottle"
      },
      {
        "title": "Viper venom"
      },
      {
        "title": "Whole bloodroot"
      }
    ]
  }
}
```

**Output:**

```html
Whole bloodroot
```

---

## array — map

> Fonte: <https://shopify.dev/docs/api/liquid/filters/map>

### Description

"Creates an array of values from a specific property of the items in an array."

### Syntax

```liquid
array | map: string
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| property | string | The property name to extract from each item in the array |

### Returns

An array containing the extracted property values from each item.

### Example

#### Input

```liquid
{%- assign product_titles = collection.products | map: 'title' -%}

{{ product_titles | join: ', ' }}
```

#### Data

```json
{
  "collection": {
    "products": [
      {
        "title": "Draught of Immortality"
      },
      {
        "title": "Glacier ice"
      },
      {
        "title": "Health potion"
      },
      {
        "title": "Invisibility potion"
      }
    ]
  }
}
```

#### Output

```html
Draught of Immortality, Glacier ice, Health potion, Invisibility potion
```

---

## array — reject

> Fonte: <https://shopify.dev/docs/api/liquid/filters/reject>

**Filters an array to exclude items with a specific property value.**

### Syntax

```liquid
array | reject: string, string
```

### Description

"Filters an array to exclude items with a specific property value." This operation requires specifying both the property name and its corresponding value to be excluded.

### Parameters

- **property** (string): The name of the property to evaluate
- **value** (string): The value to match for exclusion

### Returns

An array containing all items where the specified property does not match the provided value.

### Example

#### Input

```liquid
{% assign polina_products = collection.products | reject: 'vendor', "Polina's Potent Potions" %}

Products from other vendors than Polina's Potent Potions:

{% for product in polina_products -%}
  - {{ product.title }}
{%- endfor %}
```

#### Sample Data

```json
{
  "collection": {
    "products": [
      {"title": "Blue Mountain Flower", "vendor": "Polina's Potent Potions"},
      {"title": "Charcoal", "vendor": "Ted's Apothecary Supply"},
      {"title": "Crocodile tears", "vendor": "Polina's Potent Potions"},
      {"title": "Dandelion milk", "vendor": "Clover's Apothecary"},
      {"title": "Draught of Immortality", "vendor": "Polina's Potent Potions"},
      {"title": "Dried chamomile", "vendor": "Clover's Apothecary"},
      {"title": "Forest mushroom", "vendor": "Clover's Apothecary"},
      {"title": "Gift Card", "vendor": "Polina's Potent Potions"},
      {"title": "Glacier ice", "vendor": "Ted's Apothecary Supply"},
      {"title": "Ground mandrake root", "vendor": "Clover's Apothecary"},
      {"title": "Health potion", "vendor": "Polina's Potent Potions"},
      {"title": "Invisibility potion", "vendor": "Polina's Potent Potions"},
      {"title": "Komodo dragon scale", "vendor": "Ted's Apothecary Supply"},
      {"title": "Love Potion", "vendor": "Polina's Potent Potions"},
      {"title": "Mana potion", "vendor": "Polina's Potent Potions"},
      {"title": "Potion beats", "vendor": "Polina's Potent Potions"},
      {"title": "Potion bottle", "vendor": "Polina's Potent Potions"},
      {"title": "Viper venom", "vendor": "Ted's Apothecary Supply"},
      {"title": "Whole bloodroot", "vendor": "Clover's Apothecary"}
    ]
  }
}
```

#### Output

```html
Products from other vendors than Polina's Potent Potions:

- Charcoal
- Dandelion milk
- Dried chamomile
- Forest mushroom
- Glacier ice
- Ground mandrake root
- Komodo dragon scale
- Viper venom
- Whole bloodroot
```

---

## array — reverse

> Fonte: <https://shopify.dev/docs/api/liquid/filters/reverse>

### Description

"Reverses the order of the items in an array."

### Syntax

```liquid
array | reverse
```

### Examples

#### Basic Array Reversal

**Liquid Code:**

```liquid
Original order:
{{ collection.products | map: 'title' | join: ', ' }}

Reverse order:
{{ collection.products | reverse | map: 'title' | join: ', ' }}
```

**Data:**

```json
{
  "collection": {
    "products": [
      {
        "title": "Draught of Immortality"
      },
      {
        "title": "Glacier ice"
      },
      {
        "title": "Health potion"
      },
      {
        "title": "Invisibility potion"
      }
    ]
  }
}
```

**Output:**

```html
Original order:
Draught of Immortality, Glacier ice, Health potion, Invisibility potion

Reverse order:
Invisibility potion, Health potion, Glacier ice, Draught of Immortality
```

#### Reversing Strings

To reverse a string, use the `split` filter to create a character array, apply `reverse`, then use `join` to recombine:

**Liquid Code:**

```liquid
{{ collection.title | split: '' | reverse | join: '' }}
```

**Data:**

```json
{
  "collection": {
    "title": "Sale potions"
  }
}
```

**Output:**

```html
snoitop elaS
```

---

## array — size

> Fonte: <https://shopify.dev/docs/api/liquid/filters/size>

### Description

"Returns the size of a string or array." The size of a string represents the number of characters it contains, while the size of an array represents the number of items within it.

### Syntax

```liquid
variable | size
```

### Returns

[number](https://shopify.dev/docs/api/liquid/basics#number)

### Examples

#### Basic Usage

**Code:**

```liquid
{{ collection.title | size }}
{{ collection.products | size }}
```

**Data:**

```json
{
  "collection": {
    "products": [],
    "title": "Sale potions"
  }
}
```

**Output:**

```html
12
4
```

#### Dot Notation

You can use the `size` filter with dot notation when you need to use it inside a tag or object output.

**Code:**

```liquid
{% if collection.products.size >= 10 %}
  There are 10 or more products in this collection.
{% else %}
  There are less than 10 products in this collection.
{% endif %}
```

**Data:**

```json
{
  "collection": {
    "products": []
  }
}
```

**Output:**

```html
There are less than 10 products in this collection.
```

---

## array — slice

> Fonte: <https://shopify.dev/docs/api/liquid/filters/slice>

**Description:** "Returns a substring or series of array items, starting at a given 0-based index."

### Syntax

```liquid
string | slice: index
string | slice: index, length
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `index` | integer | The 0-based starting position. Supports negative indices to count from the end. |
| `length` | integer | Optional. Number of characters (for strings) or items (for arrays) to extract. Defaults to 1. |

### Returns

string or array

### Examples

#### Basic substring extraction

**Input:**

```liquid
{{ collection.title | slice: 0 }}
{{ collection.title | slice: 0, 5 }}
```

**Data:**

```json
{
  "collection": {
    "title": "Products"
  }
}
```

**Output:**

```
P
Produ
```

#### Array slicing with join

**Input:**

```liquid
{{ collection.all_tags | slice: 1, 2 | join: ', ' }}
```

**Data:**

```json
{
  "collection": {
    "all_tags": [
      "Burning",
      "dried",
      "extra-potent",
      "extracts",
      "fresh",
      "healing",
      "ingredients",
      "music",
      "plant",
      "Salty",
      "supplies"
    ]
  }
}
```

**Output:**

```
dried, extra-potent
```

#### Negative index

**Input:**

```liquid
{{ collection.title | slice: -3, 3 }}
```

**Data:**

```json
{
  "collection": {
    "title": "Products"
  }
}
```

**Output:**

```
cts
```

---

## array — sort

> Fonte: <https://shopify.dev/docs/api/liquid/filters/sort>

### Description

"Sorts the items in an array in case-sensitive alphabetical, or numerical, order."

### Syntax

```liquid
array | sort
```

### Basic Usage

Sort an array in case-sensitive alphabetical order:

#### Code

```liquid
{% assign tags = collection.all_tags | sort %}

{% for tag in tags -%}
  {{ tag }}
{%- endfor %}
```

#### Data

```json
{
  "collection": {
    "all_tags": [
      "Burning",
      "dried",
      "extra-potent",
      "extracts",
      "fresh",
      "healing",
      "ingredients",
      "music",
      "plant",
      "Salty",
      "supplies"
    ]
  }
}
```

#### Output

```html
Burning
Salty
dried
extra-potent
extracts
fresh
healing
ingredients
music
plant
supplies
```

### Sort by Array Item Property

#### Syntax

```liquid
array | sort: string
```

You can specify an array item property to sort by. Use any property of the objects being sorted.

#### Code

```liquid
{% assign products = collection.products | sort: 'price' %}

{% for product in products -%}
  {{ product.title }}
{%- endfor %}
```

#### Data

```json
{
  "collection": {
    "products": [
      {
        "price": "10.00",
        "title": "Blue Mountain Flower"
      },
      {
        "price": "0.00",
        "title": "Charcoal"
      },
      {
        "price": "56.00",
        "title": "Crocodile tears"
      },
      {
        "price": "0.00",
        "title": "Dandelion milk"
      },
      {
        "price": "1000000.00",
        "title": "Draught of Immortality"
      },
      {
        "price": "8.98",
        "title": "Dried chamomile"
      },
      {
        "price": "0.00",
        "title": "Forest mushroom"
      },
      {
        "price": "10.00",
        "title": "Gift Card"
      },
      {
        "price": "0.00",
        "title": "Glacier ice"
      },
      {
        "price": "0.00",
        "title": "Ground mandrake root"
      },
      {
        "price": "10.00",
        "title": "Health potion"
      },
      {
        "price": "250.00",
        "title": "Invisibility potion"
      },
      {
        "price": "0.00",
        "title": "Komodo dragon scale"
      },
      {
        "price": "0.00",
        "title": "Love Potion"
      },
      {
        "price": "10.00",
        "title": "Mana potion"
      },
      {
        "price": "0.00",
        "title": "Potion beats"
      },
      {
        "price": "0.00",
        "title": "Potion bottle"
      },
      {
        "price": "400.00",
        "title": "Viper venom"
      },
      {
        "price": "24.99",
        "title": "Whole bloodroot"
      }
    ]
  }
}
```

#### Output

```html
Charcoal
Dandelion milk
Forest mushroom
Glacier ice
Ground mandrake root
Komodo dragon scale
Love Potion
Potion beats
Potion bottle
Dried chamomile
Blue Mountain Flower
Gift Card
Health potion
Mana potion
Whole bloodroot
Crocodile tears
Invisibility potion
Viper venom
Draught of Immortality
```

---

## array — sort_natural

> Fonte: <https://shopify.dev/docs/api/liquid/filters/sort_natural>

### Description

"Sorts the items in an array in case-insensitive alphabetical order."

### Syntax

```liquid
array | sort_natural
```

```liquid
array | sort_natural: string
```

### Parameters

**Property name** (optional)
- Type: string
- Allows sorting by a specific property of array items

### Returns

A sorted array in case-insensitive alphabetical order.

### Important Note

> **Caution:** "You shouldn't use the sort_natural filter to sort numerical values. When comparing items an array, each item is converted to a string, so sorting on numerical values can lead to unexpected results."

### Examples

#### Basic Usage

**Input:**

```liquid
{% assign tags = collection.all_tags | sort_natural %}

{% for tag in tags -%}
  {{ tag }}
{%- endfor %}
```

**Data:**

```json
{
  "collection": {
    "all_tags": [
      "Burning",
      "dried",
      "extra-potent",
      "extracts",
      "fresh",
      "healing",
      "ingredients",
      "music",
      "plant",
      "Salty",
      "supplies"
    ]
  }
}
```

**Output:**

```
Burning
dried
extra-potent
extracts
fresh
healing
ingredients
music
plant
Salty
supplies
```

#### Sort by Object Property

**Input:**

```liquid
{% assign products = collection.products | sort_natural: 'title' %}

{% for product in products -%}
  {{ product.title }}
{%- endfor %}
```

**Data:**

```json
{
  "collection": {
    "products": [
      {
        "title": "Blue Mountain Flower"
      },
      {
        "title": "Charcoal"
      },
      {
        "title": "Crocodile tears"
      },
      {
        "title": "Dandelion milk"
      },
      {
        "title": "Draught of Immortality"
      },
      {
        "title": "Dried chamomile"
      },
      {
        "title": "Forest mushroom"
      },
      {
        "title": "Gift Card"
      },
      {
        "title": "Glacier ice"
      },
      {
        "title": "Ground mandrake root"
      },
      {
        "title": "Health potion"
      },
      {
        "title": "Invisibility potion"
      },
      {
        "title": "Komodo dragon scale"
      },
      {
        "title": "Love Potion"
      },
      {
        "title": "Mana potion"
      },
      {
        "title": "Potion beats"
      },
      {
        "title": "Potion bottle"
      },
      {
        "title": "Viper venom"
      },
      {
        "title": "Whole bloodroot"
      }
    ]
  }
}
```

**Output:**

```
Blue Mountain Flower
Charcoal
Crocodile tears
Dandelion milk
Draught of Immortality
Dried chamomile
Forest mushroom
Gift Card
Glacier ice
Ground mandrake root
Health potion
Invisibility potion
Komodo dragon scale
Love Potion
Mana potion
Potion beats
Potion bottle
Viper venom
Whole bloodroot
```

---

## array — sum

> Fonte: <https://shopify.dev/docs/api/liquid/filters/sum>

### Syntax

```liquid
array | sum
array | sum: string
```

### Description

"Returns the sum of all elements in an array." For object arrays, you can specify a property to sum.

### Return Type

number

### Basic Usage

```liquid
{% assign fibonacci = '0, 1, 1, 2, 3, 5' | split: ', ' %}

{{ fibonacci | sum }}
```

Output:

```html
12
```

### Sum Object Property Values

When working with arrays of objects, pass a property name as a string parameter to sum that specific field across all items.

```liquid
Total quantity of all items in cart:
{{ cart.items | sum: 'quantity' }}

Subtotal price for all items in cart:
{{ cart.items | sum: 'final_line_price' | money }}
```

Given this data:

```json
{
  "cart": {
    "items": [
      {
        "final_line_price": "22.49",
        "quantity": 1
      },
      {
        "final_line_price": "400.00",
        "quantity": 1
      }
    ]
  }
}
```

Produces:

```html
Total quantity of all items in cart:
2

Subtotal price for all items in cart:
$422.49
```

---

## array — uniq

> Fonte: <https://shopify.dev/docs/api/liquid/filters/uniq>

### Description

"Removes any duplicate items in an array."

### Syntax

```liquid
array | uniq
```

### Parameters

None

### Returns

Array with duplicate items removed.

### Example

**Input:**

```liquid
{% assign potion_array = 'invisibility, health, love, health, invisibility' | split: ', ' %}

{{ potion_array | uniq | join: ', ' }}
```

**Output:**

```html
invisibility, health, love
```

---

## array — where

> Fonte: <https://shopify.dev/docs/api/liquid/filters/where>

```liquid
array | where: string, string
```

### Description

"Filters an array to include only items with a specific property value." This filter requires both a property name and its associated value to be specified.

### Syntax

```liquid
array | where: property_name, property_value
```

or for boolean properties:

```liquid
array | where: property_name
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| property_name | string | The name of the property to filter by |
| property_value | string | The value to match (optional for boolean properties) |

### Returns

An array containing only the items where the specified property matches the given value.

---

#### Example 1: Filter by String Property

**Code**

```liquid
{% assign polina_products = collection.products | where: 'vendor', "Polina's Potent Potions" %}

Products from Polina's Potent Potions:

{% for product in polina_products -%}
  - {{ product.title }}
{%- endfor %}
```

**Data**

```json
{
  "collection": {
    "products": [
      {
        "title": "Blue Mountain Flower",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Charcoal",
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "title": "Crocodile tears",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Dandelion milk",
        "vendor": "Clover's Apothecary"
      },
      {
        "title": "Draught of Immortality",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Dried chamomile",
        "vendor": "Clover's Apothecary"
      },
      {
        "title": "Forest mushroom",
        "vendor": "Clover's Apothecary"
      },
      {
        "title": "Gift Card",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Glacier ice",
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "title": "Ground mandrake root",
        "vendor": "Clover's Apothecary"
      },
      {
        "title": "Health potion",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Invisibility potion",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Komodo dragon scale",
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "title": "Love Potion",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Mana potion",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Potion beats",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Potion bottle",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Viper venom",
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "title": "Whole bloodroot",
        "vendor": "Clover's Apothecary"
      }
    ]
  }
}
```

**Output**

```html
Products from Polina's Potent Potions:

- Blue Mountain Flower
- Crocodile tears
- Draught of Immortality
- Gift Card
- Health potion
- Invisibility potion
- Love Potion
- Mana potion
- Potion beats
- Potion bottle
```

---

#### Example 2: Filter for Boolean Properties

"You can filter for items that have a `true` value for a boolean property. This requires you to provide only the property name."

**Code**

```liquid
{% assign available_products = collection.products | where: 'available' %}

Available products:

{% for product in available_products -%}
  - {{ product.title }}
{%- endfor %}
```

**Data**

```json
{
  "collection": {
    "products": [
      {
        "available": false,
        "title": "Blue Mountain Flower"
      },
      {
        "available": true,
        "title": "Charcoal"
      },
      {
        "available": false,
        "title": "Crocodile tears"
      },
      {
        "available": false,
        "title": "Dandelion milk"
      },
      {
        "available": true,
        "title": "Draught of Immortality"
      },
      {
        "available": true,
        "title": "Dried chamomile"
      },
      {
        "available": false,
        "title": "Forest mushroom"
      },
      {
        "available": true,
        "title": "Gift Card"
      },
      {
        "available": false,
        "title": "Glacier ice"
      },
      {
        "available": true,
        "title": "Ground mandrake root"
      },
      {
        "available": true,
        "title": "Health potion"
      },
      {
        "available": true,
        "title": "Invisibility potion"
      },
      {
        "available": false,
        "title": "Komodo dragon scale"
      },
      {
        "available": false,
        "title": "Love Potion"
      },
      {
        "available": true,
        "title": "Mana potion"
      },
      {
        "available": true,
        "title": "Potion beats"
      },
      {
        "available": false,
        "title": "Potion bottle"
      },
      {
        "available": true,
        "title": "Viper venom"
      },
      {
        "available": true,
        "title": "Whole bloodroot"
      }
    ]
  }
}
```

**Output**

```html
Available products:

- Charcoal
- Draught of Immortality
- Dried chamomile
- Gift Card
- Ground mandrake root
- Health potion
- Invisibility potion
- Mana potion
- Potion beats
- Viper venom
- Whole bloodroot
```

---

## cart — item_count_for_variant

> Fonte: <https://shopify.dev/docs/api/liquid/filters/item_count_for_variant>

### Description

"Returns the total item count for a specified variant in the [`cart`](https://shopify.dev/docs/api/liquid/objects/cart) object."

### Syntax

```liquid
cart | item_count_for_variant: {variant_id}
```

### Parameters

- `variant_id` (number): The ID of the variant to count items for

### Returns

[number](https://shopify.dev/docs/api/liquid/basics#number)

### Example

**Input:**

```liquid
{{ cart | item_count_for_variant: 39888235757633 }}
```

**Output:**

```html
1
```

---

## cart — line_items_for

> Fonte: <https://shopify.dev/docs/api/liquid/filters/line_items_for>

### Description

"Returns the subset of `cart` line items that include a specified product or variant."

### Syntax

```liquid
cart | line_items_for: object
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `object` | product or variant | The product or variant to filter line items by |

### Returns

Array of `line_item` objects

### Accepted Object Types

- `product`
- `variant`

### Examples

#### Example 1: Filter by Product

**Input:**

```liquid
{% assign product = all_products['bloodroot-whole'] %}
{% assign line_items = cart | line_items_for: product %}

Total cart quantity for product: {{ line_items | sum: 'quantity' }}
```

**Data:**

```json
{
  "all_products": {
    "bloodroot-whole": {}
  }
}
```

**Output:**

```html
Total cart quantity for product: 1
```

#### Example 2: Filter by Variant

**Input:**

```liquid
{% assign product = all_products['bloodroot-whole'] %}
{% assign variant = product.variants.first %}
{% assign line_items = cart | line_items_for: variant %}

Total cart quantity for variant: {{ line_items | sum: 'quantity' }}
```

**Data:**

```json
{
  "all_products": {
    "bloodroot-whole": {
      "variants": []
    }
  },
  "product": {
    "variants": []
  }
}
```

**Output:**

```html
Total cart quantity for variant: 1
```

---

## collection — highlight_active_tag

> Fonte: <https://shopify.dev/docs/api/liquid/filters/highlight_active_tag>

### Syntax

```liquid
string | highlight_active_tag
```

### Returns

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Description

This filter wraps a tag from the collection object in an HTML `<span>` tag with class `active` when that tag is currently active. "Only applies to collection tags."

### Example

#### Input

```liquid
{% for tag in collection.all_tags %}
  {{- tag | highlight_active_tag | link_to_tag: tag }}
{% endfor %}
```

#### Data

```json
{
  "collection": {
    "all_tags": [
      "extra-potent",
      "fresh",
      "healing",
      "ingredients"
    ]
  },
  "template": "collection"
}
```

#### Output

```html
<a href="/services/liquid_rendering/extra-potent" title="Show products matching tag extra-potent"><span class="active">extra-potent</span></a>

<a href="/services/liquid_rendering/fresh" title="Show products matching tag fresh">fresh</a>

<a href="/services/liquid_rendering/healing" title="Show products matching tag healing">healing</a>

<a href="/services/liquid_rendering/ingredients" title="Show products matching tag ingredients">ingredients</a>
```

---

## collection — link_to_type

> Fonte: <https://shopify.dev/docs/api/liquid/filters/link_to_type>

**Description:** "Generates an HTML `<a>` tag with an `href` attribute linking to a collection page that lists all products of the given product type."

### Syntax

```liquid
string | link_to_type
```

**Returns:** string

### Basic Usage

#### Code

```liquid
{{ 'Health' | link_to_type }}
```

#### Output

```html
<a href="/collections/types?q=Health" title="Health">Health</a>
```

### HTML Attributes

You can specify HTML attributes by including a parameter matching the attribute name and desired value.

#### Syntax

```liquid
string | link_to_type: attribute: string
```

#### Code

```liquid
{{ 'Health' | link_to_type: class: 'link-class' }}
```

#### Output

```html
<a class="link-class" href="/collections/types?q=Health" title="Health">Health</a>
```

---

## collection — link_to_vendor

> Fonte: <https://shopify.dev/docs/api/liquid/filters/link_to_vendor>

**Description:** "Generates an HTML `<a>` tag with an `href` attribute linking to a collection page that lists all products of a given product vendor."

### Syntax

```liquid
string | link_to_vendor
```

**Returns:** `string`

### Basic Usage

#### Code

```liquid
{{ "Polina's Potent Potions" | link_to_vendor }}
```

#### Output

```html
<a href="/collections/vendors?q=Polina%27s%20Potent%20Potions" title="Polina&#39;s Potent Potions">Polina's Potent Potions</a>
```

### HTML Attributes

You can specify HTML attributes by including a parameter matching the attribute name and desired value.

#### Syntax

```liquid
string | link_to_vendor: attribute: string
```

#### Code

```liquid
{{ "Polina's Potent Potions" | link_to_vendor: class: 'link-class' }}
```

#### Output

```html
<a class="link-class" href="/collections/vendors?q=Polina%27s%20Potent%20Potions" title="Polina&#39;s Potent Potions">Polina's Potent Potions</a>
```

---

## collection — sort_by

> Fonte: <https://shopify.dev/docs/api/liquid/filters/sort_by>

### Syntax

```liquid
string | sort_by: string
```

### Returns

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Description

Generates a collection URL with the provided `sort_by` parameter appended. This filter must be applied to the object property [`collection.url`](https://shopify.dev/docs/api/liquid/objects/collection#collection-url).

### Accepted Values

The filter accepts the following sorting options:

* `manual` (as defined in the [collection settings](https://help.shopify.com/manual/products/collections/collection-layout#change-the-sort-order-for-the-products-in-a-collection))
* `best-selling`
* `title-ascending`
* `title-descending`
* `price-ascending`
* `price-descending`
* `created-ascending`
* `created-descending`

### Usage Tip

"You can append the sort_by filter to the url_for_type and url_for_vendor filters."

### Example

**Liquid:**

```liquid
{{ collection.url | sort_by: 'best-selling' }}
```

**Data:**

```json
{
  "collection": {
    "url": "/collections/sale-potions"
  }
}
```

**Output:**

```html
/collections/sale-potions?sort_by=best-selling
```

---

## collection — url_for_type

> Fonte: <https://shopify.dev/docs/api/liquid/filters/url_for_type>

### Syntax

```liquid
string | url_for_type
```

### Returns

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Description

"Generates a URL for a [collection page](https://shopify.dev/docs/storefronts/themes/architecture/templates/collection) that lists all products of the given product type."

### Example

**Input:**

```liquid
{{ 'health' | url_for_type }}
```

**Output:**

```html
/collections/types?q=health
```

---

## collection — url_for_vendor

> Fonte: <https://shopify.dev/docs/api/liquid/filters/url_for_vendor>

### Description

"Generates a URL for a collection page that lists all products from the given product vendor."

### Syntax

```liquid
string | url_for_vendor
```

### Returns

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Example

**Input:**

```liquid
{{ "Polina's Potent Potions" | url_for_vendor }}
```

**Output:**

```html
/collections/vendors?q=Polina%27s%20Potent%20Potions
```

---

## collection — within

> Fonte: <https://shopify.dev/docs/api/liquid/filters/within>

### Syntax

```liquid
string | within: collection
```

### Returns

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Description

Generates a product URL within the context of the provided collection.

When the collection context is included, you can access the associated [`collection` object](https://shopify.dev/docs/api/liquid/objects/collection) in the [product template](https://shopify.dev/themes/architecture/templates/product).

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `collection` | collection | The collection object used to generate the product URL |

### Caution

"Because a standard product page and a product page in the context of a collection have the same content on separate URLs, you should consider the SEO implications of using the within filter."

### Example

**Input:**

```liquid
{%- assign collection_product = collection.products.first -%}

{{ collection_product.url | within: collection }}
```

**Data:**

```json
{
  "collection": {
    "products": [
      {
        "url": "/products/draught-of-immortality"
      },
      {
        "url": "/products/glacier-ice"
      },
      {
        "url": "/products/health-potion"
      },
      {
        "url": "/products/invisibility-potion"
      }
    ]
  }
}
```

**Output:**

```html
/collections/sale-potions/products/draught-of-immortality
```

---

## color — brightness_difference

> Fonte: <https://shopify.dev/docs/api/liquid/filters/brightness_difference>

### Syntax

```liquid
string | brightness_difference: string
```

### Returns

[number](https://shopify.dev/docs/api/liquid/basics#number)

### Description

Calculates the perceived brightness difference between two colors, using the W3C standard for color contrast evaluation.

> "For accessibility best practices, it's recommended to have a minimum brightness difference of 125."

### Example

**Input:**

```liquid
{{ '#E800B0' | brightness_difference: '#FECEE9' }}
```

**Output:**

```html
134
```

---

## color — color_brightness

> Fonte: <https://shopify.dev/docs/api/liquid/filters/color_brightness>

### Syntax

```liquid
string | color_brightness
```

### Returns

[number](https://shopify.dev/docs/api/liquid/basics#number)

### Description

Calculates the "perceived brightness" of a given color using the W3C accessibility contrast formula.

### Example

**Input:**

```liquid
{{ '#EA5AB9' | color_brightness }}
```

**Output:**

```html
143.89
```

---

## color — color_contrast

> Fonte: <https://shopify.dev/docs/api/liquid/filters/color_contrast>

### Syntax

```liquid
string | color_contrast: string
```

### Returns

[number](https://shopify.dev/docs/api/liquid/basics#number)

### Description

"Calculates the contrast ratio between two colors and returns the ratio's numerator. The ratio's denominator, which isn't returned, is always 1. For example, with a contrast ratio of 3.5:1, this filter returns 3.5."

The sequence of color arguments does not affect the result.

### Accessibility Guidelines

For accessible design compliance, these standards apply:

- **WCAG 2.0 Level AA**: Minimum 4.5:1 contrast for standard text; 3:1 for large text
- **WCAG 2.0 Level AAA**: Minimum 7:1 contrast for standard text; 4.5:1 for large text

### Examples

#### Input

```liquid
{{ '#E800B0' | color_contrast: '#D9D8FF' }}
```

#### Output

```html
3.0
```

---

## color — color_darken

> Fonte: <https://shopify.dev/docs/api/liquid/filters/color_darken>

### Description

"Darkens a given color by a specific percentage. The percentage must be between 0 and 100."

### Syntax

```liquid
string | color_darken: number
```

### Parameters

- **number** (required): The percentage by which to darken the color, ranging from 0 to 100

### Returns

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Example

**Input:**

```liquid
{{ '#EA5AB9' | color_darken: 30 }}
```

**Output:**

```html
#98136b
```

---

## color — color_desaturate

> Fonte: <https://shopify.dev/docs/api/liquid/filters/color_desaturate>

### Syntax

```liquid
string | color_desaturate: number
```

### Returns

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Description

"Desaturates a given color by a specific percentage. The percentage must be between 0 and 100."

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| percentage | number | The desaturation amount, ranging from 0 to 100 |

### Example

**Input:**

```liquid
{{ '#EA5AB9' | color_desaturate: 30 }}
```

**Output:**

```html
#ce76b0
```

---

## color — color_difference

> Fonte: <https://shopify.dev/docs/api/liquid/filters/color_difference>

### Syntax

```liquid
string | color_difference: string
```

**Returns:** [number](https://shopify.dev/docs/api/liquid/basics#number)

### Description

Calculates the [color difference](https://www.w3.org/WAI/ER/WD-AERT/#color-contrast) between two colors.

> **Tip:** For accessibility best practices, it's recommended to have a minimum color difference of 500.

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| (second color) | string | The color to compare against the input color |

### Examples

**Input:**

```liquid
{{ '#720955' | color_difference: '#FFF3F9' }}
```

**Output:**

```html
539
```

---

## color — color_extract

> Fonte: <https://shopify.dev/docs/api/liquid/filters/color_extract>

### Syntax

```liquid
string | color_extract: string
```

### Returns

[number](https://shopify.dev/docs/api/liquid/basics#number)

### Description

"Extracts a specific color component from a given color."

### Accepted Color Components

The filter works with the following color component values:

* `alpha`
* `red`
* `green`
* `blue`
* `hue`
* `saturation`
* `lightness`

### Example

**Input:**

```liquid
{{ '#EA5AB9' | color_extract: 'red' }}
```

**Output:**

```html
234
```

---

## color — color_lighten

> Fonte: <https://shopify.dev/docs/api/liquid/filters/color_lighten>

### Syntax

```liquid
string | color_lighten: number
```

### Returns

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Description

"Lightens a given color by a specific percentage. The percentage must be between 0 and 100."

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| percentage | number | The amount to lighten the color, ranging from 0 to 100 |

### Examples

#### Input

```liquid
{{ '#EA5AB9' | color_lighten: 30 }}
```

#### Output

```html
#fbe2f3
```

---

## color — color_mix

> Fonte: <https://shopify.dev/docs/api/liquid/filters/color_mix>

### Syntax

```liquid
string | color_mix: string, number
```

### Returns

`string`

### Description

"Blends two colors together by a specific percentage factor. The percentage must be between 0 and 100."

### Parameters

- **color** (string): The second color to blend with the filtered color
- **percentage** (number): The blend factor, ranging from 0 to 100

### Tips

"A percentage factor of 100 returns the color being filtered. A percentage factor of 0 returns the color supplied to the filter."

### Examples

#### Example 1: Blending two hex colors at 50%

**Input:**

```liquid
{{ '#E800B0' | color_mix: '#00936F', 50 }}
```

**Output:**

```html
#744a90
```

#### Example 2: Blending with alpha transparency

When one input includes an alpha component and the other does not, an alpha value of 1.0 is assumed for the input lacking an alpha component.

**Input:**

```liquid
{{ 'rgba(232, 0, 176, 0.75)' | color_mix: '#00936F', 50 }}
```

**Output:**

```html
rgba(116, 74, 144, 0.88)
```

---

## color — color_modify

> Fonte: <https://shopify.dev/docs/api/liquid/filters/color_modify>

### Syntax

```liquid
string | color_modify: string, number
```

### Returns

`string`

### Description

"Modifies a specific color component of a given color by a specific amount."

### Parameters

| Component | Value Range |
| --- | --- |
| `red`, `green`, `blue` | Integer between 0 and 255 |
| `alpha` | Decimal between 0 and 1 |
| `hue` | Integer between 0 and 360 |
| `saturation`, `lightness` | Integer between 0 and 100 |

### Examples

#### Modifying the red component

**Input:**

```liquid
{{ '#EA5AB9' | color_modify: 'red', 255 }}
```

**Output:**

```html
#ff5ab9
```

#### Modifying the alpha component

**Input:**

```liquid
{{ '#EA5AB9' | color_modify: 'alpha', 0.85 }}
```

**Output:**

```html
rgba(234, 90, 185, 0.85)
```

### Notes

"The format of the modified color depends on the component being modified. For example, if you modify the `alpha` component of a color in hexadecimal format, then the modified color will be in `rgba()` format."

---

## color — color_saturate

> Fonte: <https://shopify.dev/docs/api/liquid/filters/color_saturate>

### Syntax

```liquid
string | color_saturate: number
```

### Returns

`string`

### Description

"Saturates a given color by a specific percentage. The percentage must be between 0 and 100."

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| percentage | number | The saturation increase, ranging from 0 to 100 |

### Example

**Input:**

```liquid
{{ '#EA5AB9' | color_saturate: 30 }}
```

**Output:**

```html
#ff45c0
```

---

## color — color_to_hex

> Fonte: <https://shopify.dev/docs/api/liquid/filters/color_to_hex>

### Syntax

```liquid
string | color_to_hex
```

### Returns

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Description

"Converts a CSS color string to hexadecimal format (`hex6`)."

Since colors are converted to the `hex6` format, any alpha component in a provided color will be removed from the output.

### Example

**Input:**

```liquid
{{ 'rgb(234, 90, 185)' | color_to_hex }}
```

**Output:**

```html
#ea5ab9
```

---

## color — color_to_hsl

> Fonte: <https://shopify.dev/docs/api/liquid/filters/color_to_hsl>

**Description:** "Converts a CSS color string to `HSL` format." If the color includes an alpha component, it becomes `HSLA` format.

### Syntax

```liquid
string | color_to_hsl
```

### Returns

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Example

**Input:**

```liquid
{{ '#EA5AB9' | color_to_hsl }}
```

**Output:**

```html
hsl(320, 77%, 64%)
```

---

## color — color_to_oklch

> Fonte: <https://shopify.dev/docs/api/liquid/filters/color_to_oklch>

### Description

"Converts a CSS color string to `OKLCH` format."

### Syntax

```liquid
string | color_to_oklch
```

### Returns

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Example

#### Input

```liquid
{{ '#EA5AB9' | color_to_oklch }}
```

#### Output

```html
oklch(68% 0.2 343 / 1.0)
```

---

## color — color_to_rgb

> Fonte: <https://shopify.dev/docs/api/liquid/filters/color_to_rgb>

**Description:** "Converts a CSS color string to `RGB` format." If the color includes an alpha component, the output becomes `RGBA` format.

### Syntax

```liquid
string | color_to_rgb
```

**Returns:** string

### Examples

#### Basic RGB conversion

**Input:**

```liquid
{{ '#EA5AB9' | color_to_rgb }}
```

**Output:**

```html
rgb(234, 90, 185)
```

---

## color — hex_to_rgba

> Fonte: <https://shopify.dev/docs/api/liquid/filters/hex_to_rgba>

**Description:**

"Converts a CSS color string from hexadecimal format to `RGBA` format. Shorthand hexadecimal formatting (`hex3`) is also accepted."

### Syntax

```liquid
string | hex_to_rgba
```

**Returns:** string

### Basic Usage

```liquid
{{ '#EA5AB9' | hex_to_rgba }}
```

**Output:**

```html
rgba(234,90,185,1)
```

### Parameters

#### alpha

```liquid
string | hex_to_rgba: number
```

An optional decimal parameter between 0.0 and 1.0 that sets transparency. Defaults to 1.0.

**Example:**

```liquid
{{ '#EA5AB9' | hex_to_rgba: 0.5 }}
```

**Output:**

```html
rgba(234,90,185,0.5)
```

### Deprecation Notice

"The `hex_to_rgba` filter has been replaced by [`color_to_rgb`](https://shopify.dev/docs/api/liquid/filters/color_to_rgb) and [`color_modify`](https://shopify.dev/docs/api/liquid/filters/color_modify)."

---

## customer — avatar

> Fonte: <https://shopify.dev/docs/api/liquid/filters/avatar>

### Description

"Generates HTML to render a customer's avatar, if available."

### Syntax

```liquid
customer | avatar
```

### Returns

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Usage

```liquid
{{ customer | avatar }}
```

### Tips

Use the `customer.has_avatar?` method to check whether a customer has an avatar before rendering.

---

## customer — customer_login_link

> Fonte: <https://shopify.dev/docs/api/liquid/filters/customer_login_link>

### Description

"Generates an HTML link to the customer login page."

### Syntax

```liquid
string | customer_login_link
```

### Returns

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Example

**Input:**

```liquid
{{ 'Log in' | customer_login_link }}
```

**Output:**

```html
<a href="/account/login" id="customer_login_link">Log in</a>
```

---

## customer — customer_logout_link

> Fonte: <https://shopify.dev/docs/api/liquid/filters/customer_logout_link>

**Description:** "Generates an HTML link to log the customer out of their account and redirect to the homepage."

### Syntax

```liquid
string | customer_logout_link
```

### Return Type

Returns a [string](https://shopify.dev/docs/api/liquid/basics#string)

### Example

**Input:**

```liquid
{{ 'Log out' | customer_logout_link }}
```

**Output:**

```html
<a href="/account/logout" id="customer_logout_link">Log out</a>
```

---

## customer — customer_register_link

> Fonte: <https://shopify.dev/docs/api/liquid/filters/customer_register_link>

### Syntax

```liquid
string | customer_register_link
```

### Returns

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Description

"Generates an HTML link to the customer registration page."

### Example

#### Input

```liquid
{{ 'Create an account' | customer_register_link }}
```

#### Output

```html
<a href="/account/register" id="customer_register_link">Create an account</a>
```

---

## customer — login_button

> Fonte: <https://shopify.dev/docs/api/liquid/filters/login_button>

### Description

"Generates an HTML Button that enables a customer to either sign in to the storefront using their Shop account or follow the shop in the Shop App."

### Syntax

```liquid
shop | login_button
```

### Returns

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Parameters

#### action

Controls the button's behavior following authentication.

**Type:** string

**Accepted values:**

- `default` - Authentication only
- `follow` - Performs a side-effect after authentication which follows the current shop in the Shop app. Requires additional configuration. [Learn more](https://help.shopify.com/manual/online-store/themes/customizing-themes/follow-on-shop)

**Syntax:**

```liquid
shop | login_button: action: string
```

**Example:**

```liquid
{{ shop | login_button: action: 'follow' }}
```

### Notes

"The presence of the shop object is required for validation purposes only."

---

## default — default

> Fonte: <https://shopify.dev/docs/api/liquid/filters/default>

### Description

"Sets a default value for any variable whose value is one of the following: `empty`, `false`, or `nil`"

### Syntax

```liquid
variable | default: variable
```

### Parameters

#### Basic Usage
- **variable** (required): The default value to use when the input is empty, false, or nil

#### allow_false

```liquid
variable | default: variable, allow_false: boolean
```

- **allow_false** (boolean, optional): When set to `true`, allows `false` values to be returned instead of being replaced with the default value. By default, this parameter is `false`.

### Examples

#### Basic Example

**Input:**

```liquid
{{ product.selected_variant.url | default: product.url }}
```

**Data:**

```json
{
  "product": {
    "selected_variant": null,
    "url": "/products/health-potion"
  }
}
```

**Output:**

```html
/products/health-potion
```

#### Using allow_false

**Input:**

```liquid
{%- assign display_price = false -%}

{{ display_price | default: true, allow_false: true }}
```

**Output:**

```html
false
```

---

## default — default_errors

> Fonte: <https://shopify.dev/docs/api/liquid/filters/default_errors>

### Syntax

```liquid
string | default_errors
```

### Returns

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Description

This filter generates default error messages for each possible value of [`form.errors`](https://shopify.dev/docs/themes/liquid/reference/objects/form#form-errors).

The `default_errors` filter processes form error objects and produces standardized error messages corresponding to each error type that may occur in a form submission.

**Related Reference:** For details on form error values, see [`form.errors`](https://shopify.dev/docs/themes/liquid/reference/objects/form#form-errors).

> Nota di estrazione: la pagina reference di Shopify per questo filtro contiene la definizione, la sintassi e il valore restituito, ma non include esempi di codice con relativo output renderizzato.

---

## default — default_pagination

> Fonte: <https://shopify.dev/docs/api/liquid/filters/default_pagination>

### Description

"Generates HTML for a set of links for paginated results. Must be applied to the `paginate` object."

### Syntax

```liquid
paginate | default_pagination
```

### Return Type

String

### Parameters

#### previous

```liquid
paginate | default_pagination: previous: string
```

Specify the text for the previous page link.

#### next

```liquid
paginate | default_pagination: next: string
```

Specify the text for the next page link.

#### anchor

```liquid
paginate | default_pagination: anchor: string
```

Specify the anchor to add to the pagination links.

### Examples

#### Basic Usage

**Liquid Input:**

```liquid
{% paginate collection.products by 2 %}
  {% for product in collection.products %}
    {{- product.title }}
  {% endfor %}

  {{- paginate | default_pagination -}}
{% endpaginate %}
```

**Output:**

```html
Draught of Immortality
  
Glacier ice
  
<span class="page current">1</span> <span class="page"><a href="/services/liquid_rendering/resource?page=2" title="">2</a></span> <span class="next"><a href="/services/liquid_rendering/resource?page=2" title="">Next &raquo;</a></span>
```

#### With Previous Parameter

**Liquid Input:**

```liquid
{% paginate collection.products by 2 %}
  {% for product in collection.products %}
    {{- product.title }}
  {% endfor %}

  {{- paginate | default_pagination: previous: 'Previous' -}}
{% endpaginate %}
```

**Output:**

```html
Draught of Immortality
  
Glacier ice
  
<span class="page current">1</span> <span class="page"><a href="/services/liquid_rendering/resource?page=2" title="">2</a></span> <span class="next"><a href="/services/liquid_rendering/resource?page=2" title="">Next &raquo;</a></span>
```

#### With Next Parameter

**Liquid Input:**

```liquid
{% paginate collection.products by 2 %}
  {% for product in collection.products %}
    {{- product.title }}
  {% endfor %}

  {{- paginate | default_pagination: next: 'Next' -}}
{% endpaginate %}
```

**Output:**

```html
Draught of Immortality
  
Glacier ice
  
<span class="page current">1</span> <span class="page"><a href="/services/liquid_rendering/resource?page=2" title="">2</a></span> <span class="next"><a href="/services/liquid_rendering/resource?page=2" title="">Next</a></span>
```

#### With Anchor Parameter

**Liquid Input:**

```liquid
{% paginate collection.products by 2 %}
  {% for product in collection.products %}
    {{- product.title }}
  {% endfor %}

  <div id="pagination">
    {{- paginate | default_pagination: anchor: 'pagination' -}}
  </div>
{% endpaginate %}
```

**Output:**

```html
Draught of Immortality
  
Glacier ice
  

  <div id="pagination"><span class="page current">1</span> <span class="page"><a href="/services/liquid_rendering/resource?page=2#pagination" title="">2</a></span> <span class="next"><a href="/services/liquid_rendering/resource?page=2#pagination" title="">Next &raquo;</a></span></div>
```

---

## font — font_face

> Fonte: <https://shopify.dev/docs/api/liquid/filters/font_face>

### Description

"Generates a CSS [`@font_face` declaration](https://developer.mozilla.org/en-US/docs/Web/CSS/%40font-face) to load the provided font."

### Syntax

```liquid
font | font_face
```

### Return Type

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Parameters

#### font_display (optional)

**Type:** string

You can include an optional parameter to specify the [`font_display` property](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-display) of the `@font_face` declaration.

### Examples

#### Basic Usage

**Liquid:**

```liquid
{{ settings.type_header_font | font_face }}
```

**Data:**

```json
{
  "settings": {
    "type_header_font": {}
  }
}
```

**Output:**

```css
@font-face {
  font-family: Assistant;
  font-weight: 400;
  font-style: normal;
  src: url("//polinas-potent-potions.myshopify.com/cdn/fonts/assistant/assistant_n4.9120912a469cad1cc292572851508ca49d12e768.woff2") format("woff2"),
       url("//polinas-potent-potions.myshopify.com/cdn/fonts/assistant/assistant_n4.6e9875ce64e0fefcd3f4446b7ec9036b3ddd2985.woff") format("woff");
}
```

#### With font_display Parameter

**Liquid:**

```liquid
{{ settings.type_header_font | font_face: font_display: 'swap' }}
```

**Data:**

```json
{
  "settings": {
    "type_header_font": {}
  }
}
```

**Output:**

```css
@font-face {
  font-family: Assistant;
  font-weight: 400;
  font-style: normal;
  font-display: swap;
  src: url("//polinas-potent-potions.myshopify.com/cdn/fonts/assistant/assistant_n4.9120912a469cad1cc292572851508ca49d12e768.woff2") format("woff2"),
       url("//polinas-potent-potions.myshopify.com/cdn/fonts/assistant/assistant_n4.6e9875ce64e0fefcd3f4446b7ec9036b3ddd2985.woff") format("woff");
}
```

---

## font — font_modify

> Fonte: <https://shopify.dev/docs/api/liquid/filters/font_modify>

### Syntax

```liquid
font | font_modify: string, string
```

### Returns

[font](https://shopify.dev/docs/api/liquid/objects/font)

### Description

Modifies a specific property of a given font. The `font_modify` filter requires two parameters: the first indicates which property should be modified, and the second specifies either the new value or modification amount.

### Parameters

| Property | Modification value | Output |
|----------|-------------------|--------|
| `style` | `normal` | Returns the normal variant of the same weight, if it exists. |
| | `italic` | Returns the italic variant of the same weight, if it exists. |
| | `oblique` | Returns the oblique variant of the same weight, if it exists. Oblique variants are similar to italic variants in appearance. All Shopify fonts have only oblique or italic variants, not both. |
| `weight` | `100` → `900` | Returns a variant of the same style with the given weight, if it exists. |
| | `normal` | Returns a variant of the same style with a weight of `400`, if it exists. |
| | `bold` | Returns a variant of the same style with a weight of `700`, if it exists. |
| | `+100` → `+900` | Returns a variant of the same style with a weight incremented by the given value, if it exists. For example, if a font has a weight of `400`, then using `+100` would return the font with a weight of `500`. |
| | `-100` → `-900` | Returns a variant of the same style with a weight decremented by the given value, if it exists. For example, if a font has a weight of `400`, then using `-100` would return the font with a weight of `300`. |
| | `lighter` | Returns a lighter variant of the same style by applying CSS `font-weight` rules and browser fallback weights, if it exists. |
| | `bolder` | Returns a bolder variant of the same style by applying CSS `font-weight` rules and browser fallback weights, if it exists. |

### Examples

#### Basic Example

**Input:**

```liquid
{%- assign bold_font = settings.type_body_font | font_modify: 'weight', 'bold' -%}

h2 {
  font-weight: {{ bold_font.weight }};
}
```

**Data:**

```json
{
  "settings": {
    "type_body_font": {}
  }
}
```

**Output:**

```html
h2 {
  font-weight: 700;
}
```

#### Handling Non-Existent Variants

**Input:**

```liquid
{%- assign bold_font = settings.type_body_font | font_modify: 'weight', 'bold' -%}
{%- assign italic_font = settings.type_body_font | font_modify: 'style', 'italic' -%}
{%- assign heavy_font = settings.type_body_font | font_modify: 'weight', '900' | default: bold_font -%}
{%- assign oblique_font = settings.type_body_font | font_modify: 'style', 'oblique' | default: italic_font -%}

h2 {
  font-style: {{ heavy_font.weight }};
}

.italic {
  {% if oblique_font -%}
    font-style: {{ oblique_font.style }};
  {%- else -%}
    font-style: {{ italic_font.style }};
  {%- endif %}
}
```

**Data:**

```json
{
  "settings": {
    "type_body_font": {}
  }
}
```

**Output:**

```html
h2 {
  font-style: 700;
}

.italic {
  font-style: ;
}
```

### Notes

If `font_modify` attempts to create a non-existent font variant, it returns `nil`. Handle this using the [`default` filter](https://shopify.dev/docs/api/liquid/filters/default) or by checking for `nil` before using the variant.

---

## font — font_url

> Fonte: <https://shopify.dev/docs/api/liquid/filters/font_url>

### Description

"Returns the CDN URL for the provided font in `woff2` format."

### Syntax

```liquid
font | font_url
```

```liquid
font | font_url: string
```

### Returns

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| (optional) | string | Font format: `woff` or `woff2` (default) |

### Examples

#### Default woff2 Format

**Liquid**

```liquid
{{ settings.type_header_font | font_url }}
```

**Data**

```json
{
  "settings": {
    "type_header_font": {}
  }
}
```

**Output**

```html
//polinas-potent-potions.myshopify.com/cdn/fonts/assistant/assistant_n4.9120912a469cad1cc292572851508ca49d12e768.woff2
```

#### woff Format

**Liquid**

```liquid
{{ settings.type_header_font | font_url: 'woff' }}
```

**Data**

```json
{
  "settings": {
    "type_header_font": {}
  }
}
```

**Output**

```html
//polinas-potent-potions.myshopify.com/cdn/fonts/assistant/assistant_n4.6e9875ce64e0fefcd3f4446b7ec9036b3ddd2985.woff
```

---

## format — date

> Fonte: <https://shopify.dev/docs/api/liquid/filters/date>

Converts a timestamp into another date format.

### Syntax

```liquid
string | date: string
```

**Returns:** `string`

### Description

"The `date` filter accepts the same parameters as Ruby's strftime method for formatting the date." For available format codes, see the [Ruby documentation](https://ruby-doc.org/core-3.1.1/Time.html#method-i-strftime) or [strftime reference](http://www.strfti.me/).

### Basic Usage

**Input:**

```liquid
{{ article.created_at | date: '%B %d, %Y' }}
```

**Data:**

```json
{
  "article": {
    "created_at": "2022-04-14 16:56:02 -0400"
  }
}
```

**Output:**

```
April 14, 2022
```

### Current Date

Apply the filter to `'now'` or `'today'` to output the current timestamp.

> "The timestamp will reflect the time that the Liquid was last rendered. Because of this, the timestamp might not be updated for every page view, depending on the context and caching."

**Input:**

```liquid
{{ 'now' | date: '%B %d, %Y' }}
```

### Locale-Aware Format Parameter

```liquid
string | date: format: string
```

Use predefined locale-aware formats:

* `abbreviated_date`
* `basic`
* `date`
* `date_at_time`
* `default`
* `on_date`
* `short` (deprecated)
* `long` (deprecated)

**Input:**

```liquid
{{ article.created_at | date: format: 'abbreviated_date' }}
```

**Data:**

```json
{
  "article": {
    "created_at": "2022-04-14 16:56:02 -0400"
  }
}
```

**Output:**

```
Apr 14, 2022
```

### Custom Formats in Locale Files

Define custom date formats in your theme's storefront locale files under a `date_formats` category:

```json
"date_formats": {
  "month_day_year": "%B %d, %Y"
}
```

**Input:**

```liquid
{{ article.created_at | date: format: 'month_day_year' }}
```

**Data:**

```json
{
  "article": {
    "created_at": "2022-04-14 16:56:02 -0400"
  }
}
```

**Output:**

```
April 14, 2022
```

---

## format — json

> Fonte: <https://shopify.dev/docs/api/liquid/filters/json>

```liquid
variable | json
```

**Returns:** string

Converts a string, or object, into JSON format.

---

### Tip

When using JSON output in JavaScript, you don't need to wrap it in quotes because the `json` filter includes them. The `json` filter also escapes any quotes inside the output.

---

### Product inventory

When applied to a `product` object on any Shopify store created after December 5, 2017, the `json` filter doesn't output values for the `inventory_quantity` and `inventory_policy` properties of associated variants. These properties are excluded to help prevent bots and crawlers from retrieving inventory quantities for stores to which they aren't granted access.

If you need inventory information, you can access it through individual variants.

#### Example

**Input:**

```liquid
{{ product | json }}
```

**Output:**

```json
{"id":6792602320961,"title":"Crocodile tears","handle":"crocodile-tears","description":"","published_at":"2022-04-22T11:55:58-04:00","created_at":"2022-04-22T11:55:56-04:00","vendor":"Polina's Potent Potions","type":"","tags":["Salty"],"price":5600,"price_min":5600,"price_max":5600,"available":false,"price_varies":false,"compare_at_price":null,"compare_at_price_min":0,"compare_at_price_max":0,"compare_at_price_varies":false,"variants":[{"id":39888242344001,"title":"Default Title","option1":"Default Title","option2":null,"option3":null,"sku":"","requires_shipping":true,"taxable":true,"featured_image":null,"available":false,"name":"Crocodile tears","public_title":null,"options":["Default Title"],"price":5600,"weight":0,"compare_at_price":null,"inventory_management":"shopify","barcode":"","requires_selling_plan":false,"selling_plan_allocations":[],"quantity_rule":{"min":1,"max":null,"increment":1}}],"images":["//polinas-potent-potions.myshopify.com/cdn/shop/products/amber-beard-oil-bottle.jpg?v=1650642958"],"featured_image":"//polinas-potent-potions.myshopify.com/cdn/shop/products/amber-beard-oil-bottle.jpg?v=1650642958","options":["Title"],"media":[{"alt":null,"id":21772501975105,"position":1,"preview_image":{"aspect_ratio":1.5,"height":2974,"width":4460,"src":"//polinas-potent-potions.myshopify.com/cdn/shop/products/amber-beard-oil-bottle.jpg?v=1650642958"},"aspect_ratio":1.5,"height":2974,"media_type":"image","src":"//polinas-potent-potions.myshopify.com/cdn/shop/products/amber-beard-oil-bottle.jpg?v=1650642958","width":4460}],"requires_selling_plan":false,"selling_plan_groups":[],"content":""}
```

---

## format — structured_data

> Fonte: <https://shopify.dev/docs/api/liquid/filters/structured_data>

### Description

"Converts an object into a schema.org structured data format."

### Syntax

```liquid
variable | structured_data
```

### Return Type

Returns a [string](https://shopify.dev/docs/api/liquid/basics#string)

### Usage

The `structured_data` filter works with the [`product`](https://shopify.dev/docs/api/liquid/objects/product) and [`article`](https://shopify.dev/docs/api/liquid/objects/article) objects.

**Output behavior:**
- Product objects without variants render as a [schema.org `Product`](https://schema.org/Product)
- Product objects with one or more variants render as a [`ProductGroup`](https://schema.org/ProductGroup)
- Article objects render as a [schema.org `Article`](https://schema.org/Article)

### Example

**Input:**

```liquid
<script type="application/ld+json">
  {{ product | structured_data }}
</script>
```

**Output:**

```html
<script type="application/ld+json">
  {"@context":"http:\/\/schema.org\/","@id":"\/products\/crocodile-tears#product","@type":"Product","brand":{"@type":"Brand","name":"Polina's Potent Potions"},"category":"","description":"","image":"https:\/\/polinas-potent-potions.myshopify.com\/cdn\/shop\/products\/amber-beard-oil-bottle.jpg?v=1650642958&width=1920","name":"Crocodile tears","offers":{"@id":"\/products\/crocodile-tears?variant=39888242344001#offer","@type":"Offer","availability":"http:\/\/schema.org\/OutOfStock","price":"56.00","priceCurrency":"CAD","url":"https:\/\/polinas-potent-potions.myshopify.com\/products\/crocodile-tears?variant=39888242344001"},"url":"https:\/\/polinas-potent-potions.myshopify.com\/products\/crocodile-tears"}
</script>
```

---

## format — weight_with_unit

> Fonte: <https://shopify.dev/docs/api/liquid/filters/weight_with_unit>

### Syntax

```liquid
number | weight_with_unit
```

### Returns

`string`

### Description

"Generates a formatted weight for a [`variant` object](https://shopify.dev/docs/api/liquid/objects/variant#variant-weight)." The weight unit comes from your store's general settings in the Shopify admin.

### Basic Usage

#### Code

```liquid
{%- assign variant = product.variants.first -%}

{{ variant.weight | weight_with_unit }}
```

#### Data

```json
{
  "product": {
    "variants": [
      {
        "weight": 200
      },
      {
        "weight": 200
      },
      {
        "weight": 400
      },
      {
        "weight": 200
      }
    ]
  }
}
```

#### Output

```html
0.2 kg
```

### Override the Default Unit

#### Syntax

```liquid
number | weight_with_unit: variable
```

Override the default unit from your store settings by specifying a custom unit.

#### Code

```liquid
{%- assign variant = product.variants.first -%}

{{ variant.weight | weight_with_unit: variant.weight_unit }}
```

#### Data

```json
{
  "product": {
    "variants": [
      {
        "weight": 200,
        "weight_unit": "g"
      },
      {
        "weight": 200,
        "weight_unit": "g"
      },
      {
        "weight": 400,
        "weight_unit": "g"
      },
      {
        "weight": 200,
        "weight_unit": "g"
      }
    ]
  }
}
```

#### Output

```html
200 g
```

---

## hosted_file — asset_img_url

> Fonte: <https://shopify.dev/docs/api/liquid/filters/asset_img_url>

### Description

"Returns the CDN URL for an image in the assets directory of a theme."

### Syntax

```liquid
string | asset_img_url
```

**Returns:** string

### Basic Usage

#### Code

```liquid
{{ 'red-and-black-bramble-berries.jpg' | asset_img_url }}
```

#### Output

```html
//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/red-and-black-bramble-berries_small.jpg?v=337
```

### Parameters

#### size

**Syntax:**

```liquid
image | asset_img_url: string
```

By default, this filter returns the `small` version of an image (100 x 100 px). You can specify an alternative [size](https://shopify.dev/docs/api/liquid/filters/img_url#img_url-size) parameter.

##### Code

```liquid
{{ 'red-and-black-bramble-berries.jpg' | asset_img_url: 'large' }}
```

##### Output

```html
//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/red-and-black-bramble-berries_large.jpg?v=337
```

---

## hosted_file — asset_url

> Fonte: <https://shopify.dev/docs/api/liquid/filters/asset_url>

### Syntax

```liquid
string | asset_url
```

### Returns

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Description

Generates the [CDN URL](https://shopify.dev/themes/best-practices/performance/platform#shopify-cdn) pointing to a file located in a theme's [`assets` directory](https://shopify.dev/themes/architecture#assets).

### Example

#### Input

```liquid
{{ 'cart.js' | asset_url }}
```

#### Output

```html
//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/cart.js?v=83971781268232213281663872410
```

---

## hosted_file — file_img_url

> Fonte: <https://shopify.dev/docs/api/liquid/filters/file_img_url>

**Description:** "Returns the CDN URL for an image from the Files page of the Shopify admin."

### Syntax

```liquid
string | file_img_url
```

```liquid
image | file_img_url: string
```

### Return Type

Returns `string`

### Basic Usage

#### Example 1: Default Size

**Input:**

```liquid
{{ 'potions-header.png' | file_img_url }}
```

**Output:**

```html
//polinas-potent-potions.myshopify.com/cdn/shop/files/potions-header_small.png?v=4246568442683817558
```

### The size parameter

By default, this filter returns the `small` version of the image (100 x 100 px). You can specify an alternative size.

**Parameter:** `size` (string)

#### Example 2: Large Size

**Input:**

```liquid
{{ 'potions-header.png' | file_img_url: 'large' }}
```

**Output:**

```html
//polinas-potent-potions.myshopify.com/cdn/shop/files/potions-header_large.png?v=4246568442683817558
```

---

## hosted_file — file_url

> Fonte: <https://shopify.dev/docs/api/liquid/filters/file_url>

### Description

"Returns the CDN URL for a file from the Files page of the Shopify admin."

### Syntax

```liquid
string | file_url
```

### Returns

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Example

**Input:**

```liquid
{{ 'disclaimer.pdf' | file_url }}
```

**Output:**

```html
//polinas-potent-potions.myshopify.com/cdn/shop/files/disclaimer.pdf?v=9043651738044769859
```

---

## hosted_file — global_asset_url

> Fonte: <https://shopify.dev/docs/api/liquid/filters/global_asset_url>

### Description

"Returns the CDN URL for a global asset." Global assets are hosted on Shopify's servers and can provide faster loading than direct resource access.

### Syntax

```liquid
string | global_asset_url
```

### Returns

`string` - The CDN URL for the specified global asset

### Usage Notes

Depending on the resource type, additional filters may be required:

| Resource Type | Additional Filter |
|---|---|
| JavaScript (.js) | `script_tag` |
| CSS (.css) | `stylesheet_tag` |

### Available Global Assets

#### Firebug
- firebug/firebug.css
- firebug/firebug.html
- firebug/firebug.js
- firebug/firebugx.js
- firebug/errorIcon.png
- firebug/infoIcon.png
- firebug/warningIcon.png

#### JavaScript Libraries
- controls.js
- dragdrop.js
- effects.js
- ga.js
- mootools.js

#### Lightbox
- lightbox.css
- lightbox.js
- lightbox/v1/lightbox.css
- lightbox/v1/lightbox.js
- lightbox/v2/lightbox.css
- lightbox/v2/lightbox.js
- lightbox/v2/close.gif
- lightbox/v2/loading.gif
- lightbox/v2/overlay.png
- lightbox/v2/zoom-lg.gif
- lightbox/v204/lightbox.css
- lightbox/v204/lightbox.js
- lightbox/v204/bullet.gif
- lightbox/v204/close.gif
- lightbox/v204/closelabel.gif
- lightbox/v204/donatebutton.gif
- lightbox/v204/downloadicon.gif
- lightbox/v204/loading.gif
- lightbox/v204/nextlabel.png
- lightbox/v204/prevlabel.gif

#### Prototype
- prototype.js
- prototype/1.5/prototype.js
- prototype/1.6/prototype.js

#### script.aculo.us
- scriptaculous/1.8.2/scriptaculous.js
- scriptaculous/1.8.2/builder.js
- scriptaculous/1.8.2/controls.js
- scriptaculous/1.8.2/dragdrop.js
- scriptaculous/1.8.2/effects.js
- scriptaculous/1.8.2/slider.js
- scriptaculous/1.8.2/sound.js
- scriptaculous/1.8.2/unittest.js

#### Shopify
- list-collection.css
- textile.css

### Examples

#### Input

```liquid
{{ 'lightbox.js' | global_asset_url | script_tag }}

{{ 'lightbox.css' | global_asset_url | stylesheet_tag }}
```

#### Output

```html
<script src="//polinas-potent-potions.myshopify.com/cdn/s/global/lightbox.js" type="text/javascript"></script>

<link href="//polinas-potent-potions.myshopify.com/cdn/s/global/lightbox.css" rel="stylesheet" type="text/css" media="all" />
```

---

## hosted_file — img_tag

> Fonte: <https://shopify.dev/docs/api/liquid/filters/img_tag>

### Description

"Generates an HTML `<img>` tag for a given image URL."

### Syntax

```liquid
string | img_tag
```

### Return Type

Returns `string`

### Applicable Objects

This filter can be used on the following objects:

- `article`
- `collection`
- `image`
- `line_item`
- `product`
- `variant`

### Deprecation Notice

"The `img_tag` filter has been replaced by `image_tag`."

### Basic Usage

#### Example 1

**Input:**

```liquid
{{ product | img_tag }}
```

**Output:**

```html
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_small.jpg?v=1683744744" alt="" />
```

### Optional Parameters

```liquid
variable | img_tag: string, string, string
```

The filter accepts three unnamed parameters (in order):

1. **Alt text** (string) – Sets the `alt` attribute
2. **CSS class** (string) – Sets the `class` attribute
3. **Image size** (string) – Specifies the image dimensions

"Because the parameters are read in that order, you must include a value for each parameter before the last parameter you want to specify." Use empty strings to skip intermediate parameters.

#### Example 2

**Input:**

```liquid
{{ product | img_tag: 'image alt text', '', '450x450' }}
```

**Output:**

```html
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_450x450.jpg?v=1683744744" alt="image alt text" class="" />
```

### Important Note

The `size` parameter cannot be combined with the `img_url` filter. If both are applied, the `img_url` filter will take precedence.

---

## hosted_file — script_tag

> Fonte: <https://shopify.dev/docs/api/liquid/filters/script_tag>

```liquid
string | script_tag
```

**Returns:** [string](https://shopify.dev/docs/api/liquid/basics#string)

### Description

"Generates an HTML `<script>` tag for a given resource URL. The tag has a `type` attribute of `text/javascript`."

### Syntax

```liquid
{{ 'cart.js' | asset_url | script_tag }}
```

### Example Output

```html
<script src="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/cart.js?v=83971781268232213281663872410" type="text/javascript"></script>
```

---

## hosted_file — shopify_asset_url

> Fonte: <https://shopify.dev/docs/api/liquid/filters/shopify_asset_url>

### Syntax

```liquid
string | shopify_asset_url
```

### Returns

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Description

"Returns the CDN URL for a globally accessible Shopify asset."

The following assets are globally accessible through Shopify:

* `option_selection.js`
* `api.jquery.js`
* `shopify_common.js`
* `customer_area.js`
* `currencies.js`
* `customer.css`

### Examples

#### Input

```liquid
{{ 'option_selection.js' | shopify_asset_url }}
```

#### Output

```html
//polinas-potent-potions.myshopify.com/cdn/shopifycloud/storefront/assets/themes_support/option_selection-b017cd28.js
```

---

## hosted_file — stylesheet_tag

> Fonte: <https://shopify.dev/docs/api/liquid/filters/stylesheet_tag>

### Description

"Generates an HTML `<link>` tag for a given resource URL. The tag has the following parameters:"

| Attribute | Value |
| --- | --- |
| `rel` | `stylesheet` |
| `type` | `text/css` |
| `media` | `all` |

### Syntax

```liquid
string | stylesheet_tag
```

### Returns

`string`

### Examples

#### Basic Usage

**Input:**

```liquid
{{ 'base.css' | asset_url | stylesheet_tag }}
```

**Output:**

```html
<link href="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/base.css?v=88290808517547527771663872409" rel="stylesheet" type="text/css" media="all" />
```

### Parameters

#### preload

**Syntax:**

```liquid
stylesheet_url | stylesheet_tag: preload: boolean
```

**Description:**

"Specify whether the stylesheet should be preloaded. When `preload` is set to `true`, a resource hint is sent as a Link header with a `rel` value of `preload`."

```
Link: <STYLESHEET_URL>; rel=preload; as=style
```

"This option doesn't affect the HTML link tag directly. You should use the `preload` parameter sparingly. For example, consider preloading only render-blocking stylesheets that are needed for initial functionality of the page, such as above-the-fold content."

---

## html — class_list

> Fonte: <https://shopify.dev/docs/api/liquid/filters/class_list>

### Description

"Generates the list of style classes for a style setting or a collection of settings."

### Syntax

```liquid
settings.layout | class_list
```

### Returns

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Example

**Code:**

```liquid
{{ settings.layout | class_list }}
```

**Data:**

```json
{
  "settings": {
    "layout": {}
  }
}
```

**Output:**

```html
styles:layout:flex styles:settings:layout
```

> Nota di estrazione: la pagina reference diretta `…/filters/class_list` non è risultata raggiungibile via fetch automatico (HTTP 404 sul renderer usato); il contenuto qui riportato (descrizione, sintassi, esempio e output) proviene dalla documentazione ufficiale Shopify recuperata tramite ricerca su shopify.dev.

---

## html — escape

> Fonte: <https://shopify.dev/docs/api/liquid/filters/escape>

### Syntax

```liquid
string | escape
```

### Returns

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Description

This filter escapes special HTML characters including `<>`, `'`, and `&`, converting them into their corresponding escape sequences. Characters without an escape sequence remain unchanged.

### Example

**Input:**

```liquid
{{ '<p>Text to be escaped.</p>' | escape }}
```

**Output:**

```html
&lt;p&gt;Text to be escaped.&lt;/p&gt;
```

---

## html — highlight

> Fonte: <https://shopify.dev/docs/api/liquid/filters/highlight>

### Syntax

```liquid
string | highlight: string
```

### Returns

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Description

Wraps all instances of a specific string within a given string with an HTML `<strong>` tag having a `class` attribute of `highlight`.

### Example

#### Input

```liquid
{% for item in search.results %}
  {% if item.object_type == 'product' %}
    {{ item.description | highlight: search.terms }}
  {% else %}
    {{ item.content | highlight: search.terms }}
  {% endif %}
{% endfor %}
```

#### Data

```json
{
  "search": {
    "results": [
      {
        "description": "Some relaxing music to stir potions to!",
        "object_type": "product"
      },
      {
        "description": "",
        "object_type": "product"
      },
      {
        "description": "",
        "object_type": "product"
      },
      {
        "description": "This is a love potion.",
        "object_type": "product"
      },
      {
        "description": "",
        "object_type": "product"
      },
      {
        "description": "",
        "object_type": "product"
      },
      {
        "description": "",
        "object_type": "product"
      },
      {
        "description": "",
        "object_type": "product"
      },
      {
        "description": "",
        "object_type": "product"
      }
    ],
    "terms": "love"
  }
}
```

#### Output

```html
Some relaxing music to stir potions to!
  

  
    
  

  
    
  

  
    This is a <strong class="highlight">love</strong> potion.
```

---

## html — newline_to_br

> Fonte: <https://shopify.dev/docs/api/liquid/filters/newline_to_br>

### Description

"Converts newlines (`\n`) in a string to HTML line breaks (`<br>`)."

### Syntax

```liquid
string | newline_to_br
```

### Return Type

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Example

#### Input

**Liquid code:**

```liquid
{{ product.description | newline_to_br }}
```

**Data:**

```json
{
  "product": {
    "description": "<h3>Are you low on health? Well we've got the potion just for you!</h3>\n<p>Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!</p>"
  }
}
```

#### Output

```html
<h3>Are you low on health? Well we've got the potion just for you!</h3><br />
<p>Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!</p>
```

---

## html — strip_html

> Fonte: <https://shopify.dev/docs/api/liquid/filters/strip_html>

### Syntax

```liquid
string | strip_html
```

### Returns

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Description

"Strips all HTML tags from a string."

### Example

#### Liquid Input

```liquid
<!-- With HTML -->
{{ product.description }}

<!-- HTML stripped -->
{{ product.description | strip_html }}
```

#### Data

```json
{
  "product": {
    "description": "<h3>Are you low on health? Well we've got the potion just for you!</h3>\n<p>Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!</p>"
  }
}
```

#### Output

```html
<!-- With HTML -->
<h3>Are you low on health? Well we've got the potion just for you!</h3>
<p>Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!</p>

<!-- HTML stripped -->
Are you low on health? Well we've got the potion just for you!
Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!
```

---

## html — time_tag

> Fonte: <https://shopify.dev/docs/api/liquid/filters/time_tag>

**Description:** "Converts a timestamp into an HTML `<time>` tag."

### Syntax

```liquid
string | time_tag: string
```

**Returns:** string

### Basic Usage

The filter accepts the same parameters as Ruby's strftime method. Refer to the [Ruby documentation](https://ruby-doc.org/core-3.1.1/Time.html#method-i-strftime) or [strftime reference](http://www.strfti.me/) for formatting options.

#### Example

**Input:**

```liquid
{{ article.created_at | time_tag: '%B %d, %Y' }}
```

**Data:**

```json
{
  "article": {
    "created_at": "2022-04-14 16:56:02 -0400"
  }
}
```

**Output:**

```html
<time datetime="2022-04-14T20:56:02Z">April 14, 2022</time>
```

---

### Parameters

#### format

```liquid
string | time_tag: format: string
```

Specify a locale-aware date format. Accepts the following values:

- `abbreviated_date`
- `basic`
- `date`
- `date_at_time`
- `default`
- `on_date`
- `short` (deprecated)
- `long` (deprecated)

Custom formats can be defined in your theme's locale files.

**Example:**

**Input:**

```liquid
{{ article.created_at | time_tag: format: 'abbreviated_date' }}
```

**Data:**

```json
{
  "article": {
    "created_at": "2022-04-14 16:56:02 -0400"
  }
}
```

**Output:**

```html
<time datetime="2022-04-14T20:56:02Z">Apr 14, 2022</time>
```

#### datetime

```liquid
string | time_tag: datetime: string
```

Customize the format of the `datetime` attribute. By default, it uses `YYYY-MM-DDThh:mm:ssTZD`. Accepts strftime shorthand formats.

**Example:**

**Input:**

```liquid
{{ article.created_at | time_tag: '%B %d, %Y', datetime: '%Y-%m-%d' }}
```

**Data:**

```json
{
  "article": {
    "created_at": "2022-04-14 16:56:02 -0400"
  }
}
```

**Output:**

```html
<time datetime="2022-04-14">April 14, 2022</time>
```

---

### Custom Format in Locale Files

Define custom date formats in your theme's storefront locale files within a `date_formats` category:

```json
"date_formats": {
  "month_day_year": "%B %d, %Y"
}
```

**Example:**

**Input:**

```liquid
{{ article.created_at | time_tag: format: 'month_day_year' }}
```

**Data:**

```json
{
  "article": {
    "created_at": "2022-04-14 16:56:02 -0400"
  }
}
```

**Output:**

```html
<time datetime="2022-04-14T20:56:02Z">April 14, 2022</time>
```

---

## html — url_escape

> Fonte: <https://shopify.dev/docs/api/liquid/filters/url_escape>

### Syntax

```liquid
string | url_escape
```

### Returns

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Description

"Escapes any URL-unsafe characters in a string."

### Example

**Input:**

```liquid
{{ '<p>Health & Love potions</p>' | url_escape }}
```

**Output:**

```html
%3Cp%3EHealth%20&%20Love%20potions%3C/p%3E
```

---

## html — url_param_escape

> Fonte: <https://shopify.dev/docs/api/liquid/filters/url_param_escape>

**Description:** "Escapes any characters in a string that are unsafe for URL parameters."

### Syntax

```liquid
string | url_param_escape
```

### Returns

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Details

This filter escapes the same characters as [`url_escape`](https://shopify.dev/docs/api/liquid/filters/url_escape), with the addition of the ampersand character (`&`).

### Example

**Input:**

```liquid
{{ '<p>Health & Love potions</p>' | url_param_escape }}
```

**Output:**

```html
%3Cp%3EHealth%20%26%20Love%20potions%3C/p%3E
```

---

## localization — currency_selector

> Fonte: <https://shopify.dev/docs/api/liquid/filters/currency_selector>

### Overview

"Generates an HTML `<select>` element with an option for each currency available on the store."

**Return type:** string

### Syntax

```liquid
form | currency_selector
```

### Description

The `currency_selector` filter must be applied to the `form` object within a currency form.

#### Deprecation Notice

"Deprecated without a direct replacement because the currency form has also been deprecated." The currency form was superseded by the localization form. For implementing currency selection, refer to guidance on creating a country selector using the localization form.

### Parameters

#### class

Specify the `class` attribute of the `<select>` element.

**Type:** string

#### id

Specify the `id` attribute of the `<select>` element.

**Type:** string

### Examples

#### Basic Usage

**Liquid:**

```liquid
{% form 'currency' %}
  {{ form | currency_selector }}
{% endform %}
```

**Output:**

```html
<form method="post" action="/cart/update" id="currency_form" accept-charset="UTF-8" class="shopify-currency-form" enctype="multipart/form-data"><input type="hidden" name="form_type" value="currency" /><input type="hidden" name="utf8" value="✓" /><input type="hidden" name="return_to" value="/services/liquid_rendering/resource" />
  <select name="currency"><option value="AED">AED د.إ</option><option value="AFN">AFN ؋</option><option value="AUD">AUD $</option><option value="CAD" selected="selected">CAD $</option><option value="CHF">CHF CHF</option><option value="CZK">CZK Kč</option><option value="DKK">DKK kr.</option><option value="EUR">EUR €</option><option value="GBP">GBP £</option><option value="HKD">HKD $</option><option value="ILS">ILS ₪</option><option value="JPY">JPY ¥</option><option value="KRW">KRW ₩</option><option value="MYR">MYR RM</option><option value="NZD">NZD $</option><option value="PLN">PLN zł</option><option value="SEK">SEK kr</option><option value="SGD">SGD $</option><option value="USD">USD $</option></select>
</form>
```

#### With Custom Class

**Liquid:**

```liquid
{% form 'currency' %}
  {{ form | currency_selector: class: 'custom-class' }}
{% endform %}
```

**Output:**

```html
<form method="post" action="/cart/update" id="currency_form" accept-charset="UTF-8" class="shopify-currency-form" enctype="multipart/form-data"><input type="hidden" name="form_type" value="currency" /><input type="hidden" name="utf8" value="✓" /><input type="hidden" name="return_to" value="/services/liquid_rendering/resource" />
  <select class="custom-class" name="currency"><option value="AED">AED د.إ</option><option value="AFN">AFN ؋</option><option value="AUD">AUD $</option><option value="CAD" selected="selected">CAD $</option><option value="CHF">CHF CHF</option><option value="CZK">CZK Kč</option><option value="DKK">DKK kr.</option><option value="EUR">EUR €</option><option value="GBP">GBP £</option><option value="HKD">HKD $</option><option value="ILS">ILS ₪</option><option value="JPY">JPY ¥</option><option value="KRW">KRW ₩</option><option value="MYR">MYR RM</option><option value="NZD">NZD $</option><option value="PLN">PLN zł</option><option value="SEK">SEK kr</option><option value="SGD">SGD $</option><option value="USD">USD $</option></select>
</form>
```

#### With Custom ID

**Liquid:**

```liquid
{% form 'currency' %}
  {{ form | currency_selector: id: 'custom-id' }}
{% endform %}
```

**Output:**

```html
<form method="post" action="/cart/update" id="currency_form" accept-charset="UTF-8" class="shopify-currency-form" enctype="multipart/form-data"><input type="hidden" name="form_type" value="currency" /><input type="hidden" name="utf8" value="✓" /><input type="hidden" name="return_to" value="/services/liquid_rendering/resource" />
  <select id="custom-id" name="currency"><option value="AED">AED د.إ</option><option value="AFN">AFN ؋</option><option value="AUD">AUD $</option><option value="CAD" selected="selected">CAD $</option><option value="CHF">CHF CHF</option><option value="CZK">CZK Kč</option><option value="DKK">DKK kr.</option><option value="EUR">EUR €</option><option value="GBP">GBP £</option><option value="HKD">HKD $</option><option value="ILS">ILS ₪</option><option value="JPY">JPY ¥</option><option value="KRW">KRW ₩</option><option value="MYR">MYR RM</option><option value="NZD">NZD $</option><option value="PLN">PLN zł</option><option value="SEK">SEK kr</option><option value="SGD">SGD $</option><option value="USD">USD $</option></select>
</form>
```

---

## localization — format_address

> Fonte: <https://shopify.dev/docs/api/liquid/filters/format_address>

### Syntax

```liquid
address | format_address
```

### Returns

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Description

"Generates an HTML address display, with each address component ordered according to the address's locale."

### Examples

#### Example 1: Shop Address

**Liquid Code:**

```liquid
{{ shop.address | format_address }}
```

**Data:**

```json
{
  "shop": {
    "address": {}
  }
}
```

**Output:**

```html
<p>Polina&#39;s Potions, LLC<br>150 Elgin Street<br>8th floor<br>Ottawa ON K2P 1L4<br>Canada</p>
```

#### Example 2: Customer Default Address

**Liquid Code:**

```liquid
{{ customer.default_address | format_address }}
```

**Data:**

```json
{
  "customer": {
    "default_address": {}
  }
}
```

**Output:**

```html
<p>Cornelius Potionmaker<br>12 Phoenix Feather Alley<br>1<br>Calgary AB T1X 0L4<br>Canada</p>
```

---

## localization — translate (t)

> Fonte: <https://shopify.dev/docs/api/liquid/filters/translate>

```liquid
string | t
```

**Returns:** [string](https://shopify.dev/docs/api/liquid/basics#string)

Provides translated text for a specified translation key sourced from a [locale file](https://shopify.dev/themes/architecture/locales).

The `translate` filter uses the shorter alias `t`, which is the more widely adopted form.

### Overview

This filter retrieves translated strings using keys defined in locale files. According to the documentation, "The `translate` filter has an alias of `t`, which is more commonly used."

### Section locales vs. theme locales

The `t` filter can reference keys from the [`locales` object](https://shopify.dev/themes/architecture/sections/section-schema#locales) in a section file's `schema` tag. Content placed in section schema `locales` is accessible only within that section, making it valuable for creating standalone, shareable sections across themes.

Theme-level translations belong in the theme's `locales` directory for global access across multiple pages and components.

> "Translations in the section's `schema` tag that aren't part of the `locales` object are used for merchant-facing text shown in the theme editor. These translations don't use the `t` filter."

### Learn more

Refer to [storefront locale file usage](https://shopify.dev/themes/architecture/locales/storefront-locale-files#usage) or [schema locale file usage](https://shopify.dev/themes/architecture/locales/schema-locale-files#usage) documentation for detailed implementation guidance.

---

## math — abs

> Fonte: <https://shopify.dev/docs/api/liquid/filters/abs>

### Syntax

```liquid
number | abs
```

### Returns

[number](https://shopify.dev/docs/api/liquid/basics#number)

### Description

"Returns the absolute value of a number."

### Example

**Input:**

```liquid
{{ -3 | abs }}
```

**Output:**

```html
3
```

---

## math — at_least

> Fonte: <https://shopify.dev/docs/api/liquid/filters/at_least>

### Description

"Limits a number to a minimum value."

### Syntax

```liquid
number | at_least: minimum_value
```

### Returns

[number](https://shopify.dev/docs/api/liquid/basics#number)

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `minimum_value` | number | The minimum value to limit the input number to |

### Examples

#### Input

```liquid
{{ 4 | at_least: 5 }}
{{ 4 | at_least: 3 }}
```

#### Output

```html
5
4
```

---

## math — at_most

> Fonte: <https://shopify.dev/docs/api/liquid/filters/at_most>

### Description

"Limits a number to a maximum value."

### Syntax

```liquid
number | at_most: value
```

### Returns

[number](https://shopify.dev/docs/api/liquid/basics#number)

### Parameters

- `value` (number) - The maximum value to limit the number to

### Examples

#### Input

```liquid
{{ 6 | at_most: 5 }}
{{ 4 | at_most: 5 }}
```

#### Output

```html
5
4
```

---

## math — ceil

> Fonte: <https://shopify.dev/docs/api/liquid/filters/ceil>

**Description:** "Rounds a number up to the nearest integer."

### Syntax

```liquid
number | ceil
```

### Returns

[number](https://shopify.dev/docs/api/liquid/basics#number)

### Example

**Input:**

```liquid
{{ 1.2 | ceil }}
```

**Output:**

```html
2
```

---

## math — divided_by

> Fonte: <https://shopify.dev/docs/api/liquid/filters/divided_by>

### Syntax

```liquid
number | divided_by: number
```

### Returns

[number](https://shopify.dev/docs/api/liquid/basics#number)

### Description

"Divides a number by a given number. The `divided_by` filter produces a result of the same type as the divisor." This means dividing by an integer yields an integer result, while dividing by a float produces a float result.

### Examples

#### Input

```liquid
{{ 4 | divided_by: 2 }}

# divisor is an integer
{{ 20 | divided_by: 7 }}

# divisor is a float 
{{ 20 | divided_by: 7.0 }}
```

#### Output

```html
2

# divisor is an integer
2

# divisor is a float 
2.857142857142857
```

---

## math — floor

> Fonte: <https://shopify.dev/docs/api/liquid/filters/floor>

### Syntax

```liquid
number | floor
```

### Returns

[number](https://shopify.dev/docs/api/liquid/basics#number)

### Description

"Rounds a number down to the nearest integer."

### Example

**Input:**

```liquid
{{ 1.2 | floor }}
```

**Output:**

```html
1
```

---

## math — minus

> Fonte: <https://shopify.dev/docs/api/liquid/filters/minus>

### Syntax

```liquid
number | minus: number
```

### Returns

[number](https://shopify.dev/docs/api/liquid/basics#number)

### Description

"Subtracts a given number from another number."

### Example

**Input:**

```liquid
{{ 4 | minus: 2 }}
```

**Output:**

```html
2
```

---

## math — modulo

> Fonte: <https://shopify.dev/docs/api/liquid/filters/modulo>

### Description

"Returns the remainder of dividing a number by a given number."

### Syntax

```liquid
number | modulo: number
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| divisor | number | The number to divide by |

### Returns

[number](https://shopify.dev/docs/api/liquid/basics#number)

### Examples

#### Example 1

**Input:**

```liquid
{{ 12 | modulo: 5 }}
```

**Output:**

```html
2
```

---

## math — plus

> Fonte: <https://shopify.dev/docs/api/liquid/filters/plus>

### Syntax

```liquid
number | plus: number
```

### Returns

[number](https://shopify.dev/docs/api/liquid/basics#number)

### Description

"Adds two numbers."

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `number` | number | The value to add to the input number |

### Example

**Liquid input:**

```liquid
{{ 2 | plus: 2 }}
```

**Output:**

```html
4
```

---

## math — round

> Fonte: <https://shopify.dev/docs/api/liquid/filters/round>

### Description

"Rounds a number to the nearest integer."

### Syntax

```liquid
number | round
```

### Returns

[number](https://shopify.dev/docs/api/liquid/basics#number)

### Examples

#### Basic rounding

**Input:**

```liquid
{{ 2.7 | round }}
{{ 1.3 | round }}
```

**Output:**

```html
3
1
```

#### Round to a specific number of decimal places

Specify a number of decimal places to round to. Without a parameter, the filter rounds to the nearest whole number.

**Input:**

```liquid
{{ 3.14159 | round: 2 }}
```

**Output:**

```html
3.14
```

---

## math — times

> Fonte: <https://shopify.dev/docs/api/liquid/filters/times>

### Syntax

```liquid
number | times: number
```

### Returns

[number](https://shopify.dev/docs/api/liquid/basics#number)

### Description

"Multiplies a number by a given number."

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| number | number | The multiplier |

### Examples

#### Input

```liquid
{{ 2 | times: 2 }}
```

#### Output

```html
4
```

---

## Pagine non catturate

Nessun filtro delle categorie A–L è stato saltato o perso. Tutti i filtri assegnati sono stati catturati con sintassi, parametri ed esempi.

Note tecniche (non sono filtri mancanti):

- **`class_list` (categoria html)** — La pagina diretta `https://shopify.dev/docs/api/liquid/filters/class_list` ha restituito HTTP 404 al renderer del tool di fetch. Il contenuto è stato comunque recuperato in modo fedele (descrizione, sintassi, esempio e output) dalla documentazione ufficiale Shopify tramite ricerca su `shopify.dev` ed è incluso integralmente sopra.
- **`default_errors` (categoria default)** — La pagina ufficiale contiene descrizione, sintassi e tipo restituito ma **non** include esempi di codice/output renderizzato; la sezione riflette quindi esattamente il contenuto disponibile sulla pagina sorgente.
- **URL inesistente `…/filters/javascript`** — Non esiste una pagina filtro `javascript`. Il filtro corretto della categoria `hosted_file` per generare il tag `<script>` è **`script_tag`** (incluso sopra). Nessun filtro perso.
- **URL inesistenti `…/filters/html_escape` e `…/filters/html_safe`** — Non esistono pagine reference autonome con questi slug su shopify.dev. Nella categoria `html` la funzione di escaping dei caratteri HTML è coperta dal filtro **`escape`** (incluso sopra).
