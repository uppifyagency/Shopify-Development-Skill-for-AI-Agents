# Liquid Filters — index (155 unici)

How to use: find your filter, then open the listed file and Grep the heading `## <category> — <filter>` for full syntax, params, and examples.
Part 1 (A–L) = `reference/09-liquid-filters-part1.md` · Part 2 (M–Z) = `reference/10-liquid-filters-part2.md`

## array  (part 1)
| Filter | Signature | Purpose |
|--------|-----------|---------|
| `compact` | `array \| compact` | Removes any `nil` items from an array |
| `concat` | `array \| concat: array` | Concatenates (combines) two arrays |
| `find` | `array \| find: string, string` | Returns the first item in an array with a specific property value |
| `find_index` | `array \| find_index: string, string` | Returns the index of the first item with a specific property value |
| `first` | `array \| first` | Returns the first item in an array |
| `has` | `array \| has: string, string` | Tests if any item in an array has a specific property value |
| `join` | `array \| join` / `array \| join: string` | Combines all items into a single string, separated by a space (or a given separator) |
| `last` | `array \| last` | Returns the last item in an array |
| `map` | `array \| map: string` | Creates an array of values from a specific property of the items |
| `reject` | `array \| reject: string, string` | Filters an array to exclude items with a specific property value |
| `reverse` | `array \| reverse` | Reverses the order of the items in an array |
| `size` | `variable \| size` | Returns the size of a string (chars) or array (items) |
| `slice` | `string \| slice: index` / `string \| slice: index, length` | Returns a substring or array items, starting at a 0-based index |
| `sort` | `array \| sort` | Sorts items in case-sensitive alphabetical or numerical order |
| `sort_natural` | `array \| sort_natural` | Sorts items in case-insensitive alphabetical order |
| `sum` | `array \| sum` / `array \| sum: string` | Returns the sum of all elements (optionally summing a property) |
| `uniq` | `array \| uniq` | Removes any duplicate items in an array |
| `where` | `array \| where: property_name, property_value` | Filters an array to include only items with a specific property value |

## cart  (part 1)
| Filter | Signature | Purpose |
|--------|-----------|---------|
| `item_count_for_variant` | `cart \| item_count_for_variant: {variant_id}` | Returns the total item count for a specified variant in the `cart` object |
| `line_items_for` | `cart \| line_items_for: object` | Returns the subset of cart line items that include a given product or variant |

## collection  (part 1)
| Filter | Signature | Purpose |
|--------|-----------|---------|
| `highlight_active_tag` | `string \| highlight_active_tag` | Wraps an active collection tag in a `<span class="active">` |
| `link_to_type` | `string \| link_to_type` | HTML `<a>` linking to a collection page listing all products of a product type |
| `link_to_vendor` | `string \| link_to_vendor` | HTML `<a>` linking to a collection page listing all products of a vendor |
| `sort_by` | `string \| sort_by: string` | Appends a `sort_by` parameter to a `collection.url` |
| `url_for_type` | `string \| url_for_type` | Generates a URL for a collection page listing all products of a product type |
| `url_for_vendor` | `string \| url_for_vendor` | Generates a URL for a collection page listing all products of a vendor |
| `within` | `string \| within: collection` | Generates a product URL within the context of a collection |

## color  (part 1)
| Filter | Signature | Purpose |
|--------|-----------|---------|
| `brightness_difference` | `string \| brightness_difference: string` | Perceived brightness difference between two colors (W3C standard) |
| `color_brightness` | `string \| color_brightness` | Perceived brightness of a color (W3C accessibility formula) |
| `color_contrast` | `string \| color_contrast: string` | Contrast ratio numerator between two colors |
| `color_darken` | `string \| color_darken: number` | Darkens a color by a percentage (0–100) |
| `color_desaturate` | `string \| color_desaturate: number` | Desaturates a color by a percentage (0–100) |
| `color_difference` | `string \| color_difference: string` | Color difference between two colors |
| `color_extract` | `string \| color_extract: string` | Extracts a specific color component from a color |
| `color_lighten` | `string \| color_lighten: number` | Lightens a color by a percentage (0–100) |
| `color_mix` | `string \| color_mix: string, number` | Blends two colors by a percentage factor (0–100) |
| `color_modify` | `string \| color_modify: string, number` | Modifies a specific color component by a given amount |
| `color_saturate` | `string \| color_saturate: number` | Saturates a color by a percentage (0–100) |
| `color_to_hex` | `string \| color_to_hex` | Converts a CSS color string to hexadecimal (`hex6`) |
| `color_to_hsl` | `string \| color_to_hsl` | Converts a CSS color string to HSL (HSLA if alpha) |
| `color_to_oklch` | `string \| color_to_oklch` | Converts a CSS color string to OKLCH format |
| `color_to_rgb` | `string \| color_to_rgb` | Converts a CSS color string to RGB (RGBA if alpha) |
| `hex_to_rgba` | `string \| hex_to_rgba` | Converts a hex color string to RGBA (hex3 shorthand accepted) |

