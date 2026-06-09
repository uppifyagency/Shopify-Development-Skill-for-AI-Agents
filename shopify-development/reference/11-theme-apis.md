# 11. Theme APIs (Ajax + Section Rendering)

This chapter captures the two client-side JavaScript APIs available to Shopify themes: the **Ajax API** (a suite of lightweight REST endpoints for reading cart/product data and updating the cart) and the **Section Rendering API** (for requesting the rendered HTML markup of theme sections via Ajax). Both APIs can only be used by themes hosted by Shopify and are designed to update page content without a full page reload.

All content below is reproduced faithfully from the official Shopify dev documentation. Every endpoint is captured with its HTTP method and URL, request parameters, response fields, status/error codes, and code examples.

---

## Ajax API

The Ajax API provides a suite of lightweight REST API endpoints for development of Shopify themes. It accepts `GET` requests to read cart and some product data, and `POST` requests to update the cart for the current session. This is an unauthenticated API that returns JSON-formatted data.

### Table of contents

1. [About the Shopify Ajax API (overview)](#about-the-shopify-ajax-api-overview) — `https://shopify.dev/docs/api/ajax`
2. [Ajax API Reference (index)](#ajax-api-reference-index) — `https://shopify.dev/docs/api/ajax/reference`
3. [Cart API reference](#cart-api-reference) — `https://shopify.dev/docs/api/ajax/reference/cart`
4. [Product API reference](#product-api-reference) — `https://shopify.dev/docs/api/ajax/reference/product`
5. [Product Recommendations API reference](#product-recommendations-api-reference) — `https://shopify.dev/docs/api/ajax/reference/product-recommendations`
6. [Predictive Search API reference](#predictive-search-api-reference) — `https://shopify.dev/docs/api/ajax/reference/predictive-search`

---

### About the Shopify Ajax API (overview)

> Fonte: https://shopify.dev/docs/api/ajax

The Ajax API provides a suite of lightweight REST API endpoints for development of [Shopify themes](https://shopify.dev/docs/storefronts/themes). The Ajax API can only be used by themes that are hosted by Shopify. You can't use the Ajax API on a Shopify custom storefront.

**Tip:**

To request the HTML markup for theme sections using an AJAX request, use the [Section Rendering API](https://shopify.dev/docs/api/ajax/section-rendering).

#### Use cases

Possible uses of the Ajax API include:

* Add products to the cart and update the cart item counter.
* Display related product recommendations.
* Suggest products and collections to visitors as they type in a search field.

Refer to the [Ajax API reference](https://shopify.dev/docs/api/ajax/reference/) for a full list of available API endpoints.

#### Making requests to the API

The Ajax API accepts two types of HTTP requests:

* `GET` requests to read cart and some product data
* `POST` requests to update the cart for the current session

For instance, to fetch the current contents of the cart, send a client-side request to the store's `/cart.js` endpoint.

```javascript
var cartContents = fetch(window.Shopify.routes.root + 'cart.js')
.then(response => response.json())
.then(data => { return data });
```

#### Locale-aware URLs

Stores can have [dynamic URLs](https://shopify.dev/docs/storefronts/themes/markets/multiple-currencies-languages#locale-aware-urls) generated for them when they sell internationally or in multiple languages. When using the Ajax API, it's important to use dynamic, locale-aware URLs so that you can give visitors a consistent experience for the language and country that they've chosen.

The global value `window.Shopify.routes.root` is available to use as a base when building locale-aware URLs in JavaScript. The global value will always end in a `/` character, so you can safely use simple string concatenation to build the full URLs.

#### Requirements and limitations

* This is an unauthenticated API. It doesn't require access tokens or a client ID to access.
* There are no hard rate limits on the Ajax API. It's still subject to Shopify's standard API abuse-prevention measures.
* All API responses return JSON-formatted data.
* Product JSON responses are limited to a maximum of 250 variants.
* The Ajax API can't be used to read any customer or order data, or update any store data. If you need more extensive access, check the [GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql).

#### Tutorials

* [Show product recommendations on product pages using the Ajax API](https://shopify.dev/docs/storefronts/themes/product-merchandising/recommendations)

---

### Ajax API Reference (index)

> Fonte: https://shopify.dev/docs/api/ajax/reference

The Ajax API reference index lists the available endpoint categories:

- **[Cart](https://shopify.dev/docs/api/ajax/reference/cart)** — Update cart line items, attributes, and notes.
- **[Product](https://shopify.dev/docs/api/ajax/reference/product)** — Fetch information about any product in the catalog.
- **[Product Recommendations](https://shopify.dev/docs/api/ajax/reference/product-recommendations)** — Display recommended products on product pages.
- **[Predictive Search](https://shopify.dev/docs/api/ajax/reference/predictive-search)** — Suggest products, collections, pages and articles to buyers as they type their search queries.

---

### Cart API reference

> Fonte: https://shopify.dev/docs/api/ajax/reference/cart

The Cart API facilitates interaction with a customer's cart throughout their shopping session. This guide demonstrates how to manage cart line items, set cart attributes and notes, and obtain shipping rate estimates.

All Ajax API requests should employ [locale-aware URLs](https://shopify.dev/docs/api/ajax#locale-aware-urls) for consistent visitor experiences.

**Note:** Code examples in this guide may omit callbacks for brevity.

#### POST /{locale}/cart/add.js

Add one or multiple product variants to the cart.

##### Request Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `items` | Array | Array of variant objects to add |
| `items[].id` | Integer | Variant ID |
| `items[].quantity` | Integer | Quantity to add |
| `items[].properties` | Object | (Optional) Line item key-value properties |
| `items[].selling_plan` | Integer | (Optional) Selling plan ID |

##### Example Request (JSON)

```js
let formData = {
 'items': [{
  'id': 36110175633573,
  'quantity': 2
  }]
};

fetch(window.Shopify.routes.root + 'cart/add.js', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(formData)
})
.then(response => {
  return response.json();
})
.catch((error) => {
  console.error('Error:', error);
});
```

##### Example Request (FormData)

```js
let addToCartForm = document.querySelector('form[action$="/cart/add"]');
let formData = new FormData(addToCartForm);

fetch(window.Shopify.routes.root + 'cart/add.js', {
  method: 'POST',
  body: formData
})
.then(response => {
  return response.json();
})
.catch((error) => {
  console.error('Error:', error);
});
```

##### Response

```json
{
  "items": [
    {
      "id": 36110175633573,
      "title": "Red Rain Coat - Small",
      "key": "794864229:03af7a8cb59a4c3c45595c76fa8cb53c",
      "price": 12900,
      "line_price": 12900,
      "quantity": 2,
      "sku": null,
      "grams": 0,
      "vendor": "Shopify",
      "properties": {},
      "variant_id": 794864229,
      "gift_card": false,
      "url": "/products/red-rain-coat?variant=794864229",
      "featured_image": {
        "url": "http://cdn.shopify.com/s/files/1/0040/7092/products/red-rain-coat.jpeg?v=1402604893",
        "aspect_ratio": 1.0,
        "alt": "Red rain coat with a hood"
      },
      "image": "http://cdn.shopify.com/s/files/1/0040/7092/products/red-rain-coat.jpeg?v=1402604893",
      "handle": "red-rain-coat",
      "requires_shipping": true,
      "product_title": "Red Rain Coat",
      "product_description": "A bright red rain coat for rainy days!",
      "product_type": "Coat",
      "properties": null,
      "variant_title": "Red",
      "variant_options": ["Red"],
      "options_with_values": [
        {
          "name": "Color",
          "value": "Red"
        }
      ]
    }
  ]
}
```

##### Error Responses

**Quantity Exceeds Stock:**

```json
{
  "status": 422,
  "message": "Cart Error",
  "description": "You can't add more #{item.name} to the cart."
}
```

**Product Sold Out:**

```json
{
  "status": 422,
  "message": "Cart Error",
  "description": "The product '#{item.name}' is already sold out."
}
```

**Stock Exhausted:**

```json
{
  "status": 422,
  "message": "Cart Error",
  "description": "You can't add more #{item.name} to the cart."
}
```

##### Add Line Item Properties

Attach custom properties using the `properties` object (key-value pairs):

```js
items: [
  {
    quantity: 1,
    id: 794864229,
    properties: {
      'First name': 'Caroline'
    }
  }
]
```

**Response:**

```json
{
  "items": [
    {
      "id": 794864229,
      "quantity": 1,
      "properties" : {
        "First name": "Caroline"
      }
    }
  ]
}
```

##### Add a Selling Plan

Include a selling plan ID via the `selling_plan` parameter:

```js
items: [
  {
    quantity: 1,
    id: 794864229,
    selling_plan: 183638
  }
]
```

**Response:**

```json
{
  "items": [
    {
      "id": 794864229,
      "selling_plan_allocation": {
        "price": 3120,
        "compare_at_price": 3900,
        "per_delivery_price": 3120,
        "selling_plan": {
          "id": 183638,
          "name": "Pay every month, delivery every month | save 20%",
          "description": "No commitment · Auto-renews · Skip or cancel anytime",
          "options": [{
            "name": "Delivery Frequency",
            "position": 1,
            "value": "Month"
          }, {
            "name": "Billing Frequency",
            "position": 2,
            "value": "Month"
          }],
          "recurring_deliveries": true
        }
      }
    }
  ]
}
```

##### Multiple Items Example

```js
items: [
  {
    id: 36323170943141,
    quantity: 1
  },
  {
    id: 36323170943141,
    selling_plan: 6717605,
    quantity: 1
  },
  {
    id: 36323170943141,
    parent_id: 4534355122,
    quantity: 1
  }
]
```

**Response:**

```json
{
  "items":[
    {
      "id":36323170943141,
      "properties":null,
      "quantity":1,
      "variant_id":36323170943141,
      "key":"36323170943141:b15f59bb6d406f2f45dc383a5493bdb8",
      "title":"Great Granola Bar",
      "price":2000,
      "original_price":2000,
      "discounted_price":2000,
      "line_price":2000,
      "original_line_price":2000,
      "total_discount":0,
      "discounts":[],
      "sku":"",
      "grams":0,
      "vendor":"shopify",
      "taxable":true,
      "product_id":5680114172069,
      "product_has_only_default_variant":true,
      "gift_card":false,
      "final_price":2000,
      "final_line_price":2000,
      "url":"/products/great-granola-bar?variant=36323170943141",
      "featured_image":{
        "aspect_ratio":1.504,
        "alt":"Great Granola Bar",
        "height":1277,
        "url":"https://cdn.shopify.com/s/files/1/0401/3218/2181/products/fallon-michael-h2UH2674Bg4-unsplash.jpg?v=1600796940",
        "width":1920
      },
      "image":"https://cdn.shopify.com/s/files/1/0401/3218/2181/products/fallon-michael-h2UH2674Bg4-unsplash.jpg?v=1600796940",
      "handle":"great-granola-bar",
      "requires_shipping":true
    }
  ]
}
```

#### GET /{locale}/cart.js

Retrieve cart contents as JSON. All monetary values are in the customer's presentment currency.

##### Response: Cart with Items

```json
{
  "token": "Z2NwLXVzLXdlc3QxOjAxSjBQTVk1Sjc5NVFKTjNOVlhLWENXQUI1?key=0d9909213054e22d092152de385763f0",
  "note": "Hello!",
  "attributes": {
    "Gift wrap": "Yes"
  },
  "original_total_price": 3399,
  "total_price": 2925,
  "total_discount": 474,
  "total_weight": 500,
  "item_count": 2,
  "items": [
    {
      "id": 39897499729985,
      "properties": {},
      "quantity": 1,
      "variant_id": 39897499729985,
      "key": "39897499729985:b1fca88d0e8bf5290f306f808785f744",
      "title": "Health potion - S / Low",
      "price": 900,
      "original_price": 900,
      "discounted_price": 900,
      "line_price": 900,
      "original_line_price": 900,
      "total_discount": 0,
      "discounts": [],
      "sku": "",
      "grams": 500,
      "vendor": "Polina's Potent Potions",
      "taxable": true,
      "product_id": 6786188247105,
      "product_has_only_default_variant": false,
      "gift_card": false,
      "final_price": 900,
      "final_line_price": 900,
      "url": "/products/health-potion?selling_plan=610435137&variant=39897499729985"
    }
  ]
}
```

##### Response: Empty Cart

```json
{
  "token": "Z2NwLXVzLXdlc3QxOjAxSjBQTVk1Sjc5NVFKTjNOVlhLWENXQUI1?key=0d9909213054e22d092152de385763f0",
  "note": null,
  "attributes": {},
  "original_total_price": 0,
  "total_price": 0,
  "total_discount": 0,
  "total_weight": 0,
  "item_count": 0,
  "items": [],
  "requires_shipping": false,
  "currency": "CAD",
  "items_subtotal_price": 0,
  "cart_level_discount_applications": []
}
```

##### Response: Cart with Remote Products

```json
{
  "token": "Z2NwLXVzLXdlc3QxOjAxSjBQTVk1Sjc5NVFKTjNOVlhLWENXQUI1?key=0d9909213054e22d092152de385763f0",
  "note": null,
  "attributes": {},
  "original_total_price": 4925,
  "total_price": 4925,
  "total_discount": 0,
  "total_weight": 500,
  "item_count": 3,
  "items": [
    {
      "id": 36323170943141,
      "quantity": 1,
      "title": "Blue Mug - Sold by Sam's Shop",
      "remote": true
    },
    {
      "id": 36323170943142,
      "quantity": 1,
      "title": "Salad bowl - Sold by Home Experts",
      "remote": true
    },
    {
      "id": 36323170943143,
      "quantity": 1,
      "title": "Silverware set"
    }
  ],
  "requires_shipping": false,
  "currency": "CAD",
  "items_subtotal_price": 3149,
  "cart_level_discount_applications": []
}
```

#### POST /{locale}/cart/update.js

Update cart line item quantities, note, and/or attributes. Submit serialized cart forms or separate updates.

##### Update Line Item Quantities

Use an `updates` object with key-value pairs where the value is the desired quantity. The key must be either the variant ID or line item key.

###### Using Variant ID

```js
let updates = {
  794864053: 2,
  794864233: 3
};

fetch(window.Shopify.routes.root + 'cart/update.js', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ updates })
})
.then(response => {
  return response.json();
})
.catch((error) => {
  console.error('Error:', error);
});
```

###### Using FormData

```js
var formData = new FormData();
formData.append("updates[794864053]", 2);
formData.append("updates[794864233]", 3);

fetch(window.Shopify.routes.root + 'cart/update.js', {
  method: 'POST',
  body: formData
})
.then(response => response.json())
.then(data => console.log(data));
```

###### Using Array of Quantities

```js
fetch(window.Shopify.routes.root + 'cart/update.js', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ updates: [3, 2, 1] })
})
.then(response => response.json())
.then(data => console.log(data));
```

###### Remove Items

Set quantity to 0:

```js
let updates = {
  794864053: 0,
  794864233: 0
};

fetch(window.Shopify.routes.root + 'cart/update.js', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ updates })
})
.then(response => {
  return response.json();
})
.catch((error) => {
  console.error('Error:', error);
});
```

##### Update the Cart Note

```js
{
  note: 'This is a note about my order'
}
```

##### Update Cart Attributes

```js
{
  attributes: {
    'Gift wrap': 'Yes'
  }
}
```

###### Using FormData

```js
var formData = new FormData();
formData.append("attributes[Gift wrap]", "Yes");

fetch(window.Shopify.routes.root + 'cart/update.js', {
  method: 'POST',
  body: formData
})
.then(response => response.json())
.then(data => console.log(data));
```

##### Apply Discount Codes

Single discount:

```js
{
  discount: 'discount_code'
}
```

Multiple discounts (comma-separated):

```js
{
  discount: 'discount_code,discount_code2'
}
```

Remove all discounts:

```js
{
  discount: ''
}
```

##### Response

The JSON representation of the updated cart.

##### Error Response

```json
{
  "status": 404,
  "message": "Cart Error",
  "description": "Cannot find variant"
}
```

**Note:** The endpoint does not validate quantities for items already in the cart, potentially allowing inventory overages.

#### POST /{locale}/cart/change.js

Modify `quantity`, `properties`, and `selling_plan` of an existing cart line item. Only one line item can be changed per request.

##### Identify the Line Item

Use either an `id` or `line` property:

###### Using Variant ID

```js
{
  'id': 794864053,
  'quantity': 3
}
```

###### Using Line Item Key

```js
{
  'id': '794864053:83503fd282b94a4737d2c95bd95db0b8',
  'quantity': 3
}
```

###### Using Line Position (1-based index)

```js
{
  'line': 1,
  'quantity': 3
}
```

##### Update Quantity

```js
{
  'line': 2,
  'quantity': 1
}
```

##### Remove a Line Item

```js
{
  'line': 2,
  'quantity': 0
}
```

##### Update Properties

```js
{
  'line': 2,
  'properties': { 'gift_wrap': true }
}
```

**Note:** Specifying `properties` overwrites the entire properties object.

##### Update Selling Plan

Add a selling plan:

```js
{
  'line': 2,
  'quantity': 2,
  'selling_plan': 183638
}
```

Remove a selling plan:

```js
{
  'line': 2,
  'quantity': 2,
  'selling_plan': null
}
```

##### Response

The JSON representation of the updated cart.

##### Error Response

```json
{
  "status": "bad_request",
  "message": "no valid id or line parameter",
  "description": "no valid id or line parameter"
}
```

#### POST /{locale}/cart/clear.js

Set all line item quantities to zero, clearing the cart. Cart attributes and notes are preserved.

##### Response

```json
{
  "token": "Z2NwLXVzLXdlc3QxOjAxSjBQTVk1Sjc5NVFKTjNOVlhLWENXQUI1?key=0d9909213054e22d092152de385763f0",
  "note": null,
  "attributes": {},
  "total_price": 0,
  "total_weight": 0,
  "item_count": 0,
  "items": [],
  "requires_shipping": false
}
```

#### Shipping Rate Endpoints

##### POST /{locale}/cart/prepare_shipping_rates.json

Initiate shipping rate calculations for a cart destination.

###### Example Request

```
/{locale}/cart/prepare_shipping_rates.json?shipping_address%5Bzip%5D=K1N+5T2&shipping_address%5Bcountry%5D=Canada&shipping_address%5Bprovince%5D=Ontario
```

###### Response

```
null
```

##### GET /{locale}/cart/async_shipping_rates.json

Retrieve shipping rates if calculations are complete.

###### Example Request

```
/{locale}/cart/async_shipping_rates.json?shipping_address%5Bzip%5D=K1N+5T2&shipping_address%5Bcountry%5D=Canada&shipping_address%5Bprovince%5D=Ontario
```

###### Response (Rates Ready)

```json
{
  "shipping_rates": [
    {
      "name": "Generic Rate",
      "presentment_name": "Generic Rate",
      "code": "Generic Rate",
      "price": "6.00",
      "markup": null,
      "source": "shopify",
      "delivery_date": null,
      "delivery_range": null,
      "delivery_days": [],
      "compare_price": null,
      "phone_required": false,
      "currency": null,
      "carrier_identifier": null,
      "delivery_category": null,
      "using_merchant_account": null,
      "carrier_service_id": null,
      "description": null,
      "api_client_id": null,
      "requested_fulfillment_service_id": null,
      "shipment_options": null,
      "charge_items": null,
      "has_restrictions": null,
      "rating_classification": null,
      "accepts_instructions": false
    },
    {
      "name": "Carrier Service Mail",
      "presentment_name": "Carrier Service Mail",
      "code": "CarrierServiceMail",
      "price": "12.46",
      "markup": "0.00",
      "source": "usps",
      "delivery_date": "2020-10-09",
      "delivery_range": [
          "2020-10-06",
          "2020-10-09"
      ],
      "delivery_days": [
          0,
          3
      ],
      "compare_price": null,
      "phone_required": true,
      "currency": null,
      "carrier_identifier": null,
      "delivery_category": null,
      "using_merchant_account": null,
      "carrier_service_id": 2,
      "description": null,
      "api_client_id": null,
      "requested_fulfillment_service_id": null,
      "shipment_options": null,
      "charge_items": null,
      "has_restrictions": null,
      "rating_classification": null,
      "accepts_instructions": false
    }
  ]
}
```

###### Response (Rates Not Ready)

```
null
```

##### GET /{locale}/cart/shipping_rates.json

Retrieve estimated shipping rates directly. The recommended approach uses `prepare_shipping_rates.json` and `async_shipping_rates.json` endpoints for better performance.

###### Example Request

```
/{locale}/cart/shipping_rates.json?shipping_address%5Bzip%5D=K1N+5T2&shipping_address%5Bcountry%5D=Canada&shipping_address%5Bprovince%5D=Ontario
```

###### Response

```json
{
  "shipping_rates": [
    {
      "name": "Ground Shipping",
      "price": "8.00",
      "delivery_date": null,
      "source": "shopify"
    },
    {
      "name": "Expedited Shipping",
      "price": "15.00",
      "delivery_date": null,
      "source": "shopify"
    },
    {
      "name": "Express Shipping",
      "price": "30.00",
      "delivery_date": null,
      "source": "shopify"
    }
  ]
}
```

#### Private Properties and Attributes

##### Private Line Item Properties

Prepend an underscore (`_`) to the property key:

```js
items: [
  {
    'quantity': 2,
    'id': 794864229,
    'properties': {
      '_foo': 'bar'
    }
  }
]
```

Mix public and private properties:

```js
items: [
  {
    quantity: 2,
    id: 794864229,
    properties: {
      '_foo': 'bar',
      'gift_wrap': true
    }
  }
]
```

###### Hide Properties in Theme (Liquid)

```liquid
{% for property in line_item.properties %}
  {% assign first_character_in_key = property.first | slice: 0 %}
  {% unless first_character_in_key == '_' %}
    {{ property.first }}: {{ property.last }}
  {% endunless %}
{% endfor %}
```

##### Private Cart Attributes

Prepend a double underscore (`__`) to the attribute name. Private cart attributes are not exposed in Liquid or the Ajax API and require no theme modifications to hide.

#### Bundled Section Rendering

Request HTML markup for up to five sections alongside Cart API calls. Available for:

- `/{locale}/cart/add`
- `/{locale}/cart/change`
- `/{locale}/cart/clear`
- `/{locale}/cart/update`

##### Request Sections

Include a `sections` parameter (comma-separated list or array):

```json
items: [
  {
   id: 36110175633573,
   quantity: 2
  }
],
sections: "cart-items,cart-icon-bubble,cart-live-region-text,cart-footer"
```

##### Specify Page Context

Use `sections_url` parameter (must begin with `/`):

```json
sections: "cart-items,cart-icon-bubble,cart-live-region-text,cart-footer",
sections_url: "/cart?some_param=foo"
```

##### Response with Sections

```json
{
  "attributes": {},
  "cart_level_discount_applications": [],
  "currency": "CAD",
  "item_count": 1,
  "items": [{…}],
  "items_subtotal_price": 100100,
  "note": null,
  "original_total_price": 100100,
  "requires_shipping": true,
  "sections": {
    "cart-items": "<div id=\"shopify-section-template--14199693705272_…9930913703934\" defer=\"defer\"></script>\n\n\n\n\n</div>",
    "cart-icon-bubble": "<div id=\"shopify-section-cart-icon-bubble\" className=\"…ss=\"visually-hidden\">1 item</span>\n  </div></div>",
    "cart-live-region-text": "<div id=\"shopify-section-cart-live-region-text\" cl…opify-section\">New subtotal: $1,001.00 CAD\n</div>",
    "cart-footer": "<div id=\"shopify-section-template--14199693705272_…   </div>\n    </div>\n  </div>\n</div>\n\n\n\n\n\n\n</div>"
  },
  "token": "Z2NwLXVzLXdlc3QxOjAxSjBQTVk1Sjc5NVFKTjNOVlhLWENXQUI1?key=0d9909213054e22d092152de385763f0",
  "total_discount": 0,
  "total_price": 100100,
  "total_weight": 1000
}
```

##### Error Response

Sections that fail to render return `null`. Invalid `sections` or `sections_url` values (e.g., `sections_url` not beginning with `/`) cause an **HTTP 400 Bad Request** status, though data modifications may still succeed.

---

### Product API reference

> Fonte: https://shopify.dev/docs/api/ajax/reference/product

You can make a `GET` request for product information using the Ajax Product API.

All Ajax API requests should use locale-aware URLs to provide visitors with a consistent experience.

#### GET /{locale}/products/{product-handle}.js

Retrieves the JSON representation of a product using the product handle.

All monetary properties are returned in the customer's presentment currency. To check the customer's presentment currency, use the `currency` field of the `/{locale}/cart.js` endpoint. For more information about selling in multiple currencies, see Support multiple currencies and languages.

##### Example

```js
fetch(window.Shopify.routes.root + 'products/red-rain-coat.js')
.then(response => response.json())
.then(product => alert('The title of this product is ' + product.title));
```

#### Response

The API returns the product as a JSON object.

##### Example Response

```json
{
  "id": 329678821,
  "title": "Red Rain Coat",
  "handle": "red-rain-coat",
  "description": "<p>Lorem Ipsum.</p>",
  "published_at": "2014-06-12T16:28:11-04:00",
  "created_at": "2014-06-12T16:28:13-04:00",
  "vendor": "Shopify",
  "type": "Coat",
  "tags": ["Spring"],
  "price": 12900,
  "price_min": 12900,
  "price_max": 12900,
  "available": true,
  "price_varies": false,
  "compare_at_price": null,
  "compare_at_price_min": 0,
  "compare_at_price_max": 0,
  "compare_at_price_varies": false,
  "variants": [
    {
      "id": 794864229,
      "title": "Small",
      "options": ["Small"],
      "option1": "Small",
      "option2": null,
      "option3": null,
      "price": 12900,
      "weight": 0,
      "compare_at_price": null,
      "inventory_management": "shopify",
      "available": true,
      "sku": null,
      "requires_shipping": true,
      "taxable": true,
      "barcode": "49738645"
    },
    {
      "id": 794864233,
      "title": "Medium",
      "options": ["Medium"],
      "option1": "Medium",
      "option2": null,
      "option3": null,
      "price": 12900,
      "weight": 0,
      "compare_at_price": null,
      "inventory_management": "shopify",
      "available": true,
      "sku": null,
      "requires_shipping": true,
      "taxable": true,
      "barcode": "49738657"
    },
    {
      "id": 794864237,
      "title": "Large",
      "options": ["Large"],
      "option1": "Large",
      "option2": null,
      "option3": null,
      "price": 12900,
      "weight": 0,
      "compare_at_price": null,
      "inventory_management": "shopify",
      "available": true,
      "sku": null,
      "requires_shipping": true,
      "taxable": true,
      "barcode": "49738673"
    }
  ],
  "images": ["//cdn.shopify.com/s/files/1/0040/7092/products/red-rain-coat.jpeg?v=1402604893"],
  "featured_image": "//cdn.shopify.com/s/files/1/0040/7092/products/red-rain-coat.jpeg?v=1402604893",
  "options": [
    {
      "name": "Size",
      "position": 1
    }
  ],
  "url": "/products/red-rain-coat"
}
```

**Note:** "The JSON of the product can contain a maximum of 250 variants in the variants array."

##### Selling Plan Example

Products with selling plans contain additional properties:

```json
{
  "id": 5290511958181,
  "variants": [
    {
      "id": 34620489400485,
      "requires_selling_plan": false,
      "selling_plan_allocations": [
        {
          "price": 3120,
          "compare_at_price": 3900,
          "per_delivery_price": 3120,
          "selling_plan_id": 360613,
          "selling_plan_group_id": 14699254537353206000
        },
        {
          "price": 3510,
          "compare_at_price": 3900,
          "per_delivery_price": 3510,
          "selling_plan_id": 393381,
          "selling_plan_group_id": 14699254537353206000
        }
      ]
    }
  ],
  "requires_selling_plan": false,
  "selling_plan_groups": [
    {
      "id": 14699254537353206000,
      "name": "Subscribe and Save",
      "options": [
        {
          "name": "Delivery Frequency",
          "position": 1,
          "values": ["Month", "Week"]
        },
        {
          "name": "Billing Frequency",
          "position": 2,
          "values": ["Month", "Week"]
        }
      ],
      "selling_plans": [
        {
          "id": 360613,
          "name": "Pay every month, delivery every month | save 20%",
          "description": "No commitment · Auto-renews · Skip or cancel anytime",
          "options": [
            {
              "name": "Delivery Frequency",
              "position": 1,
              "value": "Month"
            },
            {
              "name": "Billing Frequency",
              "position": 2,
              "value": "Month"
            }
          ],
          "recurring_deliveries": true
        }
      ]
    }
  ]
}
```

---

### Product Recommendations API reference

> Fonte: https://shopify.dev/docs/api/ajax/reference/product-recommendations

The Product Recommendations API enables merchants to recommend related products for a given product. For comprehensive information about how recommendations work and their limitations, see the [Product recommendations](https://shopify.dev/docs/storefronts/themes/product-merchandising/recommendations) documentation.

All Ajax API requests should use [locale-aware URLs](https://shopify.dev/docs/api/ajax#locale-aware-urls) to provide visitors with a consistent experience.

**Note:** The [Shopify Search & Discovery app](https://apps.shopify.com/search-and-discovery) enables customization of product recommendation and search results, which may impact results from [storefront search](https://shopify.dev/docs/storefronts/themes/navigation-search/search) and the Ajax Product Recommendations API. Visit the [Shopify Help Center](https://help.shopify.com/manual/online-store/search-and-discovery/product-recommendations) to learn more.

#### GET /{locale}/recommendations/products.json

Retrieves recommended products for a specific product in JSON format.

```
GET /{locale}/recommendations/products.json?product_id={product-id}&intent={intent}
```

##### Query parameters

| Query parameter | Required | Description |
| - | - | - |
| `product_id` | Yes | The unique [product ID](https://shopify.dev/docs/api/liquid/objects/product#product-id) of the product for which to retrieve recommendations. |
| `limit` | No | Limits the number of results. Valid range: `1` to `10`. Default: `10`. |
| `intent` | No | The recommendation strategy. Accepted values: `related`, `complementary`. Default: `related`. [Learn more about recommendation intents](https://shopify.dev/docs/storefronts/themes/product-merchandising/recommendations). |

##### Example request object

```json
{
  "product_id": "1234567890123",
  "limit": 4,
  "intent": "related"
}
```

##### Example request using Fetch

```js
fetch(window.Shopify.routes.root + "recommendations/products.json?product_id=1234567890123&limit=4&intent=related")
  .then(response => response.json())
  .then(({ products }) => {
    if (products.length > 0) {
      const firstRecommendedProduct = products[0];

      alert(
        `The title of the first recommended product is: ${firstRecommendedProduct.title}`
      );
    }
  }
);
```

##### Example product response

```json
{
 "intent": "related",
 "products": [
   {
     "id": 35,
     "title": "Gorgeous Silk Coat",
     "handle": "gorgeous-silk-coat",
     "description": null,
     "published_at": "2019-02-26T11:34:58-05:00",
     "created_at": "2019-02-26T11:34:58-05:00",
     "vendor": "Marge Group",
     "type": "Outdoors",
     "tags": [],
     "price": 380000,
     "price_min": 380000,
     "price_max": 790000,
     "available": true,
     "price_varies": true,
     "compare_at_price": null,
     "compare_at_price_min": 0,
     "compare_at_price_max": 0,
     "compare_at_price_varies": false,
     "variants": [
       {
         "id": 69,
         "title": "Small Aluminum Knife",
         "option1": "Small Aluminum Knife",
         "option2": null,
         "option3": null,
         "sku": "",
         "requires_shipping": true,
         "taxable": true,
         "featured_image": null,
         "available": true,
         "name": "Gorgeous Silk Coat - Small Aluminum Knife",
         "public_title": "Small Aluminum Knife",
       }
     ]
   }
 ]
}
```

##### Error responses

###### Invalid parameter

Missing `product_id` parameter:

```json
{
  "status": 422,
  "message": "Invalid parameter error",
  "description": "A product_id value is missing"
}
```

Invalid `intent` parameter:

```json
{
  "status": 422,
  "message": "Invalid parameter error",
  "description": "The intent parameter must be one of related, complementary"
}
```

###### Product not found

```json
{
  "status": 404,
  "message": "Product not found",
  "description": "No product with id <product_id> is published in the online store"
}
```

#### GET /{locale}/recommendations/products

Retrieves HTML from a section rendered with product recommendations.

```
GET /{locale}/recommendations/products?product_id={product-id}&section_id=product-recommendations
```

##### Query parameters

| Query parameter | Required | Description |
| - | - | - |
| `product_id` | Yes | The unique [product ID](https://shopify.dev/docs/api/liquid/objects/product#product-id) of the product for which to retrieve recommendations. |
| `limit` | No | Limits the number of results. Valid range: `1` to `10`. Default: `10`. |
| `section_id` | Yes | The unique [section ID](https://shopify.dev/docs/api/ajax/section-rendering#find-section-ids) of the section file to render with recommendations. |
| `intent` | No | The recommendation strategy. Accepted values: `related`, `complementary`. Default: `related`. [Learn more about recommendation intents](https://shopify.dev/docs/storefronts/themes/product-merchandising/recommendations#recommendation-intents). |

##### Example request object

```json
{
  "product_id": "1234567890123",
  "limit": 4,
  "section_id": "product-recommendations",
  "intent": "related"
}
```

##### Example request using Fetch

```js
const productRecommendationsSection = document.querySelector('.product-recommendations');

fetch(window.Shopify.routes.root + "recommendations/products?product_id=12345690123&limit=4&section_id=product-recommendations&intent=related")
 .then(response => response.text())
 .then((text) => {
    const html = document.createElement('div');
    html.innerHTML = text;
    const recommendations = html.querySelector('.product-recommendations');

    if (recommendations && recommendations.innerHTML.trim().length) {
      productRecommendationsSection.innerHTML = recommendations.innerHTML;
    }
 });
```

##### Example section

```liquid
{%- if recommendations.performed? -%}
  <div id="product-recommendations">
    {%- if recommendations.products_count > 0 -%}
      {% if recommendations.intent == 'related' %}
        <h2>You may also like</h2>
      {% elsif recommendations.intent == 'complementary' %}
        <h2>Pair it with</h2>
      {% endif %}

      <ul>
        {%- for product in recommendations.products -%}
          <li className="grid__item small--one-half medium-up--one-quarter">
            <a href="{{ product.url }}">
              <span>{{ product.title }}</span>
              <span>{{ product.price | money }}</span>
            </a>
          </li>
        {%- endfor -%}
      </ul>
    {%- endif -%}
  </div>
{%- endif -%}
```

##### Example section response

```html
<div id="product-recommendations">
  <h2>You may also like</h2>

  <ul>
    <li className="grid__item small--one-half medium-up--one-quarter">
      <a href="/products/gorgeous-silk-coat?pr_choice=default&pr_prod_strat=copurchase&pr_rec_pid=35&pr_ref_pid=17&pr_seq=alternating">
        <span>Gorgeous Silk Coat</span>
        <span>$380.00</span>
      </a>
    </li>
    ...
  </ul>
</div>
```

##### Error responses

| Status code | Description |
| - | - |
| `404` | * **Product not found** - The provided product ID doesn't exist or isn't published on the **Online store** channel. * **Section not found** - The provided section ID wasn't found in the theme. |
| `422` | * **Invalid parameter error** - The `product_id` query parameter was missing. * **Invalid parameter error** - The `intent` parameter must be one of `related`, `complementary`. |

#### Tracking conversions for product recommendations

The `url` property for each product in the products response contains URL parameters enabling conversion funnel tracking through Shopify reports. Similarly, the Liquid `url` property returned for [`recommendations.products`](https://shopify.dev/docs/api/liquid/objects/recommendations#recommendations-products) includes this tracking information. The URL format:

```
/products/gorgeous-wooden-computer?pr_choice=default&pr_prod_strat=description&pr_rec_pid=13&pr_ref_pid=17&pr_seq=alternating
```

For more information about product recommendation reports, see [Product recommendation conversion over time](https://help.shopify.com/manual/reports-and-analytics/shopify-reports/report-types/behaviour-reports#product-recommendation-conversions-over-time).

---

### Predictive Search API reference

> Fonte: https://shopify.dev/docs/api/ajax/reference/predictive-search

The Predictive Search API can be used to display predictive search results for queries, products, collections, pages, and articles.

To learn how to use predictive search in a theme, refer to [Add predictive search to your theme](https://shopify.dev/docs/storefronts/themes/navigation-search/search/predictive-search).

All Ajax API requests should use [locale-aware URLs](https://shopify.dev/docs/api/ajax#locale-aware-urls) to give visitors a consistent experience.

#### GET /{locale}/search/suggest.json

The following example request retrieves predictive results for a specified search query:

```js
GET /{locale}/search/suggest.json?q={query}
```

##### Query parameters

| Query parameter | Required | Description |
| - | - | - |
| `q` | Yes | The search query. |
| `resources[type]` | No | Specifies the type of results requested. The following are the accepted values, which can be combined in a comma-separated list: `product`, `page`, `article`, `collection`, `query`. The default value is `query,product,collection,page`. To change the default value, you can use [Search Settings](https://help.shopify.com/manual/online-store/search-and-discovery/settings) in the Search & Discovery app. |
| `resources[limit]` | No | Limits the number of results based on `limit_scope`. The value can range from `1` to `10`, and the default is `10`. |
| `resources[limit_scope]` | No | Decides the distribution of results. The following are the accepted values: `all` (Return results up to `limit` across all types), `each` (Return results up to `limit` per type). The default value is `all`. |
| `resources[options][unavailable_products]` | No | Specifies whether to display results for unavailable products. The following are the accepted values: `show` (Show unavailable products), `hide` (Hide unavailable products), `last` (Show unavailable products below other matching results). The default value is `last`. To change the default value, you can use [Search Settings](https://help.shopify.com/manual/online-store/search-and-discovery/settings) in the Search & Discovery app. This parameter is only applicable to type `product`. |
| `resources[options][fields]` | No | Specifies the list of resource fields to search. The following are the accepted values: `author`, `body`, `product_type`, `tag`, `title`, `variants.barcode`, `variants.sku`, `variants.title`, `vendor`. The default fields searched on are `title`, `product_type`, `variants.title`, and `vendor`. For the best search experience, you should search on the default field set. |

##### Example request object

```json
{
  "q": "bag",
  "resources": {
    "type": "product",
    "options": {
      "unavailable_products": "hide",
      "fields": "title,product_type,variants.title"
    }
  }
}
```

##### Example request using Fetch

```javascript
fetch(window.Shopify.routes.root + "search/suggest.json?q=bag&resources[type]=product&resources[options][unavailable_products]=hide&resources[options][fields]=title,product_type,variants.title")
  .then((response) => response.json())
  .then((suggestions) => {
    const productSuggestions = suggestions.resources.results.products;

    if (productSuggestions.length > 0) {
      const firstProductSuggestion = productSuggestions[0];

      alert(`The title of the first product suggestion is: ${
        firstProductSuggestion.title}`
      );
    }
  }
);
```

##### Resources response

The following example is a response to a successful request to the `/{locale}/search/suggest.json` endpoint, which contains resource objects associated with the specified query:

##### Example resources response

```json
{
  "resources": {
    "results": {
      "queries" : "ARRAY OF RELEVANT search queries",
      "products": "ARRAY OF MATCHING product_object",
      "collections": "ARRAY OF MATCHING collection_object",
      "pages": "ARRAY OF MATCHING page_object",
      "articles": "ARRAY OF MATCHING article_object"
    }
  }
}
```

**Caution:** You shouldn't output the `body` content of resource objects for stores that support multiple languages. When a store supports multiple languages, the `body` content contains a combination of the content translated in each language.

##### Example product_object

```json
{
  "available": "BOOLEAN",
  "body": "STRING w/HTML",
  "compare_at_price_max": "DECIMAL (\"0.00\" when the product has no variants with a \"compare_at_price\")",
  "compare_at_price_min": "DECIMAL (\"0.00\" when the product has no variants with a \"compare_at_price\")",
  "handle": "STRING",
  "id": "INTEGER",
  "image": "STRING e.g, \"https://cdn.shopify.com/s/...\"",
  "price": "DECIMAL",
  "price_max": "DECIMAL",
  "price_min": "DECIMAL",
  "tags": "ARRAY OF STRING",
  "title": "STRING",
  "type": "STRING",
  "url": "STRING e.g, \"/products/fast-snowboard?_pos=1&_psq=snowb&_ss=e&_v=1.0\"",
  "variants": [
    {
      "available": "BOOLEAN",
      "compare_at_price": "DECIMAL (nullable)",
      "id": "INTEGER",
      "image": "STRING e.g, \"https://cdn.shopify.com/s/...\"",
      "price": "DECIMAL",
      "title": "STRING",
      "url": "STRING e.g, \"/products/fast-snowboard?_pos=1&_psq=snowb&_ss=e&_v=1.0\"",
      "featured_image": {
        "alt": "STRING",
        "aspect_ratio": "DECIMAL",
        "height": "INTEGER",
        "url": "STRING e.g, \"https://cdn.shopify.com/s/...\"",
        "width": "INTEGER"
      }
    }
  ],
  "vendor": "STRING",
  "featured_image": {
    "alt": "STRING",
    "aspect_ratio": "DECIMAL",
    "height": "INTEGER",
    "url": "STRING e.g, \"https://cdn.shopify.com/s/...\"",
    "width": "INTEGER"
  }
}
```

**Note:** A product variant is returned only when the query matches terms specific to the variant title. Only the variant with the most matching terms is returned. When a variant is returned, the following `product_object` fields will match those of the variant:

* `featured_image`
* `image`
* `url`

For example, a store has a snowboard with a blue variant and a light blue variant. If you search for `snowbo`, then only the snowboard product is returned. However, if you search for `light blue snowbo`, then the snowboard product is returned with the light blue variant.

##### Example collection_object

```json
{
  "body": "STRING w/HTML",
  "handle": "STRING",
  "id": "INTEGER",
  "featured_image": {
    "alt": "STRING",
    "width": "INTEGER",
    "height": "INTEGER",
    "aspect_ratio": "DECIMAL",
    "url": "STRING e.g, \"https://cdn.shopify.com/s/...\""
  },
  "published_at": "STRING DATE",
  "title": "STRING",
  "url": "STRING e.g, \"/collections/snowboards?_pos=1&_psq=sno&_ss=e&_v=1.0\""
}
```

##### Example query_object

```json
{
  "url": "STRING e.g, \"/search?_pos=1&_psq=cos&_ss=e&_v=1.0&q=costume\"",
  "text": "STRING",
  "styled_text": "STRING e.g, \"<mark>cos</mark><span>tume</span>\""
}
```

##### Example page_object

```json
{
  "author": "STRING",
  "body": "STRING w/HTML",
  "handle": "STRING",
  "id": "INTEGER",
  "published_at": "STRING DATE",
  "title": "STRING",
  "url": "STRING e.g, \"/pages/my-page?_pos=1&_psq=my&_ss=e&_v=1.0\""
}
```

##### Example article_object

```json
{
  "author": "STRING",
  "body": "STRING w/HTML",
  "handle": "STRING",
  "id": "INTEGER",
  "image": "STRING e.g, \"https://cdn.shopify.com/s/...\"",
  "published_at": "STRING DATE",
  "summary_html": "STRING w/HTML",
  "tags": "ARRAY OF STRING",
  "title": "STRING",
  "url": "STRING e.g, \"/blogs/news/my-article?_pos=1&_psq=my&_ss=e&_v=1.0\""
}
```

##### Error responses

When a request to the `/{locale}/search/suggest.json` endpoint is unsuccessful, one of the following error responses is returned:

* [Invalid parameter error](#invalid-parameter-error)
* [Expectation failed](#expectation-failed)
* [Too many requests](#too-many-requests)

Any other errors not listed will return a `5xx` status code.

###### Invalid parameter error

All errors related to the request parameters are returned with a 422 status code and a relevant error message. The `description` field describes the request error.

###### Invalid parameter example

```json
{
  "status": "422",
  "message": "Invalid parameter error",
  "description": "Invalid option for `unavailable_products` parameter"
}
```

###### Expectation failed

If your theme isn't using one of the [supported languages](#supported-languages), then the API returns the following error:

###### Expectation failed example

```json
{
  "status": "417",
  "message": "Expectation Failed",
  "description": "Unsupported buyer locale"
}
```

###### Too many requests

Exceeding the request throttle limit will return a 429 status code with a relevant error message.

###### Too many requests example

```json
{
  "status": "429",
  "message": "Too many requests",
  "description": "Throttled"
}
```

In this case, the response will also contain an HTTP header with the Retry-After value in seconds.

###### Retry-After example

```text
Retry-After: 1
```

#### GET /{locale}/search/suggest

The following example request retrieves the HTML from a section rendered with the predictive results for a specified search query.

```js
GET /{locale}/search/suggest?q={query}&resources[type]=product&section_id={section_id}
```

##### Query parameters

The `/search/suggest` endpoint supports the same [query parameters](#query-parameters) as the `/search/suggest.json` endpoint, in addition to the following:

| Query parameter | Required | Description |
| - | - | - |
| `section_id` | Yes | The unique [section ID](https://shopify.dev/docs/api/ajax/section-rendering#find-section-ids) of the section file that you want render with the predictive search query. |

##### Example request object

```json
{
  "q": "bag",
  "resources": {
    "type": "product",
    "options": {
      "unavailable_products": "hide",
      "fields": "title, product_type, variants.title"
    }
  },
  "section_id": "predictive-search"
}
```

##### Example request using Fetch

```javascript
const predictiveSearchSection = document.querySelector('.predictive-search-results');
var requestResponse;

fetch(window.Shopify.routes.root + "search/suggest?q=bag&resources[type]=product&resources[options][unavailable_products]=hide&resources[options][fields]=title,product_type,variants.title&section_id=predictive-search")
  .then((response) => {
    requestResponse = response;
    return response.text();
   })
  .then((text) => {
    if (!requestResponse.ok) {
      throw new Error(`${requestResponse.status}: ${text}`);
    }

    const resultsMarkup = new DOMParser()
      .parseFromString(text, 'text/html')
      .querySelector('#shopify-section-predictive-search').innerHTML;

    predictiveSearchSection.innerHTML = resultsMarkup;
  })
  .catch((error) => {
    console.error(error);
  });
```

##### Section response

The response to a successful request to the `/{locale}/search/suggest` endpoint contains the HTML of the provided section rendered with the [`predictive_search` object](https://shopify.dev/docs/api/liquid/objects/predictive_search) containing the results of the specified query.

##### Example section

```liquid
{%- if predictive_search.performed -%}
  <div id="predictive-search-results">
    {%- if predictive_search.resources.products.size > 0 -%}
      <h3>Products</h3>
      <ul>
        {%- for product in predictive_search.resources.products -%}
          <li><a href="{{ product.url }}">{{ product.title }}</a></li>
        {%- endfor -%}
      </ul>
    {%- endif -%}
  </div>
{%- endif -%}
```

##### Example section response

```html
<div id="shopify-section-predictive-search">
  <div id="predictive-search-results">
    <h3>Products</h3>
    <ul>
      <li><a href="/products/running-shoes">Running Shoes</a></li>
      <li><a href="/products/tennis-shoes">Tennis Shoes</a></li>
    </ul>
  </div>
</div>
```

**Note:** For the `product` resources type, if the query matches terms specific to a variant's title, the following [`product` object](https://shopify.dev/docs/api/liquid/objects/product) fields will match those of the variant:

* `featured_media`
* `url`

For example, a store has a snowboard with a blue variant and a light blue variant. If you search for `snowbo`, then the snowboard product is returned showing the featured media and URL for the snowboard product. However, if you search for `light blue snowbo`, then the snowboard product is returned showing the featured media and URL for the light blue variant.

##### Error responses

When a request to the `/{locale}/search/suggest` endpoint is unsuccessful, one of the following error status codes is returned:

| Status code | Description |
| - | - |
| `404` | **Section not found** - The provided section ID wasn't found in the theme. |
| `417` | **Expectation failed** - The buyer isn't using one of the [supported languages](#supported-languages). |
| `422` | **Invalid parameter error** - The value used for a query parameter was invalid. |
| `429` | **Too many requests** - The request throttle limit has been exceeded. |

You can output the response text to get more details about an error.

**Note:** Any other errors not listed will return a `5xx` status code.

#### Searchable properties

Search results are based on different searchable properties, depending on the resource `type` that you include in your query.

| Resource type | Searchable properties |
| - | - |
| Products | `body`, `product_type`, `tag`, `title`, `variants.barcode`, `variants.sku`, `variants.title`, `vendor` |
| Pages | `author`, `body`, `title` |
| Articles | `author`, `body`, `tag`, `title` |
| Collections | `title` |

##### Searchable translations

When searching a translated storefront, you can search the following properties:

| Resource type | Searchable translations |
| - | - |
| Products | `body`, `title`, `variants.title` |
| Pages | `body`, `title` |
| Articles | `body`, `title` |

#### Typo tolerance

Predictive search includes typo tolerance, which lets search terms containing typos return the correct matching search results.

Typo tolerance is set to `1`, which means that search displays results that differ from the search term by 1 letter, or results that have 2 letters in a different order. The first 4 letters of a search term need to be entered correctly for typo tolerance to take effect.

The following fields support typo tolerance:

| Resource type | Fields supporting typo tolerance |
| - | - |
| Products | `title`, `product_type`, `variants.title`, `vendor` |
| Pages | `author`, `title` |
| Articles | `author`, `title` |
| Collections | `title` |

##### Partial word matches

Predictive search supports partial word matches. This means that it suggests results even if the word you've entered is still incomplete. For example, if you enter `sweate`, then you might see a suggested search result for `sweater`.

Predictive search has the following limitations when it applies partial word matches:

* If a search query has more than one term, then partial word matches are applied only to the last term in the query.
* Partial word matches are applied only to the end of a search term. For example, if you enter `book`, then you won't see a suggested search result for `ebook`.
* Partial word matches are supported only for themes using specific languages. For more details, refer to [Requirements and limitations](#requirements-and-limitations).

Predictive search uses a different search engine than storefront search. Because of this, it doesn't handle partial word matches in the same way. Although predictive search supports partial word matches, storefront search supports them only if the [prefix option parameter](https://shopify.dev/docs/storefronts/themes/navigation-search/search#query-parameters) is set to `last`.

#### Requirements and limitations

This section contains information about how predictive search is supported, and any current limitations.

##### Supported languages

Predictive search is supported when the customer's online store session (`buyer locale`) is in one of the following supported languages:

* Afrikaans
* Albanian
* Armenian
* Bosnian
* Bulgarian
* Catalan
* Croatian
* Czech
* Danish
* Dutch
* English
* Estonian
* Faroese
* Finnish
* French
* Gaelic
* German
* Greek
* Hungarian
* Icelandic
* Indonesian
* Italian
* Latin
* Latvian
* Lithuanian
* Macedonian
* Moldovan
* Norwegian
* Norwegian (Bokmål)
* Norwegian Nynorsk
* Polish
* Portuguese (Brazil)
* Portuguese (Portugal)
* Romanian
* Russian
* Serbian
* Serbo-Croatian
* Slovak
* Slovenian
* Spanish
* Swedish
* Turkish
* Ukrainian
* Vietnamese
* Welsh

A script tag in the `<head>` section indicates whether predictive search is supported for the theme language: `<script id="shopify-features"></script>`. This script tag includes a JSON-encoded `predictiveSearch` key with a boolean value. When it's set to `true`, the theme language is supported, and predictive search is enabled. Otherwise, it's set to `false`.

##### Limitations

* Individual products can't be excluded from predictive search results. If a product is hidden from search engines and sitemaps with the metafield `seo.hidden`, then it won't appear in predictive search results. Learn more about [hiding resources with this metafield](https://shopify.dev/docs/apps/build/marketing-analytics/optimize-storefront-seo#step-2-hide-a-resource-from-search-engines-and-sitemaps).
* The API returns no more than 10 predictive suggestions per request type.
* Collection suggestions are based on the store's primary language. A customer's search won't be compared to a collection's translated content.
* Query suggestions are available in English only, and require the store's primary language (`shop primary locale`) and the customer's online store session (`buyer locale`) to be in English.

---

## Section Rendering API

> Fonte: https://shopify.dev/docs/api/ajax/section-rendering

You can use the Section Rendering API to request the HTML markup for theme sections using an AJAX request. This allows you to update page content without reloading the entire page by fetching and dynamically replacing only certain elements.

For example, you can use the Section Rendering API to paginate search results without performing a full page reload between pages.

> If you want to use the Section Rendering API to update a page based on changes to the cart, then you should consider bundled section rendering.

### Request sections

You can use the `sections` query parameter to render up to five sections, identified by their section IDs. The response is a JSON object that includes pairs for each section ID and its corresponding rendered HTML.

The `sections` parameter can be a comma-separated list of IDs or an array:

```text
?sections=main-password-header,sections--1234__header
?sections[]=main-password-header&sections[]=sections--1234__header
```

Sections can be rendered in the context of any page by appending the `sections` parameter to any page URL. For example, you can request `/?sections=sections--1234__header` for the root page, or `/collections/featured?sections=sections--1234__header` for a featured collection page.

> You can't specify section setting values through the Section Rendering API. If a requested section exists in a template, or is statically rendered, then the existing section settings apply. Otherwise, any default values are used.

#### Example Request

```js
function handleResponse() {
  JSON.parse(this.responseText);
}

const request = new XMLHttpRequest();

request.addEventListener('load', handleResponse);
request.open('GET', '/?sections=main-password-header,sections--1234__header', true);
request.send();
```

#### Example Response

```json
{
  "header":"<div id=\"shopify-section-main-password-header\" className=\"shopify-section\">\n<!-- section content -->\n</div>",
  "footer":"<div id=\"shopify-section-sections--1234__header\" className=\"shopify-section shopify-section-group-header-group\">\n<!-- section content -->\n</div>"
}
```

> Any query parameters that are respected when rendering the full page, such as `q` or `page`, are also respected when sections are rendered.

#### Sections Error Response

Sections that fail to render, including those that fail because they do not exist for the published theme, are returned as `null` in the JSON response. A response might have an HTTP 200 status, but still include one or more sections that failed to render. You should account for the possibility of `null` sections.

### Request a single section

You can use the `section_id` query parameter to request a single section as an alternative approach:

```text
?section_id=main-password-header
```

Sections rendered in response to the `section_id` query parameter are returned directly as HTML and can be used to render a section in the context of any page.

> You can't specify section setting values through the Section Rendering API. If a requested section exists in a template, or is statically rendered, then the existing section settings apply. Otherwise, any default values are used.

#### Single Section Error Response

If the requested section ID doesn't exist on the theme, the server responds with a `404` status.

### Find section IDs

You can access a section ID in two ways:

* Through the Liquid `section` object, using `section.id`
* Extract it from the ID attribute of the section wrapper

> If you want to reference a statically rendered section, then the section ID is the file name. For example, if you had a `social.liquid` section, then the ID would be `social`.

#### Extract a section ID from the wrapper

You can extract a section ID from the ID attribute of the section wrapper. The general format for a section wrapper is:

```html
<div id="shopify-section-[section-id]" className="shopify-section">
  <!-- section content -->
</div>
```

If a section is included in a JSON template or a section group, it's assigned a dynamic section ID. Dynamic section IDs ensure no two sections of the same type have the same ID.

For example, a section inside of a section group might have an ID of `sections--1234__header`, and a section inside of a JSON template might have an ID of `template--5678__image_banner`.

### Locale-aware URLs

When using the Section Rendering API, it's important to use dynamic, locale-aware URLs so that you can give visitors a consistent experience for the language and country that they've chosen.

The global value `window.Shopify.routes.root` is available to use as a base when building locale-aware URLs in JavaScript:

#### Loading a section in the context of the root

```javascript
fetch(window.Shopify.routes.root + "?sections={section-id}")
  .then(res => res.json())
```

Alternatively, a section can be loaded in the context of the current page by using `window.location.pathname` as a base:

#### Loading a section in the context of the current page

```javascript
fetch(window.location.pathname + "?sections={section-id}")
  .then(res => res.json())
```
