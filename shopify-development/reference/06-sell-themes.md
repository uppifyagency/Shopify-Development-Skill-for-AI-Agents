# 6. Sell Themes (Theme Store)

This chapter is a faithful, 1:1 extraction of the **"Sell themes" (Theme Store)** section of the Shopify Themes documentation. It covers everything a theme developer needs to publish, sell, and grow a theme on the [Shopify Theme Store](https://themes.shopify.com): the full requirements checklist, how to test a theme, the review and submission process, how to build a Theme Store listing, how to be successful after launch (reviews, brand assets, updates, removal, prohibited actions), and how revenue share works.

Each page below preserves the original headings, paragraphs, lists, tables, code blocks, notes, warnings, and tips. The `> Fonte:` line under each page title gives the exact source URL.

---

## Chapter table of contents

1. [Shopify Theme Store (Overview)](#shopify-theme-store-overview) — `/docs/storefronts/themes/store`
2. [Theme store requirements](#theme-store-requirements) — `/docs/storefronts/themes/store/requirements`
3. [Testing your theme for the Shopify Theme Store](#testing-your-theme-for-the-shopify-theme-store) — `/docs/storefronts/themes/store/test-theme`
   - [Testing assets](#testing-assets) — `/docs/storefronts/themes/store/test-theme/assets`
   - [Testing checklist](#testing-your-theme-for-the-shopify-theme-store-checklist) — `/docs/storefronts/themes/store/test-theme/checklist`
4. [Review process](#review-process) — `/docs/storefronts/themes/store/review-process`
   - [Submitting a theme to the Shopify Theme Store](#submitting-a-theme-to-the-shopify-theme-store) — `/docs/storefronts/themes/store/review-process/submit-theme`
   - [Theme Store listing page](#theme-store-listing-page) — `/docs/storefronts/themes/store/review-process/listings`
5. [Being successful in the Shopify Theme Store](#being-successful-in-the-shopify-theme-store) — `/docs/storefronts/themes/store/success`
   - [Prohibited actions on the Shopify Theme Store](#prohibited-actions-on-the-shopify-theme-store) — `/docs/storefronts/themes/store/success/prohibited-actions`
   - [Managing theme reviews](#managing-theme-reviews) — `/docs/storefronts/themes/store/success/managing-theme-reviews`
   - [Shopify Brand Assets for Marketing Your Theme](#shopify-brand-assets-for-marketing-your-theme) — `/docs/storefronts/themes/store/success/brand-assets`
   - [Updating your theme](#updating-your-theme) — `/docs/storefronts/themes/store/success/updates`
   - [Removing your theme from the Shopify Theme Store](#removing-your-theme-from-the-shopify-theme-store) — `/docs/storefronts/themes/store/success/remove-theme`
6. [Revenue share for Shopify Theme Store developers](#revenue-share-for-shopify-theme-store-developers) — `/docs/storefronts/themes/store/theme-revenue-share`

---

## Shopify Theme Store (Overview)

> Fonte: https://shopify.dev/docs/storefronts/themes/store

# Shopify Theme Store

The [Shopify Theme Store](https://themes.shopify.com) is one of the first stops in a merchant's journey to launching their online store. With flexible pricing and smart marketing features, building themes for the Shopify Theme Store is a great way to build your business while helping millions of merchants build theirs.

## 1. Get to know our requirements

The first step to becoming a Shopify Theme Partner is to get familiar with our Theme Store requirements. Our checklist covers everything from technical and performance requirements to theme design and user experience.

> **Warning:** Themes must meet all of our requirements to be published in the Shopify Theme Store.

## 2. Test your theme

To ensure that your theme contains the required Shopify features, and to ensure that it's flexible, resilient, and performant, you should test it before submission.

## 3. Submit your theme

When you're ready to share your theme, learn about the review process and how to submit your theme to the Shopify Theme Store. We'll help you craft a Theme Store listing so that merchants can understand the full potential of your theme.

## 4. Grow your theme business

After you're published on the Shopify Theme Store, learn how to make your theme more successful by supporting your theme, keeping it up to date, and managing merchant reviews. You can download the brand assets that you need to promote your theme in your own marketing materials.

> **Tip:** New to Shopify themes? Start here.

## 5. Learn about theme revenues

> Themes sold through the Shopify Theme Store are subject to a 15% revenue share.

---

## Theme store requirements

> Fonte: https://shopify.dev/docs/storefronts/themes/store/requirements

# Theme store requirements

Our Theme Store is a canvas for creativity, innovation, and merchant expression. We're looking for unique, original submissions that push design boundaries, offer standout visual quality, and deliver delightful, engaging user experiences. Themes should be visually distinctive, professionally crafted, and empower merchants to tell their brand's story clearly and expressively. We value themes that not only meet merchants' functional business needs, but also actively inspire merchants and their customers, elevating online shopping experiences through thoughtful layouts, bold visuals, purposeful creativity, and intuitive, high-quality usability.

[Themes and presets](https://shopify.dev/docs/storefronts/themes/architecture/config/settings-data-json) published on the Shopify Theme Store must meet all requirements. If your submission misses any requirement, then it will be rejected and you'll need to make corrections before resubmitting.

Test your theme thoroughly before submitting to ensure it meets functionality and quality standards. Poorly tested themes will be rejected without further review, and repeated issues may lead to suspension or permanent rejection.

Learn about the theme review process and how to [submit your theme to the Shopify Theme Store](https://shopify.dev/docs/storefronts/themes/store/review-process/submit-theme).

---

### 1. Theme Store exclusivity

Themes on the Theme Store must be exclusive to the Theme Store and can't contain external marketing material, so merchants can continue to benefit from the highest quality themes and the newest features.

All themes must meet the following exclusivity requirements:

- Themes listed on the Shopify Theme Store can only be distributed through the Shopify Theme Store. Themes on the Theme Store must not be distributed on other marketplaces.
- Themes on the Shopify Theme Store can't contain designer credits, such as a link to a theme developer's website, or any affiliate links in the theme files.

---

### 2. Uniqueness from other themes

Your theme must be fundamentally different from other themes on the [Shopify Theme Store](https://themes.shopify.com) (including your own). You must make meaningful design and functional innovations beyond minor cosmetic changes. Clear differentiation builds merchant trust by keeping theme quality high, and helps merchants find the right fit faster.

We use these standards to evaluate uniqueness:

- Uniqueness is measured by the overall experience across core templates and elements. You may reuse components and libraries, but how you assemble them must be substantially different.

- Your theme's identity and capabilities must not be easily reproducible. They should not be achievable by adjusting settings, superficial styling, or adding a few sections or options to another theme. Reproducing your overall experience should require substantial structural changes to the theme.

- Use an inventive art direction that distinguishes the theme, with clear systems for header and navigation, product cards, media treatments, and page structure.

- Cosmetic or additive alterations are insufficient. For example: spacing tweaks, color or typography swaps, gradients, shape dividers, background effects or blurs, animation or transition tweaks, or adding a few settings or sections to an existing codebase.

- Embed uniqueness at the architectural level so the theme remains unmistakably its own as new settings, sections, and features are added.

- A merchant shouldn't be able to buy your theme then customize it to appear almost identical to a different theme on the Shopify Theme Store.

> **Note:** [Shopify's Skeleton Theme](https://github.com/shopify/skeleton-theme) is the only approved codebase for Theme Store development. Otherwise, themes must be built with fully original code. New theme submissions built on or derived from Dawn or Horizon are not eligible for the Shopify Theme Store.

---

### 3. Theme design and UX

The UX & Design criteria below set clear, objective expectations for the exceptional quality required on the Shopify Theme Store. Themes must meet **every** checkpoint listed below to be accepted. If your theme fails any of these requirements, you must address the issue before acceptance.

#### Visual design and art direction

- **Unique and intentional design:** Your theme clearly stands apart, does not closely resemble existing themes on the Theme Store, and clearly targets a specific merchant type or industry with a thoughtful, deliberate visual style.

- **Professional-quality visuals:** All images, graphics, and icons across your theme are high-quality, clear, appropriately sized, and consistent. No blurry, stretched, pixelated, or clipart-level imagery is present.

- **Simple, complementary color palette:** You include cohesive colors throughout the theme. Colors work well together without clashing or reducing readability.

#### Layout

- **Clear, organized page structure:** Your design clearly follows a logical grid structure. Spacing and alignment between sections and blocks feel deliberate and consistent, making the page easy to scan and visually balanced.

- **Clear content hierarchy:** Your design intentionally guides user attention toward important elements first by clearly using size, color, contrast, and position to emphasize key details. Secondary information clearly appears smaller, lighter, or appropriately lower-priority, creating a clear design hierarchy that's easy to follow and visually appealing.

- **Flexible layouts that look intentional:** Layouts are designed deliberately to remain visually appealing, organized, and balanced, even when content length, number of images, or text quantity changes. Page structures remain attractive and professional, avoiding awkward gaps, large blank areas, or broken layouts when content varies.

#### Consistency

- **Consistent typography:** Avoid using an over abundance of fonts throughout the theme, choosing fonts that clearly complement each other visually. All text uses consistent font pairing everywhere, resulting in a clean, balanced look that's attractive and easy to read.

- **Consistent visual and interaction design:** Interactive elements such as buttons, links, and forms use consistent styles, size, colors, and behaviors everywhere in the theme.

- **Settings clearly organized:** Theme customization in the theme editor must be easy for merchants to understand and use. Settings must use simple, merchant-friendly language and be grouped logically so that common tasks are discoverable without extensive searching.

- **Merchant-first theme editor experience:** Themes in the Shopify Theme Store are evaluated using a merchant-first approach. Customization in the theme editor must be intuitive and consistent. Settings must prioritize merchant clarity and discoverability. There must be a balance between flexibility and opinionated settings.

#### Customer shopping experience

- **Clear & effortless navigation:** Customers can easily navigate from homepage to product discovery, product pages, cart, and checkout without confusion or friction.

- **Thoughtful product discovery:** Theme design thoughtfully guides customers toward relevant products or collections—clearly helping them discover items they might want, through intuitive menus, featured collections, or clearly presented recommendations.

- **Frictionless shopping interactions:** The shopping experience is smooth, easy, and completely frustration-free. All key customer actions—such as choosing product options, adding to cart, editing cart items, and moving to checkout—are clear, intuitive, and immediately responsive.

#### Demo store experience

- **Complete, realistic demo store:** Your demo store showcases a fully realistic example of a merchant's business, using thoughtfully selected products, professional images, real-life scenarios, and clearly written, original text—no "Lorem Ipsum" or placeholder content.

- **Relevant, intentional sections:** All sections and features shown in your demo store explicitly fit the type of business being portrayed. Sections clearly make sense and realistically help merchants showcase their products—avoid using sections or interactions that do not logically support the store's products or message.

- **Inspiring merchant experience:** Your demo inspires merchants with engaging content, attractive layouts, and realistic, intentional product displays.

Learn more about [design best practices](https://shopify.dev/docs/storefronts/themes/best-practices/design).

---

### 4. Features

Feature-rich themes support the varied needs of merchants, and enable each merchant to use a theme in a way that fits their business.

All themes must support the following features:

**Sections Everywhere** - Refer to [**Templates, sections, and blocks**](https://shopify.dev/themes/store/requirements#templates) to ensure compatibility with Online Store 2.0.

Learn more about [migrating a theme to OS 2.0](https://shopify.dev/docs/storefronts/themes/best-practices/version-control).

**Discounts** - [Display discount amounts](https://shopify.dev/docs/storefronts/themes/pricing-payments/discounts) for individual items and for entire orders in the cart, checkout, and order templates. Discounts must be supported on the Cart page.

Learn more about [discounts](https://help.shopify.com/manual/discounts).

**Accelerated checkout buttons** - Include [accelerated checkout buttons on product pages](https://shopify.dev/docs/storefronts/themes/architecture/templates/product#accelerated-checkout-buttons) and [cart pages](https://shopify.dev/docs/storefronts/themes/pricing-payments/accelerated-checkout#implementing-accelerated-checkout-buttons-in-your-theme) so that customers can checkout quickly.

Accelerated checkout buttons must be supported on the following pages:

- Product page
- Cart page

The branded dynamic and accelerator checkout button colors must not be modified.

Learn more about [accelerated checkout](https://help.shopify.com/manual/payments/accelerated-checkouts).

**Faceted search filtering** - Use [search filtering](https://shopify.dev/docs/storefronts/themes/navigation-search/filtering) so that customers can filter on collection and search pages based on product availability, price, type, vendor, and variant options. You need to support faceted search filtering on collection pages and search pages.

**Gift cards** - Include a [gift card template](https://shopify.dev/docs/storefronts/themes/architecture/templates/gift-card-liquid) that renders the gift card page, which displays the gift card that's issued to a customer upon purchase.

Learn more about [gift cards](https://help.shopify.com/manual/products/gift-card-products).

**Image focal points** - Make sure that your theme supports the [focal point](https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings#image-focal-points) of an image. Focal points can be set in the theme editor `image_picker` setting, or from the **Files** page in the Shopify admin.

**Images for social sharing** - Add a [`page_image` object](https://shopify.dev/docs/api/liquid/objects/page#page-image) for social sharing so that merchants can display a thumbnail image in their post when they share a link to their online store on social media, such as on Facebook or Pinterest.

Learn more about [social media images](https://help.shopify.com/manual/online-store/images/showing-social-media-thumbnail-images).

**Country selection** - When merchants sell to other countries and regions [in their local currency](https://shopify.dev/docs/storefronts/themes/markets/multiple-currencies-languages#the-country-selector) customers must be able to select their currency and their country or region on the storefront. Selectors must follow the [UX guidelines](https://shopify.dev/docs/storefronts/themes/markets/country-language-ux).

Learn more about [selling in multiple currencies](https://help.shopify.com/manual/payments/shopify-payments/multi-currency).

**Language selection** - When merchants sell [in multiple languages](https://shopify.dev/docs/storefronts/themes/markets/multiple-currencies-languages#the-language-selector), customers must be able to select their preferred language on the storefront. Selectors must follow the [UX guidelines](https://shopify.dev/docs/storefronts/themes/markets/country-language-ux).

Learn more about [selling in multiple languages](https://help.shopify.com/manual/cross-border/multilingual-online-store).

**Multi-level menus** - Add [nested menus](https://shopify.dev/docs/storefronts/themes/navigation-search/navigation) so that merchants can create multi-level drop down menus.

Learn more about [setting up drop down menus](https://help.shopify.com/manual/online-store/menus-and-links/drop-down-menus).

**Newsletter forms** - Add a [newsletter signup](https://shopify.dev/docs/storefronts/themes/customer-engagement/email-consent#newsletter-sign-up-form) so that merchants can collect customer email addresses to use in email marketing campaigns.

Learn more about [newsletter signups](https://help.shopify.com/manual/online-store/themes/customizing-themes/add-newsletter).

**Pickup availability** - [Add pickup availability to product pages](https://shopify.dev/docs/storefronts/themes/delivery-fulfillment/pickup-availability) so that merchants can display whether a product is available for local pickup without having to add the product to cart. Pickup availability must be supported on the Product page.

Learn more about [pickup availability](https://help.shopify.com/manual/shipping/setting-up-and-managing-your-shipping/local-methods/local-pickup#show-pickup-availability-to-your-customers).

**Related product recommendations** - Add a section to your product pages that displays an automatically generated list of [related product recommendations](https://shopify.dev/docs/storefronts/themes/product-merchandising/recommendations/related-products). Displaying related products to customers makes it easier for them to discover new products, and can help to increase online store sales.

Learn more about [related product recommendations](https://help.shopify.com/manual/online-store/themes/customizing-themes/add-product-recommendations).

**Complementary product recommendations** - Add [complementary products](https://shopify.dev/docs/storefronts/themes/product-merchandising/recommendations/complementary-products) to product pages so that merchants can display other products that pair well with a product.

Learn more about [complementary product recommendations](https://help.shopify.com/manual/online-store/themes/customizing-themes/add-complementary-products).

**Rich product media** - [Add rich product media](https://shopify.dev/docs/storefronts/themes/product-merchandising/media) such as 3D models, embedded videos, and Vimeo or YouTube videos. Include rich product media in the product template, featured product section, and product forms such as quick view features.

**Search box or a link to search** - The search box or a link to search must include the following:

- A [search template](https://shopify.dev/docs/storefronts/themes/architecture/templates/search)
- [Predictive search](https://shopify.dev/docs/storefronts/themes/navigation-search/search/predictive-search) functionality

**Selling plans** - Merchants are able to create selling plans to offer subscriptions. Selected selling plans need to be [shown to customers in the cart and on customer order pages](https://shopify.dev/docs/storefronts/themes/pricing-payments/subscriptions/add-subscriptions-to-your-theme#customer-order-selling-plan-display).

Selling plans must be supported on the following pages:

- Cart page
- Customer page

Learn more about [subscriptions](https://help.shopify.com/manual/products/subscriptions).

**Shop Pay Installments** - Add a [Shop Pay Installments banner](https://shopify.dev/docs/storefronts/themes/pricing-payments/installments) on `product.liquid` to let customers know that they have the option to pay for their order using installments. Shop Pay Installments must be supported on the Product page.

Learn more about [Shop Pay Installments](https://help.shopify.com/manual/payments/shop-pay-installments).

**Unit pricing** - Merchants in some areas are required to [show unit prices](https://shopify.dev/docs/storefronts/themes/pricing-payments/unit-pricing).

Unit pricing must be supported on the following pages:

- Collection page
- Product page
- Cart page
- Customer page

Learn more about how merchants can add unit prices to products in [the European Union (EU) and in Switzerland](https://help.shopify.com/manual/products/details/product-pricing/unit-pricing).

**Variant images** - [Enable themes to use variant images](https://shopify.dev/docs/storefronts/themes/product-merchandising/variants) so that merchants can associate an image with a product variant.

Learn more about [adding images to product variants](https://help.shopify.com/manual/products/product-media/add-images-variants).

**Follow on Shop** - Add a **Follow on Shop button** using the [login\_button](https://shopify.dev/docs/api/liquid/filters/login_button) Liquid filter to enable a customer to follow a store in the Shop app.

The branded **Follow on Shop** button colors must not be modified.

Learn more about [Follow on Shop](https://help.shopify.com/manual/online-store/themes/customizing-themes/follow-on-shop).

---

### 5. Templates, sections, and blocks

Merchants can use sections and blocks to arrange page templates, which provides more flexibility in their store's content, and allows them to control the look and feel of their online store without needing to edit code.

#### Template support requirements

Themes must support the following templates and their formats:

- `theme.liquid` (layout file)
- `404.json`
- `article.json`
- `blog.json`
- `cart.json`
- `collection.json`
- `index.json`
- `list-collections.json`
- `page.json`
- `page.contact.json`
- `password.json`
- `product.json`
- `search.json`
- `gift_card.liquid`
- `settings_data.json` (config file)
- `settings_schema.json` (config file)

#### Section support requirements

- All templates must support sections (JSON templates), with the exception of Customer Account pages, Gift Card pages, and Checkout, which don't need to support sections.
- Themes must include a **Custom Liquid** section. The section needs to include a setting of type [`liquid`](https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings#liquid), and should be available on all templates that support sections. The **Custom Liquid** section can act as an insertion point for certain types of apps.
- Header and footer sections must be rendered within [section groups](https://shopify.dev/docs/storefronts/themes/architecture/section-groups). Section groups allow merchants to dynamically add, remove, and reorder sections in the header and footer areas of the layout.

#### Block and app block support requirements

- Themes must support blocks for all or most elements on the main section of the product page. For example, elements such as product price, product vendor, and product description should each be individual blocks within the main product section. Refer to [Dawn's main product section](https://github.com/Shopify/dawn/blob/main/sections/main-product.liquid) for an example of how these blocks should be implemented.
- Themes must support [app blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks) (blocks of type `@app`) in the main product section and featured product section.
- Introduce **Custom Liquid** blocks into certain sections. Add a **Custom Liquid** block anywhere you'd consider adding an [app block](https://shopify.dev/docs/storefronts/themes/best-practices/templates-sections-blocks#considerations-for-app-blocks), because the **Custom Liquid** block can act as an insertion point for certain types of apps. This block should include a setting of type [`liquid`](https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings#liquid).

Learn more about [best practices for sections and blocks](https://shopify.dev/docs/storefronts/themes/best-practices/templates-sections-blocks).

> **Note:** Do not include the `config/markets.json` file with your theme when submitting.

---

### 6. Lighthouse performance and accessibility

Performance and accessibility are important factors for merchants when they choose a theme for their online store. Optimizing your theme for performance and accessibility is key to the success of the merchants that you support, and the experience of their customers.

#### Lighthouse performance and accessibility requirements

- Themes must have a minimum average Lighthouse performance score of **60** across the theme's product, collection, and home page, for both desktop and mobile. Tests are run using a [benchmark dataset](https://shopify.dev/docs/storefronts/themes/best-practices/performance#run-a-lighthouse-audit-using-shopify-data).
- Themes must have a minimum average Lighthouse accessibility score of **90** across the theme's product, collection, and home page, for both desktop and mobile. Tests are run using a [benchmark dataset](https://shopify.dev/docs/storefronts/themes/best-practices/performance#run-a-lighthouse-audit-using-shopify-data).

When verifying performance and accessibility scores, sections must contain actual images and content. The sections can't be empty.

#### Testing the performance of your theme

You can quickly test the [performance](https://shopify.dev/docs/storefronts/themes/best-practices/performance) of your theme before you submit it to the Shopify Theme Store by running performance tests against a benchmark shop. If you want to test your theme before you submit it, then refer to these [performance best practices](https://shopify.dev/docs/storefronts/themes/best-practices/performance#testing-for-performance).

#### Testing the accessibility of your theme

You can quickly test the [accessibility](https://shopify.dev/docs/storefronts/themes/best-practices/accessibility) of your theme before you submit it to the Shopify Theme Store by running accessibility tests against a benchmark shop. If you want to test your theme before you submit it, then refer to these [accessibility best practices](https://shopify.dev/docs/storefronts/themes/best-practices/accessibility#accessibility-testing).

---

### 7. Pages

Including well-designed page types in your theme enables merchants to build all of the elements they need to run their online store.

#### Layout page requirements

- If payment method logos are output, then use the `enabled_payment_types` property of the [`shop` object](https://shopify.dev/docs/api/liquid/objects/shop), and the [`payment_type_img_url`](https://shopify.dev/docs/api/liquid/filters/payment_type_img_url) or [`payment_type_svg_tag`](https://shopify.dev/docs/api/liquid/filters/payment_type_svg_tag) filter, to output payment icons. The icons must be in full color.
- The `<html>` element must specify a `lang` attribute. The `lang` attribute value can be populated with the `locale` property of the [`request` object](https://shopify.dev/docs/api/liquid/objects/request#request-locale).

```liquid
<html ... lang="{{ request.locale.iso_code }}">
```

- You must use the [`routes` object](https://shopify.dev/docs/api/liquid/objects/routes) for generating dynamic URLs to your storefront. Instead of `href=/` to link to the homepage, you can now use `href="{{ routes.root_url }}"`. This ensures that your theme supports any changes that Shopify makes to the URL format, such as allowing a page to be available in multiple languages.
- Don't modify or parse the `content_for_header` object. If `content_for_header` changes, then your Liquid's behavior changes.

#### Product page requirements

The product page must contain the following product information:

- `product.title` (not truncated)
- `variant.price`
- `variant.unit_price`
- variant's compare-at price
- `product.description`
- option names and option values

Additional product page requirements:

- All product images must be displayed and viewable. Different image ratios shouldn't break the layout.
- Variant images must be shown when the associated variant is selected.
- The product page must use `cart.taxes_included` to display an indication that taxes are included in the price when a store is using tax-inclusive prices.
- The product page must contain the following buying functions:
  - Variants that are split up into separate options for users to select.
  - The ability to select a quantity.
  - An **Add to cart** button (often disabled or replaced when an unavailable variant combination, or sold-out variant, is selected).
  - A callback function to update the price, compare-at-price, and sold-out messages for the currently selected variant.
  - The [first available variant](https://shopify.dev/docs/api/liquid/objects/product#product-selected_or_first_available_variant) loads on a page.

- The product page must support the following features:
  - Product recommendations
  - Rich product media
  - Accelerated checkout buttons (must be enabled by default)
  - Pickup availability
  - Shop Pay Installments

- Gift card products must have the option to send the card to a [recipient](https://shopify.dev/docs/api/liquid/objects/gift_card#gift_card-recipient).

- The following attributes of the [`form` object](https://shopify.dev/docs/api/liquid/objects/form) must be used:
  - `form.email`
  - `form.name`
  - `form.message`

- The following attribute of the [`gift_card` object](https://shopify.dev/docs/api/liquid/objects/gift_card) must be used:
  - `send_on`

- For product options, swatches must be supported to visually display either a hex or an image of the given product option. Use the following attributes of the `swatch` [object](https://shopify.dev/docs/api/liquid/objects/swatch) output:
  - `swatch.image`
  - `swatch.color`

#### Collection page requirements

Attributes of the [`collection` object](https://shopify.dev/docs/api/liquid/objects/collection) that must be outputted:

- `collection.title` (not truncated)
- `collection.description`
- `collection.image`

Additional collection page requirements:

- Products must be listed in a grid or list, with the following attributes of the [`product` object](https://shopify.dev/docs/api/liquid/objects/product) output:
  - `product.title` (not truncated and links to product.url)
  - `product.price`
  - `product.images`
  - `variant.unit_price`
  - At least one piece of media for a product

- Product grid must not break because of product images of varying aspect ratios.
- The **Sale** badge or `product.compare_at_price_max` is shown when appropriate.
- Must provide the ability to sort the products inside [collections](https://shopify.dev/docs/storefronts/themes/architecture/templates/collection).
- Must display a message if a collection has no products in it.
- If a product has variants with different prices, then use `product.price_varies` to show the price variation. For example, show the range between `product.price_min` and `product.price_max`.
- Must use [pagination or lazy loading](https://shopify.dev/docs/api/liquid/tags/paginate).

#### Collection List page requirements

Attributes of the [`collection` object](https://shopify.dev/docs/api/liquid/objects/collection) that must be outputted:

- `collection.title` (not truncated)

Additional collection list page requirements:

- Must use `collection.featured_image`. If a [collection image](https://shopify.dev/docs/api/liquid/objects/collection#collection-image) doesn't exist, this property loads the featured image of the first product in that collection instead.
- Must use [pagination or lazy loading](https://shopify.dev/docs/api/liquid/tags/paginate).

#### Cart page requirements

Must display details of the [`line_item` object](https://shopify.dev/docs/api/liquid/objects/line_item), including:

- `title`
- `unit_price`
- `image`
- `final_price`
- `quantity`
- `options_with_values`

Additional cart page requirements:

- The [`cart.total_price`](https://shopify.dev/docs/api/liquid/objects/cart#cart-total_price) must be visible.
- The cart page must use `cart.taxes_included` to display an indication that taxes are included in the price when a store is using tax-inclusive prices.
- Must include a checkout button that submits the cart form.
- Must refresh all line items when the quantity is updated to ensure the total updates correctly.
- Must provide the ability to change the quantity of each line item.
- Must display a message when the cart is empty.
- The cart page must support the following features:
  - Cart notes
  - Selling plans
  - Automatic discount codes
  - Accelerated checkout buttons (must be enabled by default)

#### Page requirements

Must include:

- `page.title`
- `page.content`

Must include an alternate template for a contact form.

#### Blog page requirements

- Attributes of the [`blog` object](https://shopify.dev/docs/api/liquid/objects/blog) must output the [blog.title](https://shopify.dev/docs/api/liquid/objects/blog#blog-title).
- Each [article](https://shopify.dev/docs/api/liquid/objects/article) must display the following information:
  - `article.title` (not truncated, links to `article.url`)
  - `article.image`
  - `article.excerpt_or_content` not `article.content`

- Must use [pagination or lazy loading](https://shopify.dev/docs/api/liquid/tags/paginate).

#### Article page requirements

An [article](https://shopify.dev/docs/api/liquid/objects/article) must display the following information:

- `article.title` (not truncated)
- `article.comments`
- `article.published_at` (but not `article.created_at`)

Additional article page requirements:

- Comments must be [paginated](https://shopify.dev/docs/api/liquid/tags/paginate).
- Comments workflow must function without moderation, and all success or error messages must be properly output.

#### Search page requirements

- Must return a message if there are no search results.
- Must have the ability to return different object types (products, blogs, pages). The `object_type` must be used when displaying [search results](https://shopify.dev/docs/api/liquid/objects/search).
- [Pagination or lazy loading](https://shopify.dev/docs/api/liquid/tags/paginate).

#### 404 page requirements

- Must have a clear message stating that the page wasn't found.
- Must have options for how to proceed, such as a search bar or a link to the homepage.

#### Gift Card page requirements

- Must support [Apple Wallet](https://shopify.dev/docs/storefronts/themes/architecture/templates/gift-card-liquid#apple-wallet-passes).
- Must show a gift card code.
- Must show a QR code. The minimum size required is 120px x 120px.
- Must include the logo or `shop.name`.

#### Customer page requirements

Must display details of the [`line_item` object](https://shopify.dev/docs/api/liquid/objects/line_item), including:

- `line_item.unit_price`

Additional customer page requirements:

- The customer page must support the following features:
  - Selling plans
  - Unit pricing

#### Password page requirements

Must include the following information:

- the logo or `shop.name`
- `shop.password_message`
- a way to enter the [storefront's password](https://shopify.dev/docs/api/liquid/tags/from#form-storefront_password)

---

### 8. Consistency and functionality

Building a theme that functions properly and consistently ensures that merchants can rely on the quality of your theme.

All themes must meet the following functional requirements:

- All RTE-generated content must be consistent (such as `h1`-`h6`, `blockquotes`, `ul`, `ol`) across all templates. Styling of RTE content is consistent with those of blog articles, product descriptions, and collection descriptions.
- Scripts included in theme code must be hosted on Shopify's servers, with the exception of approved third-party libraries.
- Themes must not include any Javascript or code that interferes with, or augments, any native Shopify feature within the theme editor or Shopify admin.
- Any link in the code that points to one of Shopify's domains can take multiple attributes, but must include a `rel="nofollow"` attribute.
- You must link assets using protocol-relative URLs. Hard-defining `http` or `https` isn't permitted.
- The appropriate licenses must be obtained for all third party plugins and images.
- Themes must not include functionality that's dependent on an app.
- Themes must not incorporate app-like functionalities that require API access for full functionality. Examples include wishlists, appointment scheduling, cart-level discount codes, or an Instagram feed. Incomplete features resembling those found in apps will not be accepted.
- Themes must not mislead or deceive merchants or customers with false data or claims. Examples include fake urgency and scarcity tactics like fictitious countdown timers, stock levels, or viewer activity counts.

---

### 9. Browser compatibility

Ensure that your theme lets merchants access the same information and experience across different browsers.

#### Desktop browser requirements

A theme's layout, browsing experience, and purchasing actions must support the following desktop browsers and releases:

- Safari - latest two releases for Mac
- Chrome - latest three releases for Mac and PC
- Firefox - latest three releases for Mac and PC
- Edge - latest two releases for PC

#### Mobile browser requirements

A theme's layout must meet the following mobile browser layout requirements:

- Themes must be mobile responsive.

A theme's layout, browsing experience, and purchasing actions must support the following mobile browsers and releases:

- Mobile Safari - latest two releases for iOS
- Chrome Mobile - latest three releases for Android and iOS
- Samsung Internet - latest two releases for Android

#### Webviews and other application requirements

Themes must support browsing and purchasing actions when rendered in webviews for the following applications:

- Instagram - latest release for Android and iOS
- Facebook - latest release for Android and iOS
- Pinterest - latest release for Android and iOS

---

### 10. Assets

All themes must meet the following requirements, so their assets are delivered by the Shopify platform in an optimal manner.

- Themes must not use Sass, or include `.scss` or `.scss.liquid` files. Instead, use only native CSS, and write or compile your stylesheets into `.css` or `.css.liquid` files.
- Themes must not include minified `.css` or `.js` files, with the exception of ES6 and third-party libraries. Shopify automatically minifies CSS files, as well as JavaScript files that use ES5 syntax or lower, when they're requested by the storefront.

---

### 11. Search engine optimization (SEO)

Effective SEO helps you build better relationships with your audience, improve the merchant experience, and drive more people to your theme.

All themes must meet the following SEO requirements:

- Themes must contain the [theme SEO metadata](https://shopify.dev/docs/storefronts/themes/seo/metadata) code snippet with the title, meta description, and canonical URL.
- Themes must include Google's rich product snippets. To test your structured data, use [Google's Structured Data Testing Tool](https://developers.google.com/structured-data/testing-tool).
- Themes must not include a `robots.txt.liquid` template.

Learn more about [SEO best practices](https://shopify.dev/docs/storefronts/themes/seo).

---

### 12. Accessibility

Accessibility for your theme is essential to providing an inclusive experience for both merchants and customers. An accessible theme is designed so that it can be used by everyone, including people with vision impairment.

All themes must meet the following accessibility requirements:

- All parts of a page must be keyboard accessible, including dropdown navigation.
- When navigating with the keyboard, focusable elements must feature a visible focus state.
- All images require the `alt` attribute. Themes must use [`image.alt`](https://shopify.dev/docs/api/liquid/objects/image#image-alt) or [`image_url | image_tag: alt: string`](https://shopify.dev/docs/api/liquid/filters/image_tag#image_tag-alt) for product images.
- Form inputs must have a unique ID, and labels with `for` attributes that match the input ID.
- Themes must be built with valid HTML.
- Text color contrast ratio must be 4.5:1 for main body content. For text larger than 18pt, and non-text elements such as borders and icons, the color contrast ratio must be 3:1.
- Keyboard focus order must match the DOM order. Focus is expected to move top-bottom, left-right.
- The size of the touch target for pointer inputs must be at least 24 by 24 CSS pixels. The minimum size doesn't apply to inline body text, or elements that meet [other exception criteria](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html).
- Headings `h1`-`h6` must be visually different from each other.

Learn more about [accessibility best practices](https://shopify.dev/docs/storefronts/themes/best-practices/accessibility).

---

### 13. Social media

Social media links help merchant grow their followers.

All themes must meet the following requirements for social media:

- Must have a set of social media icons to choose from.
- Must contain [Open Graph](https://ogp.me/) and [Twitter card tags](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/markup).
- Social media placeholder text must be left empty.

---

### 14. Settings

Settings for sections, blocks, and presets should be clearly named and structured to align with merchant expectations. Avoid unnecessarily deep nesting of blocks or complicated configuration structures that make it hard to find or understand primary controls.

#### Basic requirements

- All theme settings must adhere to the [text style](#text-style-requirements) and [terminology](#terminology-requirements) requirements.
- The setting labels and informational text for the theme must be grammatically correct and free of spelling errors.
- Default setting values for section and block content should indicate how to use the setting. Don't use Lorem Ipsum text or demo store content as a placeholder.
- Must have a favicon setting.
- Logo upload must work with images of different aspect ratios (for example, landscape or portrait).
- All [settings](https://shopify.dev/docs/storefronts/themes/architecture/config/settings-schema-json) must have a `label`.
- All settings of type `link_list` in the Header or Footer must have a `default` value of `main-menu` or `footer`, depending on the location of the setting.
- When you supply a default value for resource-based settings such as product, the referenced resource must exist.
- For [`metaobject`](https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings#metaobject) and [`metaobject_list`](https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings#metaobject_list) settings, only standard definitions can be used as `metaobject_type`. Custom or app-owned definitions cannot be used.
- Must have a [`theme_info`](https://shopify.dev/docs/storefronts/themes/architecture/config/settings-schema-json) section.

#### Theme editor event requirements

- Changes made in the theme editor must be reflected in the editor preview. Refer to [`request.design_mode`](https://shopify.dev/docs/api/liquid/objects/request#request-design_mode) for troubleshooting.

#### Text style requirements

- Write section, preset, and category names in sentence case. Only capitalize the first word and proper nouns (like 'Facebook').
- Use descriptive setting names for multi-option settings or sections of different variations. Avoid using numbered options or section titles, with the exception of colors and color schemes.

| Use this | Don't use this |
| --- | --- |
| Logo position on large screens- Middle left- Top left- Top center | Logo position on large screens- Position 1- Position 2- Position 3 |
| Theme sections- Collage- Image banner- Image with text | Theme sections- Image 1- Image 2- Image 3 |

Use language that's intuitive and easy to understand for all merchants. For example:

- Use "Horizontal position" or "Vertical position" instead of "X position" or "Y position".
- Use "Button label" instead of "CTA label".

Use American English.

| Use this | Don't use this |
| --- | --- |
| **canceled** | cancelled |
| **catalog** | catalogue |
| **center, centered** | centre, centred |
| **color** | colour |
| **customize** | customise |
| **dialog** | dialogue |
| **gray** | grey |
| **organize** | organise |

- Don't use ampersands ( **&** ).
- Use declarative statements instead of questions.

| Use this | Don't use this |
| --- | --- |
| **Use a custom logo** | Use a custom logo? |

- The subject of each section (like 'slideshow') is stated only once in the heading. Avoid subject repetition, such as 'slideshow', 'slideshow color', and 'slideshow image'.
- Use active voice.
- All buttons and actions must start with a verb.
- All technical specifications follow these formats:

| Technical specification | Format | Example |
| --- | --- | --- |
| Image size | \[numeral] x \[numeral]px (required/recommended) | 64 x 64px required |
| Image size | \[numeral]:\[numeral] aspect ratio (required/recommended) | 3:2 aspect ratio recommended |
| Image size with format | \[numeral] x \[numeral]px \[.format] (required/recommended) | 1200 x 300px .jpg recommended |
| Word / character count | \[numeral] words (max) | 32 words max |
| Text format | Use basic HTML to format text | |

#### Terminology requirements

Use the following Shopify terminology throughout your theme:

| Use this | Don't use this |
| --- | --- |
| **home page** | homepage |
| **top bar** | meta-nav, search bar |
| **bottom bar** | below footer, legal |
| **slideshow** | slider |
| **checkout** (when naming settings) | check out |
| **heading** | title |
| **subheading** | sub-heading |
| **body text** | main text |
| **signup** | sign-up, sign up |
| **favicon** | shortcut icon, website icon |
| **sidebar** | side bar |
| **button label** | button name |
| **social media** (when naming sections or settings) | social, social sharing |
| **social media icons** | social media buttons |
| **navigation** (to refer to all navigational elements) | menus, menu |
| **main menu** (to refer to primary navigational element) | navigation, menu |
| **secondary menu** (to refer to secondary navigational element) | navigation, menu |
| **footer menu** (to refer to a menu located in the footer) | navigation, menu |
| **cart type** (with "drawer", "page", and/or "modal" options) | Ajax, Ajaxify, Ajax cart |
| **.png** | PNG, png, .PNG |
| **use** (for actionable options that include a next step, such as uploading a file) | show, enable |
| **show** (for options that allow the merchant to show or hide a basic element) | use, enable |
| **enable** (for options related to apps or plugins, or something that will significantly modify the theme layout) | use, show |

#### Section name guidelines

Each section in a theme needs a name. Section names appear in the section picker and in the sidebar listing the sections in a template.

Section names should relate to the section's function, for example `Header`, `Product list`, `Slideshow`, or `Image gallery`.

Refer to [Shopify's theme terminology list](https://shopify.dev/docs/storefronts/themes/store/requirements#terminology-requirements) to make sure that you name sections using the right Shopify terms.

##### Suggested section names

- Header
- Featured products
- Featured collections
- Slideshow
- Image gallery
- Logo list
- Newsletter
- Map
- Blog posts
- Testimonials
- Footer

#### Section preset guidelines

Section presets are predefined configurations of sections that merchants start with when adding content.

Preset names should relate to the type of content in the preset, for example `Image and text`, `Map`, `Columns`, or `Blog articles`.

Refer to [Shopify's theme terminology list](https://shopify.dev/docs/storefronts/themes/store/requirements#terminology-requirements) to make sure that you name presets using the right Shopify terms.

##### Content placeholders

If your preset features images, videos, or icons, then you should display [placeholder content](https://www.shopify.com/ca/partners/blog/placeholder-images) so that the merchant can get a better idea of how the content looks before they add their own media.

In your presets, use the following content placeholders:

| Type of content | Placeholder |
| --- | --- |
| Images that aren't products or collections Adjacent images without margins | Image icon |
| Lists of logos | Logo icon |
| Slideshows Images with overlaid text Full-width images | Lifestyle image |
| Videos | [Default YouTube video ID](https://www.youtube.com/watch?v=_9VUPq3SxOc) |

---

### 15. Font picker

Font picker fields can be used to capture a font selection for various theme elements, such as the base heading font.

Font pickers must have the following settings:

- All fonts must use the setting type [font\_picker](https://shopify.dev/docs/themes/architecture/settings/input-settings#font_picker).
- A default font is loaded. For example, `default: work_sans_n6`.
- Fonts used in defaults and presets must use a currently [available font](https://shopify.dev/docs/storefronts/themes/architecture/settings/fonts#available-fonts).
- The CSS file loads bold, italic, and bold-italic variants for each font using the `font_modify` filter.
- Custom fonts aren't accepted.

Learn more about [setting fonts](https://shopify.dev/docs/storefronts/themes/architecture/settings/fonts).

---

### 16. Color system

Selecting the right foreground and background colors enhances the effectiveness of your theme.

- A minimum of 4 colors are required.
- All background color settings must include a corresponding foreground color setting.
- Color settings must use a `type` of `color`.

Learn more about [color system best practices](https://shopify.dev/docs/storefronts/themes/best-practices/design/color-system).

---

### 17. Responsive images

Responsive images are important to the user experience. With the shift to smaller devices, developers face new challenges to ensure that images load quickly, regardless of screen size.

All themes must meet the following image requirements:

- Images must adopt a responsive image strategy. Small images such as icons are an exception.
- Images must load only as they are needed to minimize the number of images loaded initially per page.

---

### 18. Naming themes and theme presets

Choose clear and unique names for your theme and presets when submitting to the Theme Store. Good names help merchants quickly identify and understand your theme.

#### Theme and preset naming requirements

- Theme and preset names must be distinct from Shopify products. You can't use the same name as, or similar to, Shopify products, events, or branded content. For example, don't name your theme Shopify, Unite, or Polaris.
- Theme and preset names must be distinct from company names. You can't include the name of your company or Shopify Partner account in your theme name. Your Partner account name is displayed automatically on the theme listing page.
- Theme and preset names must be distinct from websites, ecommerce platforms, and SEO-related benefits. For example, don't name your theme Performance, Mobile, or Sales.
- Theme and preset names must be distinct from industries and collections in the Theme Store. For example, don't name your theme Fashion, Electronics, or Jewelry.
- One theme preset must take the name of the parent theme.
- Theme and preset names must be 1-2 words.
- Theme and preset names must be less than 30 characters.
- Theme and preset names must be unique and distinct from existing themes in the Shopify Theme Store to avoid confusion or conflicts.

#### Theme and preset name guidelines

Use the following guidelines to help you choose the right name for your theme and presets:

- Summarize, or allude to, the purpose of the theme preset.
- Give the merchant an idea of what to expect when using the theme preset, the core ideas behind the preset, and the preset's target demographic.
- Use a noun for the name. Nouns are more suitable for creating product names that stick, have identity, and create a lasting impression. A noun can better define the focus of the theme, and offer a better understanding of the shopping experience being offered.
- Use a name that's easy to spell and pronounce. This will help merchants with recall and search.
- Work across different dialects. Since some words and phrases can have different meanings in different regions, you should consult with an idiom dictionary.
- Use a name that's different from theme names on different platforms.

#### Increasing clarity and discoverability

For clarity and discoverability, consider the following guidelines when naming your theme and preset:

- Don't use trendy names. Trends fade, and theme names should transcend trends.
- Don't use unusual spellings. Not only are unusual spellings more difficult to remember, but they're also more susceptible to autocorrect errors, and they limit discoverability by merchants.
- Don't use lengthy names. Even if you're trying to be descriptive, creating a long name can hurt a merchant's ability to remember what your theme is called.
- Don't use the same name as a theme on a different platform.
- Don't use the same name as an existing theme and preset name.

#### Adding presets to your theme zip submission

If you have more than one preset, you need to include a unique set of [templates](https://shopify.dev/docs/storefronts/themes/store/requirements#5-templates-sections-and-blocks) showcasing each preset. The contents of these templates should be similar to the [demo store](https://shopify.dev/docs/storefronts/themes/store/requirements#20-demo-stores) it is associated with.

Preset templates need to be included in a `/listings` folder in your theme zip. See the following example of a theme with two presets:

##### Shopify theme preset file structure

```text
.
├── assets
├── blocks
├── config
├── layout
├── locales
├── listings
    ├── preset-name-one
        └── templates
            └── *.json
        └── sections (optional)
            └── *.json
    └── another-preset-name
        └── templates
            └── *.json
        └── sections (optional)
            └── *.json
├── sections
├── snippets
└── templates
```

> **Note:** If you only have one preset, you do not need to include the `/listings` folder.

You can optionally include preset-specific [section groups](docs/storefronts/themes/architecture/section-groups) under a `/sections` folder under your preset listing folders. To learn more about how theme zips should be structured, refer to the [themes architecture documentation](https://shopify.dev/docs/storefronts/themes/architecture).

For a more detailed example of how to structure presets in your theme zip, refer to this [best practices page](docs/storefronts/themes/store/success/updates#best-practices-on-structuring-your-theme-zip).

#### Preset parity with demo store (install state)

- On install, the theme should match the demo store's look and expectations.
- If multiple presets are offered, then each preset's install state should mirror its demo.
- Layout and color/typography settings must match the demo.
- Use demo copy where appropriate. Adjust or remove copy that could cause support issues. We recommend that you use industry-specific copy, but this is optional.
- Demo imagery doesn't transfer on install.

---

### 19. Theme versions and release notes

Theme versions help merchants easily identify which theme they have, so that they can determine which features are available, or if there are more recent versions to update to.

When you submit your theme to the Shopify Theme Store, either for the first time or for an update, the theme needs to have a [version number](https://shopify.dev/docs/storefronts/themes/store/success/updates#versioning) and [release notes](https://shopify.dev/docs/storefronts/themes/store/success/updates#release-notes) that highlight the main features of the version.

---

### 20. Demo stores

Setting up a demo store is a great way to showcase your theme's features and functionality, and to provide merchants with real-world examples of how they can use your theme. A demo store that's beautifully designed and functions flawlessly lets merchants explore and interact with your theme, and helps them understand if your theme is right for them.

To build your demo store, create a [Client transfer store](https://help.shopify.com/en/partners/manage-clients-stores/client-transfer-stores/create-client-transfer-stores) from your Shopify Partner Dashboard.

> **Note:** Development stores with developer previews enabled can't be transferred.

#### Demo store requirements

- All theme presets must include at least one demo store.
- Each demo store must match the primary industry and catalog size that the theme preset is tagged to.
- Each theme preset install store must match the expectations set by the demo store.
- Each demo store has the [Bogus Gateway](https://help.shopify.com/manual/checkout-settings/test-orders#place-a-test-order-by-simulating-a-transaction) or Shopify Payments [test mode](https://help.shopify.com/manual/payments/shopify-payments/testing-shopify-payments#test-mode) enabled, and all other checkout options disabled.
- All demo store pages must use authentic text content. Don't use Lorem Ipsum or onboarding text. Don't include profanities.
- The [`powered_by_link`](https://shopify.dev/docs/api/liquid/objects/powered_by_link) link can't be altered and must contain only `powered_by_link`.
- Affiliate linking isn't allowed.
- Any link in the code that points to one of Shopify's domains must include a `rel="nofollow"` attribute.
- To avoid potential merchant confusion, demo stores can only showcase elements and functionality that are built into the theme. For example:
  - Don't use embedded text or buttons in images, except for the text on physical products, infographics, badges, or instagram images.
  - Don't use animated gif images in places where they can be mistaken for theme functionality.
  - Don't use apps. In some cases, special consideration applies to free product review apps and [free translation apps](https://apps.shopify.com/categories/store-design-internationalization). If you're showcasing multi-language options using translation apps, then all content must be translated.

- You must obtain the appropriate rights for all demo store assets in accordance with the [Shopify Partner Agreement](https://www.shopify.com/ca/partners/terms#:~:text=Each%20Theme%20Developer,any%20third%20party.). Before using any brand names, images, or content, permission must be directly granted by the brand owners.

If you're looking for a good source of royalty-free images, then try [Shopify Burst](https://burst.shopify.com/).

#### Demo store recommendations

When designing your demo store, consider the following recommendations to help you showcase the full potential of your theme. The following recommendations aren't mandatory requirements that need to be met for submission.

- Identify the source of any product images used in the product description.
- Use the latest version of your theme in your demo store.
- Incorporate built-in Shopify features to showcase the power and capabilities of your theme.
- Illustrate the versatility and variability of your theme, by including examples such as a product that's on sale, a sold-out product or variant, a product with multiple variants, and a gift card product.

---

### 21. Documentation and contact forms

Having clear, detailed, and accessible information about your theme helps merchants feel supported and helps to reduce support issues. Creating organized and effective documentation is important to your overall success as a Theme Partner.

#### Documentation and contact form requirements

- You must provide theme documentation and a public support contact form.
- You must have your theme documentation and contact form ready before launching your theme.
- You must link your documentation and contact form to your theme listing page in the Shopify Theme Store.

#### Merchant-facing theme documentation

- The copy for all theme documentation must be grammatically correct and free of spelling errors.
- The theme documentation must be consistent with the copy in the theme settings.

You need to keep your documentation up to date as changes occur within Shopify and you update your theme. As you support merchants using your theme, be sure to identify any gaps in your theme documentation and make updates as necessary.

Your theme documentation should include an FAQ section and any other relevant information that you feel could help address potential support questions that merchants might have.

##### Clear support policy

Consider specifying your support policy in your theme documentation. As a Theme Partner, you must [support bug fixes and answer any merchant questions regarding your theme](https://shopify.dev/docs/storefronts/themes/store/requirements#merchant-support-requirements). You might want to provide additional services to merchants such as customizations, app-integrations, and help with theme updates, but you can't include these services in the cost of your theme.

##### Clarity on custom two-column MDX tutorials

If you offer custom coding tutorials in your documentation, then specify whether the custom tutorials are supported. Also, include a warning to merchants in your tutorials that they should duplicate their theme before editing their code, and include a suggestion that merchants hire a [Shopify Partner](https://www.shopify.com/partners/directory) for help.

#### Contact forms

Your contact form lets merchants contact you. You should include your contact form in your theme documentation. If you use a modal for your contact form, then make sure that it's mobile friendly and linkable from the Theme Store. Try to avoid fields that ask merchants about budget, phone numbers, project type, or other unnecessary questions. You can have a form outlining your agency work on a separate page, but the contact form that you link to from the Theme Store should comply with the following guidelines.

| Field | Guideline |
| --- | --- |
| (First and Last) Name Field | |
| Email Address Field | |
| Store URL Field | Include an example URL for clarity, such as <http://www.storename.myshopify.com>. |
| Description of Problem Field | This should be a text-area field. |
| File Upload Function | Allow merchants to highlight their issues with images. |
| Auto-responder Function | The auto-responder is triggered when the contact form is submitted to reduce the amount of merchants contacting Shopify and Theme Partners asking if their support requests have been received. |
| Theme Name | Provide the theme name if you offer multiple themes. |
| Subject | If you include this field, then it should auto populate the email subject line. |

---

### 22. Supporting your theme

As a Theme Partner, you're responsible for supporting merchants who use your theme. Being merchant-focused, providing quality support, and having a collaborative attitude with Shopify is essential for the success of your theme.

Merchant support requests are submitted through your [contact form](#contact-forms), which you should link to from the Shopify Theme Store and your theme documentation.

#### Merchant support requirements

- You must assist merchants with their theme-related questions.
- You must reply to support requests from merchants within two business days.
- If there is a technical issue with your theme, such as a broken layout, a dead link, or a logical error, then you're responsible for fixing the issue in a timely manner.
- You must fix critical bugs immediately or your theme may be temporarily removed from the Theme Store.

##### Tips for improving the merchant installation experience

- Make sure your `.json` files don't include resources specific to your demo store admin (for example, custom metafields or URLs starting with `shopify://`).
- For `link_list` settings in the Header or Footer, always set a default value of `main-menu` or `footer`, depending on the location of the setting.
- When providing default values for resource-based settings (such as products), make sure the referenced resources exist in all stores.
- For `metaobject` and `metaobject_list` settings, only standard definitions can be used as the `metaobject_type`. Custom or app-owned definitions aren't supported.

#### Estimating the support workload

Being a Theme Partner is a full-time job, and supporting merchants who use your theme is a large part of that. All of our current Theme Partners have dedicated support teams working for them. If you become a Theme Partner, then you'll need to consider how to balance Theme Partner work with any other jobs that you're currently doing. New Theme Partners typically underestimate the amount of time that they'll need to allocate to support.

To understand how much effort is required to support a theme, Shopify merchants currently generate thousands of support tickets each month for the paid themes in the Shopify Theme Store, and support requests continue to grow as more merchants join the platform.

---

## Testing your theme for the Shopify Theme Store

> Fonte: https://shopify.dev/docs/storefronts/themes/store/test-theme

# Testing your theme for the Shopify Theme Store

To ensure that your theme contains the required Shopify features, and to ensure that it's flexible, resilient, and performant, you should test it before submission.

You should test the following:

- **Mandatory features**: Add Shopify Theme Store testing assets to your store, and then test your theme using the review checklist to verify that it contains the required features and responds to interactions and inputs as expected.

- **Performance**: Ensure that your theme meets Lighthouse performance standards using testing best practices.

- **Accessibility**: Ensure that your theme meets Lighthouse accessibility standards using testing best practices.

- **Browser compatibility**: Verify that your theme supports older browsers using tools like BrowserStack

You should also thoroughly review the Theme Store requirements before submission.

## Other testing tips

- When you're developing, use Theme Check to analyze and correct your Liquid Code.
- Test your performance and accessibility scores regularly using the Shopify Lighthouse CI GitHub Action.
- Disable JavaScript using Chrome DevTools to verify that navigation elements and the product form work without JavaScript.
- Consider testing your theme with people outside of your organization.

---

### Testing assets

> Fonte: https://shopify.dev/docs/storefronts/themes/store/test-theme/assets

# Testing assets

To test your theme, you need store data that enables you to test certain cases.

Shopify provides a few CSV datasets that help you to test these cases in your theme. [Import](https://help.shopify.com/manual/products/import-export/import-products) the following CSVs into your store:

- The [theme review team product CSV](https://shopify.dev/csv/theme-store-testing-shop-product-data.csv). This is the CSV that the theme review team uses to test your theme for acceptance to the theme store.

- The [performance test product CSV](https://shopify.dev/csv/theme-performance-shop-product-data.csv). This is the same CSV that you might use to run a Lighthouse audit. You should include this CSV so your store contains a large enough volume of products and collections for certain tests.

Some features require additional setup before they can be tested in your store.

---

## Additional setup

Due to the limitations of the CSV import process, you need to modify some product data and set up some features manually before you can test your theme:

- [Inventory quantities](#inventory-quantities)
- [Local pickup](#local-pickup)
- [Unit pricing](#unit-pricing)
- [Rich media](#rich-media)
- [Selling plans](#selling-plans)
- [Shop Pay Installments](#shop-pay-installments)

### Inventory quantities

If your test environment has multiple locations set up, then your store won't import product inventory quantities from CSV files. Instead, all product quantities default to zero.

Follow the steps below to configure inventory quantities for testing:

1. Adjust the inventory quantity on all products, except for **Bowtie (Rich Product Media)**. Leave this product as sold out. You should set up varying quantities for different product variants.

2. Update one product with two options so that each has a different quantity and availability. For example, you can use **Socks (two options)** and set some variants' quantities to zero, or use the following table as a reference. After setup, this product should have some sold out and unavailable variants.

| | S/M | M/L | Kids |
| - | - | - | - |
| Geometric | 0 | N/A | N/A |
| Hotdog | 4 | N/A | N/A |
| Dog | 3 | 10 | N/A |
| Cat | 5 | 0 | N/A |
| Plain white | N/A | 6 | N/A |
| Paw | N/A | N/A | 6 |

### Local pickup

To test the local pickup banner on your product page, you need to enable local pickup:

1. [Enable locations](https://help.shopify.com/en/manual/locations) in your store.

2. Add five or more locations.

3. Enable [local pickup](https://help.shopify.com/en/manual/shipping/setting-up-and-managing-your-shipping/local-methods) in your store.

4. Disable the local pickup option for one location.

5. Create a product with 5 variants, or use the **Enamel pin (1 option)** product.

6. Set up the quantity and availability for each variant:

   - Variant 1: available and in stock at all locations
   - Variant 2: available and in stock only in one location
   - Variant 3: available in two locations, sold out in one of the locations
   - Variant 4: available and in stock only in one location that doesn't offer pickup
   - Variant 5: sold out at all locations

### Unit pricing

To test unit pricing on your products, you need to change or override your store settings, and add unit prices to products:

1. Enable unit pricing in one of the following ways:

   - Set up a store located in the European Union (EU) or Switzerland. To test unit pricing in an existing store, you can change your store address to a valid address in your [store details](https://shopify.com/admin/settings/general).
   - Contact [Partner Support](https://partners.shopify.com/current/support/) to request a unit pricing beta flag for your test store. A beta flag bypasses store settings.

2. Add a product with multiple variants, or use any of the multi-variant products that you imported. [Set up different unit prices](https://help.shopify.com/manual/products/details/product-pricing/unit-pricing#add-unit-prices-to-your-product) for each variant.

### Rich media

CSV import doesn't support rich media. You need to add media to a product to test these features.

1. Use the **Bowtie (product rich media)** product and [add the following media](https://help.shopify.com/en/manual/products/product-media):

   1. Two 3D objects. You can use Shopify [sample models](https://help.shopify.com/zip/SampleModels.zip).
   2. One YouTube video
   3. One Vimeo video
   4. One MP4 video

2. Set all variants of this product to zero, so that you can preview the rich media on the collection page. Setting a quantity for the variant defaults the product card image to the variant image instead of the rich media.

### Selling plans

Selling plans can only be created and applied to products by an app. To test selling plan elements in your theme, you need to install a [subscription app](https://apps.shopify.com/collections/checkout-subscription) to verify that selling plans are appearing correctly on your theme.

### Shop pay installments

1. Enable Shop Pay Installments in one of the following ways:

   - Set up a store with a US address
   - Contact [Partner Support](https://partners.shopify.com/current/support/) to request a Shop Pay Installments beta flag for your test store. A beta flag bypasses store settings.

2. Add a product with multiple variants and varying prices, or use the **Socks (2 options)** product that you imported.

### Follow on Shop

Enable the Follow on Shop button in one of the following ways:

- Install the [Shop sales channel](https://apps.shopify.com/shop) and activate [Shopify Payments test mode](https://help.shopify.com/manual/payments/shopify-payments/testing-shopify-payments).
- Contact [Partner Support](https://partners.shopify.com/current/support/) to request a Follow on Shop beta flag for your test store. A beta flag bypasses store settings.

---

### Testing your theme for the Shopify Theme Store (checklist)

> Fonte: https://shopify.dev/docs/storefronts/themes/store/test-theme/checklist

# Testing your theme for the Shopify Theme Store

Use this checklist to ensure that your theme meets the functional requirements for the Shopify Theme Store. The checklist doesn't comprehensively represent all of the requirements for the Theme Store, but it can help you to make sure that your theme addresses edge cases that the theme review team will test as a part of the review process.

To run these tests, you need to populate your store with data, and configure some additional features. To download this data and learn about the additional configurations you need to make, refer to [Testing assets](https://shopify.dev/docs/storefronts/themes/store/test-theme/assets).

You should run these tests in both the theme editor and the storefront.

---

## 1. Home page

Add the following sections to the home page. After you add all of the sections, verify that they work properly.

- Three slideshows
- Five featured products, three of which are the same product
- Three different featured collections
- One collection list
- Three image with text
- One newsletter
- One rich text
- One blog post
- Two video (if applicable)
- Add additional sections until the homepage has 25 sections

---

## 2. Header

Run the following tests on your header. For each of these tests, verify the following:

- The store name or logo displays properly and is accessible
- Header icons or links display properly and are accessible
- The navigation functions properly, and navigation titles are fully visible

### Add logo fallback text:
- Long store name (30-40 characters, no spaces)

### Add a logo:
Test different aspect ratios in portrait and landscape mode:
- 16:9
- 4:3
- 3:2
- 1:1
- Transparent background on PNG image
- Logo scaling
- Different positions and alignments (if applicable)

### Add navigation:
- Long navigation menu (10+ menu items)
- Single-level navigation
- Two-level nested navigation
- Three-level nested navigation
- Long level one menu item titles (30-60 characters)
- Long level two menu item titles (30-60 characters)
- Long level three menu item titles (30-60 characters)
- Mega menu (if applicable)

---

## 3. Footer

Run the following tests on your footer. For each of these tests, verify that footer text, icons, images are fully visible and functional.

- Add five columns or blocks, or the maximum number of blocks
- Add multiple menus
- Add a long navigation menu (10+ menu items)
- Add menu items with long titles (30-60 characters)
- Add all social links
- If your footer has a newsletter form, then test the following:
  - Input form text
  - Submit the form
  - Test error detection and handling
  - Test the submission success message

---

## 4. Sections

Test the following sections in your theme:

- [Announcement bar](#announcement-bar)
- [Slideshow](#slideshow)
- [Featured product](#featured-product)
- [Featured collection](#featured-collection)
- [Collection list](#collection-list)
- [Image with text](#image-with-text)
- [Newsletter](#newsletter)
- [Rich text](#rich-text)
- [Blog posts](#blog-posts)
- [Video](#video)
- [Any sections unique to your theme](#unique-sections)

### Announcement bar

Run the following tests on your announcement bar section. For each of these tests, verify the following:

- Text and icons are fully visible
- Any links function properly
- Link styling indicates that the text is clickable

#### Text input:
- If the text input is plain text, then add 60-100 characters of text, or the maximum character limit
- If the text input is rich text, then add the following text:
  - Text with a single line break
  - Text with two line breaks
  - Text with three line breaks
  - A paragraph (40-50 words)

#### Add links:
- An internal link
- An external link
- Link opens in the same window
- Link opens in a new window

### Slideshow

Run the following tests on your slideshow section.

- Add three slideshow sections
- Add the maximum number of slides. If there's no limit, then add 10 slides.

#### Test the following image sizes:
- 2048px for retina displays
- 1024px for standard widescreen displays

#### Test the following aspect ratios using 72ppi, portrait, and landscape:
- 16:9
- 4:3
- 3:2
- 1:1

#### Additional elements:
- Add video (if applicable)

#### Add text:
- A heading
- A subheading (60 characters)
- A description
- If the text input is a plain single line text, then add 60-100 characters of text
- If the text input is rich text, then add the following text:
  - Text with a single line break (60-100 characters)
  - Text with two line breaks
  - Text with three line breaks
  - A paragraph (40-50 words)

#### Add links:
- An internal link
- An external link
- Link opens in the same window
- Link opens in a new window
- Link styling indicates that the text is clickable

#### Add button text:
- A single word label (30 characters, no spacing)
- A multiple word label (30 characters)

#### Add button links:
- Internal link
- External link
- Link opens in the same window
- Link opens in a new window

#### Test autoplay behavior:
- If multiple slideshows have autoplay enabled, then each slideshow autoplays as expected
- Slideshow controls work as expected when slideshow is on autoplay

### Featured product

Run the following tests on your featured product section. For each of these tests, verify the following:

- Adding duplicate featured products doesn't break the section or the page
- Customers can add different featured products to the cart

#### Tests:
- Add five featured product sections, three of which are the same product
- Select different variants for one of the duplicated products
- Add one of the duplicated products to the cart
- Perform tests from the [product page checklist](#product-page)

### Featured collection

Run the following tests on your featured collection section. For each of these tests, verify the following:

- All sections work as expected
- Adding multiple featured collections doesn't break the section or the page

#### Tests:
- Add three featured collection sections, using collections of varying sizes
- Perform tests from the [collection page checklist](#collection-page)

### Collection list

Run the following tests on your collection list section. For each of these tests, verify the following:

- Collection titles are visible
- Collections with no image display the first product in the collection, or the collection's title, in the image block
- Adding multiple collection list sections doesn't break the section or the page

#### Tests:
- Add the maximum number of collections. If there's no limit, then add 10 collections.
- Add a collection with a long title
- Add a collection with a single word title (30 characters, no spacing)
- Add a collection with a multi-word title (30 characters)
- Add collections where the collection images have different aspect ratios, in portrait and landscape orientations
  - 16:9
  - 4:3
  - 3:2
  - 1:1
- Add one collection with no featured collection image

### Image with text

Run the following tests on your image with text section. For each of these tests, verify the following:

- All text is completely visible
- Varying image qualities and ratios are supported
- Images must support varying image qualities and ratios
- Adding multiple image with text sections doesn't break the section or the page

#### Tests:
- Add three image with text sections

#### Add text:
- A heading
- A subheading (60 characters)
- A description
- If the text input is a plain single line text, then add 60-100 characters of text
- If the text input is rich text, then add the following text:
  - Text with a single line break (60-100 characters)
  - Text with two line breaks
  - Text with three line breaks
  - A paragraph (40-50 words)

#### Add links:
- An internal link
- An external link
- Link opens in the same window
- Link opens in a new window
- Link styling indicates that the text is clickable

#### Test the following image sizes:
- 2048px for retina displays
- 1024px for standard widescreen

#### Test the following aspect ratios using 72ppi, portrait, and landscape:
- 16:9
- 4:3
- 3:2
- 1:1

### Newsletter

Run the following tests on your newsletter section. For each of these tests, verify the following:

- All text is completely visible
- The form outputs proper error and success messages

#### Test the following parts of the newsletter form:
- Input form text
- Submit the form
- Test error detection and handling
- Test the submission success message

#### Add a description:
- If the text input is a plain single line text, then add 60-100 characters of text
- If the text input is rich text, then add the following text:
  - Text with a single line break (60-100 characters)
  - Text with two line breaks
  - Text with three line breaks
  - A paragraph (40-50 words)

#### Add links:
- An internal link
- An external link
- Link opens in the same window
- Link opens in a new window
- Link styling indicates that the text is clickable

### Rich text

Run the following tests on your rich text section. For each of these tests, verify that all of the text is visible.

- Add a heading
- Add a subheading (60 characters)
- Add a description
- Add multiple paragraphs (minimum 1000 characters)

#### Add links:
- Internal link
- An external link
- Link opens in the same window
- Link opens in a new window
- Link styling indicates that the text is clickable

### Blog posts

Run the following tests on your blog posts section. For each of these tests, verify the following:

- All text is visible
- The blog post grid supports varying image ratios

#### Tests:
- Add blog posts with different image aspect ratios:
  - 16:9
  - 4:3
  - 3:2
  - 1:1
- Add a blog post with a long title
- Add a blog post with a single word title (30 characters, no spacing)
- Add a blog post with a multi-word title (30 characters)

### Video

Add the following video types in a video section. For each of these tests, verify the following:

- Adding multiple video sections doesn't break section or the page
- Video controls are present and functional

#### Tests:
- Add a YouTube video
- Add a Vimeo video
- Add an MP4 video (if applicable)

### Unique sections

If your theme has any additional sections then you need to test them as well. Run the tests that apply to your section. Verify the following:

- Each section supports varying image qualities and ratios
- All text is visible
- Adding multiples of the same section doesn't break the section or the page

#### Tests:
- Add 2-3 instances of the same section

#### Add text:
- A heading
- A subheading (60 characters)
- A description
- If the text input is a plain single line text, then add 60-100 characters of text
- If the text input is rich text, then add the following text:
  - Text with a single line break (60-100 characters)
  - Text with two line breaks
  - Text with three line breaks
  - A paragraph (40-50 words)

#### Add links:
- An internal link
- An external link
- Link opens in the same window
- Link opens in a new window
- Link styling indicates that the text is clickable

#### Test the following image sizes:
- 2048px for retina displays
- 1024px for standard widescreen

#### Test the following aspect ratios using 72ppi, portrait, and landscape:
- 16:9
- 4:3
- 3:2
- 1:1

---

## 5. Pages

Test the following pages or elements in your theme:

- [Password page](#password-page)
- [Collection list page](#collection-list-page)
- [Collection page](#collection-page)
- [Product page](#product-page)
- [Blog page](#blog-page)
- [Blog post/article page](#blog-post-page-article)
- [Cart](#cart-page-modal-or-drawer)
- [Search page](#search-page)
- [Pages](#pages)
- [Page with a contact form](#pages-contact-form-template)
- [Gift card page](#gift-card-page)

### Password page

Run the following tests on your password page. For each of these tests, verify the following:

- Customers are able to access the store with a password
- The store logo or name and the password message are fully visible

#### Add logo fallback text:
- Long store name (30-40 characters, no spaces)
- Long store name with hyphens

#### Add a logo:
Test the following logo aspect ratios using portrait and landscape:
- 16:9
- 4:3
- 3:2
- 1:1
- Transparent background on PNG image
- Logo scales appropriately

#### Test the password form:
- Fill the email field
- Submit the form
- Test error detection and handling
- Test the submission success message

#### Add a password message (500+ characters)

#### Add different sized background images, if applicable:
- 2048px for retina displays
- 1024px for standard widescreen

Test the following aspect ratios using portrait and landscape:
- 16:9
- 4:3
- 3:2
- 1:1

### Collection list page

Run the following tests on your collection list page. For each of these tests, verify the following:

- Multiple collection image ratios are supported
- A collection with no image displays the first product in that collection, or displays the collection's title in the image block

#### Tests:
- Add a collection with a long title
- Add a collection with a single word title (30 characters, no spacing)
- Add a collection with a multi-word title (30 characters)

Test the following aspect ratios using portrait and landscape:
- 16:9
- 4:3
- 3:2
- 1:1

#### Additional tests:
- Add a collection with no featured collection image

### Collection page

Run the following tests on your collection page. For each of these tests, verify the following:

- All products in the collection are accessible
- The collection can be sorted and filtered
- Combining filter tags doesn't break the page
- Product information in the product grid is fully visible

#### Filter tests (if applicable):
- Test group filtering (if applicable)
- Add a single word tag (30 characters, no spacing)
- Add a long list of tags (20+ tags)

#### Pagination and display tests:
- Verify that only a limited number of products are displayed on initial load
- Test pagination (if applicable)
- Pagination truncates on a collection with five or more pages
- Test **View more** button (if applicable)
- Test infinite scrolling (if applicable)

#### Product information tests:
- Add a product title:
  - A single word title (30 characters, no spacing)
  - A multi-word title (30-60 characters)
- Add a product vendor:
  - A single word vendor (30 characters, no spacing)
  - A multi-word vendor (30-60 characters)

#### Image and variant tests:
- Test the way the grid responds to images of different aspect ratios, using portrait and landscape:
  - 16:9
  - 4:3
  - 3:2
  - 1:1
- If the collection page has an **Add to cart** button, verify that it's replaced or disabled when a sold out or unavailable variant is selected.
- Verify that the sold out message or badge is displayed when applicable.

### Product page

Run the following tests on your product page, on each of the product configurations outlined. For each of these tests, verify the following:

- Customers can add a selected variant to the cart
- Variant information changes dynamically when different variants are selected
- Customers are prevented from adding more than the available quantity of items to the cart

#### Product configurations:
- Single product (no variants)
- On sale product
- Product with one option
- Product with more than 1 option with different variant quantity inventories (out of stock variant, unavailable variant).
- Product with three options
- Product with 100 variants
- Product with no image
- Product with varying product media (image, video, 3D model, AR, MP4)
- Product with unit price

#### Tests:
- Add a product title:
  - A single word title (30 characters, no spacing)
  - A multi-word title (30-60 characters)

#### Dynamic variant updates:
Verify that when variants are selected from drop-down menus, product details are updated dynamically:
- Variant prices
- Variant media
- Variant SKU
- Action buttons (disable **Add to cart** and accelerated checkout buttons on sold out and unavailable variants)
- Variant selectors (cross out or disable sold out and unavailable variants)
- Unit price
- [Shop Pay Installments banner](https://shopify.dev/docs/storefronts/themes/store/test-theme/assets#shop-pay-installments)
- [Local pickup banner](#7-local-pickup)
- Inventory quantity (if applicable)

#### Product images:
- Product images
- No image
- Test the following aspect ratios using portrait and landscape:
  - 16:9
  - 4:3
  - 3:2
  - 1:1
- PNG image
- Image zoom (if applicable)
- Color swatches (if applicable)
- Option to disable swatches
- Clear instruction on how to upload custom swatches

#### Product description:
- Add multiple paragraphs (minimum 1000 characters)

#### Description links:
- Internal link
- External link
- Link opens in the same window
- Link opens in a new window
- Link styling indicates that the text is clickable

#### Description images:
- Add images (images must display as they appear in the rich text editor)

#### Cart validation:
- Verify that an error message appears when customers try to add more than the available quantity of items to the cart

### Blog page

Run the following tests on your blog page. For each of these tests, verify the following:

- All blog posts in the collection are accessible
- Multiple blog post image ratios are supported
- Must support varying blog post image ratios
- Blog post information must be visible. This includes the title, excerpt, author, date, and comment count
- If available, blog filtering works as expected and combining filter tags doesn't break the page

#### Image aspect ratio tests:
Test the way the grid responds to blog images of different aspect ratios, using portrait and landscape:
- 16:9
- 4:3
- 3:2
- 1:1

#### Blog filtering (if applicable):
- Filter by a single-word tag (30 characters, no spacing)
- Filter by a long list of tags (20+ tags)

#### Blog with many posts:
- Test pagination (if applicable)
- Verify that only five pages show on initial load
- Test the **View more** button (if applicable)
- Test infinite scrolling (if applicable)

### Blog post page (Article)

Run the following tests on your blog post page.

#### Add blog post content:
- Add multiple paragraphs (minimum 1000 characters)

#### Add links:
- Internal link
- External link
- Link opens in the same window
- Link opens in a new window
- Link styling indicates that the text is clickable

#### Add images:
- Add images (images must display as they appear in the rich text editor)

#### Add comments:
- Input comment text
- Submit the form
- Test error detection and handling
- Test the submission success message
- Verify that comments over a certain limit are paginated

#### Image aspect ratio tests:
Test the following blog post image aspect ratios using portrait and landscape:
- 16:9
- 4:3
- 3:2
- 1:1

### Cart page, modal, or drawer

Run the following tests on your cart. For each of these tests, verify the following:

- All products in the cart are fully visible
- The customer must be able to update the product quantity
- Automatic discounts must update dynamically

#### Tests:
- Add enough products to the cart to trigger scrolling
- Setting 0 for quantity should remove the product
- Verify that an error message appears when customers try to add more than the available quantity of items to the cart
- Automatic discount
- Cart notes

### Search page

Run the following tests on your search page. For each of these tests, verify that search result attributes are fully visible.

- Verify that the number of results displayed on first load is limited
- Test pagination (if applicable)
- Pagination truncates on search results with five or more pages
- Test the **View more** button (if applicable)
- Test infinite scrolling (if applicable)
- Test filtering (if applicable)
- Test both list and grid view (if applicable)
- Test error detection and handling, for example, when no results are found

### Pages

Run the following tests on a page that uses the generic page template. For each of these tests, verify that page content is fully visible.

#### Add a page title:
- A single word title (30 characters, no spacing)
- A multi-word title (30-60 characters)

#### Page content:
- Add multiple paragraphs (minimum 3000 characters)

#### Add links:
- Internal link
- External link
- Link opens in the same window
- Link opens in a new window
- Link styling indicates that the text is clickable

#### Add image:
- Add image—must display imagery as inputted in the RTE

#### Additional tests:
- Repeat testing for all existing product templates

### Pages (contact form template)

Run the following tests on a page that uses the contact form template. For each of these tests, verify that customers can send the merchant an email using the contact form.

- Input text
- Test mandatory fields, such as the message field
- Submit the form
- Test error detection and handling
- Test the submission success message

### Gift card page

Run the following tests on the gift card page. For each of these tests, verify that the gift card code and store name or logo is fully visible.

#### Add logo fallback text:
- Long store name (30-40 characters, no spaces)
- Long store name with hyphens

#### Add a logo:
Test the following logo aspect ratios using portrait and landscape:
- 16:9
- 4:3
- 3:2
- 1:1
- Transparent background on PNG image
- Logo scales appropriately
- Varying positions/alignments (if applicable)

#### Additional tests:
- Gift card code must not be cut off

---

## 6. Link sharing

Share a link to the store where you're testing your theme on various social media platforms. Verify that the sharing image appears. You can use tools like the [Facebook sharing debugger](https://developers.facebook.com/tools/debug/) and the [Twitter card validator](https://cards-dev.twitter.com/validator) to perform this test.

---

## 7. Local pickup

Test your local pickup banner in the following scenarios. Before you start, [prepare your store to test local pickup](https://shopify.dev/docs/storefronts/themes/store/test-theme/assets).

### Variant 1 - available for pickup at five locations:

- Verify that the pickup banner appears
- When you click **Check availability at other stores**, verify that all locations are visible, and that you can scroll to see all location information

### Variant 2 - available for pickup at only one location:

- Verify that the pickup banner appears
- Verify that the **Check availability at other stores** text is updated to **View store information**

### Variant 3 - available for pickup at only two locations, and sold out one of those locations:

- Verify that the pickup banner appears, and indicates that the item is available or unavailable at one of the locations.
- Verify that the **Check availability at other stores** link is present
- Verify that clicking on **Check availability at other stores** brings up only two locations

### Variant 4 - only available at a location that doesn't offer pickup:

- Verify that the pickup banner is removed

### Variant 5 - sold out at all locations:

- Verify that the pickup banner is removed
- Verify that the **Add to cart** button is changed to **Sold out**

### General tests:

- Ensure the pickup banner changes dynamically when a new variant is selected

---

## 8. Unit pricing

Test unit prices in your theme. Before you start, [prepare your store to test unit pricing](https://shopify.dev/docs/storefronts/themes/store/test-theme/assets).

- Verify that unit prices change dynamically on variant change
- Verify that unit prices appear in the following locations:
  - Product page
  - Collection page product cards
  - Cart drawer, page, or popup
  - Customer order page

---

## 9. Rich media

Test rich media in your theme. Before you start, [prepare your store to test rich media](https://shopify.dev/docs/storefronts/themes/store/test-theme/assets).

### Verify 3D/AR behavior:

- Verify that you can view and move 3d models on desktop and mobile devices
- Verify that the **View in your space** button appears on mobile devices
- Verify that can view both AR objects on mobile devices

### Verify video behavior (YouTube, Vimeo, MP4):

- Verify that video controls are accessible
- Verify that you can mute and unmute videos
- Verify that you can play and pause videos
- Verify that variant display when the associated variant is selected

### Verify that rich media types don't break the product card layout of the collection page:

- YouTube
- Vimeo
- MP4
- 3D models

---

## 10. Selling plans

Test selling plans in your theme. Before you start, [prepare your store to test selling plans](https://shopify.dev/docs/storefronts/themes/store/test-theme/assets).

- Applied selling plans appear on the cart page
- Applied selling plans appear on the customer order page

---

## Review process

> Fonte: https://shopify.dev/docs/storefronts/themes/store/review-process

# Review process

When you're ready to share your theme, learn about our review process and how to submit your theme to the Shopify Theme Store.

Set up a Theme Store listing so that merchants can understand the full potential of your theme.

---

### Submitting a theme to the Shopify Theme Store

> Fonte: https://shopify.dev/docs/storefronts/themes/store/review-process/submit-theme

# Submitting a theme to the Shopify Theme Store

When you submit a theme to the Shopify Theme Store, Shopify's theme review team reviews your theme to ensure that it meets the [Theme Store requirements](https://shopify.dev/docs/storefronts/themes/store/requirements). If your theme meets the requirements, it's considered for approval.

---

## Theme review process

The theme review process consists of 5 stages. Your theme must meet all requirements in each stage to advance to the next stage.

### Stage 1: Theme features and Online Store 2.0 (OS 2.0) compatibility

- [Features](https://shopify.dev/docs/storefronts/themes/store/requirements#features)
- [OS 2.0](https://shopify.dev/docs/storefronts/themes/best-practices/version-control) compatibility in the theme's [templates, sections, and blocks](https://shopify.dev/docs/storefronts/themes/store/requirements#templates)

### Stage 2: Lighthouse performance and accessibility

- [Lighthouse performance and accessibility requirements](https://shopify.dev/docs/storefronts/themes/store/requirements#lighthouse-performance-and-accessibility-requirements)

### Stage 3: Technical requirements

- [Pages](https://shopify.dev/docs/storefronts/themes/store/requirements#pages)
- [Consistency and functionality](https://shopify.dev/docs/storefronts/themes/store/requirements#8-consistency-and-functionality)
- [Browser compatibility](https://shopify.dev/docs/storefronts/themes/store/requirements#9-browser-compatibility)
- [Assets](https://shopify.dev/docs/storefronts/themes/store/requirements#10-assets)
- [Search engine optimization (SEO)](https://shopify.dev/docs/storefronts/themes/store/requirements#11-search-engine-optimization-seo)
- [Accessibility](https://shopify.dev/docs/storefronts/themes/store/requirements#12-accessibility)
- [Social media](https://shopify.dev/docs/storefronts/themes/store/requirements#13-social-media)

During the first three stages, the theme review team might identify design and UX issues or provide suggestions around design or UX. However, this feedback isn't a complete design and UX review. The team provides in-depth feedback in stage 4.

### Stage 4: Design and UX

- [Theme design and UX](https://shopify.dev/docs/storefronts/themes/store/requirements#3-theme-design-and-ux)
- [Settings](https://shopify.dev/docs/storefronts/themes/store/requirements#14-settings)
- [Font picker](https://shopify.dev/docs/storefronts/themes/store/requirements#15-font-picker)
- [The color system](https://shopify.dev/docs/storefronts/themes/store/requirements#16-color-system)
- [Responsive images](https://shopify.dev/docs/storefronts/themes/store/requirements#17-responsive-images)

### Stage 5: Pre-launch checks

- [Theme store exclusivity](https://shopify.dev/docs/storefronts/themes/store/requirements#1-theme-store-exclusivity)
- [Naming themes and theme styles](https://shopify.dev/docs/storefronts/themes/store/requirements#18-naming-themes-and-theme-presets)
- [Demo stores](https://shopify.dev/docs/storefronts/themes/store/requirements#20-demo-stores)
- [Documentation and contact forms](https://shopify.dev/docs/storefronts/themes/store/requirements#21-documentation-and-contact-forms)
- [Supporting your theme](https://shopify.dev/docs/storefronts/themes/store/requirements#22-supporting-your-theme)

---

## Submit your theme for review

1. Log in to your [Partner Dashboard](https://app.shopify.com/services/partners/auth/login).
2. In the sidebar navigation, click **Themes**.
3. Click **Submit a theme**.
4. Add your theme ZIP file.
5. Select the check box to acknowledge that you have read and agree to the [Shopify Partner Agreement](https://www.shopify.com/partners/terms).
6. Click **Upload file**.
7. On the **Theme submission form**, enter the listing information for your theme and theme presets that will be published to the Shopify Theme Store. Learn more about the [Theme Listing page](https://shopify.dev/docs/storefronts/themes/store/review-process/listings).
8. Click **Submit**.

---

## What to expect from Shopify when you submit your theme

After you submit your theme for review, Shopify's theme review team tests your theme to ensure that it meets [Shopify's Theme Store requirements](https://shopify.dev/docs/storefronts/themes/store/requirements) before your theme can be approved.

The Shopify theme review team might also access the Shopify admin of your demo store as part of the theme review process.

If your theme submission doesn't meet the requirements, your theme is rejected and you're notified by email. If your theme requires minor changes for approval, you receive an email with a list of required changes. The email outlines areas of the theme that require attention before continuing through the review process. You have the opportunity to discuss the feedback with the theme review team by replying to the email.

> **Caution:** If you resubmit your theme without addressing the reasons why it was rejected, you could be temporarily suspended from submitting themes to the Shopify Theme Store.

After the theme review team has fully reviewed your theme and ensured that it meets all Shopify requirements, you can list your theme on the Shopify Theme Store.

> **Note:** When a theme is submitted for review, we expect that the theme has been built following our requirements and has been fully tested for issues and bugs.

---

## Contact throughout the review process

During the review process, Shopify contacts you at the email specified in the **Theme submission contact email** field when you completed your theme listing. To ensure you receive emails from Shopify, add `themes@shopify.com` and `noreply@shopify.com` to your allowed senders list in your email service provider's settings.

---

## Changing your theme during review

After you submit your theme for review, you can still submit changes to your theme as long as the theme review team hasn't initiated the review. To submit changes to your theme, do the following:

1. Log in to your [Partner Dashboard](https://app.shopify.com/services/partners/auth/login).
2. In the sidebar navigation, click **Themes**.
3. Click the theme that you want to update.
4. Click **Upload new zip** and upload the changed version of your theme.

> **Note:** You'll receive an email notification immediately after your submission. However, it can take up to 24 hours for submission details to be reflected in your Partner Dashboard.

After the theme review team initiates a review, you won't be able to make changes until the review has been completed and the assessment is sent to you.

---

### Theme Store listing page

> Fonte: https://shopify.dev/docs/storefronts/themes/store/review-process/listings

# Theme Store listing page

Follow these guidelines for submitting your theme to the Shopify Theme Store and filling out your preset listing pages.

---

## Theme zip file

The first step to submitting your theme is uploading the theme ZIP file. Be sure to test your theme on your development store before you submit it to the Theme Store.

If you use a CLI tool, you can package the zip file using the [Shopify CLI](https://shopify.dev/docs/api/shopify-cli/theme) with the following command:

### Terminal

```terminal
shopify theme package
```

A ZIP validator assesses the contents of your .zip file, including the following:

- the name of the theme as specified, in the `theme_name` attribute the `settings_schema.json`
- the name and number of the presets included in your theme

You can't change the theme or preset name after uploading, so ensure that you follow the [naming guidelines](https://shopify.dev/docs/storefronts/themes/store/requirements#naming-themes).

---

## Presets and demo stores

### Presets

A separate listing form is generated for each preset that's included in your theme ZIP file. Each theme preset requires its own individual Theme Store listing page and must be tailored to a specific merchant segment to meet their unique needs.

### Demo store url

For each preset, provide a link to a complete and fully functioning demo store that uses that preset. Ensure that your demo stores meet Shopify's [demo store requirements](https://shopify.dev/docs/storefronts/themes/store/requirements#demo-stores) before linking.

### Demo store screenshots

For each demo store, provide one mobile and one desktop screenshot of the home page.

Screenshot requirements:

- Desktop screenshot dimensions must be 1000px by 1248px or 2000px by 2496px.
- Mobile screenshot dimensions must be 750px by 1334px.
- Provide alt text for all images for accessibility and to improve SEO.
- Don't include desktop backgrounds, added text, and browser windows in your screenshots. Crop them so that your images aren't cluttered and don't distract merchants from your theme.
- Your mobile screenshots can't be duplicates of your desktop screenshots.

### Theme preset tagline

This is a one-line advertisement for your theme preset, using 70 characters or less. Taglines should be short, succinct, and they should sum up what makes your theme preset unique. Effective approaches to writing theme taglines are:

- Identify the unique purpose of the theme preset. For example, "Designed for your crowdfunding campaign" or "Tailor-made for modern apparel stores".
- Describe the style and benefit of the theme preset. For example, "A minimalist theme that puts your photography front and center" or "An editorial-inspired design that's perfect for publishers".
- Avoid using the tagline to describe specific theme features.
- Avoid using technical words that might not be clear.
- Avoid overt uses of marketing language such as "world's best", or overusing adjectives such as "stunning" or "amazing".

### Industry

Choose the primary industry that your preset works best for. Demo store images should also represent the industry you select. This helps merchants set up quickly with minimal customization.

Industry tags are used for filters, search, and recommendations for merchants.

The following is the list of industries that you can select from for this field.

| Industry | Definition |
| - | - |
| Art | Artwork, photography, digital prints, art supplies, etc. |
| Auto | Cars, motorcycles, ATVs, vehicle parts, etc. |
| Bags | Backpacks, purses, luggage, wallets, etc. |
| Beauty | Skincare, makeup, hair, perfume, cosmetics, etc. |
| Clothing | Tshirts, hoodies, fashion, apparel, etc. |
| Electronics | Cameras, computers, headphones, phone accessories, etc. |
| Entertainment | Books, music, videos, podcasts, gaming, etc. |
| Food and drink | Food, beverages, restaurants, grocery, meal kits, etc. |
| Garden | Plants, plant pots, seeds, garden tools, etc. |
| Hardware | Tools, industrial equipment, building materials, electrical supplies, etc. |
| Home | Furniture, home decor, home appliances, dinnerware, etc. |
| Jewelry and accessories | Necklaces, watches, bracelets, belts, hats, etc. |
| Kids | Kids clothing, baby items, strollers, etc. |
| Office | Office supplies, stationery, work desks, etc. |
| Pets | Pet food, pet toys, pet accessories, etc. |
| Services | Classes, workshops, virtual appointments, etc. |
| Shoes | Sneakers, boots, dress shoes, sandals, etc. |
| Sports | Sports equipment, fitness, camping, recreation, etc. |
| Toys | Puzzles, dolls, plushies, wooden blocks, etc. |
| Wellness | Supplements, medicine, health, first aid, etc. |

### Catalog size

While presets can be customized for multiple catalog sizes, select the one best suited to the purpose of the preset. Catalog size tags are used for filters, search, and recommendations for merchants.

The following is the list of catalog sizes that you can select from for this field.

| Catalog size |
| - |
| 1 product |
| Few (2-10) |
| Some (11-100+) |
| Lots (500+) |

---

## Key highlights

Include three highlights that differentiate your theme preset for merchants. Your first highlight can be a video or a still image.

**Video guidelines:**

- Use videos to help showcase interactive or animated aspects of the theme preset, or versatility in theme setup that can't be expressed in screenshots.

- Don't use video for onboarding or tutorials. Save those for your theme documentation.

- Recommended length of a video is 2 minutes or less.

- Don't use the Shopify logo or name in your video.

- The video must be hosted on YouTube. You can [turn off comments](https://support.google.com/youtube/answer/9482556) and [set your video to unlisted](https://support.google.com/youtubecreatorstudio/answer/6302665) to prevent unwanted monetization or replies.

- You need to provide the embed URL for the video, for example, `https://www.youtube.com/embed/<video ID>`.

  To find the embed URL:

  - Click the **Share** tab of your YouTube video.
  - Click **Embed**.
  - Copy the `src` attribute from the iframe tag.

**Static image guidelines:**

- Provide a title (maximum 30 characters) and description (maximum 140 characters).
- Don't use the Shopify logo or name in your images.
- Image dimensions must be 1600px by 1200px.
- Don't use animated gif images.

---

## SEO and tracking

Get data on visits to your page.

---

## SEO

### Metadata description

The metadata description is used by external search, and is shown in search engine results and link previews. Include keywords that are relevant to your theme to help with SEO, but ensure that your description is still readable. Use grammatical sentences rather than a string of keywords.

---

## Tracking IDs

### Google analytics code

To track page views for your theme preset listing using Google Analytics 4, enter your measurement ID. Learn more about [tracking your listing traffic](https://support.google.com/analytics/answer/9304153).

#### Full-funnel theme install attributions

To provide full details of the theme installation funnel, the Shopify Theme Store uses [Google Analytics 4's Measurement Protocol](https://developers.google.com/analytics/devguides/collection/protocol/ga4) for server-side events, on theme installation on purchase. To receive these events, you must use Google Analytics 4 with your theme listing, and have entered an API secret generated in the Google Analytics UI.

The following events are sent to Google Analytics and display in the real-time view. However, event parameters might take up to 24 hours to propagate and need to be added as an [event-scoped custom dimension](https://support.google.com/analytics/answer/10075209?hl=en#zippy=%2Ccreate-an-event-scoped-custom-dimension%2Ccreate-a-custom-metric%2Canalyze-an-event-scoped-custom-dimension).

| Event name | Parameters | Description |
| - | - | - |
| `shopify_theme_install` | * `shop_id`<br>* `theme_handle`<br>* `preset_handle`<br>* `shop_name`<br>* `shop_url` | Sent when a merchant finishes purchasing and installing a theme |

To generate an API secret:

1. Log into [Google Analytics](https://analytics.google.com/analytics/web/#/).
2. Click the **Admin** icon in the bottom left corner.
3. Click **Data Streams** under **Property settings**.
4. Select the measurement stream that corresponds to the **Measurement ID** which you've added to your app listing.
5. Click **Measurement Protocol API secrets**.
6. Click **Create** to generate a new API secret.

To add the API secret to your app listing:

1. Log in to your [Partner Dashboard](https://partners.shopify.com/organizations).
2. Click **Themes**.
3. Click the name of your app.
4. Click **Edit Theme**.
5. In the **SEO and tracking** section for each preset, enter your Google Analytics 4 measurement ID.
6. Enter your API secret.
7. Click **Save** to save the changes as a draft.
8. Click **Publish changes** to publish the changes.

### Google e-commerce events

To enhance tracking for e-commerce related interactions, the following events have been implemented:

| Event name | Parameters | Description |
| - | - | - |
| [`view_item`](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?sjid=2649380085872637034-NC\&client_type=gtag#view_item) | * `currency`<br>* `value`<br>* `items`<br>* `item_id`<br>* `item_name`<br>* `price`<br>* `quantity` | Sent when a merchant views a theme's details page |
| [`add_to_cart`](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?sjid=2649380085872637034-NC\&client_type=gtag#add_to_cart) | * `currency`<br>* `value`<br>* `items`<br>* `item_id`<br>* `item_name`<br>* `price`<br>* `quantity` | Sent when a merchant clicks the **Try theme** button |

### Google remarketing code

To add Google remarketing code to your theme preset listing, enter the number that follows `var google_conversion_id =` in the remarketing tag that you received from Google. We don't currently support specific tag remarketing lists. Learn about [Google remarketing](https://support.google.com/google-ads/answer/2453998).

### Facebook pixel ID

To add Facebook Pixel tracking to your theme preset listing, enter the ID number for your theme from the Facebook Event Manager. Learn about [Facebook pixels](https://www.facebook.com/business/help/952192354843755?id=1205376682832142).

### Meta Pixel events

To enhance tracking for e-commerce related interactions, the following events have been implemented:

| Event name | Parameters | Description |
| - | - | - |
| `ViewContent` | * `content_ids`<br>* `content_name`<br>* `currency`<br>* `value` | Sent when a merchant views a theme's details page |
| `AddToCart` | * `content_ids`<br>* `content_name`<br>* `currency`<br>* `value` | Sent when a merchant clicks the **Try theme** button |

---

## Theme price and value proposition

### Theme price

You can price your theme from $100 USD to $500 USD in increments of $10. Gage the amount of settings, level of design, size of the catalog it's built for, and the amount of development it took to build your theme, and then price your theme accordingly. Make sure to include the cost of providing high quality support when considering how to price your theme. You'll be expected to provide bug fixes and to answer questions about your theme. The quality of support you provide can affect how merchants rate your theme.

---

## Theme features

### Features

Select the features that your theme supports without needing additional code. Having features that are associated with a particular industry or business type helps your theme rank higher in relevant categories and recommendations for merchants. However, to make setup easier for merchants, your theme should only contain the features that are most useful to your target merchant segment.

| Category | Feature tag | Description |
| - | - | - |
| **Merchandising** | | |
| Image display | high resolution images | Theme is optimized for high quality, large images |
| | image galleries | Display multiple images at once in a thumbnail grid or tiled mosaic-style layouts |
| | image hotspot | Tag images with interactive hotspots for popups or additional information |
| | image rollover | Show different images or info when hovering over an image |
| | image zoom | Allow close-up view of images |
| | lookbooks | Display a portfolio of images that feature a product line or collection |
| | slideshow | Display multiple images one at a time in a carousel |
| Product details | color swatches | Display color options for a product on the product page |
| | ingredients/nutritional information | Show an ingredients list or nutritional information for a product |
| | product options | Show available product options such as finishes, brands, or colours on collection pages |
| | product tabs | Present product details across multiple tabs or sheets on the product page |
| | product videos | Include a video on the product page |
| | shipping/delivery information | Show information such as shipping options and estimated delivery time |
| | size chart | Display a size chart for products |
| | usage information | Show usage information for a product |
| Visual effects | animation | Include animations, such as page transitions, scrolling, or animated cart actions |
| **Marketing and conversion** | | |
| Conversion optimization | cross-selling (complete the look) | Show products commonly purchased together |
| | quick view | View product details in a popup without leaving the current page |
| | recently viewed | Show products that a visitor has recently looked at |
| | recommended products | Show products based on customer behavior or past purchases |
| | stock counter | Show current stock levels for a product |
| | store locator | Provide map or direction to physical location |
| Email capture | back-in-stock alert | Prompt to collect email info for notifying when product is back in stock |
| | customizable contact form | Create a custom contact form with additional fields and content |
| Promotional content | blogs | Use advanced blogging features such as surfacing blog posts on product and collection pages, or support for muliple blogs and reader comments |
| | event calendar | Show a feed or calendar of upcoming events |
| | in-menu promos | Embed images and promotional content into your navigation |
| | press coverage | Highlight media coverage and press mentions |
| | product badges | Add stickers or labels to product images to highlight sales, new items, top sellers, or other product features |
| | promo banners | Add a banner announcing sales, discounts, or events |
| | promo popups | Add a popup announcing sales, discounts, or events |
| | promo tiles | Add custom promo elements alongside product images |
| Trust/social proof | age verifier | Require age verfication before purchase or entering the site |
| | FAQ page | Provide an FAQ page to answer visitor questions about anything from returns to shipping |
| | product reviews | Automatically integrate with Shopify Product reviews app and display reviews on product pages |
| | trust badges | Display badges indicating secure payment and checkout |
| **Cart and checkout optimization** | | |
| Carts and checkout | cart notes | Allow customers to add notes to their order |
| | gift wrapping | Allow customers to select gift wrapping as part of their order |
| | in-store pickups | Allow customers to select a local pickup option instead of delivery |
| | quick buy | Allow customers to add products to the cart without leaving the page |
| | slide-out cart | Make cart accessible from any page |
| | sticky cart | Keep add to cart button visible as customers browse and scroll |
| **Product discovery** | | |
| Navigation and filtering | back-to-top button | Provide a button that takes customers to the top of the page. |
| | breadcrumbs | Show a set of links that tells the customer where they are in the site and allows them to return to a previous page |
| | collection page navigation | Provide navigation menu or sidebar links on collection pages |
| | enhanced search | Enable predictive or smart searching |
| | infinite scroll | Continuously load content at the bottom of a page so that customers don't have to click to the next page |
| | mega menu | Configure menu navigation that provides multi-column drop-down navigation |
| | product filtering and sorting | Allow customers to filter products on the collection page by features such as size, color, or brand |
| | sticky header | Provide a header that's visible in the same position as customers scroll down a page |
| Product highlights | recently viewed | Allow customers to see a set of products that they recently viewed |
| | recommended products | Provide a set of recommended products that are associated with the product page or collection that a customer is currently looking at |

### Merchant stores using your theme

After your theme is published and you've made some sales, then you can optionally provide URLs and screenshots of some of the shops that use your theme, up to a maximum of five stores. These examples can help showcase your theme in use.

Make sure that you have permission to feature these stores on your listing. Make sure to check on these stores occasionally, as stores can change or become inactive over time.

Screenshot guidelines:

- Image dimensions must be 779px by 1000px.

The following types of stores can't be used to showcase samples of your theme:

- adult product stores
- stores with violent or hateful content
- stores selling restricted substances
- any stores that don't meet our [Terms of Service](https://www.shopify.ca/legal/terms-payments-us) standards

---

## Merchant support

### Contact and documentation

You're required to provide a way for merchants to get help through a [contact form](https://shopify.dev/docs/storefronts/themes/store/requirements#documentation-and-contact-forms), as well as provide a link to the [documentation for your theme](https://shopify.dev/docs/storefronts/themes/store/requirements#documentation-and-contact-forms). We encourage partners to have a CRM software such as a help desk set up to help manage merchant tickets. A contact email address isn't sufficient for the long term. See [Supporting your theme](https://shopify.dev/docs/storefronts/themes/store/requirements#supporting-your-theme) for more details about how to successfully support merchants.

### Merchant review notifications

Provide an email address to notify you when a merchant reviews your theme, or when existing reviews are updated or deleted.

---

## Submission notes

### Theme submission contact

Provide a contact email address for the review team to communicate with you about your theme submission. If no contact email is provided, then the business email for your partner account is used. To prevent our email messages from being caught in spam filters, add `theme-submissions@shopify.com` and `noreply@shopify.com` to your email provider's allowed address list.

### Demo store testing

**Testing instructions:** Provide instructions for testing your theme. Include any special setup that's required, such as admin settings. Provide instructions on how to find the main features of your theme.

**Password for demo stores:** All demo stores must use the same password. Share your password for the demo stores so that reviewers can easily see and test the theme customization settings.

### Theme review notes

Provide details about your theme and development experience. Describe the type of merchant that your theme is built for, and how the features of this theme help merchants to be successful in engaging and converting customers. Tell us about your experience with developing themes. This information isn't shown directly to merchants, but helps our reviewers understand your goals for the theme, and it helps our operations team curate themes for collections and recommendations for specific merchant segments.

---

## Being successful in the Shopify Theme Store

> Fonte: https://shopify.dev/docs/storefronts/themes/store/success

# Being successful in the Shopify Theme Store

After your theme is approved, you can market and support your theme to make it more successful. By default, approved themes are listed on the Shopify Theme Store. By being successful on the Shopify Theme Store, you can get even more merchants to use your theme, and you can promote and grow your business. To get started, use the following resources:

- [Prohibited actions](https://shopify.dev/docs/storefronts/themes/store/success/prohibited-actions) - To keep your theme on the Shopify Theme Store, make sure you don't engage in these prohibited actions.

- [Managing theme reviews](https://shopify.dev/docs/storefronts/themes/store/success/managing-theme-reviews) - Merchants can review your theme in the Shopify Theme Store. Learn how to get feedback and work with negative reviews.

- [Marketing your theme using the Shopify Theme Store ad badge](https://shopify.dev/docs/storefronts/themes/store/success/brand-assets) - You can increase merchant confidence in your theme by using the official Shopify Theme Store Ad Badge on your ads and digital properties such as your website.

- [Updating your theme](https://shopify.dev/docs/storefronts/themes/store/success/updates) - Provide iterative updates to your theme to support merchants and demonstrate your commitment to quality and innovation.

- [Removing your theme](https://shopify.dev/docs/storefronts/themes/store/success/remove-theme) - If you want to remove a theme from the Shopify Theme Store, then you need to follow these steps.

> **Note:** You can't transfer a theme between Partner accounts.

---

### Prohibited actions on the Shopify Theme Store

> Fonte: https://shopify.dev/docs/storefronts/themes/store/success/prohibited-actions

# Prohibited actions on the Shopify Theme Store

We value our theme partners and want to make the theme experience the best possible for everyone involved. Theme partners are expected to adhere to the [Partner Program Agreement](https://www.shopify.com/partners/terms).

This page outlines some of the actions that could lead to your theme being removed from the Shopify Theme Store, or to you being removed from the Shopify Partner program. While this page presents a series of important guidelines, it's not intended to be comprehensive.

If you violate any of the terms in the Partner Program Agreement, then the Shopify Theme Store team will use their discretion to determine the appropriate disciplinary action, which can include the following:

- an email requiring your prompt attention with a set time frame to take action
- immediate removal of your theme from the Shopify Theme Store
- removal from the Shopify Partners program

The terms can change at any time without notice. Any other behavior that the Shopify Theme Store team deems unacceptable, objectionable, or harmful can also result in the theme being removed from the Shopify Theme Store.

---

## Merchant experience

- Continuous failure to respond to merchant support requests. The requirements for support can be found in Supporting your theme.
- Selling or abusing merchant data (section C-2 of the [Partner Program Agreement](https://www.shopify.com/partners/terms)).
- Failing to provide consistent service, themes can experience critical errors resulting in support debt.
- Failing to provide enough notice before you remove your theme from the Shopify Theme Store. Refer to the guidelines for [removing your theme from the Theme Store](https://shopify.dev/docs/storefronts/themes/store/success/remove-theme).
- Reviews that don't comply with section C-1 of the [Partner Program Agreement](https://www.shopify.com/partners/terms). This includes fake or misleading reviews, and review incentivization. Refer to [Managing theme reviews](https://shopify.dev/docs/storefronts/themes/store/success/managing-theme-reviews) for best practices.

---

## Unsolicited marketing

- No spam, illegal, or invasive marketing tactics (A-2). Emails, and SMS or text messages, should only be sent to merchants who have your theme actively installed or have clearly opted-in to your marketing communications.
- No affiliate links in your theme listing page, or within any links in the theme files.

---

## Requirement violations

- Modifying your theme or theme listing after publication, which results in the theme no longer meeting the Shopify theme requirements.
- Fatal errors resulting in the theme failing to install from the Shopify Theme Store.
- Copyright infringement or leveraging the code base of a third-party theme for theme builds.
- Selling or distributing listed themes outside of the Shopify Theme Store. Themes listed on the Shopify Theme Store can only be distributed through the Shopify Theme Store.

---

## Reporting violations

If you encounter a theme that doesn't adhere to the [Partner Program Agreement](https://www.shopify.com/partners/terms), then you can report it directly by filling out the [Report a Partner violation form](https://www.shopify.com/legal/tools/report-an-issue/report-a-partner-violation).

---

### Managing theme reviews

> Fonte: https://shopify.dev/docs/storefronts/themes/store/success/managing-theme-reviews

# Managing theme reviews

After a merchant installs your theme on their store, they can publish a review. Positive reviews can encourage other merchants to install and use your theme.

When a merchant leaves a review for your theme, they choose a rating of **I love it!**, **Neutral**, or **I'm not happy**, and they can also enter a comment. You will receive an email notification each time your theme is reviewed or a review is updated.

> **Caution:** Reviews that don't comply with Shopify's Partner Program Agreement are prohibited, and might result in action being taken against your account. This includes submitting fake or misleading reviews, and review incentivization. For more information, refer to the [Partner Program Agreement terms](https://www.shopify.com/partners/terms).

---

## How to ask for theme reviews

You can ask merchants to leave reviews on your theme as long as you don't encourage them to leave a good review. You should use neutral language, and never make an offer in exchange for a review—that goes against our review policy.

Here's an acceptable example of an **appropriate** review request:

> "We value feedback! It helps us make our product better and keeps us energized. Let us know how we're doing."

Here are some examples of **inappropriate** review requests:

- "Like our service? Leave us a positive review!"

  This request motivates only users who have a favorable perception of your services.

- "Get free customizations by leaving us a review!"

  If you're giving a merchant something for free, you're influencing them to leave a positive review.

- "Positive feedback keeps us going! Help by leaving a review now!"

  This suggests that the review should only be positive.

---

## Replying to theme reviews

Replying to theme reviews can help you identify issues, engage with merchants, and give them a more favorable experience with your theme. Replies can also show other merchants how engaged you are which can encourage them to install your theme.

You can reply to theme reviews if you're an account owner, or if you have a staff account with the **Manage public listings** permission. You can change an account's permissions from your [Partner Dashboard](https://partners.shopify.com/current/memberships).

### Steps:

1. Log into your [Partner Dashboard](https://partners.shopify.com/organizations)

2. Click **Themes**

3. Click the theme you want to view

4. On the **Total reviews** card, click **View all reviews**

   Your theme listing page will open in the Shopify Theme Store, and you'll see the **Reviews** section

5. Under the review you want to respond to, click **Reply**.

6. Enter your reply, then click **Submit reply**.

When you reply to a review, your reply appears below the review on your theme listing page. You can edit your response at any time, and only your latest response will be shown on your theme listing page.

The merchant will receive a notification that you replied to their review. The merchant can decide to edit their review, including the rating. If a merchant updates their review, it will replace the original review and rating. When a merchant updates a review, you'll receive an email notification.

### Tips for replying to reviews

- Consider replying first to reviews with the lowest star rating, or that mention an issue the merchant has experienced
- Reply to reviews as they come in—prompt replies can help engage the merchant in a productive conversation
- Use language consistent with your brand
- Be clear and concise
- Avoid including any technical jargon, marketing language, or spam
- Personalize the response for the merchant instead of giving them a generic response, but make sure you don't share any personal or financial information in your responses. Personal information includes full name, contact information, and private conversations between yourself and a merchant.
- Anyone who visits your theme listing can see your responses, so make sure every response is professional, respectful, and empathetic

---

## Managing negative reviews

Negative reviews can help you identify issues with your theme. If a merchant leaves a negative review because of a bug or other issue, you should work with the merchant to fix the issue. After the issue is fixed, you can ask the merchant to consider updating their review. This request should never be forceful or attached to an incentive.

If a merchant leaves a negative review containing information that you disagree with, the best course of action is to respond and seek to understand their feedback. You can also use your reply to share your perspective on the matter, in a respectful way.

### Circumstances where Shopify will intervene

Sometimes, reviews are fake, incentivized, or non-compliant with our policies. In these circumstances, we'll intervene and potentially edit or remove reviews from theme listings. We'll investigate reviews that include the following:

- **Inappropriate content** - The review contains swearing, slurs, or threats.

- **Personal information** - The review contains phone numbers, email addresses, mailing addresses, or other personal information.

- **Conflict of interest** - The review was written by a merchant who was offered something in exchange for a review. We'll also remove reviews left by theme developers and affiliated employees on either their own theme or on a competing theme.

If you find a review that meets any of the criteria above, you can [report it](https://www.shopify.com/legal/tools/report-an-issue/report-a-partner-violation).

---

### Shopify Brand Assets for Marketing Your Theme

> Fonte: https://shopify.dev/docs/storefronts/themes/store/success/brand-assets

# Shopify Brand Assets for Marketing Your Theme

Shopify provides Partners with tools to help promote and grow their business on the Shopify Theme Store. To help you showcase your presence on the Shopify Theme Store in your marketing materials, we've created the following Shopify brand assets and guidelines for you to use in any digital display ads and digital properties, such as your website, social marketing, email marketing, print materials.

Before downloading and using the Shopify brand assets, make sure that you read and fully understand the following usage guidelines.

---

## Shopify Theme Store Ad Badge

Although you might market your theme outside of the Shopify Theme Store, the purchase flow must redirect to the Shopify Theme Store. Themes listed on the Shopify Theme Store are only permitted to be sold through the Shopify Theme Store. Use the following official badge assets for using the Shopify brand when you market your Shopify theme.

| | |
| - | - |
| Preferred badge | Alternate badge |

[Download the badge assets](https://shopify.dev/zip/shopify-theme-store-badges.zip)

---

## Using the Shopify Theme Store ad badge

Having a standardized ad badge that can only be used by active and approved Partners creates consistency in our ecosystem branding and reinforces the Shopify Theme Store as a trusted place for merchants to source high-quality themes. To maintain this consistency, the logo should not be altered in any way.

### Prohibited alterations

To keep consistency in how the Shopify Theme Store ad badge is used, you can't make any of the following alterations:

- Crop any part of the badge
- Stretch or squash the badge
- Rotate or tilt the badge
- Modify the colors
- Add a gradient or shadow
- Animate the badge
- Accessorize the badge or layer other images over the top of it
- Add a border or treatment around the badge
- Layer the badge over another logo or branded image

| | | |
| - | - | - |
| Don't alter or remove parts of the badge | Don't squish or stretch | Don't rotate the badge |
| Don't use busy backgrounds | Don't add gradients or shadows | Don't change the color |

### Minimum size and spacing

The badge looks best with specific size and spacing. The badge shouldn't be smaller than 30px in height. It should have a minimum clear space around it equal to the size of the Shopify bag icon in the image. Don't place any typography, imagery, or other graphical images inside the clear space.

| | |
| - | - |
| Badge spacing | Minimum badge height |

### Link and alt tag requirements

- Any hyperlinks must point to the theme page listing on the Shopify Theme Store (not to a download/install URL).
- Alt tags on the badge should include the theme name and reference to the Shopify Theme Store.

---

## Further reading

The use of the Shopify Theme Store Ad Badge (the "Badge") is subject to our [Trademark Usage Guidelines](https://www.shopify.com/press/brand). Use of the Badge must be explicitly authorized by Shopify in writing. For Developers who are part of the Shopify Partner Program, this authorization is provided in Part A, Section 5 of the [Shopify Partner Program Agreement](https://www.shopify.com/partners/terms). Where used on a web page, the Badge should include embedded hyperlinks to your Theme listing page on the Shopify Theme Store.

---

### Updating your theme

> Fonte: https://shopify.dev/docs/storefronts/themes/store/success/updates

# Updating your theme

> **Caution:** All themes published before May 15, 2025 on the Shopify Theme Store must be updated and submitted for review. To keep your themes published:
> - Review and meet new [requirements](https://shopify.dev/docs/storefronts/themes/store/requirements) for your themes and presets
> - Update your theme zip with the [new file structure](#adding-theme-presets) by June 22, 2025
> - Edit your preset [listing pages](https://shopify.dev/docs/storefronts/themes/store/review-process/listings) by July 1, 2025

After you've first published a theme on the Theme Store, you begin the iterative process of considering merchant feedback, persistently innovating your build through regular quality assurance testing, and actively integrating the updates required by Shopify.

To avoid update fatigue for merchants, you must have a minimum of four weeks between updates. New themes on the Shopify Theme Store are an exception, and can have an update every two weeks for the first two months.

As a Shopify Theme Partner, you're required to provide ongoing updates to your theme to remain on the Shopify Theme Store.

The following sections describe the theme update process, the types of updates, and adding theme presets.

---

## Theme update process

You can submit your updates for review as ZIP files through your Partner Dashboard. Each update should have a [version number](#versioning), determined by the content of the update, and [release notes](#release-notes).

The theme review team primarily reviews theme updates during Eastern Standard Time (EST) hours, Monday through Friday. If you need to make a crucial update, then try to submit it earlier in the week, and earlier in the business day. Submitting a theme update outside of EST business hours might impact how quickly merchants receive and apply your updates.

Updates mandated by Shopify might be required by a deadline to accommodate a feature's release date.

After your update has been successfully reviewed and published, you receive an automatic notification email. If you've added new presets, you will need to edit your theme's listing and provide marketing information for them. New presets are visible on the Theme Store once required marketing information is completed and submitted via the `edit listing` page, accessible from [Partner Dashboard](https://partners.shopify.com/current/themes).

> **Note:** The Theme Store only lists the latest version of your theme and presets. Reviews from all previous versions appear under the same listing. You can't charge different prices per version.

---

## Update types

Depending on the contents of the new theme version, a merchant's theme can be updated in the following ways:

- A [manual update](#manual-updates)
- An [automated update](#automated-updates)

Because each update type uses a unique update process, you should group changes based on update types as much as possible. Specifically, automated updates are more merchant-friendly as they require no manual action. Therefore, grouping changes can help to ensure that a greater number of merchants who have purchased your theme receive as many automatic updates as possible.

### Manual updates

The theme review team publishes a theme update as a manual update if it contains at least one of the following code changes:

- A setting ID is changed or removed
- A setting type is changed or removed
- The `min` value for a setting of type `range` is increased
- The `max` value for a setting of type `range` is decreased
- A section or block is removed

These changes can significantly impact the merchant's experience, because they can invalidate current settings, or require the merchant to review and adjust their theme configuration. For example, changing the ID of a setting is equivalent to removing the current setting and adding a new one with the default value, which can lead to a poor merchant experience and should be avoided.

When an update is published as a manual update, merchants are shown a notification on the **Online store** > **Themes** page letting them know that they can update their theme. The updated theme is installed as an unpublished theme in their theme library. Merchants can review this unpublished theme before they publish it in their store. The parent theme is not modified.

![Sample online store with a manual update available for Dawn theme.](https://shopify.dev/assets/assets/images/themes/store/success/add-to-theme-library-Dzr-rGRm.png)

### Automated updates

If a theme update doesn't contain any changes that would categorize it as a manual update, then it's published as an automatic update. In this case, the new version of the theme replaces the current published version that merchant has installed, without creating a new theme.

A theme is automatically updated only if all theme files, except `settings_data.json` and any JSON files in the `/templates` directory, are in their original state. If a theme can't be automatically updated, then merchants are shown a notification on the **Online store** > **Themes** page letting them know that they can apply the update to an unpublished copy of their theme to be reviewed and published.

---

## Considerations for new versions

Consider the following, and the associated merchant impact, when creating new versions:

- If you change an existing setting so that the merchant's value is no longer valid, then the merchant's value will be reset to the default, as specified in your new version. To create less friction for existing merchants, you should keep the same default settings when possible.

- If you change the class of a section or change a CSS class name, then a merchant's [custom CSS](https://help.shopify.com/manual/online-store/themes/theme-structure/extend/add-css) might be invalidated. You should avoid renaming existing classes unless necessary, and document any of these changes in your release notes.

> **Caution:** Reducing certain limits or section availability can break and invalidate existing themes, and make themes ineligible for an update. Theme versions can't be submitted to the Theme Store if they include any of the following updates:
> - Reducing the number of instances to any section file by changing the section [limit](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#limit).
> - Reducing the limit of blocks in a section.
> - Adding section restrictions to section groups using `disabled_on` or `enabled_on`.
> - Adding restrictions that prevent sections from appearing on certain templates.

---

## Versioning

Theme versions help merchants easily identify which theme they have, so that they can determine which features are available, or if there are more recent versions to update to.

When building your version string, you should use [semantic versioning](https://semver.org/) in the format of `X.Y.Z`.

| Component | Description |
| --- | --- |
| `X` | Represents a major version that introduces or modifies features that aren't backwards compatible, such as the following: - Modifying a settings value. - Removing a setting, section, or block. - Adding a global setting. For example, you might move from `1.4.8` to `2.0.0`. |
| `Y` | Represents a minor version that introduces or modifies features that are backwards compatible, such as the following: - Modifying the label or default value of an existing setting. - Adding a section or block. - Changing the visual design, or functionality, of an existing section or block without changing their setting schema. For example, you might move from `1.4.8` to `1.5.0`. |
| `Z` | Represents a maintenance version that fixes bugs or security issues, or makes non-visual code improvements. For example, you might move from `1.4.8` to `1.4.9`. |

The theme version can be included in the theme through [theme metadata](https://shopify.dev/docs/storefronts/themes/architecture/config/settings-schema-json#add-theme-metadata).

---

## Release notes

For each theme version, you need to have release notes that highlight the main features of the version.

The main audience for release notes is merchants, so the language you use should reflect that. Release notes aren't intended to be a changelog, but rather a curated list of items that will impact merchants, or their buyers. As such, any user-facing changes should be included, and developer-facing changes should be excluded. You should also include only information related to the current release.

### Include release notes in your theme

To include release notes with your theme, create a markdown file in the root of your theme's ZIP called `release-notes.md`.

> **Note:** The `release-notes.md` file is required only after a theme has been published to the Theme Store. You should exclude this file during the review process.

The file's contents should contain the following components:

| Component | Description |
| --- | --- |
| Description | A summarized description of the most important changes in this version. |
| List of changes | A list of changes contained in the version. Changes can fall under one of the following headings: - **Added** - **Changed** - **Removed** - **Security** - **Other fixes and improvements** Changes should be listed in bullet point under their respective heading. Each heading should be treated as an **H3**, so needs to be preceded by `###`. For example, `### Added`. If there are specific changes that you want to bring attention to, then you can prepend the change with `Important:`. For example: `- Important: This is an important change.` When the release notes are rendered, these important changes will be visually highlighted. |

#### Example

```markdown
We've added the ability to add Shop Pay Installment payment options for your customers, removed the Instagram section, and changed how the social media section works.

### Added

- Important: Added search faceted filtering
- Added selling plans to cart notifications

### Changed

- Important: Changed default social media sharing image with the one from the Shopify admin. You can add a default image to be used when a featured image for the page can't be found.

### Removed

- Removed the Instagram section since the API has been deprecated with no suitable replacement. From now on you'll need to switch to using an app to display your Instagram feed.

### Security

- Fixed security issues

### Fixes and other improvements

- The collection page sidebar is now aligned with the utility bar
- The products in the collection 'list-view' no longer have a long blue outline when viewed on an iOS device
- Fixed the 'forgot your password' link on the customer login page
- Fixed collection list pagination displaying incorrectly with large collection sets
```

![Example of rendered release notes.](https://shopify.dev/assets/assets/images/themes/store/success/release-notes-example-Dokp99Du.png)

---

## Urgent updates

An urgent update is a theme update that merchants require immediately to run their business without interruption. Urgent updates can be either [manual](#manual-updates) or [automated](#automated-updates). The urgency is meant to alert the theme review team that the update is more critical than a regular update.

Typically, only updates that address an issue with the purchase flow are considered urgent. The purchase flow is the process that a customer undertakes when making a purchase, starting from the product page and continuing to checkout through the accelerated checkout button, or continuing from the cart to checkout through the checkout call-to-action or accelerated checkout buttons.

If you have an update that you deem to be important that doesn't affect the purchase flow, then you can consult your Theme Partner Manager before you submit the update.

---

## Adding theme presets

Presets enable you to create up to five pre-configured designs from the same theme code base. Each preset includes a combination of layout options, color schemes, typography, and other visual elements.

Theme presets are included under one theme package. This gives merchants multiple customization options that they can apply to their store to change the general look and feel of the theme without extensive design skills or coding knowledge. Each preset gets its own dedicated listing page on the [Theme Store](https://themes.shopify.com/) that aligns to a primary industry and catalog size to appeal to a specific merchant segment.

Complete the following steps to update your theme so that it includes a theme preset:

1. Edit your theme code to [add a new preset](https://shopify.dev/docs/storefronts/themes/architecture/config/settings-data-json#theme-presets). Themes must use the following file structure when adding presets:

```
.
├── assets
├── blocks
├── config
├── layout
├── locales
├── listings
│   ├── existing-preset-name
│   │   └── templates
│   │       └── *.json
│   │   └── sections (optional)
│   │       └── *.json
│   └── new-preset-name
│       └── templates
│           └── *.json
│       └── sections (optional)
│           └── *.json
├── sections
├── snippets
└── templates
```

2. Submit a new ZIP file through the Partner Dashboard as a [theme update](#theme-update-process).
3. Include the new preset demo URL and password in the theme update submission form.
4. After submitting, our team will review and test your update before rejecting or approving. You will receive an email notification once we've made a decision.

> **Caution:** After your update has been approved, you need to edit your theme's listing page to provide marketing information and demo store details. This can be accessed in the [Partner Dashboard](https://partners.shopify.com/current/themes) for the newly added presets. Once the required fields are complete, submit. Your new presets will be visible on the Theme Store.

---

## Best practices on structuring your theme zip

The following is an example of what would pass validation as a theme zip submission. You need to modify your `settings_data.json` file and contents in the theme zip's `/listings` folder to ensure your theme matches the new structure rules.

**Example theme:** Embiggen (specified in `settings_schema.json`)

**Example presets:**

- Embiggen
- Canine Gourmand
- Zenful
- Embox
- 7th Street

### Example settings_data.json

```json
[
  {
    "current": {...},
    "presets": {
         "Embiggen": {...},
         "Canine Gourmand": {...},
         "Zenful": {...},
         "Embox": {...},
         "7th Street": {...}
    }
  }
]
```

### Do:

- Use upper and lower case letters to reflect proper sentence structure
- Use less than 30 characters and 1-2 words for preset names
- Name one preset the same as your theme name

### Don't:

- Include special characters (i.e. - . é), except a single space
- Include more than two words for preset names

### Example theme zip structure

```
/assets
/blocks
/config
/layout
/locales
/listings
	/embiggen
		/templates
			404.json
			index.json
			product.json
	/canine-gourmand
		/templates
			index.json
			blog.json
			collection.json
			cart.json
		/sections
			header-group.json
	/zenful
		/templates
			blog.json
	/embox
		/templates
			index.json
			404.json
			product.json
			cart.json
			collection.json
			blog.json
		/sections
			header-group.json
			footer-group.json
	/7th-street
		/templates
			index.json
			404.json
			product.json
			cart.json
			collection.json
			blog.json
		/sections
			header-group.json
			footer-group.json
/sections
/snippets
/templates
```

### Do:

- Include preset-unique .json files in each preset listing folder; no need to duplicate identical files
  - Preset folders do not need to include the same number of .json files.
  - Root level `/templates` and `/sections` folders should include the complete "base" set of .json files.
  - Include `/templates` folder in for each preset, these will overwrite the base set of /template .json files.
  - Include `/sections` folder as necessary. If you don't have preset-specific changes, you can exclude this folder entirely. These will overwrite the "base" `/sections` .json files.
- Preset listing folders are kebab-case so that they can be used in URLs (i.e. `hello there` → `hello-there`).

### Don't:

- Include special characters in folder names (i.e. do not use spaces)
- Duplicate .json files for every preset when the contents are identical
- Include "demo" .json (or sections within that .json file) that shouldn't be used by merchants (i.e. things that showcase what your theme does vs. what a merchant would use upon install)

---

### Removing your theme from the Shopify Theme Store

> Fonte: https://shopify.dev/docs/storefronts/themes/store/success/remove-theme

# Removing your theme from the Shopify Theme Store

This guide describes the process of removing a theme that you no longer want to support from the Shopify Theme Store.

---

## Should I remove a theme?

The success of a merchant's business depends greatly on their theme, and removing a theme from the Shopify Theme Store could have an adverse impact on their business. When purchasing a theme, a merchant expects that the theme includes support, future platform updates, and bug fixes.

As a Shopify Partner, you have a responsibility to your merchants, and removing a theme should always be a last resort. When removing your theme, make sure to minimize the negative impact on merchants.

> **Tip:** If your reason for removing a theme is related to poor sales, then explore ways to [improve your theme's success](https://shopify.dev/docs/storefronts/themes/store/success).

---

## Removing a theme

If you want to remove a theme that you've listed on the Shopify Theme Store, then contact Partner Support through your Partner Dashboard and inform them that you want to notify the Theme Store Operations team that you intend to remove your theme. Make sure that you provide the reasons behind your decision.

While you wait for your theme to be removed, you need to continue supporting your theme and providing bug fixes. You're also expected to continue to support existing merchants using your theme with general bug fixes and maintenance for at least one month after removal.

> **Caution:** Failing to follow these guidelines can impact your relationship with Shopify and the Shopify Theme Store.

---

## Previous theme removals or inactive themes

If a theme has been removed from the Shopify Theme Store or is inactive for over two years, then Shopify has the right to reuse the theme's name for a different theme.

---

## Revenue share for Shopify Theme Store developers

> Fonte: https://shopify.dev/docs/storefronts/themes/store/theme-revenue-share

# Revenue share for Shopify Theme Store developers

Theme developers can earn revenue by selling their themes to merchants on the Shopify Theme Store, where there are no fees for submitting themes for listing. However, total theme revenues are subject to a 15% revenue share. This revenue share applies to all themes listed on the Shopify Theme Store.

Other income, such as from the Shopify App Store or referrals, isn't included in revenue share calculation for the Shopify Theme Store. Learn more about [app revenue share](https://shopify.dev/docs/apps/launch/distribution/revenue-share).

> **Tip:** Revenue share is calculated based on gross sales, not net sales.

## Associated Theme Developer accounts

An Associated Theme Developer Account is any Partner account that a theme developer or Associated Theme Developer has registered with Shopify. Learn more about [Associated Developer Accounts](https://help.shopify.com/en/partners/dashboard/associated-accounts) on Shopify Help Center.

## Billing fees and sales tax

All billing is subject to a 2.9% processing fee and applicable sales tax. As of August 1, 2021, fees and taxes are charged separately.

Earnings in some countries or regions are subject to additional [regulatory operating fees](https://help.shopify.com/en/partners/how-to-earn#regulatory-operating-fee).

## Viewing your earnings and fees

There are several ways to review your earnings and fees in the [Partner Dashboard](https://partners.shopify.com/current/stores):

- [View app charges for a specific store](https://shopify.dev/docs/apps/launch/billing/view-charges-earnings#store-page)
- [View app charges in the Payouts page](https://shopify.dev/docs/apps/launch/billing/view-charges-earnings#payouts-page)
- [View app charges from the App history page](https://shopify.dev/docs/apps/launch/billing/view-charges-earnings#app-history-page)
- [Download a CSV of your payouts in the Payouts page](https://help.shopify.com/partners/getting-started/getting-paid#export-your-payouts)
- [Review the Shopify fees invoice in the Payouts page](https://help.shopify.com/partners/getting-started/getting-paid#shopify-fees-invoice)

You can also use the [Shopify Partner API](https://shopify.dev/api/partner) to programmatically access the data found in your Partner Dashboard to automate your front and back office operations.

---

## Pagine non catturate

Nessuna. Tutte le pagine della sezione "Sell themes" (Theme Store) sono state catturate con successo.

> **Nota sui percorsi/slug:** Lo slug della sezione **Testing** nella documentazione attuale è `/store/test-theme` (non `/store/testing`), e quello della sezione **Theme success** è `/store/success` (non `/store/theme-success`). Lo slug della pagina **Theme revenue share** è `/store/theme-revenue-share`. Gli slug ipotizzati `testing`, `theme-success` e `theme-revenue-share`/`revenue-share` come URL diretti restituivano 404; i contenuti corretti sono stati recuperati dagli slug reali sopra indicati.