## customer  (part 1)
| Filter | Signature | Purpose |
|--------|-----------|---------|
| `avatar` | `customer \| avatar` | Generates HTML to render a customer's avatar, if available |
| `customer_login_link` | `string \| customer_login_link` | Generates an HTML link to the customer login page |
| `customer_logout_link` | `string \| customer_logout_link` | HTML link that logs the customer out and redirects to the homepage |
| `customer_register_link` | `string \| customer_register_link` | Generates an HTML link to the customer registration page |
| `login_button` | `shop \| login_button` | HTML button to sign in with a Shop account or follow the shop in Shop app |

## default  (part 1)
| Filter | Signature | Purpose |
|--------|-----------|---------|
| `default` | `variable \| default: variable` | Sets a default value when the value is `empty`, `false`, or `nil` |
| `default_errors` | `string \| default_errors` | Generates default error messages for each `form.errors` value |
| `default_pagination` | `paginate \| default_pagination` | Generates HTML links for paginated results (applied to `paginate`) |

## font  (part 1)
| Filter | Signature | Purpose |
|--------|-----------|---------|
| `font_face` | `font \| font_face` | Generates a CSS `@font-face` declaration to load the font |
| `font_modify` | `font \| font_modify: string, string` | Modifies a specific property of a font (property, value/amount) |
| `font_url` | `font \| font_url` | Returns the CDN URL for the font in `woff2` format |

## format  (part 1)
| Filter | Signature | Purpose |
|--------|-----------|---------|
| `date` | `string \| date: string` | Formats a date using Ruby strftime parameters |
| `json` | `variable \| json` | Converts a string or object into JSON format |
| `structured_data` | `variable \| structured_data` | Converts an object into schema.org structured data format |
| `weight_with_unit` | `number \| weight_with_unit` | Generates a formatted weight for a variant using the store's weight unit |

## hosted_file  (part 1)
| Filter | Signature | Purpose |
|--------|-----------|---------|
| `asset_img_url` | `string \| asset_img_url` | Returns the CDN URL for an image in a theme's assets directory |
| `asset_url` | `string \| asset_url` | Returns the CDN URL for a file in a theme's `assets` directory |
| `file_img_url` | `string \| file_img_url` | Returns the CDN URL for an image from the admin Files page |
| `file_url` | `string \| file_url` | Returns the CDN URL for a file from the admin Files page |
| `global_asset_url` | `string \| global_asset_url` | Returns the CDN URL for a global asset hosted on Shopify |
| `img_tag` | `string \| img_tag` | Generates an HTML `<img>` tag for a given image URL |
| `script_tag` | `string \| script_tag` | Generates an HTML `<script type="text/javascript">` tag for a resource URL |
| `shopify_asset_url` | `string \| shopify_asset_url` | Returns the CDN URL for a globally accessible Shopify asset |
| `stylesheet_tag` | `string \| stylesheet_tag` | Generates an HTML `<link>` tag for a given resource URL |

## html  (part 1)
| Filter | Signature | Purpose |
|--------|-----------|---------|
| `class_list` | `settings.layout \| class_list` | Generates the list of style classes for a style setting or settings |
| `escape` | `string \| escape` | Escapes special HTML characters (`<>`, `'`, `&`) into escape sequences |
| `highlight` | `string \| highlight: string` | Wraps instances of a string in `<strong class="highlight">` |
| `newline_to_br` | `string \| newline_to_br` | Converts newlines (`\n`) to HTML line breaks (`<br>`) |
| `strip_html` | `string \| strip_html` | Strips all HTML tags from a string |
| `time_tag` | `string \| time_tag: string` | Converts a timestamp into an HTML `<time>` tag (strftime params) |
| `url_escape` | `string \| url_escape` | Escapes any URL-unsafe characters in a string |
| `url_param_escape` | `string \| url_param_escape` | Escapes characters unsafe for URL parameters (incl. `&`) |

