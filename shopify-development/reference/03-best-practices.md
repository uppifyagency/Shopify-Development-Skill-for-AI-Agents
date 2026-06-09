# 3. Best Practices

This chapter reproduces the **Best practices** section of the Shopify Themes documentation. To optimize your theme development experience, Shopify has established a set of best practices that you can refer to when developing your theme and setting up your toolchains and processes. The pages below cover the overview and guiding principles, how to architect templates, sections and blocks, how to bundle JavaScript and stylesheet tags, performance (including the Shopify platform and stylesheet subsetting), accessibility, the theme editor (integrating sections/blocks and the preview inspector), design (including the color system), working on merchant stores, version control, file transformation, and avoiding deceptive coding practices.

Each section preserves the source content faithfully (1:1) and cites its source URL.

---

## Chapter table of contents

1. [Overview — Best practices for building Shopify themes](#overview--best-practices-for-building-shopify-themes)
2. [Building with sections and blocks](#building-with-sections-and-blocks)
3. [JavaScript and stylesheet tags](#javascript-and-stylesheet-tags)
4. [Performance best practices for Shopify themes](#performance-best-practices-for-shopify-themes)
   - [The Shopify Platform](#the-shopify-platform)
   - [Stylesheet content subsetting](#stylesheet-content-subsetting)
5. [Accessibility best practices for Shopify themes](#accessibility-best-practices-for-shopify-themes)
6. [Theme editor best practices](#theme-editor-best-practices)
   - [Integrate sections and blocks with the theme editor](#integrate-sections-and-blocks-with-the-theme-editor)
   - [Theme editor preview inspector best practices](#theme-editor-preview-inspector-best-practices)
7. [Designing Shopify themes](#designing-shopify-themes)
   - [Color system best practices](#color-system-best-practices)
8. [Working on themes attached to merchant stores](#working-on-themes-attached-to-merchant-stores)
9. [Version control for Shopify themes](#version-control-for-shopify-themes)
10. [File transformation best practices for Shopify themes](#file-transformation-best-practices-for-shopify-themes)
11. [Avoid deceptive coding practices](#avoid-deceptive-coding-practices)

---

## Overview — Best practices for building Shopify themes

> Fonte: https://shopify.dev/docs/storefronts/themes/best-practices

# Best practices for building Shopify themes

To optimize your theme development experience, Shopify has established a set of best practices that you can refer to when developing your theme and setting up your toolchains and processes.

---

### Designing and coding a theme

A great theme creates a great customer experience, while ensuring the merchant's store is fast, accessible and discoverable. Shopify developers have identified principles and best practices that you can follow to design and build an optimized theme:

* [**Templates, sections, and blocks**](https://shopify.dev/docs/storefronts/themes/best-practices/templates-sections-blocks)
* [**Performance**](https://shopify.dev/docs/storefronts/themes/best-practices/performance)
* [**Accessibility**](https://shopify.dev/docs/storefronts/themes/best-practices/accessibility)
* [**Design**](https://shopify.dev/docs/storefronts/themes/best-practices/design)

#### Avoiding deceptive coding practices

As a Partner and a developer, you should never use deceptive coding practices, such as obfuscating code or manipulating search engines.

---

### Using theme tools and build tools

* [**Version control**](https://shopify.dev/docs/storefronts/themes/best-practices/version-control)
* [**File transformation**](https://shopify.dev/docs/storefronts/themes/best-practices/file-transformation)

---

### Guiding principles for theme development

| Principle | Description |
| - | - |
| Be performant | "Themes should be built with performance in mind...minimize the use of JavaScript" |
| Be purpose-built | "Each theme's layout, style, and feature set should be opinionated and optimized" |
| Offer best-in-class UX | Themes should prioritize quality and customer experience |
| Be mobile first | Mobile devices must be central to the theme build process |
| Be accessible | "Themes must be built from the ground up with accessibility best practices" |
| Make customization simple | Provide intuitive merchant customization options |

---

## Building with sections and blocks

> Fonte: https://shopify.dev/docs/storefronts/themes/best-practices/templates-sections-blocks

# Building with sections and blocks

When you're designing a theme, you should consider when to provide functionality in a section or a block. Sections and blocks are modular components that give merchants the opportunity to customize and extend their theme. Merchants can add and remove sections and theme blocks, adjust section and block settings, and introduce [app blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks) and [metafields](https://shopify.dev/docs/api/liquid/objects/metafield).

These guidelines apply to [Online Store 2.0](https://shopify.dev/docs/storefronts/themes/best-practices/version-control) themes, which use [JSON templates](https://shopify.dev/docs/storefronts/themes/architecture/templates) and [section groups](https://shopify.dev/docs/storefronts/themes/architecture/section-groups). You can't add or remove [static sections](https://shopify.dev/docs/storefronts/themes/architecture/sections#statically-render-a-section) from Liquid templates or layouts.

---

### Sections

[Sections](https://shopify.dev/docs/storefronts/themes/architecture/sections) are available on all pages.

When building theme templates, you should ensure that your template's default content is available in a main template section, and that sections can be added, removed, and reordered. You can use sections to do the following:

* To add, remove, or reorder content at the template or section group level
* To control theme settings that are scoped to the entire section's layout and content

---

### Blocks

You should provide [blocks](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#blocks) to add, remove, or reorder content at the section level, or when it enhances the usability of a section.

Keep the following principles in mind when developing blocks:

* Ensure that the [theme settings](https://shopify.dev/docs/storefronts/themes/architecture/settings) are scoped to the block.
* Choose a [block layout](#block-layouts) that is appropriate for the content, and ensure that your blocks flow logically regardless of block type or sequence.
* Select an appropriate [flexibility level](#blocks-and-flexibility) to introduce using blocks.

#### Block layouts

When designing the grid layout for your section, ensure that your blocks follow a logical and intuitive reading flow regardless of the block types and block sequence.

Consider the following when determining how blocks should flow in a section:

* Stack blocks vertically for text-based content that requires hierarchy.
* If you don't need to show hierarchy, then either stack blocks horizontally or create a grid that adapts to the block types that are available in the section.
* When stacking blocks horizontally, either ensure that the section grid can wrap on several lines or offer horizontal sliding controls to maintain a comfortable block width. Ensure your section grid is responsive and that blocks can reflow depending on screen size.

**Do:**
- Blocks wrap on several lines.
- Add sliding controls to move between blocks in narrow viewports.

**Don't:**
- Avoid squeezing blocks to fit in narrow viewports.

* Don't rely on a specific block type or sequence to design a layout, and don't use a specific block order to change the grid layout.

**Do:**
- Enforce expected layouts by grouping settings into a single block.

**Don't:**
- Don't rely on a specific block type or sequence to design a section layout.
- Don't use a specific block order to change the grid layout.

#### Blocks and flexibility

To balance simplicity and flexibility, you should carefully consider when to add blocks and what each block should contain. Too many blocks creates clutter and complexity. You can use the following principles to understand how to define your blocks.

* Group settings into blocks to simplify the editing experience and declutter the editor sidebar. For example, you can nest theme settings to customize an image block inside of the block.
* When elements follow a specific hierarchy, group elements together and optionally allow block insertion points before and after. For example, you might create a single block that controls cart page line items.
* Avoid providing blocks that are too granular. Granularity adds complexity to the theme code and to the merchant editing experience. For example, you should group the author, date, and comments into a single block or into settings, rather than introducing these attributes as three separate blocks.

**Do:**
- Choose the right level of granularity for blocks in your sections.

**Don't:**
- Avoid overly granular block design.

#### Considerations for app blocks

Merchants can add [app-provided blocks](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions) to their themes. As a theme developer, you need to [add support](https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks) for these types of blocks to your sections. Consider the following when deciding whether to support app blocks in a section:

* Provide app blocks in sections that have clear use cases for layering additional conversion tools, or purchase decision factors. For example, you might want to include an app block with the product information on the product page, or in the cart template.
* Always consider antifragility and the section's purpose when considering extending a theme using app blocks. Would the layout break easily when inserting unexpected block types? Would it require adding edge-case CSS styles to handle those blocks? Would it make the section's purpose vague, or inconsistent? If the answer is yes to these questions, then avoid app blocks.

---

### Theme settings

Use [theme settings](https://shopify.dev/docs/storefronts/themes/architecture/settings) to provide different look and feel options. Theme settings can be applied at the section, block, and theme levels.

#### Metafields

Shopify provides various standard [metafields](https://shopify.dev/docs/api/liquid/objects/metafield) that can fit your target segment. Review what's available and consider which use cases make sense for the theme. For example, you might include either sections or blocks for a care guide or size chart metafield. These metafields, when referenced as [dynamic sources](https://shopify.dev/docs/storefronts/themes/architecture/settings/dynamic-sources), update to reflect their context, such as the product that is being rendered.

When building metafields into your theme, consider building specific blocks for metafields. You can also audit ecommerce websites for your target segment, and analyze how content is presented to identify opportunities to design specific components. For example, you might want to use metafields to create a well-formatted information list for electronic products, or to add information about a coffee blend and origin.

---

## JavaScript and stylesheet tags

> Fonte: https://shopify.dev/docs/storefronts/themes/best-practices/javascript-and-stylesheet-tags

# JavaScript and stylesheet tags

You can bundle JavaScript and stylesheet assets with `section`, `block` and `snippet` files using the following Liquid tags:

* `{% javascript %}`
* `{% stylesheet %}`

Including assets with the relevant files can help you keep the theme modular, making the files portable across different themes and shops without losing their functionality or styling.

If reusability isn't a concern, then you can place the JavaScript or CSS styles that your file needs in your theme's `assets` directory and include them using the `asset_url` filter with either the `script_tag` filter or `stylesheet_tag` filter. If an asset has already been included in a parent layout or template, then you don't need to include it again.

**Caution:**

"Liquid isn't rendered in `{% javascript %}` or `{% stylesheet %}` tags. Including Liquid code in these tags can cause syntax errors, or prevent styles from being applied to the theme."

---

### javascript

To include JavaScript, use the `{% javascript %}` tag:

```liquid
{% javascript %}
  document.querySelector('.slideshow').slideshow();
{% endjavascript %}
```

**Caution:**

"Each file can only have one `{% javascript %}` tag. Having more than one will result in a syntax error when editing your theme code."

Shopify concatenates the content from `{% javascript %}` tags across all section, block and snippet files into one file per file type:

* **sections**: `scripts.js`
* **blocks**: `block-scripts.js`
* **snippets**: `snippet-scripts.js`

These files are then injected into the theme through the `content_for_header` Liquid object and asynchronously loaded through a `<script>` tag with the `defer` attribute.

The content from each `{% javascript %}` tag is wrapped in a self-executing anonymous function so that any variables are defined within a closure, and runtime exceptions won't affect other sections.

#### Instance specific JavaScript

Bundled assets are only injected once for each section, block or snippet file, not for each instance of that file. If you need instance-specific JavaScript, then add data attributes to your section markup and reference those attributes in your JavaScript. For example:

##### /sections/slideshow.liquid

```liquid
<div className="slideshow-wrapper" data-slide-speed="{{ section.settings.speed }}">
  <!-- slideshow content -->
</div>


{% javascript %}
  var slideshowSpeed = parseInt(document.querySelector('.slideshow-wrapper').dataset.slideSpeed);
{% endjavascript %}
```

---

### stylesheet

The `{% stylesheet %}` tag can be used to include CSS styles:

```liquid
<div className="slideshow-wrapper" data-slide-speed="{{ section.settings.speed }}">
  <!-- slideshow content -->
</div>


{% stylesheet %}
.slideshow-wrapper {
  // your styles
}
{% endstylesheet %}
```

**Caution:**

"Each file can only have one `{% stylesheet %}` tag. Having more than one will result in a syntax error when editing your theme code."

Shopify collects the content from `{% stylesheet %}` tags across sections, blocks, and snippets into a single `styles.css` file. A link to this generated file is automatically injected into the theme through the `content_for_header` global Liquid object. To optimize performance, Shopify subsets this CSS so that each page only loads the styles from files in its render tree, rather than bundling all `{% stylesheet %}` CSS on every page.

#### Instance specific styles

Bundled assets are only injected once for each section, block or snippet file, not for each instance of that file. If you need instance-specific CSS, then use an inline `<style>` tag.

---

## Performance best practices for Shopify themes

> Fonte: https://shopify.dev/docs/storefronts/themes/best-practices/performance

# Performance Best Practices for Shopify Themes

Performance is a critical factor when merchants evaluate themes. Optimizing your theme directly influences conversion rates, repeat business, and search engine rankings.

For Shopify Theme Store submission, themes must achieve a minimum average Lighthouse performance score of 60 across home, product, and collection pages. Shopify's Dawn theme exemplifies these performance principles.

### Optimizing for Performance

#### Optimize Your JavaScript

##### Reduce JavaScript Usage

Build themes primarily with HTML and CSS. JavaScript should enhance functionality progressively, not provide essential features like product browsing or purchasing.

CSS renders faster than JavaScript. Your minified JavaScript bundle should not exceed 16 KB. Shopify automatically minifies JavaScript upon storefront request.

##### Avoid Namespace Collisions

Wrap JavaScript values in function scope to prevent global namespace collisions when minifiers rename variables:

```js
(function () {
  var a; function b() {}
})();
```

Use the Immediately Invoked Function Expression (IIFE) pattern. Scripts injected in themes must always be wrapped in an IIFE to prevent global namespace collisions.

##### Reduce Dependency on External Frameworks and Libraries

Avoid third-party frameworks like React, Angular, and Vue, or large utilities like jQuery. Use native browser features and modern DOM APIs instead. Avoid polyfills for very old browsers. Target browsers with >1% marketshare using browserslist.

##### Avoid Parser-Blocking Scripts

Parser-blocking scripts prevent DOM construction and rendering until execution completes. Use `defer` or `async` attributes on script tags to avoid blocking First Contentful Paint and Largest Contentful Paint metrics.

#### Preload Key Resources, Defer or Avoid Loading Others

##### Use Resource Hints to Preload Key Resources

Add up to two resource hints per template using:

* The `preload_tag` filter
* The `preload` keyword argument on `stylesheet_tag` or `image_tag` filters

When Shopify renders pages with preload instructions, it sends preload resource hints as Link headers on subsequent requests. Use resource hints sparingly—preload only render-blocking stylesheets needed for above-the-fold content.

##### Lazy Load Below-the-Fold Images

Load images only when needed. Pass `loading: 'lazy'` to the `image_tag` filter:

```liquid
{{ settings.favicon | image_url: width: 200 | image_tag: loading: 'lazy' }}
```

Never lazy-load above-the-fold content. Above-the-fold resources are critical assets that should load normally.

##### Load Non-Critical Resources on Interaction

Use the import on interaction pattern to load components or resources that aren't always used, avoiding unnecessary parsing and execution.

##### Consider Using a System Font

System fonts avoid requiring clients to download additional resources before text rendering.

#### Host Assets on Shopify Servers

Deliver assets from the Shopify CDN by adding them to the theme's `/assets` folder using:

* Manual addition
* GitHub Integration
* Asset REST Admin API resource

Create links using URL filters. Using the same host avoids unnecessary HTTP connections and enables HTTP/2 prioritization.

#### Use Responsive Images

Responsive images automatically resize for device screens. Specifying image sizes ensures downloading the smallest file without quality loss.

Use the `image_tag` filter to add responsive images:

##### Input

```liquid
{{ product.featured_image | image_url: width: 2000 | image_tag }}
```

##### Output

```html
<img
  src="/content/assets/images//cdn.shopify.com/s/files/1/0251/7476/9720/files/.png?v=1580676830&amp;width=2000"
  alt=""
  srcset="//cdn.shopify.com/s/files/1/0251/7476/9720/files/teal-polo.png?v=1580676830&amp;width=352 352w,
          //cdn.shopify.com/s/files/1/0251/7476/9720/files/teal-polo.png?v=1580676830&amp;width=832 832w,
          //cdn.shopify.com/s/files/1/0251/7476/9720/files/teal-polo.png?v=1580676830&amp;width=1200 1200w,
          //cdn.shopify.com/s/files/1/0251/7476/9720/files/teal-polo.png?v=1580676830&amp;width=1920 1920w"
  width="2000"
  height="2007" />
```

Adjust srcset sizes using the `sizes` keyword argument.

#### Optimize Liquid Code

Perform complex operations before loops, not within them. Order products before iterating through them rather than calculating order for each product.

Use the Shopify Theme Inspector for Chrome to identify slow code lines. Review analysis on the Shopify Engineering blog.

#### Ensure Compatibility with Stylesheet Subsetting

Shopify automatically subsets CSS from `{% stylesheet %}` tags so each page loads only necessary styles. Ensure each file's CSS classes are used only within that file or files it directly renders. Run Theme Check to detect cross-file CSS dependencies that could cause missing styles.

#### Use Theme Check to Identify Performance Issues

Theme Check identifies performance issues including large CSS and JS bundles, remote asset references, parser-blocking JavaScript, and cross-file CSS dependencies.

### Testing for Performance

Shopify offers a Web Performance Dashboard & Reports using Real User Monitoring (RUM) data to measure store performance against Core Web Vitals standards for loading speed, interactivity, and visual stability.

PerformanceMetrics and PerformanceEvents queries (unstable GraphQL Admin API versions) provide web performance metric and Shopify event data.

For shops with minimal traffic, use Lighthouse performance scores. Run audits manually, via CI, or review managed store speed scores.

#### Run a Lighthouse Audit Using Shopify Data

Emulate Shopify's Theme Store testing process:

1. Create a development store.

2. Import the test product CSV to the store with no other collections, products, or variants.

3. In your development store beside **Online Store**, click the eye icon to preview.

4. In the preview bar, click the link icon to copy the preview link (`shopifypreview.com` URL).

5. Get URLs for pages to audit: home page, product page, and collection page.

   Example: `https://12345678.shopifypreview.com/products/sunglasses`

6. Append `pb=0` to each URL to disable the preview bar during audits:

   `https://12345678.shopifypreview.com/products/sunglasses?pb=0`

7. Visit Google Lighthouse and run reports for each page, noting mobile scores.

8. Apply this formula: [(*p* × 31) + (*c* × 33) + (*h* × 13)] / 77

   where *p* = product page score, *c* = collection page score, *h* = home page score.

Repeat multiple times and use the median for accuracy.

#### Use Lighthouse CI to Catch Performance Issues Early

Add a CI check to prevent theme changes from negatively impacting performance. Use the Shopify Lighthouse CI GitHub action, which uploads theme code to a benchmark shop and calculates speed scores.

### Next Steps

* Learn about theme accessibility best practices
* Submit your theme to the Shopify Theme Store

---

### The Shopify Platform

> Fonte: https://shopify.dev/docs/storefronts/themes/best-practices/performance/platform

# The Shopify Platform

Learn about the infrastructure that Shopify provides to make the online store, and your theme, faster.

---

#### Shopify CDN

Shopify provides merchants a world class content delivery network (CDN) backed by [Cloudflare](https://cloudflare.com/). Using a CDN means that your online store will load quickly around the globe.

Files delivered over the Shopify CDN are minified and compressed automatically using [Brotli](https://github.com/google/brotli) and [gzip](https://en.wikipedia.org/wiki/Gzip), reducing the size of the files the browser must download. Requests use [HTTP/3](https://developers.cloudflare.com/http3/) and [TLS 1.3](https://www.cloudflare.com/learning-resources/tls-1-3/) to further enhance request performance and security.

Most asset URLs are rendered using the domain `cdn.shopify.com`. In certain cases, such as images or stylesheets loaded on a storefront, assets are loaded using the storefront domain, in the format `{shop}.myshopify.com/cdn`. This is done to improve performance by maximizing connection reuse in the browser.

##### Short delays for images in your store

Using a CDN means that all of your online store images are cached at thousands of servers around the world. When you make changes to your images, Shopify informs the CDN that the images have changed. To do this, Shopify uses the [`asset_url`](https://shopify.dev/docs/api/liquid/filters/asset_url) filter, which automatically appends version numbers to all of the URLs that it generates. For example, a version number appended to the end of a URL might look like this: `?v=1384022871`.

If you link to an image without using the `asset_url` filter and upload a new version of the same image, then the image on your online store might not change to the new version for a day or more.

**Supported query parameters:**

Only specific query parameters are recognized for versioning. The supported format uses the `v` parameter for version (for example, `?v=1384022871`). Query parameters that aren't on the allowlist, such as appending a raw timestamp value without the `v=` prefix or using arbitrary parameter names, won't bust the cache.

##### CSS syntax to ensure automatic updates

If you reference an image directly in your CSS, then the URL will be static and won't carry the asset version that Shopify updates automatically.

To make sure that your images are automatically updated, change your CSS syntax to include the [`asset_url`](https://shopify.dev/docs/api/liquid/filters/asset_url) filter.

For example, if your CSS looks like this:

```css
background: url(bg.gif);
```

then change it to look like this:

```liquid
background: url({{ 'bg.gif' | asset_url }});
```

---

#### Server-side rendering

Storefront Renderer (SFR) is a server-side renderer that handles storefront requests. SFR is dedicated to serving storefront requests as fast as possible.

Our storefront renderer significantly improves performance for cache misses - instances where a page or other requested data isn't found in the cache memory and has to be retrieved from other cache levels or the main memory.

---

#### Minification

Shopify automatically minifies CSS files, as well as JavaScript files that use valid syntax to ES5, when they're requested by the storefront. Minified JavaScript and CSS files are cached until the next time the file is updated.

Minification allows the browser to download less data, resulting in shorter load times.

Shopify delivers the original version of a JavaScript or CSS file if it meets one of the following criteria:

* The minified file would be larger than the original file. This might happen if a file is already minified with better compression.
* It has the extension `.min.js` or `.min.css`.

**Tip:**

Minification might remove debugger statements from code. To debug your code, you can temporarily change your file extension to `.min.js` or `.min.css`.

---

#### Speculation rules

To improve buyer experience on Shopify stores, Shopify automatically injects [speculation rules](https://developer.mozilla.org/docs/Web/API/Speculation_Rules_API) in [supporting browsers](https://developer.mozilla.org/docs/Web/API/Speculation_Rules_API#html.elements.script.type.speculationrules).

The rules we output aim to provide largest speed gains without introducing issues with data usage, caching, or analytics. Themes can add extra rules of their own based on specific requirements and opportunities.

---

#### Polyfills

Shopify automatically includes the [`es-module-shims`](https://github.com/guybedford/es-module-shims) polyfill library in the storefront when needed. This library enhances compatibility for modern JavaScript module features, primarily [**import maps**](https://developer.mozilla.org/docs/Web/HTML/Reference/Elements/script/type/importmap), across different browsers.

Import maps are a standard web platform feature allowing developers to control how JavaScript modules are resolved, similar to server-side package managers. While widely supported in the latest versions of major browsers, older browser versions might lack native support for import maps or other newer module features that `es-module-shims` polyfills, such as using [multiple import maps](https://developer.mozilla.org/docs/Web/HTML/Reference/Elements/script/type/importmap#browser_compatibility) in the same document.

In your theme code, you can use features like `<script type="importmap">` tags and standard `<script type="module">` tags without needing to manage browser-specific compatibility concerns for module loading yourself. Shopify ensures this polyfill is included and will maintain it as long as necessary to support a reasonable range of browser versions used by buyers.

**Tip:**

If possible, rely on this platform-provided polyfill for import map functionality. Avoid loading a separate version of `es-module-shims` or similar polyfills, as this could lead to conflicts or unnecessary overhead.

---

#### Pagination limits

Shopify limits pagination of arrays of objects to 25,000 objects. Pagination deep into large arrays is resource intensive and can slow down other requests. To keep all requests performant a limit of 25,000 was put in place that balances performance with practical use-cases.

Pagination above 25,000 items suggest a more suitable design can be found to help buyers narrow down their search to a manageable amount of items before paging through all results. If you're finding yourself constrained by this limitation [see how you can add filters to your shop](https://help.shopify.com/en/manual/online-store/search-and-discovery/filters).

This limit is also enforced on count queries. Counts are accurate up to 25,000 items. For arrays with more items 25,001 is returned as the count signaling that there are more than 25,000 items in the array.

---

### Stylesheet content subsetting

> Fonte: https://shopify.dev/docs/storefronts/themes/best-practices/performance/stylesheet-subsetting

# Stylesheet content subsetting

Shopify automatically subsets CSS from `{% stylesheet %}` tags so that each storefront page only loads the styles it needs. Instead of bundling all `{% stylesheet %}` CSS from every theme file into a single payload, Shopify identifies which files are part of the page's render tree — the set of Liquid files (sections, blocks, and snippets) that are actually rendered on that page — and includes only their CSS.

This reduces the amount of CSS that browsers download and parse, which improves page load times for merchants and their customers.

---

#### How subsetting works

When a storefront page is rendered, Shopify determines which Liquid files are part of the page's render tree. Only the CSS from those files' `{% stylesheet %}` tags is included in the linked `styles.css` file.

For example, if `sections/collection.liquid` renders `snippets/product-card.liquid` using `{% render 'product-card' %}`, then both files' `{% stylesheet %}` CSS is included on any page that renders the collection section. The snippet's CSS is included because its parent (the collection section) is in the render tree.

##### What isn't affected

The following types of CSS aren't subject to subsetting:

* **Asset stylesheets**: CSS files in the `assets/` folder that are loaded through `{{ 'style.css' | asset_url | stylesheet_tag }}` continue to work as before. They're included based on where you reference them in your layouts and templates.
* **Inline styles**: Inline `style` attributes on HTML elements aren't affected.
* **HTML `<style>` tags**: CSS in `<style>` tags (not `{% stylesheet %}`) renders as-is with the HTML output.
* **CSS inside the liquid `{% style %}` tag**: CSS inside the liquid `{% style %}` tag is not affected.

---

#### Compatible and incompatible patterns

A theme is compatible with subsetting when each file's CSS classes are used only within that file or files it directly renders. Most themes that follow a co-located, component-scoped pattern for `{% stylesheet %}` tags are already compatible. The following examples show what works and what doesn't.

##### Compatible pattern: self-contained styles

CSS classes that are defined and used in the same file are always safe:

###### /sections/product.liquid

```liquid
{% stylesheet %}
  .product-title { font-size: 1.5rem; font-weight: bold; }
  .product-price { color: #333; }
{% endstylesheet %}


<div class="product-title">{{ product.title }}</div>
<div class="product-price">{{ product.price | money }}</div>
```

##### Compatible pattern: parent styles used by rendered children

CSS classes that are defined in a parent file and used by a rendered child through `{% render %}` are safe, because the parent is always in the render tree when the child is:

###### /sections/collection.liquid

```liquid
{% stylesheet %}
  .collection-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; }
  .collection-grid__item { border: 1px solid #eee; padding: 1rem; }
{% endstylesheet %}


<div class="collection-grid">
  {% for product in collection.products %}
    {% render 'product-card', product: product %}
  {% endfor %}
</div>
```

###### /snippets/product-card.liquid

```liquid
<div class="collection-grid__item">
  {{ product.title }}
</div>
```

##### Incompatible pattern: cross-file CSS dependency

A CSS class that's defined in one file's `{% stylesheet %}` tag but used in a different, unrelated file is incompatible. If the defining file isn't in the page's render tree, then the styles won't be included:

###### /sections/header.liquid

```liquid
{% stylesheet %}
  .site-banner { background: var(--color-accent); padding: 0.5rem 1rem; }
{% endstylesheet %}


<div class="site-banner">{{ section.settings.announcement }}</div>
```

###### /sections/footer.liquid

```liquid
<div class="site-banner">
  {{ section.settings.promo_text }}
</div>
```

In this example, `footer.liquid` uses `.site-banner` but doesn't define it. It relies on `header.liquid`'s `{% stylesheet %}` being on the same page. If a page doesn't render the header section, then the class won't be available, and the footer won't be styled correctly.

---

#### Checking your theme

The `ValidScopedCSSClass` check in Theme Check detects cross-file CSS dependencies. It's enabled by default in the recommended configuration.

Run Theme Check on your theme:

```bash
shopify theme check
```

The check reports warnings when a CSS class that's used in an HTML `class` attribute is defined in another file's `{% stylesheet %}` tag, and that file isn't a direct ancestor in the render tree. For example:

```
CSS class `site-banner` is defined in another liquid file's stylesheet tags
that isn't an explicit ancestor: `sections/header.liquid`
```

CSS classes defined in `assets/*.css` are allowlisted, so they won't trigger warnings when used in Liquid files.

---

#### Fixing flagged issues

There are a few approaches to fixing any classes that have been flagged by the Theme Check linter:

##### Move CSS to the file that uses it

If a class is used in one or a few specific files, then either add the class definition to each file's `{% stylesheet %}` tag, or define it once in a common parent.

##### Move CSS to a shared asset stylesheet

If a class is truly global and used across many unrelated sections (such as utility classes or shared typography), then move it to a `.css` file in the `assets/` folder and load it through `stylesheet_tag` in your layout:

###### /assets/global.css

```css
.site-banner { background: var(--color-accent); padding: 0.5rem 1rem; }
```

###### /layout/theme.liquid

```liquid
{{ 'global.css' | asset_url | stylesheet_tag }}
```

Asset stylesheets aren't subject to subsetting and are always available on every page that loads them.

---

#### Subsetting and the section rendering API

Subsetting also applies when sections are fetched dynamically. When you use the section rendering API to fetch a section, the response includes a `<style data-section-stylesheet>` tag containing the section's subsetted CSS:

```html
<section id="shopify-section-sections--28375442096184__featured_collection" class="shopify-section">
  <style data-section-stylesheet>
    .collection-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; }
  </style>
  <!-- section content -->
</section>
```

If you insert the full section response into the DOM, then the styles are included automatically. If you insert only a portion of the response, then you also need to extract the `<style data-section-stylesheet>` element and insert it into the DOM so the section's styles are applied.

---

## Accessibility best practices for Shopify themes

> Fonte: https://shopify.dev/docs/storefronts/themes/best-practices/accessibility

# Accessibility best practices for Shopify themes

When you create a theme, make design choices that help keep content accessible. An accessible theme is designed so that it can be used by everyone, including people who rely on [assistive technology](https://www.w3.org/WAI/perspective-videos/). Accessibility for your theme is essential to providing an inclusive experience for merchants and customers.

The accessibility best practices for Shopify themes were created with the [Web Content Accessibility Guidelines (WCAG)](https://www.w3.org/TR/WCAG21/) in mind.

**Note:** There are many factors to consider when creating an accessible theme. Following only the best practices on this page doesn't guarantee that your theme is completely accessible.

---

### Accessibility testing

You can test the accessibility of your theme by using tools such as:

* [Accessibility Insights for Web](https://accessibilityinsights.io/en/)
* [Lighthouse](https://developers.google.com/web/tools/lighthouse)
* [WAVE](https://wave.webaim.org/)

If you use a continuous integration (CI) process for your themes during development, then you can add a CI check to make sure that changes to your theme code don't have a significant negative impact on your accessibility score. You can do so using [the Shopify Lighthouse CI GitHub action](https://shopify.dev/docs/storefronts/themes/tools/lighthouse-ci), a Shopify-developed GitHub action that uploads your theme code to a benchmark shop and then measures and calculates your theme accessibility.

---

### Accessibility principles

When creating your theme, focus on the main principles of the WCAG 2.0 Guidelines:

* **Perceivable**: Information and UI components must be presentable to users in ways that they can perceive.
* **Operable**: UI components and navigation must be operable.
* **Understandable**: Information and the operation of the UI must be understandable.
* **Robust**: Content must be clear enough that it can be interpreted reliably by a wide variety of user agents, including assistive technologies.

The following sections provide a list of accessibility best practices for how merchants and customers interact with your theme.

---

### Keyboard and gesture controls

Merchants and customers who have visual or motor impairments might use a keyboard to navigate and complete tasks online. These users rely on a visual indicator to communicate where their keyboard's focus is on a web page. Your theme must allow for all links, buttons, dropdown navigation, and form controls to be controlled using a keyboard.

#### Keyboard support

* The focus indicator is visible and consistent on active elements. When navigating with either the mouse or the keyboard, the focus indicator is apparent on active elements.
* The keyboard focus order must match the DOM order. Focus should move from top to bottom and left to right.
* The focus style is visible on the desktop when using a keyboard.
* Your theme doesn't rely on a mouse hover action to be visible or accessible.
* The `Tab` key and `Shift` + `Tab` keys can be used to navigate your theme.
* No sudden changes of context when a part of your theme receives focus. For example, when navigating with a keyboard, focus must not switch to something else when a control receives focus.

#### Gesture support

* Zooming gestures, for example pinch to zoom, are always available.
* Any functionality that requires several fingers or complex gestures, for example navigating 3D models, should be available with a single tap or click.

---

### Page structure

Your theme must be built using valid HTML. You can validate the generated HTML using the [W3 HTML checker](https://validator.w3.org/nu/#textarea). The following sections provides best practices for specific elements of the page structure.

#### Global

* The page `lang` attribute is set on the `html` element to help screen readers pronounce content in the correct accent and dialect.
* The viewport zoom is enabled. Your theme shouldn't use the `maximum-scale` and `user-scalable="no"` attributes.
* Skip link is available and visible when focused to provide quick access to page content by skipping past common content such as headers. Your themes should include `tabindex="-1"` on the container for the main content to receive focus.
* The content flow is linear. Your themes uses no `tabindex` attributes values other than `0` or `-1` and no `autofocus` attribute. Positive `tabindex` values in use and autofocus take the power away from the user by forcing a specific focus order. Let the user discover page content organically.

#### Headings

* The HTML heading elements use heading markup. Your theme uses heading tags (`h1` to `h6`) to communicate the organization of the content on the page.
* The heading tags are used in sequence. Your theme shouldn't use headings for design but rather to set the logical order of content on the page.
* The `h1` element is used to identify the main topic of a page.

#### Navigation

* The navigation areas are wrapped with the `nav` HTML element.
* `aria-current` is used to communicate the current page when traversing links.
* `role="menu"` or `role="menuitem"` aren't used for navigation.

#### Drop-down menu navigation

* `aria-expanded` is used to communicate the state of collapsible navigation.
* `aria-controls` is used to convey to assistive technology that there's a visually-hidden container that the drop-down menu controls.
* `aria-current` is used to communicate the current location or page when traversing navigation items.
* `Enter` and `Space` keys are supported to open the drop-down menu. Your theme must keep focus on the launcher control. The `Tab` key moves focus to the first item in the drop-down menu.
* The `Esc` key is supported to collapse the drop-down menu and return focus to the launcher control.

#### Product information

* Product images include descriptive [alt text](https://ux.shopify.com/considerations-when-writing-alt-text-a9c1985a8204).
* Sale and regular prices are marked differently, both visually and by using markup for screen readers. Your theme must use visually-hidden text to help discern the regular price from the sales price.
* If your theme dynamically changes a product price and availability when different variants are selected, then the changes must also be communicated to screen readers.
* `aria-live` is used to communicate dynamic changes in the UI.

#### Controls

* The `a` element is used for links. Your theme should use links for navigation, loading a new page, or shifting keyboard focus from one element to another.
* The `button` element is used for on-screen actions such as launching a modal window and sorting a data table.
* The destination of your link must be clear from the text alone.
* Links that open a new window include a warning. Your theme should include a visual icon with alternative text to help screen reader and sighted, keyboard-only users understand that clicking the link opens a new window.

#### Tables

* The `table` element is used for tables data.
* The `caption` element is used to help assistive technology identify that a table is being read.
* The `th` element is used for headers with `scope` attributes.
* The `scope="col"` element is used for column headers, and `scope="row"` for row headers.

#### Forms

* All form fields include a label. Fields can use `aria-label`, the `.visuallyhidden` element, floating labels, or a visible label to label forms. Form inputs and controls have names that clearly state their purpose.
* Form inputs have labels with `for` attributes, including form labels in the theme settings.
* Required inputs have the `required` attribute.
* Fields use the `autocomplete` attribute. Auto-complete helps people fill in form fields by using the data stored in their browser.

##### Form errors

* Focus is placed on the feedback message. Any errors returned as a result of completing or submitting a form are communicated to screen readers where possible and as soon as possible.
* Error messages are clear and descriptive.
* The `aria-describedby` attribute is applied to `input` elements which reference the error text container.
* Notifications, error messages, success messages are announced aloud. Critical information is announced by screen readers using `aria-live`.

---

### Media

Media can be distracting, disruptive, or unexpected. All the media in your theme should adhere to the following best practices:

* Media doesn't autoplay.
* Media controls are marked up using native HTML elements. Make sure your theme has a toggle state for buttons and range input for sliders.
* Media can be paused using the `Space` key.

#### Images and icons

* All `img` elements must have an `alt` attribute. Without an `alt` attribute, screen readers announce the name and path of the image file.
* Product or content images feature `alt` text which describes the image for screen reader users.
* Decorative images use empty values for `alt` attributes. Use `<img src="/content/assets/images/…" alt="" />` to hide images and icons from screen readers.

#### Video

* Closed captions are available.
* Descriptive audio is available.
* If an auto-playing video is required, including videos in slideshows, the sound is muted.
* Videos with audio aren't visually obstructed.
* The `Space` key can be used to pause and play the video.

#### Audio

* Transcripts are available.
* Auto-playing audio can be paused.

---

### Color and contrast

When you add colors to your theme, make sure that all of your text is accessible to merchants and customers who are colorblind or have other visual impairments. These merchants and customers rely on adequate color contrast to visually differentiate one thing from another.

You can use an [online contrast ratio tool](https://contrast-ratio.com/) to check the contrast of the different parts of your store. The content in your theme should adhere to the following best practices:

* Text that is less than 24 pixels (regular) or 18.5 pixels (bold) has a contrast ratio of 4.5:1 against its background.
* Text that is 24 pixels (regular), or 18.5 pixels (bold) and larger, has a contrast ratio of 3.0:1 against its background.
* Icons have a contrast ratio of 3.0:1 against their background.
* Input element borders have a contrast ratio of 3.0:1 against their background.
* Color isn't the only indicator used to convey information.

---

### Dynamic components

Dynamic components such as slideshows, predictive search, modal windows, and tabs can be complex and difficult to navigate. Use elements that can be interpreted by screen readers, provide context, and include keyboard functionality.

#### Drawers and modals

* When a drawer or modal is opened, focus is moved to the element that labels the drawer or modal.
* Navigating with the keyboard stays within the open drawer or modal.
* The `Esc` key is supported to close drawers and modals, and returns keyboard focus to the launcher element.
* The role used to identify modals is `dialog`.

#### Slideshows

* Content that plays automatically in a slideshow can be paused or stopped.
* Content in a slideshow can be accessed through next and previous buttons.

---

### Touch screen and mobile devices

The main consideration for touch screens and mobile devices is to make sure that the merchant or customer can easily change the orientation and tap the target to navigate the content.

Touch targets on primary controls and links need to be at least 44 by 44 pixels. Primary touch targets include controls and links such as:

* Main menu links (regardless if first or third level)
* Submit buttons for any forms, such as contact forms, comment forms, search, and add to cart
* Menu buttons for carts and for hamburger menus
* Close buttons for modals
* Product page variants and options, such as color, size, and quantity

---

## Theme editor best practices

> Fonte: https://shopify.dev/docs/storefronts/themes/best-practices/editor

# Theme editor best practices

The [theme editor](https://shopify.com/admin/themes/current/editor) lets merchants easily customize their online store without touching code. It provides a visual interface for modifying themes, previewing changes, and publishing updates. Merchants use the editor to add, remove, and rearrange sections and blocks, adjust settings, and preview their store on multiple devices.

![The theme editor in the Shopify admin](https://shopify.dev/assets/assets/images/themes/theme_editor-fhUF7rbL.png)

As a theme developer, your goal is to build themes that integrate smoothly with the theme editor, providing merchants with a clear, intuitive, and powerful editing experience.

***

### Integrate sections and blocks with the theme editor

When merchants customize sections and blocks using the theme editor, content dynamically updates without reloading the entire page. To ensure a seamless editing experience, your theme should respond correctly to theme editor actions, such as adding, removing, selecting, or reordering elements. You can also detect when the theme editor or its visual preview mode is active, and adjust your theme's behavior accordingly.

Learn more about [integrating blocks and sections with the theme editor](https://shopify.dev/docs/storefronts/themes/best-practices/editor/integrate-sections-and-blocks).

***

### Integrate with the preview inspector

The preview inspector lets merchants quickly identify and edit sections and blocks directly from the theme preview. By properly integrating your theme with the preview inspector, you help merchants instantly see which settings affect specific elements. This integration streamlines the editing process and improves merchant confidence when customizing their store.

Learn more about [integrating with the preview inspector](https://shopify.dev/docs/storefronts/themes/best-practices/editor/preview-inspector).

---

### Integrate sections and blocks with the theme editor

> Fonte: https://shopify.dev/docs/storefronts/themes/best-practices/editor/integrate-sections-and-blocks

# Integrate sections and blocks with the theme editor

When users customize sections and blocks through the theme editor, their HTML is dynamically added, removed, or re-rendered directly onto the existing DOM, without reloading the entire page. However, any associated JavaScript that runs when the page loads won't run again.

Additionally, you must make sure that when a section or block is selected, that section or block becomes, and remains, visible while it's selected. For example, a slideshow section should scroll into view when the section is selected, slide to a selected block (slide), and pause while that block is selected.

To help identify theme editor actions like section and block selection or reordering, you can use the [JavaScript events](#javascript-events) emitted by the theme editor.

You might also want to prevent specific code from running in the theme editor. To do so, you can use Liquid and JavaScript variables for [detecting the theme editor](#detect-the-theme-editor).

> **Tip:**
> Section and block files must define presets in their schema to support being added to JSON templates using the theme editor. Files without presets should be included in the JSON file manually, and can't be removed using the theme editor.

---

#### JavaScript events

To identify sections and blocks, the theme editor looks for specific data attributes on the parent element of the associated section or block. Sections are wrapped by a Shopify-generated element which includes this attribute by default. However, blocks need to have the attribute added manually using the `shopify_attributes` property of the `block` object.

The theme editor emits section and block JavaScript events that bubble, and are not cancellable. Each event has a target (`event.target`), which is either the associated section or block element based on the data attribute mentioned above.

In addition to section and block events, the theme editor also emits events for when the theme editor preview inspector is activated or deactivated.

The following table outlines the events emitted by the theme editor:

| Type | Target | Detail | Trigger | Expected action |
| --- | --- | --- | --- | --- |
| `shopify:inspector:activate` | — | — | The theme editor preview inspector has been activated. | |
| `shopify:inspector:deactivate` | — | — | The theme editor preview inspector has been deactivated. | |
| `shopify:section:load` | section | `{sectionId}` | A section has been added or re-rendered. | Re-execute any JavaScript needed for the section to work and display properly, as if the page had just been loaded. |
| `shopify:section:unload` | section | `{sectionId}` | A section has been deleted or is being re-rendered. | Clean up any event listeners, variables, etc., so that nothing breaks when the page is interacted with and no memory leaks occur. |
| `shopify:section:select` | section | `{sectionId, load}` | The user has selected the section in the sidebar. | The theme editor automatically scrolls to the section, so make sure the section is in view, and stays in view, while selected. |
| `shopify:section:deselect` | section | `{sectionId}` | The user has deselected the section in the sidebar. | |
| `shopify:section:reorder` | section | `{sectionId}` | A section has been reordered. | |
| `shopify:block:select` | block | `{blockId, sectionId, load}` | The user has selected the block in the sidebar. | The theme editor automatically scrolls to the section, so make sure the block is in view, and stays in view, while selected. |
| `shopify:block:deselect` | block | `{blockId, sectionId}` | User has deselected the block in the sidebar. | |

In the table above, `blockId` represents the block ID, `sectionId` represents the section ID, and `load` indicates whether the event is being triggered by a section re-render, or a user selection. The value of `load` is `true` or `false`.

> **Tip:**
> Refer to the `theme-editor.js` asset in Dawn for examples of how the theme editor JavaScript events can be used.

---

#### Detect the theme editor

You can detect whether you're in the theme editor in [Liquid](#liquid) and [JavaScript](#javascript).

##### Liquid

The Liquid `request` object has a `design_mode` attribute that will return `true` if you're in the theme editor, and `false` if not. For example:

```liquid
{% if request.design_mode %}
<!-- This will only render in the theme editor -->
{% endif %}
```

##### JavaScript

In JavaScript, the global variable `Shopify.designMode` will return `true` if you're in the theme editor, and `undefined` if not. For example:

```js
if (Shopify.designMode) {
  // This will only render in the theme editor
}
```

---

#### Detect the theme editor preview inspector

In addition to the [JavaScript events](#javascript-events) that are triggered when the theme editor preview inspector is activated or deactivated, you can use the global variable `Shopify.inspectMode`. It will return `true` if the preview inspector is activated, and `false` if not. For example:

```js
if (Shopify.inspectMode) {
  // This will only execute if the theme editor preview inspector is currently activated
}
```

---

#### Detect the theme editor visual preview

You can detect whether you're in the theme editor visual preview using [Liquid](#liquid-1) and [JavaScript](#javascript-1). This mode is useful when customizing how sections and blocks render in the preview when merchants add new presets.

For example, you might expand an accordion section by default, ensuring the preview accurately represents what merchants will see in their template.

##### Liquid

The Liquid `request` object has a `visual_preview_mode` attribute that returns `true` if you're in the theme editor visual preview, and `false` if not. For example:

```liquid
{% if request.visual_preview_mode %}
  <!-- This will only render in the theme editor visual preview -->
{% endif %}
```

##### JavaScript

The global variable `Shopify.visualPreviewMode` will return `true` if you're in the theme editor's visual preview, and `undefined` if not.

For example:

```js
if (Shopify.visualPreviewMode) {
  // This will only execute inside the theme editor's visual preview
}
```

---

### Theme editor preview inspector best practices

> Fonte: https://shopify.dev/docs/storefronts/themes/best-practices/editor/preview-inspector

# Theme Editor Preview Inspector Best Practices

The [theme editor preview inspector](https://help.shopify.com/manual/online-store/themes/customizing-themes/edit#preview-inspector) allows you to navigate sections and blocks directly in the preview, and makes finding corresponding settings more intuitive.

The theme editor preview inspector draws outlines around sections and blocks to differentiate them. However, the preview inspector relies on coordinates returned by the browser's [`Element.getBoundingClientRect()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect) method to draw these outlines, which can highlight aspects of a theme's foundation that aren't normally visible.

Consider the following design guidelines to ensure that the outline of the section or block displays properly in the preview inspector:

#### Avoid using negative margins

You should avoid using negative margins to position blocks inside a section because the blocks can show outside of the section outline.

#### Avoid using padding for block spacing

To add space between blocks, you should use `margin` or `gap`, instead of `padding`. If you use `padding`, then the block outline might not display as expected.

#### Avoid using visually hidden elements

To hide an element, you should remove it from the DOM or use `display: none`, instead of visually hiding it. Visually hiding an element might result in an element outline with no element to interact with.

#### Disable fixed-position elements

You should disable fixed-position elements, such as sticky headers, when the preview inspector is enabled. Leaving these elements enabled can lead to a confusing experience.

**Tip:**

To learn more about detecting the theme editor preview inspector, refer to [Integrate sections with the theme editor](https://shopify.dev/docs/storefronts/themes/best-practices/editor/integrate-sections-and-blocks#javascript-events).

#### Section and block duplication

If you need to duplicate a section or block, then you should ensure that the element that you want the theme editor to recognize is the only one that includes a `data-shopify-editor` attribute. The theme editor relies on the `data-shopify-editor` attributes to identify sections and blocks, so duplicating them can lead to conflicts in identifying the correct element.

**Note:**

Sections use the `data-shopify-editor-section` attribute, and blocks use the `data-shopify-editor-blocks` attribute.

---

## Designing Shopify themes

> Fonte: https://shopify.dev/docs/storefronts/themes/best-practices/design

# Designing Shopify themes

A well-designed theme lets both merchants and customers know that you have their needs in mind. To help you to tackle the requirements of these two audiences, the design principles in this topic are split between the merchant and customer experiences.

Before you start designing your theme, make sure that you have a feedback loop between the theme designer and theme developer. Although there are several factors to consider, your theme shouldn't sacrifice performance at the expense of design. For more information about theme performance, refer to the [theme performance best practices](https://shopify.dev/docs/storefronts/themes/best-practices/performance).

For detailed considerations around making your theme modular and customizable using sections and blocks, refer to our [best practices](https://shopify.dev/docs/storefronts/themes/best-practices/templates-sections-blocks) for using sections and blocks.

***

### Design principles for the merchant experience

When you're creating your theme, there are design considerations that are specific to the merchant experience. For example, you might want to design a scalable theme that takes into account how your merchant's inventory will grow.

#### Purposeful

A purposefully-designed theme considers and balances the following key factors:

* Conversion

* Purchasing decisions

* Brand expression

To create a purposeful theme, do the following:

* Design sections and blocks that are tailored to your target audience. For example a theme optimized for merchants selling apparel can offer a size chart block in the main section of their product page template.

* Create different sections for each template to showcase different customer experiences. For example, a theme might include an upsell section designed specifically for the cart template.

* Define your segment based on the target audience, inventory size, and customer experience. Build your theme-specific principles accordingly.

* Build a strong, opinionated theme art direction and make sure you balance those design decisions with ecommerce best practices.

* Build variations of the same component, rather than providing two components that achieve the same purpose.

#### Easy to set up

A theme that's easy to set up is configured to avoid merchant confusion during the customization process and reduces overhead before launching.

To create a theme that's easy to set up, do the following:

* Keep theme settings to the minimum that's required to empower the majority of merchants. Avoid niche settings and settings for edge cases.

* Consider [blocks](https://shopify.dev/docs/storefronts/themes/best-practices/templates-sections-blocks) to improve a section's usability. For example, you can group settings by component to facilitate content reordering and content input.

* Create theme empty states and placeholders that leverage existing store data to provide a ready-to-launch look and feel wherever possible.

#### Antifragile

An antifragile theme has components that are designed to be robust and to scale with any type of content.

To create an antifragile theme, do the following:

* Make sure your components don't require perfect assets and image ratios to look professional. For example, product cards should look clean and cohesive, even with inconsistent product images.

* Use an atomic design approach to theme components. Atomic design systems deliberately set order and hierarchy. When creating your theme, make sure to pay attention to the semantic order of elements.

* Provide a robust layout no matter how much content is added, even if content is missing.

* Include a robust font system where the hierarchy scales for different scenarios. For example, consider using a shorter text for labels on product cards and a longer text for promotions.

* Make sure font styles are associated with the right elements, such as associating all headings with the same font setting, for consistency.

* Apply your [color scheme](https://shopify.dev/docs/storefronts/themes/best-practices/design/color-system) consistently across the theme to always provide an optimal contrast for legibility and accessibility.

* Make sure that no critical action can be obscured by apps that add a floating component to the page, such as chat apps and cookie banners.

#### Flexible

A flexible theme offers flexibility only where it matters most for merchants to express their brand and tell their story beautifully.

To create a flexible theme, do the following:

* Make sure that all the flexibility provided in the theme is predictable. A merchant's actions should lead to expected results. Avoid any magic settings that remove control from merchants.

* Provide flexibility in your theme settings that aligns with best practices for SEO, accessibility, layout responsiveness, content management, and translation and localization. For example, provide a text field along with an image setting to allow merchants to add an image with text.

* Avoid replacing platform functionality with theme settings.

* Avoid providing workarounds that go beyond displaying and organizing content.

#### Extensible

An extensible theme helps merchants extend the functionality of their stores without sacrificing the look and feel of their stores.

You can extend a merchant's theme by using [metafields, theme blocks, and app blocks](https://shopify.dev/docs/storefronts/themes/best-practices/templates-sections-blocks). For example, you can [add support for app blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks) in sections that have clear use cases for layering additional conversion tools or purchase decision factors.

***

### Design principles for the customer experience

When you're creating your theme, there are design considerations specific to the customer experience. For example, you might want to design an expressive theme that helps merchants share their story with customers.

#### Accessible

In order to submit your theme to the Shopify theme store, you're required to meet accessibility standards. For more information about theme accessibility, refer to the [theme accessibility best practices](https://shopify.dev/docs/storefronts/themes/best-practices/accessibility).

To create an accessible theme, do the following:

* Use the [color system best practices](https://shopify.dev/docs/storefronts/themes/best-practices/design/color-system) to build a robust color palette for your theme.

* Make sure you design components respect the DOM order and the elements tab order.

The [Polaris accessibility considerations](https://polaris.shopify.com/foundations/accessibility) can be used to design your theme.

#### Expressive

An expressive theme includes sections that let merchants tell their stories: who they are, what value they bring, and how they differ from other merchants. For example, you might include a section to display lifestyle imagery or video, or a section that displays either short or long text in an appealing layout.

#### Intuitive

An intuitive theme facilitates the flow of product discovery and leads customers to conversion.

To create an intuitive theme, do the following:

* Tailor the product discovery experience to your target segment. For example, consider inspirational flows for the fashion industry, where these flows account for a large proportion of conversion (cross-selling patterns).

* Design a prominent and discoverable navigation and intuitive menu interactions

* Include entry points, such as a featured collection or a highlighted products section, that lead further down the purchase consideration funnel.

* Design each product page with a prominent title, price, and buy button. Make sure the description and secondary information are easily discoverable.

* Select design patterns that build trust with customers. Prioritize customers' interests first, to create long term customer relationships, and avoid dark patterns.

* Test your theme with real users. When testing, include a decision-making and purchase scenario for users to complete.

#### Cohesive

A cohesive theme articulates the merchants brand in a unified voice as customers navigate the store. The scale, spacing, weight of components, layouts, and pages in your theme should be consistent.

#### Efficient

An efficient theme provides a fast and clear path to checkout.

To create an efficient theme, do the following:

* Limit the number of steps required to make a purchase. For example, reduce steps by enabling accelerated checkout by default.

* Design navigation and interaction patterns with immediate feedback that feels performant.

* Optimize layouts for a powerful mobile-first experience.

* Avoid elements that require additional cognitive load to understand. For example, use standard, well-established iconography for the menu and user accounts.

---

### Color system best practices

> Fonte: https://shopify.dev/docs/storefronts/themes/best-practices/design/color-system

# Color system best practices

One of the most important components of designing a visually appealing, functional, and accessible theme is color. Not only does a well-designed color system reinforce a merchant's branding, it has the power to enhance and direct the user's experience.

When designing the color system for your theme, consider both the overall look and feel, and the interplay or relationship between elements. There should be an established hierarchy between elements. For example, emphasize a call-to-action, and provide adequate color contrast between foreground and background elements. This sets merchants up for success by providing seamless and accessible experiences for their customers.

To help make your theme's color system more robust and intuitive for merchants to use, you can use color schemes.

---

#### Color schemes

Color schemes are a theme setting that let you group together elements and their respective colors, in a visually representative way to merchants. You can create an infinite amount of color schemes to offer merchants more flexibility and variety for their storefronts.

When designing color schemes for your themes, include elements that are used throughout the theme. Consider areas where merchants would benefit from being able to change colors in one shared place.

**Example**: Your color scheme includes text, background, link and button text. You have a specific section where users can add a grid of icons to represent product features. You can allow merchants to use a bespoke color for these icons if you so choose.

##### Number of colors

While you could be tempted to convey that your theme is highly customizable to merchants, we recommend not offering unnecessary granular colors to avoid overwhelming your color system and merchants' experience. Prioritize optimizing for when multiple objects can wear the same color reference of a scheme or a bespoke color.

##### Color scheme diversity

Create color schemes that are distinct enough to provide variety, but similar enough to maintain a good visual balance throughout the design.

---

#### Color scheme roles

A color role is a designated purpose or function assigned to a specific color within a design system. While there are specific roles that can be associated with certain colors, such as background, text, and buttons, remember that a color scheme isn't limited to these roles. Other important parts of the theme, such as other accent colors, could also be considered when defining a color scheme.

There are [10 required roles](https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings#role) that can be reliably used by apps and other parts of the Shopify ecosystem. They are used to:

* Provide a predictable mapping to represent the scheme preview. This is what provides users the visual cue of what color scheme they are selecting.

* Provide a predictable mapping so that other parts of the Shopify ecosystem, such as apps, can understand what colors are in a given theme in a predictable way.

These roles are the most commonly used color relationships we observe in themes and apps. While auditing our ecosystem, we found that links are used more often than dividers. Dividers are often derived from other existing colors, and don't necessarily warrant their own role.

![Dawn color role settings](https://shopify.dev/assets/assets/images/themes/color-scheme/color-system-roles-e19daCrT.png)

---

#### Naming conventions

Use the following naming conventions for color schemes:

* **Roles**: Use semantically predictable roles. For example, an app shouldn't rely on guesswork to understand the intended application of a color.
* **Scheme's color**: Color scheme labels can be named however works best for your theme. The labels should be clear and descriptive, making it easy for users to understand the purpose of each color picker.

---

#### Additional colors outside color schemes

Color schemes can be used in conjunction with the existing color setting type. If you want to add more colors for the design of your theme, then you can create new color groups. If the colors don't impact elements that require an accessible contrast ratio, then you aren't required to include them in the color scheme definition.

![Theme color settings](https://shopify.dev/assets/assets/images/themes/color-scheme/theme-color-settings-ro0hMW_r.png)

---

#### Hardcoded colors

You can use hardcoded colors, but you shouldn't apply hardcoded colors to elements that require an accessible contrast ratio.

![Hardcoded color risk example](https://shopify.dev/assets/assets/images/themes/color-scheme/hardcoded-colors-OgvIBroW.png)

![Hardcoded color risk example continued](https://shopify.dev/assets/assets/images/themes/color-scheme/hardcoded-colors2-CMFwsYIw.png)

---

## Working on themes attached to merchant stores

> Fonte: https://shopify.dev/docs/storefronts/themes/best-practices/merchant-stores

# Working on themes attached to merchant stores

When you're developing or customizing a theme for a merchant, you should keep the following best practices in mind.

---

### Access

You might want to access a client's store to perform specific tasks related to building a theme. For example, you can access a client's store to test a theme using a merchant's data.

To access a client's store, you can use one of the following accounts:

* **Collaborator account**: You can use collaborator accounts to access your clients' stores directly through your own Partner Dashboard or using the Shopify app. Collaborator accounts give you access to only the sections of a store that your client wants you to access, and don't count towards a store's staff limit. Any stores that you have access to using a collaborator account are labeled as **Managed** stores in your Partner Dashboard. [Learn how to send a collaborator request to a merchant](https://help.shopify.com/partners/dashboard/managing-stores/request-access).

* **Staff account**: If you need to do something that can't be accomplished with a collaborator account, then you can request that a merchant create a [staff account](https://help.shopify.com/manual/your-account/staff-accounts) for you to use. For example, you might need to access the Shopify admin on a mobile device to test an app.

  Asking a merchant for their password, or using a merchant's credentials to access their store, is prohibited.

#### Accounts and Shopify tools

You can't use a collaborator account to set up the [Shopify GitHub integration](https://shopify.dev/docs/storefronts/themes/tools/github).

If you want to set up the Shopify GitHub integration, then you can request that a merchant create a staff account for you to use.

Asking a merchant for their password, or using a merchant's credentials to access their store, is prohibited.

---

### Version control

If you have an ongoing relationship with a merchant, then you might want to connect their theme to version control using the Shopify GitHub integration. Before you do this, you should discuss whether the merchant or your partner organization controls or maintains the GitHub repository. You might [transfer the repository](https://docs.github.com/en/github/administering-a-repository/managing-repository-settings/transferring-a-repository) as a part of the final package that you deliver to the merchant so they or other developers can work on it.

---

## Version control for Shopify themes

> Fonte: https://shopify.dev/docs/storefronts/themes/best-practices/version-control

# Version Control for Shopify Themes

When you build a Shopify theme, you can introduce optional version control to track and manage changes to your theme code. Version control helps you to manage changes to your code over time.

The [Shopify GitHub integration](https://shopify.dev/docs/storefronts/themes/tools/github) lets you add version control to themes in a Shopify store. When a theme is connected to a GitHub repository using the Shopify GitHub integration, any changes that a merchant makes to the theme are tracked as commits to the branch.

You should consider the following factors when planning a version control strategy for a Shopify theme:

* **Branch organization and publishing strategy** - Because the GitHub integration lets you develop features and campaigns using branches, you should consider how you want to organize your branches and manage your published theme.
* **Managing source and compiled code** - The Shopify GitHub integration only supports the [default Shopify theme folder structure](https://shopify.dev/docs/storefronts/themes/tools/github#repository-structure). If you use a build pipeline to [transform](https://shopify.dev/docs/storefronts/themes/best-practices/file-transformation) your theme's source code into compiled code, then you need to choose an approach that allows you to use a build pipeline, but also lets you track and manage changes to compiled code using the GitHub integration.

---

### Branch Organization

If you're using the Shopify GitHub integration to develop your theme, then consider connecting your `main` or `master` branch to your store and then publishing the resulting theme. This ensures that the published theme is always up to date with features as they are merged to the main or master branch.

For events like sales, consider using non-main branches to customize your theme. Themes connected to these branches can be published temporarily. After the event is over, you can republish the theme that's connected to your main branch.

If you use a build pipeline to transform your code, then you should create a specific deploy branch that acts as your main production code branch, and then deploy the code that you compile off of master to this branch. To learn more, read about managing source and compiled code in the next section.

---

### Managing Source and Compiled Code

You might use a build pipeline to [transform](https://shopify.dev/docs/storefronts/themes/best-practices/file-transformation) your theme's source code into compiled code that's optimized for browser runtime. Because the Shopify GitHub integration supports [only branches that match the default Shopify theme folder structure](https://shopify.dev/docs/storefronts/themes/tools/github#repository-structure), you need to organize your code so that a branch that's connected to Shopify matches this structure. For example, a branch that's connected to Shopify can't contain `src` and `dist` folders.

You can choose from several strategies to manage both your source and compiled code in version control:

* [Use separate repositories for source code and compiled code](#use-separate-repositories-for-source-code-and-compiled-code)
* [Separate source code and compiled code using branches](#separate-source-code-and-compiled-code-using-branches-recommended) (recommended)
* [Mix source code and compiled code](#mix-source-code-and-compiled-code)
* If you don't want to track your theme code using the Shopify GitHub integration, then you can also choose to manage [only your source code](#manage-only-your-source-code-in-version-control) in version control.

**Tip:**

Instead of using a build pipeline, you can also use Shopify-provided just-in-time file transformations for certain file transformation tasks. This strategy lets you organize your theme code using the default folder structure. To learn more, refer to [Just-in-time file transformations](https://shopify.dev/docs/storefronts/themes/best-practices/file-transformation#just-in-time-file-transformations).

#### Advantages to Managing Your Source and Compiled Code Using Version Control

Managing your source and compiled code using version control has the following advantages:

* You can leverage common build tools such as Webpack, Rollup, and PostCSS.
* Files can be incrementally built on the developer's machine, which allows for live previews of changes made to source code.
* Changes to compiled code via Shopify can be easily identified.
* You can push changes to compiled code to the store using [the Shopify GitHub integration](https://shopify.dev/docs/storefronts/themes/tools/github).

However, using this model, changes made to compiled code need to be manually backfilled into the source code.

#### Use Separate Repositories for Source Code and Compiled Code

A developer can have one repository that contains their source code and build tools, and another repository that contains a versioned representation of their compiled code.

##### Advantages

* Using separate repositories is easy to adopt when moving from a [source-only versioning model](#manage-only-your-source-code-in-version-control). You can continue to push compiled code directly to a store, and then use [the Shopify GitHub integration](https://shopify.dev/docs/storefronts/themes/tools/github) to track changes to your compiled code over time.

##### Disadvantages

* You need to work across two repositories for a single theme, which can make [backfilling](https://shopify.dev/docs/storefronts/themes/best-practices/file-transformation#backfilling-changes-to-compiled-code) source code more complex.
* Static files that aren't impacted by file transformations are copied between repositories, resulting in extra maintenance and backfilling.

#### Separate Source Code and Compiled Code Using Branches (Recommended)

You can publish the compiled code for a theme in a separate branch from the source code. The contents of this branch are compatible with the Shopify theme platform and Theme Check.

One way to accomplish this is by using `git subtree`. Using the `subtree` command, you can extract your compiled code to a branch that can then be safely connected to a theme.

##### Advantages

* There is a distinct location within your repository for your production code.
* The commit history of the branch is clean. The only commits in the production branches are updates to production code. Changes to source code stay in their own branches.

##### Disadvantages

* Previewing the contents of a working branch requires another branch that contains the "preview" production code. Managing branches might become cumbersome.
* Static files that aren't impacted by file transformations reside in separate branches, resulting in extra maintenance and backfilling.

#### Mix Source Code and Compiled Code

You can mix compiled code files within the same folder structure as the source code. For example, inside of an `assets` folder, you can add a `main.js` source file and a compiled `main.min.js`.

##### Advantages

* Mixing source and compiled code minimizes the number of compiled files to only those that need to be compiled. This means that a merchant's changes to non-compiled files don't need to be backfilled or backported to your source code.

##### Disadvantages

* Compiled code might be hard to identify, and merchants might edit it directly.
* If edits are made to compiled code, then they need to be backfilled to avoid being lost the next time the code is compiled from its source.

#### Manage Only Your Source Code in Version Control

You can choose to commit only your source code to version control, and then deploy compiled code directly to a store when you want to create a release. Deployment can be done manually from a developer's machine using [Shopify CLI](https://shopify.dev/docs/storefronts/themes/tools/cli/cli-2/commands), or automated using continuous integration.

##### Advantages

* This approach is well supported in the Shopify theme developer community.
* It can leverage common build tools such as Webpack, Rollup, and PostCSS.
* Files can be incrementally built on the developer's machine, which allows for live previews of changes made to source code.

##### Disadvantages

* Because the repo only contains source code that isn't compatible with the Shopify theme platform, this method isn't compatible with [the Shopify GitHub integration](https://shopify.dev/docs/storefronts/themes/tools/github).
* Compiled code isn't version controlled, which makes tracking changes difficult. You need to manually identify changes to the compiled code, and then backfill your source code so that changes persist the next time the code is compiled and the theme is overwritten.

---

## File transformation best practices for Shopify themes

> Fonte: https://shopify.dev/docs/storefronts/themes/best-practices/file-transformation

# File transformation best practices for Shopify themes

File transformations improve the developer experience by letting you write and maintain code using your preferred strategies and build tools, and ship compiled code that is optimized for browser runtime.

For example, you might want to divide your stylesheets into multiple files, each scoped to a particular UI element, which makes them easier to maintain. However, loading a large number of small stylesheets is slower than loading one or two larger stylesheets. You can use file transformations to automate the process of combining these smaller, scoped stylesheets into fewer, larger bundles.

You can transform files as part of a build process, and then upload your compiled code as a theme that can be accessed in the Shopify admin.

Below are some examples of file transformations that theme developers might want to perform:

| File transformation | Benefit |
| --- | --- |
| Custom file structure > Shopify theme file structure | Code maintenance flexibility |
| SCSS > CSS | Write in SCSS, output Shopify-compatible CSS |
| SVG > snippet | Include SVGs inline in HTML |
| [PostCSS](https://github.com/postcss/postcss) transformations (e.g. Autoprefixer, cssnano, tailwindcss) | Linting, variables, transpiling, browser compatibility |
| Section folders > section files | Build sections in separate Liquid, JS, CSS, and JSON files |
| Automated calculation and inlining of critical styles | Avoid load-blocking CSS resources |
| Optimized JavaScript bundles | Reduced load times, smaller file sizes |
| JavaScript, CSS, and HTML minification | Reduced load times, smaller file sizes |

If you want to perform transformations on your files, then you need to decide how you want to manage both the source code and the transformed, or compiled, code. To learn about the options, and which options can be used with Shopify tools, refer to [Version control best practices for Shopify themes](https://shopify.dev/docs/storefronts/themes/best-practices/version-control).

You can also consider using [just-in-time (JIT) file transformations](#just-in-time-file-transformations) to reduce the need to track changes to compiled code. JIT transformations can deliver optimized dependencies and resources at runtime, allowing for a unified code base that doesn't need to be backfilled.

---

### Compiled code and merchant or app customizations

After a theme is uploaded to Shopify, merchants can customize it using the [theme editor](https://shopify.dev/docs/storefronts/themes/tools/online-editor) or the [code editor](https://shopify.dev/docs/storefronts/themes/tools/code-editor). [Apps](https://shopify.dev/docs/apps/build) might also change the theme code through the `Asset` [REST Admin API resource](https://shopify.dev/docs/apps/build/online-store/asset-legacy). This can lead to situations where compiled code has been altered, but source code hasn't been updated.

You might need to identify changes to the compiled code, and then manually backfill those changes into your source code so the changes persist the next time the code is compiled. This is a particular risk if you are a Partner or merchant developer who performs ongoing customizations to a merchant's theme. You should consider the impact of merchant or app customizations when planning your file transformation and [version control](https://shopify.dev/docs/storefronts/themes/best-practices/version-control) strategy.

**Tip:**

If you perform file transformations using [Just-in-time services](#just-in-time-file-transformations), then you don't need to backfill changes.

#### Backfilling changes to compiled code

When a change is made to a compiled file and the theme is [connected to GitHub](https://shopify.dev/docs/storefronts/themes/tools/github), then the change is added to the theme's GitHub repo as a commit. You can use this commit to identify and backfill merchant changes.

The following is an example of identifying and backfilling a change to a theme that's connected to version control using [the Shopify GitHub integration](https://shopify.dev/docs/storefronts/themes/tools/github).

##### Step 1: The developer writes source code and compiles it

You create the following scoped JavaScript resources for a theme.

**assets/scopeA.js**

```js
export console.log('ScopeA JS is running!');
```

**assets/scopeB.js**

```js
export console.log('ScopeB JS is running!');
```

**assets/index.js**

```js
import './scopeA.js'
import './scopeB.js'
```

These three files are bundled for optimized delivery, resulting in the following file:

**assets/index.bundle.js**

```js
console.log('ScopeA JS is running!');
console.log('ScopeB JS is running!');
```

These files are all committed to the GitHub repo, and then `index.bundle.js` is synced with the store using [the Shopify GitHub integration](https://shopify.dev/docs/storefronts/themes/tools/github).

`index.bundle.js` is called inside of a Liquid template:

**templates/index.liquid**

```liquid
<script src="{{ 'index.bundle.js' | asset_url }}"></script>
```

This store or theme is handed off to the merchant.

##### Step 2: The merchant edits compiled code

When the merchant starts using the theme, they need to make a change to the compiled JS bundle using the code editor in the Shopify admin:

**assets/index.bundle.js**

```js
console.log('ScopeA JS is running!');
console.log('ScopeB JS is running!');
+ console.log('ScopeB is way cooler than ScopeA');
```

This change is synced to the theme's associated GitHub repo as a commit.

##### Step 3: The developer identifies changes to compiled code and backfills them

When the merchant contacts you to add another feature to your theme, you can see the commit from the Shopify admin in the repo.

Because the change was made to the compiled `index.bundle.js`, this change will disappear when the file is recompiled, unless a corresponding change is made to the source files.

To make sure changes made to compiled code persist after the code is recompiled, you can manually backport the change into the source code. In this case, you can modify `index.js`:

**assets/index.js**

```js
import './scopeA.js'
import './scopeB.js'
+ console.log('ScopeB is way cooler than ScopeA');
```

---

### Just-in-time file transformations

Many transformations are one-way: you can transform source code into compiled code, but you can't transform compiled code into source code. Most code management strategies for Shopify themes involve tracking changes to compiled code and backfilling source code. This is because the code a merchant sees is often the result of a file transformation, and a merchant might edit the code or install code-injecting apps as a part of running a store.

You can use just-in-time (JIT) file transformations for some of your common file transformation tasks. JIT transformations move the functionality of installed developer tools to on-demand services that can generate an optimized runtime file from source code.

When you remove the need to perform certain types of file transformations, you can further reduce or even eliminate the number of compiled files that you need to create, track and maintain. Merchants can edit source code rather than compiled code, allowing for a unified code base that doesn't need to be backfilled.

Common uses for JIT transformations include JavaScript minification, CSS optimization and minification, and third-party dependency management.

#### Advantages

* This method is compatible with the [Shopify GitHub integration](https://shopify.dev/docs/storefronts/themes/tools/github).
* Maintenance is performed by service owners.
* This method works within Shopify's supported [theme file structure](https://shopify.dev/docs/storefronts/themes/architecture).
* Merchants can work on source files, resulting in reduced backfilling.

#### Shopify minification

Shopify automatically minifies CSS and JavaScript files. For instance, you can include a CSS file such as `main.css` in your asset folder. Shopify compiles and sends a minified version of it, which updates every time the source file changes.

---

## Avoid deceptive coding practices

> Fonte: https://shopify.dev/docs/storefronts/themes/best-practices/deceptive-code

# Avoid deceptive coding practices

Deceptive development practices are prohibited on Shopify's platform. Shopify expects app developers to act with integrity and in the best interests of app users. Developers should regularly review, and remain compliant with, the [Partner Program Agreement](https://www.shopify.com/partners/terms) and Shopify's [API Terms of Service](https://www.shopify.com/legal/api-terms).

The following sections describe some of the development practices that Shopify considers deceptive. Any developer that uses these practices, or any other practices considered by Shopify to be deceptive or harmful to merchants, is subject to Partner governance action.

---

### Obfuscating code

Don't obfuscate your code. Obfuscation means changing simple, straightforward code into code that is difficult to understand. Obfuscated code obscures the intended behaviour of the code, usually with the intention of hiding that behavior from users. In addition, obfuscation techniques might also hinder the performance of a user's site. There is no legitimate reason for developers to inject obfuscated code into themes.

---

### Manipulating search engines

Themes shouldn't include any code that targets search engines to misrepresent the site content. One example of this type of deceptive coding practice is cloaking. Cloaking refers to the use of code that presents different content to search engines than is presented to users.

Developers should never use any code that attempts to trick search engines for any purpose, including increasing page speed scores.

---

## Pagine non catturate

Nessuna. Tutte le pagine elencate nella sidebar della sezione *Best practices* sono state catturate. Nota: lo slug della sezione "Theme editor" non è `theme-editor` (404) ma `editor`; verificato e usato lo slug corretto.
