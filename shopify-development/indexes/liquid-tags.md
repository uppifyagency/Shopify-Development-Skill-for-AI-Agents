# Liquid Tags — index (28)

How to use: find your tag, then open `reference/08-liquid-tags.md` and Grep the heading `## <tag>` for full syntax, parameters, and examples.

| Tag | Category | Syntax | Purpose |
|-----|----------|--------|---------|
| `if` | conditional | `{% if condition %}…{% endif %}` | Renders an expression if a condition is true (supports `elsif`/`else`) |
| `unless` | conditional | `{% unless condition %}…{% endunless %}` | Renders an expression unless a condition is true (inverse of `if`) |
| `case` | conditional | `{% case var %}{% when v %}…{% else %}…{% endcase %}` | Renders an expression depending on the value of a variable (switch) |
| `form` | html | `{% form 'form_type' %}…{% endform %}` | Generates an HTML `<form>` with required hidden inputs for a Shopify endpoint |
| `for` | iteration | `{% for item in array %}…{% endfor %}` | Iterates over an array (supports `limit`/`offset`/`reversed`/range; `forloop` object) |
| `cycle` | iteration | `{% cycle 'a', 'b', … %}` | Outputs strings one per iteration of a `for` loop (e.g. odd/even patterns) |
| `tablerow` | iteration | `{% tablerow item in array %}…{% endtablerow %}` | Generates HTML table rows for each item (supports `cols`; `tablerowloop` object) |
| `break` | iteration | `{% break %}` | Stops a `for` loop from iterating |
| `continue` | iteration | `{% continue %}` | Skips to the next iteration of a `for` loop |
| `paginate` | iteration | `{% paginate array by page_size %}…{% endpaginate %}` | Splits an array across multiple pages (needed beyond the 50-iteration `for` limit) |
| `comment` | syntax | `{% comment %}…{% endcomment %}` / `{% # … %}` | Prevents an expression from rendering or output (block or inline comment) |
| `doc` | syntax | `{% doc %}…{% enddoc %}` | Documents template elements with LiquidDoc annotations; content is not rendered |
| `echo` | syntax | `{% liquid echo expression %}` | Outputs an expression (like `{{ }}`) usable inside `liquid` tags; supports filters |
| `liquid` | syntax | `{% liquid expression %}` | Runs a block of Liquid without per-tag delimiters (one tag per line) |
| `raw` | syntax | `{% raw %}…{% endraw %}` | Outputs Liquid code as literal text instead of rendering it |
| `content_for` | theme | `{% content_for 'blocks' %}` / `{% content_for 'block', type:, id: %}` | Creates an area to render theme blocks (dynamic) or a single static block |
| `javascript` | theme | `{% javascript %}…{% endjavascript %}` | Holds JavaScript for a section/block/snippet (one per file; no Liquid inside) |
| `layout` | theme | `{% layout name %}` / `{% layout none %}` | Specifies which layout file to use (defaults to `theme.liquid`) |
| `render` | theme | `{% render 'filename', var: value %}` | Renders a snippet/app block with isolated scope (supports `for`/`with`/`as`) |
| `section` | theme | `{% section 'name' %}` | Renders a section statically |
| `sections` | theme | `{% sections 'name' %}` | Renders a section group in the layout |
| `style` | theme | `{% style %}…{% endstyle %}` | Generates an HTML `<style data-shopify>` tag (live-updates color settings) |
| `stylesheet` | theme | `{% stylesheet %}…{% endstylesheet %}` | Holds CSS for a section/block/snippet (one per file; no Liquid inside) |
| `assign` | variable | `{% assign name = value %}` | Creates a new variable of any basic type, object, or property |
| `capture` | variable | `{% capture name %}…{% endcapture %}` | Creates a new variable from a captured string built with Liquid logic |
| `increment` | variable | `{% increment name %}` | Creates/increments a counter (starts at 0, +1 per call; shares with `decrement`) |
| `decrement` | variable | `{% decrement name %}` | Creates/decrements a counter (starts at -1, -1 per call; shares with `increment`) |
| `include` | deprecated | `{% include 'filename' %}` | Renders a snippet with shared scope — deprecated, replaced by `render` |

Totale: 28 tag