## localization  (part 1)
| Filter | Signature | Purpose |
|--------|-----------|---------|
| `currency_selector` | `form \| currency_selector` | Renders a currency selector (applied to a `form` in a currency form) |
| `format_address` | `address \| format_address` | Generates an HTML address ordered per the address's locale |
| `translate (t)` | `string \| t` | Provides translated text for a translation key from a locale file |

## math  (part 1)
| Filter | Signature | Purpose |
|--------|-----------|---------|
| `abs` | `number \| abs` | Returns the absolute value of a number |
| `at_least` | `number \| at_least: minimum_value` | Limits a number to a minimum value |
| `at_most` | `number \| at_most: value` | Limits a number to a maximum value |
| `ceil` | `number \| ceil` | Rounds a number up to the nearest integer |
| `divided_by` | `number \| divided_by: number` | Divides a number; result type matches the divisor |
| `floor` | `number \| floor` | Rounds a number down to the nearest integer |
| `minus` | `number \| minus: number` | Subtracts a given number from another number |
| `modulo` | `number \| modulo: number` | Returns the remainder of dividing by a given number |
| `plus` | `number \| plus: number` | Adds two numbers |
| `round` | `number \| round` | Rounds a number to the nearest integer |
| `times` | `number \| times: number` | Multiplies a number by a given number |

## media  (part 2)
| Filter | Signature | Purpose |
|--------|-----------|---------|
| `external_video_tag` | `variable \| external_video_tag` | Generates an HTML `<iframe>` player for an external video |
| `external_video_url` | `media \| external_video_url: attribute: string` | Returns the URL for an external video, with player parameters |
| `image_tag` | `string \| image_tag` | Generates an HTML `<img>` tag for a given `image_url` |
| `media_tag` | `media \| media_tag` | Generates an appropriate HTML tag for a media object |
| `model_viewer_tag` | `media \| model_viewer_tag` | Generates a Google model-viewer component for a 3D model |
| `video_tag` | `media \| video_tag` | Generates an HTML `<video>` tag for a given video |
| `article_img_url` | `variable \| article_img_url` | Deprecated — replaced by `image_url` |
| `collection_img_url` | `variable \| collection_img_url` | Deprecated — replaced by `image_url` |
| `image_url` | `variable \| image_url: width: number, height: number` | Returns the CDN URL for an image |
| `img_tag` | `string \| img_tag` | Deprecated — replaced by `image_tag` |
| `img_url` | `variable \| img_url` | Deprecated — replaced by `image_url` |
| `product_img_url` | `variable \| product_img_url` | Deprecated — replaced by `image_url` |

## metafield  (part 2)
| Filter | Signature | Purpose |
|--------|-----------|---------|
| `metafield_tag` | `metafield \| metafield_tag` | Generates an HTML element hosting the data from a `metafield` object |
| `metafield_text` | `metafield \| metafield_text` | Generates a text version of the data from a `metafield` object |

## money  (part 2)
| Filter | Signature | Purpose |
|--------|-----------|---------|
| `money` | `number \| money` | Formats a price per the store's HTML-without-currency setting |
| `money_amount` | `number \| money_amount` | Formats a price as a plain decimal string (no symbols/separators) |
| `money_with_currency` | `number \| money_with_currency` | Formats a price per the store's HTML-with-currency setting |
| `money_without_currency` | `number \| money_without_currency` | Formats a price without the currency symbol |
| `money_without_trailing_zeros` | `number \| money_without_trailing_zeros` | Formats a price excluding the decimal separator and trailing zeros |

## payment  (part 2)
| Filter | Signature | Purpose |
|--------|-----------|---------|
| `payment_button` | `form \| payment_button` | Generates an HTML container for accelerated checkout buttons |
| `payment_terms` | `form \| payment_terms` | Generates the HTML for the Shop Pay Installments banner |
| `payment_type_img_url` | `string \| payment_type_img_url` | Returns the URL for an SVG image of a payment type |
| `payment_type_svg_tag` | `string \| payment_type_svg_tag` | Generates an HTML `<svg>` tag for a payment type |

