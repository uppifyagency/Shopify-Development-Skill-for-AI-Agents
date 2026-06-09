# Liquid Objects — index (135)

How to use: find your object below, then open `reference/07-liquid-objects.md` and Grep the heading `### <name>` to read its full property table and examples.

| Object | What it is | Key properties |
|--------|-----------|----------------|
| `additional_checkout_buttons` | Returns `true` if the store has payment providers with offsite (accelerated) checkouts | — (boolean flag) |
| `address` | An address, such as a customer address or order shipping address | address1, city, country, first_name, last_name, zip, summary |
| `all_country_option_tags` | Outputs an `<option>` tag for every country (for a country selector) | — (renders HTML) |
| `all_products` | All products on the store, accessed by handle (limit 20 handles/page) | — (lookup by handle → product) |
| `app` | An app, used for theme app extension data | metafields |
| `article` | A blog post (article) in a blog | title, author, content, image, comments, tags, published_at, url |
| `articles` | All articles across the store's blogs, accessed by handle | — (lookup by handle → article) |
| `block` | The content and settings of a section block | id, type, settings, shopify_attributes |
| `blog` | A specific blog in the store | title, articles, articles_count, all_tags, handle, url |
| `blogs` | All blogs in the store, accessed by handle | — (lookup by handle → blog) |
| `brand` | The store's brand assets | logo, square_logo, cover_image, colors, slogan, short_description, metafields |
| `brand_color` | Colors defined in the store's brand assets | background, foreground (accessed via primary/secondary group + index) |
| `canonical_url` | The canonical URL for the current page | — (string) |
| `cart` | The customer's cart | items, item_count, total_price, currency, total_discount, note, attributes |
| `checkout` | A customer's checkout (Order status / checkout.liquid) | line_items, total_price, shipping_address, customer, tax_lines, transactions |
| `collection` | A collection in the store | title, products, products_count, description, image, filters, sort_options, url |
| `collections` | All collections on the store, accessed by handle | — (lookup by handle → collection) |
| `color` | A color from a `color` setting | red, green, blue, alpha, hue, lightness, rgb, rgba, oklch |
| `color_scheme` | A color scheme from a `color_scheme` setting | id, settings |
| `color_scheme_group` | A color scheme group from a `color_scheme_group` setting | — (iterated for scheme.id and scheme.settings) |
| `comment` | An article (blog) comment | author, content, email, status, created_at, url |
| `company` | A company that a B2B customer is purchasing for | name, id, available_locations, available_locations_count, metafields |
| `company_address` | The address of a company location | address1, city, country, province, zip, street, attention |
| `company_location` | A location of the company a customer is purchasing for | name, company, shipping_address, current?, store_credit_account, url_to_set_as_current |
| `content_for_additional_checkout_buttons` | Renders the checkout buttons for active offsite payment providers | — (renders HTML) |
| `content_for_header` | Dynamically returns all scripts required by Shopify (required in theme.liquid `<head>`) | — (renders scripts) |
| `content_for_index` | Returns the section content for the home page (Liquid index template) | — (renders sections) |
| `content_for_layout` | Returns content based on the current template (required in theme.liquid `<body>`) | — (renders template content) |
| `country` | A country supported by the store's localization options | name, iso_code, currency, market, available_languages, continent, unit_system |
| `country_option_tags` | Outputs `<option>` tags for countries/regions in the store's shipping zones | — (renders HTML) |
| `currency` | Information about a currency | iso_code, name, symbol |
| `current_page` | The current page number (1 for non-paginated resources) | — (number) |
| `current_tags` | The currently applied tags (on blog or collection pages) | — (array of tags) |
| `customer` | A customer of the store | name, email, first_name, orders, addresses, default_address, tags, total_spent |
| `customer_payment_method` | A customer's saved payment method | payment_instrument_type, token |
| `discount` | A discount applied to a cart, line item, or order (deprecated) | title, code, amount, savings, type, total_amount |
| `discount_allocation` | How a discount affects a specific item | amount, discount_application |
| `discount_application` | Information about the intent of a discount | title, value, value_type, type, target_type, target_selection, total_allocated_amount |
| `external_video` | An external video from YouTube or Vimeo | host, external_id, aspect_ratio, media_type, position, preview_image, alt |
| `filter` | A storefront filter | label, type, values, active_values, param_name, operator, url_to_remove |
| `filter_value` | A specific value of a filter | label, value, count, active, url_to_add, url_to_remove, param_name, swatch |
| `filter_value_display` | Visual representation of a filter value (deprecated → swatch) | type, value |
| `focal_point` | The focal point for an image | x, y |
| `font` | A font from a `font_picker` setting | family, style, weight, variants, fallback_families, system? |
| `forloop` | Information about a parent `for` loop | index, index0, first, last, length, rindex, parentloop |
| `form` | Information about a form created by a `form` tag | id, errors, posted_successfully?, first_name, last_name, address1, email |
| `form_errors` | The error category strings for errors from a `form` tag | messages, translated_fields |
| `fulfillment` | An order fulfillment (line items + shipment tracking) | fulfillment_line_items, item_count, tracking_company, tracking_number, tracking_url |
| `generic_file` | A non-image, non-video file from a `file_reference` metafield | url, alt, id, media_type, preview_image |
| `gift_card` | A gift card issued to a customer or recipient | balance, code, currency, expires_on, initial_value, customer, product, url |
| `group` | A group of rules for the robots.txt file | rules, sitemap, user_agent |
| `handle` | The handle of the resource for the current template (article/blog/collection/page/product) | — (string) |
| `image` | An image, such as a product or collection image | src, alt, width, height, aspect_ratio, id, variants, presentation |
| `image_presentation` | The presentation settings for an image | focal_point |
| `images` | All images uploaded to the store, accessed by filename | — (lookup by filename → image) |
| `instructions` | Instructions for a nested cart line item | can_remove, can_update_quantity |
| `line_item` | A line in a cart, checkout, or order (one product variant) | product, variant, quantity, final_price, final_line_price, title, image, properties |
| `link` | A link in a menu | title, url, type, active, current, links, levels, object |
| `linklist` | A menu in the store | title, handle, links, levels |
| `linklists` | All menus in the store, accessed by handle | — (lookup by handle → linklist) |
| `localization` | Countries and languages accessible on the store | country, language, market, available_countries, available_languages |
| `location` | A store location (pickup-enabled) | name, address, id, latitude, longitude, metafields |
| `market` | A group of regions a merchant is targeting for sales | handle, id, metafields |
| `measurement` | A measurement from a dimension/volume/weight metafield | type, unit, value |
| `media` | An abstract media object (image, model, video, external_video) | media_type, id, alt, position, preview_image |
| `metafield` | A metafield attached to a parent object | type, value, list? |
| `metaobject` | A metaobject entry with values for a set of fields | system (+ user-defined field keys) |
| `metaobject_definition` | The structure (field definitions) for a metaobject type | values, values_count |
| `metaobject_system` | Basic system info about a metaobject (grouped under `system`) | handle, id, type, url |
| `metaobjects` | All metaobjects of the store, accessed by type and handle | — (lookup by type/handle → metaobject) |
| `model` | A 3D model uploaded as product media | sources, alt, id, media_type, position, preview_image |
| `model_source` | A model source file | format, mime_type, url |
| `money` | A monetary value in the customer's local (presentment) currency | currency |
| `order` | An order | name, line_items, total_price, customer, financial_status, fulfillment_status, created_at, shipping_address |
| `page` | A page on the store | title, content, handle, author, url, published_at, metafields |
| `page_description` | The meta description of the current page (SEO/social) | — (string) |
| `page_image` | Image shown in search/social previews for the current page | — (image; powers og:image) |
| `page_title` | The title of the current page (SEO/social) | — (string) |
| `pages` | All pages on the store, accessed by handle | — (lookup by handle → page) |
| `paginate` | Information about pagination inside `paginate` tags | current_page, pages, items, page_size, parts, next, previous, current_offset |
| `parent_relationship` | Parent relationship for a nested cart line item | parent |
| `part` | A part in pagination navigation | is_link, title, url |
| `pending_payment_instruction_input` | Header-value pairs for offline payment method instructions | header, value |
| `policy` | A store policy (privacy, return, etc.) | title, body, url, id |
| `powered_by_link` | Renders an HTML link to a localized shopify.com | — (renders HTML link) |
| `predictive_search` | Results from a predictive search query | performed, terms, resources, types |
| `predictive_search_resources` | Arrays of resources returned by a predictive search query | articles, collections, pages, products |
| `product` | A product in the store | title, price, variants, options, featured_image, available, media, metafields, url |
| `product_option` | A product option, such as size or color | name, position, selected_value, values |
| `product_option_value` | A product option value, such as "red" for "color" | name, id, available, selected, swatch, variant, product_url |
| `quantity_price_break` | Per-unit price of a variant at a minimum quantity or more | minimum_quantity, price |
| `quantity_rule` | A variant order quantity rule | min, max, increment |
| `rating` | Information for a `rating` type metafield | rating, scale_min, scale_max |
| `recipient` | A recipient associated with a gift card | email, name, nickname |
| `recommendations` | Product recommendations for a specific product | products, products_count, performed?, intent |
| `remote_details` | Information about the remote source an object came from | shop, type |
| `remote_product` | A product sourced remotely (all product functionality + remote context) | remote_details, title, variants, price, available, options, media |
| `remote_shop` | Information about a remote store | name, brand, policies, refund_policy, shipping_policy |
| `request` | Information about the current URL and page | path, host, origin, page_type, locale, design_mode |
| `robots` | The default rule groups for the robots.txt file | default_groups |
| `routes` | Standard storefront URLs (localization-safe) | root_url, cart_url, search_url, account_url, collections_url, cart_add_url |
| `rule` | A rule for the robots.txt file (Allow/Disallow) | directive, value |
| `script` | Information about a Shopify Script (being sunset) | id, name |
| `search` | Information about a storefront search query | terms, results, results_count, performed, filters, sort_options, types |
| `section` | The properties and settings of a section | id, blocks, settings, index, location |
| `selling_plan` | The intent of how a selling plan affects a line item | name, id, description, options, price_adjustments, checkout_charge, recurring_deliveries, selected |
| `selling_plan_allocation` | How a specific selling plan affects a line item | price, compare_at_price, per_delivery_price, selling_plan, price_adjustments, checkout_charge_amount |
| `selling_plan_allocation_price_adjustment` | Resulting price from a selling_plan_price_adjustment | position, price |
| `selling_plan_checkout_charge` | How a selling plan affects the amount due at checkout | value, value_type |
| `selling_plan_group` | A group of selling plans including a product's variants | name, id, options, selling_plans, app_id, selling_plan_selected |
| `selling_plan_group_option` | An option in a selling plan group | name, position, values, selected_value |
| `selling_plan_option` | A selling plan's value for a group option | name, position, value |
| `selling_plan_price_adjustment` | How a selling plan changes a variant's price over time | value, value_type, position, order_count |
| `settings` | Access to all the theme's settings (settings_schema.json) | — (lookup by setting name) |
| `shipping_method` | The shipping method for an order | title, handle, id, original_price, price_with_discounts, tax_lines, discount_allocations |
| `shop` | Information about the store | name, domain, currency, url, email, metafields, products_count, policies, address |
| `shop_locale` | A language in the store | name, iso_code, endonym_name, primary, root_url |
| `sitemap` | The sitemap for a group in robots.txt | directive, value |
| `sort_option` | A sort option for a collection or search results page | name, value |
| `store_availability` | A variant's inventory info for a physical store location | available, location, pick_up_enabled, pick_up_time |
| `store_credit_account` | A store credit account belonging to a customer | balance |
| `swatch` | Color/image visual representation for option or filter values | color, image |
| `tablerowloop` | Information about a parent `tablerow` loop | col, row, index, first, last, length, col_first, col_last, rindex |
| `tax_line` | A tax line of a checkout or order | price, rate, rate_percentage, title |
| `taxonomy_category` | The taxonomy category for a product | name, id, gid, ancestors |
| `template` | Information about the current template | name, directory, suffix |
| `theme` | Information about the current theme (deprecated values) | id, name, role |
| `transaction` | A transaction associated with a checkout or order | amount, kind, status, gateway, gateway_display_name, payment_details, created_at |
| `transaction_payment_details` | Payment method info used for a transaction | credit_card_company, credit_card_last_four_digits, credit_card_number, gift_card |
| `unit_price_measurement` | How units of a product variant are measured | measured_type, quantity_value, quantity_unit, reference_value, reference_unit |
| `user` | The author of a blog article | name, first_name, last_name, email, bio, image, homepage, account_owner |
| `user_agent` | The user-agent (crawler name) for a robots.txt group | directive, value |
| `variant` | A product variant | id, title, price, available, options, sku, inventory_quantity, image, compare_at_price |
| `video` | A video uploaded as product media or a file_reference metafield | sources, duration, aspect_ratio, alt, media_type, position, preview_image |
| `video_source` | A source file for a video | format, url, mime_type, width, height |

Totale: 135 oggetti indicizzati
