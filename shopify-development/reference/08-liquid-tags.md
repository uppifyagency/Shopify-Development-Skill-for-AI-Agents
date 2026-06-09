# 8. Liquid — Tags

Tags create the logic and control flow for templates. They're enclosed in curly brace percentage delimiters `{% %}` and don't output content by themselves: they set variables, render templates, and control whether and how other parts of a template render. This chapter is a faithful 1:1 extraction of every Shopify Liquid tag reference page, organized by the categories used in the official documentation index.

> Fonte (indice): https://shopify.dev/docs/api/liquid/tags

## Indice dei tag

**Conditional tags**
- [if](#if)
- [unless](#unless)
- [case](#case)

**HTML tags**
- [form](#form)

**Iteration tags**
- [for](#for)
- [cycle](#cycle)
- [tablerow](#tablerow)
- [break](#break)
- [continue](#continue)
- [paginate](#paginate)

**Syntax tags**
- [comment](#comment)
- [doc](#doc)
- [echo](#echo)
- [liquid](#liquid)
- [raw](#raw)

**Theme tags**
- [content_for](#content_for)
- [javascript](#javascript)
- [layout](#layout)
- [render](#render)
- [section](#section)
- [sections](#sections)
- [style](#style)
- [stylesheet](#stylesheet)

**Variable tags**
- [assign](#assign)
- [capture](#capture)
- [increment](#increment)
- [decrement](#decrement)

**Deprecated tags**
- [include](#include)

---

# Conditional tags

## if

> Fonte: https://shopify.dev/docs/api/liquid/tags/if

Renders an expression if a specific condition is `true`.

### Syntax

```liquid
{% if condition %}
  expression
{% endif %}
```

#### condition

The condition to evaluate.

#### expression

The expression to render if the condition is met.

### Examples

#### Basic if statement

**Code:**
```liquid
{% if product.compare_at_price > product.price %}
  This product is on sale!
{% endif %}
```

**Data:**
```json
{
  "product": {
    "compare_at_price": "10.00",
    "price": "0.00"
  }
}
```

**Output:**
```html
This product is on sale!
```

#### elsif

Use the `elsif` tag to check for multiple conditions.

**Code:**
```liquid
{% if product.type == 'Love' %}
  This is a love potion!
{% elsif product.type == 'Health' %}
  This is a health potion!
{% endif %}
```

**Data:**
```json
{
  "product": {
    "type": null
  }
}
```

**Output:**
```html
This is a health potion!
```

---

## unless

> Fonte: https://shopify.dev/docs/api/liquid/tags/unless

Renders an expression unless a specific condition is `true`.

> Similar to the `if` tag, you can use `elsif` to add more conditions to an `unless` tag.

### Syntax

```liquid
{% unless condition %}
  expression
{% endunless %}
```

#### Parameters

| Parameter | Description |
|-----------|-------------|
| `condition` | The condition to evaluate. |
| `expression` | The expression to render unless the condition is met. |

### Example

**Input:**

```liquid
{% unless product.has_only_default_variant %}
  // Variant selection functionality
{% endunless %}
```

**Data:**

```json
{
  "product": {
    "has_only_default_variant": false
  }
}
```

**Output:**

```html
// Variant selection functionality
```

---

## case

> Fonte: https://shopify.dev/docs/api/liquid/tags/case

Renders a specific expression depending on the value of a specific variable.

### Syntax

```liquid
{% case variable %}
  {% when first_value %}
    first_expression
  {% when second_value %}
    second_expression
  {% else %}
    third_expression
{% endcase %}
```

#### Parameters

| Parameter | Description |
|-----------|-------------|
| `variable` | The name of the variable you want to base your case statement on. |
| `first_value` | A specific value to check for. |
| `second_value` | A specific value to check for. |
| `first_expression` | An expression to be rendered when the variable's value matches `first_value`. |
| `second_expression` | An expression to be rendered when the variable's value matches `second_value`. |
| `third_expression` | An expression to be rendered when the variable's value has no match. |

### Example

**Input:**
```liquid
{% case product.type %}
  {% when 'Health' %}
    This is a health potion.
  {% when 'Love' %}
    This is a love potion.
  {% else %}
    This is a potion.
{% endcase %}
```

**Data:**
```json
{
  "product": {
    "type": null
  }
}
```

**Output:**
```html
This is a health potion.
```

### Multiple values

A `when` tag can accept multiple values. When multiple values are provided, the expression is returned when the variable matches any of the values inside of the tag. Provide the values as a comma-separated list, or separate them using an `or` operator.

#### Syntax

```liquid
{% case variable %}
  {% when first_value or second_value or third_value %}
    first_expression
  {% when fourth_value, fifth_value, sixth_value %}
    second_expression
  {% else %}
    third_expression
{% endcase %}
```

#### Example

**Input:**
```liquid
{% case product.type %}
  {% when 'Love' or 'Luck' %}
    This is a love or luck potion.
  {% when 'Strength','Health' %}
    This is a strength or health potion.
  {% else %}
    This is a potion.
{% endcase %}
```

**Data:**
```json
{
  "product": {
    "type": null
  }
}
```

**Output:**
```html
This is a strength or health potion.
```

---

# HTML tags

## form

> Fonte: https://shopify.dev/docs/api/liquid/tags/form

Generates an HTML `<form>` tag, including any required `<input>` tags to submit the form to a specific endpoint.

Because there are many different form types available in Shopify themes, the `form` tag requires a type. Depending on the form type, an additional parameter might be required.

### Syntax

```liquid
{% form 'form_type' %}
  content
{% endform %}
```

#### Parameters

| Parameter | Description |
|-----------|-------------|
| `form_type` | The name of the desired form type. |
| `content` | The form contents. |

### Form types

#### activate_customer_password

**Syntax**

```liquid
{% form 'activate_customer_password' %}
  form_content
{% endform %}
```

Generates a form for activating a customer account. To learn more about using this form, and its contents, refer to the `customers/activate_account` template.

**Code**

```liquid
{% form 'activate_customer_password' %}
  <!-- form content -->
{% endform %}
```

**Output**

```html
<form method="post" action="/account/activate" accept-charset="UTF-8"><input type="hidden" name="form_type" value="activate_customer_password" /><input type="hidden" name="utf8" value="✓" />
  <!-- form content -->
</form>
```

#### cart

**Syntax**

```liquid
{% form 'cart', cart %}
  form_content
{% endform %}
```

Generates a form for creating a checkout based on the items currently in the cart. The `cart` form requires a `cart` object as a parameter. To learn more about using the cart form in your theme, refer to the `cart` template.

**Code**

```liquid
{% form 'cart', cart %}
  <!-- form content -->
{% endform %}
```

**Output**

```html
<form method="post" action="/cart" id="cart_form" accept-charset="UTF-8" class="shopify-cart-form" enctype="multipart/form-data"><input type="hidden" name="form_type" value="cart" /><input type="hidden" name="utf8" value="✓" />
  <!-- form content -->
</form>
```

#### contact

**Syntax**

```liquid
{% form 'contact' %}
  form_content
{% endform %}
```

Generates a form for submitting an email to the merchant. To learn more about using this form in your theme, refer to Add a contact form to your theme.

**Code**

```liquid
{% form 'contact' %}
  <!-- form content -->
{% endform %}
```

**Output**

```html
<form method="post" action="/contact#contact_form" id="contact_form" accept-charset="UTF-8" class="contact-form"><input type="hidden" name="form_type" value="contact" /><input type="hidden" name="utf8" value="✓" />
  <!-- form content -->
</form>
```

#### create_customer

**Syntax**

```liquid
{% form 'create_customer' %}
  form_content
{% endform %}
```

Generates a form for creating a new customer account. To learn more about using this form, and its contents, refer to the `customers/register` template.

**Code**

```liquid
{% form 'create_customer' %}
  <!-- form content -->
{% endform %}
```

**Output**

```html
<form method="post" action="/account" id="create_customer" accept-charset="UTF-8" data-login-with-shop-sign-up="true"><input type="hidden" name="form_type" value="create_customer" /><input type="hidden" name="utf8" value="✓" />
  <!-- form content -->
</form>
```

#### currency

**Syntax**

```liquid
{% form 'currency' %}
  form_content
{% endform %}
```

**Deprecated:** The `currency` form is deprecated and has been replaced by the `localization` form.

Generates a form for customers to select their preferred currency.

**Code**

```liquid
{% form 'currency' %}
  {{ form | currency_selector }}
{% endform %}
```

**Output**

```html
<form method="post" action="/cart/update" id="currency_form" accept-charset="UTF-8" class="shopify-currency-form" enctype="multipart/form-data"><input type="hidden" name="form_type" value="currency" /><input type="hidden" name="utf8" value="✓" /><input type="hidden" name="return_to" value="/services/liquid_rendering/resource" />
  <select name="currency"><option value="AED">AED د.إ</option><option value="AFN">AFN ؋</option><option value="AUD">AUD $</option><option value="CAD" selected="selected">CAD $</option><option value="CHF">CHF CHF</option><option value="CZK">CZK Kč</option><option value="DKK">DKK kr.</option><option value="EUR">EUR €</option><option value="GBP">GBP £</option><option value="HKD">HKD $</option><option value="ILS">ILS ₪</option><option value="JPY">JPY ¥</option><option value="KRW">KRW ₩</option><option value="MYR">MYR RM</option><option value="NZD">NZD $</option><option value="PLN">PLN zł</option><option value="SEK">SEK kr</option><option value="SGD">SGD $</option><option value="USD">USD $</option></select>
</form>
```

#### customer

**Syntax**

```liquid
{% form 'customer' %}
  form_content
{% endform %}
```

Generates a form for creating a new customer without registering a new account. This form is useful for collecting customer information when you don't want customers to log in to your store, such as building a list of emails from a newsletter signup.

To learn more about using this form, and its contents, refer to Email consent.

**Code**

```liquid
{% form 'customer' %}
  <!-- form content -->
{% endform %}
```

**Output**

```html
<form method="post" action="/contact#contact_form" id="contact_form" accept-charset="UTF-8" class="contact-form"><input type="hidden" name="form_type" value="customer" /><input type="hidden" name="utf8" value="✓" />
  <!-- form content -->
</form>
```

#### customer_address

**Syntax**

```liquid
{% form 'customer_address', address_type %}
  form_content
{% endform %}
```

Generates a form for creating a new address on a customer account, or editing an existing one. The `customer_address` form requires a specific parameter, depending on whether a new address is being created or an existing one is being edited:

| Parameter value | Use-case |
|-----------------|----------|
| `customer.new_address` | When a new address is being created. |
| `address` | When an existing address is being edited. |

To learn more about using this form, and its contents, refer to the `customers/addresses` template.

**Code**

```liquid
{% form 'customer_address', customer.new_address %}
  <!-- form content -->
{% endform %}
```

**Data**

```json
{
  "customer": {
    "new_address": {}
  }
}
```

**Output**

```html
<form method="post" action="/account/addresses" id="address_form_new" accept-charset="UTF-8"><input type="hidden" name="form_type" value="customer_address" /><input type="hidden" name="utf8" value="✓" />
  <!-- form content -->
</form>
```

#### customer_login

**Syntax**

```liquid
{% form 'customer_login' %}
  form_content
{% endform %}
```

Generates a form for logging into a customer account. To learn more about using this form, and its contents, refer to the `customers/login` template.

**Code**

```liquid
{% form 'customer_login' %}
  <!-- form content -->
{% endform %}
```

**Output**

```html
<form method="post" action="/account/login" id="customer_login" accept-charset="UTF-8" data-login-with-shop-sign-in="true"><input type="hidden" name="form_type" value="customer_login" /><input type="hidden" name="utf8" value="✓" />
  <!-- form content -->
</form>
```

#### guest_login

**Syntax**

```liquid
{% form 'guest_login' %}
  form_content
{% endform %}
```

Generates a form, for use in the `customers/login` template, that directs customers back to their checkout session as a guest instead of logging in to an account. To learn more about using this form, and its contents, refer to Offer guest checkout.

**Code**

```liquid
{% form 'guest_login' %}
  <!-- form content -->
{% endform %}
```

**Output**

```html
<form method="post" action="/account/login" id="customer_login_guest" accept-charset="UTF-8"><input type="hidden" name="form_type" value="guest_login" /><input type="hidden" name="utf8" value="✓" />
  <!-- form content -->
<input type="hidden" name="guest" value="true" /></form>
```

#### localization

**Syntax**

```liquid
{% form 'localization' %}
  form_content
{% endform %}
```

Generates a form for customers to select their preferred country so that they're shown the appropriate language and currency. The `localization` form can contain one of two selectors:

* A country selector
* A language selector

The `localization` form replaces the deprecated `currency` form.

To learn more about using this form, and its contents, refer to Support multiple currencies and languages.

**Code**

```liquid
{% form 'localization' %}
  <!-- form content -->
{% endform %}
```

**Output**

```html
<form method="post" action="/localization" id="localization_form" accept-charset="UTF-8" class="shopify-localization-form" enctype="multipart/form-data"><input type="hidden" name="form_type" value="localization" /><input type="hidden" name="utf8" value="✓" /><input type="hidden" name="_method" value="put" /><input type="hidden" name="return_to" value="/services/liquid_rendering/resource" />
  <!-- form content -->
</form>
```

#### new_comment

**Syntax**

```liquid
{% form 'new_comment', article %}
  form_content
{% endform %}
```

Generates a form for creating a new comment on an article. The `new_comment` form requires an `article` object as a parameter. To learn more about using this form, and its contents, refer to the `article` template.

**Code**

```liquid
{% form 'new_comment', article %}
  <!-- form content -->
{% endform %}
```

**Output**

```html
<form method="post" action="/blogs/potion-notions/how-to-tell-if-you-have-run-out-of-invisibility-potion/comments#comment_form" id="comment_form" accept-charset="UTF-8" class="comment-form"><input type="hidden" name="form_type" value="new_comment" /><input type="hidden" name="utf8" value="✓" />
  <!-- form content -->
</form>
```

#### product

**Syntax**

```liquid
{% form 'product', product %}
  form_content
{% endform %}
```

Generates a form for adding a product variant to the cart. The `product` form requires a `product` object as a parameter. To learn more about using this form, and its contents, refer to the `product` template.

**Code**

```liquid
{% form 'product', product %}
  <!-- form content -->
{% endform %}
```

**Data**

```json
{
  "product": {
    "id": 6786188247105
  }
}
```

**Output**

```html
<form method="post" action="/cart/add" id="product_form_6786188247105" accept-charset="UTF-8" class="shopify-product-form" enctype="multipart/form-data"><input type="hidden" name="form_type" value="product" /><input type="hidden" name="utf8" value="✓" />
  <!-- form content -->
<input type="hidden" name="product-id" value="6786188247105" /></form>
```

#### recover_customer_password

**Syntax**

```liquid
{% form 'recover_customer_password' %}
  form_content
{% endform %}
```

Generates a form, for use in the `customers/login` template, for a customer to recover a lost or forgotten password. To learn more about using this form, and its contents, refer to Provide a "Forgot your password" option.

**Code**

```liquid
{% form 'recover_customer_password' %}
  <!-- form content -->
{% endform %}
```

**Output**

```html
<form method="post" action="/account/recover" accept-charset="UTF-8"><input type="hidden" name="form_type" value="recover_customer_password" /><input type="hidden" name="utf8" value="✓" />
  <!-- form content -->
</form>
```

#### reset_customer_password

**Syntax**

```liquid
{% form 'reset_customer_password' %}
  form_content
{% endform %}
```

Generates a form for a customer to reset their password. To learn more about using this form, and its contents, refer to the `customers/reset_password` template.

**Code**

```liquid
{% form 'reset_customer_password' %}
  <!-- form content -->
{% endform %}
```

**Output**

```html
<form method="post" action="/account/reset" accept-charset="UTF-8"><input type="hidden" name="form_type" value="reset_customer_password" /><input type="hidden" name="utf8" value="✓" />
  <!-- form content -->
</form>
```

#### storefront_password

**Syntax**

```liquid
{% form 'storefront_password' %}
  form_content
{% endform %}
```

Generates a form for entering a password protected storefront. To learn more about using this form, and its contents, refer to the `password` template.

**Code**

```liquid
{% form 'storefront_password' %}
  <!-- form content -->
{% endform %}
```

**Output**

```html
<form method="post" action="/password" id="login_form" accept-charset="UTF-8" class="storefront-password-form"><input type="hidden" name="form_type" value="storefront_password" /><input type="hidden" name="utf8" value="✓" />
  <!-- form content -->
</form>
```

### Form tag parameters

#### return_to

**Syntax**

```liquid
{% form 'form_type', return_to: string %}
  content
{% endform %}
```

By default, each form type redirects customers to a specific page after the form submits. For example, the `product` form redirects to the cart page.

The `return_to` parameter allows you to specify a URL to redirect to. This can be done with the following values:

| Value | Description |
|-------|-------------|
| `back` | Redirect back to the same page that the customer was on before submitting the form. |
| A relative path | A specific URL path. For example `/collections/all`. |
| A `routes` attribute | For example, `routes.root_url` |

**Code**

```liquid
{% form 'customer_login', return_to: routes.root_url %}
  <!-- form content -->
{% endform %}
```

**Data**

```json
{
  "routes": {
    "root_url": "/"
  }
}
```

**Output**

```html
<form method="post" action="/account/login" id="customer_login" accept-charset="UTF-8" data-login-with-shop-sign-in="true"><input type="hidden" name="form_type" value="customer_login" /><input type="hidden" name="utf8" value="✓" /><input type="hidden" name="return_to" value="/" />
  <!-- form content -->
</form>
```

#### HTML attributes

**Syntax**

```liquid
{% form 'form_type', attribute: string %}
  content
{% endform %}
```

You can specify HTML attributes by adding a parameter that matches the attribute name with `data-` prepended, and the desired value.

**Code**

```liquid
{% form "product", product, id: 'custom-id', class: 'custom-class', data-example: '100' %}
  <!-- form content -->
{% endform %}
```

**Data**

```json
{
  "product": {
    "id": 6786188247105
  }
}
```

**Output**

```html
<form method="post" action="/cart/add" id="custom-id" accept-charset="UTF-8" class="custom-class" enctype="multipart/form-data" data-example="100"><input type="hidden" name="form_type" value="product" /><input type="hidden" name="utf8" value="✓" />
  <!-- form content -->
<input type="hidden" name="product-id" value="6786188247105" /></form>
```

---

# Iteration tags

## for

> Fonte: https://shopify.dev/docs/api/liquid/tags/for

Renders an expression for every item in an array.

You can do a maximum of 50 iterations with a `for` loop. If you need to iterate over more than 50 items, then use the `paginate` tag to split the items over multiple pages.

**Tip:** Every `for` loop has an associated `forloop` object with information about the loop.

### Syntax

```liquid
{% for variable in array %}
  expression
{% endfor %}
```

#### Parameters

| Parameter | Description |
|-----------|-------------|
| `variable` | The current item in the array. |
| `array` | The array to iterate over. |
| `expression` | The expression to render for each iteration. |

#### Example

**Code:**
```liquid
{% for product in collection.products -%}
  {{ product.title }}
{%- endfor %}
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
Draught of Immortality
Glacier ice
Health potion
Invisibility potion
```

### limit

Limit the number of iterations using the `limit` parameter.

```liquid
{% for variable in array limit: number %}
  expression
{% endfor %}
```

**Tip:** Limit data fetching for paginated arrays using the `paginate` tag instead of `limit` for improved server-side performance.

#### Example

**Code:**
```liquid
{% for product in collection.products limit: 2 -%}
  {{ product.title }}
{%- endfor %}
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
Draught of Immortality
Glacier ice
```

### offset

Specify a 1-based index to start iterating at using the `offset` parameter.

```liquid
{% for variable in array offset: number %}
  expression
{% endfor %}
```

#### Example

**Code:**
```liquid
{% for product in collection.products offset: 2 -%}
  {{ product.title }}
{%- endfor %}
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
Health potion
Invisibility potion
```

### range

Instead of iterating over specific items in an array, you can specify a numeric range to iterate over.

```liquid
{% for variable in (number..number) %}
  expression
{% endfor %}
```

**Note:** You can define the range using both literal and variable values.

#### Example

**Code:**
```liquid
{% for i in (1..3) -%}
  {{ i }}
{%- endfor %}

{%- assign lower_limit = 2 -%}
{%- assign upper_limit = 4 -%}

{% for i in (lower_limit..upper_limit) -%}
  {{ i }}
{%- endfor %}
```

**Output:**
```html
1
2
3

2
3
4
```

### reversed

Iterate in reverse order using the `reversed` parameter.

```liquid
{% for variable in array reversed %}
  expression
{% endfor %}
```

#### Example

**Code:**
```liquid
{% for product in collection.products reversed -%}
  {{ product.title }}
{%- endfor %}
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
Invisibility potion
Health potion
Glacier ice
Draught of Immortality
```

### forloop object

Information about a parent `for` loop.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| `first` | boolean | Returns `true` if the current iteration is the first. Returns `false` if not. |
| `index` | number | The 1-based index of the current iteration. |
| `index0` | number | The 0-based index of the current iteration. |
| `last` | boolean | Returns `true` if the current iteration is the last. Returns `false` if not. |
| `length` | number | The total number of iterations in the loop. |
| `parentloop` | forloop | The parent `forloop` object. If the current `for` loop isn't nested inside another `for` loop, then `nil` is returned. |
| `rindex` | number | The 1-based index of the current iteration, in reverse order. |
| `rindex0` | number | The 0-based index of the current iteration, in reverse order. |

**Example:**
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

#### Use the parentloop property

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

#### Use the forloop object

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

## cycle

> Fonte: https://shopify.dev/docs/api/liquid/tags/cycle

Loops through a group of strings and outputs them one at a time for each iteration of a `for` loop.

The `cycle` tag must be used inside a `for` loop.

**Tip:** Use the `cycle` tag to output text in a predictable pattern. For example, to apply odd/even classes to rows in a table.

### Syntax

```liquid
{% cycle string, string, ... %}
```

### Example

**Input:**

```liquid
{% for i in (1..4) -%}
  {% cycle 'one', 'two', 'three' %}
{%- endfor %}
```

**Output:**

```html
one
two
three
one
```

### Create unique cycle groups

#### Syntax

```liquid
{% cycle string: string, string, ... %}
```

If you include multiple `cycle` tags with the same parameters in the same template, each set of tags is treated as the same group. This means a `cycle` tag might output any of the provided strings instead of always starting at the first. To prevent this, specify a group name for each `cycle` tag.

#### Example

**Input:**

```liquid
<!-- Iteration 1 -->
{% for i in (1..4) -%}
  {% cycle 'one', 'two', 'three' %}
{%- endfor %}

<!-- Iteration 2 -->
{% for i in (1..4) -%}
  {% cycle 'one', 'two', 'three' %}
{%- endfor %}

<!-- Iteration 3 -->
{% for i in (1..4) -%}
  {% cycle 'group_1': 'one', 'two', 'three' %}
{%- endfor %}

<!-- Iteration 4 -->
{% for i in (1..4) -%}
  {% cycle 'group_2': 'one', 'two', 'three' %}
{%- endfor %}
```

**Output:**

```html
<!-- Iteration 1 -->
one
two
three
one


<!-- Iteration 2 -->
two
three
one
two


<!-- Iteration 3 -->
one
two
three
one


<!-- Iteration 4 -->
one
two
three
one
```

---

## tablerow

> Fonte: https://shopify.dev/docs/api/liquid/tags/tablerow

Generates HTML table rows for every item in an array.

The `tablerow` tag must be wrapped in HTML `<table>` and `</table>` tags.

**Tip:** Every `tablerow` loop has an associated `tablerowloop` object with information about the loop.

### Syntax

```liquid
{% tablerow variable in array %}
  expression
{% endtablerow %}
```

#### Parameters

| Parameter | Description |
|-----------|-------------|
| `variable` | The current item in the array. |
| `array` | The array to iterate over. |
| `expression` | The expression to render. |

### Examples

#### Basic tablerow

```liquid
<table>
  {% tablerow product in collection.products %}
    {{ product.title }}
  {% endtablerow %}
</table>
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
<table>
  <tr class="row1">
<td class="col1">
    Draught of Immortality
  </td><td class="col2">
    Glacier ice
  </td><td class="col3">
    Health potion
  </td><td class="col4">
    Invisibility potion
  </td></tr>

</table>
```

### tablerow tag parameters

#### cols

```liquid
{% tablerow variable in array cols: number %}
  expression
{% endtablerow %}
```

Defines how many columns the table should have using the `cols` parameter.

**Example:**
```liquid
<table>
  {% tablerow product in collection.products cols: 2 %}
    {{ product.title }}
  {% endtablerow %}
</table>
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
<table>
  <tr class="row1">
<td class="col1">
    Draught of Immortality
  </td><td class="col2">
    Glacier ice
  </td></tr>
<tr class="row2"><td class="col1">
    Health potion
  </td><td class="col2">
    Invisibility potion
  </td></tr>

</table>
```

#### limit

```liquid
{% tablerow variable in array limit: number %}
  expression
{% endtablerow %}
```

Limits the number of iterations using the `limit` parameter.

**Example:**
```liquid
<table>
  {% tablerow product in collection.products limit: 2 %}
    {{ product.title }}
  {% endtablerow %}
</table>
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
<table>
  <tr class="row1">
<td class="col1">
    Draught of Immortality
  </td><td class="col2">
    Glacier ice
  </td></tr>

</table>
```

#### offset

```liquid
{% tablerow variable in array offset: number %}
  expression
{% endtablerow %}
```

Specifies a 1-based index to start iterating at using the `offset` parameter.

**Example:**
```liquid
<table>
  {% tablerow product in collection.products offset: 2 %}
    {{ product.title }}
  {% endtablerow %}
</table>
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
<table>
  <tr class="row1">
<td class="col1">
    Health potion
  </td><td class="col2">
    Invisibility potion
  </td></tr>

</table>
```

#### range

```liquid
{% tablerow variable in (number..number) %}
  expression
{% endtablerow %}
```

Instead of iterating over specific items in an array, you can specify a numeric range to iterate over.

**Note:** You can define the range using both literal and variable values.

**Example:**
```liquid
<table>
  {% tablerow i in (1..3) %}
    {{ i }}
  {% endtablerow %}
</table>

{%- assign lower_limit = 2 -%}
{%- assign upper_limit = 4 -%}

<table>
  {% tablerow i in (lower_limit..upper_limit) %}
    {{ i }}
  {% endtablerow %}
</table>
```

**Output:**
```html
<table>
  <tr class="row1">
<td class="col1">
    1
  </td><td class="col2">
    2
  </td><td class="col3">
    3
  </td></tr>

</table><table>
  <tr class="row1">
<td class="col1">
    2
  </td><td class="col2">
    3
  </td><td class="col3">
    4
  </td></tr>

</table>
```

### tablerowloop object

Information about a parent `tablerow` loop.

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| `col` | number | The 1-based index of the current column. |
| `col_first` | boolean | Returns `true` if the current column is the first in the row. Returns `false` if not. |
| `col_last` | boolean | Returns `true` if the current column is the last in the row. Returns `false` if not. |
| `col0` | number | The 0-based index of the current column. |
| `first` | boolean | Returns `true` if the current iteration is the first. Returns `false` if not. |
| `index` | number | The 1-based index of the current iteration. |
| `index0` | number | The 0-based index of the current iteration. |
| `last` | boolean | Returns `true` if the current iteration is the last. Returns `false` if not. |
| `length` | number | The total number of iterations in the loop. |
| `rindex` | number | The 1-based index of the current iteration, in reverse order. |
| `rindex0` | number | The 0-based index of the current iteration, in reverse order. |
| `row` | number | The 1-based index of current row. |

**Example:**
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

## break

> Fonte: https://shopify.dev/docs/api/liquid/tags/break

Stops a `for` loop from iterating.

### Syntax

```liquid
{% break %}
```

### Example

**Input:**

```liquid
{% for i in (1..5) -%}
  {%- if i == 4 -%}
    {% break %}
  {%- else -%}
    {{ i }}
  {%- endif -%}
{%- endfor %}
```

**Output:**

```html
1
2
3
```

---

## continue

> Fonte: https://shopify.dev/docs/api/liquid/tags/continue

Causes a `for` loop to skip to the next iteration.

### Syntax

```liquid
{% continue %}
```

### Example

**Input:**

```liquid
{% for i in (1..5) -%}
  {%- if i == 4 -%}
    {% continue %}
  {%- else -%}
    {{ i }}
  {%- endif -%}
{%- endfor %}
```

**Output:**

```html
1
2
3
5
```

---

## paginate

> Fonte: https://shopify.dev/docs/api/liquid/tags/paginate

Splits an array's items across multiple pages.

Because `for` loops are limited to 50 iterations per page, you need to use the `paginate` tag to iterate over an array that has more than 50 items. The following arrays can be paginated:

* `article.comments`
* `blog.articles`
* `collections`
* `collection.products`
* `customer.addresses`
* `customer.orders`
* `metaobject_definition.values`
* `pages`
* `product.variants`
* `search.results`
* `article_list` settings
* `collection_list` settings
* `product_list` settings

Within the `paginate` tag, you have access to the `paginate` object. You can use this object, or the `default_pagination` filter, to build page navigation.

> The `paginate` tag allows the user to paginate to the 25,000th item in the array and no further. To reach items further in the array it should be filtered before paginating.

### Syntax

```liquid
{% paginate array by page_size %}
  {% for item in array %}
    forloop_content
  {% endfor %}
{% endpaginate %}
```

#### Parameters

| Parameter | Description |
|-----------|-------------|
| `array` | The array to be looped over. |
| `page_size` | The number of array items to include per page, between 1 and 250. |
| `item` | An item in the array being looped. |
| `forloop_content` | Content for each loop iteration. |

### Examples

#### Basic pagination

```liquid
{% paginate collection.products by 5 %}
  {% for product in collection.products -%}
    {{ product.title }}
  {%- endfor %}

  {{- paginate | default_pagination }}
{% endpaginate %}
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
      }
    ],
    "products_count": 19
  }
}
```

**Output:**

```html
Blue Mountain Flower
Charcoal
Crocodile tears
Dandelion milk
Draught of Immortality

<span class="page current">1</span> <span class="page"><a href="/services/liquid_rendering/resource?page=2" title="">2</a></span> <span class="page"><a href="/services/liquid_rendering/resource?page=3" title="">3</a></span> <span class="page"><a href="/services/liquid_rendering/resource?page=4" title="">4</a></span> <span class="next"><a href="/services/liquid_rendering/resource?page=2" title="">Next &raquo;</a></span>
```

#### Paginating setting arrays

To allow the pagination of `article_list`, `collection_list` and `product_list` settings to operate independently from other paginated lists on a page, these lists use a pagination query parameter with a unique key. The key is automatically assigned by the `paginate` tag, and you don't need to reference the key in your code. However, you can access the key using `paginate.page_param`.

> To paginate two arrays independently without refreshing the entire page, you can use the Section Rendering API.

#### Limit data fetching

The `limit` parameter of the `for` tag controls the number of iterations, but not the amount of information fetched. Using the `paginate` tag with a matching `page_size` can reduce the data queried, leading to faster server response times.

For example, referencing `collection.products` will fetch up to 50 products by default, regardless of the forloop's `limit` parameter. Use `paginate` and set a `page_size` to limit the amount of data fetched, and opt not to display any pagination controls.

More data than requested in a specific section may be returned. Because of this, make sure to include both `paginate` and `limit` when using this technique.

```liquid
{% paginate collection.products by 4 %}
  {% for product in collection.products limit: 4 -%}
    {{ product.title }}
  {%- endfor %}
{% endpaginate -%}

<!-- Less performant method -->
{% for product in collection.products limit: 4 -%}
  {{ product.title }}
{%- endfor -%}
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
      }
    ],
    "products_count": 19
  }
}
```

**Output:**

```html
Blue Mountain Flower
Charcoal
Crocodile tears
Dandelion milk

<!-- Less performant method -->
Blue Mountain Flower
Charcoal
Crocodile tears
Dandelion milk
```

### window_size parameter

#### Syntax

```liquid
{% paginate collection.products by 3, window_size: 1 %}
```

Set the window size of the pagination. The window size is the number of pages that should be visible in the pagination navigation.

#### Example

```liquid
{% paginate collection.products by 3, window_size: 1 %}
  {% for product in collection.products -%}
    {{ product.title }}
  {%- endfor %}

  {{- paginate | default_pagination }}
{% endpaginate %}
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
      }
    ],
    "products_count": 19
  }
}
```

**Output:**

```html
Blue Mountain Flower
Charcoal
Crocodile tears

<span class="page current">1</span> <span class="deco">&hellip;</span> <span class="page"><a href="/services/liquid_rendering/resource?page=7" title="">7</a></span> <span class="next"><a href="/services/liquid_rendering/resource?page=2" title="">Next &raquo;</a></span>
```

---

# Syntax tags

## comment

> Fonte: https://shopify.dev/docs/api/liquid/tags/comment

Prevents an expression from being rendered or output.

Any text inside `comment` tags won't be output, and any Liquid code will be parsed, but not executed.

### Syntax

```liquid
{% comment %}
  content
{% endcomment %}
```

#### content

The content of the comment.

### Inline comments

#### Syntax

```liquid
{% # content %}
```

Inline comments prevent an expression inside of a tag `{% %}` from being rendered or output.

You can use inline comment tags to annotate your code, or to temporarily prevent logic in your code from executing.

You can create multi-line inline comments. However, each line in the tag must begin with a `#`, or a syntax error will occur.

#### Code

```liquid
{% # this is a comment %}

{% # for i in (1..3) -%}
  {{ i }}
{% # endfor %}

{%
  ###############################
  # This is a comment
  # across multiple lines
  ###############################
%}
```

### Inline comments inside `liquid` tags

You can use inline comment tags inside `liquid` tags. The tag must be used for each line that you want to comment.

#### Code

```liquid
{% liquid
  # this is a comment
  assign topic = 'Learning about comments!'
  echo topic
%}
```

#### Output

```html
Learning about comments!
```

---

## doc

> Fonte: https://shopify.dev/docs/api/liquid/tags/doc

Documents template elements with annotations.

The `doc` tag enables developers to embed documentation directly within Liquid templates. Content enclosed in `doc` tags remains unrendered and unoutputted. While Liquid code inside gets parsed, it won't execute. This supports developer tooling for features such as code completion, linting, and embedded reference material.

For comprehensive documentation syntax and usage patterns, consult the `LiquidDoc` reference.

### Syntax

```liquid
{% doc %}
  Renders a message.

  @param {string} foo - A string value.
  @param {string} [bar] - An optional string value.

  @example
  {% render 'message', foo: 'Hello', bar: 'World' %}
{% enddoc %}
```

---

## echo

> Fonte: https://shopify.dev/docs/api/liquid/tags/echo

Outputs an expression.

Using the `echo` tag is the same as wrapping an expression in curly brackets (`{{` and `}}`). However, unlike the curly bracket method, you can use the `echo` tag inside `liquid` tags.

**Tip:** You can use filters on expressions inside `echo` tags.

### Syntax

```liquid
{% liquid
  echo expression
%}
```

#### expression

The expression to be output.

### Examples

**Input:**

```liquid
{% echo product.title %}

{% liquid
  echo product.price | money
%}
```

**Data:**

```json
{
  "product": {
    "price": "10.00",
    "title": "Health potion"
  }
}
```

**Output:**

```html
Health potion

$10.00
```

---

## liquid

> Fonte: https://shopify.dev/docs/api/liquid/tags/liquid

Allows you to have a block of Liquid without delimiters on each tag.

Because the tags don't have delimiters, each tag needs to be on its own line.

> **Tip:** Use the `echo` tag to output an expression inside `liquid` tags.

### Syntax

```liquid
{% liquid
  expression
%}
```

#### expression

The expression to be rendered inside the `liquid` tag.

### Example

**Input:**

```liquid
{% liquid
  # Show a message that's customized to the product type

  assign product_type = product.type | downcase
  assign message = ''

  case product_type
    when 'health'
      assign message = 'This is a health potion!'
    when 'love'
      assign message = 'This is a love potion!'
    else
      assign message = 'This is a potion!'
  endcase

  echo message
%}
```

**Data:**

```json
{
  "product": {
    "type": null
  }
}
```

**Output:**

```html
This is a health potion!
```

---

## raw

> Fonte: https://shopify.dev/docs/api/liquid/tags/raw

Outputs any Liquid code as text instead of rendering it.

### Syntax

```liquid
{% raw %}
  expression
{% endraw %}
```

#### expression

The expression to be output without being rendered.

### Examples

#### Code

```liquid
{% raw %}
{{ 2 | plus: 2 }} equals 4.
{% endraw %}
```

#### Output

```html
{{ 2 | plus: 2 }} equals 4.
```

---

# Theme tags

## content_for

> Fonte: https://shopify.dev/docs/api/liquid/tags/content_for

Creates a designated area in your theme where blocks can be rendered.

The `content_for` tag requires a type parameter to differentiate between rendering a number of theme blocks (`'blocks'`) and a single static block (`'block'`).

### Syntax

```liquid
{% content_for 'blocks' %}
{% content_for 'block', type: "slide", id: "slide-1" %}
```

### blocks

#### Syntax

```liquid
{% content_for "blocks" %}
```

Creates a designated area that renders theme blocks as configured in the JSON template or section groups, allowing merchants to add, remove, and rearrange blocks using the theme editor. See theme blocks documentation for more information.

### block

#### Syntax

```liquid
{% content_for "block", type: "button", id: "static-block-1", color: "red" %}
```

Renders a static theme block of the specified type with the provided ID. You can pass additional arbitrary parameters (such as `color`) that will be accessible within the static block using `{{ color }}`. Consult static blocks documentation to learn more.

---

## javascript

> Fonte: https://shopify.dev/docs/api/liquid/tags/javascript

JavaScript code included in section, block and snippet files.

Each section, block or snippet can have only one `{% javascript %}` tag.

To learn more about how JavaScript that's defined between the `javascript` tags is loaded and run, refer to the documentation for javascript tags.

> **Caution:** Liquid isn't rendered inside of `{% javascript %}` tags. Including Liquid code can cause syntax errors.

### Syntax

```liquid
{% javascript %}
  javascript_code
{% endjavascript %}
```

#### javascript_code

The JavaScript code for the section, block or snippet.

---

## layout

> Fonte: https://shopify.dev/docs/api/liquid/tags/layout

Specify which layout to use.

### Syntax

```liquid
{% layout name %}
```

#### name

The name of the layout file you want to use, wrapped in quotes, or `none` for no layout.

By default, the `theme.liquid` layout is used. The `layout` tag allows you to specify an alternate layout, or use no layout.

```liquid
{% layout 'full-width' %}
{% layout none %}
```

---

## render

> Fonte: https://shopify.dev/docs/api/liquid/tags/render

Renders a snippet or app block.

Inside snippets and app blocks, you can't directly access variables that are created outside of the snippet or app block. However, you can specify variables as parameters to pass outside variables to snippets.

While you can't directly access created variables, you can access global objects, as well as any objects that are directly accessible outside the snippet or app block. For example, a snippet or app block inside the product template can access the `product` object, and a snippet or app block inside a section can access the `section` object.

Outside a snippet or app block, you can't access variables created inside the snippet or app block.

> **Note:** When you render a snippet using the `render` tag, you can't use the `include` tag inside the snippet.

### Syntax

```liquid
{% render 'filename' %}
```

#### filename

The name of the snippet to render, without the `.liquid` extension.

### render tag parameters

#### for

**Syntax**

```liquid
{% render 'filename' for array as item %}
```

You can render a snippet for every item in an array using the `for` parameter. You can also supply an optional `as` parameter to reference the current item in the iteration inside the snippet. Additionally, you can access a `forloop` object for the loop inside the snippet.

#### Passing variables to a snippet

**Syntax**

```liquid
{% render 'filename', variable: value %}
```

Variables that have been created outside of a snippet can be passed to a snippet as parameters on the `render` tag.

> **Note:** Any changes that are made to a passed variable apply only within the snippet.

#### with

**Syntax**

```liquid
{% render 'filename' with object as name %}
```

You can pass a single object to a snippet using the `with` parameter. You can also supply an optional `as` parameter to specify a custom name to reference the object inside the snippet. If you don't use the `as` parameter to specify a custom name, then you can reference the object using the snippet filename.

---

## section

> Fonte: https://shopify.dev/docs/api/liquid/tags/section

Renders a section.

Rendering a section with the `section` tag renders a section statically. To learn more about sections and how to use them in your theme, refer to Render a section.

### Syntax

```liquid
{% section 'name' %}
```

#### name

The name of the section file you want to render.

### Examples

#### Code

```liquid
{% section 'header' %}
```

#### Data

```json
{
  "cart": {
    "item_count": 2
  },
  "request": {
    "origin": "https://polinas-potent-potions.myshopify.com",
    "page_type": "index"
  },
  "routes": {
    "account_url": "/account",
    "cart_url": "/cart",
    "root_url": "/",
    "search_url": "/search"
  },
  "settings": {
    "accent_icons": "text",
    "cart_type": "notification",
    "inputs_shadow_vertical_offset": 4,
    "predictive_search_enabled": true,
    "social_facebook_link": "",
    "social_instagram_link": "",
    "social_pinterest_link": "",
    "social_snapchat_link": "",
    "social_tiktok_link": "",
    "social_tumblr_link": "",
    "social_twitter_link": "",
    "social_vimeo_link": "",
    "social_youtube_link": ""
  },
  "shop": {
    "customer_accounts_enabled": true,
    "name": "Polina's Potent Potions"
  }
}
```

#### Output

```html
<div id="shopify-section-header" class="shopify-section section-header">
  <!-- Full rendered header section HTML -->
</div>
```

---

## sections

> Fonte: https://shopify.dev/docs/api/liquid/tags/sections

Renders a section group.

Use this tag to render section groups as part of the theme's layout content. Place the `sections` tag where you want to render it in the layout.

To learn more about section groups and how to use them in your theme, refer to Section groups.

### Syntax

```liquid
{% sections 'name' %}
```

#### name

The name of the section group file you want to render.

---

## style

> Fonte: https://shopify.dev/docs/api/liquid/tags/style

Generates an HTML `<style>` tag with an attribute of `data-shopify`.

> **Note:** If you reference color settings inside `style` tags, the associated CSS rules will update as the setting changes in the theme editor, without requiring a page refresh. See additional information and limitations of live preview.

### Syntax

```liquid
{% style %}
  CSS_rules
{% endstyle %}
```

#### CSS_rules

The desired CSS rules for the `<style>` tag.

### Example

**Liquid Input:**

```liquid
{% style %}
  .h1 {
    color: {{ settings.colors_accent_1 }};
  }
{% endstyle %}
```

**Data:**

```json
{
  "settings": {
    "colors_accent_1": "#121212"
  }
}
```

**Output:**

```html
<style data-shopify>
  .h1 {
    color: #121212;
  }
</style>
```

---

## stylesheet

> Fonte: https://shopify.dev/docs/api/liquid/tags/stylesheet

CSS styles included in section, block, and snippet files.

Each section, block or snippet can have only one `{% stylesheet %}` tag.

To learn more about how CSS that's defined between the `stylesheet` tags is loaded and run, refer to the documentation for stylesheet tags.

> **Caution:** Liquid isn't rendered inside of `{% stylesheet %}` tags. Including Liquid code can cause syntax errors.

### Syntax

```liquid
{% stylesheet %}
  css_styles
{% endstylesheet %}
```

#### css_styles

The CSS styles for the section, block or snippet.

---

# Variable tags

## assign

> Fonte: https://shopify.dev/docs/api/liquid/tags/assign

Creates a new variable.

You can create variables of any basic type, object, or object property.

> **Caution:** Predefined Liquid objects can be overridden by variables with the same name. To ensure access to all Liquid objects, verify your variable name doesn't match a predefined object's name.

### Syntax

```liquid
{% assign variable_name = value %}
```

#### variable_name

The name of the variable being created.

#### value

The value you want to assign to the variable.

### Example

**Liquid input:**

```liquid
{%- assign product_title = product.title | upcase -%}

{{ product_title }}
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

---

## capture

> Fonte: https://shopify.dev/docs/api/liquid/tags/capture

Creates a new variable with a string value.

You can create complex strings with Liquid logic and variables.

> **Caution:** Predefined Liquid objects can be overridden by variables with the same name. Ensure your variable name doesn't match a predefined object's name.

### Syntax

```liquid
{% capture variable %}
  value
{% endcapture %}
```

| Parameter | Description |
|-----------|-------------|
| `variable` | The name of the variable being created. |
| `value` | The value you want to assign to the variable. |

### Example

**Input:**

```liquid
{%- assign up_title = product.title | upcase -%}
{%- assign down_title = product.title | downcase -%}
{%- assign show_up_title = true -%}

{%- capture title -%}
  {% if show_up_title -%}
    Upcase title: {{ up_title }}
  {%- else -%}
    Downcase title: {{ down_title }}
  {%- endif %}
{%- endcapture %}

{{ title }}
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
Upcase title: HEALTH POTION
```

---

## increment

> Fonte: https://shopify.dev/docs/api/liquid/tags/increment

Creates a new variable, with a default value of 0, that's increased by 1 with each subsequent call.

> **Caution:** Predefined Liquid objects can be overridden by variables with the same name. To make sure that you can access all Liquid objects, make sure that your variable name doesn't match a predefined object's name.

Variables that are declared with `increment` are unique to the layout, template, or section file that they're created in. However, the variable is shared across snippets included in the file.

Similarly, variables that are created with `increment` are independent from those created with `assign` and `capture`. However, `increment` and `decrement` share variables.

### Syntax

```liquid
{% increment variable_name %}
```

#### variable_name

The name of the variable being incremented.

### Examples

```liquid
{% increment variable %}
{% increment variable %}
{% increment variable %}
```

**Output:**

```html
0
1
2
```

---

## decrement

> Fonte: https://shopify.dev/docs/api/liquid/tags/decrement

Creates a new variable, with a default value of -1, that's decreased by 1 with each subsequent call.

> **Caution:** Predefined Liquid objects can be overridden by variables with the same name. To ensure access to all Liquid objects, variable names should not match predefined object names.

Variables declared with `decrement` are unique to the layout, template, or section file where they're created. However, the variable is shared across snippets included in that file.

Variables created with `decrement` are independent from those created with `assign` and `capture`. However, `decrement` and `increment` share variables.

### Syntax

```liquid
{% decrement variable_name %}
```

#### variable_name

The name of the variable being decremented.

### Example

**Input:**

```liquid
{% decrement variable %}
{% decrement variable %}
{% decrement variable %}
```

**Output:**

```html
-1
-2
-3
```

---

# Deprecated tags

## include

> Fonte: https://shopify.dev/docs/api/liquid/tags/include

Renders a snippet.

Inside the snippet, you can access and alter variables that are created outside of the snippet.

> **Deprecated:** Deprecated because the way that variables are handled reduces performance and makes code harder to both read and maintain.
>
> The `include` tag has been replaced by `render`.

### Syntax

```liquid
{% include 'filename' %}
```

#### filename

The name of the snippet to render, without the `.liquid` extension.

---

## Pagine non catturate

Nessuna. Tutti i tag elencati nell'indice e nelle pagine di categoria sono stati catturati con successo.

Nota: la pagina indice principale (`https://shopify.dev/docs/api/liquid/tags`) e alcune pagine di categoria (es. `conditional-tags`, `iteration-tags`, `syntax-tags`, `theme-tags`, `variable-tags`, `html-tags`) non espongono via WebFetch l'elenco completo della barra laterale; l'enumerazione dei tag foglia è stata quindi ricavata dalle pagine di categoria disponibili e dall'elenco canonico dei tag Liquid di Shopify, e ogni singola pagina di tag è stata recuperata e verificata individualmente. Il path `https://shopify.dev/docs/api/liquid/tags/deprecated-tags` restituisce HTTP 404 (categoria senza pagina di indice dedicata); il suo unico tag foglia, `include`, è stato comunque catturato dalla sua pagina individuale.