## string  (part 2)
| Filter | Signature | Purpose |
|--------|-----------|---------|
| `append` | `string \| append: '...'` | Append a string to the end of another string |
| `prepend` | `string \| prepend: '...'` | Prepend a string to the start of another string |
| `capitalize` | `string \| capitalize` | Capitalize the first character of the first word |
| `downcase` | `string \| downcase` | Convert a string to lowercase |
| `upcase` | `string \| upcase` | Convert a string to uppercase |
| `camelize` | `string \| camelize` | Convert a string to CamelCase |
| `handleize` | `string \| handleize` | Convert a string to a URL-safe handle (slug) |
| `escape` | `string \| escape` | HTML-escape a string |
| `escape_once` | `string \| escape_once` | HTML-escape without re-escaping already-escaped entities |
| `newline_to_br` | `string \| newline_to_br` | Convert newlines to `<br>` tags |
| `strip` | `string \| strip` | Remove leading and trailing whitespace |
| `lstrip` | `string \| lstrip` | Remove leading (left) whitespace |
| `rstrip` | `string \| rstrip` | Remove trailing (right) whitespace |
| `strip_html` | `string \| strip_html` | Remove all HTML tags |
| `strip_newlines` | `string \| strip_newlines` | Remove all newline characters |
| `remove` | `string \| remove: '...'` | Remove every occurrence of a substring |
| `remove_first` | `string \| remove_first: '...'` | Remove the first occurrence of a substring |
| `remove_last` | `string \| remove_last: '...'` | Remove the last occurrence of a substring |
| `replace` | `string \| replace: 'a', 'b'` | Replace every occurrence of a substring |
| `replace_first` | `string \| replace_first: 'a', 'b'` | Replace the first occurrence of a substring |
| `replace_last` | `string \| replace_last: 'a', 'b'` | Replace the last occurrence of a substring |
| `slice` | `string \| slice: start, length` | Return a substring by start index (and optional length) |
| `split` | `string \| split: ','` | Split a string into an array on a separator |
| `truncate` | `string \| truncate: n, '...'` | Truncate to n characters with an optional ellipsis |
| `truncatewords` | `string \| truncatewords: n, '...'` | Truncate to n words with an optional ellipsis |
| `pluralize` | `number \| pluralize: 'singular', 'plural'` | Return singular or plural form based on a number |
| `url_encode` | `string \| url_encode` | Percent-encode a string for use in a URL |
| `url_decode` | `string \| url_decode` | Decode a percent-encoded URL string |
| `url_escape` | `string \| url_escape` | Escape URL-unsafe characters, preserving URL structure |
| `url_param_escape` | `string \| url_param_escape` | Escape characters (incl. `&`, `=`) for a URL parameter value |
| `base64_encode` | `string \| base64_encode` | Encode a string to Base64 |
| `base64_decode` | `string \| base64_decode` | Decode a Base64 string |
| `base64_url_safe_encode` | `string \| base64_url_safe_encode` | Encode to URL-safe Base64 |
| `base64_url_safe_decode` | `string \| base64_url_safe_decode` | Decode URL-safe Base64 |
| `md5` | `string \| md5` | MD5 hash of a string |
| `sha1` | `string \| sha1` | SHA-1 hash of a string |
| `sha256` | `string \| sha256` | SHA-256 hash of a string |
| `hmac_sha1` | `string \| hmac_sha1: secret` | HMAC-SHA1 hash using a secret key |
| `hmac_sha256` | `string \| hmac_sha256: secret` | HMAC-SHA256 hash using a secret key |
| `blake3` | `string \| blake3` | BLAKE3 hash of a string |

## tag  (part 2)
| Filter | Signature | Purpose |
|--------|-----------|---------|
| `link_to_tag` | `string \| link_to_tag: tag` | Generates a link to a tag-filtered collection page |
| `link_to_add_tag` | `string \| link_to_add_tag: tag` | Generates a link that adds a tag to the current filter set |
| `link_to_remove_tag` | `string \| link_to_remove_tag: tag` | Generates a link that removes a tag from the current filter set |

---

Totale: 155 filtri unici in 18 categorie (array, cart, collection, color, customer, default, font, format, hosted_file, html, localization, math, media, metafield, money, payment, string, tag).

> Nota: il file di reference `10-liquid-filters-part2.md` ripete anche la categoria `math` (già in part 1); qui è indicizzata una sola volta sotto part 1. Il conteggio "166" della doc Shopify deriva da quel doppio conteggio di `math`.
