# 5. Theme Features

Questo capitolo raccoglie in modo fedele la sezione **"Theme features"** della documentazione Shopify Themes. Le theme features sono funzionalità Shopify che puoi abilitare o aggiungere a un tema. Se costruisci un tema per un cliente o per il tuo store, puoi scegliere quali includere; se costruisci un tema per il Shopify Theme Store, alcune di queste feature devono essere incluse.

Le feature ricadono nelle seguenti categorie: Product merchandising, Pricing and payments, Delivery and fulfillment, Customer engagement, Shopify Markets, Site navigation and search, SEO e Trust and security. Il capitolo include inoltre l'integrazione delle app, la migrazione a Online Store 2.0, i redirect di sign-in e il troubleshooting.

Ogni pagina è riprodotta integralmente con il suo URL di origine. Il codice Liquid/JSON/JS è riportato verbatim.

---

## Indice del capitolo

### Overview
- [Overview — Theme features](#overview--theme-features)

### Integrating apps
- [Integrating apps — App blocks for themes](#integrating-apps--app-blocks-for-themes)

### Product merchandising
- [Product merchandising — Overview](#product-merchandising--overview)
- [Product merchandising — Support product variants](#product-merchandising--support-product-variants)
- [Product merchandising — Product media (overview)](#product-merchandising--product-media-overview)
- [Product merchandising — Support product media](#product-merchandising--support-product-media)
- [Product merchandising — Product media UX guidelines](#product-merchandising--product-media-ux-guidelines)
- [Product merchandising — Product recommendations (overview)](#product-merchandising--product-recommendations-overview)
- [Product merchandising — Show related products on product pages](#product-merchandising--show-related-products-on-product-pages)
- [Product merchandising — Show complementary products on product pages](#product-merchandising--show-complementary-products-on-product-pages)
- [Product merchandising — Add a gift card recipient form](#product-merchandising--add-a-gift-card-recipient-form)
- [Product merchandising — Bundles grouped view emails](#product-merchandising--bundles-grouped-view-emails)

### Pricing and payments
- [Pricing and payments — Overview](#pricing-and-payments--overview)
- [Pricing and payments — Discounts](#pricing-and-payments--discounts)
- [Pricing and payments — Unit pricing](#pricing-and-payments--unit-pricing)
- [Pricing and payments — Subscriptions (overview)](#pricing-and-payments--subscriptions-overview)
- [Pricing and payments — Add subscriptions to your theme](#pricing-and-payments--add-subscriptions-to-your-theme)
- [Pricing and payments — Subscription UX guidelines](#pricing-and-payments--subscription-ux-guidelines)
- [Pricing and payments — Pre-orders and TBYB (overview)](#pricing-and-payments--pre-orders-and-tbyb-overview)
- [Pricing and payments — Add pre-orders and TBYB to your theme](#pricing-and-payments--add-pre-orders-and-tbyb-to-your-theme)
- [Pricing and payments — Pre-orders and TBYB UX guidelines](#pricing-and-payments--pre-orders-and-tbyb-ux-guidelines)
- [Pricing and payments — Accelerated checkout](#pricing-and-payments--accelerated-checkout)
- [Pricing and payments — Shop Pay Installments](#pricing-and-payments--shop-pay-installments)

### Delivery and fulfillment
- [Delivery and fulfillment — Overview](#delivery-and-fulfillment--overview)
- [Delivery and fulfillment — Show pickup availability on product pages](#delivery-and-fulfillment--show-pickup-availability-on-product-pages)

### Customer engagement
- [Customer engagement — Overview](#customer-engagement--overview)
- [Customer engagement — Email consent](#customer-engagement--email-consent)
- [Customer engagement — Add a contact form to your theme](#customer-engagement--add-a-contact-form-to-your-theme)
- [Customer engagement — Account component](#customer-engagement--account-component)

### Markets
- [Markets — Overview](#markets--overview)
- [Markets — Support multiple currencies and languages](#markets--support-multiple-currencies-and-languages)
- [Markets — Country and language selector UX guidelines](#markets--country-and-language-selector-ux-guidelines)

### Site navigation and search
- [Site navigation and search — Overview](#site-navigation-and-search--overview)
- [Site navigation and search — Add navigation to your theme](#site-navigation-and-search--add-navigation-to-your-theme)
- [Site navigation and search — Storefront search](#site-navigation-and-search--storefront-search)
- [Site navigation and search — Add predictive search to your theme](#site-navigation-and-search--add-predictive-search-to-your-theme)
- [Site navigation and search — Filtering (overview)](#site-navigation-and-search--filtering-overview)
- [Site navigation and search — Storefront filtering (overview)](#site-navigation-and-search--storefront-filtering-overview)
- [Site navigation and search — Support storefront filtering](#site-navigation-and-search--support-storefront-filtering)
- [Site navigation and search — Storefront filtering UX guidelines](#site-navigation-and-search--storefront-filtering-ux-guidelines)
- [Site navigation and search — Filter collections by tag](#site-navigation-and-search--filter-collections-by-tag)

### SEO
- [SEO — Overview](#seo--overview)
- [SEO — Add SEO metadata to your theme](#seo--add-seo-metadata-to-your-theme)
- [SEO — Customize robots.txt](#seo--customize-robotstxt)
- [SEO — Use hreflang tags in your theme](#seo--use-hreflang-tags-in-your-theme)

### Trust and security
- [Trust and security — Overview](#trust-and-security--overview)
- [Trust and security — CAPTCHA](#trust-and-security--captcha)
- [Trust and security — Security badges](#trust-and-security--security-badges)

### Migrating to Online Store 2.0
- [Migrating to Online Store 2.0 — Overview](#migrating-to-online-store-20--overview)
- [Migrating to Online Store 2.0 — Migration assessment](#migrating-to-online-store-20--migration-assessment)
- [Migrating to Online Store 2.0 — Migrating templates to Online Store 2.0](#migrating-to-online-store-20--migrating-templates-to-online-store-20)

### Sign-in redirects
- [Sign-in redirects — Customer sign-in links and redirects](#sign-in-redirects--customer-sign-in-links-and-redirects)

### Troubleshooting
- [Troubleshooting — Overview](#troubleshooting--overview)
- [Troubleshooting — Fix "Parameter Missing or Invalid" errors](#troubleshooting--fix-parameter-missing-or-invalid-errors)
- [Troubleshooting — Fix "can't be larger than 64 kilobytes" errors](#troubleshooting--fix-cant-be-larger-than-64-kilobytes-errors)
- [Troubleshooting — Using Protocol-Independent URLs](#troubleshooting--using-protocol-independent-urls)

---

## Overview — Theme features

> Fonte: https://shopify.dev/docs/storefronts/themes/theme-features

You can enable certain Shopify features or add functionality to a theme. If you're building a theme for a client, or for your own store, then you can pick and choose from these features. If you're building a theme for the Shopify Theme Store, then some of these features need to be included in your theme.

Features fall into the following categories:

* [Product merchandising](https://shopify.dev/docs/storefronts/themes/product-merchandising)
* [Pricing and payments](https://shopify.dev/docs/storefronts/themes/pricing-payments)
* [Delivery and fulfillment](https://shopify.dev/docs/storefronts/themes/delivery-fulfillment)
* [Customer engagement](https://shopify.dev/docs/storefronts/themes/customer-engagement)
* [Shopify Markets](https://shopify.dev/docs/storefronts/themes/markets)
* [Site navigation and search](https://shopify.dev/docs/storefronts/themes/navigation-search)
* [Trust and security](https://shopify.dev/docs/storefronts/themes/trust-security)

---

## Integrating apps — App blocks for themes

> Fonte: https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks

### Overview

App blocks allow merchants to add app content to themes through the theme editor without requiring direct code modifications. These blocks must be implemented within JSON template sections and are created using theme app extensions.

**Note:** Blocks of type `@app` aren't supported in statically rendered sections.

### Supporting app blocks

To enable app block functionality, include a generic `@app` block type in your section or theme block schema:

```json
"blocks": [
  {
    "type": "@app"
  }
]
```

**Caution:** Blocks of type `@app` don't accept the `limit` parameter.

### Render app blocks

Use the `{% content_for 'blocks' %}` Liquid tag to render app blocks:

```liquid
<div class="group">
  {% content_for 'blocks' %}
</div>
```

When rendering alongside section-defined blocks, use conditional rendering:

```liquid
{% for block in section.blocks %}
  {% case block.type %}
    {% when '@app' %}
      {% render block %}
    ...
  {% endcase %}
{% endfor %}
```

### App blocks and section settings

Sections that support app blocks can include only one resource setting of each type as a section setting.

### App block wrapper

Shopify wraps top-level app blocks using this hierarchy:

1. **Custom `apps.liquid`** – If provided, must support `@app` blocks and include a preset
2. **Custom `_blocks.liquid`** – Supports both `@app` and `@theme` blocks if `apps.liquid` absent
3. **Platform-generated default** – Used as fallback

**Caution:** The `apps.liquid` section schema can't contain the `templates` schema attribute.

#### Example wrapper section

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

**Note:** The `apps.liquid` section isn't a standard theme section and cannot be manually rendered.

> Nota dell'estrattore: nella sidebar "Theme features" la voce **"Integrating apps"** rimanda alla documentazione sull'integrazione delle app nei temi tramite app blocks / theme app extensions. Il contenuto canonico risiede in `architecture/blocks/app-blocks` (riprodotto qui sopra). Per approfondimenti correlati vedi anche [About theme app extensions](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions).

---

## Product merchandising — Overview

> Fonte: https://shopify.dev/docs/storefronts/themes/product-merchandising

To help merchants deliver an engaging product experience, Shopify offers these options:

* **Product variants**: A simple organization of product options to help customers easily find and select their desired product.
* **Product media**: Offer an immersive experience and enable merchants to increase a customer's confidence in their product.
* **Product recommendations**: Enable customers to discover new products.
* **Gift cards**: An alternative payment method. You can add a recipient form to your gift card product page.
* **Bundles emails**: Update your emails to account for Bundles as a grouped view.

---

## Product merchandising — Support product variants

> Fonte: https://shopify.dev/docs/storefronts/themes/product-merchandising/variants

Products can be broken up into a maximum of three options, and a single combination of those options is a variant. For example, if a t-shirt comes in sizes `S`, `M`, and `L`, and colors `Black`, `White`, and `Red`, then `S/Black` would be a variant of that product.

In this tutorial, you'll learn how to support product variants in your theme.

### Resources

To support product variants, you'll use the following:

* The [`product` object](https://shopify.dev/docs/api/liquid/objects/product)
* The [`variant` object](https://shopify.dev/docs/api/liquid/objects/variant)

### Implementing product variants

To support variants in your theme, you need to implement the following components:

* **Variant deep link handling**: A variant can be linked to directly, so you should ensure that the product information is updated for the 'selected' variant when a variant is referenced in a product link.
* **Variant selectors**: You should build a variant selector to allow customers to easily browse the available variants of a product.

  You might want to add these components to a section that can be included in a JSON product template, or a Liquid product template.

### Variant deep link handling

Variant deep links are product links that contain a `?variant=[variant-id]` query parameter, where `[variant-id]` is the [ID](https://shopify.dev/docs/api/liquid/objects/variant#variant-id) of the associated variant. This allows you to link directly to a variant. You can add this functionality to a section that can be included in a JSON product template, or a Liquid product template.

When variants are deep-linked, you can access which variant is linked through the `selected_variant` attribute of the [`product` object](https://shopify.dev/docs/api/liquid/objects/product#product-selected_variant). However, a product link won't always contain a deep-linked variant. In these cases, you can default to the selected, first available, or first variant through the `selected_or_first_available_variant` attribute.

You can also deep link using the format `?option_values=[option-value-id-1],...,[option-value-id-N]` where `[option-value-id]` is the [ID](https://shopify.dev/docs/api/liquid/objects/product_option_value#product_option_value-id) of the associated option value. One option value ID must be provided per product option and the order must match the option order. If the option value combination maps to a variant that is not present, the requested option values will be selected but the product fields [`selected_variant`](https://shopify.dev/docs/api/liquid/objects/product#product-selected_variant) and [`selected_or_first_available_variant`](https://shopify.dev/docs/api/liquid/objects/product#product-selected_or_first_available_variant) will return null.

After you identify the variant that you want to display, you need to ensure that the following product elements reflect it:

* Product media
* Product price
* Variant selector

#### Example

The following example assigns a default variant using `product.selected_or_first_available_variant`, populates a basic media and price display based on that variant, and selects that variant in a basic variant selector.

```liquid
{% assign current_variant = product.selected_or_first_available_variant %}


<!-- Product media -->
{% assign featured_media = current_variant.featured_media %}


{% case featured_media.media_type %}
{% when 'image' %}
  <div class="product-single__media"
    style="padding-top: {{ 1 | divided_by: featured_media.aspect_ratio | times: 100 }}%;"
    data-media-id="{{ featured_media.id }}"
  >
    {{ featured_media | image_url: width: 2048 | image_tag }}
  </div>
{% when 'external_video' %}
  <div class="product-single__media"
    style="padding-top: {{ 1 | divided_by: featured_media.aspect_ratio | times: 100 }}%;"
    data-media-id="{{ featured_media.id }}"
  >
    {{ featured_media | external_video_tag }}
  </div>
{% when 'video' %}
  <div class="product-single__media" data-media-id="{{ featured_media.id }}">
    {{ featured_media | video_tag: controls: true }}
  </div>
{% when 'model' %}
  <div class="product-single__media"
    style="padding-top: 100%;"
    data-media-id="{{ featured_media.id }}"
  >
    {{ featured_media | model_viewer_tag }}
  </div>
{% else %}
  <div class="product-single__media"
    style="padding-top: 100%;"
    data-media-id="{{ featured_media.id }}"
  >
    {{ featured_media | media_tag }}
  </div>
{% endcase %}


<!-- Product price -->
<div class="price">
<span class="price-reg">{{ current_variant.price | money }}</span>


{% if current_variant.compare_at_price > current_variant.price %}
  <span class="price-sale"><s>{{ current_variant.compare_at_price | money }}</s></span>
{% endif %}
</div>


<!-- Variant selector -->
<select name="id">
{% for variant in product.variants %}
  <option value="{{ variant.id }}"
    {% if variant == current_variant %}selected="selected"{% endif %}
  >
    {{ variant.title }} - {{ variant.price | money }}
  </option>
{% endfor %}
</select>
```

### Variant selectors

You can use a single variant selector where each option represents a variant. However, products may have more than one option. "For a better buyer experience and to avoid future compatibility issues, we recommend that you present each of these options separately in the UI." To achieve this, you can use the [`product.options_with_values` object](https://shopify.dev/docs/api/liquid/objects/product#product-options_with_values) to generate a selector for each option. You can then use JavaScript to update the state when a new option value is selected.

**Note:** Regardless of the approach you use for variant selection, you need to ensure that when a new variant is selected, the product media and price are updated to reflect the selected variant.

Variant selectors should be added to a section that can be included in a JSON product template, or a Liquid product template. They can also be included in product grid or product quick view snippets to allow customers to view variants on other pages, like collections.

**Tip:** Refer to the following files in Dawn for an example implementation:

* [`product-variant-picker.liquid` section](https://github.com/Shopify/dawn/blob/main/snippets/product-variant-picker.liquid)
* [`global.js` asset](https://github.com/Shopify/dawn/blob/main/assets/global.js)

---

## Product merchandising — Product media (overview)

> Fonte: https://shopify.dev/docs/storefronts/themes/product-merchandising/media

In addition to images, merchants can upload 3D models and videos, and attach YouTube or Vimeo videos as product media. This gives merchants the opportunity to offer a rich and immersive product experience.

You can display media in a theme using the following Liquid objects and filters:

* [external_video](https://shopify.dev/docs/api/liquid/objects/external_video)
* [video](https://shopify.dev/docs/api/liquid/objects/video)
* [video_source](https://shopify.dev/docs/api/liquid/objects/video_source)
* [model](https://shopify.dev/docs/api/liquid/objects/model)
* [model_source](https://shopify.dev/docs/api/liquid/objects/model_source)
* [media filters](https://shopify.dev/docs/api/liquid/filters/media-filters)

To learn about building a media display in your theme, refer to [Support product media](https://shopify.dev/docs/storefronts/themes/product-merchandising/media/support-media). In addition to a media display, you might also want to learn how to [use media preview images](https://shopify.dev/docs/storefronts/themes/product-merchandising/media/support-media#use-media-preview-images), [support AR functionality](https://shopify.dev/docs/storefronts/themes/product-merchandising/media/support-media#support-ar-functionality), and [control video functionality with parameters](https://shopify.dev/docs/storefronts/themes/product-merchandising/media/support-media#control-video-functionality-with-parameters).

You can also learn about media UX best practices in [Product media UX guidelines](https://shopify.dev/docs/storefronts/themes/product-merchandising/media/media-ux).

> **Tip:** To learn about creating 3D models for a merchant, refer to [Creating 3D models](https://help.shopify.com/en/partners/resources/creating-media/3d-models/creating-3d-models) in the Shopify Help Center.

---

## Product merchandising — Support product media

> Fonte: https://shopify.dev/docs/storefronts/themes/product-merchandising/media/support-media

Merchants can [add media](https://help.shopify.com/en/manual/products/product-media/add-media) to their products, like images, 3D models, videos, and YouTube or Vimeo videos.

In this tutorial, you'll learn how to support product media in your theme.

### Resources

* The `media` attribute of the [`product` object](https://shopify.dev/docs/api/liquid/objects/product#product-media)
* [Media filters](https://shopify.dev/docs/api/liquid/filters/media-filters)

### Implementing product media

Product media is usually displayed on the [product page](https://shopify.dev/docs/storefronts/themes/architecture/templates/product). However, you might want to display product media in other areas of your theme, so it's recommended to build your media display in a [snippet](https://shopify.dev/docs/storefronts/themes/architecture/snippets) so that it can be reused.

To display product media, you can loop through the `media` attribute of the `product` object and apply the associated media filter, depending on the media type.

#### Example

If you want to output product media on the product page, and your product page content is hosted in a `product.liquid` section, then you might do the following:

* Create a snippet called `media.liquid` to host your media display.
* Render `media.liquid` in your `product.liquid` section.

##### sections/product.liquid

```liquid
{% for media in product.media %}
  {% render 'media', media: media %}
{% endfor %}
```

##### snippets/media.liquid

```liquid
{% case media.media_type %}
  {% when 'image' %}
    <div class="product-single__media" style="padding-top: {{ 1 | divided_by: media.aspect_ratio | times: 100 }}%;" data-media-id="{{ media.id }}">
      {{ media | image_url: width: 2048, height: 2048 | image_tag }}
    </div>
  {% when 'external_video' %}
    <div class="product-single__media" style="padding-top: {{ 1 | divided_by: media.aspect_ratio | times: 100 }}%;" data-media-id="{{ media.id }}">
      {{ media | external_video_tag }}
    </div>
  {% when 'video' %}
    <div class="product-single__media" data-media-id="{{ media.id }}">
      {{ media | video_tag: controls: true }}
    </div>
  {% when 'model' %}
    <div class="product-single__media" style="padding-top: 100%;" data-media-id="{{ media.id }}">
      {{ media | model_viewer_tag }}
    </div>
  {% else %}
    <div class="product-single__media" style="padding-top: 100%;" data-media-id="{{ media.id }}">
      {{ media | media_tag }}
    </div>
{% endcase %}
```

Each media type in the example above is wrapped in a `<div>` element with custom `style` and data attributes. These are based on the considerations documented in UX considerations, and should be adjusted accordingly to match your approach.

**Tip:** For another example of supporting media in a theme, you can refer to Dawn's implementation in the [`main-product.liquid` section](https://github.com/Shopify/dawn/blob/main/sections/main-product.liquid) and [`product-thumbnail.liquid` snippet](https://github.com/Shopify/dawn/blob/main/snippets/product-thumbnail.liquid).

### UX considerations

Every theme requires a different approach to create responsive media that works across all screen sizes and devices. The following general recommendations can help ensure that you're offering a good customer experience:

* Make media elements responsive
* Preserve media element interactivity

A product can have multiple videos, so if your theme has a thumbnail view for each media element, or displays multiple media elements at once, you should ensure that only the active video is playing.

**Tip:** For more in-depth information, refer to [Product media UX guidelines](https://shopify.dev/docs/storefronts/themes/product-merchandising/media/media-ux).

#### Responsive media elements

"Shopify-hosted 3D models use Google's model viewer component, and externally rendered videos are rendered in `<iframe>` elements. Neither of these are responsive containers by default."

Shopify-hosted videos are rendered in HTML5 video players, which are responsive by default, however only once they're rendered.

Given the above, you should consider using an [aspect ratio box](https://css-tricks.com/aspect-ratio-boxes/) to create a responsive container for each.

**Tip:** 3D models don't have predefined aspect ratios, so it's common practice to create a square container by setting `padding-top` to `100%`.

#### Interactive media elements

Shopify-hosted, and externally-hosted, video elements, and 3D models have interactive components. For example, videos have progress bars and volume control, and 3D models can be rotated.

If any of these media elements are hosted in a carousel or swipe-interactive display, then the interactive components shouldn't interfere with the ability to interact with the display.

### Use media preview images

Every [media type](https://shopify.dev/docs/api/liquid/objects/media#media-preview_image) has a `preview_image` attribute. This could be useful in scenarios like the following:

* Product thumbnails
* Social media images

**Tip:** Applying the `image_url` Liquid [URL filter](https://shopify.dev/docs/api/liquid/filters/image_url) to the media object returns the `preview_image` URL.

#### Product thumbnails

If your theme displays thumbnails for each media source on the product, then you can utilize the `preview_image` attribute of the media object in order to show a thumbnail image for each media source.

For example:

```liquid
{% if product.media.size > 1 %}
  <div class="thumbnails-wrapper">
    {% for media in product.media %}
      <a data-thumbnail-id="{{ media.id }}">
        {{ media.preview_image | image_url: width: 110, height: 110, scale: 2 | image_tag: media.alt, 'product-single__thumbnail-image' }}
      </a>
    {% endfor %}
  </div>
{% endif %}
```

**Tip:** The above example adds a `data-thumbnail-id` attribute which is intended to be used in conjunction with the `data-media-id` attribute that's included in the general media loop example above. This gives you an easy way to associate a thumbnail with its media display.

#### Social media images

Rather than only showing images for social media previews, you can include media preview images as well.

For example:

```liquid
{%- if template.name == 'product' -%}
  {%- assign og_title = product.title | strip_html -%}
  {%- assign og_type = 'product' -%}


  {%- if product.media.size > 0 -%}
    {%- capture og_image_tags -%}
      {% for media in product.media limit:3 -%}
        <meta property="og:image" content="http:{{ media | image_url: width: 1200 height: 1200 }}" />
      {%- endfor %}
    {%- endcapture -%}


    {%- capture og_image_secure_url_tags -%}
      {% for media in product.media limit:3 -%}
        <meta property="og:image:secure_url" content="https:{{ media | image_url: with: 1200, height: 1200 }}" />
      {%- endfor %}
    {%- endcapture -%}
  {%- endif -%}
{%- endif -%}
```

### Support AR functionality

If merchants have 3D models of their products, then you can give them the option to showcase those models through AR. To do this, you can use the Shopify-XR library to support AR Quick Look in iOS's Safari, and Android's Scene Viewer.

You need to do the following to use this library:

* Initialize the library
* Launch the display

#### Initialize the library

The following JavaScript needs to be included on product pages to initialize the library:

```js
<script>
function setupShopifyXr(){
  if (!window.ShopifyXR) {
    document.addEventListener('shopify_xr_initialized', function() {
      setupShopifyXr();
    });
  }else{
    {% assign models = product.media | where: 'media_type', 'model' | json -%}
    window.ShopifyXR.addModels({{ models }});
    window.ShopifyXR.setupXRElements();
  }
}


window.Shopify.loadFeatures([
  {
    name: 'shopify-xr',
    version: '1.0',
    onLoad: setupShopifyXr
  }
]);
</script>
```

#### Launch the display

You can launch the display in two ways:

* With a button
* With JavaScript

##### Launch the display with a button

You can launch the display with a button that has the following attributes:

| Attribute | Description |
| - | - |
| `data-shopify-xr` | The Shopify-XR library scans the DOM for elements with this attribute and attaches a click handler to launch the display. |
| `data-shopify-model3d-id` | The [media ID](https://shopify.dev/docs/api/liquid/objects/media#media-id) of the current model. |
| `data-shopify-title` | The title of the product. |
| `data-shopify-xr-hidden` | A base data attribute for the Shopify-XR library to reference. |

You would include a button for each model type media source.

For example:

```liquid
{% for media in product.media %}
  {% case media.type %}
    ...
    {% when 'model' %}
      <div class="product-single__media" style="padding-top: 100%;" data-media-id="{{ media.id }}">
        {{ media | model_viewer_tag }}
      </div>


      <button
        data-shopify-xr
        data-shopify-model3d-id="{{ media.id }}"
        data-shopify-title="{{ product.title | escape }}"
        data-shopify-xr-hidden
      />
    ...
  {% endcase %}
{% endfor %}
```

##### Launch the display with JavaScript

Rather than include a button to launch the display, you can use JavaScript. For example:

```liquid
<script>
  window.ShopifyXR.launchXR({
    model3dId: [media-id],
    title: "{{ product.title | escape }}",
  });
</script>
```

**Note:** In the example above, `[media-id]` represents the [media ID](https://shopify.dev/docs/api/liquid/objects/media#media-id) for the associated model.

### Control video functionality with parameters

Shopify hosted videos can have all [HTML5 video attributes](https://developer.mozilla.org/docs/Web/HTML/Element/video#attributes) set when they're rendered with the Liquid [video_tag](https://shopify.dev/docs/api/liquid/filters/video_tag) or [media_tag](https://shopify.dev/docs/api/liquid/filters/media_tag) filter. For example:

* `autoplay` - Whether to automatically play the video after it's loaded.
* `loop` - Whether to loop the video.
* `muted` - Whether to mute the video's audio.
* `controls` - Whether a user can control the video playback.

Each parameter is `false` by default, however you can set them to be `true` like the following:

```liquid
<!-- Autoplay a video -->
{{ media | video_tag: autoplay: true }}


<!-- Autoplay a video, and loop it -->
{{ media | video_tag: autoplay: true, loop: true }}


<!-- Autoplay a video, loop it, and mute it -->
{{ media | video_tag: autoplay: true, loop: true, muted: true }}


<!-- Autoplay a video, loop it, mute it, and allow the user to control the video playback -->
{{ media | video_tag: autoplay: true, loop: true, muted: true, controls: true }}
```

**Tip:** You can control these same behaviors for externally-hosted videos using the Liquid [external_video_url](https://shopify.dev/docs/api/liquid/filters#external_video_url) filter. However, the available parameters depend on the video host.

---

## Product merchandising — Product media UX guidelines

> Fonte: https://shopify.dev/docs/storefronts/themes/product-merchandising/media/media-ux

The following are the main user experience (UX), and user interface (UI), aspects to consider with product media:

* Badges and buttons
* 3D model viewers
* Video players
* Slideshows

### Badges and buttons

Both video and 3D model media displays should have the following included in their display, with each associated element, respectively:

* A **play** or **3D** icon badge on the media thumbnail
* A **play** or **3D** icon button control on the featured media

3D model media displays should also include a **View in your space** button.

When adding these badges and buttons you should consider the following:

* The icons to use
* Their placement and sizing
* Their styling

#### The 'View in your space' button

When including the **View in your space** button, you should consider the following:

* If the button is being placed on top of the media display, then you need to ensure that video and 3D controls aren't obstructed.
* Only show the button for devices that support AR. Supporting devices will run iOS version 13 or higher, or Android version 9 or higher.
* If a product's media includes a 3D model, and that media should be displayed, then the button should be visible regardless of the currently displayed media type. Additionally, if the product has more than one 3D model, then the button should open the currently visible model, or the first model if none are currently visible.
* The button should include the 3D icon.
* The button should only be placed below the featured media.

**Tip:** To learn more about how to create a **View in your space** button, refer to Support product media documentation.

#### Icons

You should download an asset library that includes icons for video and 3D model displays. You should use the icons from this library, rather than create custom icons as they're industry standards that will help customers more easily identify the available interaction.

The icons come in two different styles:

* Rounded
* Angular

You should only use one style, and it should match your theme's style.

#### Badge placement and sizing

The placement, and sizing, of the display varies depending whether it's for a thumbnail badge, or a featured button control.

##### Thumbnail badge

Thumbnail badges should adhere to the following guidelines:

* They shouldn't occupy more than 1/9th of the thumbnail display, or 1/6th for landscape thumbnails, and shouldn't be smaller than `20px x 20px`.
* They can be aligned in any corner of the thumbnail, however should be uniformly aligned.

##### Featured button control

Featured button controls should be a minimum of `60px x 60px`, and maximum of `90px x 90px`.

#### Styling

The styling of the badges and buttons should adhere to the following guidelines:

* You should maintain the whitespace around the badge and button icons, as well as their proportions.
* The background of both badges, and buttons, can be modified to match your theme style. For example, a circle, rounded corners, etc.
* You should use existing colour settings to style the badges and buttons. There should be a high contrast between the background and the icon, as well as the media and the background, so settings for "Main background", "Heading", or "Text" generally give the best results.
* The opacity of the badge elements should vary depending on the element. Refer to Thumbnail badge opacity and Featured button control opacity to learn more.

In addition to the above, the **View in your space** button should either have no background color, or a very neutral color, so that it doesn't compete with primary and secondary calls to action.

##### Thumbnail badge opacity

The thumbnail badge elements should adhere to the following opacity guidelines:

* The icon opacity should be 60%.
* The badge background opacity should be 100%.
* The badge background should have a border that is at least 5% opacity of the icon's colour.

##### Featured button control opacity

The featured badge elements should adhere to the following opacity guidelines:

* The icon opacity should be 100%.
* The icon should persist on hover to maintain visibility.
* The badge background opacity should be a minimum of 75%.
* The badge background should have a border that is at least 5% opacity of the icon's colour.

### 3D model viewers

There are the following aspects to consider with 3D model viewers:

* The general behavior
* Accessibility
* The display elements
* Focus order

#### Accessibility

You should consider the following accessibility guidelines:

* "3D model content should default to inactive on page load as it can be unexpected, overwhelming, and distracting."
* 3D models should allow for panning with only the keyboard, in addition to mouse and swipe gestures.
* Add dedicated button controls, with appropriate labels, to control the model positioning.
* Ensure keyboard focus states are visible for sighted keyboard-only or voice dictation users.
* Refrain from shifting keyboard focus when interacting with a button control so customers can navigate away when they're ready.
* Allow for text descriptions of models for each stage view.
* Announce the current state of the model via ARIA live status element when button controls are interacted with.
* Test your implementation with a variety of assistive technologies. For example, keyboard alone, and multiple screen readers.

#### Display elements

3D model viewers should have the following display elements:

* 3D model viewer controls
* 3D model viewer progress bar

##### 3D model viewer controls

These controls should follow the badge and button styling suggestions, however the icons can be set to a minimum of 55% opacity.

These controls should be placed in the bottom right corner of the media element, either with even, or no padding.

You should keep visual consistency among all UI elements, so the corners of the control display shouldn't be rounded unless the icons and buttons in the theme are also rounded.

##### 3D model viewer progress bar

The progress bar is to show the load progress of the model. Similar to the controls, the progress bar should following the badge and button styling practices, however it should have 100% opacity, and should be placed at the top of the media element.

#### Focus order

In order to facilitate keyboard interaction, 3D model viewers should have a specific focus order on the related elements. There are two main states to consider:

* Inactive
* Active

##### Inactive

When the viewer is inactive, the focus order should be as follows:

1. Viewer controls

##### Active

When the viewer is active, the focus order should be as follows:

1. Viewer container
2. Zoom in
3. Zoom out
4. Fullscreen

### Video players

There are the following aspects to consider with video players:

* The general behavior
* Accessibility
* Styling and placement

#### Accessibility

* "Video content should default to paused on page load as it can be unexpected, overwhelming, and distracting."
* If a video plays on page load, it should be muted by default.
* Test your implementation with a variety of assistive technologies. For example, keyboard alone, and multiple screen readers.

#### Styling and placement

In addition to the badge and button styling suggestions, video players should adhere to the following:

* They should be placed at the bottom of the featured media, either with even, or no padding.
* If the theme uses custom focus states, then you should maintain consistency. Otherwise, the default browser focus state should be used.
* You should keep visual consistency among all UI elements, so the corners of the control display shouldn't be rounded unless the icons and buttons in the theme are also rounded.

### General behavior

**Note:** The following uses the terms "active" and "inactive". In the context of videos, this would be equivalent to "playing" and "paused".

"In general, video players and 3D model viewers should be set to inactive while advancing through media galleries as videos and models that aren't visible shouldn't be active."

If more than one media element is displaying at a time, then all media should be inactive by default, requiring the customer to initiate activity. If only one media element is visible at once, then you should adhere to the following:

* **Desktop** - The first media element on page load should be set to inactive, however as the media changes, the current media should automatically be set to active.
* **Tablet/Mobile** - All media elements should default to inactive, requiring the customer to initiate activity.

### Slideshows

If your theme uses a slideshow media gallery, then you shouldn't rely solely on swipe gestures for navigation as video players and 3D model viewers can interfere.

---

## Product merchandising — Product recommendations (overview)

> Fonte: https://shopify.dev/docs/storefronts/themes/product-merchandising/recommendations

Displaying recommended products to customers makes it easier for them to discover new products, and can help to increase online store sales.

Before you add product recommendations to your theme, it's a good idea to get familiar with the following:

* How to track recommendations
* Recommendation intents

To learn how to include recommendations in your theme, refer to [Related products](https://shopify.dev/docs/storefronts/themes/product-merchandising/recommendations/related-products) and [Complementary products](https://shopify.dev/docs/storefronts/themes/product-merchandising/recommendations/complementary-products). You can also refer to [Dawn's implementation](https://github.com/Shopify/dawn/blob/main/sections/related-products.liquid).

### Recommendation intents

Tailoring product recommendations across the customer's journey is a powerful way to help customers discover products. Recommendation intents are designed to recommend products using a targeted strategy.

Shopify provides the following types of recommendation intents:

* **Related products**: "Offer customers a mix of products that are similar to a product the customer is interacting with." An example is substitutable products that display in a **You might also like** section.
* **Complementary products**: "Offer customers products that are complementary to a product the customer is interacting with." An example is add-on products that display in a **Pair it with** section.

Only related recommendations are auto-generated by Shopify. Complementary recommendations need to be manually set up. Recommended products for each intent can be configured using the [Shopify Search & Discovery app](https://apps.shopify.com/search-and-discovery).

### Track recommendations

To track your product recommendations in Shopify, you need to use the format for product URLs that's specified by the API. To learn more, refer to [Tracking conversions for product recommendations](https://shopify.dev/docs/api/ajax/reference/product-recommendations#tracking-conversions-for-product-recommendations).

After you've implemented product recommendations, you can track how effective they are directly from the **Analytics** page in your Shopify admin. To learn more about product recommendation reports, refer to [Product recommendation conversion over time](https://help.shopify.com/manual/reports-and-analytics/shopify-reports/report-types/behaviour-reports#product-recommendation-conversions-over-time).

---

## Product merchandising — Show related products on product pages

> Fonte: https://shopify.dev/docs/storefronts/themes/product-merchandising/recommendations/related-products

Related products are products that are similar to a selected product. You can display potential substitutes to help customers discover other similar products they might like. These products should appear in a **You might also like** section on the product page.

Adding the related products section to your product pages displays an automatically generated list of product recommendations.

In this tutorial, you'll learn how to show related products in your theme.

### Resources

To implement product recommendations, you'll use the following:

* The [`recommendations`](https://shopify.dev/docs/api/liquid/objects/recommendations) object
* The `/{locale}/recommendations/products` endpoint of the [Product Recommendations API](https://shopify.dev/docs/api/ajax/reference/product-recommendations#get-locale-recommendations-products)

### Recommendation logic

The recommendation algorithm predicts the most relevant products based on the product that a customer is interacting with. The criteria that the algorithm uses depends on the merchant's online store. In general, it might take into account the following factors:

* **Purchase history**: Products that have historically been purchased together.
* **Product description**: Products with similar descriptions.
* **Related collections**: Products from collections that the current product is part of, excluding collections with handles `all` and `frontpage`.

#### Recommendation algorithm criteria

The criteria that's used depends on a merchant's online store, and the recommendation intent. The following outlines which criteria is used, and when:

| Criteria | Application |
| - | - |
| **Purchase history** and **Product description** | All merchants |
| **Related collections** | All merchants when purchase history and product description recommendations aren't available |

**Tip:** To learn more about the recommendation logic limitations, refer to Limitations.

The [Shopify Search & Discovery app](https://apps.shopify.com/search-and-discovery) enables users to customize product recommendation and search results, which can impact results from [storefront search](https://shopify.dev/docs/storefronts/themes/navigation-search/search) and the Ajax [Product Recommendations](https://shopify.dev/docs/api/ajax/reference/product-recommendations) API. To learn about how these results can be impacted, visit the [Shopify Help Center](https://help.shopify.com/manual/online-store/search-and-discovery/product-recommendations).

### Limitations

The following list describes some limitations of the recommendation logic:

* You can't customize the recommendation algorithm to exclude specific products. However, you can choose which of the returned products to show with JavaScript.
* The recommendation algorithm doesn't use orders that have been imported from another store or ecommerce platform to generate product recommendations.
* Products that are out of stock or set to a price of 0, gift cards, and products in the visitor's cart aren't included in recommendations.

### UI guidelines

The following best practices can help to make sure that you're displaying recommended products in a way that improves the customer experience:

* "The recommendation algorithm associates up to ten products with each product, in order of relevance." For this reason, it's a good idea to limit your recommendations to four products for each product page to promote only the most relevant recommendations.
* Make sure that you load the [proper image size](https://www.shopify.com/partners/blog/using-responsive-images) for the product card.
* Because the recommendations are loaded asynchronously with JavaScript, you might want to add an empty state or not show the recommended products section at all. The placeholder is swapped with the actual recommended products after you load them.
* Use phrases such as "You might also like" for the section header to explain to your customers why you're displaying the recommended products.

### Implementing product recommendations

In this implementation, the section content builds the general display by looping through each product returned through the `products` attribute of the `recommendations` object. However, this object isn't populated when the section is initially rendered, so you need to use JavaScript to retrieve the populated section content through the section response of the [Product Recommendations API](https://shopify.dev/docs/api/ajax/reference/product-recommendations#section-response).

#### Example

##### sections/product-recommendations.liquid

```liquid
<div
  class="product-recommendations"
  data-url="{{ routes.product_recommendations_url }}?section_id={{ section.id }}&product_id={{ product.id }}&limit=4&intent=related"
>
  {%- if recommendations.performed? and recommendations.products_count > 0 -%}
    {% if recommendations.intent == 'related' %}
      <h2>You may also like</h2>
    {% elsif recommendations.intent == 'complementary' %}
      <h2>Pair it with</h2>
    {% endif %}


    <ul>
      {%- for product in recommendations.products -%}
        <li class="product">
          <a href="{{ product.url }}">
            <img
              class="product__img"
              src="{{ product.featured_image | image_url: width: 300, height: 300 }}"
              alt="{{ product.featured_image.alt }}"
            />


            <p class="product__title">{{ product.title }}</p>
            <p class="product__price">{{ product.price | money}}</p>
          </a>
        </li>
      {%- endfor -%}
    </ul>
  {%- endif -%}
</div>


{% javascript %}
  const handleIntersection = (entries, observer) => {
    if (!entries[0].isIntersecting) return;


    observer.unobserve(productRecommendationsSection);


    const url = productRecommendationsSection.dataset.url;


    fetch(url)
      .then(response => response.text())
      .then(text => {
        const html = document.createElement('div');
        html.innerHTML = text;
        const recommendations = html.querySelector('.product-recommendations');


        if (recommendations && recommendations.innerHTML.trim().length) {
          productRecommendationsSection.innerHTML = recommendations.innerHTML;
        }
      })
      .catch(e => {
        console.error(e);
      });
  };


  const productRecommendationsSection = document.querySelector('.product-recommendations');
  const observer = new IntersectionObserver(handleIntersection, {rootMargin: '0px 0px 200px 0px'});


  observer.observe(productRecommendationsSection);
{% endjavascript %}


{% schema %}
  {
    "name": "Product recommendations",
    "settings": []
  }
{% endschema %}
```

---

## Product merchandising — Show complementary products on product pages

> Fonte: https://shopify.dev/docs/storefronts/themes/product-merchandising/recommendations/complementary-products

Complementary products are items that are often purchased alongside a selected product. They're frequently referred to as something that "pairs well with" the current product. You can display complementary products on the product page to help customers discover new items.

In this tutorial, you'll learn how to show complementary products in your theme.

### Resources

To implement product recommendations, you'll use the following:

* The [`recommendations`](https://shopify.dev/docs/api/liquid/objects/recommendations) object
* The `/{locale}/recommendations/products` endpoint of the [Product Recommendations API](https://shopify.dev/docs/api/ajax/reference/product-recommendations#get-locale-recommendations-products)

### Limitations

"Products that are out of stock or set to a price of 0, gift cards, and products in the visitor's cart aren't included in recommendations."

### UI guidelines

The following best practices can help ensure recommended products display in a way that improves customer experience:

* Complementary product recommendations should typically appear near the top of the product page, usually in the product information section near the original product image.
* "The product recommendations API serves up to 10 complementary products for each product. We recommend showing 2-3 products by default, and paginating for additional products."
* Ensure you load the proper image size for the product card.
* Since recommendations load asynchronously via JavaScript, consider adding an empty state or not displaying the section initially. The placeholder gets replaced with actual complementary products after loading.
* Use descriptive phrases such as "Pairs well with" for the section header to explain why these products are displayed.

### Implementing complementary products

The section content builds the general display by looping through each product returned through the `products` attribute of the `recommendations` object. However, this object isn't populated during initial section rendering, so you must use JavaScript to retrieve the populated section content through the section response of the Product Recommendations API.

> Nota: per i prodotti complementari occorre impostare `intent=complementary` nel parametro `data-url` (es. `&intent=complementary&limit=4`). L'esempio della documentazione riusa la stessa sezione `product-recommendations.liquid`.

##### sections/product-recommendations.liquid

```liquid
<div
  class="product-recommendations"
  data-url="{{ routes.product_recommendations_url }}?section_id={{ section.id }}&product_id={{ product.id }}&limit=4&intent=complementary"
>
  {%- if recommendations.performed? and recommendations.products_count > 0 -%}
    {% if recommendations.intent == 'related' %}
      <h2>You may also like</h2>
    {% elsif recommendations.intent == 'complementary' %}
      <h2>Pair it with</h2>
    {% endif %}


    <ul>
      {%- for product in recommendations.products -%}
        <li class="product">
          <a href="{{ product.url }}">
            <img
              class="product__img"
              src="{{ product.featured_image | image_url: width: 300, height: 300 }}"
              alt="{{ product.featured_image.alt }}"
            />


            <p class="product__title">{{ product.title }}</p>
            <p class="product__price">{{ product.price | money}}</p>
          </a>
        </li>
      {%- endfor -%}
    </ul>
  {%- endif -%}
</div>


{% javascript %}
  const handleIntersection = (entries, observer) => {
    if (!entries[0].isIntersecting) return;


    observer.unobserve(productRecommendationsSection);


    const url = productRecommendationsSection.dataset.url;


    fetch(url)
      .then(response => response.text())
      .then(text => {
        const html = document.createElement('div');
        html.innerHTML = text;
        const recommendations = html.querySelector('.product-recommendations');


        if (recommendations && recommendations.innerHTML.trim().length) {
          productRecommendationsSection.innerHTML = recommendations.innerHTML;
        }
      })
      .catch(e => {
        console.error(e);
      });
  };


  const productRecommendationsSection = document.querySelector('.product-recommendations');
  const observer = new IntersectionObserver(handleIntersection, {rootMargin: '0px 0px 200px 0px'});


  observer.observe(productRecommendationsSection);
{% endjavascript %}


{% schema %}
  {
    "name": "Product recommendations",
    "settings": []
  }
{% endschema %}
```

---

## Product merchandising — Add a gift card recipient form

> Fonte: https://shopify.dev/docs/storefronts/themes/product-merchandising/gift-cards

Learn how to add a recipient form to your gift card product page.

### Resources

To implement the recipient feature, you'll use the following objects:

* The [`product`](https://shopify.dev/docs/api/liquid/objects#product) object
* The [`form`](https://shopify.dev/docs/api/liquid/objects#form) object
* The [`section`](https://shopify.dev/docs/api/liquid/objects#section) object

### Implementing the recipient form

To support the gift card recipient functionality, you need to complete the following tasks:

* Add a form to collect recipient information
* Add the recipient form to your product form
* Display the recipient properties in the cart

The full implementation varies depending on your theme and what you want the display to look like. You can refer to the following files in Dawn for an example of a complete solution:

* [Gift card recipient form](https://github.com/Shopify/dawn/blob/1f794f509903e3e333a808b0b108b4e35ef683d1/snippets/gift-card-recipient-form.liquid)
* [Buy buttons](https://github.com/Shopify/dawn/blob/1f794f509903e3e333a808b0b108b4e35ef683d1/snippets/buy-buttons.liquid#L59), which is rendered in the product form
* [JS](https://github.com/Shopify/dawn/blob/1f794f509903e3e333a808b0b108b4e35ef683d1/assets/recipient-form.js)
* [CSS](https://github.com/Shopify/dawn/blob/1f794f509903e3e333a808b0b108b4e35ef683d1/assets/section-main-product.css#L1471)

### Create a form to collect recipient information

The recipient information is added to your gift card using [line item properties](https://shopify.dev/docs/storefronts/themes/architecture/templates/product#line-item-properties).

Inside your recipient form, you can use the following line item property names:

* `Recipient email`: The email address that the gift card will be sent to.
* `Recipient name`: Optional. The name that the gift card will be addressed to.
* `Message`: Optional. A message that can be included in the gift card email.
* `Send on`: Optional. The date that's used to schedule sending a gift card. The date uses [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601), with an expected format of `yyyy-mm-dd`. If you don't specify a date, then the gift card is sent immediately.
* `__shopify_send_gift_card_to_recipient`: A property that needs to be included with the value `true` to validate and process recipient information.
* `__shopify_offset`: Optional. The customer's timezone offset in minutes, used to schedule the `Send on` date relative to the recipient's local timezone. This value should be set to the output of JavaScript's `new Date().getTimezoneOffset()`. If not provided, the shop's timezone is used instead.

You can refer to the [gift card recipient form](https://github.com/Shopify/dawn/blob/1f794f509903e3e333a808b0b108b4e35ef683d1/snippets/gift-card-recipient-form.liquid) in Dawn for a complete example of the properties in context.

**Tip:** Your form should surface errors returned by the form submission to allow the customer to fix any issues with their form input.

### Add the recipient form to your product form

You need to include the recipient form that you created in your [`product`](https://shopify.dev/docs/api/liquid/tags/form#form-product) form, so that it renders on the gift card product page. The example implementation in Dawn requires you to pass in a [product object](https://shopify.dev/docs/api/liquid/objects#product), [`form`](https://shopify.dev/docs/api/liquid/objects#form) object, and [`section`](https://shopify.dev/docs/api/liquid/objects#section) object.

```liquid
{% form 'product' %}
     <!-- form content -->


     {%- if product.gift_card? -%}
          {%- render 'gift-card-recipient-form', product: product, form: form, section: section -%}
     {%- endif -%}


     <!-- buy buttons -->
{% endform %}
```

**Note:** The recipient form validation doesn't support [accelerated checkout buttons](https://help.shopify.com/manual/online-store/accelerated-checkout). The form should be used only with the **Add to Cart** button.

### Displaying the recipient properties in the cart

To learn about displaying any line item properties that are collected in the cart, refer to the cart template for [line item properties](https://shopify.dev/docs/storefronts/themes/architecture/templates/cart#display-line-item-properties).

### Limitations

* The gift card recipient name can't be longer than 255 characters.
* The gift card message can't be longer than 200 characters.
* You can only schedule a gift card to be sent up to 90 days in the future.

---

## Product merchandising — Bundles grouped view emails

> Fonte: https://shopify.dev/docs/storefronts/themes/product-merchandising/bundles-emails

Shopify's transactional emails, such as order confirmations and shipping updates, can display Bundles in a grouped view. Prior to this update Shopify used flat views to display all order line items as a linear list, while a grouped view nests items under their bundle parent. As a transactional email Partner, you can implement this view using the [GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql).

For example, in the following image, a bundle of products is left ungrouped in an order confirmation email; in a subsequent image, the products in a Bundle are presented in a grouped view.

### Step 1: Querying for the `lineItemsGroup` data

Whether you're displaying Bundles as a grouped view or as a flat view, you'll first need to query the `lineItems` on your `order`. The following query leverages [`order`](https://shopify.dev/docs/api/admin-graphql/unstable/queries/order) and is kept simple for demonstration purposes, add additional fields as needed for your purposes.

**Tip:** The following example is limited to the price after any discounts are applied. You could optionally retrieve and later calculate the price before discounts and total discounts.

#### POST https://{shop}.myshopify.com/api/{api_version}/graphql.json

##### GraphQL query

```graphql
query GetOrder {
  order(id: "gid://shopify/Order/1") {
    lineItems(first: 100) {
      nodes {
        title
        quantity
        discountedTotalSet {
          shopMoney {
            amount
            currencyCode
          }
        }
        lineItemGroup {
          id
          title
          quantity
        }
      }
    }
  }
}
```

##### JSON response

```json
{
  "data": {
    "order": {
      "lineItems": {
        "nodes": [
          {
            "title": "Short Sleeve T-Shirt - Green",
            "quantity": 1,
            "discountedTotalSet": {
              "shopMoney": {
                "amount": "22.0",
                "currencyCode": "USD"
              }
            },
            "lineItemGroup": {
              "id": "gid://shopify/LineItemGroup/1",
              "title": "Green Shirt and Shorts Bundle",
              "quantity": 1
            }
          },
          {
            "title": "Shorts - Green",
            "quantity": 1,
            "discountedTotalSet": {
              "shopMoney": {
                "amount": "0.0",
                "currencyCode": "USD"
              }
            },
            "lineItemGroup": {
              "id": "gid://shopify/LineItemGroup/1",
              "title": "Green Shirt and Shorts Bundle",
              "quantity": 1
            }
          },
          {
            "title": "Sneakers",
            "quantity": 1,
            "discountedTotalSet": {
              "shopMoney": {
                "amount": "100.0",
                "currencyCode": "USD"
              }
            },
            "lineItemGroup": null
          }
        ]
      }
    }
  }
}
```

**Note:** At this point you have all the data needed to display Bundles as a flat view. When displaying line items you'll note which products are part of a bundle.

The relevant fields we're requesting are:

* `title`: The title of the line item, potentially a Bundle component
* `quantity`: The quantity of the line item
* `discountedTotalSet.shopMoney.amount`: The total price of the line item after any discounts
* `discountedTotalsSet.shopMoney.currencyCode`: The currency code of the total price
* `lineItemGroup`: The Bundle parent of the line item, if it exists
  * `id`: The unique identifier of the `lineItemGroup`
  * `title`: The title of the Bundle parent product
  * `quantity`: The quantity of the Bundle parent product

### Step 2: Grouping Bundles

After you've retrieved `lineItemGroup` data, you'll group the Bundle components under the parent product to make it easier to present them as a grouped view.

Any product with a `null` `lineItemGroup` field is not part of a Bundle and should be displayed as a standalone product.

```javascript
function groupBundles(response) {
  const lineItems = response.data.order.lineItems.nodes;
  const bundles = new Map();
  const result = [];


  // First pass: Identify bundles and group items by productId
  lineItems.forEach((item) => {
    if (item.lineItemGroup) {
      const { id, title } = item.lineItemGroup;
      if (!bundles.has(id)) {
        bundles.set(id, {
          bundleTitle: title,
          quantity: item.quantity,
          components: [],
        });
      }


      bundles.get(id).components.push({
        title: item.title,
        quantity: item.quantity,
        price: item.discountedTotalSet.shopMoney.amount,
      });
    } else {
      // Non-bundle items would be handled here
      result.push(item);
    }
  });


  // Convert bundles map to array format
  bundles.forEach((bundle) => {
    result.unshift({
      title: bundle.bundleTitle,
      quantity: bundle.quantity,
      components: bundle.components,
      lineItemGroup: {
        title: bundle.bundleTitle,
      },
    });
  });


  return result;
}
```

Passing in our above result to this function, results in a data structure that looks like this:

```javascript
const result = [
  {
    "title": "Green Shirt and Shorts Bundle",
    "quantity": 1,
    "components": [
      {
        "title": "Short Sleeve T-Shirt - Green",
        "quantity": 1,
        "price": "22.0"
      },
      {
        "title": "Shorts - Green",
        "quantity": 1,
        "price": "0.0"
      },
    ],
    lineItemGroup: { title: 'Green Shirt and Shorts Bundle' }
  },
  {
    "title": "Sneakers",
    "quantity": 1,
    "discountedTotalSet": {
      "shopMoney": {
        "amount": "100.0",
        "currencyCode": "USD"
      }
    },
    "lineItemGroup": null
  }
]
```

With this data you can display your Bundles as a grouped view in your transactional emails.

### Step 3: Calculating the bundle price

The last thing you'll need to do is calculate the total price of a bundle if you want to display it. This is a simple sum of the prices of the components.

```javascript
function calculateBundlePrice(bundle) {
  return bundle.components.reduce((acc, component) => {
    return acc + parseFloat(component.price);
  }, 0);
}


calculateBundlePrice(result[0]); // 22.0
```

By passing in each bundle object, the above will total up the price of all the components in the bundle. You'll need to modify this depending on the fields you queried. For example, if you queried `discountedTotalSet`, you'll get the total discounted price of the line item accounting for any quantity. If instead you used `discountedUnitPriceSet`, you'd get the discounted price per unit and will need to account for price and quantity in your calculation.

---

## Pricing and payments — Overview

> Fonte: https://shopify.dev/docs/storefronts/themes/pricing-payments

Being able to clearly see pricing and discounts, as well as payment options, are important factors for customers making purchases from a merchant's store.

Some merchants might sell products in specific quantities or measurements, or as part of a selling plan. To support this, Shopify provides merchants the option to set up unit pricing, as well as Subscriptions and Pre-orders and Try before you buy.

To help make the payment process easier, Shopify integrates with payment providers that can offer accelerated checkouts, and some merchants can utilize Shop Pay to allow customers to pay in installments.

---

## Pricing and payments — Discounts

> Fonte: https://shopify.dev/docs/storefronts/themes/pricing-payments/discounts

Discounts can be applied at the line item level, or the cart, checkout, or order level. This means that they apply directly to specific line items, or apply to the cart or order as a whole. Discounts can be applied in the following ways:

* [As automatic discounts](https://help.shopify.com/manual/discounts/automatic-discounts)
* [Using manual discount codes](https://help.shopify.com/manual/discounts/managing-discount-codes)
* [Using Shopify Scripts](https://help.shopify.com/manual/checkout-settings/script-editor)

**Deprecated:** **Shopify Scripts will be sunset on June 30, 2026.** All existing Shopify Scripts will stop functioning after this date. Migrate your scripts to [Shopify Functions](https://shopify.dev/docs/api/functions) before the deadline to avoid disruption to your store's checkout, shipping, and payment customizations.

In this tutorial, you'll learn how to display discounts in your theme.

### Requirements

You've created a [cart template](https://shopify.dev/docs/storefronts/themes/architecture/templates/cart).

### Resources

To display discounts in your theme, you'll use the following:

* The `discount_application` object
* The `discount_allocation` object
* The `line_item` object

#### The `discount_application` object

The [`discount_application`](https://shopify.dev/docs/api/liquid/objects/discount#discount-application) object registers discounts at the cart, checkout, or order level. Depending on where you're implementing your discount display, you'll access the relevant discount applications through the associated parent object:

* For the [cart](https://shopify.dev/docs/storefronts/themes/architecture/templates/cart) template:
  * [`cart.discount_applications`](https://shopify.dev/docs/api/liquid/objects/cart#cart-discount_applications)
  * [`cart.cart_level_discount_applications`](https://shopify.dev/docs/api/liquid/objects/cart#cart-cart_level_discount_applications)

**Note:** Manual discount codes can only be applied at the checkout, so they're not available through `cart.discount_applications`.

#### The `discount_allocation` object

The [`discount_allocation`](https://shopify.dev/docs/api/liquid/objects/discount#discount-allocation) object associates a `discount_application` with a line item.

You can access an array of all of the discount allocations associated with a line item using [`line_item.line_level_discount_allocations`](https://shopify.dev/docs/api/liquid/objects/line_item#line_item-discount_allocations).

#### The `line_item` object

To complete the price display, you need to use price and discount attributes of the [`line_item`](https://shopify.dev/docs/api/liquid/objects/line_item) object, including:

* [`original_price`](https://shopify.dev/docs/api/liquid/objects/line_item#line_item-original_price)
* [`original_line_price`](https://shopify.dev/docs/api/liquid/objects/line_item#line_item-original_line_price)
* [`final_price`](https://shopify.dev/docs/api/liquid/objects/line_item#line_item-final_price)
* [`final_line_price`](https://shopify.dev/docs/api/liquid/objects/line_item#line_item-final_line_price)
* [`line_level_total_discount`](https://shopify.dev/docs/api/liquid/objects/line_item#line_item-line_level_total_discount)

### Implementing discount displays

Because discounts can apply to line items or to the cart or order as a whole, you should display discount information in two places:

* With individual line items
* With the total summary

The examples in this tutorial use the [cart template](https://shopify.dev/docs/storefronts/themes/architecture/templates/cart). You can implement the components directly in a Liquid template, or in a section in a JSON template.

### Line item discounts

If a discount applies to specific line items, then it should be displayed with those items. To display discounts with line items, you need to include the following in your display:

* The line item price
* The line item discount

#### Line item price

If a discount has been applied to a line item, then you should show the original price with a strikethrough, as well as the new discounted price. Each of these can be accessed with the following attributes of the Liquid [`line_item` object](https://shopify.dev/docs/api/liquid/objects/line_item):

* [`original_price`](https://shopify.dev/docs/api/liquid/objects/line_item#line_item-original_price)
* [`original_line_price`](https://shopify.dev/docs/api/liquid/objects/line_item#line_item-original_line_price)
* [`final_price`](https://shopify.dev/docs/api/liquid/objects/line_item#line_item-final_price)
* [`final_line_price`](https://shopify.dev/docs/api/liquid/objects/line_item#line_item-final_line_price)

#### Line item discounts

If a discount has been applied to a line item, then you should show each discount that's applied, with its associated discount amount, or a total discount amount. Line item-specific discounts can be accessed through the [`line_level_discount_allocations`](https://shopify.dev/docs/api/liquid/objects/line_item#line_item-line_level_discount_allocations) attribute of the Liquid [`line_item` object](https://shopify.dev/docs/api/liquid/objects/line_item), and the total line item discount can be accessed through the [`line_level_total_discount`](https://shopify.dev/docs/api/liquid/objects/line_item#line_item-line_level_total_discount) attribute.

#### Example

The following is an example that outputs the price and discounts display:

```liquid
{% for line_item in cart.items %}
  <!-- line item info -->

  {% if line_item.original_price > line_item.final_price %}
    <s>{{ line_item.original_price | money }}</s>
  {% endif %}

  {{ line_item.final_price | money }})

  {% if line_item.line_level_discount_allocations.size > 0 %}
    Discounts:
    <ul>
      {% for discount_allocation in line_item.line_level_discount_allocations %}
        <li>
          {{ discount_allocation.discount_application.title }}-{{ discount_allocation.amount | money }}
        </li>
      {% endfor %}
    </ul>
  {% endif %}
{% endfor %}
```

**Tip:** For another example of displaying line item discounts, you can refer to [Dawn's implementation](https://github.com/Shopify/dawn/blob/main/sections/main-cart-items.liquid).

### Cart discounts

The subtotal is the line item total after line item discounts have applied, and the total is the cart total after cart discounts have applied. If a discount applies to the cart as a whole, then it should display between the subtotal and total.

Cart-level discounts can be accessed through the `cart_level_discount_applications` attribute of the [`cart`](https://shopify.dev/docs/api/liquid/objects/cart#cart-cart_level_discount_applications) or [`order`](https://shopify.dev/docs/api/liquid/objects/order#order-cart_level_discount_applications) object.

#### Example

```liquid
Subtotal: {{ cart.items_subtotal_price | money }}

{% if cart.cart_level_discount_applications.size > 0 %}
  Discounts:

  <ul>
    {% for discount_application in cart.cart_level_discount_applications %}
      <li>
        {{ discount_application.title }}-{{ discount_application.total_allocated_amount | money }}
      </li>
    {% endfor %}
  </ul>
{% endif %}

Total: {{ cart.total_price | money }}
```

**Tip:** For another example of displaying cart discounts, you can refer to [Dawn's implementation](https://github.com/Shopify/dawn/blob/main/sections/main-cart-footer.liquid).

---

## Pricing and payments — Unit pricing

> Fonte: https://shopify.dev/docs/storefronts/themes/pricing-payments/unit-pricing

If a merchant sells products in specific quantities or measurements, they might need to display a price per unit for those products. For example, if a product is sold in weights of 500g, 1kg, and 1.5kg, a merchant might want to show the price per 100g for each variant.

In this tutorial, you'll learn how to display unit prices for product variants.

> **Tip:** Unit prices can be added to products through the Shopify admin.

### Resources

To display unit prices in your theme, you'll use the following:

* The `unit_price` property on the [`line_item`](https://shopify.dev/docs/api/liquid/objects/line_item#line_item-unit_price) or [`variant`](https://shopify.dev/docs/api/liquid/objects/variant#variant-unit_price) objects
* The [`unit_price_measurement`](https://shopify.dev/docs/api/liquid/objects/unit_price_measurement) object

Depending on where you're implementing your unit price display, you'll access unit price information through the associated parent object:

| Context | Example template types | Parent object |
| - | - | - |
| Variants that have been added to a cart or are part of an order | [cart](https://shopify.dev/docs/storefronts/themes/architecture/templates/cart) | [line_item](https://shopify.dev/docs/api/liquid/objects/line_item) |
| Product and variant listings | [product](https://shopify.dev/docs/storefronts/themes/architecture/templates/product) ; [collection](https://shopify.dev/docs/storefronts/themes/architecture/templates/collection) | [variant](https://shopify.dev/docs/api/liquid/objects/variant) |

### Implementing unit price displays

You should add support for unit prices wherever you have a price display. Common locations include:

* The collection template
* The product template
* The cart template

You can include this code in the relevant template or a section in the template.

Your code should do the following:

1. Check whether the variant or line item has a unit price measurement using [`variant.unit_price_measurement`](https://shopify.dev/docs/api/liquid/objects/variant#variant-unit_price_measurement) or [`line_item.unit_price_measurement`](https://shopify.dev/docs/api/liquid/objects/line_item#line_item-unit_price_measurement).
2. If the variant or line item uses a unit price measurement, then use the [`unit_price_with_measurement` filter](https://shopify.dev/docs/api/liquid/filters/unit_price_with_measurement) to display the unit price based on the store's **HTML without currency** setting.

#### Example

##### variant

```liquid
{% if variant.unit_price_measurement %}
  {{ variant.unit_price | unit_price_with_measurement: variant.unit_price_measurement }}
{% endif %}
```

##### line_item

```liquid
{% if line_item.unit_price_measurement %}
  {{ line_item.unit_price | unit_price_with_measurement: line_item.unit_price_measurement }}
{% endif %}
```

3. Use [money filters](https://shopify.dev/docs/api/liquid/filters/payment_button#money-filters) combined with the [`unit_price_with_measurement` filter](https://shopify.dev/docs/api/liquid/filters/unit_price_with_measurement) to display the unit price with a different money format.

#### Example

##### variant

```liquid
{% if variant.unit_price_measurement %}
  {{ variant.unit_price | money_with_currency | unit_price_with_measurement: variant.unit_price_measurement }}
{% endif %}
```

##### line_item

```liquid
{% if line_item.unit_price_measurement %}
  {{ line_item.unit_price | money_with_currency | unit_price_with_measurement: line_item.unit_price_measurement }}
{% endif %}
```

---

## Pricing and payments — Subscriptions (overview)

> Fonte: https://shopify.dev/docs/storefronts/themes/pricing-payments/subscriptions

Users can offer various purchasing options through subscription apps at checkout. For instance, customers might subscribe to monthly product deliveries at a 10% discount or weekly deliveries at 20% off.

**Tip:** Merchants must satisfy the [qualifying criteria](https://help.shopify.com/en/manual/products/purchase-options/subscriptions/setup#eligibility-requirements) to use Shopify subscriptions.

### How it works

Apps establish [selling plan groups](https://shopify.dev/docs/api/liquid/objects/selling_plan_group), which contain [selling plans](https://shopify.dev/docs/api/liquid/objects/selling_plan) linked to products and variants. A "Subscribe & Save" group might offer plans letting customers select delivery and billing frequencies independently. Merchants can present multiple optional plans or mandate a required plan, such as "subscription-only" offerings.

### Implementing subscriptions in a theme

Integration uses Liquid and JavaScript. Developers should consult UX guidelines for optimal user experiences.

#### Related resources

- [Add subscriptions to your theme](https://shopify.dev/docs/storefronts/themes/pricing-payments/subscriptions/add-subscriptions-to-your-theme) — Learn integration techniques for your theme
- [Subscriptions UX guidelines](https://shopify.dev/docs/storefronts/themes/pricing-payments/subscriptions/subscription-ux-guidelines) — Build subscription experiences and style components

---

## Pricing and payments — Add subscriptions to your theme

> Fonte: https://shopify.dev/docs/storefronts/themes/pricing-payments/subscriptions/add-subscriptions-to-your-theme

In this tutorial, you'll learn the basics of how to support subscriptions in your theme.

**Tip:** Refer to [Subscription UX guidelines](https://shopify.dev/docs/storefronts/themes/pricing-payments/subscriptions/subscription-ux-guidelines) to review user experience considerations that might impact your implementation.

### Requirements

* Add a [product form](https://shopify.dev/docs/api/liquid/tags/form#form-product) to a template. A product form can be added to any template that can access the [`product`](https://shopify.dev/docs/api/liquid/objects/product) object.

### Resources

To support subscriptions in your theme, you'll use the following resources:

* The [`form`](https://shopify.dev/docs/api/liquid/objects/form) object.
* Objects and object properties that represent selling plan information, including the following:
  * [`selling_plan_group`](https://shopify.dev/docs/api/liquid/objects/selling_plan_group): A group of selling plans that are available for the product's variants.
  * [`selling_plan`](https://shopify.dev/docs/api/liquid/objects/selling_plan): The details of the selling plan.
  * [`selling_plan_allocation`](https://shopify.dev/docs/api/liquid/objects/selling_plan_allocation): Information about how a particular selling plan affects a line item.
  * [`variant.requires_selling_plan`](https://shopify.dev/docs/api/liquid/objects/variant#variant-requires_selling_plan).
* The [`/{locale}/cart/change.js` endpoint](https://shopify.dev/docs/api/ajax/reference/cart#post-locale-cart-change-js) of the Cart AJAX API.

Depending on where you're implementing your selling plan functionality, you'll access selling plan information through the following parent objects:

| Context | Example template types | Parent object |
| - | - | - |
| Product and variant listings | [product](https://shopify.dev/docs/storefronts/themes/architecture/templates/product) | [variant](https://shopify.dev/docs/api/liquid/objects/variant) |
| Variants that have been added to a cart or are part of an order | [cart](https://shopify.dev/docs/storefronts/themes/architecture/templates/cart) | [line_item](https://shopify.dev/docs/api/liquid/objects/line_item) |

For more information about how to present each of these objects and their attributes, refer to [Subscription UX guidelines](https://shopify.dev/docs/storefronts/themes/pricing-payments/subscriptions/subscription-ux-guidelines).

### Implementing subscription displays

To support subscriptions in your theme, you need to implement the following components:

* **A selling plan selector on the product page**: This selector enables customers to select a selling plan.
* **JavaScript to update the selling plan**: Use JavaScript to update the available selling plans when variants are selected, and update the hidden selling plan input as selling plan options are selected.
* **A selling plan display in the cart**: Indicate to customers when a selling plan has been applied to a line item. You can also implement a selling plan selector to give the option to add a new selling plan, or to remove or edit the current selling plan.
* **A checkout charge in the cart**: Display a checkout charge that represents the amount that customers need to pay during checkout.
* **A selling plan display on the customer order pages**: Indicate to customers when a selling plan has been applied to a line item.

### The selling plan selector on the product page

You can add a selling plan selector for products wherever you can access the [product form](https://shopify.dev/docs/api/liquid/tags/form#form-product). For example, you might add a selling plan selector to the [product template](https://shopify.dev/docs/storefronts/themes/architecture/templates/product) or a section in the template.

Selling plan groups and individual selling plans have a similar structure to products and variants. You can view selling plan groups like products, where there are multiple options that comprise an individual selling plan, similar to variant options that comprise an individual variant.

You can access the available selling plan options through the `selling_plan_groups` attribute of the [product](https://shopify.dev/docs/api/liquid/objects/product#product-selling_plan_groups).

Add the following to your product form:

* For each [selling_plan_group](https://shopify.dev/docs/api/liquid/objects/selling_plan_group), output each of its options inside the product form.
* To track the ID of the selected selling plan, add an input with an attribute of `name="selling_plan"`. The value should be the ID of the selected selling plan. If there's no selected selling plan, then the value should be empty.
* Save the product object so that it can be accessed in JavaScript.

#### Example

The following example is showing an example on how you can show the selling plan group in your product form. Make sure to add the code inside your product form. The example is referring to the file `selling-plans-integration.js`, this file is covered on the JavaScript section. The following code is doing the following:

* Assign the product and the current variant to be used inside the integration
* Loop through every selling plan group, and display each associated selling plan
* When the product is only sold as a subscription, we do not allow the buyer to buy the product as a one time purchase
* Add a Subscription badge to be displayed next to the product price when a buyer selects a subscription

**Note:** This example demonstrates how to integrate selling plans into your theme. We recommend customizing this integration to suit your specific needs. The following code can also be used as a [theme app block](https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks).

##### /assets/selling-plans-integration.liquid

```liquid
{%- assign current_variant = product.selected_or_first_available_variant | default: product.variants.first -%}


{% if product.selling_plan_groups.size > 0 %}
  <div class="selling_plan_app_container" data-section-id='{{ section.id }}'>
    <script src="{{ 'selling-plans-integration.js' | asset_url }}" defer></script>
    <style>.selling_plan_theme_integration--hidden {display: none;}</style>
    {% for variant in product.variants %}
      {%liquid
        assign variantPrice = variant.price | money_with_currency | escape
        assign variantComparedAtPrice = variant.compare_at_price | money_with_currency | escape
      %}
      {% if variant.selling_plan_allocations.size > 0 %}
        <section data-variant-id='{{ variant.id }}' class='selling_plan_theme_integration {% if variant.id != current_variant.id %}selling_plan_theme_integration--hidden{% endif %}'>
          <fieldset>
            <legend>
              {{ block.settings.supporting_text_title }}
            </legend>
            <div>
              {% unless product.requires_selling_plan %}
                <div>
                  <label>
                    <input
                      aria-label='One-time purchase. Product price {{ variantPrice }}'
                      type='radio'
                      name="purchaseOption_{{ section.id }}_{{ variant.id }}"
                      {% if variant.available == false %}disabled{% endif %}
                      id='{{ section.id }}_one_time_purchase'
                      data-radio-type='one_time_purchase'
                      data-variant-id='{{ variant.id }}'
                      data-variant-price='{{ variantPrice }}'
                      data-variant-compare-at-price='{{ variantComparedAtPrice }}'
                      checked
                    />
                    One-time purchase
                  </label>
                </div>
              {% endunless %}
              {% assign group_ids = variant.selling_plan_allocations | map: 'selling_plan_group_id' | uniq %}
              {% for group_id in group_ids %}
                {%liquid
                   assign group = product | map: 'selling_plan_groups' | where: 'id', group_id | first
                   assign allocations = variant | map: 'selling_plan_allocations' | where: 'selling_plan_group_id', group_id


                   if forloop.first
                    assign first_selling_plan_group = true
                  else
                    assign first_selling_plan_group = false
                  endif
                %}
                <div>
                  <div>
                    <label>{{ group.name }}</label>
                  </div>
                  <ul>
                    {% for allocation in allocations %}


                      {%liquid
                        if forloop.first and product.requires_selling_plan and first_selling_plan_group
                          assign plan_checked = 'checked'
                        else
                          assign plan_checked = nil
                        endif


                        assign allocationPrice = allocation.price | money_with_currency | escape
                        assign allocationComparedAtPrice = allocation.compare_at_price | money_with_currency | escape
                      %}


                      <li>
                        <label>
                          <input
                            type='radio'
                            {% if variant.available == false %}disabled{% endif %}
                            aria-label='{{ allocation.selling_plan.name }}. Product price {{ allocationPrice }}'
                            name="purchaseOption_{{ section.id }}_{{ variant.id }}"
                            data-radio-type='selling_plan'
                            data-selling-plan-id='{{ allocation.selling_plan.id }}'
                            data-selling-plan-group-id='{{ section.id }}_{{ group_id }}_{{ variant.id }}'
                            data-selling-plan-adjustment='{{ allocation.selling_plan.price_adjustments.size }}'
                            data-variant-price='{{ allocationPrice }}'
                            data-variant-compare-at-price='{{ allocationComparedAtPrice }}'
                            {{ plan_checked }} />
                          {{ allocation.selling_plan.name }}
                        </label>
                      </li>
                    {% endfor %}
                  </ul>
                </div>
              {% endfor %}
            </div>
          </fieldset>
        </section>
      {% endif %}
    {% endfor %}
  </div>
  <input
    name='selling_plan'
    class='selected-selling-plan-id'
    type='hidden' />
{% endif %}
```

### JavaScript to update selling plan information

JavaScript is used to interact with the theme integration. This will make it possible for a buyer to select a product and add the correct subscription to their cart. You can create a separate file named `selling-plans-integration.js` inside the `Assets` folder of your theme. The following example illustrates how JavaScript can interact with the selling plan liquid integration:

##### /assets/selling-plans-integration.js

```js
const hiddenClass = 'selling_plan_theme_integration--hidden';


class SellingPlansWidget {
  constructor(sellingPlansWidgetContainer) {
    this.enablePerformanceObserver();
    this.sellingPlansWidgetContainer = sellingPlansWidgetContainer;
    this.appendSellingPlanInputs();
    this.updateSellingPlanInputsValues();
    this.listenToVariantChange();
    this.listenToSellingPlanFormRadioButtonChange();
    this.updatePrice();
  }


  get sectionId() {
    return this.sellingPlansWidgetContainer.getAttribute('data-section-id');
  }


  get shopifySection() {
    return document.querySelector(`#shopify-section-${this.sectionId}`);
  }


  /*
    We are careful to target the correct form, as there are instances when we encounter an installment form that we specifically aim to avoid interacting with.
  */
  get variantIdInput() {
    return (
      this.addToCartForms[1]?.querySelector(`input[name="id"]`) ||
      this.addToCartForms[1]?.querySelector(`select[name="id"]`) ||
      this.addToCartForms[0].querySelector(`input[name="id"]`) ||
      this.addToCartForms[0].querySelector(`select[name="id"]`)
    );
  }


  get priceElement() {
    return this.shopifySection.querySelector('.price');
  }
}
```

* The functions `listenToVariantChange()` and `listenToAddToCartForms()` are implemented to track when a product variant is altered or when the product form is updated. The identification of the variant is crucial as it dictates which selling plan box should be displayed. For more information about how to find a variant, refer to our [community post](https://community.shopify.com/c/shopify-apps/subscription-1p-app-block/td-p/2415591).

### The selling plan display in the cart

If a customer selects a selling plan on the product page, then they should see that selection in the cart.

Available selected selling plans are accessible through the `selling_plan_allocation` attribute of the [`line_item` object](https://shopify.dev/docs/api/liquid/objects/line_item). The following is an example:

##### /customers/order.liquid

```liquid
{% if line_item.selling_plan_allocation %}
  <p class="selling-plan">{{ line_item.selling_plan_allocation.selling_plan.name }}</p>
{% endif %}
```

#### The selling plan selector

Rather than just display the selected selling plan, you can give customers the option to add a new selling plan, or to remove or edit the current selling plan. To do this, you should implement a selling plan selector that lists out the available selling plans for the line item's variant, and reflects the currently selected selling plan.

You can loop through the `selling_plan_allocations` attribute of the [`variant`](https://shopify.dev/docs/api/liquid/objects/variant#variant-selling_plan_allocations) object associated with the line item (`line_item.variant`) to build out your selector options. You can compare the selected selling plan ID with the ID of the selling plan at the current index of the loop to make sure that the selector reflects the currently selected selling plan.

To change the selling plan for a line item, you can use the [`/{locale}/cart/change.js`](https://shopify.dev/docs/api/ajax/reference/cart#post-locale-cart-change-js) endpoint of the Cart AJAX API.

##### Example

The following example outputs a selling plan selector:

```liquid
<select name="selling-plan" data-line="{{ forloop.index }}" data-quantity="{{ line_item.quantity }}">
  <option value="">One-time purchase</option>


  {% for selling_plan_allocation in line_item.variant.selling_plan_allocations %}
    <option
      value="{{ selling_plan_allocation.selling_plan.id }}"
      {% if line_item.selling_plan_allocation.selling_plan.id == selling_plan_allocation.selling_plan.id %}selected="selected"{% endif %}
    >
      {{ selling_plan_allocation.selling_plan.name }}
    </option>
  {% endfor %}
</select>
```

The following example illustrates the concept of watching for a change in the selling plan selector and applying those changes through the `/cart/change.js` endpoint. It isn't completely functional.

```js
const sellingPlanSelectors = document.querySelectorAll('[name="selling-plan"]');


sellingPlanSelectors.forEach(function(element) {
  element.addEventListener('change', function(event) {
    const data = {
      'line': event.target.dataset.line,
      'quantity': event.target.dataset.quantity,
      'id': event.target.value
    }


    fetch('/cart/change.js', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
    .then(response => {
      // Refresh page, or re-render cart
      console.log(response);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  });
});
```

### The checkout charge display in the cart

Because pre-order and TBYB can change how much a customer has to pay up front, you should show them how much they'll be charged at checkout. You can calculate this amount using [`selling_plan.checkout_charge`](https://shopify.dev/docs/api/liquid/objects/selling_plan#selling_plan-checkout_charge) object.

You can access a line item's checkout charge through its [`selling_plan_allocation`](https://shopify.dev/docs/api/liquid/objects/selling_plan_allocation).

The following table outlines the types of checkout charges:

| Checkout charge type | Description |
| - | - |
| `percentage` | A percent value representing the percentage amount of the full price that must be paid up front. |
| `price` | The price to be paid up front, in cents. |

**Note:** You can't configure checkout charges for subscriptions. Because of this, subscriptions always have a `value_type` of `percentage` and `value` of 100.

#### Example

The following example outputs the appropriate line item price depending on whether the line item has a selling plan allocation, and what kind of selling plan it is.

```liquid
{% if item.selling_plan_allocation %}
  {%- assign checkout_charge = item.selling_plan_allocation.selling_plan.checkout_charge -%}


  {% if checkout_charge.value_type == 'percentage' %}
    {{ item.original_price | times: checkout_charge.value | divided_by: 100 | money }}
  {% else %}
    {{ checkout_charge.value | money }}
  {% endif %}
{% else %}
  {{ item.original_price | money }}
{% endif %}
```

### Customer order selling plan display

When a customer selects a selling plan, they should see the name of that selection on the customer order page.

The selected selling plan, if there is one, is accessible through the `selling_plan_allocation` attribute of the [`line_item` object](https://shopify.dev/docs/api/liquid/objects/line_item). The following is an example:

##### /customers/order.liquid

```liquid
{% if line_item.selling_plan_allocation %}
  <p class="selling-plan">{{ line_item.selling_plan_allocation.selling_plan.name }}</p>
{% endif %}
```

---

## Pricing and payments — Subscription UX guidelines

> Fonte: https://shopify.dev/docs/storefronts/themes/pricing-payments/subscriptions/subscription-ux-guidelines

A great customer-facing user experience (UX) for purchasing a subscription is important to the success of our merchants. This guide explains the key principles of subscription needs and component-level guidelines for implementing subscription user interfaces (UIs).

**Note:** In order to be eligible for Built for Shopify status, subscription apps must adhere to the [subscription app Built for Shopify design requirements](https://shopify.dev/docs/apps/design/user-experience/subscription-apps).

### User experience principles

To provide a good experience when purchasing subscriptions and gain trust from customers, make sure to implement the following UX principles:

* **Create a visible hierarchy**: Customers should be able to clearly identify the savings of a subscription plan, the selling plan options, and the terms and conditions.
* **Disclose information progressively and logically**: Customers should have a sense of progression in subscription selection as their decisions clearly influence subsequent choices. Adapt the information shown in the customer flow to communicate subscriptions clearly and concisely.
* **Provide a seamless integration**: The subscriptions UI should be integrated into the theme's existing design system.
* **Work with merchants' existing workflows**: Shopify provides the tooling for apps to build subscription experiences. Subscription experiences can be accessed directly from the Shopify admin. This allows merchants to access your app from the surface areas they are familiar with.
* **If a resource exists in Shopify, don't duplicate it in your app**: Shopify-managed resources such as customers, discounts, and products should be managed in a single place to reduce complex workflows and duplication.

### User interface guidelines

Before you integrate your subscription app into a theme, familiarize yourself with the UI guidelines and best practices that are associated with each component.

Apps should consider how subscription products appear in multiple places on the online store, such as product pages, collection pages, search results, featured product sections on the home page, and quick view modals on product cards. Surfacing potential subscription savings and pricing in these areas can further encourage customers to subscribe.

Subscription information is displayed in the following components of the online store:

* Product forms
* Cart items
* Order details

The following sections include guidance for displaying prices, styling subscription UI components, and presenting multiple subscriptions. In each section, the relevant [Liquid](https://shopify.dev/docs/api/liquid) properties needed to create each component are also referenced.

### Product forms

The product form allows a customer to select their subscription. This is where the merchant can provide clarity and more details for a product and its available variants. Product forms are used in product pages, featured product sections on home pages, and quick view modals on product cards.

The subcomponents of a product form include the following:

* A. Price
* B. Selling plan selection
* C. Selling plan details
* D. Main call-to-action

#### Price

Customers should be able to clearly identify the price of a subscription.

| # | UI element | Liquid properties and information | UI guidelines |
| - | - | - | - |
| 1 | Price | `selling_plan_allocation.price` | Reflect the price details from the selected subscription. |
| 2 | Compare at price | `selling_plan_allocation.compare_at_price` | |
| 3 | Per delivery price | `selling_plan_allocation.per_delivery_price` Displays only when the value is different from `price`. This occurs when the selling plan is a prepaid subscription. | |
| 4 | Unit price | `selling_plan_allocation.unit_price` Unit price values may differ between `sellingPlanAllocations`. Unit measurement information is on the `variant` object, as it does not change based on `sellingPlan`. | |
| 5 | Subscription badge | `selling_plan.recurring_deliveries` The badge shown when the selling plan involves recurring deliveries (subscription). | Provide a contextual subscription badge or label to help differentiate against a one-time subscription. To reduce the clutter on a product page, don't display a badge when the item can only be purchased as a subscription. Rely on other ways to express this detail. |
| 6 | Price adjustment | `selling_plan.price_adjustment` The object includes information on whether the adjustment is price or percentage based. This is used instead of sale price. | Consider adding "subscription savings" details to highlight the subscription's value. For example, "Subscription - Save $3.00" or "Subscription - Save 10%". For subscriptions with a pricing policy that changes over time, express the largest savings. For example, "Save up to 30%". For more information, refer to Communicating changes in price over time. |

#### Pricing patterns

A subscription usually comes with savings to encourage customers to purchase products. Two common patterns for displaying a subscription's pricing information are a main price component and inline pricing. These patterns can be implemented at the same time in a design, but this can be a challenge in situations where you don't have control over the codebase for both the app and the theme.

**Tip:** The inline pricing pattern is useful for subscription apps that integrate into a third-party theme codebase.

Regardless of your approach to displaying prices to customers, the following points should guide your implementation:

* The price of a subscription is clearly visible when a customer has selected a selling plan from a product form.
* For products with [unit pricing](https://help.shopify.com/en/manual/intro-to-shopify/initial-setup/sell-in-germany/price-per-unit), ensure that any change to the unit price from a subscription is displayed.
* If an item is a prepaid item, then display the price per delivery. This enables customers to better compare the price difference between one-time purchases and prepaid items.

##### Main price component

In this approach, there is a main price component on the page that's updated when a customer interacts with a selling plan selector and product variant selection.

To help customers understand the price of products that they purchase, do the following:

* Clearly display the subscription item's price and any applicable savings compared to the price of a one-time purchase.
* Add a subscription badge to the component to help clarify that the savings are conditional to the purchase of a subscription.

##### Inline pricing

In this approach, pricing information is displayed inline or close to the selling plan selection. The price updates in response to changes in selling plan and product variant selection.

This approach makes a strong association between the effects of choosing a selling plan and the price. The positioning of the price is also preferable for mobile shopping, where smaller screen sizes mean that the main price component and price updates might not be in view.

This approach is useful for [subscription apps](https://shopify.dev/docs/apps/build/purchase-options/subscriptions) that integrate into the codebase of third-party themes. Because the pricing information is contained within a selling plan selector that the app controls and injects, this approach can help to avoid conflicts between the app's and the theme's respective scripts.

#### Selling plan selection

Customers should be able to clearly identify their subscription options:

| # | UI element | Liquid properties and information | UI guidelines |
| - | - | - | - |
| 1 | subscriptions label | `product.requires_selling_plan` `product.selling_plan_groups` | One-time subscriptions and selling plan groups are considered different subscriptions. Use the term **subscriptions** in your own designs. |
| 2 | One-time subscription | `product.requires_selling_plan` If the property is `false`, then at least 1 variant can be purchased as a one-time purchase and the one-time subscription should be presented in the UI. | **Group behavior** On the first page load, select the one-time subscription by default. When the customer interacts with the UI, consider collapsing the unselected group to make good usage of space. Disable the selling plan group selection when it isn't available for a given variant. **Group layout** Prioritize displaying subscriptions in a vertically stacked list to make them readable on all devices. When displayed side-by-side, the information can be crowded on smaller screens. **Group style** Consider displaying subscriptions as radio inputs instead of buttons. Buttons can easily compete with the product form's call-to-action (submit button). |
| 3 | Selling plan group name | `selling_plan_group.name` Always make this value visible. For more information, refer to Selling plan group name. | |
| 4 | Inline price | `selling_plan_allocation.per_delivery_price` Using the `per_delivery_price` is a more relevant comparison between prepaid subscriptions and one-time purchases. | Showing the price of selling plans inline makes it easier for customers to compare subscriptions. Show "each" next to the price for both one-time subscriptions and selling plan groups to maintain consistency and clarity among similar text information. For subscriptions with a pricing policy that changes over time, add "from" before the inline pricing to clearly communicate the lowest price of the selling plan group. For example, "from $7.00". For more information, refer to Communicating changes in price over time. |
| 5 | Selling plan option name | `selling_plan_option.name` | Contextualize the type of selling plan option. **Displaying selling plan options** Selling plan option values are often written in a way that assumes that the option name is also visible to the customer. For example: Name: "Delivery every"; Option: "Month"; Option: "Week". Never hide the option names. Certain site designs will hide form labels to make a page look clean, but this can result in the values being presented with no context. |
| 6 | Selling plan option value | `selling_plan_option.value` For more information, refer to Display selling plan option values. | Don't express exact prices in option values, such as "Save $5 a week", because the values won't be accurate if the currency changes. Expressing percentages is possible because they stay consistent even if the currency changes. For more information, refer to Considerations for currency switching and price rounding. |

##### subscriptions label

Show the **subscriptions** label when the following conditions apply:

* A one-time purchase exists and there's at least one `sellingPlanGroups`.
* A one-time purchase isn't an option, but there are multiple `sellingPlanGroups`.

Shopify doesn't show the **subscriptions** label when the following conditions apply:

* There are no selling plan groups.
* The product is subscription-only and there's only 1 selling plan group. In this case, the `sellingPlanGroup`'s name remains in its position, but without the radio input.

##### Subscription-only use case

Keep the selling group name and the inline price within the selector container. This sustains a stronger relationship between subscription selection and `per_delivery_price`, and maintains a consistent approach across different use cases.

##### Selling plan group name

Selling plan names should make clear the benefit of signing up for a subscription. For example, "Subscribe and save 10%". This incentivizes customers to make a bigger commitment in comparison to one-time subscriptions.

Because the [Selling plan API](https://shopify.dev/docs/api/admin-graphql/latest/objects/sellingplan) allows for multiple selling plan groups on a product, selling plan group names are used to differentiate subscriptions.

##### Display selling plan option values

It's required to display all of the option values at a glance from a group. Consider adapting the component layout to optimize readability.

Components should adapt to the number of options being shown. When there are many options to choose from, an appropriate component should be selected to enable customers to view all options easily. Where there is a small number of options, a different component may be used. When possible, apply the appropriate layout to all values within a selling plan group for consistency:

* **4 options or less**: Show each option as a radio button to allow customers to view what's available.
* **More than 4 options**: Use a select dropdown to emphasize the customer's selection and hide other options within the collapsed dropdown.

###### UI update on variant change

A product's variants might not all support the same subscription options. As a customer changes their variant selection, the components should update to make clear which subscription options are available and unavailable.

When a selected option within a selling plan group is unavailable, three events should happen:

* The unavailable options become unselected and require the customer to make a new selection to successfully submit the form.
* The unavailable options for the selected variant are disabled.
* The form submission button is enabled. Disabling the button removes the ability to display an error message and instead displays the product as unavailable, which is false. Let the customer click the button but prevent them from adding the product to the cart. Then, anchor and scroll back to the faulty UI area and display a message that describes why the process can't complete and what the customer needs to do to proceed.

#### Selling plan details

Display important subscription terms and selections to customers. The subscription summary confirms a customer's selections, shows any conditions, and helps build trust in the brand.

| # | UI element | API properties and information | UI guidelines |
| - | - | - | - |
| 1 | Recurring price line | `selling_plan_allocation.price_adjustments` `selling_plan.price_adjustments` The `selling_plan` contains information on how a plan affects product prices, while the `selling_plan_allocation` describes the price for the variant to which the selling plan is applied. | Express the number of payment cycles at the current price, and communicate what the price will be in the future. For example, first payment $6.00, then $9.00. Include the word "each" to clarify when the number of independent recurring payment cycles is greater than 1. For example, first 3 payments $7.00 each, then $9.00. Use "free" when the value is $0.00. This mirrors natural speech and helps customers understand the element. For example, first payment free, then $9.00. |
| 2 | Selling plan description | `selling_plan.description` Merchants might use this field for promotional text. For example, they might use it for marketing terms, a call-to-action, or preemptively answering questions about cancellation policies or refunds. For more information, refer to Subscription policy link. | Don't express exact prices in option values, for example, "Save $5 a week". For more information, refer to Considerations for currency switching and price rounding. Consider including a link to the subscription policy in the description. Merchants might have a more detailed subscription policy that needs to be accessed by customers. For subscriptions with a pricing policy that changes over time, for example, "First month free, then save 10% on renewals", communicate any future price changes clearly on the product page. For more information, refer to Communicating changes in price over time. |

##### Communicating changes in price over time

Selling plans can have multiple price policies, which allows for the price of a subscription item to change after a certain period. A common approach is to encourage purchases with a lower initial price, for example, "Save $10 on the first 3 deliveries."

If an initial price incentive is applied to a subscription, then explain the current payment and how payments will change in the future.

It's important to be transparent. A lack of information can cause customer mistrust and might appear misleading. Certain states and countries have laws around price clarity, which means that merchants might be subject to lawsuits.

##### Subscription policy link

In the mockup, the link to **View subscription policy** is part of the selling plan description and therefore in the merchant's or app's control to provide. The intention is to allow individual selling plans to provide a link out to a dedicated URL, if available.

The `shop.subscription_policy` object available in Liquid makes it possible to link to a dedicated `/policies/subscription-policy` page. The content of the page is editable by the merchant in the Shopify admin under Legal settings (`/admin/settings/legal`). The content of the subscription policy is also available at checkout.

#### Main call-to-action

Having a call-to-action that reflects the subscription type helps customers differentiate between subscription options and the one-time subscription.

| # | UI element | API properties and information | UI guidelines |
| - | - | - | - |
| 1 | Call-to-action | On first page load, if the product requires a selling plan or one is selected, then switch the call-to-action string to something subscription-specific that merchants can customize. | Update the call-to-action label to **Add subscription to cart** for a subscription. |

### Cart items

Each subscription item displays the most important subscription details to help customers understand their purchase. Customers should be able to understand a subscription's delivery frequency and, if applicable, the commitment period. The price should also match what is represented on the product page.

The subcomponents of a cart item include the following:

* Cart page
* Cart notification

#### Cart page

Customers tend to scan the cart page and review the information before proceeding to checkout:

| # | UI element | API properties and information | UI guidelines |
| - | - | - | - |
| 1 | Selling plan information | `line_item.selling_plan_allocation.selling_plan.name` Use `selling_plan.name` in the cart line item. This same text is used at checkout. For more information, refer to Using the selling plan name. | Because the selling plan name is meant to accurately summarize the subscription, don't list the individual selling plan option values alongside the selling plan name. |

#### Cart notification

The cart notification returns information about the item that was just added to the cart:

| # | UI element | API properties and information | UI guidelines |
| - | - | - | - |
| 1 | Selling plan information | `line_item.selling_plan_allocation.selling_plan.name` This information comes from a Cart API JSON response. Use `selling_plan.name` in the order line item. The same text is used at checkout. For more information, refer to Using the selling plan name. | Because the selling plan name is meant to accurately summarize the subscription, don't list the individual selling plan option values alongside the selling plan name. |

##### Using the selling plan name

The `selling_plan.name` should be a succinct description of the selling plan that can be easily understood by customers. The text is displayed in multiple areas of the online store, such as cart line items, checkout, and past order details. The value is also displayed in the merchant's internal admin on order pages.

**Note:** The selling plan name shouldn't be an additional opportunity to write marketing text.

Shopify doesn't control the value of the name, which means that merchants can enter any text value they want using an app.

When creating selling plan names, implement the following recommended guidelines:

* State the delivery frequency and a prepaid period, if applicable.
* Don't state exact dollars amounts, for example, "$9 a month". Use percentages when applicable.

##### Considerations for currency switching and price rounding

Merchants can sell in [multiple currencies on their online store](https://help.shopify.com/en/manual/payments/shopify-payments/multi-currency/setup).

When a customer visits the online store, Shopify presents the currency that's determined appropriate for the customer. Online stores can offer [a currency selector](https://shopify.dev/docs/api/liquid/tags/form#form-localization) to customers to enable them to manually switch the currency. Shopify also offers a price rounding feature to merchants, which allows merchants to set custom rounding rules for converted prices.

Apps and merchants shouldn't write any prices in the various strings that are shown to customers, for example, selling plan names that say "$9.99 a month" or "Save $5". Any prices that are written in these strings won't reflect currency switching or price rounding, and might be incorrect or misleading to customers.

When an app or merchant wants to express savings in a text field, use percentages whenever possible. For example, `"Deliver every week (Save 20%)"`.

**Note:** Price properties returned from APIs of the Online Store (Liquid or JSON) reflect the currency of the customer's session and any price rounding rules.

### Order details

Customers logged in to the store can view the details of each past order. It's important to let the customer easily identify the subscription product.

| # | UI element | API properties and information | UI guidelines |
| - | - | - | - |
| 1 | Selling plan information | `line_item.selling_plan_allocation.selling_plan.name` Use `selling_plan.name` in the cart notification line item. The same text is used at checkout. For more information, refer to Using the selling plan name. | Because the selling plan name is meant to accurately summarize the subscription, don't list the individual selling plan option values alongside the selling plan name. |

### Next steps

* [Create and manage selling plans](https://shopify.dev/docs/apps/build/purchase-options/subscriptions/selling-plans): Follow a step-by-step workflow to create and manage selling plans in your subscription app.
* [Getting started building a product subscription app extension](https://shopify.dev/docs/apps/build/purchase-options/product-subscription-app-extensions/start-building): Learn how to create a new product subscription app extension with App Bridge Admin, connect the extension to Shopify, and render your working code inside Shopify's UI.

---

## Pricing and payments — Pre-orders and TBYB (overview)

> Fonte: https://shopify.dev/docs/storefronts/themes/pricing-payments/preorder-tbyb

Learn how to support pre-orders and try before you buy in your theme.

### Overview

Merchants can offer purchasing options through pre-order or TBYB apps. For instance, "customers can pre-order a product delivery, pay nothing upfront, and have it delivered a month later. Only once delivered will the customer be charged."

**Tip:** To use Shopify subscriptions, merchants must meet the [qualifying criteria](https://help.shopify.com/en/manual/products/purchase-options/subscriptions/setup#eligibility-requirements).

### How it works

Apps create selling plan groups containing selling plans linked to products and variants. A selling plan group labeled "Pre-order" might let customers choose their upfront payment amount. Merchants can offer multiple optional selling plans or require a specific one, such as "pre-order-only" offers.

### Implementing pre-orders and TBYB in a theme

Use Liquid and JavaScript to integrate these features. Review UX guidelines to ensure quality user experience.

#### Related Resources

- [Add pre-orders and TBYB to your theme](https://shopify.dev/docs/storefronts/themes/pricing-payments/preorder-tbyb/add-preorder-tbyb-to-your-theme) — Learn integration details.
- [Pre-orders and TBYB UX guidelines](https://shopify.dev/docs/storefronts/themes/pricing-payments/preorder-tbyb/preorder-tbyb-ux-guidelines) — Build experiences and style components.

---

## Pricing and payments — Add pre-orders and TBYB to your theme

> Fonte: https://shopify.dev/docs/storefronts/themes/pricing-payments/preorder-tbyb/add-preorder-tbyb-to-your-theme

In this tutorial, you'll learn the basics of how to support pre-orders and TBYB in your theme.

**Tip:** Refer to [Pre-orders and Try Before You Buy UX guidelines](https://shopify.dev/docs/storefronts/themes/pricing-payments/preorder-tbyb/preorder-tbyb-ux-guidelines) to review user experience considerations that might impact your implementation.

### Requirements

* Add a [product form](https://shopify.dev/docs/api/liquid/tags/form#form-product) to a template. A product form can be added to any template that can access the [`product`](https://shopify.dev/docs/api/liquid/objects/product) object.

### Resources

To support pre-orders or TBYB in your theme, you'll use the following resources:

* The [`form`](https://shopify.dev/docs/api/liquid/objects/form) object.
* Objects and object properties that represent selling plan information, including the following:
  * [`selling_plan_group`](https://shopify.dev/docs/api/liquid/objects/selling_plan_group): A group of selling plans that are available for the product's variants.
  * [`selling_plan`](https://shopify.dev/docs/api/liquid/objects/selling_plan): The details of the selling plan.
  * [`selling_plan_allocation`](https://shopify.dev/docs/api/liquid/objects/selling_plan_allocation): Information about how a particular selling plan affects a line item.
  * [`variant.requires_selling_plan`](https://shopify.dev/docs/api/liquid/objects/variant#variant-requires_selling_plan).
* The [`/{locale}/cart/change.js` endpoint](https://shopify.dev/docs/api/ajax/reference/cart#post-locale-cart-change-js) of the Cart AJAX API.

Depending on where you're implementing your selling plan functionality, you'll access selling plan information through the following parent objects:

| Context | Example template types | Parent object |
| - | - | - |
| Product and variant listings | [product](https://shopify.dev/docs/storefronts/themes/architecture/templates/product) | [variant](https://shopify.dev/docs/api/liquid/objects/variant) |
| Variants that have been added to a cart or are part of an order | [cart](https://shopify.dev/docs/storefronts/themes/architecture/templates/cart) | [line_item](https://shopify.dev/docs/api/liquid/objects/line_item) |

For more information about how to present each of these objects and their attributes, refer to [Pre-orders and Try Before You Buy UX guidelines](https://shopify.dev/docs/storefronts/themes/pricing-payments/preorder-tbyb/preorder-tbyb-ux-guidelines).

### Implementing pre-orders or TBYB displays

To support pre-orders or TBYB in your theme, you need to implement the following components:

* **A selling plan selector on the product page**: This selector enables customers to select a selling plan.
* **JavaScript to update the selling plan**: Use JavaScript to update the available selling plans when variants are selected, and update the hidden selling plan input as selling plan options are selected.
* **A selling plan display in the cart**: Indicate to customers when a selling plan has been applied to a line item. You can also implement a selling plan selector to give the option to add a new selling plan, or to remove or edit the current selling plan.
* **A checkout charge in the cart**: Display a checkout charge that represents the amount that customers need to pay during checkout.
* **A selling plan display on the customer order pages**: Indicate to customers when a selling plan has been applied to a line item.

### The selling plan selector on the product page

You can add a selling plan selector for products wherever you can access the [product form](https://shopify.dev/docs/api/liquid/tags/form#form-product). For example, you might add a selling plan selector to the [product template](https://shopify.dev/docs/storefronts/themes/architecture/templates/product) or a section in the template.

Selling plan groups and individual selling plans have a similar structure to products and variants. You can view selling plan groups like products, where there are multiple options that comprise an individual selling plan, similar to variant options that comprise an individual variant.

You can access the available selling plan options through the `selling_plan_groups` attribute of the [product](https://shopify.dev/docs/api/liquid/objects/product#product-selling_plan_groups).

Add the following to your product form:

* For each [selling_plan_group](https://shopify.dev/docs/api/liquid/objects/selling_plan_group), output each of its options inside the product form.
* To track the ID of the selected selling plan, add an input with an attribute of `name="selling_plan"`. The value should be the ID of the selected selling plan. If there's no selected selling plan, then the value should be empty.
* Save the product object so that it can be accessed in JavaScript.

#### Example

The following is an example of how you can display the selling plan group in your product form. Make sure to add the code inside your product form. The example is referring to the file `selling-plans-integration.js`. This file is covered in the JavaScript section. The following code is doing the following:

* Assigning the product and the current variant to be used inside the integration
* Looping through every selling plan group, and displaying each associated selling plan
* Adding a pre-orders or TBYB badge to display next to the product price when a buyer is selecting either a pre-order or TBYB

**Note:** This example demonstrates how to integrate selling plans into your theme. We recommend customizing this integration to suit your specific needs. The following code can also be used as a [theme app block](https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks).

##### /assets/selling-plans-integration.liquid

```liquid
{%- assign current_variant = product.selected_or_first_available_variant | default: product.variants.first -%}


{% if product.selling_plan_groups.size > 0 %}
  <div class="selling_plan_app_container" data-section-id='{{ section.id }}'>
    <script src="{{ 'selling-plans-integration.js' | asset_url }}" defer></script>
    <style>.selling_plan_theme_integration--hidden {display: none;}</style>
    {% for variant in product.variants %}
      {%liquid
        assign variantPrice = variant.price | money_with_currency | escape
        assign variantComparedAtPrice = variant.compare_at_price | money_with_currency | escape
      %}
      {% if variant.selling_plan_allocations.size > 0 %}
        <section data-variant-id='{{ variant.id }}' class='selling_plan_theme_integration {% if variant.id != current_variant.id %}selling_plan_theme_integration--hidden{% endif %}'>
          <fieldset>
            <legend>
              {{ block.settings.supporting_text_title }}
            </legend>
            <div>
              {% unless product.requires_selling_plan %}
                <div>
                  <label>
                    <input
                      aria-label='One-time purchase. Product price {{ variantPrice }}'
                      type='radio'
                      name="purchaseOption_{{ section.id }}_{{ variant.id }}"
                      {% if variant.available == false %}disabled{% endif %}
                      id='{{ section.id }}_one_time_purchase'
                      data-radio-type='one_time_purchase'
                      data-variant-id='{{ variant.id }}'
                      data-variant-price='{{ variantPrice }}'
                      data-variant-compare-at-price='{{ variantComparedAtPrice }}'
                      checked
                    />
                    One-time purchase
                  </label>
                </div>
              {% endunless %}
              {% assign group_ids = variant.selling_plan_allocations | map: 'selling_plan_group_id' | uniq %}
              {% for group_id in group_ids %}
                {%liquid
                   assign group = product | map: 'selling_plan_groups' | where: 'id', group_id | first
                   assign allocations = variant | map: 'selling_plan_allocations' | where: 'selling_plan_group_id', group_id


                   if forloop.first
                    assign first_selling_plan_group = true
                  else
                    assign first_selling_plan_group = false
                  endif
                %}
                <div>
                  <div>
                    <label>{{ group.name }}</label>
                  </div>
                  <ul>
                    {% for allocation in allocations %}


                      {%liquid
                        if forloop.first and product.requires_selling_plan and first_selling_plan_group
                          assign plan_checked = 'checked'
                        else
                          assign plan_checked = nil
                        endif


                        assign allocationPrice = allocation.price | money_with_currency | escape
                        assign allocationComparedAtPrice = allocation.compare_at_price | money_with_currency | escape
                      %}


                      <li>
                        <label>
                          <input
                            type='radio'
                            {% if variant.available == false %}disabled{% endif %}
                            aria-label='{{ allocation.selling_plan.name }}. Product price {{ allocationPrice }}'
                            name="purchaseOption_{{ section.id }}_{{ variant.id }}"
                            data-radio-type='selling_plan'
                            data-selling-plan-id='{{ allocation.selling_plan.id }}'
                            data-selling-plan-group-id='{{ section.id }}_{{ group_id }}_{{ variant.id }}'
                            data-selling-plan-adjustment='{{ allocation.selling_plan.price_adjustments.size }}'
                            data-variant-price='{{ allocationPrice }}'
                            data-variant-compare-at-price='{{ allocationComparedAtPrice }}'
                            {{ plan_checked }} />
                          {{ allocation.selling_plan.name }}
                        </label>
                      </li>
                    {% endfor %}
                  </ul>
                </div>
              {% endfor %}
            </div>
          </fieldset>
        </section>
      {% endif %}
    {% endfor %}
  </div>
  <input
    name='selling_plan'
    class='selected-selling-plan-id'
    type='hidden' />
{% endif %}
```

### JavaScript to update selling plan information

JavaScript is used to interact with the theme integration. This makes it possible for a buyer to select a product and add the correct pre-orders or TBYB to their cart. You can create a separate file named `selling-plans-integration.js` inside the `Assets` folder of your theme. The following example illustrates how JavaScript can interact with the selling plan liquid integration:

##### /assets/selling-plans-integration.js

```js
const hiddenClass = 'selling_plan_theme_integration--hidden';


class SellingPlansWidget {
  constructor(sellingPlansWidgetContainer) {
    this.enablePerformanceObserver();
    this.sellingPlansWidgetContainer = sellingPlansWidgetContainer;
    this.appendSellingPlanInputs();
    this.updateSellingPlanInputsValues();
    this.listenToVariantChange();
    this.listenToSellingPlanFormRadioButtonChange();
    this.updatePrice();
  }


  get sectionId() {
    return this.sellingPlansWidgetContainer.getAttribute('data-section-id');
  }


  get shopifySection() {
    return document.querySelector(`#shopify-section-${this.sectionId}`);
  }


  /*
    We are careful to target the correct form, as there are instances when we encounter an installment form that we specifically aim to avoid interacting with.
  */
  get variantIdInput() {
    return (
      this.addToCartForms[1]?.querySelector(`input[name="id"]`) ||
      this.addToCartForms[1]?.querySelector(`select[name="id"]`) ||
      this.addToCartForms[0].querySelector(`input[name="id"]`) ||
      this.addToCartForms[0].querySelector(`select[name="id"]`)
    );
  }


  get priceElement() {
    return this.shopifySection.querySelector('.price');
  }
```

* The functions `listenToVariantChange()` and `listenToAddToCartForms()` are implemented to track when a product variant is altered or when the product form is updated. The identification of the variant is crucial as it dictates which selling plan box should be displayed. For more information about how to find a variant, refer to our [community post](https://community.shopify.com/c/shopify-apps/subscription-1p-app-block/td-p/2415591).

### The selling plan display in the cart

If a customer selects a selling plan on the product page, then they should see that selection in the cart.

Available selected selling plans are accessible through the `selling_plan_allocation` attribute of the [`line_item` object](https://shopify.dev/docs/api/liquid/objects/line_item). The following is an example:

##### /customers/order.liquid

```liquid
{% if line_item.selling_plan_allocation %}
  <p class="selling-plan">{{ line_item.selling_plan_allocation.selling_plan.name }}</p>
{% endif %}
```

#### The selling plan selector

Rather than just display the selected selling plan, you can give customers the option to add a new selling plan, or to remove or edit the current selling plan. To do this, you should implement a selling plan selector that lists out the available selling plans for the line item's variant, and reflects the currently selected selling plan.

You can loop through the `selling_plan_allocations` attribute of the [`variant`](https://shopify.dev/docs/api/liquid/objects/variant#variant-selling_plan_allocations) object associated with the line item (`line_item.variant`) to build out your selector options. You can compare the selected selling plan ID with the ID of the selling plan at the current index of the loop to make sure that the selector reflects the currently selected selling plan.

To change the selling plan for a line item, you can use the [`/{locale}/cart/change.js`](https://shopify.dev/docs/api/ajax/reference/cart#post-locale-cart-change-js) endpoint of the Cart AJAX API.

##### Example

The following example outputs a selling plan selector:

```liquid
<select name="selling-plan" data-line="{{ forloop.index }}" data-quantity="{{ line_item.quantity }}">
  <option value="">One-time purchase</option>


  {% for selling_plan_allocation in line_item.variant.selling_plan_allocations %}
    <option
      value="{{ selling_plan_allocation.selling_plan.id }}"
      {% if line_item.selling_plan_allocation.selling_plan.id == selling_plan_allocation.selling_plan.id %}selected="selected"{% endif %}
    >
      {{ selling_plan_allocation.selling_plan.name }}
    </option>
  {% endfor %}
</select>
```

The following example illustrates the concept of watching for a change in the selling plan selector and applying those changes through the `/cart/change.js` endpoint. It isn't completely functional.

```js
const sellingPlanSelectors = document.querySelectorAll('[name="selling-plan"]');


sellingPlanSelectors.forEach(function(element) {
  element.addEventListener('change', function(event) {
    const data = {
      'line': event.target.dataset.line,
      'quantity': event.target.dataset.quantity,
      'id': event.target.value
    }


    fetch('/cart/change.js', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
    .then(response => {
      // Refresh page, or re-render cart
      console.log(response);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  });
});
```

### The checkout charge display in the cart

Because pre-order and TBYB can change how much a customer has to pay up front, you should show them how much they'll be charged at checkout. You can calculate this amount using [`selling_plan.checkout_charge`](https://shopify.dev/docs/api/liquid/objects/selling_plan#selling_plan-checkout_charge) object.

You can access a line item's checkout charge through its [`selling_plan_allocation`](https://shopify.dev/docs/api/liquid/objects/selling_plan_allocation).

The following table outlines the types of checkout charges:

| Checkout charge type | Description |
| - | - |
| `percentage` | A percent value representing the percentage amount of the full price that must be paid up front. |
| `price` | The price to be paid up front, in cents. |

**Note:** You can't configure checkout charges for subscriptions. Because of this, subscriptions always have a `value_type` of `percentage` and `value` of 100.

#### Example

The following example outputs the appropriate line item price depending on whether the line item has a selling plan allocation, and what kind of selling plan it is.

```liquid
{% if item.selling_plan_allocation %}
  {%- assign checkout_charge = item.selling_plan_allocation.selling_plan.checkout_charge -%}


  {% if checkout_charge.value_type == 'percentage' %}
    {{ item.original_price | times: checkout_charge.value | divided_by: 100 | money }}
  {% else %}
    {{ checkout_charge.value | money }}
  {% endif %}
{% else %}
  {{ item.original_price | money }}
{% endif %}
```

### Customer order selling plan display

When a customer selects a selling plan, they should see the name of that selection on the customer order page.

The selected selling plan, if there is one, is accessible through the `selling_plan_allocation` attribute of the [`line_item` object](https://shopify.dev/docs/api/liquid/objects/line_item). The following is an example:

##### /customers/order.liquid

```liquid
{% if line_item.selling_plan_allocation %}
  <p class="selling-plan">{{ line_item.selling_plan_allocation.selling_plan.name }}</p>
{% endif %}
```

---

## Pricing and payments — Pre-orders and TBYB UX guidelines

> Fonte: https://shopify.dev/docs/storefronts/themes/pricing-payments/preorder-tbyb/preorder-tbyb-ux-guidelines

A great customer-facing user experience (UX) for pre-orders and TBYB is important for the success of our merchants because it enables them to offer customers a more flexible purchasing process.

A pre-order or a TBYB is any transaction where the payment or fulfillment doesn't happen at the time of purchase.

This guide explains the key principles and component-level guidelines for implementing pre-order and TBYB user interfaces (UIs).

### User experience principles

To provide a good experience with pre-order or TBYB options and gain trust from customers, make sure to implement the following UX principles:

* **Be clear and up front about important information**: Customers should be able to clearly identify the options and make a choice, such as try now, pay later.
* **Provide clarity around money**: Customers should be able to clearly identify how much they will pay at checkout, the total cost of the product, when they'll be charged a remaining balance amount (when applicable), and when their payment method will be charged.
* **Offer as much clarity around delivery timelines as possible**: When possible, provide exact dates or a range, if exact dates are unavailable, for when customers can expect to receive their products, or the duration of the trial period.
* **Provide a seamless integration**: The UI for options should be integrated into the theme's existing design system.
* **Use clear language**: Use language that customers can understand and that refers to the actual purchase terms. For example, use "pre-order", "back-order", and "TBYB".

### User interface guidelines

Before you integrate your pre-order and TBYB options app into a theme, familiarize yourself with the UX guidelines and best practices that are associated with each component.

Apps should consider that products with different ways of purchasing are displayed in the following places on the online store:

* Product pages
* Collection pages
* Search results
* Featured product sections on the home page
* Quick view modals on product cards

When customers can see available ways of purchasing at relevant points in the shopping process, they're more likely to utilize them. Ensure that all relevant information is always included, such as the deposit amount and fulfillment date, estimate for pre-orders, or the trial period length for TBYB.

Pre-order and TBYB information is displayed in the following components of the online store:

* Product forms
* Cart items
* Order details

The following sections include guidance for displaying prices, styling UI components for pre-orders and TBYB, and presenting multiple purchasing options. In each section, the relevant [Liquid](https://shopify.dev/docs/api/liquid) properties that are required to create each component are also referenced.

### Product forms

The product form enables a customer to select their pre-order or TBYB option. This form is where the merchant can provide clarity and more details for a product and its available variants. Product forms are used in product pages, featured product sections on home pages, and quick view modals on product cards.

The subcomponents of a product form include the following:

* A. Price
* B. Selling plan selection
* C. Selling plan details
* D. Main call-to-action

#### A. Price

Customers should be able to clearly identify the full price of the product, and the type of purchasing option that the product is.

| # | UI element | Liquid properties and information | UI guidelines |
| - | - | - | - |
| 1 | Price | `price` | Reflect the price details from the selected pre-order. |
| 2 | Pre-order badge | `selling_plan_group.name` Reflect the price details from the selected pre-order. | Provide a contextual pre-order badge or label to help differentiate against a one-time pre-order. The badge or label will help customers quickly understand that this product can be bought as a pre-order. |

##### Pricing patterns

Pre-orders and TBYB options don't usually come with savings to encourage customers to purchase products.

**Tip:** Pricing for pre-orders often requires a deposit. Don't use visual styling that suggests money saving pricing tactics, such as price strikethroughs, to represent the full price of a product in relation to the initial deposit. Instead, simply display the full price, and if the pre-order product requires a deposit, display the deposit price elsewhere on the page.

##### Main price component

The main price component should always display the total cost of an item. When a customer selects a selling plan or a product variant, the main price component should reflect their changes.

To help customers understand what purchasing option they have selected, do the following:

* Clearly display the product's full price.
* Add the appropriate pre-order or TBYB badge to the component to help clarify to customers that they aren't buying a regular one-time product.

#### B. Selling plan selection

Customers should be able to clearly identify their pre-order or TBYB options.

| # | UI element | Liquid properties and information | UI guidelines |
| - | - | - | - |
| 1 | Purchase options | `product.selling_plan_groups` | One-time purchases and selling plan groups are considered different types of purchasing options. Use the term **Purchase options** in your own designs. |
| 2 | One-time purchase | `product.requires_selling_plan` If the property is `false`, then at least one variant can be purchased as a one-time purchase, and the one-time purchase option should be presented in the UI. | **Group behavior** On the first page load, select the one-time option by default. When the customer interacts with the UI, consider collapsing the unselected group to make good use of the space. Disable the selling plan group selection when it isn't available for a given variant. **Group layout** Prioritize displaying purchasing options in a vertically stacked list to make them readable on all devices. When displayed side-by-side, the information can be crowded on smaller screens. **Group style** Consider displaying purchasing options as radio inputs instead of buttons. Buttons can easily compete with the product form's call-to-action. For example, a submit button. |
| 3 | Selling plan group name | `selling_plan_group.name` Always make this value visible. For more information, refer to [selling_plan_group.name](https://shopify.dev/docs/api/liquid/objects/selling_plan_group#selling_plan_group-name). | |
| 4 | Selling plan option value | `selling_plan_option.value` | Don't express exact prices in option values, such as "$50 deposit", because the values won't be accurate if the currency changes. Expressing percentages is possible because they stay consistent even if the currency changes. For more information refer to Considerations for currency switching and price rounding. |

##### Purchase option label

Show the **Purchase options** label when the following conditions apply:

* A one-time purchase exists and there's at least one `sellingPlanGroup` object.
* A one-time purchase isn't available, but there are multiple `sellingPlanGroup` objects of different types.

Shopify doesn't show the **Purchase options** label when the following conditions apply:

* There are no selling plan groups.
* The product can only be purchased with a selling plan and there's only one selling plan group. In this case, the `sellingPlanGroup` name remains in its position, but without the radio input.

##### Selling plan group name

Selling plan names should make clear the benefit of choosing that option. For example, "Pre-order".

Because the `SellingPlan` object can be associated with multiple selling plan groups on a product, selling plan group names are used to differentiate purchase options.

##### Display selling plan option values

All the option values must be displayed at a glance from a group. Consider adapting the component layout to optimize readability.

Components should adapt to the number of options being shown. When there are many options to choose from, an appropriate component should be selected to enable customers to view all options easily. When there are fewer options, a different component may be used. When possible, apply the appropriate layout to all values within a selling plan group for consistency:

* Four options or less: Show each option as a radio button to allow customers to view what's available.
* More than four options: Use a select dropdown to emphasize the customer's selection and hide other options within the collapsed dropdown.

###### UI update on variant change

A product's variants might not all support the same purchasing options. As a customer changes their variant selection, the components should update to make clear which options are available and unavailable.

When a selected option within a selling plan group is unavailable, the following events should happen:

* The unavailable options are unselected, and the customer must make a new selection to successfully submit the form.
* The unavailable options for the selected variant are disabled.
* The form submission button is enabled. Disabling the button removes the ability to display an error message and instead displays the product as unavailable, which is false. Let the customer click the button but prevent them from adding the product to the cart. Then, anchor and scroll back to the faulty UI area and display a message that describes why the process can't complete and what the customer needs to do to proceed.

#### C. Selling plan details

Display important deferred pre-order and TBYB terms and selections to customers. The summary confirms a customer's selections, shows any conditions, and helps build trust in the brand.

| # | UI element | Liquid properties and information | UI guidelines |
| - | - | - | - |
| 1 | Selling plan description | `selling_plan.description` | Don't express exact prices in option values, for example, "$100 deposit". For more information, refer to Considerations for currency switching and price rounding. Consider including a link to the returns or billing policies in the description. Merchants might have more detailed policies that need to be accessed by customers. |

#### D. Main call-to-action

Having a call-to-action (main button text) that reflects the purchasing option type helps customers differentiate between a pre-order or a TBYB and a one-time purchase, even if there's only one option available.

| # | UI element | Liquid properties and information | UI guidelines |
| - | - | - | - |
| 1 | Call-to-action | On first page load, if the product requires a selling plan or one is selected, then switch the call-to-action string to something purchase option-specific that merchants can customize. | Update the call-to-action label to the accelerated checkout button for a deferred purchase option, and keep the add to cart button as is. |

### Cart items

Each pre-order or TBYB option item displays the most important details to help customers understand their purchase.

* For pre-order items, make sure that the customer understands the fulfillment date and relevant payment information, such as a deposit amount and future payments.
* For TBYB items, customers should see the trial period length. The price should also match what's represented on the product page.

A cart item includes the following subcomponents:

* Cart page
* Cart notification

#### Cart page

Customers tend to scan the cart page and review the information before proceeding to checkout, so it's important that the following elements are clearly represented.

| # | UI element | Liquid properties and information | UI guidelines |
| - | - | - | - |
| 1 | Selling plan information | `line_item.selling_plan_allocation.selling_plan.name` Use `selling_plan.name` in the cart line item. This same text is used at checkout. For more information, refer to Using the selling plan name. | Because the selling plan name is meant to accurately summarize the deferred purchase option, don't list the individual selling plan option values alongside the selling plan name. |
| 2 | Price | `price` | Display the full price of the product so that the customer is reminded of the total cost of the item they're buying. |
| 3 | Price at checkout | `selling_plan.checkout_charge.value` | The price customers will pay at checkout. For pre-order items, this price usually represents the deposit amount. For TBYB items, the price will usually be $0 to indicate to customers that they won't need to pay anything at checkout. |

#### Cart notification

The cart notification returns information about the item that was just added to the cart.

| # | UI element | Liquid properties and information | UI guidelines |
| - | - | - | - |
| 1 | Selling plan information | `line_item.selling_plan_allocation.selling_plan.name` Use `selling_plan.name` in the cart line item. This same text is used at checkout. For more information, refer to Using the selling plan name. | Because the selling plan name is meant to accurately summarize the deferred purchase option, don't list the individual selling plan option values alongside the selling plan name. |
| 2 | Price | `price` | Display the full price of the product so that the customer is reminded of the total cost of the item that they're buying. |

##### Using the selling plan name

The `selling_plan.name` should be a succinct description of the selling plan that can be easily understood by customers. The text is displayed in multiple areas of the online store, such as cart line items, checkout, and past order details. The value is also displayed in the merchant's internal admin on order pages.

**Note:** The selling plan name shouldn't include any marketing text.

Shopify doesn't control the value of the name, which means that merchants can enter any text value they want using an app.

When creating selling plan names, implement the following recommended guidelines:

* State the type of deferred purchase option.
* Write the deposit amount and payment due date of the product in order for the customer to keep a reference of it throughout the purchase journey.

##### Considerations for currency switching and price rounding

Merchants can sell in [multiple currencies on their online store](https://help.shopify.com/en/manual/payments/shopify-payments/multi-currency/setup).

When a customer visits the online store, Shopify presents the currency that's determined appropriate for the customer. Online stores can offer a [currency selector](https://shopify.dev/docs/api/liquid/tags/form#form-localization) to customers to enable them to manually switch the currency. Shopify also offers a price rounding feature to merchants, which enables merchants to set custom rounding rules for converted prices.

**Note:**

* Any prices that are written in strings won't reflect currency switching or price rounding, and might be incorrect or misleading to customers.
* Price properties returned from APIs of the Online Store (Liquid or JSON) reflect the currency of the customer's session and any price rounding rules.

### Order details

Customers logged in to the store can view the details of each past order. It's important to let the customer easily identify orders with pre-order or TBYB products.

| # | UI element | Liquid properties and information | UI guidelines |
| - | - | - | - |
| 1 | Selling plan information | `line_item.selling_plan_allocation.selling_plan.name` Use `selling_plan.name` in the cart line item. This same text is used at checkout. For more information, refer to Using the selling plan name. | Because the selling plan name is meant to accurately summarize the pre-order or TBYB option, don't list the individual selling plan option values alongside the selling plan name. |
| 2 | Price | `price` | Display the full price of the product so that the customer is reminded of the total cost of the item they're buying. |
| 3 | Price at checkout | `selling_plan.checkout_charge.value` | The price customers will pay at checkout. For pre-order items, this price usually represents the deposit amount. For TBYB items, the price will usually be $0 to indicate to customers that they won't need to pay anything at checkout. |

### Next steps

* [Create and manage pre-order and TBYB](https://shopify.dev/docs/apps/build/purchase-options/deferred/build-deferment-solution)
* [Getting started with a pre-order or TBYB app](https://shopify.dev/docs/apps/build/purchase-options/deferred/create-deferred-purchase-app/start-building)
* [Get started with product subscription app extensions](https://shopify.dev/docs/apps/build/purchase-options/product-subscription-app-extensions/start-building)

---

## Pricing and payments — Accelerated checkout

> Fonte: https://shopify.dev/docs/storefronts/themes/pricing-payments/accelerated-checkout

### Implementing Accelerated Checkout Buttons in Your Theme

You can add accelerated checkout buttons anywhere in your theme, such as in your cart or product template, within a section, or in a cart drawer.

If you're using the Section Rendering API, it re-renders the accelerated checkout buttons when the section is requested (for example, in a cart drawer). The buttons render more slowly on their first request but load more quickly on subsequent requests after the JavaScript library is downloaded and web components are registered.

Consider placing accelerated checkout buttons near the checkout input of your cart form so customers can choose between regular and accelerated checkout options.

#### Implement Accelerated Checkout Buttons on Product Pages

On product pages, Shopify dynamically recommends a single button to help customers quickly purchase the product they're viewing. To include this button, add the `payment_button` Liquid HTML filter:

```liquid
{% form 'product', product %}
  <!-- form content -->

  <input type="submit" value="Add to cart" />
  {{ form | payment_button }}
{% endform %}
```

#### Implement Accelerated Checkout Buttons on Cart

On cart pages, you can display all accelerated buttons your store has enabled.

1. Check whether your store has any accelerated checkout buttons enabled using the `additional_checkout_buttons` object
2. If it returns `true`, display the buttons using the `content_for_additional_checkout_buttons` object. Otherwise, nothing will be displayed

```liquid
{% if additional_checkout_buttons %}
  {{ content_for_additional_checkout_buttons }}
{% endif %}
```

### Customize the Accelerated Checkout Buttons

You can customize the accelerated checkout buttons on product and cart pages to match your theme.

**Caution:** The accelerated checkout buttons hide their HTML in a custom element with a closed shadow DOM. Styling or event tracking targeting the HTML structure of these buttons will not work. See the accelerated checkout upgrade guide to migrate legacy customizations to supported methods.

#### Accelerated Checkout Button CSS Custom Properties

| CSS Custom Property | Description | Default |
|---|---|---|
| `--shopify-accelerated-checkout-button-block-size` | The height of individual rendered wallet buttons. Minimum: `25px`, Maximum: `55px` | `44px` on product pages, `42px` on cart vertical layout |
| `--shopify-accelerated-checkout-button-inline-size` | (Cart only) Width of individual rendered wallet buttons in horizontal row layout. Minimum: `25px`, Maximum: `55px` | `54px` |
| `--shopify-accelerated-checkout-button-border-radius` | Corner radius of rendered wallet buttons | `0px` on product pages, `4px` on cart |
| `--shopify-accelerated-checkout-button-box-shadow` | Drop shadow cast by rendered wallet buttons | `none` |
| `--shopify-accelerated-checkout-skeleton-background-color` | Background color of loading skeleton | `#dedede` |
| `--shopify-accelerated-checkout-skeleton-animation-opacity-start` | Initial opacity in loading skeleton animation | `1` |
| `--shopify-accelerated-checkout-skeleton-animation-opacity-end` | Final opacity in loading skeleton animation | `0.5` |
| `--shopify-accelerated-checkout-skeleton-animation-duration` | Duration of opacity transition | `4s` |
| `--shopify-accelerated-checkout-skeleton-animation-timing-function` | Timing function for opacity animation | `ease` |
| `--shopify-accelerated-checkout-inline-alignment` | (Cart only) Positioning of wallet buttons in horizontal row layout. Accepts valid `justify-content` values | `start` |
| `--shopify-accelerated-checkout-row-gap` | (Cart only) Vertical spacing between rendered wallet buttons in vertical stack layout | `8px` |

Apply these CSS custom properties on the `shopify-accelerated-checkout` and `shopify-accelerated-checkout-cart` element selectors.

#### Example Usage

```css
shopify-accelerated-checkout {
  --shopify-accelerated-checkout-button-block-size: 44px;
  --shopify-accelerated-checkout-button-border-radius: 0px;
  --shopify-accelerated-checkout-button-box-shadow: none;
  --shopify-accelerated-checkout-skeleton-background-color: #dedede;
  --shopify-accelerated-checkout-skeleton-animation-opacity-start: 1;
  --shopify-accelerated-checkout-skeleton-animation-opacity-end: 0.5;
  --shopify-accelerated-checkout-skeleton-animation-duration: 4s;
  --shopify-accelerated-checkout-skeleton-animation-timing-function: ease;
}

shopify-accelerated-checkout-cart {
  --shopify-accelerated-checkout-button-block-size: 42px;
  --shopify-accelerated-checkout-button-inline-size: 54px;
  --shopify-accelerated-checkout-button-border-radius: 4px;
  --shopify-accelerated-checkout-button-box-shadow: none;
  --shopify-accelerated-checkout-inline-alignment: flex-start;
  --shopify-accelerated-checkout-row-gap: 8px;
  --shopify-accelerated-checkout-skeleton-background-color: #dedede;
  --shopify-accelerated-checkout-skeleton-animation-opacity-start: 1;
  --shopify-accelerated-checkout-skeleton-animation-opacity-end: 0.5;
  --shopify-accelerated-checkout-skeleton-animation-duration: 4s;
  --shopify-accelerated-checkout-skeleton-animation-timing-function: ease;
}
```

#### Additional Alignment Properties

By default on cart pages, accelerated checkout buttons are presented horizontally and left-aligned. If there's insufficient space for all buttons to display side-by-side, they are presented vertically and take on the full width of their container.

##### Present Buttons Vertically

To present the buttons vertically by default, add the class `additional-checkout-buttons--vertical` to the container holding the `content_for_additional_checkout_buttons` object.

```liquid
{% if additional_checkout_buttons %}
  <div class="additional-checkout-buttons--vertical">
    {{ content_for_additional_checkout_buttons }}
  </div>
{% endif %}
```

---

## Pricing and payments — Shop Pay Installments

> Fonte: https://shopify.dev/docs/storefronts/themes/pricing-payments/installments

[Shop Pay Installments](https://help.shopify.com/manual/payments/shop-pay-installments) allows customers to pay for orders between 50 USD and 3,000 USD in 4 interest-free installments.

The Shop Pay Installments banner lets customers know that they have the option to pay in installments. It includes a **Learn more** link that opens a pop-up which shows how much the installment amount is, more information about installments, and any required disclosures.

In this tutorial, you'll learn how to add a Shop Pay Installments banner to the following locations:

* The product form
* The cart form

### Requirements

Depending on where you want to add the Shop Pay Installments banner, you need to do one, or both, of the following:

* Add a [product form](https://shopify.dev/docs/api/liquid/tags/form#form-product) to a template. A product form can be added to any template that can access the [`product` object](https://shopify.dev/docs/api/liquid/objects/product).
* Add a [cart form](https://shopify.dev/docs/api/liquid/tags/form#form-cart) to a template. A cart form can be added to any template that can access the [`cart` object](https://shopify.dev/docs/api/liquid/objects/cart).

### Resources

To implement this feature, you'll use the following:

* The [`form`](https://shopify.dev/docs/api/liquid/objects/form) object
* The [`payment_terms`](https://shopify.dev/docs/api/liquid/filters/payment_terms) filter

**Tip:** The `payment_terms` filter requires the `form` object from the Liquid [product form](https://shopify.dev/docs/api/liquid/tags/form#form-product) or [cart form](https://shopify.dev/docs/api/liquid/tags/form#form-cart). If your theme doesn't use these forms, then you can convert an HTML form to Liquid by [specifying any HTML attributes](https://shopify.dev/docs/api/liquid/tags/form#form-html-attributes) you need on the form.

### Implementing a Shop Pay Installments banner

The Shop Pay Installments banner can be added to the following locations:

* The product form
* The cart form

**Note:** The Shop Pay Installments banner appears only if Shop Pay Installments is enabled in the merchant's store.

#### Add the banner to the product form

To add a Shop Pay installments banner to the [product form](https://shopify.dev/docs/api/liquid/tags/form#form-product), you need to add a reference to the [`form` object](https://shopify.dev/docs/api/liquid/objects/form), with the [`payment_terms`](https://shopify.dev/docs/api/liquid/filters/payment_terms) filter applied, between the opening and closing `form` tags:

```liquid
{% form 'product', product %}
<!-- product price -->
{{ form | payment_terms }}
...
{% endform %}
```

The reference should be below the product price so that price and payment information is grouped together.

**Note:** The installments banner automatically updates based on the currently selected variant. The currently selected variant is noted by a form input with an attribute of `name="id"`.

If your theme doesn't include the price inside the product form, then you can create a second instance of the product form near the price display to host the installments banner. Inside this second form, you need to include a hidden `<input />` that notes the currently selected variant. This hidden input needs to be updated as the variant selection changes.

```liquid
<!-- product price -->


{% form 'product', product %}
<input type="hidden" name="id" value="{{ product.selected_or_first_available_variant.id }}" />
{{ form | payment_terms }}
{% endform %}
```

The `payment_terms` filter can be used anywhere that you can use a product form. It's commonly used in the [product template](https://shopify.dev/docs/storefronts/themes/architecture/templates/product), or a section inside of the template.

#### Add the banner to the cart form

To add a Shop Pay installments banner to the [cart form](https://shopify.dev/docs/api/liquid/tags/form#form-cart), you need to add a reference to the [`form` object](https://shopify.dev/docs/api/liquid/objects/form), with the [`payment_terms`](https://shopify.dev/docs/api/liquid/filters/payment_terms) filter applied, between the opening and closing `form` tags:

```liquid
{% form 'cart', cart %}
<!-- cart subtotal -->
{{ form | payment_terms }}
...
{% endform %}
```

The reference should be below the cart subtotal price so that price and payment information is grouped together.

The `payment_terms` filter can be used anywhere that you can use a cart form. It's commonly used in the [cart template](https://shopify.dev/docs/storefronts/themes/architecture/templates/cart), or a section inside of the template.

##### Updating the banner with cart total changes

To stay updated with the cart total, the banner parses for the subtotal price based on the attribute `data-cart-subtotal`. Most free Shopify themes have this attribute on their subtotal display by default, so the banner will update automatically. If your banner doesn't update automatically, then you need to add the `data-cart-subtotal` attribute to your subtotal display.

### Example

```liquid
<span data-cart-subtotal>{{ cart.total_price | money }}</span>
```

---

## Delivery and fulfillment — Overview

> Fonte: https://shopify.dev/docs/storefronts/themes/delivery-fulfillment

While merchants face challenges converting customers, post-purchase logistics remain critical. "The most common method is shipping, however Shopify also provides merchants the option to offer products for local pickup."

Merchants can display pickup availability on product pages, enabling customers to determine if this fulfillment option suits their needs for specific products.

* [Pickup availability](https://shopify.dev/docs/storefronts/themes/delivery-fulfillment/pickup-availability)

---

## Delivery and fulfillment — Show pickup availability on product pages

> Fonte: https://shopify.dev/docs/storefronts/themes/delivery-fulfillment/pickup-availability

Merchants can make their products available through [local pickup](https://help.shopify.com/manual/shipping/setting-up-and-managing-your-shipping/local-methods/local-pickup), and you can display whether a specific product variant is available for local pickup on the product page. This allows customers to view this information without having to add the product to cart and proceed to checkout to view the shipping details.

In this tutorial, you'll learn how to show variant pickup availability on product pages.

### Requirements

* [Variant selection](https://shopify.dev/docs/storefronts/themes/product-merchandising/variants#variant-selectors) functionality. The pickup availability JavaScript function needs to be run when variants are selected.

### Resources

To implement pickup availability, you'll use the following:

* The [`variant` object](https://shopify.dev/docs/api/liquid/objects/variant)
* The [`store_availability` object](https://shopify.dev/docs/api/liquid/objects/store_availability)
* The [`location` object](https://shopify.dev/docs/api/liquid/objects/location)

### Implementing pickup availability

To support pickup availability functionality in your theme, you need to implements the following components:

* The pickup availability section: Renders the display content, which contains information about each location that the current variant is stocked at.
* The pickup availability container: An empty container on the product page that hosts the section content.
* A JavaScript function: Renders the section content inside the container, and makes any updates on variant selection.

**Caution:** The examples below are only meant to illustrate basic considerations for implementing this feature. The full implementation will vary depending on your theme and what you want the display to look like. You can refer to the following files in Dawn for an example of a complete solution:

* [Section](https://github.com/Shopify/dawn/blob/6490d2f90a8eea98d696dcbe28f092dcc9740efd/sections/pickup-availability.liquid)
* [Container](https://github.com/Shopify/dawn/blob/6490d2f90a8eea98d696dcbe28f092dcc9740efd/sections/main-product.liquid#L313)
* [Buy Button](https://github.com/Shopify/dawn/blob/6490d2f90a8eea98d696dcbe28f092dcc9740efd/snippets/buy-buttons.liquid#L102)
* [JS](https://github.com/Shopify/dawn/blob/6490d2f90a8eea98d696dcbe28f092dcc9740efd/assets/pickup-availability.js)
* [CSS](https://github.com/Shopify/dawn/blob/6490d2f90a8eea98d696dcbe28f092dcc9740efd/assets/component-pickup-availability.css)

### The pickup availability section

The pickup availability section hosts the actual content to be displayed, which has two main components:

* Availability summary
* Availability modal

This section is rendered inside the pickup availability container by the JavaScript function.

#### Availability summary

The availability summary loops through the locations returned from the `store_availabilites` attribute of the current variant to find any locations that have `pick_up_enabled` set to `true`. If there are any, then the availability of the current variant at the first location is displayed, along with a button to open the availability modal.

#### Availability modal

The availability modal displays the product and variant titles, and each location that the current variant is stocked at. For each location, the current availability and address are shown.

#### Example

The following is an example of a pickup availability section with an availability summary and modal.

**Note:** You should only output the availability summary and modal if the current variant has at least one location with pickup enabled.

##### sections/pickup-availability.liquid

```liquid
<div class="pickup-availability-container">
  {%- assign pick_up_availabilities = product_variant.store_availabilities | where: 'pick_up_enabled', true -%}


  {%- if pick_up_availabilities.size > 0 -%}
    <!-- Availability summary -->
    <div class="pickup-availability-information">
      {%- assign closest_location = pick_up_availabilities.first -%}


      {%- if closest_location.available -%}
        {% render 'icon-in-stock' %}
      {%- else -%}
        {% render 'icon-out-of-stock' %}
      {%- endif -%}


      <div class="pickup-availability-information-container">
        {%- if closest_location.available -%}
          <p class="pickup-availability-information__title">
            {{ 'pickup_availability.general.pick_up_available_at_html' | t: location_name: closest_location.location.name }}
          </p>
          <p class="pickup-availability-information__stock pickup-availability-small-text">
            {{ closest_location.pick_up_time }}
          </p>
          <button
            class="pickup-availability-information__button js-modal-open-pickup-availability-modal pickup-availability-small-text"
            data-pickup-availability-modal-open aria-haspopup="dialog"
          >
            {%- if pick_up_availabilities.size == 1 -%}
              {{ 'pickup_availability.general.view_store_info'  | t }}
            {%- else -%}
              {{ 'pickup_availability.general.check_other_stores'  | t }}
            {%- endif -%}
          </button>
        {%- else -%}
          <p class="pickup-availability-information__title">
            {{ 'pickup_availability.general.pick_up_unavailable_at_html' | t: location_name: closest_location.location.name }}
          </p>


          {%- if pick_up_availabilities.size > 1 -%}
            <button class="pickup-availability-information__button js-modal-open-pickup-availability-modal pickup-availability-small-text" data-pickup-availability-modal-open aria-haspopup="dialog">
              {{ 'pickup_availability.general.check_other_stores'  | t }}
            </button>
          {%- endif -%}
        {%- endif -%}
      </div>
    </div>


    <!-- Availability modal -->
    <div
      class="pickup-availabilities-modal modal"
      id="PickupAvailabilityModal"
      role="dialog"
      aria-modal="true"
      aria-labelledby="PickupAvailabilitiesModalProductTitle"
    >
      <div class="pickup-availabilities-modal__header">
        <div class="pickup-availabilities-modal__product-information">
          <h2
            id="PickupAvailabilitiesModalProductTitle"
            class="pickup-availabilities-modal__product-title"
            data-pickup-availability-modal-product-title
          >
          </h2>
          <p
            class="pickup-availabilities-modal__variant-title pickup-availability-small-text"
            data-pickup-availability-modal-variant-title
          >
            {{ product_variant.title }}
          </p>
        </div>
        <button
          type="button"
          class="pickup-availabilities-modal__close js-modal-close-pickup-availability-modal text-link"
          aria-label="{{ 'general.accessibility.close_modal'  | t }}"
        >
          {% render 'icon-close' %}
        </button>
      </div>
      <ul class="pickup-availabilities-list" role="list">
        {%- for availability in pick_up_availabilities -%}
          <li class="pickup-availability-list__item">
            <h3 class="pickup-availability-list__location">
              {{ availability.location.name }}
            </h3>
            <div class="pickup-availability-list__stock pickup-availability-small-text">
              {%- if availability.available -%}
                {% render 'icon-in-stock' %} {{ 'pickup_availability.general.pick_up_available'  | t }}, {{ availability.pick_up_time | downcase }}
              {%- else -%}
                {% render 'icon-out-of-stock' %} {{ 'pickup_availability.general.pick_up_currently_unavailable'  | t }}
              {%- endif -%}
            </div>
            {%- assign address = availability.location.address -%}
            <address class="pickup-availability-list__address">
              {{ address | format_address }}
            </address>
            {%- if address.phone.size > 0 -%}
              <p class="pickup-availability-list__phone pickup-availability-small-text">
                {{ address.phone }}<br />
              </p>
            {%- endif -%}
          </li>
        {%- endfor -%}
      </ul>
    </div>
  {%- endif -%}
</div>


{% schema %}
{
  "name": {},
  "settings": []
}
{% endschema %}
```

### The pickup availability container

The pickup availability container is an empty `<div>` element that the JavaScript function will render the section contents inside of. It should be placed wherever you want the availability summary to show on the product page.

#### Example

```html
<div class="product-single__store-availability-container"
data-store-availability-container
data-product-title="{{ product.title | escape }}"
data-has-only-default-variant="{{ product.has_only_default_variant }}"
data-base-url="{{ shop.url }}{{ routes.root_url }}"
>
</div>
```

### The JavaScript function

To add the pickup availability section content inside the pickup availability container, you need to use the [section rendering API](https://shopify.dev/docs/api/ajax/section-rendering). The request needs to be prefixed with a `/variants/[variant-id]` parameter, where `[variant-id]` is the [variant ID](https://shopify.dev/docs/api/liquid/objects/variant#variant-id) of the selected variant.

To access the variant ID, and update the display when a variant is selected, you need to make a call to your pickup availability JavaScript function from the [JavaScript responsible for updating product page elements on variant selection](https://shopify.dev/docs/storefronts/themes/product-merchandising/variants).

#### Example

```js
fetch(window.Shopify.routes.root + "variants/[variant-id]/?section_id=pickup-availability")
.then(response => response.text())
.then(text => {
  const container = document.querySelector('[data-store-availability-container]');
  const pickupAvailabilityHTML = new DOMParser()
    .parseFromString(text, 'text/html')
    .querySelector('.shopify-section');


  container.appendChild(pickupAvailabilityHTML);
})
.catch(e => {
  console.error(e);
});
```

**Tip:** You can't access the Liquid product object in the pickup availability section. This means that product-specific changes, like updating the title and removing the variant title if the product only has a default variant, need to be done through JavaScript. The example availability container includes `data-product-title` and `data-has-only-default-variant` attributes for this purpose.

---

## Customer engagement — Overview

> Fonte: https://shopify.dev/docs/storefronts/themes/customer-engagement

Interacting with customers represents a crucial business function for merchants. These interactions encompass:

* [Getting consent for email marketing](https://shopify.dev/docs/storefronts/themes/customer-engagement/email-consent) — enabling merchants to build repeat customer relationships
* [Adding a contact form](https://shopify.dev/docs/storefronts/themes/customer-engagement/add-contact-form) — facilitating customer communication with merchants

---

## Customer engagement — Email consent

> Fonte: https://shopify.dev/docs/storefronts/themes/customer-engagement/email-consent

Customers can consent to email marketing through the theme using a newsletter sign-up form.

### Newsletter sign-up form

You can add a newsletter sign-up form to your theme with the Liquid [form tag](https://shopify.dev/docs/api/liquid/tags/form#form-customer) and accompanying `'customer'` parameter. Inside the form, you need to include an input with the following attributes:

| Attribute | Value |
| - | - |
| `type` | `email` |
| `name` | `contact[email]` |

For example:

```liquid
{% form 'customer' %}
<div class="email">
  <label for="email">Email</label>
  <input type="email" name="contact[email]" />
</div>


<div class="submit">
  <input type="submit" value="Sign up" />
</div>
{% endform %}
```

When a customer signs up through this form, a customer will be created with the entered email, and the `accepts_marketing` attribute of the associated [`customer` object](https://shopify.dev/docs/api/liquid/objects/customer) will be set to `true`.

**Tip:** For another example of a newsletter sign-up form, you can refer to [Dawn's implementation](https://github.com/Shopify/dawn/blob/main/sections/footer.liquid).

---

## Customer engagement — Add a contact form to your theme

> Fonte: https://shopify.dev/docs/storefronts/themes/customer-engagement/add-contact-form

You can add a contact form to your theme to allow customers to get in touch with the merchant.

**Tip:** To learn more about the merchant experience of receiving submissions, refer to [View contact form submissions](https://help.shopify.com/manual/online-store/themes/customizing-themes/add-contact-page#view-contact-form-submissions).

You can add this form with the Liquid [form tag](https://shopify.dev/docs/api/liquid/tags/form#form-contact) and accompanying `'contact'` parameter. Inside the form, you can include two different input types:

* Required input
* Optional inputs

The following is an example of the form with both of the above input types:

```liquid
{% form 'contact' %}
  {{ form.errors | default_errors }}


  <div class="first-name">
    <label for="first-name">First name</label>
    <input type="text" name="contact[first_name]" id="first-name" />
  </div>


  <div class="last-name">
    <label for="last-name">Last name</label>
    <input type="text" name="contact[last_name]" id="last-name" />
  </div>


  <div class="phone">
    <label for="phone">Phone</label>
    <input type="tel" name="contact[phone]" id="phone" />
  </div>


  <div class="email">
    <label for="email">Email</label>
    <input type="email" name="contact[email]" id="email" />
  </div>


  <div class="order-number">
    <label for="order-number">Order number</label>
    <input type="text" name="contact[order_number]" id="order-number" />
  </div>


  <div class="message">
    <label for="message">Message</label>
    <textarea name="contact[body]" id="message"></textarea>
  </div>


  <div class="submit">
    <input type="submit" value="Create" />
  </div>
{% endform %}
```

**Tip:** For another example of a contact form, you can refer to [Dawn's implementation](https://github.com/Shopify/dawn/blob/main/sections/contact-form.liquid).

### Required input

The following input is required for the form to submit successfully:

| Input | type | name |
| - | - | - |
| Email | `email` | `contact[email]` |

### Optional inputs

The optional inputs can be any [HTML input type](https://developer.mozilla.org/en-US/docs/Learn/Forms/HTML5_input_types). They need to have an attribute of `name="contact[information_id]"`, where `information_id` briefly identifies the information that you're collecting. These titles appear in contact notifications, and must be unique within the form.

To make a specific field required for a customer, you need to add a field attribute of `required="required"` within the field's input element.

Below are examples of input types that you might want to add to your form.

#### Dropdown type

```html
<div class="request-type">
  <label for="request-type">What is this regarding?</label>
  <select id="request-type" name="contact[request_type]">
    <option>Returns</option>
    <option>Shipping</option>
    <option>Custom order</option>
    <option>Other</option>
  </select>
</div>
```

#### Radio type

```html
<div class="contact-method">
  <label for="contact-method">How do you want us to contact you?</label>
  <input type="radio" name="contact[contact_method]" value="email" id="email" /><label for="email">Email</label><br />
  <input type="radio" name="contact[contact_method]" value="phone" id="phone" /><label for="phone">Phone</label><br />
  <input type="radio" name="contact[contact_method]" value="text message" id="text" /><label for="text">Text message</label>
</div>
```

#### Checkbox type

To accept multiple selections, each input in a checkbox group needs to have a unique `name` value. If you don't use a unique `name` value for each input, then the form will only return the last value that was selected.

```html
<div class="contact-time">
  <label for="contact-time">When is the best time to reach you?</label>
  <input type="checkbox" name="contact[contact_time_1]" value="morning" /><label for="morning">Morning</label><br />
  <input type="checkbox" name="contact[contact_time_2]" value="afternoon" /><label for="afternoon">Afternoon</label><br />
  <input type="checkbox" name="contact[contact_time_3]" value="evening" /><label for="evening">Evening</label>
</div>
```

---

## Customer engagement — Account component

> Fonte: https://shopify.dev/docs/storefronts/themes/customer-engagement/account-component

The [`<shopify-account>`](https://shopify.dev/docs/api/storefront-web-components/components/shopify-account) component displays a customer avatar in your theme. When customers click the avatar, an account sheet opens with menu links. For signed-out customers, sign-in options appear above the menu.

The account component is designed to drive customer sign-ins to accelerate checkout and unlock storefront personalization. It supports the following sign-in methods: passwordless sign-in, automatic sign-in with Shop recognition, and social sign-in providers. Customers can also opt in to email marketing when signing in through the component.

Customers can sign in and stay on the storefront, without being diverted to their account. The account sheet displays menu links such as **Orders** and **Profile** upfront, helping customers understand what they can access before signing in.

The avatar displays differently based on customer state:

* **Signed out**: "Displays a default account icon, customizable through the [`signed-out-avatar`](https://shopify.dev/docs/api/storefront-web-components/components/shopify-account#slots-propertydetail-signedoutavatar) slot."
* **Signed in**: Displays the customer's initial or Shop profile picture.

When sign-in links are enabled, the avatar displays in the header. For shops using the latest version of customer accounts, clicking the avatar opens the account sheet. For shops using legacy customer accounts, the avatar links directly to the sign-in page instead.

**Note:** "Shopify controls this component and can update it independently of your theme. While you can apply basic styling to match your theme, the component maintains a consistent appearance across shops."

### Implementing the account component in your theme header

Add the [`<shopify-account>`](https://shopify.dev/docs/api/storefront-web-components/components/shopify-account) component to your site header and ensure it's visible on both mobile and desktop so customers can access their account from any page.

```html
{% if shop.customer_accounts_enabled %}

<shopify-account menu="customer-account-main-menu">
</shopify-account>

{% endif %}
```

### Customize the account component

You can style the component to match your theme. The customization options depend on whether the user is signed in or signed out:

#### Signed-out avatar

"The component includes a default signed-out avatar. You can style it using the CSS `part`, or replace the markup entirely using the `slot`."

```html
<style>
  shopify-account::part(signed-out-avatar) {
    padding: 12px;
    width: 64px;
    height: 64px;
  }
</style>

<shopify-account menu="customer-account-main-menu">
  <div slot="signed-out-avatar">
    <img src="{{ 'account-icon.svg' | asset_url }}" alt="Account"/>
  </div>
</shopify-account>
```

#### Signed-in avatar and account sheet

The signed-in avatar and the account sheet are controlled by the component. "You can customize the look and feel by setting CSS variables in your theme."

For the list of available CSS variables, refer to the [`shopify-account` documentation](https://shopify.dev/docs/api/storefront-web-components/components/shopify-account#css%20variables).

```html
<style>
  shopify-account {
    --shopify-account-signed-in-avatar-size: 36px;
    --shopify-account-signed-in-avatar-color-background: fuchsia;
    --shopify-account-signed-in-avatar-color-text: black;
  }
</style>

<shopify-account menu="customer-account-main-menu">
</shopify-account>
```

### Menu links

"We recommend adding a theme setting so that merchants can change which menu is used."

```html
<shopify-account menu="{{ section.settings.customer_account_menu }}">
</shopify-account>
```

```json
// Add to schema section in header.liquid
{
  "type": "link_list",
  "id": "customer_account_menu",
  "label": "Customer account menu",
  "default": "customer-account-main-menu"
}
```

Using `customer-account-main-menu` keeps links consistent between the component and customer account pages. This menu includes links to **Orders** and **Profile**.

Merchants can add, remove, or reorder links in the Shopify admin under **Content** > **Menus**. For more information, see the [Help Center](https://help.shopify.com/en/manual/online-store/menus-and-links).

---

## Markets — Overview

> Fonte: https://shopify.dev/docs/storefronts/themes/markets

Shopify enables merchants to reach international customers across multiple countries and languages. This capability requires theme support for multi-language and multi-currency functionality.

Themes include built-in selectors via the [`localization`](https://shopify.dev/docs/api/liquid/objects/localization) Liquid object and `{% form 'localization' %}` tag. These allow customers to select their preferred currency, language, or both.

For details on implementation, see [Support multiple currencies and languages](https://shopify.dev/docs/storefronts/themes/markets/multiple-currencies-languages).

Shopify Plus merchants benefit from automatic country detection using geolocation to pre-select the most relevant enabled market for each visitor.

You can [adapt your theme content for different markets](https://help.shopify.com/en/manual/online-store/themes/customizing-themes/store-contextualization) to localize the shopping experience.

---

## Markets — Support multiple currencies and languages

> Fonte: https://shopify.dev/docs/storefronts/themes/markets/multiple-currencies-languages

Merchants can enable selling in [multiple currencies](https://help.shopify.com/en/manual/payments/shopify-payments/multi-currency/setup) with Shopify Payments, and [multiple languages](https://help.shopify.com/en/manual/cross-border/multilingual-online-store). This means that customers can browse the shop, and checkout, in their preferred currency and/or language.

In this tutorial, you'll learn how to support multiple currencies and languages in your theme through country and language selectors.

You should also consider the following when dealing with multiple currencies and languages:

* Locale-aware URLs
* Search engine optimization

### Resources

To support multiple currencies and languages in your theme, you'll use the following:

* The [`form` object](https://shopify.dev/docs/api/liquid/objects/form)
* The [`localization` object](https://shopify.dev/docs/api/liquid/objects/localization)

### Implementing country and language selectors

If a merchant has enabled multiple currencies and/or languages, then you should give customers the ability to select their preference. You can build the following components to give customers this ability:

* A country selector
* A language selector

**Plus:** For merchants on the [Shopify Plus](https://www.shopify.com/plus) plan, Shopify will use geolocation to detect where customers are located and automatically select the most relevant country from the options that the merchant has enabled.

You might include a country and/or language selector in your header or footer, or inside of a navigation drawer. For more detailed placement recommendations, and to learn about best practices for styling country and language selectors, refer to the [UX guidelines](https://shopify.dev/docs/storefronts/themes/markets/country-language-ux).

### The country selector

You can build a country selector to allow customers to manually choose their preferred currency. If the currently selected language is not supported by the selected country, it will be updated to the default language for that country.

The selector needs to be placed inside a localization form. This form can be created using the Liquid [`form` tag](https://shopify.dev/docs/api/liquid/tags/form#form-localization) and the `'localization'` parameter.

The selector also needs to contain an input with the attribute `name="country_code"`, whose value will be the selected country.

The shop's enabled countries are accessible through the `available_countries` attribute of the [`localization` object](https://shopify.dev/docs/api/liquid/objects/localization), and the currently selected country is accessible through the `country` attribute.

**Note:** You should only output a country selector if there's more than one available country.

The following example includes a button and a popover containing each country option:

#### Country selector

```liquid
{% if localization.available_countries.size > 1 %}
  <localization-form>
    {% form 'localization' %}
      <div class="disclosure">
        <button type="button" class="disclosure__button" aria-expanded="false" aria-controls="CountryList">
          {{ localization.country.name }} ({{ localization.country.currency.iso_code }} {{ localization.country.currency.symbol }})

          <svg aria-hidden="true" focusable="false" role="presentation" class="icon icon-caret" viewBox="0 0 10 6">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M9.354.646a.5.5 0 00-.708 0L5 4.293 1.354.646a.5.5 0 00-.708.708l4 4a.5.5 0 00.708 0l4-4a.5.5 0 000-.708z" fill="currentColor">
          </svg>
        </button>

        <ul id="CountryList" role="list" class="disclosure__list" hidden>
          {% for country in localization.available_countries %}
            <li class="disclosure__item" tabindex="-1">
              <a href="#"{% if country.iso_code == localization.country.iso_code %} aria-current="true"{% endif %} data-value="{{ country.iso_code }}">
                {{ country.name }} ({{ country.currency.iso_code }} {{ country.currency.symbol }})
              </a>
            </li>
          {% endfor %}
        </ul>

        <input type="hidden" name="country_code" value="{{ localization.country.iso_code }}" />
      </div>
    {% endform %}
  </localization-form>
{% endif %}
```

For an example of JavaScript that manages the visibility of the option list and submits the form on selection, refer to JavaScript submission of the localization form.

**Note:** For a more in-depth example, you can refer to Dawn's implementation in the [`footer.liquid` section](https://github.com/Shopify/dawn/blob/main/sections/footer.liquid).

### The language selector

You can build a language selector to allow customers to manually choose their preferred language.

The selector needs to be placed inside a localization form. This form can be created using the Liquid [`form` tag](https://shopify.dev/docs/api/liquid/tags/form#form-localization) and the `'localization'` parameter.

The selector also needs to contain an input with the attribute `name="language_code"`, whose value will be the selected language.

The available languages are accessible through the `available_languages` attribute of the [`localization` object](https://shopify.dev/docs/api/liquid/objects/localization), and the currently selected language is accessible through the `language` attribute.

**Note:** You should only output a language selector if there's more than one available language.

The following example includes a button and a popover containing each language option:

#### Language selector

```liquid
{% if localization.available_languages.size > 1 %}
  <localization-form>
    {% form 'localization' %}
      <div class="disclosure">
        <button type="button" class="disclosure__button" aria-expanded="false" aria-controls="LanguageList">
          {{ localization.language.endonym_name | capitalize }}

          <svg aria-hidden="true" focusable="false" role="presentation" class="icon icon-caret" viewBox="0 0 10 6">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M9.354.646a.5.5 0 00-.708 0L5 4.293 1.354.646a.5.5 0 00-.708.708l4 4a.5.5 0 00.708 0l4-4a.5.5 0 000-.708z" fill="currentColor">
          </svg>
        </button>

        <ul id="LanguageList" role="list" class="disclosure__list" hidden>
          {% for language in localization.available_languages %}
            <li class="disclosure__item" tabindex="-1">
              <a href="#"{% if language.iso_code == localization.language.iso_code %} aria-current="true"{% endif %} hreflang="{{ language.iso_code }}" lang="{{ language.iso_code }}" data-value="{{ language.iso_code }}">
                {{ language.endonym_name | capitalize }}
              </a>
            </li>
          {% endfor %}
        </ul>

        <input type="hidden" name="language_code" value="{{ localization.language.iso_code }}" />
      </div>
    {% endform %}
  </localization-form>
{% endif %}
```

For an example of JavaScript that manages the visibility of the option list and submits the form on selection, refer to JavaScript submission of the localization form.

**Note:** For a more in-depth example, you can refer to Dawn's implementation in the [`footer.liquid` section](https://github.com/Shopify/dawn/blob/main/sections/footer.liquid).

### JavaScript submission of the localization form

Because your country or language selector is a custom element and there's no submit button included in the form, you need to submit the form through JavaScript.

The following example is based on the previous country and language selector examples:

#### Localization form JavaScript

```js
class LocalizationForm extends HTMLElement {
  constructor() {
    super();
    this.elements = {
      input: this.querySelector('input[name="language_code"], input[name="country_code"]'),
      button: this.querySelector('button'),
      panel: this.querySelector('ul'),
    };
    this.elements.button.addEventListener('click', this.openSelector.bind(this));
    this.elements.button.addEventListener('focusout', this.closeSelector.bind(this));
    this.addEventListener('keyup', this.onContainerKeyUp.bind(this));

    this.querySelectorAll('a').forEach(item => item.addEventListener('click', this.onItemClick.bind(this)));
  }

  hidePanel() {
    this.elements.button.setAttribute('aria-expanded', 'false');
    this.elements.panel.setAttribute('hidden', true);
  }

  onContainerKeyUp(event) {
    if (event.code.toUpperCase() !== 'ESCAPE') return;

    this.hidePanel();
    this.elements.button.focus();
  }

  onItemClick(event) {
    event.preventDefault();
    const form = this.querySelector('form');
    this.elements.input.value = event.currentTarget.dataset.value;
    if (form) form.submit();
  }

  openSelector() {
    this.elements.button.focus();
    this.elements.panel.toggleAttribute('hidden');
    this.elements.button.setAttribute('aria-expanded', (this.elements.button.getAttribute('aria-expanded') === 'false').toString());
  }

  closeSelector(event) {
    const shouldClose = event.relatedTarget && event.relatedTarget.nodeName === 'BUTTON';
    if (event.relatedTarget === null || shouldClose) {
      this.hidePanel();
    }
  }
}

customElements.define('localization-form', LocalizationForm);
```

**Note:** Your default solution should be a custom element that uses JavaScript to help with accessibility, however, you should also include a fallback in case JavaScript is disabled.

### Locale-aware URLs

Stores can have dynamic URLs generated for them when they sell internationally or in multiple languages.

* When an additional locale (language) is published on a domain, Shopify automatically creates a URL path for it. For example, if a shop's primary URL is `shop.com`, and a french (`fr`) locale is published on that domain, then the URL `shop.com/fr` is automatically created.
* When a merchant creates a new market, Shopify creates a URL path for that market. For example, if a shop's primary market is the United States and primary locale is English on `shop.com`, when a Canada market is created, then the URL `shop.com/en-ca` is created.

Given these possible dynamic changes in URL structure, you should avoid hardcoding URLs. If you've hardcoded a URL like `/cart` in a link or Ajax request, then visitors browsing in another language or market context will be forced back to the domain defaults. This means they may see the wrong language or currency. Instead, use the following instructions to build dynamic URLs in Liquid or in JavaScript.

#### In Liquid

Use one of the following approaches to build dynamic URLs with Liquid:

* The `url` attribute of any applicable Liquid objects
* The [routes object](https://shopify.dev/docs/api/liquid/objects/routes)

If a merchant has English and French locales, then the cart URL could be `/cart` or `/fr/cart`, respectively. The following example shows how to link to the cart page in the currently selected locale.

```liquid
<a href="{{ routes.cart_url }}">{{ 'templates.cart.go_to_cart'  | t }}</a>
```

#### In JavaScript

You can build dynamic URLs in JavaScript by basing them off of the dynamic root route accessible on the window object, `window.Shopify.routes.root`. This value will always end in a `/`. For instance, if a merchant has a Canadian market in addition to their primary, `window.Shopify.routes.root` could return `"/en-ca/"` when a visitor is accessing that market's subfolder.

The following example shows how to make an Ajax request to the cart while preserving the current market's pricing:

```javascript
fetch(window.Shopify.routes.root + 'cart.js')
.then(response => response.json())
.then(data => showCartContents(data));
```

### Search engine optimization

In addition to providing options for customers to select a country and/or language, you also need to ensure that search engines return localized content and prices for customers.

Shopify automatically includes [hreflang tags](https://moz.com/learn/seo/hreflang-tag) through the [content_for_header object](https://shopify.dev/docs/api/liquid/objects/content_for_header). You can also return localized prices by including, or extending, structured data in your theme.

**Note:** Any information on this page around search engines and SEO is for general information only. If you have issues related to search results and currency, then contact an SEO expert. You can find Partners with SEO expertise in Shopify's [Partner Directory](https://www.shopify.com/partners/directory).

#### Considerations for structured data

When outputting [structured data](https://developers.google.com/search/docs/guides/intro-structured-data) for products, you need to ensure that the `priceCurrency` property is set to reflect the [cart currency](https://shopify.dev/docs/api/liquid/objects/cart#cart-currency), rather than the shop's currency.

For example:

```liquid
priceCurrency: {{ cart.currency.iso_code }},
```

---

## Markets — Country and language selector UX guidelines

> Fonte: https://shopify.dev/docs/storefronts/themes/markets/country-language-ux

There are two main considerations for including country and language selectors in your theme:

* Where to place the selectors
* How to style the selectors

### Selector placement

The following are the main locations you should place country and language selectors:

* The footer
* Near the customer account links
* Near the cart
* Inside a navigation drawer

Regardless of placement, "if you have both country and language selectors, then they should always be placed together."

**Note:** The example images below only show a country selector, however the same guidelines apply to the language selector.

#### The footer

If you place the selector in the footer, then it should be placed at the top of the sub-footer content, separate from the footer navigation links.

#### Near the customer account links

If the customer account links are placed near the cart, then the selector should also be placed near the cart. The styling of the selector should match the styling of the customer account links.

#### Near the cart

If the customer account links are widely separate from the cart, then the selector should be placed near the cart for better visibility.

"The selector should complement, not compete with, the cart element on a page." If the cart element is on the right-hand side of the page, then the selector should be placed to the left of the cart to maintain ease of access for customers.

#### Inside a navigation drawer

If the selector is inside a navigation drawer, then it should be treated as a utility or footer link, as opposed to a navigation link.

### Selector styling

"Custom selectors should borrow the theme's styling for dropdown selectors as much as possible, including typography, colors, height, and hover states."

You can create a custom component for your selector instead of using a native `select` element. "When building a custom selector, you should implement it as a popover rather than a modal, since a modal can be excessive for cases where only a few options are enabled."

The menu's default hover, focused, selected, and pressed states should match your theme's link patterns. The menu's width should expand to fit its content so that longer strings don't wrap, however, the menu display shouldn't extend beyond the viewport.

#### Country and currency format

"Your selector should include the full country name and include the currency code beside the currency symbol. For example, United States (USD $) and United Kingdom (GBP £)."

---

## Site navigation and search — Overview

> Fonte: https://shopify.dev/docs/storefronts/themes/navigation-search

Customers should be able to easily discover store content. To help with this, you can implement the following methods in your theme:

* **Store navigation**: "Merchants can create menus that highlight store content, which can be featured in places like the header and footer to allow customers to easily browse content."
* **Search functionality**: "Customers are often looking for something specific, so you should provide the option to search the store directly, rather than make customers manually navigate to find what they're looking for."
* **Filtering**: "Merchants can add filtering to collection and search pages to allow customers to further specify the content they want to browse."

Links:

* [Store navigation](https://shopify.dev/docs/storefronts/themes/navigation-search/navigation)
* [Search functionality](https://shopify.dev/docs/storefronts/themes/navigation-search/search)
* [Filtering](https://shopify.dev/docs/storefronts/themes/navigation-search/filtering)

---

## Site navigation and search — Add navigation to your theme

> Fonte: https://shopify.dev/docs/storefronts/themes/navigation-search/navigation

Merchants can create [menus](https://help.shopify.com/manual/online-store/menus-and-links) for their shop navigation, and these menus can be nested to "[create drop-down menus](https://help.shopify.com/manual/online-store/menus-and-links/drop-down-menus)".

In this tutorial, you'll learn how to add navigation to your theme.

### Resources

* The [`linklists` object](https://shopify.dev/docs/api/liquid/objects/linklists)
* The [`linklist` object](https://shopify.dev/docs/api/liquid/objects/linklist)
* The [`link` object](https://shopify.dev/docs/api/liquid/objects/link)

### Implementing Navigation

To add navigation to your theme, you should reference a `linklist` object. Each `linklist` object represents a menu that's defined in the **Online Store** > **Navigation** section of the Shopify admin.

You can use the global `linklists` object to access all of the `linklist` objects in your store by their handle. The default menu in the Shopify admin is the **Main menu**, which can be accessed with its handle `main-menu`.

For example:

```liquid
{% for link in linklists.main-menu.links %}
<!-- menu content -->
{% endfor %}
```

You can let merchants select their own menu using the [`link_list` setting](https://shopify.dev/docs/themes/architecture/settings/input-settings#link_list). You can reference the menu using the setting name, which is the equivalent of a linklist handle:

```liquid
{% for link in section.settings.menu.links %}
<!-- menu content -->
{% endfor %}
```

For each menu link, you should output information such as the title and URL. You might also want to output the link's child links. You can nest links up to three levels deep, and you can access them through the `links` attribute of the `link` object.

For example, if you've created a `link_list` type setting called `menu`, so that merchants can choose the menu they want to use in the header section, then the following code shows how you might output the menu.

**Note:** The following example is only meant to illustrate how to iterate through a linklist and output multiple levels of links. It's not a complete navigation feature.

#### /sections/header.liquid

```liquid
<ul class="menu">
  {% for link in section.settings.menu.links %}
    <li class="menu-link">
      <a href="{{ link.url }}">{{ link.title }}</a>


      {% if link.links.size > 0 %}
        <ul class="menu dropdown-child">
          {% for child_link in link.links %}
            <li class="menu-link">
              <a href="{{ child_link.url }}">{{ child_link.title }}</a>


              {% if child_link.links.size > 0 %}
                <ul class="menu dropdown-grandchild">
                  {% for grandchild_link in child_link.links %}
                    <li class="menu-link">
                      <a href="{{ grandchild_link.url }}">{{ grandchild_link.title }}</a>
                    </li>
                  {% endfor %}
                </ul>
              {% endif %}
            </li>
          {% endfor %}
        </ul>
      {% endif %}
    </li>
  {% endfor %}
</ul>
```

Depending on the kind of navigation you're building, you should include your navigation code in your header or footer sections.

**Tip:** For another example of outputting menus, you can refer to "[Dawn's implementation](https://github.com/Shopify/dawn/blob/main/sections/header.liquid)".

---

## Site navigation and search — Storefront search

> Fonte: https://shopify.dev/docs/storefronts/themes/navigation-search/search

Storefront search is based on query parameters that determine what information is returned, and how it's returned, in the search results. In addition to the search query itself, there are parameters that allow you to customize the search in the following ways:

* Only search for certain resource types
* Choose whether unavailable products are returned, and where in the results
* Enable partial word matches

The query parameters can be used by including inputs in your search form, and they're reflected in the search URL when a search is performed.

**Tip:** To learn more about storefront search functionality and search query options, refer to the [Shopify Help Center](https://help.shopify.com/manual/online-store/storefront-search).

You can also add predictive search to your theme so that suggested results appear immediately as you type into the search field. To learn about predictive search, refer to [Add predictive search to your theme](https://shopify.dev/docs/storefronts/themes/navigation-search/search/predictive-search).

The [Shopify Search & Discovery app](https://apps.shopify.com/search-and-discovery) enables users to customize product recommendation and search results, which can impact results from storefront search and the Ajax [Product Recommendations](https://shopify.dev/docs/api/ajax/reference/product-recommendations) API. To learn about how these results can be impacted, visit the [Shopify Help Center](https://help.shopify.com/manual/online-store/search-and-discovery/product-recommendations).

### Query parameters

Search queries accept the following parameters:

| Query parameter | Type | Required | Description |
| - | - | - | - |
| `q` | String | Yes | The search query. |
| `type` | Comma-separated values | No | Specifies the type of results requested. The possible options are: `product`, `page`, `article`. Defaults to all types. To change the default value, you can use [Search Settings](https://help.shopify.com/manual/online-store/search-and-discovery/settings) in the Search & Discovery app. |
| `page` | Integer | No | Specifies the current search results page. Defaults to `1`. |
| `options` | Hash | No | Specifies search options that you can customize with the `unavailable_products` and `prefix` settings. |
| `unavailable_products` | String | No | Specifies whether to display results for unavailable products or variants in filtered results. The following are the possible options: `show` - Show unavailable products or variants in the order that they're found. `hide` - Exclude unavailable products or variants. `last` - Show unavailable products or variants after all other matching results. Defaults to `last`. To change the default value, you can use [Search Settings](https://help.shopify.com/manual/online-store/search-and-discovery/settings) in the Search & Discovery app. |
| `prefix` | String | No | Specifies whether we want to perform a partial word match on the last search term. For example, if "winter snow" is used as a search query, a search will find all applicable resources that contain both "winter" and any term that starts with "snow". This could be terms like "snow", "snowshoe", or "snowboard". The possible options are: `last` - Perform a partial word match on the last search term. This is the default. `none` - Don't perform a partial word match on the last search term. |
| `sort_by` | String | No | Specifies the sort order of the results. The possible options are: `relevance` - Sort results by relevance to the search query. `price-ascending` - Sort results by price from high to low. All non-product results are pushed to the end of the results array. `price-descending` - Sort results by price from low to high. All non-product results are pushed to the end of the results array. Defaults to `relevance`. |

### The search form

The search form can be included with a `<form>` element that has an attribute of `action="/search"`.

**Tip:** You should use the [`routes` object](https://shopify.dev/docs/api/liquid/objects/routes#routes-search_url) to populate the `action` attribute so that the appropriate URL is used for multi-language stores.

Inside the form, you can include inputs for each of the query parameters above, where each input has the following attributes:

* `name="query-parameter"`
* `value="parameter-value"`

Aside from the `q` parameter, none of the query parameters require user input, so they should be hidden inputs.

#### Example search form

```html
<form action="{{ routes.search_url }}">
  <input type="text"
    placeholder="Search"
    name="q"
    value="{{ search.terms | escape }}"
  />
  <input type="hidden" name="type" value="product,page" />
  <input type="hidden" name="options[unavailable_products]" value="hide" />
  <input type="hidden" name="options[prefix]" value="last" />
  <input type="submit" value="Search" />
</form>
```

**Tip:** For another example of a search form, you can refer to [Dawn's implementation](https://github.com/Shopify/dawn/blob/main/sections/main-search.liquid).

### Search URL structure

When a search is performed, the search page's URL is updated to reflect that.

For example, a search with the following parameters returns the following URL:

| Attribute | Value |
| - | - |
| `q` | `snow` |
| `type` | `product,page` |
| `options[unavailable_products]` | `hide` |
| `options[prefix]` | `last` |

```text
/search?q=snow&type=product,page&options[unavailable_products]=hide&options[prefix]=last
```

---

## Site navigation and search — Add predictive search to your theme

> Fonte: https://shopify.dev/docs/storefronts/themes/navigation-search/search/predictive-search

You can add predictive search to your theme so that suggested results appear immediately as you type into the search field. Predictive search helps customers articulate and refine their search queries, and provides new ways for them to explore an online store. It also lets them quickly browse matches without having to leave their current page to see a separate list of search results.

Predictive search supports suggestions for products, collections, queries, pages, and articles.

Before implementing predictive search in your theme, it's important to be familiar with how suggestions are generated, current API limitations, and the UX guidelines.

### How suggestions are generated

The predictive search dropdown displays the following information when you enter a query.

| Point | Description |
| - | - |
| **1** | Predictive search dropdown |
| **2** | Query suggestions |
| **3** | Collection suggestions |
| **4** | Product suggestions |
| **5** | Page suggestions |
| **6** | Article suggestions |

After you start typing into the search bar, predictive search suggests results that are related to what you're typing. They match search terms either exactly or with typo tolerance on searchable properties of shop resources.

Matching products or variants are returned as product suggestions that drop down from the search bar. For example, you're looking for a snowboard and type `very-fast snowbo`. Product suggestions appear for products or variants that contain `very`, `fast`, and a term that begins with `snowbo`.

If a word is separated by a hyphen or space, then it will be considered as two terms. Words or phrases that are separated into multiple terms return different results than a single term that includes the same words. For example, `T-shirt` and `t shirt` return the same results, but `tshirt` does not.

Product variants are returned only when the query matches terms specific to the variant title. Only the variants with the most matching terms are returned as results. For example, a store has a snowboard with a blue variant and a light blue variant. If you search for `snowbo`, then the snowboard product is returned. However, if you search for `light blue snowbo`, then only the light blue variant is returned.

Query suggestions are generated by extracting words and phrases from your product catalog, as well as from customer searches, using natural language processing techniques.

### Resources

* The [`predictive_search` object](https://shopify.dev/docs/api/liquid/objects/predictive_search)
* The `/{locale}/search/suggest` endpoint of the [Predictive Search API](https://shopify.dev/docs/api/ajax/reference/predictive-search#get-locale-search-suggest)

### Implementing predictive search

To support predictive search, you need to implement the following components:

* **The main search**: A search input for predictive search to apply to.
* **The predictive search section**: A section to host the general predictive search display. This display is populated with the results of the predictive search using the `resources` attribute of the `predictive_search` object.
* **A JavaScript function**: Renders the predictive search section using the section response of the Predictive Search API.

The following examples illustrate a basic predictive search implementation. These examples follow the listbox component pattern suggested by the W3C ARIA authoring practices guide.

**Tip:** For a more in-depth example, refer to the following files in Dawn:

* [sections/main-search.liquid](https://github.com/Shopify/dawn/tree/main/sections/main-search.liquid)
* [sections/predictive-search.liquid](https://github.com/Shopify/dawn/tree/main/sections/predictive-search.liquid)
* [assets/predictive-search.js](https://github.com/Shopify/dawn/tree/main/assets/predictive-search.js)

#### The main search

The main search is a search input for the predictive search functionality to apply to.

##### /sections/main-search.liquid

```liquid
<script src="{{ 'predictive-search.js' | asset_url }}" defer="defer"></script>


<predictive-search>
  <form action="{{ routes.search_url }}" method="get" role="search">
    <label for="Search">Search</label>
    <input
      id="Search"
      type="search"
      name="q"
      value="{{ search.terms | escape }}"
      role="combobox"
      aria-expanded="false"
      aria-owns="predictive-search-results"
      aria-controls="predictive-search-results"
      aria-haspopup="listbox"
      aria-autocomplete="list"
     />
    <input name="options[prefix]" type="hidden" value="last" />


    <div id="predictive-search" tabindex="-1"></div>
  </form>
</predictive-search>
```

#### The predictive search section

The predictive search section hosts the predictive search results. These results are output by looping through the `resources` attribute of the `predictive_search` object.

This section is rendered with the main search using the JavaScript function.

The following example renders the products from the search results. For a more complex template that accepts all resource types, refer to [Dawn's source files](https://github.com/Shopify/dawn/blob/main/sections/predictive-search.liquid).

##### /sections/predictive-search.liquid

```liquid
{%- if predictive_search.performed -%}
  <div id="predictive-search-results">
    {%- if predictive_search.resources.products.size > 0 -%}
      <h3 id="predictive-search-products">
        Products
      </h3>
      <ul role="listbox" aria-labelledby="predictive-search-products">
        {%- for product in predictive_search.resources.products -%}
          <li role="option">
            <a href="{{ product.url }}">
              {{ product | image_url: width: 50 | image_tag }}
              <span>{{ product.title }}</span>
            </a>
          </li>
        {%- endfor -%}
      </ul>
    {%- endif -%}
    <button>
      Search for "{{ predictive_search.terms }}"
    </button>
  </div>
{%- endif -%}
```

#### The JavaScript function

The `predictive_search` object isn't defined when the predictive search section is initially rendered, so you need to retrieve the populated section content using the section response of the Predictive Search API.

The following example uses the default parameters for the Predictive Search API, but you can customize them to fit your needs.

**Tip:** It's recommended to use the Liquid [`routes` object](https://shopify.dev/docs/api/liquid/objects/routes#routes-predictive_search_url) to dynamically set the endpoint URL for the `fetch` call.

##### /assets/predictive-search.js

```js
class PredictiveSearch extends HTMLElement {
  constructor() {
    super();


    this.input = this.querySelector('input[type="search"]');
    this.predictiveSearchResults = this.querySelector('#predictive-search');


    this.input.addEventListener('input', this.debounce((event) => {
      this.onChange(event);
    }, 300).bind(this));
  }


  onChange() {
    const searchTerm = this.input.value.trim();


    if (!searchTerm.length) {
      this.close();
      return;
    }


    this.getSearchResults(searchTerm);
  }


  getSearchResults(searchTerm) {
    fetch(`/search/suggest?q=${searchTerm}&section_id=predictive-search`)
      .then((response) => {
        if (!response.ok) {
          var error = new Error(response.status);
          this.close();
          throw error;
        }


        return response.text();
      })
      .then((text) => {
        const resultsMarkup = new DOMParser().parseFromString(text, 'text/html').querySelector('#shopify-section-predictive-search').innerHTML;
        this.predictiveSearchResults.innerHTML = resultsMarkup;
        this.open();
      })
      .catch((error) => {
        this.close();
        throw error;
      });
  }


  open() {
    this.predictiveSearchResults.style.display = 'block';
  }


  close() {
    this.predictiveSearchResults.style.display = 'none';
  }


  debounce(fn, wait) {
    let t;
    return (...args) => {
      clearTimeout(t);
      t = setTimeout(() => fn.apply(this, args), wait);
    };
  }
}


customElements.define('predictive-search', PredictiveSearch);
```

---

## Site navigation and search — Filtering (overview)

> Fonte: https://shopify.dev/docs/storefronts/themes/navigation-search/filtering

A beneficial capability for e-commerce is allowing customers to narrow product lists by various criteria to facilitate discovery.

Shopify themes support two filtering approaches:

* Storefront filtering
* Tag filtering

### Storefront Filtering

"Storefront filtering is the recommended method for filtering products." It enables merchants to establish filter groups derived from product information such as availability, price, and variant options, applicable to both collections and search results.

For implementation guidance, consult the support documentation and review the user experience considerations specific to this approach.

### Tag Filtering

Product tags enable merchants to partition collections into smaller product subsets. Refer to the tag filtering documentation for detailed implementation instructions.

Links:

* [Support storefront filtering](https://shopify.dev/docs/storefronts/themes/navigation-search/filtering/storefront-filtering/support-storefront-filtering)
* [Storefront filtering UX considerations](https://shopify.dev/docs/storefronts/themes/navigation-search/filtering/storefront-filtering/storefront-filtering-ux)
* [Filter collections by tag](https://shopify.dev/docs/storefronts/themes/navigation-search/filtering/tag-filtering)
* [Storefront filtering overview](https://shopify.dev/docs/storefronts/themes/navigation-search/filtering/storefront-filtering)

---

## Site navigation and search — Storefront filtering (overview)

> Fonte: https://shopify.dev/docs/storefronts/themes/navigation-search/filtering/storefront-filtering

Storefront filtering is the recommended method for filtering products in a theme. It allows merchants to easily create filters for filtering collection and search results pages.

Filters can be based on the following product and variant data:

* Availability
* Category
* Price
* Product tags
* Product type
* Vendor
* Variant options
* Metafields

Filters are applied with `AND` logic, and filter values with `OR`. For example, you can return products that are a specific color *and* a specific size, or you can return products that are one color *or* another.

When filters are applied, they're reflected in the collection or search URL through URL parameters.

### Implementing Storefront Filtering

Use the following resources to learn how to implement storefront filtering in your theme.

* [Support Storefront Filtering](https://shopify.dev/docs/storefronts/themes/navigation-search/filtering/storefront-filtering/support-storefront-filtering) - Learn how to support storefront filtering in your theme.
* [Storefront Filtering UX](https://shopify.dev/docs/storefronts/themes/navigation-search/filtering/storefront-filtering/storefront-filtering-ux) - Familiarize yourself with UX considerations for storefront filtering.

### Filter URL Parameters

Applied filters are reflected in the page URL with URL parameters based on the filter type. These URL parameters have a specific structure.

**Note:** Before filters can be applied, they need to be created in the Shopify admin.

#### URL Parameter Structure

Filter URL parameters consist of the following components:

| Component | Required | Description |
| - | - | - |
| `filter` | Yes | The default namespace for filter URL parameters. |
| `filter_scope` | Yes | The scope of the filter. Can be either: `p` (product level) or `v` (variant level). |
| `attribute` | Yes | The attribute the filter is based on. Refer to Filter types for available attributes. |
| `attribute_scope` | No | The attribute scope for `option` and `price` attributes. Refer to Variant-specific filters for details. |
| `value` | Yes | The filter value. Refer to Filter types for value format details. |

Depending on the filter `attribute`, the format of the URL parameter can be one of the following:

```text
filter.filter_scope.attribute=value
filter.filter_scope.attribute.attribute_scope=value
```

For example, if you had the following filters:

* A filter based on the `shoes` product type
* A filter based on the **Color** variant option, with a value of `red`

Then the URL parameters for each would be the following:

```text
filter.p.product_type=shoes
filter.v.option.color=red
```

If these filters were applied to the `all` collection, then the collection URL would be the following:

```text
/collections/all?filter.p.product_type=shoes&filter.v.option.color=red
```

##### Multiple Filters

You can have multiple filters like the following:

```text
filter.v.option.color=red&filter.v.option.size=L
```

You can also filter on multiple values from the same filter. This can be done in two ways:

* Include multiple values in a single parameter
* Include a parameter for each value

##### Example

```text
filter.v.option.color=red,blue
filter.v.option.color=red&filter.v.option.color=blue
```

#### Filter Types

Filters can be applied at two levels:

* The product level
* The variant level

##### Product-Specific Filters

The following outlines the product-specific filters and how they're reflected as a URL parameter:

| Name | Description | Parameter Name | Accepted Parameter Value |
| - | - | - | - |
| Category | Filter based on specific product categories. | `t.category` | A single category ID or a `__` separated list of category IDs. For example, `aa-1`, or `aa-1__aa-2`. |
| Product tags | Filter based on specific product tags. | `tag` | A single product tag, or a comma-separated list of product tags. For example `new`, or `new,trending`. |
| Product type | Filter based on specific product types. | `product_type` | A single product type, or a comma-separated list of product types. For example `shoes`, or `shoes,belts`. |
| Vendor | Filter based on specific vendors. | `vendor` | A single vendor, or a comma-separated list of vendors. For example `vendor1`, or `vendor1,vendor2`. |
| Metafield | Filter based on a specific product metafield. Metafield-based filters can reference metafields of types: `single_line_text_field`, `list.single_line_text_field`, `metaobject_reference`, `list.metaobject_reference`, `number_integer`, `number_decimal`, or `boolean`. Metafield-based filters also need to specify the metafield namespace and key for the `attribute_scope` component. For example, if your metafield has a namespace of `custom` and key of `made_in`, then the structure would be: `m.custom.made_in` | `m` | A single metafield value, or a comma-separated list of metafield values. For example, `canada` or `canada,usa`. **Note:** A comma-separated list of metafield values is a list of individual metafield values, not a single metafield value that contains a comma-separated list. |

**Note:** Users can create up to a maximum of 25 filters.

The following is an example of the full URL parameter structure for the product-specific filters:

```text
// Product tag
filter.p.tag=new,trending

// Product type
filter.p.product_type=shoes

// Product vendor
filter.p.vendor=vendor1

// Product metafield
filter.p.m.custom.made_in=canada
```

##### Variant-Specific Filters

The following outlines the variant-specific filters and how they're reflected as a URL parameter:

| Name | Description | Parameter Name | Accepted Parameter Value |
| - | - | - | - |
| Availability | Filter based on variant availability. | `availability` | Either: `0` (out of stock), `1` (in stock), or `0,1` (either stock status). |
| Variant option | Filter based on a variant option, such as **Size** or **Color**. Variant option filters also need to specify the option name for the `attribute_scope` component. For example, `option.color`. | `option` | A single variant option value, or a comma-separated list of variant option values. For example `red`, or `red,blue`. |
| Price | Filter based on variant price. Price filters also need to specify the price condition for the `attribute_scope` component. Accepted values: `lte` (prices less than or equal to the entered value) or `gte` (prices greater than or equal to the entered value). | `price` | A single monetary value in the format of the shop's default currency. For example `5` or `20.40`. |
| Standard product attribute | Filter based on a product metafield generated for a standard product attribute that can be connected to product options. Standard product attribute metafield-based filters reference standard metafields of type `list.metaobject_reference`. Standard product attribute metafield-based filters also need to specify the `shopify` namespace and key for the `attribute_scope` component. For example, if your standard product attribute metafield has the key `fabric`, then the structure would be `t.shopify.fabric`. | `t` | A single metaobject GID, a comma-separated list of metaobject GIDs, a single taxonomy value GID, or a comma-separated list of taxonomy value GIDs. For example, `gid://shopify/Metaobject/1` or `gid://shopify/Metaobject/1, gid://shopify/Metaobject/3`. |
| Metafield | Filter based on a specific variant metafield. Metafield-based filters can reference metafields of types: `single_line_text_field`, `list.single_line_text_field`, `metaobject_reference`, `list.metaobject_reference`, `number_integer`, `number_decimal`, or `boolean`. Metafield-based filters also need to specify the metafield namespace and key for the `attribute_scope` component. For example, if your metafield has a namespace of `custom` and key of `fabric`, then the structure would be: `m.custom.fabric` | `m` | A single metafield value, or a comma-separated list of metafield values. For example, `leather` or `leather,suede`. **Note:** A comma-separated list of metafield values is a list of individual metafield values, not a single metafield value that contains a comma-separated list. |

**Note:** Users can create up to a maximum of 25 filters.

The following is an example of the full URL parameter structure for the variant-specific filters:

```text
// Variant availability
filter.v.availability=1

// Variant price
filter.v.price.lte=5

// Variant option
filter.v.option.color=red

// Standard product attribute
filter.v.t.shopify.fabric=gid://shopify/Metaobject/1

// Variant metafields
filter.v.m.custom.fabric=leather
```

**Tip:** When variant-specific filters are applied, the `featured_media` and `url` attributes of the product object are updated to reflect the first variant that matches the current filters. The `featured_media` attribute returns the featured media of the first matching variant with media included, and the `url` attribute is updated to deep link the first matching variant.

---

## Site navigation and search — Support storefront filtering

> Fonte: https://shopify.dev/docs/storefronts/themes/navigation-search/filtering/storefront-filtering/support-storefront-filtering

Storefront filtering allows merchants to easily create filters for filtering collection and search results pages. Filters are based on existing product data, like availability, price, variant options, and more.

In this tutorial, you'll learn how to support storefront filtering in your theme.

### Resources

To implement storefront filtering, you'll use the following:

* The `filter` object
* One of the following, depending on the page you're working with:
  * The `collection` object
  * The `search` object

### Implementing storefront filtering

To support storefront filtering, you need to implement a filter display for customers to interact with.

Applied filters are reflected through URL parameters, so you should also familiarize yourself with the structure of filter URL parameters.

**Note:** Before filters can be applied, they need to be created in the Shopify admin.

### The filter display

**Note:** Collections that contain over 5,000 products don't display filters.

The following sections outline a basic collection and search results filter implementation. Each implementation uses a form to host the filter inputs with "submit" buttons to apply the associated filters. However, you can use JavaScript to automatically submit the form based on input changes. When the form is submitted, the page is refreshed with the filters applied.

For a more in-depth solution, refer to Dawn's implementation on GitHub.

**Tip:** Refer to Storefront filtering UX guidelines for more information on UX best practices when building a filter display.

#### Collection filter display

The collection filter display should be included in the `collection` template, or a section that's included as part of the `collection` template.

The following example implementation contains two main components:

* A list of filter groups and values.
* A list of active filters, if there are any.

  Each of these components are output through the `filters` attribute of the `collection` object, and the associated `filter` objects.

##### Example collection filter display

```liquid
<form>
  {%- for filter in collection.filters -%}
    <details>
      <summary>
        <div>
          <span>{{ filter.label }}</span>


          {%- if filter.active_values.size > 0 -%}
            <span>({{ filter.active_values.size }})</span>
          {%- endif -%}
        </div>
      </summary>


      <div>
        <div>
          <p>{{ filter.active_values.size }} selected</p>
          {%- if filter.active_values.size > 0 -%}
            <p><a href="{{ filter.url_to_remove }}">Reset</a></p>
          {%- endif -%}
        </div>
        {%- case filter.type -%}
          {%- when 'boolean' -%}
            <ul>
                <li>
                  <label for="Filter-{{ filter.param_name }}-{{ filter.true_value.value }}">
                  <input type="checkbox"
                    name="{{ filter.param_name }}"
                    value="{{ filter.true_value.value }}"
                    id="Filter-{{ filter.param_name }}"
                    {% if filter.true_value.active -%}checked{%- endif %}
                    {% if filter.true_value.count == 0 and filter.true_value.active == false -%}disabled{%- endif -%}
                   />{{ filter.true_value.label }}</label>
                </li>
                <li>
                  <label for="Filter-{{ filter.param_name }}-{{ filter.false_value.value }}">
                  <input type="checkbox"
```

> Nota: l'esempio nella documentazione originale è troncato in questo punto; il pattern prosegue gestendo gli altri tipi di filtro (`list`, `price_range`) tramite `{%- case filter.type -%}`. Per l'implementazione completa fare riferimento all'implementazione di Dawn su GitHub.

#### Search results filter display

**Note:** Search results that exceed 1,000 products don't display filters.

The search results filter display should be included in the `search` template, or in a section that's included as part of the `search` template.

The following example implementation contains two main components:

* A list of filter groups and values.
* A list of active filters, if there are any.

  Each of these components are output through the `filters` attribute of the `search` object, and the associated `filter` objects.

  If you apply filters on the search results page, then all non-product results are filtered out.

##### Example search results filter display

```liquid
<form>
  <input type="hidden" name="q" value="{{ search.terms }}" />


  {%- for filter in search.filters -%}
    <details>
      <summary>
        <div>
          <span>{{ filter.label }}</span>


          {%- if filter.active_values.size > 0 -%}
            <span>({{ filter.active_values.size }})</span>
          {%- endif -%}
        </div>
      </summary>


      <div>
        <div>
          <p>{{ filter.active_values.size }} selected</p>
          {%- if filter.active_values.size > 0 -%}
            <p><a href="{{ filter.url_to_remove }}">Reset</a></p>
          {%- endif -%}
        </div>
        {%- case filter.type -%}
          {%- when 'boolean' -%}
            <ul>
                <li>
                  <label for="Filter-{{ filter.param_name }}-{{ filter.true_value.value }}">
                  <input type="checkbox"
                    name="{{ filter.param_name }}"
                    value="{{ filter.true_value.value }}"
                    id="Filter-{{ filter.param_name }}"
                    {% if filter.true_value.active -%}checked{%- endif %}
                    {% if filter.true_value.count == 0 and filter.true_value.active == false -%}disabled{%- endif -%}
                   />{{ filter.true_value.label }}</label>
                </li>
                <li>
```

> Nota: anche questo esempio nella documentazione originale è troncato; il pattern prosegue come nel filtro collezione. Riferirsi all'implementazione di Dawn per la versione completa.

---

## Site navigation and search — Storefront filtering UX guidelines

> Fonte: https://shopify.dev/docs/storefronts/themes/navigation-search/filtering/storefront-filtering/storefront-filtering-ux

Storefront filtering is an essential component to the customer experience as it helps them find what they're looking for faster, which can help increase conversions for merchants.

The following outlines some key considerations related the filtering experience.

To learn how to implement a basic version of storefront filtering, refer to [Support storefront filtering](https://shopify.dev/docs/storefronts/themes/navigation-search/filtering/storefront-filtering/support-storefront-filtering).

### Provide the right interface for each filter type

There are two filter types:

* List
* Price range

#### List

It's recommended to use a set of checkbox inputs for filters of type `list` to make it obvious that multiple values can be selected at once.

#### Price range

It's recommended to use a dual-handled slider for filters of type `price_range`, however you should also include number input fields for the "start" and "end" values of the range to account for accessibility. You should ensure that the fields number fields have labels, such as "From" and "To", even if they're visually hidden.

### Provide a choice of filter layout

There are two standard layouts for filtering on larger screens:

* A horizontal toolbar above the product list
* A vertical sidebar to the left of the product list

In order to provide flexibility for varying merchant needs, you should consider providing both layouts as an option behind a theme setting.

#### Horizontal toolbar filters

A horizontal toolbar above the product list can provide a compact entry point to both filtering and sorting, but works best for smaller stores that need less than five filters at a time.

#### Vertical sidebar filters

A vertical sidebar to the left of the product list works best for stores with more than five filters.

### Provide a clear visual hierarchy

You should style filters to make relationships clear. For example, the name of each filter group should stand out from its values, and there should be a clear separation between filter groups.

### Avoid dead ends

"Customers shouldn't end up with zero results." As such, you should always show the count of results with each filter value, and disable any values that have zero results.

### Show applied filters

If a customer lands on a page with filters already applied, they need to be able to see which filters have been applied. Similarly, if a customer adds a filter, they need feedback that it applied.

In both of the above scenarios, customers should have an easy way to remove an individual filter, or clear all filters.

Often, filter values are clear enough that applied filter labels can just display the value, such as "Shoe" or "In stock". However, sometimes it may not be clear which filter a value applies to, such as having filters for both "Width" and "Height".

To account for this possibility, you should add a theme setting to allow merchants to include the filter group name with the filter value.

### Manage filter groups

In vertical sidebars, you should consider collapsing filter groups after the first five. This makes it easier to scan for the desired filter group with minimal scrolling.

### Manage filter values

Filter groups can display up to 100 values, so you should truncate the list to 10 values with the option to show more. The first 10 values likely aren't the most relevant, so if possible, you should show the 10 most relevant values.

### Optimize for mobile

In general, the filter interface on mobile should be moved into a drawer or modal. With that, there are two standard options for surfacing that interface:

* A single button
* A horizontally scrolling filter group list

#### Filter button

With the main filtering interface inside a drawer or modal, you can include a "filter" button to show it.

#### Horizontal filter group list

With the main filtering interface inside a drawer or modal, you can provide quick access to filter groups with a horizontally scrolling list of filter groups, where each group will open the associated filters in a modal. You should also consider having a "filter" button like the previous example as a fallback.

### Use progressive enhancement

"In order to build lean, fast themes, you should implement as much as you can without JavaScript." For filters, this means using links, or forms with manual submit buttons, to apply selected filters.

JavaScript can be layered onto the basic implementation to enhance the experience, such as live-updating the product grid.

---

## Site navigation and search — Filter collections by tag

> Fonte: https://shopify.dev/docs/storefronts/themes/navigation-search/filtering/tag-filtering

**Note:** Consider using [storefront filtering](https://shopify.dev/docs/storefronts/themes/navigation-search/filtering/storefront-filtering) instead of filtering by tag. Storefront filtering enables merchants to create filters based on existing product data without manually building a tag system. It also applies to search results in addition to collections.

You can use [product tags](https://shopify.dev/docs/api/liquid/objects/product#product-tags) to filter a collection into smaller subsets of products.

### How tag filtering works

Tag filters are applied by appending `/[tag-handle]` to the collection URL, where `[tag-handle]` is the [handleized](https://shopify.dev/docs/api/liquid/filters/handleize) version of the desired product tag.

For example, to show products from the `frontpage` collection tagged with `new`, use this URL structure:

```text
{shop}.myshopify.com/collections/frontpage/new
```

You can filter by multiple tags by combining the handleized tags with a `+`:

```text
{shop}.myshopify.com/collections/frontpage/new+sale
```

"Tag filtering uses the AND operator, so only products that have both `new` and `sale` are shown." If no products match all tags, customers see a page with no results.

#### Redirecting unused product tags

"If a tag in the URL isn't used on any of the store's products, then Shopify redirects to a collection URL with the tag removed." For example, if `summer-sale` is removed from all products, customers visiting `{shop}.myshopify.com/collections/frontpage/summer-sale` redirect to `{shop}.myshopify.com/collections/frontpage`.

When multiple tag handles exist in the URL, "only the tags not applicable to any products in the store are removed and the rest are kept in the redirect URL."

This behavior supports displaying products when customers follow outdated collection links or mistype a tag handle.

### Implementing tag filtering

The tag filter display should be included in the [`collection` template](https://shopify.dev/docs/storefronts/themes/architecture/templates/collection), or through a section included in the `collection` template.

To implement tag filtering in your Liquid template, loop through all product tags using the [`all_tags` object](https://shopify.dev/docs/api/liquid/objects/collection#collection-all_tags) of the `collection` object. For each tag, check for its presence in the [`current_tags` object](https://shopify.dev/docs/api/liquid/objects/current_tags), then output a link to add or remove it using these [URL tag filters](https://shopify.dev/docs/api/liquid/filters/tag-filters):

* `link_to_add_tag`
* `link_to_remove_tag`

#### Example tag filtering

```liquid
{% if collection.all_tags.size > 0 %}
  <ul class="tag-filters">
    {% for tag in collection.all_tags %}
      {% if current_tags contains tag %}
        <li class="tag-filters__item active">{{ tag | link_to_remove_tag: tag }}</li>
      {% else %}
        <li class="tag-filters__item">{{ tag | link_to_add_tag: tag }}</li>
      {% endif %}
    {% endfor %}
  </ul>
{% endif %}
```

---

## SEO — Overview

> Fonte: https://shopify.dev/docs/storefronts/themes/seo

Search engine optimization (SEO) enables customers to discover merchant shops through search engines like Google. These best practices help ensure your theme includes necessary SEO data.

### In this section

* **[Add SEO metadata to your theme](https://shopify.dev/docs/storefronts/themes/seo/metadata)** — Learn how to add metadata to your theme to allow search engines to find key information about the site.
* **[Customize robots.txt](https://shopify.dev/docs/storefronts/themes/seo/robots-txt)** — Learn how to customize robots.txt to control which pages search engine crawlers can access.
* **[Use hreflang tags in your theme](https://shopify.dev/docs/storefronts/themes/seo/hreflang)** — Learn how to use hreflang tags in your theme to allow search engines to surface regionalized and translated content.

---

## SEO — Add SEO metadata to your theme

> Fonte: https://shopify.dev/docs/storefronts/themes/seo/metadata

You can include search engine optimization (SEO) metadata in your theme using HTML and Liquid. There are three main aspects to consider:

* The title tag
* The meta description
* Canonical URLs

The code for the above SEO metadata should be included in the `<head>` element.

For example:

### layouts/theme.liquid

```liquid
<head>
  <title>
    {{ page_title -}}
    {%- if current_tags %} &ndash; tagged "{{ current_tags | join: ', ' }}"{% endif -%}
    {%- if current_page != 1 %} &ndash; Page {{ current_page }}{% endif -%}
    {%- unless page_title contains shop.name %} &ndash; {{ shop.name }}{% endunless -%}
  </title>


  {% if page_description %}
    <meta name="description" content="{{ page_description | escape }}" />
  {% endif %}


  <link rel="canonical" href="{{ canonical_url }}" />
</head>
```

**Tip:** For another example of including metadata in a theme, you can refer to [Dawn's implementation](https://github.com/Shopify/dawn/blob/main/layout/theme.liquid).

### The title tag

You can include a `<title>` element for search engines to read the page title from. The title for most pages can be set in the Shopify admin, and you can access this title with the Liquid [page_title object](https://shopify.dev/docs/api/liquid/objects/page_title).

### The meta description

You can include a `<meta />` element for search engines to read the page description from. The description for most pages can be set in the Shopify admin, and you can access this description with the Liquid [page_description object](https://shopify.dev/docs/api/liquid/objects/page_description).

### Canonical URLs

You can specify a canonical URL for a given page using the global Liquid [canonical_url object](https://shopify.dev/docs/api/liquid/objects/canonical_url).

---

## SEO — Customize robots.txt

> Fonte: https://shopify.dev/docs/storefronts/themes/seo/robots-txt

The `robots.txt` file tells search engines which pages can, or can't, be crawled on a site. It contains groups of rules for doing so, and each group has three main components:

* The user agent, which notes which crawler the group of rules applies to. For example, `adsbot-google`.
* The rules themselves, which note specific URLs that crawlers can, or can't, access.
* An optional sitemap URL.

**Tip:** To learn more about `robots.txt` and rule-set components, refer to [Google's documentation](https://developers.google.com/search/docs/advanced/robots/intro).

Shopify generates a default `robots.txt` file that works for most stores. However, you can add the [`robots.txt.liquid` template](https://shopify.dev/docs/storefronts/themes/architecture/templates/robots-txt-liquid) to make customizations.

In this tutorial, you'll learn how you can customize the `robots.txt.liquid` template.

### Requirements

Add the `robots.txt.liquid` template with the following steps:

1. In the code editor for the theme you want to edit, locate the **Templates** folder.
2. Right-click on the **Templates** folder.
3. Click **New File** from the context menu.
4. Name the file `robots.txt.liquid`.
5. Press Enter to create the file.

### Resources

The `robots.txt.liquid` template supports only the following Liquid objects:

* [`robots`](https://shopify.dev/docs/api/liquid/objects/robots)
* [`group`](https://shopify.dev/docs/api/liquid/objects/group)
* [`rule`](https://shopify.dev/docs/api/liquid/objects/rule)
* [`user_agent`](https://shopify.dev/docs/api/liquid/objects/user_agent)
* [`sitemap`](https://shopify.dev/docs/api/liquid/objects/sitemap)
* [`request`](https://shopify.dev/docs/api/liquid/objects/request)

### Customize `robots.txt.liquid`

You can make the following customizations:

* Add a new rule to an existing group
* Remove a rule from an existing group
* Add custom rules

**Tip:** The examples below make use of Liquid's [whitespace control](https://shopify.dev/docs/api/liquid/basics/whitespace) in order to maintain standard formatting.

While you can replace all of the template content with plain text rules, it's strongly recommended to use the provided Liquid objects whenever possible. The default rules are updated regularly to ensure that SEO best practices are always applied.

#### Add a new rule to an existing group

If you want to add a new rule to an existing group, then you can adjust the Liquid for outputting the default rules to check for the associated group and include your rule.

For example, you can use the following to block all crawlers from accessing pages with the URL parameter `?q=`:

```liquid
{% for group in robots.default_groups %}
  {{- group.user_agent }}


  {%- for rule in group.rules -%}
    {{ rule }}
  {%- endfor -%}


  {%- if group.user_agent.value == '*' -%}
    {{ 'Disallow: /*?q=*' }}
  {%- endif -%}


  {%- if group.sitemap != blank -%}
	  {{ group.sitemap }}
  {%- endif -%}
{% endfor %}
```

##### Add host-specific rules

If you're using multiple domains for different markets, then you can create host-specific rules using the `request.host` object. You should only implement host-specific rules if you're using [Shopify Markets](https://shopify.dev/docs/storefronts/themes/markets) and you have distinct domains or subdomains that require different crawling behaviors per market.

For example, you could block crawling of English content on a French domain while maintaining default rules:

```liquid
{% for group in robots.default_groups %}
  {{- group.user_agent }}


  {%- for rule in group.rules -%}
    {{ rule }}
  {%- endfor -%}


  {%- if request.host == 'example.fr' -%}
    {{ 'Disallow: /en/' }}
  {%- endif -%}


  {%- if group.sitemap != blank -%}
	  {{ group.sitemap }}
  {%- endif -%}
{% endfor %}
```

#### Remove a default rule from an existing group

If you want to remove a default rule from an existing group, then you can adjust the Liquid for outputting the default rules to check for that rule and skip over it.

For example, you can use the following to remove the rule blocking crawlers from accessing the `/policies/` page:

```liquid
{% for group in robots.default_groups %}
  {{- group.user_agent }}


  {%- for rule in group.rules -%}
    {%- unless rule.directive == 'Disallow' and rule.value == '/policies/' -%}
      {{ rule }}
    {%- endunless -%}
  {%- endfor -%}


  {%- if group.sitemap != blank -%}
	  {{ group.sitemap }}
  {%- endif -%}
{% endfor %}
```

#### Add custom rules

If you want to add a new rule that's not part of a default group, then you can manually enter the rule outside of the Liquid for outputting the default rules.

Common examples of these custom rules are:

* Block certain crawlers
* Allow certain crawlers
* Add extra sitemap URLs

##### Block certain crawlers

If a crawler isn't in the default rule set, then you can manually add a rule to block it.

For example, the following directive would allow you to block the `discobot` crawler:

```text
<!-- Liquid for default rules -->


User-agent: discobot
Disallow: /
```

##### Allow certain crawlers

Similar to blocking certain crawlers, you can also manually add a rule to allow search engines to crawl a subdirectory or page.

For example, the following directive would allow the `discobot` crawler:

```text
<!-- Liquid for default rules -->


User-agent: discobot
Allow: /
```

##### Add extra sitemap URLs

The following example, where `[sitemap-url]` is the sitemap URL, would allow you to include an extra sitemap URL:

```text
<!-- Liquid for default rules -->


Sitemap: [sitemap-url]
```

---

## SEO — Use hreflang tags in your theme

> Fonte: https://shopify.dev/docs/storefronts/themes/seo/hreflang

This guide describes how to use hreflang tags in your theme to allow search engines to surface regionalized and translated content.

### How it works

When search engines crawl websites, they look for hreflang tags to determine the language and region that the website is intended for, and then use that to serve the correct URL based on a user's language and location.

For example, if a store has a default URL of `your-store.myshopify.com`, and a Spanish language version of `es.your-store.myshopify.com`, then including hreflang tags in your theme will ensure that a customer located in Spain, or with a Spanish language setting, will be served the Spanish URL.

### hreflang tags in theme.liquid

An hreflang tag is a `link` element that identifies a localized URL of a website. You should add a unique hreflang tag for each language or region URL that exists, and they should be included in the `<head>`, which is commonly found in `theme.liquid`:

#### layout/theme.liquid

```html
<head>
  <!-- head element content -->

  <link rel="alternate" hreflang="en" href="your-store.myshopify.com" />
  <link rel="alternate" hreflang="es" href="es.your-store.myshopify.com" />
</head>
```

The following examples show how to add hreflang tags to collection and product pages:

#### layout/theme.liquid

```html
<head>
  <!-- head element content -->

  <link rel="alternate" hreflang="en" href="your-store.myshopify.com/collections/{collection-name}" />
  <link rel="alternate" hreflang="es" href="es.your-store.myshopify.com/collections/{collection-name}" />
</head>
```

#### layout/theme.liquid

```html
<head>
  <!-- head element content -->

  <link rel="alternate" hreflang="en" href="your-store.myshopify.com/products/{product-name}" />
  <link rel="alternate" hreflang="es" href="es.your-store.myshopify.com/products/{product-name}" />
</head>
```

### Next steps

* Learn more about using hreflang tags in multilingual stores
* Refer to Google's documentation to learn more about hreflang tags and how to use them

---

## Trust and security — Overview

> Fonte: https://shopify.dev/docs/storefronts/themes/trust-security

Trust and security represent key considerations for theme development, affecting both merchant operations and customer confidence. "Trust and security are important aspects of a theme for both merchants, and customers."

The page addresses two primary protective mechanisms:

1. **Spam Protection**: Shopify implements captcha technology on customer, contact, and blog comment forms to protect merchants from unwanted submissions.
2. **Customer Assurance**: Security badges are available to demonstrate compliance with Payment Card Industry (PCI) standards, helping customers trust the merchant's shop security practices.

Links:

* [Captcha](https://shopify.dev/docs/storefronts/themes/trust-security/captcha)
* [Security Badges](https://shopify.dev/docs/storefronts/themes/trust-security/security-badges)

---

## Trust and security — CAPTCHA

> Fonte: https://shopify.dev/docs/storefronts/themes/trust-security/captcha

Shopify uses [hCaptcha](https://hcaptcha.com) to help prevent spam through customer, contact, and blog comment forms.

Initially, hCaptcha analyzes website visitor behavior to provide a score indicating the likelihood of the visitor being a bot, without requiring the visitor to solve an interactive challenge.

If the assessment result is suspicious enough, or if too many requests are made within a short period of time, then the visitor is redirected to the `/challenge` page to perform an interactive challenge for further assessment.

Merchants are able to [disable hCaptcha functionality](https://help.shopify.com/manual/online-store/setting-up/preferences#enable-or-disable-recaptcha-on-online-store) on the **Online Store** > **Preferences** page in the Shopify admin.

### How CAPTCHA is included in themes

The necessary code for the CAPTCHA functionality is included through the [`content_for_header` object](https://shopify.dev/docs/api/liquid/objects/content_for_header). This means that if a merchant has CAPTCHA enabled, but the `content_for_header` object isn't present, then the CAPTCHA functionality won't be present.

The CAPTCHA functionality is initialized based on the presence of customer, contact, and blog comment forms, and by default is triggered when the forms are interacted with. For example, the functionality is triggered when a user clicks a text field of an associated form.

These forms are identified based on the `action` attribute of the form, as well as specific input attributes:

| Form type | Form `action` attribute | Input attributes (included on a single input) |
| - | - | - |
| Customer | Contains `/account` | `name="form_type"` One of the following, depending on the form: `value="customer_login"`, `value="create_customer"`, or `value="recover_customer_password"` |
| Contact | Contains `/contact` | `name="form_type"` One of the following, depending on the form: `value="contact"` or `value="customer"` |
| Blog | Contains `/blogs` | `name="form_type"` and `value="new_comment"` |

**Tip:** The form `action` attribute and associated input attributes are output by default when using a relevant Liquid [form tag](https://shopify.dev/docs/api/liquid/tags/form). If your theme uses custom forms, then make sure that the above attributes are included so that your forms are compatible with CAPTCHA functionality.

#### Example

```html
<form action="/account/login" ...>
  <input type="hidden" name="form_type" value="customer_login" />
  ...
</form>
```

In addition to triggering the CAPTCHA functionality on user interaction, a CAPTCHA logo is added to the bottom right corner of the page to notify visitors of the behavior analysis. You can opt to show a text disclaimer with the form instead.

### Show a text disclaimer

If CAPTCHA is enabled and CAPTCHA has loaded, then the CAPTCHA logo appears in the bottom right corner of any associated pages. You can choose to show a text disclaimer with the form, rather than this logo.

To do this, you need to include the following code within any forms you wish to change this for:

```liquid
{{ 'shopify.online_store.spam_detection.disclaimer_html'  | t }}
```

### Advanced: Forcing CAPTCHA wire up to a form

**Caution:** To keep your integration compatible with Shopify's form abuse protection mechanisms, avoid working directly with the underlying CAPTCHA libraries. For example, don't call methods on `window.hCaptcha`. Instead, use the following supported methods.

In some scenarios, it might be necessary to force CAPTCHA wire up to a form. For example, the form might be indirectly populated and submitted, so the default behavior of wiring CAPTCHA on user interaction never happens. In these cases, you have the following options:

#### Wire up using a data attribute

Adding the `data-shopify-captcha` attribute with a value of `true` causes CAPTCHA to wire up to the form immediately when the page loads.

##### Data attribute example (Liquid)

```liquid
{%- form 'customer_login', data-shopify-captcha: "true" -%}
```

##### Data attribute example (HTML)

```html
<form data-shopify-captcha="true" action="/account/login" ...>
  <input type="hidden" name="form_type" value="customer_login" />
  ...
</form>
```

#### Wire up using JavaScript

Alternatively, CAPTCHA can be wired up to a form using JavaScript. `window.Shopify.captcha.protect` should be invoked with the form that you want to wire up as the first argument, and with an optional callback function as the second argument. If provided, the callback is invoked after CAPTCHA is ready.

This is primarily useful in cases where you programmatically manipulate and submit the form in response to other user action.

##### JavaScript example

```javascript
const myForm = document.querySelector('#my-form');
window.Shopify.captcha.protect(myForm, () => {
  myForm.elements["contact[email]"].value = 'test@example.com';
  myForm.submit();
});
```

### Verifying that hCaptcha is wired up

You can verify that hCaptcha is correctly wired to your form by using your browser's network dev tools while the form is being submitted.

1. Open dev tools on the **Network** tab.
2. Fill in and submit the form.
3. In the browser's dev tools, inspect the payload of the POST request to the server.
4. Ensure that the `h-captcha-response` field is present and contains data.

### Troubleshooting

* Ensure that your theme includes Liquid's [`content_for_header`](https://shopify.dev/docs/api/liquid/objects/content_for_header) object in layouts that contain forms that require hCaptcha. Ensure that no code modifies or changes this object.
* If you want your form to be automatically wired up, ensure that its markup is correct, with the requisite `action` attribute and corresponding `form_type` child input. For more information, refer to how CAPTCHA is included in themes.
* By default, hCaptcha is initialized on the [`DOMContentLoaded`](https://developer.mozilla.org/en-US/docs/Web/API/Document/DOMContentLoaded_event) event, but is only wired up when the user interacts with the form. If you're building or submitting forms programmatically or adding them to the DOM after the `DOMContentLoaded` event has been emitted, then you might need to use `window.Shopify.captcha.protect` to ensure that CAPTCHA executes correctly.
* Some third-party applications may block hCaptcha resources, or otherwise manipulate the DOM in ways that cause hCaptcha to not wire up correctly. Such apps could be focused on improving page load metrics or managing GDPR consent. Consider temporarily disabling such apps while you debug. Often the apps have ignore lists that enable you to fix the issue after it's identified.

---

## Trust and security — Security badges

> Fonte: https://shopify.dev/docs/storefronts/themes/trust-security/security-badges

To help establish customer trust, you can include a security badge in your theme, and link it to Shopify's documentation on [Payment Card Industry (PCI) standard compliance](https://www.shopify.com/security/pci-compliant?utm_medium=shop&utm_source=secure). Depending on your theme's color scheme, you can use a light-colored, or dark-colored, version.

### Add security badges to your theme

Security badges are often included in the footer or near the **Add to cart** button on product pages. However, they can be included anywhere you have access to include HTML.

**Note:** You can't add a security badge to the checkout page unless you're working on a [Shopify Plus](https://www.shopify.com/plus) store that has access to [checkout.liquid](https://shopify.dev/docs/storefronts/themes/architecture/layouts/checkout-liquid).

The following examples show the HTML to include for each version of the badge:

### Light

```html
<a
  href="https://www.shopify.com/security/pci-compliant?utm_medium=shop&utm_source=secure"
  title="This online store is secured by Shopify"
  target="_blank"
  rel="nofollow"
>
  <img
    src="https://cdn.shopify.com/s/images/badges/shopify-secure-badge-white.svg"
    alt="Shopify secure badge"
   />
</a>
```

### Dark

```html
<a
  href="https://www.shopify.com/security/pci-compliant?utm_medium=shop&utm_source=secure"
  title="This online store is secured by Shopify"
  target="_blank"
  rel="nofollow"
>
  <img
    src="https://cdn.shopify.com/s/images/badges/shopify-secure-badge-dark.svg"
    alt="Shopify secure badge"
   />
</a>
```

**Tip:** "The image files used for each badge are in `.svg` format, so they can be resized with no quality loss."

---

## Migrating to Online Store 2.0 — Overview

> Fonte: https://shopify.dev/docs/storefronts/themes/os20

Online Store 2.0 is a set of features and feature improvements that make themes and theme apps easier to build, more flexible, and easier to maintain.

Many Online Store 2.0 features rely on [JSON templates](https://shopify.dev/docs/storefronts/themes/architecture/templates). You can migrate a theme's templates to add support for these features by converting a Liquid template into a JSON template, and moving any required Liquid code or HTML into sections that you can include in the new JSON template.

Upgrading to Online Store 2.0 isn't mandatory. Merchants can continue using a vintage theme if it meets their needs.

### Added functionality and support

After you migrate your theme to Online Store 2.0, the theme can use or support the following features.

**Note:** These features were announced at Shopify Unite 2021. [Watch the full Shopify Unite 2021 stream](https://unite.shopify.com/).

#### Sections on every page

Online Store 2.0 introduces a new [JSON template format](https://shopify.dev/docs/storefronts/themes/architecture/templates) that lets you add new and existing sections to most pages in your theme, and add and remove sections from any page directly in the Shopify theme editor.

This feature lets merchants personalize many more aspects of a store without relying on a developer. It also lets developers build maintainable themes with more modular components.

#### Dynamic sources

Merchants can connect [dynamic sources](https://shopify.dev/docs/storefronts/themes/architecture/settings/dynamic-sources) to settings in their themes. A dynamic source is an attribute that updates to reflect its context. It can be an object attribute or [custom metafield attribute](https://shopify.dev/docs/api/liquid/objects/metafield).

You can also introduce [standard metafields](https://shopify.dev/docs/apps/build/custom-data/metafields) as default settings in your theme. Using standard metafields can help to make your components more flexible and reusable, or to provide standard templates for certain business segments.

#### App blocks

Themes that use this new architecture can [add support](https://shopify.dev/docs/storefronts/themes/os20/migration.md#step-8-add-support-for-app-blocks-to-sections) for app blocks built with [theme app extensions](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions), an app development framework that lets you add an app to a theme, or update an app, without altering a merchant's theme code. Code is packaged in modular app blocks that merchants can control using the Shopify theme editor. When an app is uninstalled by a merchant, the app code is removed with it. This makes your theme easier to support and troubleshoot.

### Migrating to Online Store 2.0

You can add Online Store 2.0 features to a store in several ways:

* **Download an Online Store 2.0 theme from the [Shopify Theme Store](https://themes.shopify.com/)**: Update the look of a store and get access to new features by downloading a new theme from the Shopify Theme Store.
* **Download a new version of a theme**: If a theme offers an updated version that uses Online Store 2.0, then you can add the latest theme version to a store manually.
* **Migrate a theme manually**: Add Online Store 2.0 functionality to a theme by converting a Liquid template into a JSON template, and moving any required Liquid code or HTML into sections that you can include in the new JSON template.

  You can migrate individual templates to take advantage of Online Store 2.0 features in specific parts of your theme, or you can migrate the entire theme by migrating all templates.

  You don't need to be a developer or a Shopify Partner to migrate your own theme manually, but migrating a theme requires an understanding of Liquid, HTML, CSS, and JavaScript.

Before you migrate your own theme or a customer's theme, you can review the migration assessment to identify which path makes sense for your or your customer's business.

* [Migration assessment](https://shopify.dev/docs/storefronts/themes/os20/assessment) — Identify the best Online Store 2.0 migration path for a business.
* [Migration guide](https://shopify.dev/docs/storefronts/themes/os20/migration) — Learn how to migrate a template to add support for Online Store 2.0 features.

---

## Migrating to Online Store 2.0 — Migration assessment

> Fonte: https://shopify.dev/docs/storefronts/themes/os20/assessment

You can add Online Store 2.0 features to a store in several ways:

* **Download an Online Store 2.0 theme from the [Shopify Theme Store](https://themes.shopify.com/)**: Update the look of a store and get access to new features by downloading a new theme from the Shopify Theme Store.
* **Download a new version of a theme**: If a theme offers an updated version that uses Online Store 2.0, then you can add the latest theme version to a store manually.
* **[Migrate a theme manually](https://shopify.dev/docs/storefronts/themes/os20/migration)**: Add Online Store 2.0 functionality to a theme by converting a Liquid template into a JSON template, and moving any required Liquid code or HTML into sections that you can include in the new JSON template.

Before you migrate your own theme or a client's theme, consider the following factors to identify which path makes sense for your or your client's business.

Upgrading to Online Store 2.0 isn't mandatory. Merchants can continue using a vintage theme if it meets their needs.

Use the following table as a quick reference to understand which migration path makes the most sense for a business. Click on the name of each consideration to learn more.

| Consideration | Don't migrate | Install new theme | Install new version of the current theme | Migrate manually |
| - | - | - | - | - |
| **Requires Online Store 2.0 features** | | | | |
| Yes | | ✓ | ✓ | ✓ |
| No | ✓ | | | |
| **Satisfied with the current theme** | | | | |
| Yes | | | ✓ | ✓ |
| No | | ✓ | | |
| **Uses many apps and theme customizations** | | | | |
| Yes | | | | ✓ |
| No | | ✓ | ✓ | |
| **Has a budget for migration** | | | | |
| Yes | | ✓ | ✓ | ✓ |
| No | | Choose from [free themes by Shopify](https://themes.shopify.com/themes?price=free) | ✓ | ✓ |
| **Comfortable with writing and editing code** | | | | |
| Yes | | ✓ | ✓ | ✓ |
| No | | ✓ | ✓ | Hire an expert to migrate |

### Online Store 2.0 feature requirements

If you or your client wants to use any of the [features introduced in Online Store 2.0](https://shopify.dev/docs/storefronts/themes/best-practices/version-control), then you should consider migrating.

If you or your client have a basic store that doesn't require ongoing changes to the current theme, and you or your client are satisfied with the current theme, then you might not choose to migrate at this time.

### Satisfaction with the current theme

Identify whether you or your client enjoy the design and basic functionality of the current theme.

If you or your client **like** the current theme but want to take advantage of Online Store 2.0 features:

* If the theme developer offers it, download the Online Store 2.0 version of the current theme from the Shopify Theme Store
* If the current theme hasn't been upgraded to Online Store 2.0, then follow one of the methods below:
  * Upgrade the theme [manually](https://shopify.dev/docs/storefronts/themes/os20/migration)
  * Choose a similar Online Store 2.0 theme from the [Shopify Theme Store](https://themes.shopify.com)

If the client **dislikes** their current theme, they can choose a new Online Store 2.0 theme from the [Shopify Theme Store](https://themes.shopify.com) to migrate to Online Store 2.0.

### Apps and customizations

Customizations made by apps, or customizations made manually to a theme, can't be migrated automatically. This means that themes that rely on several apps, or themes that are heavily customized, are harder to migrate.

If the theme relies on apps, then you should ensure that any key apps are compatible with Online Store 2.0 before migrating using a new theme or migrating manually.

If the theme is a free or paid theme that doesn't use many apps or customizations, then consider installing an upgraded version of the theme, or a new Online Store 2.0 theme from the [Shopify Theme Store](https://themes.shopify.com).

If the theme was made specifically for you, or it is a heavily customized version of a free or paid theme, then it should be migrated [manually](https://shopify.dev/docs/storefronts/themes/os20/migration). Consider the amount of time it will take to reinstall any required apps on your migrated themes.

### Budget

If you or your client has a budget to migrate to Online Store 2.0, then consider the following options:

* Purchase a new paid theme from the [Shopify Theme Store](https://themes.shopify.com)
* [Hire a Shopify Partner](https://www.shopify.com/partners/directory) to migrate the theme to Online Store 2.0 [manually](https://shopify.dev/docs/storefronts/themes/os20/migration)

If you or your client don't have a budget to perform a migration, then consider the following options:

* Choose a free Online Store 2.0 theme from the [Shopify Theme Store](https://themes.shopify.com/themes?price=free)
* If the theme developer offers it, then download the Online Store 2.0 version of the current theme from the Shopify Theme Store
* If you're comfortable with writing or editing code, then migrate the theme [manually](https://shopify.dev/docs/storefronts/themes/os20/migration) at no cost

### Code expertise

If you're comfortable with writing or editing code, then you can consider migrating your theme [manually](https://shopify.dev/docs/storefronts/themes/os20/migration). You can migrate individual templates to take advantage of Online Store 2.0 features in specific parts of your theme, or you can migrate the entire theme by migrating all templates.

If you're not comfortable with writing or editing code, then you can do the following:

* [Hire a Shopify Partner](https://www.shopify.com/partners/directory) to migrate the theme to Online Store 2.0 [manually](https://shopify.dev/docs/storefronts/themes/os20/migration)
* If the theme developer offers it, then download the Online Store 2.0 version of the current theme from the Shopify Theme Store
* Choose a new Online Store 2.0 theme from the [Shopify Theme Store](https://themes.shopify.com)

---

## Migrating to Online Store 2.0 — Migrating templates to Online Store 2.0

> Fonte: https://shopify.dev/docs/storefronts/themes/os20/migration

### Requirements

Before you start, do the following:

* Identify the theme that you want to migrate.
* If you want to migrate your theme using your local development environment and Shopify CLI:
  * [Install](https://shopify.dev/docs/api/shopify-cli) Shopify CLI.
  * Make sure that you have a [collaborator account](https://shopify.dev/docs/storefronts/themes/tools/collaborator-accounts) or a [staff account](https://help.shopify.com/manual/your-account/staff-accounts) for the store you want to work on, or you're the owner of the store. If you have a collaborator account or staff account, then you must be granted the **Manage themes** permission or **Themes** permission for the store. Store owners have these permissions by default.
  * Note the URL of the store that you want to work on.

### Step 1: Back up the theme

After you identify the theme that you want to work on, make a copy of it.

If you're editing the theme using the code editor, then [duplicate](https://help.shopify.com/manual/online-store/themes/managing-themes/duplicating-themes) the theme. Make sure that the theme is unpublished while you're editing it. This is because you'll be removing files from the theme, which would impact the live storefront. You might also need a back-up copy to reference or revert to later.

If you're editing the theme locally using Shopify CLI, then download the theme files using the [`shopify theme pull`](https://shopify.dev/docs/api/shopify-cli/theme/theme-pull) command.

### Step 2: Identify sections and remove section references

To start converting your Liquid template into a JSON template, you must make note of and then remove any `{% section %}` tags.

You need to remove these references so that you can move the rest of the code into a section file. Section files can't contain references to other section files.

1. Open your theme in the code editor or your local development environment.
2. Locate the `product.liquid` file in the `/templates` directory.
3. Search for any `{% section %}` tags where sections are being included. Note their names and where they are located.

   For example, in Debut, there are two sections included at the top of the template:

   ```liquid
   {% section 'product-template' %}
   {% section 'product-recommendations' %}
   ```

   The first section tag references the `product-template` section, which contains most of the markup needed to render the product page. That includes the product title, product images, add to cart button, and more.

   Next is a reference to the `product-recommendations` section, which displays a list of products automatically selected as suggestions for customers.

4. After you've found any `{% section %}` tags and made a note of their location, delete the tags from the `product.liquid` file.

### Step 3: Move code from the template into a section

After you remove the `{% section %}` tags from the template code, you need to decide where to move it. You can move this code to an existing section or a new section.

#### Option 1: Add code to an existing section

You might already have a section that renders a large portion of the code for a page. For example, in Debut, the `product-template` section contains a portion of the code for the product page.

1. Open the section file where you want to add the template code.
2. Copy the remaining code from `product.liquid`.
3. Paste the code into the section file above the opening `{% schema %}` tags.

#### Option 2: Add code to a new section

If none of the existing section files in your theme are appropriate, then you can create a new section to host your Liquid template code.

1. Create a new file in the `/sections` directory. For example, `product-content.liquid`. If you're creating the section through the code editor, then delete the placeholder code for the section.
2. After you create your new section file, copy the remaining code from the `product.liquid` file and paste it into the empty section file.

### Step 4: Delete the Liquid template file

After you copy the code from `product.liquid`, delete `product.liquid` from the `/templates` directory. This is because it will be replaced with a `product.json` file, and a `product.liquid` and `product.json` file can't be stored in the `/templates` directory at the same time.

### Step 5: Create a JSON template file

After the `product.liquid` file has been deleted, you can create the replacement JSON template.

1. Create a new file in the `/templates` directory called `product.json`:

   * If you're using the code editor:
     1. Select **Add a new template**.
     2. From the **Create a template for** drop-down menu, choose **Product**.
     3. Select **JSON** as the template type.
   * If you're editing the theme locally, then create a new file called `product.json` and save it in the `/templates` directory.

2. After you create the `product.json` file, replace any default code inside this file with the following:

   ```json
   {
     "sections": {
       "main": {
         "type": "product-template"
       }
     },
     "order": [
       "main"
     ]
   }
   ```

   The `type` property should reference the name of the section file where you transferred the markup of the product template file in step 3.

3. Save the file.

### Step 6: Test the template

After you create your new template, open it in the theme editor to make sure that it renders correctly.

To access the theme editor using Shopify CLI:

1. In a terminal, type `shopify login --store <DOMAIN>`, where `<DOMAIN>` is the store that you want to log in to. Click the link to finish the login process.
2. Navigate to the working directory for the theme.
3. Type `shopify theme dev`. The dev command returns a link to the Shopify admin theme editor.

Open the theme editor and navigate to a product page. An **Add section** button should appear in the left sidebar. All the sections that were previously accessible only from the home page should now appear in the **Add section** menu.

### Step 7: Add references to sections

If the original `product.liquid` template file contained references to additional sections, such as a product recommendations section, then you can define these within the `product.json` file, and then define their order.

1. Open `product.json`. The file currently references only a main section, the section that contains your migrated code.

   ```json
   {
     "sections": {
       "main": {
         "type": "product-template"
       }
     },
     "order": [
       "main"
     ]
   }
   ```

2. Add additional sections using this structure. For example, you can add a reference to a `product-recommendations` section.

   In this example, below the `main` object, you can insert a second object called `recommendations`. The `type` property contains the filename of this section:

   ```json
   {
     "sections": {
       "main": {
         "type": "product-template"
       },
       "recommendations": {
         "type": "product-recommendations"
       }
     },
     "order": [
       "main"
     ]
   }
   ```

3. Define the order in which the sections appear.

   For example, you can order the `recommendation` section relative to the `main` section.

   Within the `order` array, add `recommendations` where the section should appear. In this case, the section should appear below the existing `main` section.

   After you define the order, your `product.json` file should look like this:

   ```json
   {
     "sections": {
       "main": {
         "type": "product-template"
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

When you navigate to the theme editor and select a product page, the product recommendations section should now appear on the page below the product template section.

**Tip:** You can also add a section, or adjust the order of the sections, using the theme editor.

### Step 8: Add support for app blocks to sections

If you want to let merchants add app blocks to sections in your theme, then you need to make the following changes to your section code:

* Add the necessary schema
* Render the block content

You need to make these changes for every section where you want to support app blocks. [Learn more about supporting app blocks in your theme](https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks).

**Note:** App blocks are built using [theme app extensions](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions), which are currently available only as a developer preview. You can test your updated section code by adding the [product reviews sample app](https://github.com/Shopify/product-reviews-sample-app).

#### Enable app blocks in the section schema

To let merchants add an app block to a section, you need to add blocks of type `@app` to the section's schema.

Blocks of type `@app` aren't supported in [statically rendered sections](https://shopify.dev/docs/storefronts/themes/architecture/sections#statically-render-a-section).

For example, to add support for app blocks to the Debut `product-template` section, you can add the code below. Because the section doesn't contain any blocks, you can add a new `blocks` node after the schema's `settings` node.

```json
"settings": [
...
],
"blocks": [
  {
    "type": "@app"
  }
]
```

#### Render app blocks

To render an app block in your theme, check for the appropriate type, and then render the block using a `{% render block %}` tag. You can add this code wherever it makes sense for your section.

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

### Step 9: Repeat the process

You can repeat the process outlined above to convert all of the sections in your theme.

### Next steps

After you create new JSON templates based off your Liquid templates, consider enhancing your theme further:

* **Make your template more modular** - You can extract functionality that existed in the core template code into sections and blocks. For example, you can convert a `Show vendor` checkbox into a block that represents the vendor. [Learn some best practices for using sections and blocks](https://shopify.dev/docs/storefronts/themes/best-practices/templates-sections-blocks).
* **Connect theme settings to dynamic sources** - You can update your theme's default settings to reference dynamic sources. For example, you can reference a product attribute as a default value of a text box. [Learn about dynamic sources](https://shopify.dev/docs/storefronts/themes/architecture/settings/dynamic-sources).
* **Add version control to your theme** - To make later theme updates simpler, and to track theme changes made in the theme editor, code editor, and more, you [can connect your theme to a GitHub repository](https://shopify.dev/docs/storefronts/themes/tools/github).
* **Explore tools for building Shopify themes** - As a part of Online Store 2.0, Shopify released a new suite of developer tools that help you to streamline your theme development and testing process. [Learn more about the tools that are now available](https://shopify.dev/docs/storefronts/themes/tools).

---

## Sign-in redirects — Customer sign-in links and redirects

> Fonte: https://shopify.dev/docs/storefronts/themes/sign-in

You can configure where customers are redirected after they sign in to their account on your store. For example, you might want to redirect customers to the page they were on when they signed in, or a specific product collection.

In this tutorial, you'll learn how to configure custom redirects in your theme.

### Resources

Use [`routes` object](https://shopify.dev/docs/api/liquid/objects/routes) to manage sign-in redirection.

### Direct links

Direct links send customers to specific destinations in customer accounts, routing them through sign-in when needed, with optional parameters to make the process faster.

#### Link to the sign-in page with email prepopulated

You can create sign-in links that prepopulate the customer's email address on the sign-in page. This is useful when you already know the customer's email address, such as when you've captured it through a form on your store.

Use the `login_hint` parameter to specify the email address. The customer is taken to the sign-in page with the email address prefilled, allowing them to review it before continuing.

In the following example snippet, you'll see how you can pre-fill an email address into this `login_hint` parameter after a form submission:

##### /sections/header.liquid

```liquid
<a href="{{ routes.storefront_login_url | append: '&login_hint=' | append: customer.email | url_param_escape }}">Sign in</a>
```

#### Redirecting to customer accounts

Before you edit your theme code, review the [considerations for customizing your theme](https://help.shopify.com/manual/online-store/themes/customizing-themes#before-you-customize-your-theme) to prevent any unintended changes to your store.

In Liquid, the [`routes`](https://shopify.dev/docs/api/liquid/objects/routes) object can be used to direct customers to customer accounts, where they can view their order history and track current orders:

* **`routes.account_login_url`**: Takes customers to the sign-in page and then to the order index page after they sign in successfully.
* **`routes.account_url`**: Takes customers to customer accounts order index page directly.

If you need to append a path (such as for an account extension, tab, or subpage) to `routes.account_url`, be aware that this URL may sometimes contain query parameters (for example, after a successful sign-in).

To ensure your generated links remain valid, always split `routes.account_url` on the `?` character before appending your extension, then re-attach any query parameters at the end.

Example:

##### /sections/header.liquid

```liquid
{% assign url_parts = routes.account_url | split: '?' %}
{% assign base_url = url_parts | first %}
<a href="{{ base_url }}/pages/extensionId{% if url_parts.size > 1 %}?{{ url_parts.last }}{% endif %}">Account Extension Link</a>
```

This approach always produces a valid link, regardless of whether `routes.account_url` contains query parameters.

##### Modify your sign-in links to redirect to the order index page

If your store's theme supports a customer account sign-in link, then the following is an example of the default route on the `header.liquid` page:

##### /sections/header.liquid

```liquid
{%- if shop.customer_accounts_enabled -%}
  <a href="{%- if customer -%}{{ routes.account_url }}{%- else -%}{{ routes.account_login_url }}{%- endif -%}"
    class="header__icon header__icon--account link focus-inset{% if section.settings.menu != blank %} small-hide{% endif %}"
    rel="nofollow">
  </a>
{%- endif -%}
```

If your theme doesn't display a sign-in link in your theme header, then you can add a customer account sign-in link to your theme with the following Liquid code:

##### /sections/header.liquid

```liquid
{%- if shop.customer_accounts_enabled -%}
  {% if customer %}
    <a href="{{ routes.account_url }}">Account</a>
  {% else %}
    <a href="{{ routes.account_login_url }}">Sign in</a>
  {%- endif %}
{%- endif -%}
```

##### Link directly to customer account pages

Create direct links to redirect customers to specific customer account pages, such as their **Profile** page:

##### /sections/header.liquid

```liquid
{% assign url_parts = routes.account_url | split: '?' %}
{% assign base_url = url_parts | first %}
<a href="{{ base_url }}/profile{% if url_parts.size > 1 %}?{{ url_parts.last }}{% endif %}">Account Profile</a>
```

Link to a customer account full-page extension with the following Liquid code:

##### /sections/header.liquid

```liquid
{% assign url_parts = routes.account_url | split: '?' %}
{% assign base_url = url_parts | first %}
<a href="{{ base_url }}/pages/extensionId{% if url_parts.size > 1 %}?{{ url_parts.last }}{% endif %}">Account Extension</a>
```

### Redirect customers after signing in

#### Direct customers back to the online store

Direct your customers back to the online store after successful sign in by editing your theme code to use the [`routes.storefront_login_url`](https://shopify.dev/docs/api/liquid/objects/routes#routes-storefront_login_url) object. Once signed in, the customer will be taken back to the page where the sign-in originated. For example, if a customer is on the **Catalog** page and clicks on the sign-in link, they will be taken back to **Catalog** after a successful sign in.

The following example demonstrates how you can modify the customer account sign-in link with the `storefront_login_url` route. In this example, after a customer signs in, they're taken back to the storefront. If they click on the sign-in link again, they're taken to customer accounts:

##### /sections/header.liquid

```liquid
{%- if shop.customer_accounts_enabled -%}
  <a href="{%- if customer -%}{{ routes.account_url }}{%- else -%}{{ routes.storefront_login_url }}{%- endif -%}"
    class="header__icon header__icon--account link focus-inset{% if section.settings.menu != blank %} small-hide{% endif %}"
    rel="nofollow">
  </a>
{%- endif -%}
```

You can also add the route to any sign-in URL on your storefront with the following Liquid code:

##### /sections/header.liquid

```liquid
<a href="{{ routes.storefront_login_url }}">Sign in</a>
```

**Note:** If you choose to direct customers back to the online store after signing in, by replacing the default sign-in link route, we recommend you use another link on your theme that navigates customers to their account and orders.

#### Direct customers back to another page on the online store

You can redirect customers to any page on your online store using the `/customer_authentication/login` path with a `return_to` parameter.

For example, to redirect customers to your **Contact** page after signing in, use this Liquid code:

##### /sections/header.liquid

```liquid
<a href="/customer_authentication/login?return_to={{ "/pages/contact" | url_encode }}">Contact</a>
```

**Note:** The `return_to` parameter only works with relative URLs.

---

## Troubleshooting — Overview

> Fonte: https://shopify.dev/docs/storefronts/themes/troubleshooting

Below are some errors that you might encounter while working on your theme. Click the link for details.

* [Parameter Missing or Invalid: Required parameter missing or invalid](https://shopify.dev/docs/storefronts/themes/troubleshooting/fix-parameter-missing-or-invalid-errors)
* [Description can't be larger than 64 kilobytes](https://shopify.dev/docs/storefronts/themes/troubleshooting/fix-64-kilobyte-limit-errors)
* [Browser address bar warnings, inconsistent or missing elements](https://shopify.dev/docs/storefronts/themes/troubleshooting/use-protocol-independent-urls)

---

## Troubleshooting — Fix "Parameter Missing or Invalid" errors

> Fonte: https://shopify.dev/docs/storefronts/themes/troubleshooting/fix-parameter-missing-or-invalid-errors

When adding an item to the cart, you may encounter the error **Parameter Missing or Invalid: Required parameter missing or invalid**. This occurs when a variant ID or quantity is not submitted with your Add to Cart form.

### Possible causes and solutions

* **Malformed HTML in customized template** — Validate your HTML using the [W3C Validator](https://validator.w3.org).
* **Hidden default option for single-variant products** — If you removed the dropdown or radio button for a product with one variant, replace it with a hidden field that passes the variant ID of the first variant to Shopify. Visit the [.dev Community](https://community.shopify.dev) for assistance.
* **Unchecked radio buttons** — When using radio buttons for product variants in a custom theme, ensure the first option is selected by default using `selected="selected"`. Without a default selection, no variant ID submits with the form.

### Important notes

> "If you are using a custom theme, our Support team cannot help you with this error."

Refer to the [Design Policy](https://help.shopify.com/manual/online-store/themes/theme-support) for more information.

If these methods don't resolve the issue, you can [roll back](https://help.shopify.com/manual/online-store/themes/theme-structure/extend/edit-theme-code) your `product.liquid` template to an earlier version.

---

## Troubleshooting — Fix "can't be larger than 64 kilobytes" errors

> Fonte: https://shopify.dev/docs/storefronts/themes/troubleshooting/fix-64-kilobyte-limit-errors

Have you encountered this error message while working on any pages within Shopify?

**Description can't be larger than 64 kilobytes.**

Below is a description of why this would occur as well as a work-around to prevent it from happening.

### The Problem

In some rare circumstances, you may run into a situation where your page is larger than 64kb (64 kilobytes). First off, 64kb is a huge amount of textual data. To give some idea of what 64kb really means:

```text
64KB = 64000 bytes = 64,000 characters (@ 1 character/byte). Or, more than 10,000 English words.
```

"This is not a Shopify imposed limit, rather it is a MySQL database cell limit for TEXT data type." In the rare event that you have a page that must exceed this database limit, don't worry - we have a work around for you.

### The Solution

In this situation, you must break up your data into smaller chunks **and** [create an alternate page template](https://shopify.dev/docs/storefronts/themes/architecture/templates/alternate-templates) for your special page to "glue" these chunks back together.

You can approach this in one of two ways:

* Use multiple **pages** to show the content
* Use multiple **snippets** to show the content.

Either way, the new alternate page template will be used to "glue" your content together.

**Tip:** If you use snippets you must create any HTML for display yourself. If you use a page the RTE will build the HTML for you but you may still need to check the mark-up in HTML view to make sure it is precise.

**To get started:**

1. Create either your pages for your content or your snippets and make note of their names—you'll need them to use in your template in order to "glue" them back together.
2. Make a new template based on your page template. If you are unclear on how to do this, please read [this page](https://shopify.dev/docs/storefronts/themes/architecture/templates/alternate-templates) before proceeding.
3. Once your special template has been created you need to call the broken up content into the template. For pages, your template will look something like this, using the page handles for each of your parts:

```liquid
<h1>{{ page.title }}</h1>
{{ pages.terms-part-1.content }}
{{ pages.terms-part-2.content }}
{{ pages.terms-part-3.content }}
```

If you are using snippets then your page code should look something like this:

```liquid
<h1>{{ page.title }}</h1>
{% render 'terms-part-1' %}
{% render 'terms-part-2' %}
{% render 'terms-part-3' %}
```

---

## Troubleshooting — Using Protocol-Independent URLs

> Fonte: https://shopify.dev/docs/storefronts/themes/troubleshooting/use-protocol-independent-urls

Different web protocols might cause your store to behave unexpectedly for some users.

* Colors don't display correctly
* Some page elements or images don't appear
* Your browser address bar shows a warning

This might happen if some of your theme **assets** don't use protocol-independent URLs. These URLs are required if you want to load your site through a secure connection (`https://`).

### About assets

Assets are files that your theme needs to function properly. These include JavaScript files, stylesheets, and image files. External hyperlinks are not considered assets.

### Protocol-independent URLs

URL protocols look like `http://`, `https://`, and `ftp://`. "A protocol-independent URL simply begins with `//`."

You might be loading your store through a secured connection (`https`) if any of the following apply to you:

* you use the `.myshopify.com` address as your primary domain
* you're a Shopify Plus merchant with custom SSL security on your store
* you've activated SSL for your online store

For your store to load properly, all theme assets must use your store's secure protocol. You can make sure this by replacing the `http://` in their reference addresses with `//`.

### Updating assets to use protocol-independent URLs

To make sure your assets work properly when your store is viewed through a secure connection, search your theme files for the text `http://`, and replace all instances of that text with `//`. For example:

Before:

```html
<link
  href="http://fonts.googleapis.com/css?family=Open+Sans"
  rel="stylesheet"
  type="text/css"
/>
```

After:

```html
<link
  href="//fonts.googleapis.com/css?family=Open+Sans"
  rel="stylesheet"
  type="text/css"
/>
```

#### Best practices

* You can download your theme and use the **Replace all** feature in a text editor to replace the URL protocol in all your theme files. You can then upload your edited theme and publish the imported theme that has protocol-independent URLs.
* To find out which assets are not loading securely, you can check your browser console. The console should list the assets that are not loading properly.

**Tip:** You might notice that YouTube videos don't load in the online code editor. This is because the embed code for these videos doesn't use the HTTPS protocol. Not to worry though, they'll still display properly on your online store.

---

*Fine del capitolo 5 — Theme Features.*
