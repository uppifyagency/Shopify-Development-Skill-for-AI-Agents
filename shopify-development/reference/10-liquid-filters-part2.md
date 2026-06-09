# 10. Liquid — Filters (parte 2: categorie M–Z)

> **Categorie coperte in questo file (M–Z):** `math`, `media`, `metafield`, `money`, `payment`, `string`, `tag`.
> Le categorie A–L (`array`, `cart`, `collection`, `color`, `customer`, `date`, `default`, `font`, `format`, `hosted_file`, `html`, `localization`) sono nel file complementare *part 1*. Nessuna sovrapposizione e nessun buco tra i due file.

Questo capitolo documenta in modo fedele (1:1) ogni filtro Liquid di Shopify la cui **categoria** inizia con una lettera da M a Z. Per ciascun filtro sono riportati: nome, categoria, descrizione, sintassi (`input | filter: params`), parametri con tipo e descrizione, valore restituito, eventuali note di deprecazione/disponibilità, e tutti gli esempi di codice (input Liquid e output renderizzato) così come pubblicati su shopify.dev.

Fonte indice: https://shopify.dev/docs/api/liquid/filters

## Indice (per categoria)

- **math**
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

- **media**
  - [media — external_video_tag](#media--external_video_tag)
  - [media — external_video_url](#media--external_video_url)
  - [media — image_tag](#media--image_tag)
  - [media — media_tag](#media--media_tag)
  - [media — model_viewer_tag](#media--model_viewer_tag)
  - [media — video_tag](#media--video_tag)
  - [media — article_img_url](#media--article_img_url) _(deprecato)_
  - [media — collection_img_url](#media--collection_img_url) _(deprecato)_
  - [media — image_url](#media--image_url)
  - [media — img_tag](#media--img_tag) _(deprecato)_
  - [media — img_url](#media--img_url) _(deprecato)_
  - [media — product_img_url](#media--product_img_url) _(deprecato)_

- **metafield**
  - [metafield — metafield_tag](#metafield--metafield_tag)
  - [metafield — metafield_text](#metafield--metafield_text)

- **money**
  - [money — money](#money--money)
  - [money — money_amount](#money--money_amount)
  - [money — money_with_currency](#money--money_with_currency)
  - [money — money_without_currency](#money--money_without_currency)
  - [money — money_without_trailing_zeros](#money--money_without_trailing_zeros)

- **payment**
  - [payment — payment_button](#payment--payment_button)
  - [payment — payment_terms](#payment--payment_terms)
  - [payment — payment_type_img_url](#payment--payment_type_img_url)
  - [payment — payment_type_svg_tag](#payment--payment_type_svg_tag)

- **string**
  - [string — blake3](#string--blake3)
  - [string — hmac_sha1](#string--hmac_sha1)
  - [string — hmac_sha256](#string--hmac_sha256)
  - [string — md5](#string--md5)
  - [string — sha1](#string--sha1)
  - [string — sha256](#string--sha256)
  - [string — append](#string--append)
  - [string — base64_decode](#string--base64_decode)
  - [string — base64_encode](#string--base64_encode)
  - [string — base64_url_safe_decode](#string--base64_url_safe_decode)
  - [string — base64_url_safe_encode](#string--base64_url_safe_encode)
  - [string — capitalize](#string--capitalize)
  - [string — downcase](#string--downcase)
  - [string — escape](#string--escape)
  - [string — escape_once](#string--escape_once)
  - [string — lstrip](#string--lstrip)
  - [string — newline_to_br](#string--newline_to_br)
  - [string — prepend](#string--prepend)
  - [string — remove](#string--remove)
  - [string — remove_first](#string--remove_first)
  - [string — remove_last](#string--remove_last)
  - [string — replace](#string--replace)
  - [string — replace_first](#string--replace_first)
  - [string — replace_last](#string--replace_last)
  - [string — rstrip](#string--rstrip)
  - [string — slice](#string--slice)
  - [string — split](#string--split)
  - [string — strip](#string--strip)
  - [string — strip_html](#string--strip_html)
  - [string — strip_newlines](#string--strip_newlines)
  - [string — truncate](#string--truncate)
  - [string — truncatewords](#string--truncatewords)
  - [string — upcase](#string--upcase)
  - [string — url_decode](#string--url_decode)
  - [string — url_encode](#string--url_encode)
  - [string — camelize](#string--camelize)
  - [string — handleize](#string--handleize)
  - [string — url_escape](#string--url_escape)
  - [string — url_param_escape](#string--url_param_escape)
  - [string — pluralize](#string--pluralize)

- **tag**
  - [tag — link_to_add_tag](#tag--link_to_add_tag)
  - [tag — link_to_remove_tag](#tag--link_to_remove_tag)
  - [tag — link_to_tag](#tag--link_to_tag)


# Categoria: math

## math — abs

> Fonte: https://shopify.dev/docs/api/liquid/filters/abs

Returns the absolute value of a number.

### Sintassi

```liquid
number | abs
```

### Restituisce

[number](https://shopify.dev/docs/api/liquid/basics#number)

### Esempi

**Input:**

```liquid
{{ -3 | abs }}
```

**Output:**

```html
3
```


## math — at_least

> Fonte: https://shopify.dev/docs/api/liquid/filters/at_least

Limits a number to a minimum value.

### Sintassi

```liquid
number | at_least
```

### Restituisce

[number](https://shopify.dev/docs/api/liquid/basics#number)

### Esempi

**Input:**

```liquid
{{ 4 | at_least: 5 }}
{{ 4 | at_least: 3 }}
```

**Output:**

```html
5
4
```


## math — at_most

> Fonte: https://shopify.dev/docs/api/liquid/filters/at_most

Limits a number to a maximum value.

### Sintassi

```liquid
number | at_most
```

### Restituisce

[number](https://shopify.dev/docs/api/liquid/basics#number)

### Esempi

**Input:**

```liquid
{{ 6 | at_most: 5 }}
{{ 4 | at_most: 5 }}
```

**Output:**

```html
5
4
```


## math — ceil

> Fonte: https://shopify.dev/docs/api/liquid/filters/ceil

Rounds a number up to the nearest integer.

### Sintassi

```liquid
number | ceil
```

### Restituisce

[number](https://shopify.dev/docs/api/liquid/basics#number)

### Esempi

**Input:**

```liquid
{{ 1.2 | ceil }}
```

**Output:**

```html
2
```


## math — divided_by

> Fonte: https://shopify.dev/docs/api/liquid/filters/divided_by

Divides a number by a given number. The `divided_by` filter produces a result of the same type as the divisor. This means if you divide by an integer, the result will be an integer, and if you divide by a float, the result will be a float.

### Sintassi

```liquid
number | divided_by: number
```

### Restituisce

[number](https://shopify.dev/docs/api/liquid/basics#number)

### Esempi

**Input:**

```liquid
{{ 4 | divided_by: 2 }}

# divisor is an integer
{{ 20 | divided_by: 7 }}

# divisor is a float 
{{ 20 | divided_by: 7.0 }}
```

**Output:**

```html
2

# divisor is an integer
2

# divisor is a float 
2.857142857142857
```


## math — floor

> Fonte: https://shopify.dev/docs/api/liquid/filters/floor

Rounds a number down to the nearest integer.

### Sintassi

```liquid
number | floor
```

### Restituisce

[number](https://shopify.dev/docs/api/liquid/basics#number)

### Esempi

**Input:**

```liquid
{{ 1.2 | floor }}
```

**Output:**

```html
1
```


## math — minus

> Fonte: https://shopify.dev/docs/api/liquid/filters/minus

Subtracts a given number from another number.

### Sintassi

```liquid
number | minus: number
```

### Restituisce

[number](https://shopify.dev/docs/api/liquid/basics#number)

### Esempi

**Input:**

```liquid
{{ 4 | minus: 2 }}
```

**Output:**

```html
2
```


## math — modulo

> Fonte: https://shopify.dev/docs/api/liquid/filters/modulo

Returns the remainder of dividing a number by a given number.

### Sintassi

```liquid
number | modulo: number
```

### Restituisce

[number](https://shopify.dev/docs/api/liquid/basics#number)

### Esempi

**Input:**

```liquid
{{ 12 | modulo: 5 }}
```

**Output:**

```html
2
```


## math — plus

> Fonte: https://shopify.dev/docs/api/liquid/filters/plus

Adds two numbers.

### Sintassi

```liquid
number | plus: number
```

### Restituisce

[number](https://shopify.dev/docs/api/liquid/basics#number)

### Esempi

**Input:**

```liquid
{{ 2 | plus: 2 }}
```

**Output:**

```html
4
```


## math — round

> Fonte: https://shopify.dev/docs/api/liquid/filters/round

Rounds a number to the nearest integer.

### Sintassi

```liquid
number | round
```

### Restituisce

[number](https://shopify.dev/docs/api/liquid/basics#number)

### Esempi

#### Esempio 1

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

You can specify a number of decimal places to round to. If you don't specify a number, then the `round` filter rounds to the nearest integer.

**Input:**

```liquid
{{ 3.14159 | round: 2 }}
```

**Output:**

```html
3.14
```


## math — times

> Fonte: https://shopify.dev/docs/api/liquid/filters/times

Multiplies a number by a given number.

### Sintassi

```liquid
number | times: number
```

### Restituisce

[number](https://shopify.dev/docs/api/liquid/basics#number)

### Esempi

**Input:**

```liquid
{{ 2 | times: 2 }}
```

**Output:**

```html
4
```


# Categoria: media

## media — external_video_tag

> Fonte: https://shopify.dev/docs/api/liquid/filters/external_video_tag

Generates an HTML `<iframe>` tag containing the player for a given external video. The input for the `external_video_tag`
filter can be either a [`media` object](https://shopify.dev/docs/api/liquid/objects/media) or [`external_video_url`](https://shopify.dev/docs/api/liquid/filters/external_video_url).

If [alt text is set on the video](https://help.shopify.com/en/manual/products/product-media/add-alt-text), then it's
included in the `title` attribute of the `<iframe>`. If no alt text is set, then the `title` attribute is set to the
product title.

### Sintassi

```liquid
variable | external_video_tag
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

#### Esempio 1

**Input:**

```liquid
{% for media in product.media %}
  {% if media.media_type == 'external_video' %}
    {% if media.host == 'youtube' %}
      {{ media | external_video_url: color: 'white' | external_video_tag }}
    {% elsif media.host == 'vimeo' %}
      {{ media | external_video_url: loop: '1', muted: '1' | external_video_tag }}
    {% endif %}
  {% endif %}
{% endfor %}
```

**Output:**

```html
<iframe frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen" src="https://www.youtube.com/embed/vj01PAffOac?color=white&amp;controls=1&amp;enablejsapi=1&amp;modestbranding=1&amp;origin=https%3A%2F%2Fpolinas-potent-potions.myshopify.com&amp;playsinline=1&amp;rel=0" title="Potion beats"></iframe>
```

#### HTML attributes

You can specify [HTML attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe#attributes) by adding a parameter that matches the attribute name, and the desired value.

Sintassi:

```liquid
variable | external_video_tag: attribute: string
```

**Input:**

```liquid
{% for media in product.media %}
  {% if media.media_type == 'external_video' %}
    {% if media.host == 'youtube' %}
      {{ media | external_video_url: color: 'white' | external_video_tag: class:'youtube-video' }}
    {% endif %}
  {% endif %}
{% endfor %}
```

**Output:**

```html
<iframe frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen" class="youtube-video" src="https://www.youtube.com/embed/vj01PAffOac?color=white&amp;controls=1&amp;enablejsapi=1&amp;modestbranding=1&amp;origin=https%3A%2F%2Fpolinas-potent-potions.myshopify.com&amp;playsinline=1&amp;rel=0" title="Potion beats"></iframe>
```


## media — external_video_url

> Fonte: https://shopify.dev/docs/api/liquid/filters/external_video_url

Returns the URL for a given external video. Use this filter to specify parameters for the external video player generated
by the [`external_video_tag` filter](https://shopify.dev/docs/api/liquid/filters/external_video_tag).

### Sintassi

```liquid
media | external_video_url: attribute: string
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

You can specify [YouTube](https://developers.google.com/youtube/player_parameters#Parameters) and [Vimeo](https://vimeo.zendesk.com/hc/en-us/articles/360001494447-Using-Player-Parameters) video parameters by adding a parameter that matches the parameter name, and the desired value.

**Input:**

```liquid
{% for media in product.media %}
  {% if media.media_type == 'external_video' %}
    {% if media.host == 'youtube' %}
      {{ media | external_video_url: color: 'white' | external_video_tag }}
    {% elsif media.host == 'vimeo' %}
      {{ media | external_video_url: loop: '1', muted: '1' | external_video_tag }}
    {% endif %}
  {% endif %}
{% endfor %}
```

**Output:**

```html
<iframe frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen" src="https://www.youtube.com/embed/vj01PAffOac?color=white&amp;controls=1&amp;enablejsapi=1&amp;modestbranding=1&amp;origin=https%3A%2F%2Fpolinas-potent-potions.myshopify.com&amp;playsinline=1&amp;rel=0" title="Potion beats"></iframe>
```


## media — image_tag

> Fonte: https://shopify.dev/docs/api/liquid/filters/image_tag

Generates an HTML `<img>` tag for a given [`image_url`](https://shopify.dev/docs/api/liquid/filters/image_url).

By default, `width` and `height` attributes are added to the `<img>` tag based on the dimensions and aspect ratio from
the image URL. However, you can override these attributes with the [width](https://shopify.dev/docs/api/liquid/filters/image_tag#image_tag-width) and [height](https://shopify.dev/docs/api/liquid/filters/image_tag#image_tag-height)
parameters. If only one parameter is provided, then only that attribute is added.

### Sintassi

```liquid
string | image_tag
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Parametri

| Parametro | Tipo | Obbligatorio | Posizionale | Descrizione |
|---|---|---|---|---|
| `width` | number | no | no | The width of the image. |
| `height` | number | no | no | The height of the image. |
| `sizes` | number | no | no | The source sizes for responsiveness. |
| `widths` | number | no | no | The widths to associate with custom `srcset` values. |
| `srcset` | number | no | no | The `srcset` for responsiveness. |
| `preload` | boolean | no | no | Whether the resource should be preloaded. |
| `alt` | number | no | no | The image's alt text. |

### Esempi

#### Esempio 1

**Input:**

```liquid
{{ product | image_url: width: 200 | image_tag }}
```

**Output:**

```html
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=200" alt="Health potion" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=200 200w" width="200" height="133">
```

#### Lazy loading

If you don't apply the `preload` attribute to `image_tag`, then `loading` is automatically set to `lazy` for images in sections further down the page.
You shouldn't lazy load images above the fold. If the default value doesn't work for your theme, then consider writing your own logic using the `section.index` and `section.location` properties. For more information, refer to the [`section` object](https://shopify.dev/docs/api/liquid/objects/section).

#### `image_tag` and focal points

This filter automatically applies a focal point to the image using the `object-position` CSS style, if focal point coordinates are available. You can also access an image's focal point coordinates directly through the [`focal_point`](https://shopify.dev/docs/api/liquid/objects/focal_point) object. [Learn how to set a focal point](https://help.shopify.com/manual/online-store/images/theme-images#set-a-focal-point-on-a-theme-image).

**Input:**

```liquid
{{ images['potions-header.png'] | image_url: width: 300 | image_tag }}
```

**Output:**

```html
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/potions-header.png?v=1650325393&amp;width=300" alt="" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/files/potions-header.png?v=1650325393&amp;width=300 300w" width="300" height="173" style="object-position:1.9231% 9.7917%;">
```

#### width

Specify the `width` attribute of the `<img>` tag. You can set the parameter to `nil` to prevent the attribute from being added.

Sintassi:

```liquid
image_url | image_tag: width: number
```

**Input:**

```liquid
<!-- With a width -->
{{ product | image_url: width: 400 | image_tag: width: 300 }}

<!-- With the width set to nil -->
{{ product | image_url: width: 400 | image_tag: width: nil }}
```

**Output:**

```html
<!-- With a width -->
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=400" alt="Health potion" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=300 300w, //polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=352 352w" width="300">

<!-- With the width set to nil -->
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=400" alt="Health potion" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=352 352w">
```

#### height

Specify the `height` attribute of the `<img>` tag. You can set the parameter to `nil` to prevent the attribute from being added.

Sintassi:

```liquid
image_url | image_tag: height: number
```

**Input:**

```liquid
<!-- With a height -->
{{ product | image_url: width: 400 | image_tag: height: 300 }}

<!-- With the height set to nil -->
{{ product | image_url: width: 400 | image_tag: height: nil }}
```

**Output:**

```html
<!-- With a height -->
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=400" alt="Health potion" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=352 352w" height="300">

<!-- With the height set to nil -->
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=400" alt="Health potion" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=352 352w">
```

#### sizes

Specify source sizes with the [HTML `sizes` attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attr-sizes).

Sintassi:

```liquid
image_url | image_tag: sizes: string
```

**Input:**

```liquid
{{ product | image_url: width: 200 | image_tag: sizes: '(min-width:1600px) 960px, (min-width: 750px) calc((100vw - 11.5rem) / 2), calc(100vw - 4rem)' }}
```

**Output:**

```html
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=200" alt="Health potion" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=200 200w" width="200" height="133" sizes="(min-width:1600px) 960px, (min-width: 750px) calc((100vw - 11.5rem) / 2), calc(100vw - 4rem)">
```

#### widths

By default, Shopify generates a `srcset` with a smart set of default widths up to the maximum defined in the image URL. However, you can create your own set of widths.

Sintassi:

```liquid
image_url | image_tag: widths: string
```

**Input:**

```liquid
{{ product | image_url: width: 600 | image_tag: widths: '200, 300, 400' }}
```

**Output:**

```html
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=600" alt="Health potion" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=200 200w, //polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=300 300w, //polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=400 400w" width="600" height="400">
```

#### srcset

By default, Shopify generates a `srcset`. However, you can create your own `srcset`.
The `srcset` parameter takes precedence over the [`width` parameter](https://shopify.dev/docs/api/liquid/filters/image_tag#image_tag-width).
You shouldn't to use the `srcset` parameter unless you want to remove the attribute by setting the parameter to `nil`.

Sintassi:

```liquid
image_url | image_tag: srcset: string
```

**Input:**

```liquid
{{ product | image_url: width: 200 | image_tag: srcset: nil }}
```

**Output:**

```html
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=200" alt="Health potion" width="200" height="133">
```

#### preload

Specify whether the image should be preloaded.

When `preload` is set to `true`, a resource hint is sent as a [Link HTTP header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Link)
with a `rel` value of [`preload`](https://developer.mozilla.org/en-US/docs/Web/HTML/Link_types/preload).
The Link header also includes `imagesrcset` and `imagesizes` that match the `srcset` and `sizes` attribute of the tag,
where present:

```liquid
Link: <IMAGE_URL>; rel=preload; as=image
Link: <IMAGE_URL>; rel=preload; as=image; imagesrcset=ADDITIONAL_IMAGE_URL 352w; imagesizes=40vw
```

This option doesn't affect the HTML img tag directly.

You should use the preload parameter sparingly. For example, consider preloading only above-the-fold images.
To learn more about resource hints in Shopify themes, refer to [Performance best practices for Shopify themes](https://shopify.dev/themes/best-practices/performance#preload-key-resources-defer-or-avoid-loading-others).

Sintassi:

```liquid
image_url | image_tag: preload: boolean
```

#### alt

By default, the `alt` attribute of the `<img>` tag is set to the [media alt text](https://help.shopify.com/manual/products/product-media/add-alt-text), or the resource title for article, collection, line item, product, and variant images. However, you can override this default, or set the value if there's no default.

Sintassi:

```liquid
image_url | image_tag: alt: string
```

**Input:**

```liquid
{{ product | image_url: width: 200 | image_tag: alt: "My image's alt text" }}
```

**Output:**

```html
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=200" alt="My image&#39;s alt text" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=200 200w" width="200" height="133">
```

#### HTML attributes

You can specify [HTML attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attributes) by adding a parameter that matches the attribute name, and the desired value.

Sintassi:

```liquid
image_url | image_tag: attribute: string
```

**Input:**

```liquid
{{ product | image_url: width: 200 | image_tag: class: 'custom-class', loading: 'lazy' }}
```

**Output:**

```html
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=200" alt="Health potion" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=200 200w" width="200" height="133" loading="lazy" class="custom-class">
```


## media — media_tag

> Fonte: https://shopify.dev/docs/api/liquid/filters/media_tag

Generates an appropriate HTML tag for a given media object.

### Sintassi

```liquid
media | media_tag
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Parametri

| Parametro | Tipo | Obbligatorio | Posizionale | Descrizione |
|---|---|---|---|---|
| `image_size` | string | no | no | The dimensions of the media's poster image. |

### Esempi

#### Esempio 1

**Input:**

```liquid
{% for media in product.media %}
  {{- media | media_tag }}
{% endfor %}
```

**Output:**

```html
<iframe frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen" src="https://www.youtube.com/embed/vj01PAffOac?controls=1&amp;enablejsapi=1&amp;modestbranding=1&amp;origin=https%3A%2F%2Fpolinas-potent-potions.myshopify.com&amp;playsinline=1&amp;rel=0" title="Potion beats"></iframe>

<video playsinline="playsinline" controls="controls" preload="metadata" aria-label="Potion beats" poster="//polinas-potent-potions.myshopify.com/cdn/shop/products/4edc28a708b7405093a927cebe794f1a.thumbnail.0000000_small.jpg?v=1655255324"><source src="//polinas-potent-potions.myshopify.com/cdn/shop/videos/c/vp/4edc28a708b7405093a927cebe794f1a/4edc28a708b7405093a927cebe794f1a.HD-1080p-7.2Mbps.mp4?v=0" type="video/mp4"><img src="//polinas-potent-potions.myshopify.com/cdn/shop/products/4edc28a708b7405093a927cebe794f1a.thumbnail.0000000_small.jpg?v=1655255324"></video>
```

#### image_size

Specify the dimensions of the media's poster image in pixels.

Sintassi:

```liquid
media | media_tag: image_size: string
```

**Input:**

```liquid
{% for media in product.media %}
  {{- media | media_tag: image_size: '400x' }}
{% endfor %}
```

**Output:**

```html
<iframe frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen" image_size="400x" src="https://www.youtube.com/embed/vj01PAffOac?controls=1&amp;enablejsapi=1&amp;modestbranding=1&amp;origin=https%3A%2F%2Fpolinas-potent-potions.myshopify.com&amp;playsinline=1&amp;rel=0" title="Potion beats"></iframe>

<video playsinline="playsinline" controls="controls" preload="metadata" aria-label="Potion beats" poster="//polinas-potent-potions.myshopify.com/cdn/shop/products/4edc28a708b7405093a927cebe794f1a.thumbnail.0000000_400x.jpg?v=1655255324"><source src="//polinas-potent-potions.myshopify.com/cdn/shop/videos/c/vp/4edc28a708b7405093a927cebe794f1a/4edc28a708b7405093a927cebe794f1a.HD-1080p-7.2Mbps.mp4?v=0" type="video/mp4"><img src="//polinas-potent-potions.myshopify.com/cdn/shop/products/4edc28a708b7405093a927cebe794f1a.thumbnail.0000000_400x.jpg?v=1655255324"></video>
```


## media — model_viewer_tag

> Fonte: https://shopify.dev/docs/api/liquid/filters/model_viewer_tag

Generates a [Google model viewer component](https://modelviewer.dev/) for a given 3D model.

### Sintassi

```liquid
media | model_viewer_tag
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Parametri

| Parametro | Tipo | Obbligatorio | Posizionale | Descrizione |
|---|---|---|---|---|
| `image_size` | string | no | no | The dimensions of the model viewer's poster image. |

### Esempi

#### Esempio 1

**Input:**

```liquid
{% for media in product.media %}
  {% if media.media_type == 'model' %}
    {{ media | model_viewer_tag }}
  {% endif %}
{% endfor %}
```

**Output:**

```html
<model-viewer src="//polinas-potent-potions.myshopify.com/cdn/shop/3d/models/o/eb9388299ce0557c/WaterBottle.glb?v=0" camera-controls="true" style="--poster-color: transparent;" data-shopify-feature="1.12" alt="Potion bottle" poster="//polinas-potent-potions.myshopify.com/cdn/shop/products/WaterBottle_small.jpg?v=1655189057"></model-viewer>
```

#### Model viewer attributes

By default, the model viewer component has the following attributes:

| Attribute | Value |
| --- | --- |
| `alt` | `[alt-text]` - The media's alt text. |
| `poster` | `[preview-image-url]` - The media's preview image URL. |
| `camera-controls` | N/A - Allows for controls via mouse/touch. |

You can override these attributes, or any [supported model viewer component attributes](https://modelviewer.dev/docs/index.html#stagingandcameras-attributes) by adding a parameter that matches the attribute name, and the desired value.

Sintassi:

```liquid
media | model_viewer_tag: attribute: string
```

**Input:**

```liquid
{% for media in product.media %}
  {% if media.media_type == 'model' %}
    {{ media | model_viewer_tag: interaction-policy: 'allow-when-focused' }}
  {% endif %}
{% endfor %}
```

**Output:**

```html
<model-viewer interaction-policy="allow-when-focused" src="//polinas-potent-potions.myshopify.com/cdn/shop/3d/models/o/eb9388299ce0557c/WaterBottle.glb?v=0" camera-controls="true" style="--poster-color: transparent;" data-shopify-feature="1.12" alt="Potion bottle" poster="//polinas-potent-potions.myshopify.com/cdn/shop/products/WaterBottle_small.jpg?v=1655189057"></model-viewer>
```

#### image_size

Specify the dimensions of the model's poster image in pixels.

Sintassi:

```liquid
media | model_viewer_tag: image_size: string
```

**Input:**

```liquid
{% for media in product.media %}
  {% if media.media_type == 'model' %}
    {{ media | model_viewer_tag: image_size: '400x' }}
  {% endif %}
{% endfor %}
```

**Output:**

```html
<model-viewer src="//polinas-potent-potions.myshopify.com/cdn/shop/3d/models/o/eb9388299ce0557c/WaterBottle.glb?v=0" camera-controls="true" style="--poster-color: transparent;" data-shopify-feature="1.12" alt="Potion bottle" poster="//polinas-potent-potions.myshopify.com/cdn/shop/products/WaterBottle_400x.jpg?v=1655189057"></model-viewer>
```


## media — video_tag

> Fonte: https://shopify.dev/docs/api/liquid/filters/video_tag

Generates an HTML `<video>` tag for a given video.

> Note:
> When `mp4` videos are uploaded, Shopify generates an `m3u8` file as an additional [`video_source`](https://shopify.dev/docs/api/liquid/objects/video_source).
> An `m3u8` file enables video players to leverage [HTTP live streaming (HLS)](https://developer.apple.com/streaming/),
> resulting in an optimized video experience based on the user's internet connection. If loop is enabled, the HLS source is not used
> in order to allow progessive download to cache the video.
>
> If the `m3u8` source isn't supported, then the player falls back to the `mp4` source.

### Sintassi

```liquid
media | video_tag
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Parametri

| Parametro | Tipo | Obbligatorio | Posizionale | Descrizione |
|---|---|---|---|---|
| `image_size` | string | no | no | The dimensions of the video's poster image. |

### Esempi

#### Esempio 1

**Input:**

```liquid
{% for media in product.media %}
  {% if media.media_type == 'video' %}
    {{ media | video_tag }}
  {% endif %}
{% endfor %}
```

**Output:**

```html
<video playsinline="playsinline" preload="metadata" aria-label="Potion beats" poster="//polinas-potent-potions.myshopify.com/cdn/shop/products/4edc28a708b7405093a927cebe794f1a.thumbnail.0000000_small.jpg?v=1655255324"><source src="//polinas-potent-potions.myshopify.com/cdn/shop/videos/c/vp/4edc28a708b7405093a927cebe794f1a/4edc28a708b7405093a927cebe794f1a.HD-1080p-7.2Mbps.mp4?v=0" type="video/mp4"><img src="//polinas-potent-potions.myshopify.com/cdn/shop/products/4edc28a708b7405093a927cebe794f1a.thumbnail.0000000_small.jpg?v=1655255324"></video>
```

#### image_size

Specify the dimensions of the video's poster image in pixels.

Sintassi:

```liquid
media | video_tag: image_size: string
```

**Input:**

```liquid
{% for media in product.media %}
  {% if media.media_type == 'video' %}
    {{ media | video_tag: image_size: '400x' }}
  {% endif %}
{% endfor %}
```

**Output:**

```html
<video playsinline="playsinline" preload="metadata" aria-label="Potion beats" poster="//polinas-potent-potions.myshopify.com/cdn/shop/products/4edc28a708b7405093a927cebe794f1a.thumbnail.0000000_400x.jpg?v=1655255324"><source src="//polinas-potent-potions.myshopify.com/cdn/shop/videos/c/vp/4edc28a708b7405093a927cebe794f1a/4edc28a708b7405093a927cebe794f1a.HD-1080p-7.2Mbps.mp4?v=0" type="video/mp4"><img src="//polinas-potent-potions.myshopify.com/cdn/shop/products/4edc28a708b7405093a927cebe794f1a.thumbnail.0000000_400x.jpg?v=1655255324"></video>
```

#### Optional supported HTML5 attributes

`video_tag` supports all [HTML5 video attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video#attributes).
For example:

| Attribute | Value |
| --- | --- |
| `autoplay` | Whether to automatically play the video after it’s loaded. Accepted values:`true`,`false`|
| `loop` | Whether to loop the video. Accepted values:`true`,`false`|
| `muted` | Whether to mute the video’s audio. Accepted values:`true`,`false`|
| `controls` | Whether a user can control the video playback. Accepted values:`true`,`false`|

Sintassi:

```liquid
media | video_tag: attribute: boolean
```

**Input:**

```liquid
{% for media in product.media %}
  {% if media.media_type == 'video' %}
    {{ media | video_tag: autoplay: true, loop: true, muted: true, controls: true }}
  {% endif %}
{% endfor %}
```

**Output:**

```html
<video playsinline="playsinline" autoplay="autoplay" loop="loop" muted="muted" controls="controls" preload="metadata" aria-label="Potion beats" poster="//polinas-potent-potions.myshopify.com/cdn/shop/products/4edc28a708b7405093a927cebe794f1a.thumbnail.0000000_small.jpg?v=1655255324"><source src="//polinas-potent-potions.myshopify.com/cdn/shop/videos/c/vp/4edc28a708b7405093a927cebe794f1a/4edc28a708b7405093a927cebe794f1a.HD-1080p-7.2Mbps.mp4?v=0" type="video/mp4"><img src="//polinas-potent-potions.myshopify.com/cdn/shop/products/4edc28a708b7405093a927cebe794f1a.thumbnail.0000000_small.jpg?v=1655255324"></video>
```


## media — article_img_url

> Fonte: https://shopify.dev/docs/api/liquid/filters/article_img_url

> ⚠️ **Deprecato.** The `article_img_url` filter has been replaced by [`image_url`](https://shopify.dev/docs/api/liquid/filters/image_url).

Returns the [CDN URL](https://shopify.dev/themes/best-practices/performance/platform#shopify-cdn) for an [article's image](https://shopify.dev/docs/api/liquid/objects/article#article-image).

### Sintassi

```liquid
variable | article_img_url
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Parametri

| Parametro | Tipo | Obbligatorio | Posizionale | Descrizione |
|---|---|---|---|---|
| `size` | string | no | sì | The desired image size. |

### Esempi

#### Esempio 1

**Input:**

```liquid
{{ article.image | article_img_url }}
```

**Output:**

```html
//polinas-potent-potions.myshopify.com/cdn/shop/articles/beakers-for-science-with-water_small.jpg?v=1654385193
```

#### size

By default, the `article_img_url` filter returns the `small` version of the image (100 x 100 px). However, you can specify a [size](https://shopify.dev/docs/api/liquid/filters/img_url#img_url-size).

Sintassi:

```liquid
image | article_img_url: string
```

**Input:**

```liquid
{{ article.image | article_img_url: 'large' }}
```

**Output:**

```html
//polinas-potent-potions.myshopify.com/cdn/shop/articles/beakers-for-science-with-water_large.jpg?v=1654385193
```


## media — collection_img_url

> Fonte: https://shopify.dev/docs/api/liquid/filters/collection_img_url

> ⚠️ **Deprecato.** The `collection_img_url` filter has been replaced by [`image_url`](https://shopify.dev/docs/api/liquid/filters/image_url).

Returns the [CDN URL](https://shopify.dev/themes/best-practices/performance/platform#shopify-cdn) for a [collection's image](https://shopify.dev/docs/api/liquid/objects/collection#collection-image).

### Sintassi

```liquid
variable | collection_img_url
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Parametri

| Parametro | Tipo | Obbligatorio | Posizionale | Descrizione |
|---|---|---|---|---|
| `size` | string | no | sì | The desired image size. |

### Esempi

#### Esempio 1

**Input:**

```liquid
{{ collection.image | collection_img_url }}
```

**Output:**

```html
//polinas-potent-potions.myshopify.com/cdn/shop/collections/sale-written-in-lights.jpg?v=1657654130
```

#### The size parameter

By default, the `collection_img_url` filter returns the `small` version of the image (100 x 100 px). However, you can specify a [size](https://shopify.dev/docs/api/liquid/filters/img_url#img_url-size).

Sintassi:

```liquid
image | collection_img_url: string
```

**Input:**

```liquid
{{ collection.image | collection_img_url: 'large' }}
```

**Output:**

```html
//polinas-potent-potions.myshopify.com/cdn/shop/collections/sale-written-in-lights_large.jpg?v=1657654130
```


## media — image_url

> Fonte: https://shopify.dev/docs/api/liquid/filters/image_url

Returns the [CDN URL](https://shopify.dev/themes/best-practices/performance/platform#shopify-cdn) for an image.

You can use the `image_url` filter on the following objects, as well as their `src` property:

- [`article`](https://shopify.dev/docs/api/liquid/objects/article)
- [`collection`](https://shopify.dev/docs/api/liquid/objects/collection)
- [`image`](https://shopify.dev/docs/api/liquid/objects/image)
- [`line_item`](https://shopify.dev/docs/api/liquid/objects/line_item)
- [`product`](https://shopify.dev/docs/api/liquid/objects/product)
- [`variant`](https://shopify.dev/docs/api/liquid/objects/variant)
- [`country`](https://shopify.dev/docs/api/liquid/objects/country)

> Caution:
> You need to specify either a [`width`](https://shopify.dev/docs/api/liquid/filters/image_url#image_url-width) or
> [`height`](https://shopify.dev/docs/api/liquid/filters/image_url#image_url-height) parameter. If neither are specified, then an error is returned.

> Note:
> Regardless of the specified dimensions, an image can never be resized to be larger than its original dimensions.

### Sintassi

```liquid
variable | image_url: width: number, height: number
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Parametri

| Parametro | Tipo | Obbligatorio | Posizionale | Descrizione |
|---|---|---|---|---|
| `crop` | string | no | no | How the image should be cropped to match the desired dimensions. |
| `format` | string | no | no | The file format for the image. |
| `pad_color` | string | no | no | The padding color, if the provided image is smaller than the requested dimensions. |
| `width` | number | sì | no | The desired image width, in pixels. |
| `height` | number | sì | no | The desired image height, in pixels. |

### Esempi

#### Esempio 1

**Input:**

```liquid
{{ product | image_url: width: 450 }}
```

**Output:**

```html
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&width=450
```

#### width

Specify the width of the image up to a maximum of `5760px`. If only the width is specified, then the height is automatically calculated based on the image's dimensions.

Sintassi:

```liquid
variable | image_url: width: number
```

**Input:**

```liquid
{{ product | image_url: width: 450 }}
```

**Output:**

```html
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&width=450
```

#### height

Specify the height of the image up to a maximum of `5760px`. If only the height is specified, then the width is automatically calculated based on the image's dimensions.

Sintassi:

```liquid
variable | image_url: height: number
```

**Input:**

```liquid
{{ product | image_url: height: 450 }}
```

**Output:**

```html
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?height=450&v=1683744744
```

#### crop

Specify which part of the image to show if the specified dimensions result in an aspect ratio that differs from the original. You can use the following values:

- `top`
- `center`
- `bottom`
- `left`
- `right`
- `region`

The default value is `center`.

When using the `region` crop mode, the starting point for the crop is defined by `crop_left` and `crop_top` and extends to the `crop_width` and `crop_height`.
Optionally, to resize the region extracted by the crop, use the `width` and `height` parameters.

> Note:
> Country flags are SVG images and can only be cropped if a value for `format`
> is also provided.

Sintassi:

```liquid
variable | image_url: crop: string
```

**Input:**

```liquid
{{ product | image_url: width: 400, height: 400, crop: 'bottom' }}

{{ product | image_url: crop: 'region', crop_left: 32, crop_top: 32, crop_width: 512, crop_height: 512 }}

{{ product | image_url: crop: 'region', width: 100, height: 100, crop_left: 32, crop_top: 32, crop_width: 512, crop_height: 512 }}
```

**Output:**

```html
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?crop=bottom&height=400&v=1683744744&width=400

//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?crop=region&crop_height=512&crop_left=32&crop_top=32&crop_width=512&v=1683744744

//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?crop=region&crop_height=512&crop_left=32&crop_top=32&crop_width=512&height=100&v=1683744744&width=100
```

#### format

Specify which file format to use for the image. The valid formats are `pjpg` and `jpg`.

It's not practical to convert a lossy image format, like `jpg`, to a lossless image format, like `png`, so Shopify can do
only the following conversions:

- `png` to `jpg`
- `png` to `pjpg`
- `jpg` to `pjpg`

> Note:
> Shopify automatically detects which image formats are supported by the client (e.g. `WebP`, `AVIF`, etc.) and
> selects a file format for optimal quality and file size. When a format is specified, Shopify takes into account
> the features (e.g. progressive, alpha channel) of the specified file format when making the final automatic format selection.
> To learn more, visit https://cdn.shopify.com/.

Sintassi:

```liquid
variable | image_url: format: string
```

**Input:**

```liquid
{{ product | image_url: width: 450, format: 'pjpg' }}
```

**Output:**

```html
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?format=pjpg&v=1683744744&width=450
```

#### pad_color

Specify a color to pad the image if the specified dimensions result in an aspect ratio that differs from the original. The color must be in hexadecimal format (`hex3` or `hex6`).

Sintassi:

```liquid
variable | image_url: pad_color: string
```

**Input:**

```liquid
{{ product | image_url: width: 400, height: 400, pad_color: '000' }}
```

**Output:**

```html
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?height=400&pad_color=000&v=1683744744&width=400
```


## media — img_tag

> Fonte: https://shopify.dev/docs/api/liquid/filters/img_tag

> ⚠️ **Deprecato.** The `img_tag` filter has been replaced by [`image_tag`](https://shopify.dev/docs/api/liquid/filters/image_tag).

Generates an HTML `<img>` tag for a given image URL.

You can also use the `img_tag` filter on the following objects:

- [`article`](https://shopify.dev/docs/api/liquid/objects/article)
- [`collection`](https://shopify.dev/docs/api/liquid/objects/collection)
- [`image`](https://shopify.dev/docs/api/liquid/objects/image)
- [`line_item`](https://shopify.dev/docs/api/liquid/objects/line_item)
- [`product`](https://shopify.dev/docs/api/liquid/objects/product)
- [`variant`](https://shopify.dev/docs/api/liquid/objects/variant)

### Sintassi

```liquid
string | img_tag
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Parametri

| Parametro | Tipo | Obbligatorio | Posizionale | Descrizione |
|---|---|---|---|---|
| `alt` | string | no | sì | The image's alt text. |
| `class` | string | no | sì | The desired `class` attribute. |
| `size` | string | no | sì | The desired image size. |

### Esempi

#### Esempio 1

**Input:**

```liquid
{{ product | img_tag }}
```

**Output:**

```html
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_small.jpg?v=1683744744" alt="" />
```

#### Optional parameters

The `img_tag` filter accepts 3 unnamed parameters, separated by commas, to specify the `alt` and `class` attributes, and the
[size](https://shopify.dev/docs/api/liquid/filters/img_url#img_url-size) of the image. Because the parameters are read in that order, you must include a value for each parameter before the last
parameter you want to specify. If you don't want to include a parameter that precedes one that you do want to include, then
you can set the value to an empty string.

> Note:
> The `size` attribute of the `img_tag` filter can't be used in conjunction with the [`img_url` filter](https://shopify.dev/docs/api/liquid/filters/img_url).
> If both are used, then the `img_url` filter will override the `size` parameter of the `img_tag` filter.

Sintassi:

```liquid
variable | img_tag: string, string, string
```

**Input:**

```liquid
{{ product | img_tag: 'image alt text', '', '450x450' }}
```

**Output:**

```html
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_450x450.jpg?v=1683744744" alt="image alt text" class="" />
```


## media — img_url

> Fonte: https://shopify.dev/docs/api/liquid/filters/img_url

> ⚠️ **Deprecato.** The `img_url` filter has been replaced by [`image_url`](https://shopify.dev/docs/api/liquid/filters/image_url).

Returns the [CDN URL](https://shopify.dev/themes/best-practices/performance/platform#shopify-cdn) for an image.

You can use the `img_url` filter on the following objects:

- [`article`](https://shopify.dev/docs/api/liquid/objects/article)
- [`collection`](https://shopify.dev/docs/api/liquid/objects/collection)
- [`image`](https://shopify.dev/docs/api/liquid/objects/image)
- [`line_item`](https://shopify.dev/docs/api/liquid/objects/line_item)
- [`product`](https://shopify.dev/docs/api/liquid/objects/product)
- [`variant`](https://shopify.dev/docs/api/liquid/objects/variant)

### Sintassi

```liquid
variable | img_url
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Parametri

| Parametro | Tipo | Obbligatorio | Posizionale | Descrizione |
|---|---|---|---|---|
| `size` | string | no | sì | The desired image size. |
| `crop` | string | no | no | The part of the image to show if the specified image has an aspect ratio that differs from the original. |
| `scale` | number | no | no | The desired pixel density. |
| `format` | string | no | no | The desired image format. |

### Esempi

#### Esempio 1

**Input:**

```liquid
{{ product | img_url }}
```

**Output:**

```html
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_small.jpg?v=1683744744
```

#### size

The size parameter allows you to specify the dimensions of the image up to a maximum of 5760 x 5760 px. You can specify only the width, only the height, or both, and you can also use the following named sizes:

| Name | Dimensions |
| --- | --- |
| `pico` | `16x16 px` |
| `icon` | `32x32 px` |
| `thumb` | `50x50 px` |
| `small` | `100x100 px` |
| `compact` | `160x160 px` |
| `medium` | `240x240 px` |
| `large` |`480x480 px` |
| `grande` | `600x600 px` |
| `original`<br>`master` | `1024x1024 px` |

Sintassi:

```liquid
variable | img_url: string
```

**Input:**

```liquid
{{ product | img_url: '480x' }}

{{ product | img_url: 'x480' }}

{{ product | img_url: '480x480' }}

{{ product | img_url: 'large' }}
```

**Output:**

```html
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_480x.jpg?v=1683744744

//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_x480.jpg?v=1683744744

//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_480x480.jpg?v=1683744744

//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_large.jpg?v=1683744744
```

#### crop

The `crop` parameter allows you to specify which part of the image to show if the specified dimensions result in an aspect ratio that differs from the original. You can use the following values:

- `top`
- `center`
- `bottom`
- `left`
- `right`

The default value is `center`.

Sintassi:

```liquid
variable | img_url: crop: string
```

**Input:**

```liquid
{{ product | img_url: crop: 'bottom' }}
```

**Output:**

```html
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_small.jpg?v=1683744744
```

#### format

Specify which file format to use for the image. The valid formats are `pjpg` and `jpg`.

It's not practical to convert a lossy image format, like `jpg`, to a lossless image format, like `png`, so this filter does
only the following conversions:

- `png` to `jpg`
- `png` to `pjpg`
- `jpg` to `pjpg`

> Note:
> Shopify automatically detects which image formats are supported by the client (e.g. `WebP`, `AVIF`, etc.) and
> selects a file format for optimal quality and file size. When a format is specified, Shopify takes into account
> the features (e.g. progressive, alpha channel) of the specified file format when making the final automatic format selection.
> To learn more, visit https://cdn.shopify.com/.

Sintassi:

```liquid
variable | img_url: format: string
```

**Input:**

```liquid
{{ product | img_url: format: 'pjpg' }}
```

**Output:**

```html
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_small.jpg?v=1683744744
```

#### scale

Specify the pixel density of the image. The valid densities are 2 and 3.

Sintassi:

```liquid
variable | img_url: scale: number
```

**Input:**

```liquid
{{ product | img_url: scale: 2 }}
```

**Output:**

```html
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_small.jpg?v=1683744744
```


## media — product_img_url

> Fonte: https://shopify.dev/docs/api/liquid/filters/product_img_url

> ⚠️ **Deprecato.** The `product_img_url` filter has been replaced by [`image_url`](https://shopify.dev/docs/api/liquid/filters/image_url).

Returns the [CDN URL](https://shopify.dev/themes/best-practices/performance/platform#shopify-cdn) for a [product image](https://shopify.dev/docs/api/liquid/objects/product).

This can be the product's `featured_image` or any image from the `images` array.

### Sintassi

```liquid
variable | product_img_url
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Parametri

| Parametro | Tipo | Obbligatorio | Posizionale | Descrizione |
|---|---|---|---|---|
| `size` | string | no | sì | The desired image size. |

### Esempi

#### Esempio 1

**Input:**

```liquid
{{ product.featured_image | product_img_url }}
```

**Output:**

```html
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_small.jpg?v=1683744744
```

#### The size parameter

By default, the `product_img_url` filter returns the `small` version of the image (100 x 100 px). However, you can specify a [size](https://shopify.dev/docs/api/liquid/filters/img_url#img_url-size).

Sintassi:

```liquid
image | product_img_url: string
```

**Input:**

```liquid
{{ product.images[0] | product_img_url: 'large' }}
```

**Output:**

```html
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_large.jpg?v=1683744744
```


# Categoria: metafield

## metafield — metafield_tag

> Fonte: https://shopify.dev/docs/api/liquid/filters/metafield_tag

Generates an HTML element to host the data from a [`metafield` object](https://shopify.dev/docs/api/liquid/objects/metafield).
The type of element that's generated differs depending on the type of metafield.

> Note:
> The `metafield_tag` filter doesn't currently support list metafields other than `list.single_line_text_field` and `list.metaobject_reference`.

### Sintassi

```liquid
metafield | metafield_tag
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Parametri

| Parametro | Tipo | Obbligatorio | Posizionale | Descrizione |
|---|---|---|---|---|
| `field` | string | no | no | Specifies which field should be used. Only applicable to `list.metaobject_reference` and `metaobject_reference` types. |
| `list_format` | string | no | no | The desired list format. Accepts `unordered` or `ordered`. Default: `unordered`. |

### Esempi

#### Basic types

Most metafield types return a simple HTML element:

| Type | Element | Attributes |
| --- | --- | --- |
| `boolean` | `<span>` | `class="metafield-boolean"` |
| `collection_reference` | `<a>` | `class="metafield-collection_reference"` |
| `color` | `<span>` | `class="metafield-color"` |
| `date` | `<time>` | `datetime="<the metafield value>"`<br><br>`class="metafield-date"`<br><br>Value is localized to the customer |
| `date_time` | `<time>` | `datetime="<the metafield value>"`<br><br>`class="metafield-date"`<br><br>Value is localized to the customer |
| `json` | `<script>` | `type="application/json"`<br><br>`class="metafield-json"` |
| `money` | `<span>` | `class="metafield-money"`<br><br>Value is formatted using the store's [HTML with currency setting](https://help.shopify.com/manual/payments/currency-formatting) |
| `multi_line_text_field` | `<span>` | `class="metafield-multi_line_text_field"` |
| `number_decimal` | `<span>` | `class="metafield-number_decimal"` |
| `number_integer` | `<span>` | `class="metafield-number_integer"` |
| `page_reference` | `<a>` | `class="metafield-page_reference"` |
| `product_reference` | `<a>` | `class="metafield-page_reference"` |
| `rating` | `<span>` | `class="metafield-rating"` | |
| `single_line_text_field` | `<span>` | `class="metafield-single_line_text_field"` |
| `url` | `<a>` | `class="metafield-url"` |
| `variant_reference` | `<a>` | `class="metafield-variant_reference"` |
| `rich_text_field` | `<div>` | `class="metafield-rich_text_field"` |

**Input:**

```liquid
<!-- boolean -->
{{ product.metafields.information.seasonal | metafield_tag }}

<!-- collection_reference -->
{{ product.metafields.information.related_collection | metafield_tag }}

<!-- color -->
{{ product.metafields.details.potion_color | metafield_tag }}

<!-- date -->
{{ product.metafields.information.expiry | metafield_tag }}

<!-- date_time -->
{{ product.metafields.information.brew_date | metafield_tag }}

<!-- json -->
{{ product.metafields.information.burn_temperature | metafield_tag }}

<!-- money -->
{{ product.metafields.details.price_per_ml | metafield_tag }}

<!-- multi_line_text_field -->
{{ product.metafields.information.shipping | metafield_tag }}

<!-- number_decimal -->
{{ product.metafields.information.salinity | metafield_tag }}

<!-- number_integer -->
{{ product.metafields.information.doses_per_day | metafield_tag }}

<!-- page_reference -->
{{ product.metafields.information.dosage | metafield_tag }}

<!-- product_reference -->
{{ product.metafields.information.related_product | metafield_tag }}

<!-- rating -->
{{ product.metafields.details.rating | metafield_tag }}

<!-- single_line_text_field -->
{{ product.metafields.information.directions | metafield_tag }}

<!-- url -->
{{ product.metafields.information.health | metafield_tag }}

<!-- variant_reference -->
{{ product.metafields.information.best_seller | metafield_tag }}

<!-- rich_text_field -->
{{ product.metafields.information.rich_description | metafield_tag }}
```

**Output:**

```html
<!-- boolean -->
<span class="metafield-boolean">false</span>

<!-- collection_reference -->
<a href="/collections/sale-potions" class="metafield-collection_reference">Sale potions</a>

<!-- color -->
<span class="metafield-color">#ff0000</span>

<!-- date -->
<time datetime="2040-01-01" class="metafield-date">January 1, 2040</time>

<!-- date_time -->
<time datetime="2022-06-22T13:00:00Z" class="metafield-date_time">Jun 22, 2022, 1:00 pm</time>

<!-- json -->
<script type="application/json" class="metafield-json">{"temperature":"700","unit":"degrees","scale":"Fahrenheit"}</script>

<!-- money -->
<span class="metafield-money">$0.10 CAD</span>

<!-- multi_line_text_field -->
<span class="metafield-multi_line_text_field">All health potions are made to order, so it might take up to 2 weeks before your order can be shipped.<br />
<br />
Thanks for your patience!</span>

<!-- number_decimal -->
<span class="metafield-number_decimal">8.4</span>

<!-- number_integer -->
<span class="metafield-number_integer">3</span>

<!-- page_reference -->
<a href="/pages/potion-dosages" class="metafield-page_reference">Potion dosages</a>

<!-- product_reference -->
<a href="/products/dried-chamomile" class="metafield-product_reference">Dried chamomile</a>

<!-- rating -->
<span class="metafield-rating">4.5</span>

<!-- single_line_text_field -->
<span class="metafield-single_line_text_field">Take with a meal.</span>

<!-- url -->
<a href="https://www.canada.ca/en/health-canada/services/food-nutrition/legislation-guidelines/acts-regulations/canada-food-drugs.html" class="metafield-url">www.canada.ca/en/health-canada/services/food-nutrition/legislation-guidelines/acts-regulations/canada-food-drugs.html</a>

<!-- variant_reference -->
<a href="/products/health-potion?variant=39897499762753" class="metafield-variant_reference">S / Medium</a>

<!-- rich_text_field -->
<div class="metafield-rich_text_field"><h3>Are you low on health? Well we&#39;ve got the potion just for you!</h3><p>Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!</p></div>
```

#### Complex types

The following metafield types return nested elements, or different elements depending on the metafield contents:

- [`dimension`](https://shopify.dev/docs/api/liquid/filters/metafield_tag#metafield_tag-dimension)
- [`file_reference`](https://shopify.dev/docs/api/liquid/filters/metafield_tag#metafield_tag-file_reference)
- [`list.metaobject_reference`](https://shopify.dev/docs/api/liquid/filters/metafield_tag#metafield_tag-list.metaobject_reference)
- [`list.single_line_text_field`](https://shopify.dev/docs/api/liquid/filters/metafield_tag#metafield_tag-list.single_line_text_field)
- [`metaobject_reference`](https://shopify.dev/docs/api/liquid/filters/metafield_tag#metafield_tag-metaobject_reference)
- [`volume`](https://shopify.dev/docs/api/liquid/filters/metafield_tag#metafield_tag-volume)
- [`weight`](https://shopify.dev/docs/api/liquid/filters/metafield_tag#metafield_tag-weight)

#### dimension

Outputs a `<span>` element with the following attribute:

| Attribute | Value |
| --- | --- |
| `class` | `metafield-dimension` |

The `<span>` element contains the following child elements:

| Child element | HTML element | Attributes |
| --- | --- | --- |
| The dimension value.<br><br>If it's a decimal with more than two places, then it'll be formatted to have a precision of two with trailing zeros removed. | `<span>` | `class="metafield-dimension_value"` |
| The dimension unit. | `<span>` | `class="metafield-dimension_unit"` |

**Input:**

```liquid
{{ product.metafields.details.scale_width | metafield_tag }}
```

**Output:**

```html
<span class="metafield-dimension"><span class="metafield-dimension_value">3 </span><span class="metafield-dimension_unit">cm</span></span>
```

#### file_reference

The output varies depending on the type of file. There are the following categories of file type:

| File type | Description |
| --- | --- |
| Image | Images in the format of `jpg`, `png`, `gif`, `heic`, and `webp`. |
| Video | Videos in the format of `mov`, and `mp4`. |
| Other | Any other file type. |

##### Image

Outputs an `<img>` element with the following attributes:

| Attribute | Value |
| --- | --- |
| `src` | The image's URL. |
| `alt` | The image's alt text. |
| `class` | `metafield-file_reference` |

##### Video

Outputs a `<video>` element with the following attributes:

| Attribute | Value |
| --- | --- |
| `src` | The video's URL. |
| `poster` | The video's preview image (poster) URL. |
| `playsinline` | N/A - Indicates the video will be played "inline" within the element's playback area. |
| `preload` | `metadata` - Only metadata is pre-fetched before the video is played. |

The `<video>` element contains the following child elements:

| Child element | HTML element | Attributes |
| --- | --- | --- |
| The video's multimedia playlist source, for [HTTP live streaming (HLS)](https://developer.apple.com/streaming/) | `<source>` | `src="<the video's m3u8 source URL>"`<br><br>`type="application/x-mpegURL"` |
| The video's original source | `<source>` | `src="<the video's source URL>"`<br><br>`type="<the video's original source MIME type>"` |
| The video's preview (poster) image | `<img>` | `src="<the video's preview image URL>"` |

##### Other

Outputs an `<a>` element with a link to the file and the following attribute:

| Attribute | Value |
| --- | --- |
| `class` | `metafield-file_reference` |

The `<a>` element contains an `<img>` element for the file's [preview image](https://shopify.dev/docs/api/liquid/objects/generic_file#generic_file-preview_image) with the following attributes:

| Attribute | Value |
| --- | --- |
| `src` | The file's preview image URL. |
| `loading` | `lazy` - The image isn't loaded until it's almost in view. |

**Input:**

```liquid
<!-- Image -->
{{ product.metafields.information.promo_image | metafield_tag }}

<!-- Video -->
{{ product.metafields.information.promo_video | metafield_tag }}

<!-- Other -->
{{ product.metafields.information.disclaimers | metafield_tag }}
```

**Output:**

```html
<!-- Image -->
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/potions-header.png?v=1650325393" loading="lazy" class="metafield-file_reference">

<!-- Video -->
<video playsinline="playsinline" preload="metadata" poster="//polinas-potent-potions.myshopify.com/cdn/shop/files/preview_images/4733c31cd9d744f6994f61458fda85e6.thumbnail.0000000_small.jpg?v=1655257099"><source src="//polinas-potent-potions.myshopify.com/cdn/shop/videos/c/vp/4733c31cd9d744f6994f61458fda85e6/4733c31cd9d744f6994f61458fda85e6.HD-1080p-7.2Mbps.mp4?v=0" type="video/mp4"><img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/preview_images/4733c31cd9d744f6994f61458fda85e6.thumbnail.0000000_small.jpg?v=1655257099"></video>

<!-- Other -->
<a href="//polinas-potent-potions.myshopify.com/cdn/shop/files/disclaimer.pdf?v=9043651738044769859" class="metafield-file_reference"><img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/preview_images/document-7f23220eb4be7eeaa6e225738b97d943f22e74367cd2d7544fc3b37fb36acd71.png?v=1653087800" loading="lazy"></a>
```

#### list.metaobject_reference

Outputs a `<ul>` element by default with the following attribute:

| Attribute | Value |
| --- | --- |
| `class` | `metafield-single_line_text_field-array` |

The `<ul>` element contains an `<li>` element for each metaobject in the list with a `class` of `metafield-single_line_text_field`. The required `field` parameter specifies which field should be rendered for each metaobject. The `field` parameter can reference only metafields of type `single_line_text_field`.

To output an `<ol>` element, pass the `list_format` parameter with a value of `ordered`.

Sintassi:

```liquid
metafield | metafield_tag: field: string
```

**Input:**

```liquid
<!-- <ul> element -->
{{ product.metafields.information.ingredients | metafield_tag: field: 'name' }}

<!-- <ol> element -->
{{ product.metafields.information.ingredients | metafield_tag: field: 'name', list_format: 'ordered' }}
```

**Output:**

```html
<!-- <ul> element -->
<ul class="metafield-single_line_text_field-array"><li class="metafield-single_line_text_field">Spinach</li><li class="metafield-single_line_text_field">Kale</li><li class="metafield-single_line_text_field">Mushrooms</li></ul>

<!-- <ol> element -->
<ol class="metafield-single_line_text_field-array"><li class="metafield-single_line_text_field">Spinach</li><li class="metafield-single_line_text_field">Kale</li><li class="metafield-single_line_text_field">Mushrooms</li></ol>
```

#### list.single_line_text_field

Outputs a `<ul>` element by default with the following attribute:

| Attribute | Value |
| --- | --- |
| `class` | `metafield-single_line_text_field-array` |

The `<ul>` element contains an `<li>` element for each item in the list with a `class` of `metafield-single_line_text_field`.

To output an `<ol>` element, pass the `list_format` parameter with a value of `ordered`.

**Input:**

```liquid
<!-- <ul> element -->
{{ product.metafields.information.pickup_locations | metafield_tag }}

<!-- <ol> element -->
{{ product.metafields.information.pickup_locations | metafield_tag: list_format: 'ordered' }}
```

**Output:**

```html
<!-- <ul> element -->
<ul class="metafield-single_line_text_field-array"><li class="metafield-single_line_text_field">Ottawa</li><li class="metafield-single_line_text_field">Toronto</li><li class="metafield-single_line_text_field">Montreal</li><li class="metafield-single_line_text_field">Vancouver</li></ul>

<!-- <ol> element -->
<ol class="metafield-single_line_text_field-array"><li class="metafield-single_line_text_field">Ottawa</li><li class="metafield-single_line_text_field">Toronto</li><li class="metafield-single_line_text_field">Montreal</li><li class="metafield-single_line_text_field">Vancouver</li></ol>
```

#### metaobject_reference

Outputs an HTML element for the metaobject field specified by the required `field` parameter. The `field` parameter can reference only metafields of type `single_line_text_field`.

Sintassi:

```liquid
metafield | metafield_tag: field: string
```

**Input:**

```liquid
{{ product.metafields.information.primary_ingredient | metafield_tag: field: 'name' }}
```

**Output:**

```html
<span class="metafield-single_line_text_field">Spinach</span>
```

#### volume

Outputs a `<span>` element with the following attribute:

| Attribute | Value |
| --- | --- |
| `class` | `metafield-volume` |

The `<span>` element contains the following child elements:

| Child element | HTML element | Attributes |
| --- | --- | --- |
| The volume value.<br><br>If it's a decimal with more than two places, then it'll be formatted to have a precision of two with trailing zeros removed. | `<span>` | `class="metafield-volume_value"` |
| The volume unit. | `<span>` | `class="metafield-volume_unit"` |

**Input:**

```liquid
{{ product.metafields.details.milk_container_volume | metafield_tag }}
```

**Output:**

```html
<span class="metafield-volume"><span class="metafield-volume_value">500 </span><span class="metafield-volume_unit">mL</span></span>
```

#### weight

Outputs a `<span>` element with the following attribute:

| Attribute | Value |
| --- | --- |
| `class` | `metafield-weight` |

The `<span>` element contains the following child elements:

| Child element | HTML element | Attributes |
| --- | --- | --- |
| The weight value.<br><br>If it's a decimal with more than two places, then it'll be formatted to have a precision of two with trailing zeros removed. | `<span>` | `class="metafield-weight_value"` |
| The weight unit. | `<span>` | `class="metafield-weight_unit"` |

**Input:**

```liquid
{{ product.metafields.details.chamomile_base_weight | metafield_tag }}
```

**Output:**

```html
<span class="metafield-weight"><span class="metafield-weight_value">50 </span><span class="metafield-weight_unit">g</span></span>
```


## metafield — metafield_text

> Fonte: https://shopify.dev/docs/api/liquid/filters/metafield_text

Generates a text version of the data from a [`metafield` object](https://shopify.dev/docs/api/liquid/objects/metafield).

> Note:
> The `metafield_text` filter doesn't currently support list metafields other than `list.single_line_text_field` and `list.metaobject_reference`.

### Sintassi

```liquid
metafield | metafield_text
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Parametri

| Parametro | Tipo | Obbligatorio | Posizionale | Descrizione |
|---|---|---|---|---|
| `field` | string | no | no | Specifies which field should be used. Only applicable to types `list.metaobject_reference` and `metaobject_reference`. |

### Esempi

#### Basic types

The following outlines the output for each metafield type:

| Metafield type | Output |
| --- | --- |
| `single_line_text_field` | The metafield text. |
| `multi_line_text_field` | The metafield text. |
| `page_reference` | The page title. |
| `product_reference` | The product title. |
| `collection_reference` | The collection title. |
| `variant_reference` | The variant title. |
| `file_reference` | The file URL. |
| `number_integer` | The number. |
| `number_decimal` | The number. |
| `date` | The date. |
| `date-time` | The date and time. |
| `url` | The URL. |
| `json` | The JSON. |
| `boolean` | The boolean value. |
| `color` | The color value. |
| `weight` | The weight value and unit.<br><br>If the value is a decimal with more than two places, then it'll be formatted to have a precision of two with trailing zeros removed. |
| `volume` | The volume value and unit.<br><br>If the value is a decimal with more than two places, then it'll be formatted to have a precision of two with trailing zeros removed. |
| `dimension` | The dimension value and unit.<br><br>If the value is a decimal with more than two places, then it'll be formatted to have a precision of two with trailing zeros removed. |
| `rating` | The rating value. |
| `list.single_line_text_field` | The metafield values in sentence format.<br><br>For example, if you had the values `Toronto`, `Ottawa`, and `Vancouver`, then the output would be:<br><br>`Toronto, Ottawa, and Vancouver` |
| `money` | The money value, formatted using the store's [**HTML with currency** setting](https://help.shopify.com/manual/payments/currency-formatting). |
| `rich_text_field` | The rich text value as simple text. |

**Input:**

```liquid
{{ product.metafields.information.dosage | metafield_text }}
```

**Output:**

```html
Potion dosages
```

#### Complex types

The following metafield types produce different output depending on the provided `field` parameter:

- [`list.metaobject_reference`](https://shopify.dev/docs/api/liquid/filters/metafield_text#metafield_text-list.metaobject_reference)
- [`metaobject_reference`](https://shopify.dev/docs/api/liquid/filters/metafield_text#metafield_text-metaobject_reference)

#### list.metaobject_reference

Outputs the list of metaobjects in sentence format. The required `field` parameter specifies which field should be rendered for each metaobject. The `field` parameter can reference only metafields of type `single_line_text_field`.

Sintassi:

```liquid
metafield | metafield_text: field: string
```

**Input:**

```liquid
{{ product.metafields.information.ingredients | metafield_text: field: 'name' }}
```

**Output:**

```html
Spinach, Kale, and Mushrooms
```

#### metaobject_reference

Outputs the metafield text for the metaobject field specified by the required `field` parameter. The `field` parameter can reference only metafields of type `single_line_text_field`.

Sintassi:

```liquid
metafield | metafield_text: field: string
```

**Input:**

```liquid
{{ product.metafields.information.primary_ingredient | metafield_tag: field: 'name' }}
```

**Output:**

```html
<span class="metafield-single_line_text_field">Spinach</span>
```


# Categoria: money

## money — money

> Fonte: https://shopify.dev/docs/api/liquid/filters/money

Formats a given price based on the store's [**HTML without currency** setting](https://help.shopify.com/manual/payments/currency-formatting).

### Sintassi

```liquid
number | money
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{{ product.price | money }}
```

**Output:**

```html
$10.00
```


## money — money_amount

> Fonte: https://shopify.dev/docs/api/liquid/filters/money_amount

Formats a given price as a plain decimal string, without currency symbols, thousand separators, or locale formatting.

### Sintassi

```liquid
number | money_amount
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{{ product.price | money_amount }}
```

**Output:**

```html
10.0
```


## money — money_with_currency

> Fonte: https://shopify.dev/docs/api/liquid/filters/money_with_currency

Formats a given price based on the store's [**HTML with currency** setting](https://help.shopify.com/manual/payments/currency-formatting).

### Sintassi

```liquid
number | money_with_currency
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{{ product.price | money_with_currency }}
```

**Output:**

```html
$10.00 CAD
```


## money — money_without_currency

> Fonte: https://shopify.dev/docs/api/liquid/filters/money_without_currency

Formats a given price based on the store's [**HTML without currency** setting](https://help.shopify.com/manual/payments/currency-formatting), without the currency symbol.

### Sintassi

```liquid
number | money_without_currency
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{{ product.price | money_without_currency }}
```

**Output:**

```html
10.00
```


## money — money_without_trailing_zeros

> Fonte: https://shopify.dev/docs/api/liquid/filters/money_without_trailing_zeros

Formats a given price based on the store's [**HTML without currency** setting](https://help.shopify.com/manual/payments/currency-formatting), excluding the decimal separator
(either `.` or `,`) and trailing zeros.

If the price has a non-zero decimal value, then the output is the same as the [`money` filter](https://shopify.dev/docs/api/liquid/filters#money).

### Sintassi

```liquid
number | money_without_trailing_zeros
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{{ product.price | money_without_trailing_zeros }}
```

**Output:**

```html
$10
```


# Categoria: payment

## payment — payment_button

> Fonte: https://shopify.dev/docs/api/liquid/filters/payment_button

Generates an HTML container to host [accelerated checkout buttons](https://help.shopify.com/manual/online-store/dynamic-checkout)
for a product. The `payment_button` filter must be used on the `form` object within a [product form](https://shopify.dev/docs/api/liquid/tags/form#form-product).

### Sintassi

```liquid
form | payment_button
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{% form 'product', product %}
  {{ form | payment_button }}
{% endform %}
```

**Output:**

```html
<form method="post" action="/cart/add" id="product_form_6786188247105" accept-charset="UTF-8" class="shopify-product-form" enctype="multipart/form-data"><input type="hidden" name="form_type" value="product" /><input type="hidden" name="utf8" value="✓" />
  <div data-shopify="payment-button" class="shopify-payment-button"> <shopify-accelerated-checkout recommended="null" fallback="{&quot;supports_subs&quot;:true,&quot;supports_def_opts&quot;:true,&quot;name&quot;:&quot;buy_it_now&quot;,&quot;wallet_params&quot;:{}}" access-token="7be588c245f69602e5db198d53fcfde5" buyer-country="CA" buyer-locale="en" buyer-currency="CAD" variant-params="[{&quot;id&quot;:39897499729985,&quot;requiresShipping&quot;:true},{&quot;id&quot;:39897499762753,&quot;requiresShipping&quot;:true},{&quot;id&quot;:39897499795521,&quot;requiresShipping&quot;:true},{&quot;id&quot;:39897499828289,&quot;requiresShipping&quot;:true},{&quot;id&quot;:39897499861057,&quot;requiresShipping&quot;:true},{&quot;id&quot;:39897499893825,&quot;requiresShipping&quot;:true},{&quot;id&quot;:39897499926593,&quot;requiresShipping&quot;:true},{&quot;id&quot;:39897499959361,&quot;requiresShipping&quot;:true},{&quot;id&quot;:39897499992129,&quot;requiresShipping&quot;:true}]" shop-id="56174706753" enabled-flags="[&quot;98c6d7e1&quot;]" > <div class="shopify-payment-button__button" role="button" disabled aria-hidden="true" style="background-color: transparent; border: none"> <div class="shopify-payment-button__skeleton">&nbsp;</div> </div> </shopify-accelerated-checkout> <small id="shopify-buyer-consent" class="hidden" aria-hidden="true" data-consent-type="subscription"> This item is a deferred, subscription, or recurring purchase. By continuing, I agree to the <span id="shopify-subscription-policy-button">cancellation policy</span> and authorize you to charge my payment method at the prices, frequency and dates listed on this page until my order is fulfilled or I cancel, if permitted. </small> </div>
<input type="hidden" name="product-id" value="6786188247105" /></form>
```


## payment — payment_terms

> Fonte: https://shopify.dev/docs/api/liquid/filters/payment_terms

Generates the HTML for the [Shop Pay Installments banner](https://shopify.dev/themes/pricing-payments/installments).

The `payment_terms` filter must be used on the `form` object within a [product form](https://shopify.dev/docs/api/liquid/tags/form#form-product) or
[cart form](https://shopify.dev/docs/api/liquid/tags/form#form-cart).

```liquid
{% form 'product', product %}
  {{ form | payment_terms }}
{% endform %}
```

```liquid
{% form 'cart', cart %}
  {{ form | payment_terms }}
{% endform %}
```

### Sintassi

```liquid
form | payment_terms
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)


## payment — payment_type_img_url

> Fonte: https://shopify.dev/docs/api/liquid/filters/payment_type_img_url

Returns the URL for an SVG image of a given [payment type](https://shopify.dev/docs/api/liquid/objects/shop#shop-enabled_payment_types).

### Sintassi

```liquid
string | payment_type_img_url
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{% for type in shop.enabled_payment_types %}
<img src="{{ type | payment_type_img_url }}" width="50" height="50" />
{% endfor %}
```

**Output:**

```html
<img src="//polinas-potent-potions.myshopify.com/cdn/shopifycloud/storefront/assets/payment_icons/visa-65d650f7.svg" width="50" height="50" />

<img src="//polinas-potent-potions.myshopify.com/cdn/shopifycloud/storefront/assets/payment_icons/master-54b5a7ce.svg" width="50" height="50" />

<img src="//polinas-potent-potions.myshopify.com/cdn/shopifycloud/storefront/assets/payment_icons/american_express-1efdc6a3.svg" width="50" height="50" />

<img src="//polinas-potent-potions.myshopify.com/cdn/shopifycloud/storefront/assets/payment_icons/paypal-a7c68b85.svg" width="50" height="50" />

<img src="//polinas-potent-potions.myshopify.com/cdn/shopifycloud/storefront/assets/payment_icons/diners_club-678e3046.svg" width="50" height="50" />

<img src="//polinas-potent-potions.myshopify.com/cdn/shopifycloud/storefront/assets/payment_icons/discover-59880595.svg" width="50" height="50" />
```


## payment — payment_type_svg_tag

> Fonte: https://shopify.dev/docs/api/liquid/filters/payment_type_svg_tag

Generates an HTML `<svg>` tag for a given [payment type](https://shopify.dev/docs/api/liquid/objects/shop#shop-enabled_payment_types).

### Sintassi

```liquid
string | payment_type_svg_tag
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Parametri

| Parametro | Tipo | Obbligatorio | Posizionale | Descrizione |
|---|---|---|---|---|
| `class` | string | no | no | The desired `class` attribute. |

### Esempi

#### Esempio 1

**Input:**

```liquid
{% for type in shop.enabled_payment_types -%}
  {{ type | payment_type_svg_tag }}
{% endfor %}
```

**Output:**

```html
<svg viewBox="0 0 38 24" xmlns="http://www.w3.org/2000/svg" role="img" width="38" height="24" aria-labelledby="pi-visa"><title id="pi-visa">Visa</title><path opacity=".07" d="M35 0H3C1.3 0 0 1.3 0 3v18c0 1.7 1.4 3 3 3h32c1.7 0 3-1.3 3-3V3c0-1.7-1.4-3-3-3z"/><path fill="#fff" d="M35 1c1.1 0 2 .9 2 2v18c0 1.1-.9 2-2 2H3c-1.1 0-2-.9-2-2V3c0-1.1.9-2 2-2h32"/><path d="M28.3 10.1H28c-.4 1-.7 1.5-1 3h1.9c-.3-1.5-.3-2.2-.6-3zm2.9 5.9h-1.7c-.1 0-.1 0-.2-.1l-.2-.9-.1-.2h-2.4c-.1 0-.2 0-.2.2l-.3.9c0 .1-.1.1-.1.1h-2.1l.2-.5L27 8.7c0-.5.3-.7.8-.7h1.5c.1 0 .2 0 .2.2l1.4 6.5c.1.4.2.7.2 1.1.1.1.1.1.1.2zm-13.4-.3l.4-1.8c.1 0 .2.1.2.1.7.3 1.4.5 2.1.4.2 0 .5-.1.7-.2.5-.2.5-.7.1-1.1-.2-.2-.5-.3-.8-.5-.4-.2-.8-.4-1.1-.7-1.2-1-.8-2.4-.1-3.1.6-.4.9-.8 1.7-.8 1.2 0 2.5 0 3.1.2h.1c-.1.6-.2 1.1-.4 1.7-.5-.2-1-.4-1.5-.4-.3 0-.6 0-.9.1-.2 0-.3.1-.4.2-.2.2-.2.5 0 .7l.5.4c.4.2.8.4 1.1.6.5.3 1 .8 1.1 1.4.2.9-.1 1.7-.9 2.3-.5.4-.7.6-1.4.6-1.4 0-2.5.1-3.4-.2-.1.2-.1.2-.2.1zm-3.5.3c.1-.7.1-.7.2-1 .5-2.2 1-4.5 1.4-6.7.1-.2.1-.3.3-.3H18c-.2 1.2-.4 2.1-.7 3.2-.3 1.5-.6 3-1 4.5 0 .2-.1.2-.3.2M5 8.2c0-.1.2-.2.3-.2h3.4c.5 0 .9.3 1 .8l.9 4.4c0 .1 0 .1.1.2 0-.1.1-.1.1-.1l2.1-5.1c-.1-.1 0-.2.1-.2h2.1c0 .1 0 .1-.1.2l-3.1 7.3c-.1.2-.1.3-.2.4-.1.1-.3 0-.5 0H9.7c-.1 0-.2 0-.2-.2L7.9 9.5c-.2-.2-.5-.5-.9-.6-.6-.3-1.7-.5-1.9-.5L5 8.2z" fill="#142688"/></svg>
<svg viewBox="0 0 38 24" xmlns="http://www.w3.org/2000/svg" role="img" width="38" height="24" aria-labelledby="pi-master"><title id="pi-master">Mastercard</title><path opacity=".07" d="M35 0H3C1.3 0 0 1.3 0 3v18c0 1.7 1.4 3 3 3h32c1.7 0 3-1.3 3-3V3c0-1.7-1.4-3-3-3z"/><path fill="#fff" d="M35 1c1.1 0 2 .9 2 2v18c0 1.1-.9 2-2 2H3c-1.1 0-2-.9-2-2V3c0-1.1.9-2 2-2h32"/><circle fill="#EB001B" cx="15" cy="12" r="7"/><circle fill="#F79E1B" cx="23" cy="12" r="7"/><path fill="#FF5F00" d="M22 12c0-2.4-1.2-4.5-3-5.7-1.8 1.3-3 3.4-3 5.7s1.2 4.5 3 5.7c1.8-1.2 3-3.3 3-5.7z"/></svg>
<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="pi-american_express" viewBox="0 0 38 24" width="38" height="24"><title id="pi-american_express">American Express</title><path fill="#000" d="M35 0H3C1.3 0 0 1.3 0 3v18c0 1.7 1.4 3 3 3h32c1.7 0 3-1.3 3-3V3c0-1.7-1.4-3-3-3Z" opacity=".07"/><path fill="#006FCF" d="M35 1c1.1 0 2 .9 2 2v18c0 1.1-.9 2-2 2H3c-1.1 0-2-.9-2-2V3c0-1.1.9-2 2-2h32Z"/><path fill="#FFF" d="M22.012 19.936v-8.421L37 11.528v2.326l-1.732 1.852L37 17.573v2.375h-2.766l-1.47-1.622-1.46 1.628-9.292-.02Z"/><path fill="#006FCF" d="M23.013 19.012v-6.57h5.572v1.513h-3.768v1.028h3.678v1.488h-3.678v1.01h3.768v1.531h-5.572Z"/><path fill="#006FCF" d="m28.557 19.012 3.083-3.289-3.083-3.282h2.386l1.884 2.083 1.89-2.082H37v.051l-3.017 3.23L37 18.92v.093h-2.307l-1.917-2.103-1.898 2.104h-2.321Z"/><path fill="#FFF" d="M22.71 4.04h3.614l1.269 2.881V4.04h4.46l.77 2.159.771-2.159H37v8.421H19l3.71-8.421Z"/><path fill="#006FCF" d="m23.395 4.955-2.916 6.566h2l.55-1.315h2.98l.55 1.315h2.05l-2.904-6.566h-2.31Zm.25 3.777.875-2.09.873 2.09h-1.748Z"/><path fill="#006FCF" d="M28.581 11.52V4.953l2.811.01L32.84 9l1.456-4.046H37v6.565l-1.74.016v-4.51l-1.644 4.494h-1.59L30.35 7.01v4.51h-1.768Z"/></svg>

<svg viewBox="0 0 38 24" xmlns="http://www.w3.org/2000/svg" width="38" height="24" role="img" aria-labelledby="pi-paypal"><title id="pi-paypal">PayPal</title><path opacity=".07" d="M35 0H3C1.3 0 0 1.3 0 3v18c0 1.7 1.4 3 3 3h32c1.7 0 3-1.3 3-3V3c0-1.7-1.4-3-3-3z"/><path fill="#fff" d="M35 1c1.1 0 2 .9 2 2v18c0 1.1-.9 2-2 2H3c-1.1 0-2-.9-2-2V3c0-1.1.9-2 2-2h32"/><path fill="#003087" d="M23.9 8.3c.2-1 0-1.7-.6-2.3-.6-.7-1.7-1-3.1-1h-4.1c-.3 0-.5.2-.6.5L14 15.6c0 .2.1.4.3.4H17l.4-3.4 1.8-2.2 4.7-2.1z"/><path fill="#3086C8" d="M23.9 8.3l-.2.2c-.5 2.8-2.2 3.8-4.6 3.8H18c-.3 0-.5.2-.6.5l-.6 3.9-.2 1c0 .2.1.4.3.4H19c.3 0 .5-.2.5-.4v-.1l.4-2.4v-.1c0-.2.3-.4.5-.4h.3c2.1 0 3.7-.8 4.1-3.2.2-1 .1-1.8-.4-2.4-.1-.5-.3-.7-.5-.8z"/><path fill="#012169" d="M23.3 8.1c-.1-.1-.2-.1-.3-.1-.1 0-.2 0-.3-.1-.3-.1-.7-.1-1.1-.1h-3c-.1 0-.2 0-.2.1-.2.1-.3.2-.3.4l-.7 4.4v.1c0-.3.3-.5.6-.5h1.3c2.5 0 4.1-1 4.6-3.8v-.2c-.1-.1-.3-.2-.5-.2h-.1z"/></svg>
<svg viewBox="0 0 38 24" xmlns="http://www.w3.org/2000/svg" role="img" width="38" height="24" aria-labelledby="pi-diners_club"><title id="pi-diners_club">Diners Club</title><path opacity=".07" d="M35 0H3C1.3 0 0 1.3 0 3v18c0 1.7 1.4 3 3 3h32c1.7 0 3-1.3 3-3V3c0-1.7-1.4-3-3-3z"/><path fill="#fff" d="M35 1c1.1 0 2 .9 2 2v18c0 1.1-.9 2-2 2H3c-1.1 0-2-.9-2-2V3c0-1.1.9-2 2-2h32"/><path d="M12 12v3.7c0 .3-.2.3-.5.2-1.9-.8-3-3.3-2.3-5.4.4-1.1 1.2-2 2.3-2.4.4-.2.5-.1.5.2V12zm2 0V8.3c0-.3 0-.3.3-.2 2.1.8 3.2 3.3 2.4 5.4-.4 1.1-1.2 2-2.3 2.4-.4.2-.4.1-.4-.2V12zm7.2-7H13c3.8 0 6.8 3.1 6.8 7s-3 7-6.8 7h8.2c3.8 0 6.8-3.1 6.8-7s-3-7-6.8-7z" fill="#3086C8"/></svg>
<svg viewBox="0 0 38 24" width="38" height="24" role="img" aria-labelledby="pi-discover" fill="none" xmlns="http://www.w3.org/2000/svg"><title id="pi-discover">Discover</title><path fill="#000" opacity=".07" d="M35 0H3C1.3 0 0 1.3 0 3v18c0 1.7 1.4 3 3 3h32c1.7 0 3-1.3 3-3V3c0-1.7-1.4-3-3-3z"/><path d="M35 1c1.1 0 2 .9 2 2v18c0 1.1-.9 2-2 2H3c-1.1 0-2-.9-2-2V3c0-1.1.9-2 2-2h32z" fill="#fff"/><path d="M3.57 7.16H2v5.5h1.57c.83 0 1.43-.2 1.96-.63.63-.52 1-1.3 1-2.11-.01-1.63-1.22-2.76-2.96-2.76zm1.26 4.14c-.34.3-.77.44-1.47.44h-.29V8.1h.29c.69 0 1.11.12 1.47.44.37.33.59.84.59 1.37 0 .53-.22 1.06-.59 1.39zm2.19-4.14h1.07v5.5H7.02v-5.5zm3.69 2.11c-.64-.24-.83-.4-.83-.69 0-.35.34-.61.8-.61.32 0 .59.13.86.45l.56-.73c-.46-.4-1.01-.61-1.62-.61-.97 0-1.72.68-1.72 1.58 0 .76.35 1.15 1.35 1.51.42.15.63.25.74.31.21.14.32.34.32.57 0 .45-.35.78-.83.78-.51 0-.92-.26-1.17-.73l-.69.67c.49.73 1.09 1.05 1.9 1.05 1.11 0 1.9-.74 1.9-1.81.02-.89-.35-1.29-1.57-1.74zm1.92.65c0 1.62 1.27 2.87 2.9 2.87.46 0 .86-.09 1.34-.32v-1.26c-.43.43-.81.6-1.29.6-1.08 0-1.85-.78-1.85-1.9 0-1.06.79-1.89 1.8-1.89.51 0 .9.18 1.34.62V7.38c-.47-.24-.86-.34-1.32-.34-1.61 0-2.92 1.28-2.92 2.88zm12.76.94l-1.47-3.7h-1.17l2.33 5.64h.58l2.37-5.64h-1.16l-1.48 3.7zm3.13 1.8h3.04v-.93h-1.97v-1.48h1.9v-.93h-1.9V8.1h1.97v-.94h-3.04v5.5zm7.29-3.87c0-1.03-.71-1.62-1.95-1.62h-1.59v5.5h1.07v-2.21h.14l1.48 2.21h1.32l-1.73-2.32c.81-.17 1.26-.72 1.26-1.56zm-2.16.91h-.31V8.03h.33c.67 0 1.03.28 1.03.82 0 .55-.36.85-1.05.85z" fill="#231F20"/><path d="M20.16 12.86a2.931 2.931 0 100-5.862 2.931 2.931 0 000 5.862z" fill="url(#pi-paint0_linear)"/><path opacity=".65" d="M20.16 12.86a2.931 2.931 0 100-5.862 2.931 2.931 0 000 5.862z" fill="url(#pi-paint1_linear)"/><path d="M36.57 7.506c0-.1-.07-.15-.18-.15h-.16v.48h.12v-.19l.14.19h.14l-.16-.2c.06-.01.1-.06.1-.13zm-.2.07h-.02v-.13h.02c.06 0 .09.02.09.06 0 .05-.03.07-.09.07z" fill="#231F20"/><path d="M36.41 7.176c-.23 0-.42.19-.42.42 0 .23.19.42.42.42.23 0 .42-.19.42-.42 0-.23-.19-.42-.42-.42zm0 .77c-.18 0-.34-.15-.34-.35 0-.19.15-.35.34-.35.18 0 .33.16.33.35 0 .19-.15.35-.33.35z" fill="#231F20"/><path d="M37 12.984S27.09 19.873 8.976 23h26.023a2 2 0 002-1.984l.024-3.02L37 12.985z" fill="#F48120"/><defs><linearGradient id="pi-paint0_linear" x1="21.657" y1="12.275" x2="19.632" y2="9.104" gradientUnits="userSpaceOnUse"><stop stop-color="#F89F20"/><stop offset=".25" stop-color="#F79A20"/><stop offset=".533" stop-color="#F68D20"/><stop offset=".62" stop-color="#F58720"/><stop offset=".723" stop-color="#F48120"/><stop offset="1" stop-color="#F37521"/></linearGradient><linearGradient id="pi-paint1_linear" x1="21.338" y1="12.232" x2="18.378" y2="6.446" gradientUnits="userSpaceOnUse"><stop stop-color="#F58720"/><stop offset=".359" stop-color="#E16F27"/><stop offset=".703" stop-color="#D4602C"/><stop offset=".982" stop-color="#D05B2E"/></linearGradient></defs></svg>
```

#### class

Specify the `class` attribute of the `<svg>` tag.

Sintassi:

```liquid
type | payment_type_svg_tag: class: string
```

**Input:**

```liquid
{% for type in shop.enabled_payment_types -%}
  {{ type | payment_type_svg_tag: class: 'custom-class' }}
{% endfor %}
```

**Output:**

```html
<svg class="custom-class" viewBox="0 0 38 24" xmlns="http://www.w3.org/2000/svg" role="img" width="38" height="24" aria-labelledby="pi-visa"><title id="pi-visa">Visa</title><path opacity=".07" d="M35 0H3C1.3 0 0 1.3 0 3v18c0 1.7 1.4 3 3 3h32c1.7 0 3-1.3 3-3V3c0-1.7-1.4-3-3-3z"/><path fill="#fff" d="M35 1c1.1 0 2 .9 2 2v18c0 1.1-.9 2-2 2H3c-1.1 0-2-.9-2-2V3c0-1.1.9-2 2-2h32"/><path d="M28.3 10.1H28c-.4 1-.7 1.5-1 3h1.9c-.3-1.5-.3-2.2-.6-3zm2.9 5.9h-1.7c-.1 0-.1 0-.2-.1l-.2-.9-.1-.2h-2.4c-.1 0-.2 0-.2.2l-.3.9c0 .1-.1.1-.1.1h-2.1l.2-.5L27 8.7c0-.5.3-.7.8-.7h1.5c.1 0 .2 0 .2.2l1.4 6.5c.1.4.2.7.2 1.1.1.1.1.1.1.2zm-13.4-.3l.4-1.8c.1 0 .2.1.2.1.7.3 1.4.5 2.1.4.2 0 .5-.1.7-.2.5-.2.5-.7.1-1.1-.2-.2-.5-.3-.8-.5-.4-.2-.8-.4-1.1-.7-1.2-1-.8-2.4-.1-3.1.6-.4.9-.8 1.7-.8 1.2 0 2.5 0 3.1.2h.1c-.1.6-.2 1.1-.4 1.7-.5-.2-1-.4-1.5-.4-.3 0-.6 0-.9.1-.2 0-.3.1-.4.2-.2.2-.2.5 0 .7l.5.4c.4.2.8.4 1.1.6.5.3 1 .8 1.1 1.4.2.9-.1 1.7-.9 2.3-.5.4-.7.6-1.4.6-1.4 0-2.5.1-3.4-.2-.1.2-.1.2-.2.1zm-3.5.3c.1-.7.1-.7.2-1 .5-2.2 1-4.5 1.4-6.7.1-.2.1-.3.3-.3H18c-.2 1.2-.4 2.1-.7 3.2-.3 1.5-.6 3-1 4.5 0 .2-.1.2-.3.2M5 8.2c0-.1.2-.2.3-.2h3.4c.5 0 .9.3 1 .8l.9 4.4c0 .1 0 .1.1.2 0-.1.1-.1.1-.1l2.1-5.1c-.1-.1 0-.2.1-.2h2.1c0 .1 0 .1-.1.2l-3.1 7.3c-.1.2-.1.3-.2.4-.1.1-.3 0-.5 0H9.7c-.1 0-.2 0-.2-.2L7.9 9.5c-.2-.2-.5-.5-.9-.6-.6-.3-1.7-.5-1.9-.5L5 8.2z" fill="#142688"/></svg>
<svg class="custom-class" viewBox="0 0 38 24" xmlns="http://www.w3.org/2000/svg" role="img" width="38" height="24" aria-labelledby="pi-master"><title id="pi-master">Mastercard</title><path opacity=".07" d="M35 0H3C1.3 0 0 1.3 0 3v18c0 1.7 1.4 3 3 3h32c1.7 0 3-1.3 3-3V3c0-1.7-1.4-3-3-3z"/><path fill="#fff" d="M35 1c1.1 0 2 .9 2 2v18c0 1.1-.9 2-2 2H3c-1.1 0-2-.9-2-2V3c0-1.1.9-2 2-2h32"/><circle fill="#EB001B" cx="15" cy="12" r="7"/><circle fill="#F79E1B" cx="23" cy="12" r="7"/><path fill="#FF5F00" d="M22 12c0-2.4-1.2-4.5-3-5.7-1.8 1.3-3 3.4-3 5.7s1.2 4.5 3 5.7c1.8-1.2 3-3.3 3-5.7z"/></svg>
<svg class="custom-class" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="pi-american_express" viewBox="0 0 38 24" width="38" height="24"><title id="pi-american_express">American Express</title><path fill="#000" d="M35 0H3C1.3 0 0 1.3 0 3v18c0 1.7 1.4 3 3 3h32c1.7 0 3-1.3 3-3V3c0-1.7-1.4-3-3-3Z" opacity=".07"/><path fill="#006FCF" d="M35 1c1.1 0 2 .9 2 2v18c0 1.1-.9 2-2 2H3c-1.1 0-2-.9-2-2V3c0-1.1.9-2 2-2h32Z"/><path fill="#FFF" d="M22.012 19.936v-8.421L37 11.528v2.326l-1.732 1.852L37 17.573v2.375h-2.766l-1.47-1.622-1.46 1.628-9.292-.02Z"/><path fill="#006FCF" d="M23.013 19.012v-6.57h5.572v1.513h-3.768v1.028h3.678v1.488h-3.678v1.01h3.768v1.531h-5.572Z"/><path fill="#006FCF" d="m28.557 19.012 3.083-3.289-3.083-3.282h2.386l1.884 2.083 1.89-2.082H37v.051l-3.017 3.23L37 18.92v.093h-2.307l-1.917-2.103-1.898 2.104h-2.321Z"/><path fill="#FFF" d="M22.71 4.04h3.614l1.269 2.881V4.04h4.46l.77 2.159.771-2.159H37v8.421H19l3.71-8.421Z"/><path fill="#006FCF" d="m23.395 4.955-2.916 6.566h2l.55-1.315h2.98l.55 1.315h2.05l-2.904-6.566h-2.31Zm.25 3.777.875-2.09.873 2.09h-1.748Z"/><path fill="#006FCF" d="M28.581 11.52V4.953l2.811.01L32.84 9l1.456-4.046H37v6.565l-1.74.016v-4.51l-1.644 4.494h-1.59L30.35 7.01v4.51h-1.768Z"/></svg>

<svg class="custom-class" viewBox="0 0 38 24" xmlns="http://www.w3.org/2000/svg" width="38" height="24" role="img" aria-labelledby="pi-paypal"><title id="pi-paypal">PayPal</title><path opacity=".07" d="M35 0H3C1.3 0 0 1.3 0 3v18c0 1.7 1.4 3 3 3h32c1.7 0 3-1.3 3-3V3c0-1.7-1.4-3-3-3z"/><path fill="#fff" d="M35 1c1.1 0 2 .9 2 2v18c0 1.1-.9 2-2 2H3c-1.1 0-2-.9-2-2V3c0-1.1.9-2 2-2h32"/><path fill="#003087" d="M23.9 8.3c.2-1 0-1.7-.6-2.3-.6-.7-1.7-1-3.1-1h-4.1c-.3 0-.5.2-.6.5L14 15.6c0 .2.1.4.3.4H17l.4-3.4 1.8-2.2 4.7-2.1z"/><path fill="#3086C8" d="M23.9 8.3l-.2.2c-.5 2.8-2.2 3.8-4.6 3.8H18c-.3 0-.5.2-.6.5l-.6 3.9-.2 1c0 .2.1.4.3.4H19c.3 0 .5-.2.5-.4v-.1l.4-2.4v-.1c0-.2.3-.4.5-.4h.3c2.1 0 3.7-.8 4.1-3.2.2-1 .1-1.8-.4-2.4-.1-.5-.3-.7-.5-.8z"/><path fill="#012169" d="M23.3 8.1c-.1-.1-.2-.1-.3-.1-.1 0-.2 0-.3-.1-.3-.1-.7-.1-1.1-.1h-3c-.1 0-.2 0-.2.1-.2.1-.3.2-.3.4l-.7 4.4v.1c0-.3.3-.5.6-.5h1.3c2.5 0 4.1-1 4.6-3.8v-.2c-.1-.1-.3-.2-.5-.2h-.1z"/></svg>
<svg class="custom-class" viewBox="0 0 38 24" xmlns="http://www.w3.org/2000/svg" role="img" width="38" height="24" aria-labelledby="pi-diners_club"><title id="pi-diners_club">Diners Club</title><path opacity=".07" d="M35 0H3C1.3 0 0 1.3 0 3v18c0 1.7 1.4 3 3 3h32c1.7 0 3-1.3 3-3V3c0-1.7-1.4-3-3-3z"/><path fill="#fff" d="M35 1c1.1 0 2 .9 2 2v18c0 1.1-.9 2-2 2H3c-1.1 0-2-.9-2-2V3c0-1.1.9-2 2-2h32"/><path d="M12 12v3.7c0 .3-.2.3-.5.2-1.9-.8-3-3.3-2.3-5.4.4-1.1 1.2-2 2.3-2.4.4-.2.5-.1.5.2V12zm2 0V8.3c0-.3 0-.3.3-.2 2.1.8 3.2 3.3 2.4 5.4-.4 1.1-1.2 2-2.3 2.4-.4.2-.4.1-.4-.2V12zm7.2-7H13c3.8 0 6.8 3.1 6.8 7s-3 7-6.8 7h8.2c3.8 0 6.8-3.1 6.8-7s-3-7-6.8-7z" fill="#3086C8"/></svg>
<svg class="custom-class" viewBox="0 0 38 24" width="38" height="24" role="img" aria-labelledby="pi-discover" fill="none" xmlns="http://www.w3.org/2000/svg"><title id="pi-discover">Discover</title><path fill="#000" opacity=".07" d="M35 0H3C1.3 0 0 1.3 0 3v18c0 1.7 1.4 3 3 3h32c1.7 0 3-1.3 3-3V3c0-1.7-1.4-3-3-3z"/><path d="M35 1c1.1 0 2 .9 2 2v18c0 1.1-.9 2-2 2H3c-1.1 0-2-.9-2-2V3c0-1.1.9-2 2-2h32z" fill="#fff"/><path d="M3.57 7.16H2v5.5h1.57c.83 0 1.43-.2 1.96-.63.63-.52 1-1.3 1-2.11-.01-1.63-1.22-2.76-2.96-2.76zm1.26 4.14c-.34.3-.77.44-1.47.44h-.29V8.1h.29c.69 0 1.11.12 1.47.44.37.33.59.84.59 1.37 0 .53-.22 1.06-.59 1.39zm2.19-4.14h1.07v5.5H7.02v-5.5zm3.69 2.11c-.64-.24-.83-.4-.83-.69 0-.35.34-.61.8-.61.32 0 .59.13.86.45l.56-.73c-.46-.4-1.01-.61-1.62-.61-.97 0-1.72.68-1.72 1.58 0 .76.35 1.15 1.35 1.51.42.15.63.25.74.31.21.14.32.34.32.57 0 .45-.35.78-.83.78-.51 0-.92-.26-1.17-.73l-.69.67c.49.73 1.09 1.05 1.9 1.05 1.11 0 1.9-.74 1.9-1.81.02-.89-.35-1.29-1.57-1.74zm1.92.65c0 1.62 1.27 2.87 2.9 2.87.46 0 .86-.09 1.34-.32v-1.26c-.43.43-.81.6-1.29.6-1.08 0-1.85-.78-1.85-1.9 0-1.06.79-1.89 1.8-1.89.51 0 .9.18 1.34.62V7.38c-.47-.24-.86-.34-1.32-.34-1.61 0-2.92 1.28-2.92 2.88zm12.76.94l-1.47-3.7h-1.17l2.33 5.64h.58l2.37-5.64h-1.16l-1.48 3.7zm3.13 1.8h3.04v-.93h-1.97v-1.48h1.9v-.93h-1.9V8.1h1.97v-.94h-3.04v5.5zm7.29-3.87c0-1.03-.71-1.62-1.95-1.62h-1.59v5.5h1.07v-2.21h.14l1.48 2.21h1.32l-1.73-2.32c.81-.17 1.26-.72 1.26-1.56zm-2.16.91h-.31V8.03h.33c.67 0 1.03.28 1.03.82 0 .55-.36.85-1.05.85z" fill="#231F20"/><path d="M20.16 12.86a2.931 2.931 0 100-5.862 2.931 2.931 0 000 5.862z" fill="url(#pi-paint0_linear)"/><path opacity=".65" d="M20.16 12.86a2.931 2.931 0 100-5.862 2.931 2.931 0 000 5.862z" fill="url(#pi-paint1_linear)"/><path d="M36.57 7.506c0-.1-.07-.15-.18-.15h-.16v.48h.12v-.19l.14.19h.14l-.16-.2c.06-.01.1-.06.1-.13zm-.2.07h-.02v-.13h.02c.06 0 .09.02.09.06 0 .05-.03.07-.09.07z" fill="#231F20"/><path d="M36.41 7.176c-.23 0-.42.19-.42.42 0 .23.19.42.42.42.23 0 .42-.19.42-.42 0-.23-.19-.42-.42-.42zm0 .77c-.18 0-.34-.15-.34-.35 0-.19.15-.35.34-.35.18 0 .33.16.33.35 0 .19-.15.35-.33.35z" fill="#231F20"/><path d="M37 12.984S27.09 19.873 8.976 23h26.023a2 2 0 002-1.984l.024-3.02L37 12.985z" fill="#F48120"/><defs><linearGradient id="pi-paint0_linear" x1="21.657" y1="12.275" x2="19.632" y2="9.104" gradientUnits="userSpaceOnUse"><stop stop-color="#F89F20"/><stop offset=".25" stop-color="#F79A20"/><stop offset=".533" stop-color="#F68D20"/><stop offset=".62" stop-color="#F58720"/><stop offset=".723" stop-color="#F48120"/><stop offset="1" stop-color="#F37521"/></linearGradient><linearGradient id="pi-paint1_linear" x1="21.338" y1="12.232" x2="18.378" y2="6.446" gradientUnits="userSpaceOnUse"><stop stop-color="#F58720"/><stop offset=".359" stop-color="#E16F27"/><stop offset=".703" stop-color="#D4602C"/><stop offset=".982" stop-color="#D05B2E"/></linearGradient></defs></svg>
```


# Categoria: string

## string — blake3

> Fonte: https://shopify.dev/docs/api/liquid/filters/blake3

Converts a string into a Blake3 hash.

### Sintassi

```liquid
string | blake3
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{{ '' | blake3 }}
```

**Output:**

```html
af1349b9f5f9a1a6a0404dea36dcc9499bcb25c9adc112b7cc9a93cae41f3262
```


## string — hmac_sha1

> Fonte: https://shopify.dev/docs/api/liquid/filters/hmac_sha1

Converts a string into an SHA-1 hash using a hash message authentication code (HMAC).

The secret key for the message is supplied as a parameter to the filter.

### Sintassi

```liquid
string | hmac_sha1: string
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{%- assign secret_potion = 'Polyjuice' | hmac_sha1: 'Polina' -%}

My secret potion: {{ secret_potion }}
```

**Output:**

```html
My secret potion: 63304203b005ea4bc80546f1c6fdfe252d2062b2
```


## string — hmac_sha256

> Fonte: https://shopify.dev/docs/api/liquid/filters/hmac_sha256

Converts a string into an SHA-256 hash using a hash message authentication code (HMAC).

The secret key for the message is supplied as a parameter to the filter.

### Sintassi

```liquid
string | hmac_sha256: string
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{%- assign secret_potion = 'Polyjuice' | hmac_sha256: 'Polina' -%}

My secret potion: {{ secret_potion }}
```

**Output:**

```html
My secret potion: 8e0d5d65cff1242a4af66c8f4a32854fd5fb80edcc8aabe9b302b29c7c71dc20
```


## string — md5

> Fonte: https://shopify.dev/docs/api/liquid/filters/md5

Converts a string into an MD5 hash. MD5 is not considered safe anymore. Please use ['blake3'](https://shopify.dev/docs/api/liquid/filters/blake3) instead for better security and performance.

### Sintassi

```liquid
string | md5
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{{ '' | md5 }}
```

**Output:**

```html
d41d8cd98f00b204e9800998ecf8427e
```


## string — sha1

> Fonte: https://shopify.dev/docs/api/liquid/filters/sha1

Converts a string into an SHA-1 hash. SHA-1 is not considered safe anymore. Please use ['blake3'](https://shopify.dev/docs/api/liquid/filters/blake3) instead for better security and performance.

### Sintassi

```liquid
string | sha1: string
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{%- assign secret_potion = 'Polyjuice' | sha1 -%}

My secret potion: {{ secret_potion }}
```

**Output:**

```html
My secret potion: bd0ca3935467e5238d7662ada4df899f09b70d5a
```


## string — sha256

> Fonte: https://shopify.dev/docs/api/liquid/filters/sha256

Converts a string into an SHA-256 hash. Please use ['blake3'](https://shopify.dev/docs/api/liquid/filters/blake3) instead for better security and performance.

### Sintassi

```liquid
string | sha256: string
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{%- assign secret_potion = 'Polyjuice' | sha256 -%}

My secret potion: {{ secret_potion }}
```

**Output:**

```html
My secret potion: 44ac1d7a2936e30a5de07082fd65d6fe9b1fb658a1a98bfe65bc5959beac5dd0
```


## string — append

> Fonte: https://shopify.dev/docs/api/liquid/filters/append

Adds a given string to the end of a string.

### Sintassi

```liquid
string | append: string
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{%-  assign path = product.url -%}

{{ request.origin | append: path }}
```

**Output:**

```html
https://polinas-potent-potions.myshopify.com/products/health-potion
```


## string — base64_decode

> Fonte: https://shopify.dev/docs/api/liquid/filters/base64_decode

Decodes a string in [Base64 format](https://developer.mozilla.org/en-US/docs/Glossary/Base64).

### Sintassi

```liquid
string | base64_decode
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{{ 'b25lIHR3byB0aHJlZQ==' | base64_decode }}
```

**Output:**

```html
one two three
```


## string — base64_encode

> Fonte: https://shopify.dev/docs/api/liquid/filters/base64_encode

Encodes a string to [Base64 format](https://developer.mozilla.org/en-US/docs/Glossary/Base64).

### Sintassi

```liquid
string | base64_encode
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{{ 'one two three' | base64_encode }}
```

**Output:**

```html
b25lIHR3byB0aHJlZQ==
```


## string — base64_url_safe_decode

> Fonte: https://shopify.dev/docs/api/liquid/filters/base64_url_safe_decode

Decodes a string in URL-safe [Base64 format](https://developer.mozilla.org/en-US/docs/Glossary/Base64).

### Sintassi

```liquid
string | base64_url_safe_decode
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{{ 'b25lIHR3byB0aHJlZQ==' | base64_url_safe_decode }}
```

**Output:**

```html
one two three
```


## string — base64_url_safe_encode

> Fonte: https://shopify.dev/docs/api/liquid/filters/base64_url_safe_encode

Encodes a string to URL-safe [Base64 format](https://developer.mozilla.org/en-US/docs/Glossary/Base64).

### Sintassi

```liquid
string | base64_url_safe_encode
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

To produce URL-safe Base64, this filter uses `-` and `_` in place of `+` and `/`.

**Input:**

```liquid
{{ 'one two three' | base64_url_safe_encode }}
```

**Output:**

```html
b25lIHR3byB0aHJlZQ==
```


## string — capitalize

> Fonte: https://shopify.dev/docs/api/liquid/filters/capitalize

Capitalizes the first word in a string and downcases the remaining characters.

### Sintassi

```liquid
string | capitalize
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{{ 'this sentence should start with a capitalized word.' | capitalize }}
```

**Output:**

```html
This sentence should start with a capitalized word.
```


## string — downcase

> Fonte: https://shopify.dev/docs/api/liquid/filters/downcase

Converts a string to all lowercase characters.

### Sintassi

```liquid
string | downcase
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{{ product.title | downcase }}
```

**Output:**

```html
health potion
```


## string — escape

> Fonte: https://shopify.dev/docs/api/liquid/filters/escape

Escapes special characters in HTML, such as `<>`, `'`, and `&`, and converts characters into escape sequences. The filter doesn't effect characters within the string that don’t have a corresponding escape sequence.".

### Sintassi

```liquid
string | escape
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{{ '<p>Text to be escaped.</p>' | escape }}
```

**Output:**

```html
&lt;p&gt;Text to be escaped.&lt;/p&gt;
```


## string — escape_once

> Fonte: https://shopify.dev/docs/api/liquid/filters/escape_once

Escapes a string without changing characters that have already been escaped.

### Sintassi

```liquid
string | escape_once
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
# applying the escape filter to already escaped text escapes characters in HTML entities:

{{ "&lt;p&gt;Text to be escaped.&lt;/p&gt;" | escape }}

# applying the escape_once filter to already escaped text skips characters in HTML entities:

{{ "&lt;p&gt;Text to be escaped.&lt;/p&gt;" | escape_once }}

# use escape_once to escape strings where a combination of HTML entities and non-escaped characters might be present:

{{ "&lt;p&gt;Text to be escaped.&lt;/p&gt; & some additional text" | escape_once }}
```

**Output:**

```html
# applying the escape filter to already escaped text escapes characters in HTML entities:

&amp;lt;p&amp;gt;Text to be escaped.&amp;lt;/p&amp;gt;

# applying the escape_once filter to already escaped text skips characters in HTML entities:

&lt;p&gt;Text to be escaped.&lt;/p&gt;

# use escape_once to escape strings where a combination of HTML entities and non-escaped characters might be present:

&lt;p&gt;Text to be escaped.&lt;/p&gt; &amp; some additional text
```


## string — lstrip

> Fonte: https://shopify.dev/docs/api/liquid/filters/lstrip

Strips all whitespace from the left of a string.

### Sintassi

```liquid
string | lstrip
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{%- assign text = '  Some potions create whitespace.      ' -%}

"{{ text }}"
"{{ text | lstrip }}"
```

**Output:**

```html
"  Some potions create whitespace.      "
"Some potions create whitespace.      "
```


## string — newline_to_br

> Fonte: https://shopify.dev/docs/api/liquid/filters/newline_to_br

Converts newlines (`\n`) in a string to HTML line breaks (`<br>`).

### Sintassi

```liquid
string | newline_to_br
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{{ product.description | newline_to_br }}
```

**Output:**

```html
<h3>Are you low on health? Well we've got the potion just for you!</h3><br />
<p>Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!</p>
```


## string — prepend

> Fonte: https://shopify.dev/docs/api/liquid/filters/prepend

Adds a given string to the beginning of a string.

### Sintassi

```liquid
string | prepend: string
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{%- assign origin = request.origin -%}

{{ product.url | prepend: origin }}
```

**Output:**

```html
https://polinas-potent-potions.myshopify.com/products/health-potion
```


## string — remove

> Fonte: https://shopify.dev/docs/api/liquid/filters/remove

Removes any instance of a substring inside a string.

### Sintassi

```liquid
string | remove: string
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{{ "I can't do it!" | remove: "'t" }}
```

**Output:**

```html
I can do it!
```


## string — remove_first

> Fonte: https://shopify.dev/docs/api/liquid/filters/remove_first

Removes the first instance of a substring inside a string.

### Sintassi

```liquid
string | remove_first: string
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{{ "I hate it when I accidentally spill my duplication potion accidentally!" | remove_first: ' accidentally' }}
```

**Output:**

```html
I hate it when I spill my duplication potion accidentally!
```


## string — remove_last

> Fonte: https://shopify.dev/docs/api/liquid/filters/remove_last

Removes the last instance of a substring inside a string.

### Sintassi

```liquid
string | remove_last: string
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{{ "I hate it when I accidentally spill my duplication potion accidentally!" | remove_last: ' accidentally' }}
```

**Output:**

```html
I hate it when I accidentally spill my duplication potion!
```


## string — replace

> Fonte: https://shopify.dev/docs/api/liquid/filters/replace

Replaces any instance of a substring inside a string with a given string.

### Sintassi

```liquid
string | replace: string, string
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{{ product.handle | replace: '-', ' ' }}
```

**Output:**

```html
komodo dragon scale
```


## string — replace_first

> Fonte: https://shopify.dev/docs/api/liquid/filters/replace_first

Replaces the first instance of a substring inside a string with a given string.

### Sintassi

```liquid
string | replace_first: string, string
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{{ product.handle | replace_first: '-', ' ' }}
```

**Output:**

```html
komodo dragon-scale
```


## string — replace_last

> Fonte: https://shopify.dev/docs/api/liquid/filters/replace_last

Replaces the last instance of a substring inside a string with a given string.

### Sintassi

```liquid
string | replace_last: string, string
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{{ product.handle | replace_last: '-', ' ' }}
```

**Output:**

```html
komodo-dragon scale
```


## string — rstrip

> Fonte: https://shopify.dev/docs/api/liquid/filters/rstrip

Strips all whitespace from the right of a string.

### Sintassi

```liquid
string | rstrip
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{%- assign text = '  Some potions create whitespace.      ' -%}

"{{ text }}"
"{{ text | rstrip }}"
```

**Output:**

```html
"  Some potions create whitespace.      "
"  Some potions create whitespace."
```


## string — slice

> Fonte: https://shopify.dev/docs/api/liquid/filters/slice

Returns a substring or series of array items, starting at a given 0-based index.

By default, the substring has a length of one character, and the array series has one array item. However, you can
provide a second parameter to specify the number of characters or array items.

### Sintassi

```liquid
string | slice
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

#### Esempio 1

**Input:**

```liquid
{{ collection.title | slice: 0 }}
{{ collection.title | slice: 0, 5 }}

{{ collection.all_tags | slice: 1, 2 | join: ', ' }}
```

**Output:**

```html
P
Produ

dried, extra-potent
```

#### Negative index

You can supply a negative index which will count from the end of the string.

**Input:**

```liquid
{{ collection.title | slice: -3, 3 }}
```

**Output:**

```html
cts
```


## string — split

> Fonte: https://shopify.dev/docs/api/liquid/filters/split

Splits a string into an array of substrings based on a given separator.

### Sintassi

```liquid
string | split: string
```

### Restituisce

[array of string](https://shopify.dev/docs/api/liquid/basics#array)

### Esempi

**Input:**

```liquid
{%- assign title_words = product.handle | split: '-' -%}

{% for word in title_words -%}
  {{ word }}
{%- endfor %}
```

**Output:**

```html
health
potion
```


## string — strip

> Fonte: https://shopify.dev/docs/api/liquid/filters/strip

Strips all whitespace from the left and right of a string.

### Sintassi

```liquid
string | strip
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{%- assign text = '  Some potions create whitespace.      ' -%}

"{{ text }}"
"{{ text | strip }}"
```

**Output:**

```html
"  Some potions create whitespace.      "
"Some potions create whitespace."
```


## string — strip_html

> Fonte: https://shopify.dev/docs/api/liquid/filters/strip_html

Strips all HTML tags from a string.

### Sintassi

```liquid
string | strip_html
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
<!-- With HTML -->
{{ product.description }}

<!-- HTML stripped -->
{{ product.description | strip_html }}
```

**Output:**

```html
<!-- With HTML -->
<h3>Are you low on health? Well we've got the potion just for you!</h3>
<p>Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!</p>

<!-- HTML stripped -->
Are you low on health? Well we've got the potion just for you!
Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!
```


## string — strip_newlines

> Fonte: https://shopify.dev/docs/api/liquid/filters/strip_newlines

Strips all newline characters (line breaks) from a string.

### Sintassi

```liquid
string | strip_newlines
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
<!-- With newlines -->
{{ product.description }}

<!-- Newlines stripped -->
{{ product.description | strip_newlines }}
```

**Output:**

```html
<!-- With newlines -->
<h3>Are you low on health? Well we've got the potion just for you!</h3>
<p>Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!</p>

<!-- Newlines stripped -->
<h3>Are you low on health? Well we've got the potion just for you!</h3><p>Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!</p>
```


## string — truncate

> Fonte: https://shopify.dev/docs/api/liquid/filters/truncate

Truncates a string down to a given number of characters.

If the specified number of characters is less than the length of the string, then an ellipsis (`...`) is appended to
the truncated string. The ellipsis is included in the character count of the truncated string.

### Sintassi

```liquid
string | truncate: number
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

#### Esempio 1

**Input:**

```liquid
{{ article.title | truncate: 15 }}
```

**Output:**

```html
How to tell ...
```

#### Specify a custom ellipsis

You can provide a second parameter to specify a custom ellipsis. If you don't want an ellipsis, then you can supply an empty string.

Sintassi:

```liquid
string | truncate: number, string
```

**Input:**

```liquid
{{ article.title | truncate: 15, '--' }}
{{ article.title | truncate: 15, '' }}
```

**Output:**

```html
How to tell i--
How to tell if
```


## string — truncatewords

> Fonte: https://shopify.dev/docs/api/liquid/filters/truncatewords

Truncates a string down to a given number of words.

If the specified number of words is less than the number of words in the string, then an ellipsis (`...`) is appended to
the truncated string.

> Caution:
> HTML tags are treated as words, so you should strip any HTML from truncated content. If you don't strip HTML, then
> closing HTML tags can be removed, which can result in unexpected behavior.

### Sintassi

```liquid
string | truncatewords: number
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

#### Esempio 1

**Input:**

```liquid
{{ article.content | strip_html | truncatewords: 15 }}
```

**Output:**

```html
We've all had this problem before: we peek into the potions vault to determine which...
```

#### Specify a custom ellipsis

You can provide a second parameter to specify a custom ellipsis. If you don't want an ellipsis, then you can supply an empty string.

Sintassi:

```liquid
string | truncatewords: number, string
```

**Input:**

```liquid
{{ article.content | strip_html | truncatewords: 15, '--' }}

{{ article.content | strip_html | truncatewords: 15, '' }}
```

**Output:**

```html
We've all had this problem before: we peek into the potions vault to determine which--

We've all had this problem before: we peek into the potions vault to determine which
```


## string — upcase

> Fonte: https://shopify.dev/docs/api/liquid/filters/upcase

Converts a string to all uppercase characters.

### Sintassi

```liquid
string | upcase
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{{ product.title | upcase }}
```

**Output:**

```html
HEALTH POTION
```


## string — url_decode

> Fonte: https://shopify.dev/docs/api/liquid/filters/url_decode

Decodes any [percent-encoded](https://developer.mozilla.org/en-US/docs/Glossary/percent-encoding) characters
in a string.

### Sintassi

```liquid
string | url_decode
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{{ 'test%40test.com' | url_decode }}
```

**Output:**

```html
test@test.com
```


## string — url_encode

> Fonte: https://shopify.dev/docs/api/liquid/filters/url_encode

Converts any URL-unsafe characters in a string to the
[percent-encoded](https://developer.mozilla.org/en-US/docs/Glossary/percent-encoding) equivalent.

> Note:
> Spaces are converted to a `+` character, instead of a percent-encoded character.

### Sintassi

```liquid
string | url_encode
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{{ 'test@test.com' | url_encode }}
```

**Output:**

```html
test%40test.com
```


## string — camelize

> Fonte: https://shopify.dev/docs/api/liquid/filters/camelize

Converts a string to CamelCase.

### Sintassi

```liquid
string | camelize
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{{ 'variable-name' | camelize }}
```

**Output:**

```html
VariableName
```


## string — handleize

> Fonte: https://shopify.dev/docs/api/liquid/filters/handleize

Converts a string into a [handle](https://shopify.dev/docs/api/liquid/basics#handles).

> Note:
> The `handleize` filter has an alias of `handle`.

### Sintassi

```liquid
string | handleize
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{{ product.title | handleize }}
{{ product.title | handle }}
```

**Output:**

```html
health-potion
health-potion
```


## string — url_escape

> Fonte: https://shopify.dev/docs/api/liquid/filters/url_escape

Escapes any URL-unsafe characters in a string.

### Sintassi

```liquid
string | url_escape
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{{ '<p>Health & Love potions</p>' | url_escape }}
```

**Output:**

```html
%3Cp%3EHealth%20&%20Love%20potions%3C/p%3E
```


## string — url_param_escape

> Fonte: https://shopify.dev/docs/api/liquid/filters/url_param_escape

Escapes any characters in a string that are unsafe for URL parameters.

The `url_param_escape` filter escapes the same characters as [`url_escape`](https://shopify.dev/docs/api/liquid/filters/url_escape), with the
addition of `&`.

### Sintassi

```liquid
string | url_param_escape
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{{ '<p>Health & Love potions</p>' | url_param_escape }}
```

**Output:**

```html
%3Cp%3EHealth%20%26%20Love%20potions%3C/p%3E
```


## string — pluralize

> Fonte: https://shopify.dev/docs/api/liquid/filters/pluralize

Outputs the singular or plural version of a string based on a given number.

> Caution:
> The `pluralize` filter applies English pluralization rules to determine which string to output. You shouldn't use this
> filter on non-English strings because it could lead to incorrect pluralizations.

### Sintassi

```liquid
number | pluralize: string, string
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
Cart item count: {{ cart.item_count }} {{ cart.item_count | pluralize: 'item', 'items' }}
```

**Output:**

```html
Cart item count: 2 items
```


# Categoria: tag

## tag — link_to_add_tag

> Fonte: https://shopify.dev/docs/api/liquid/filters/link_to_add_tag

Generates an HTML `<a>` tag with an `href` attribute linking to the current blog or collection, filtered to show
only articles or products that have a given tag, as well as any currently active tags.

> Tip:
> To learn more about filtering by tag, refer to [Filter articles by tag](https://shopify.dev/themes/architecture/templates/blog#filter-articles-by-tag)
> or [Filter collections by tag](https://shopify.dev/themes/navigation-search/filtering/tag-filtering).

### Sintassi

```liquid
string | link_to_add_tag
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{% for tag in collection.all_tags %}
  {%- if current_tags contains tag -%}
    {{ tag }}
  {%- else -%}
    {{ tag | link_to_add_tag: tag }}
  {%- endif -%}
{% endfor %}
```

**Output:**

```html
<a href="/services/liquid_rendering/extra-potent" title="Narrow selection to products matching tag extra-potent">extra-potent</a>

<a href="/services/liquid_rendering/fresh" title="Narrow selection to products matching tag fresh">fresh</a>

<a href="/services/liquid_rendering/healing" title="Narrow selection to products matching tag healing">healing</a>

<a href="/services/liquid_rendering/ingredients" title="Narrow selection to products matching tag ingredients">ingredients</a>
```


## tag — link_to_remove_tag

> Fonte: https://shopify.dev/docs/api/liquid/filters/link_to_remove_tag

Generates an HTML `<a>` tag with an `href` attribute linking to the current blog or collection, filtered to show
only articles or products that have any currently active tags, except the provided tag.

> Tip:
> To learn more about filtering by tag, refer to [Filter articles by tag](https://shopify.dev/themes/architecture/templates/blog#filter-articles-by-tag)
> or [Filter collections by tag](https://shopify.dev/themes/navigation-search/filtering/tag-filtering).

### Sintassi

```liquid
string | link_to_remove_tag
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{% for tag in collection.all_tags %}
  {%- if current_tags contains tag -%}
    {{ tag | link_to_remove_tag: tag }}
  {%- else -%}
    {{ tag | link_to_add_tag: tag }}
  {%- endif -%}
{% endfor %}
```

**Output:**

```html
<a href="/services/liquid_rendering/extra-potent" title="Narrow selection to products matching tag extra-potent">extra-potent</a>

<a href="/services/liquid_rendering/fresh" title="Narrow selection to products matching tag fresh">fresh</a>

<a href="/services/liquid_rendering/healing" title="Narrow selection to products matching tag healing">healing</a>

<a href="/services/liquid_rendering/ingredients" title="Narrow selection to products matching tag ingredients">ingredients</a>
```


## tag — link_to_tag

> Fonte: https://shopify.dev/docs/api/liquid/filters/link_to_tag

Generates an HTML `<a>` tag with an `href` attribute linking to the current blog or collection, filtered to show
only articles or products that have a given tag.

> Tip:
> To learn more about filtering by tag, refer to [Filter articles by tag](https://shopify.dev/themes/architecture/templates/blog#filter-articles-by-tag)
> or [Filter collections by tag](https://shopify.dev/themes/navigation-search/filtering/tag-filtering).

### Sintassi

```liquid
string | link_to_tag
```

### Restituisce

[string](https://shopify.dev/docs/api/liquid/basics#string)

### Esempi

**Input:**

```liquid
{% for tag in collection.all_tags %}
  {{- tag | link_to_tag: tag }}
{% endfor %}
```

**Output:**

```html
<a href="/services/liquid_rendering/extra-potent" title="Show products matching tag extra-potent">extra-potent</a>

<a href="/services/liquid_rendering/fresh" title="Show products matching tag fresh">fresh</a>

<a href="/services/liquid_rendering/healing" title="Show products matching tag healing">healing</a>

<a href="/services/liquid_rendering/ingredients" title="Show products matching tag ingredients">ingredients</a>
```


## Pagine non catturate

Nessuna. Tutti i 77 filtri delle categorie M–Z sono stati catturati con sintassi, parametri ed esempi.

> Note di fedeltà:
> - `payment_terms` e gli esempi puramente descrittivi (es. `image_tag` › *Lazy loading*/*preload*, `metafield_tag`/`metafield_text` › *Complex types*) non mostrano un output renderizzato nella documentazione ufficiale; sono segnalati come tali.
> - Gli esempi di `link_to_remove_tag` e `link_to_add_tag` nella documentazione ufficiale producono entrambi link "Narrow selection…" perché nello store demo nessun tag è in `current_tags` (viene eseguito il ramo `else` con `link_to_add_tag`): output riportato verbatim.
