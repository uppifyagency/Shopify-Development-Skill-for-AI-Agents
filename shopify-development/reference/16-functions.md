# 16. Shopify Functions

Shopify Functions let developers customize the backend logic of Shopify. They run custom code during key purchase flows — discounts, cart transformation, checkout validation, delivery and payment customization, fulfillment, and order routing — by injecting WebAssembly (Wasm) modules into well-defined extension points called **targets**. Each function reads a JSON input (produced by a GraphQL input query you define) and returns a JSON output of declarative operations for Shopify to execute.

This chapter is a faithful extraction of the Shopify Functions documentation. It is organized in two parts:

1. **Overview & infrastructure** — how functions work, language support (Rust / JavaScript / Wasm), input/output and input queries, metafields and variables, network access, configuration and versioning, limits, testing & debugging, monitoring/errors, and migrating from Shopify Scripts.
2. **One section per function type** — Discounts, Cart Transform, Cart & Checkout Validation, Delivery Customization, Payment Customization, Fulfillment Constraints, Order Routing (Location Rule), Local Pickup Delivery Option Generator, and Pickup Point Delivery Option Generator — each with its guide context plus the API reference (targets, input, output operations, and verbatim Rust/JS/GraphQL/JSON examples).

> Note on the schema reference pages: each Function API reference includes an enormous field-by-field listing of its `Input` GraphQL object (cart, buyer identity, lines, localization, shop, metafields, etc.). For the discount and cart-transform APIs the full input schema is reproduced; for the other APIs the input schema is condensed to its top-level fields (the nested fields follow the same `Cart`/`BuyerIdentity`/`ProductVariant`/`Metafield` shapes documented under the Discount API). All targets, output operation types, notes, and code examples are preserved verbatim.

---

## Overview & infrastructure

### About Shopify Functions

> Fonte: https://shopify.dev/docs/apps/build/functions

#### Functions availability

* Stores on any plan can use public apps distributed through the Shopify App Store that contain functions. Only stores on a Shopify Plus plan can use custom apps that contain Shopify Function APIs.
* Some Shopify Functions capabilities are available only to Shopify Plus plan stores. See Shopify Function APIs for details.

Shopify Functions allow developers to customize the backend logic of Shopify. This guide introduces how Shopify Functions work and the benefits of using Shopify Functions.

#### How Shopify Functions work

Function Targets inject code into the backend logic of Shopify. Shopify invokes a function which has been configured for a target:

* **Function input:** The function input is a JSON object which is the result of a GraphQL input query you define. Input queries allow you to select the specific data you need for your function, such as cart line product data or metafields.

* **Function logic:** The function logic is written in any language that can compile a WebAssembly module which meets function requirements. Function templates and client libraries are available for Rust and JavaScript.

  **Caution:** Shopify strongly recommends Rust as the most performant language choice to avoid your function failing with large carts.

* **Function output:** The function output is a JSON document that describes the operations you'd like Shopify to carry out.

GraphQL schemas provided by Shopify specify the targets, available inputs, and expected outputs for a Functions API.

#### Lifecycle of a Shopify Function

* **App developers** create and deploy apps that contain functions.
* **Merchants** install the app on their Shopify store and configure the function. An API call is made with the function configuration.
* **Customers** interact with a Shopify store and **Shopify** executes the function.

For example, an app developer might create and deploy an app with a function that defines a new discount type. The merchant can then install the app on their Shopify store and create a new discount from a discount type provided by the app. Shopify executes the function to calculate the discount when a customer adds a product to their cart.

Shopify Functions are never invoked directly by URL or otherwise. Shopify invokes them as-needed within the customer journey.

#### Getting started

Learn how to use Shopify Functions by following one of our use case tutorials:

* [Build a discount function](https://shopify.dev/docs/apps/build/discounts/build-discount-function) — Use Shopify Functions to create a new discount type for users.
* [Create a payments function](https://shopify.dev/docs/apps/build/checkout/payments/create-payments-function) — Use Shopify Functions to hide a payment option offered to customers at checkout.
* [Build a delivery options function](https://shopify.dev/docs/apps/build/checkout/delivery-shipping/delivery-options/build-function) — Use Shopify Functions to rename a delivery option offered to customers at checkout.
* [Create a server-side validation function](https://shopify.dev/docs/apps/build/checkout/cart-checkout-validation/create-server-side-validation-function) — Block progress on a checkout when the cart line quantities exceed a limit.
* [Build a location rule function](https://shopify.dev/docs/apps/build/orders-fulfillment/order-routing-apps/location-rules/build-location-rule-function) — Choose a different order location during checkout.
* [Add a customized bundle function](https://shopify.dev/docs/apps/build/product-merchandising/bundles/add-customized-bundle-function) — Group products together and sell them as a single unit.
* [Build a fulfillment constraints function](https://shopify.dev/docs/apps/build/orders-fulfillment/order-routing-apps/build-fulfillment-constraints-function) — Customize fulfillment and delivery strategies.
* [Build a local pickup options function](https://shopify.dev/docs/apps/build/orders-fulfillment/order-routing-apps/build-local-pickup-options-function) — Generate local pickup delivery options at checkout.
* [Create a local pickup charges function](https://shopify.dev/docs/apps/build/checkout/delivery-shipping/delivery-methods/create-local-pickup-charges-function) — Create local pickup charges at checkout.
* [Generate a pickup points function](https://shopify.dev/docs/apps/build/checkout/delivery-shipping/delivery-methods/generate-pickup-points) — Generate pickup point delivery options at checkout.

#### Developer tools and resources

* [Shopify Function APIs reference](https://shopify.dev/docs/api/functions) — Learn about the available APIs for Shopify Functions.
* [Language support](https://shopify.dev/docs/apps/build/functions/programming-languages) — Learn about the language support and tooling available in Shopify Functions.

#### Deleting functions

To delete a Shopify Function, you need to remove the relevant files from your app's `/extensions` directory, and then redeploy your app.

When you delete a function, the following behavior occurs:

* The function, including all associated function owners, is permanently deleted.
* The function no longer runs, and becomes inaccessible to any Shopify stores that have your app installed.

---

### Function APIs (reference home)

> Fonte: https://shopify.dev/docs/api/functions

Shopify Functions enable you to customize Shopify's backend logic by running custom code during the checkout process. You can create functions to implement specialized features that aren't available natively. For example, you can generate custom delivery options, create new types of discounts, and provide your own validation of a cart and checkout.

When you build a function, prioritize performance. Functions run in the context of key purchase flows, like discounts and checkout. Delays can negatively impact the Shopify backend and prevent customers from making purchases.

#### Shopify CLI scaffold

Function APIs require a set of essential files, such as TOML configuration, GraphQL schema, GraphQL input query, and function code. Use Shopify CLI to scaffold the essential elements that you need to get started.

```terminal
shopify app generate extension
```

#### Function execution order in checkout

When building Shopify Functions, you need to understand where they fit into the checkout process. Functions execute in a specific sequence during checkout, and each function depends on data from earlier steps. This sequencing is important because:

* Your function's input data comes from previous checkout operations.
* The logic of your function might change, depending on where it's executed during the checkout process.
* Understanding this flow helps you build more reliable and efficient functions.

For example, when a customer adds items to their cart and proceeds to checkout, several functions might run in sequence: first, functions that change the pricing and presentation of items in a cart run; then, functions that calculate discounts execute; finally, functions that validate the cart contents run. Each step builds on the data from previous steps, so a cart validation function can't run until after discount calculations are complete.

The order each function runs during checkout:

1. **Cart lines**
   1. [Cart Transform](https://shopify.dev/docs/api/functions/latest/cart-transform)
2. **Cart line discounts**
   1. [Discount](https://shopify.dev/docs/api/functions/latest/discount)
3. **Fulfillment groups**
   1. [Fulfillment Constraints](https://shopify.dev/docs/api/functions/latest/fulfillment-constraints)
   2. [Order Routing](https://shopify.dev/docs/api/functions/latest/order-routing-location-rule)
4. **Delivery methods**
   1. [Pickup Point Delivery Option Generator](https://shopify.dev/docs/api/functions/unstable/pickup-point-delivery-option-generator)
   2. [Local Pickup Delivery Option Generator](https://shopify.dev/docs/api/functions/unstable/local-pickup-delivery-option-generator)
   3. [Delivery Customization](https://shopify.dev/docs/api/functions/latest/delivery-customization)
5. **Delivery discounts**
   1. [Discount](https://shopify.dev/docs/api/functions/latest/discount)
6. **Payment methods**
   1. [Payment Customization](https://shopify.dev/docs/api/functions/latest/payment-customization)
7. **Verification**
   1. [Cart and Checkout Validation](https://shopify.dev/docs/api/functions/latest/cart-and-checkout-validation)

#### Function extension target types

Identifiers that specify where you're injecting code into Shopify. Targets define where functions run during the commerce loop.

* **Fetch target (limited)** — Input → Function module → Output, plus a Shopify-network HTTPS call to an external service.
* **Run target** — Input → Function module → Output.

##### Fetch target limited access

**Limited access:** The fetch target is limited to custom apps installed on Enterprise stores. You'll also need to [request network access for Functions](https://shopify.dev/docs/apps/build/functions/network-access), as it's not currently available on development stores or in a developer preview. However, there are exceptions for some Function APIs. For information on fetch target access for a specific API, refer to that Function's API reference page.

A fetch target is a mechanism for retrieving data from a third party provider and passing the data to the run target. Shopify calls the fetch target before the run target. Shopify makes the HTTP call on your behalf, which makes the fetch results available to the run target. This ensures that the run target has access to data from an external source. Returning a network request is optional if it's not necessary for a specific function execution.

##### Run target

An extension point that enables you to customize Shopify's backend with custom business logic. For example, you can prioritize locations for order routing, or create a new type of discount that's applied to a product or product variant in the cart. The run target uses either Shopify data, hardcoded values, or fetch results from external providers.

```toml
[[extensions.targeting]]
target = "<target_name>.fetch"
input_query = "src/fetch.graphql"
export = "fetch"
```

```toml
[[extensions.targeting]]
target = "<target_name>.run"
input_query = "src/run.graphql"
export = "run"
```

#### Function anatomy

When you create a function, you write a GraphQL input query that defines the shape of your data. Then you write logic that transforms the input data and returns the output to Shopify. Shopify Functions query input data from the schema of a Function API. The output is also defined by the same Function API schema.

You can write functions in any language that can compile to WebAssembly (Wasm), although Rust is recommended and strongly preferred.

**Input** — The `Input` object is the complete GraphQL schema that your function can receive as input. You specify what input your function needs using an input query. Before calling your target, Shopify runs its associated GraphQL query and passes the resulting JSON data to your target. When you create a function, the Shopify CLI generates a GraphQL file for your input query. In `run.graphql` you can edit the query to request the data you need. The structure of the JSON input in `input.json` then matches the shape of that query. You can customize input queries using metafields, app-owned metaobjects, or input variables. Each target that your function extension implements can have a unique input query.

```graphql
# run.graphql
query {
  cart {
    cart_field {
      property
    }
  }
}
```

```json
// input.json
{
  "cart": {
    "cart_field": {
      "property": "bar"
    }
  }
}
```

**Function** — The logic that processes your input data to generate a standardized response. It transforms your data into an ordered list of operations. Each operation specifies the action to take based on your function's purpose. Shopify processes your response to present the results, such as available cart line discounts, during the commerce flow.

```rust
fn main() {
    println!("Hello, world!");
}
```

```javascript
//@param {input}
//@returns {FunctionRunResult} or {functionFetchResult}

export function run(input) {
    //function logic
    return { };
}
```

**Output** — When your function runs, it returns an object that Shopify uses to perform one or more operations. Each Function API extension target specifies the shape of the function's output using a GraphQL type. Function output is a declarative object which represents operations for Shopify to execute.

```json
{
  "operations": [
    {
      "operations_field": {
        "field": "value"
      }
    }
  ]
}
```

#### Configuration

Functions rely on a `shopify.extension.toml` file that contains the extension's configuration. This includes the extension name, type, API version, UI paths, build configuration, and metafields for query variables. The `name` value is what displays in the Shopify admin to merchants. We recommend that the `api_version` reflects the latest supported API version.

Functions use common configuration properties for app extensions. Additionally, the following properties in `shopify.extension.toml` are specific to Shopify Functions:

**`[[extensions.targeting]]` (required)** — Array containing a target and its associated WebAssembly module export:

* `target` (required) — An identifier that specifies where you're injecting code into the Shopify backend.
* `input_query` (optional) — The path to the input query file for the target. If omitted, then the function receives no input.
* `export` (optional) — The name of the WebAssembly export in your module that executes the target. Functions don't use the `extensions.targeting.module` setting; use `export` instead. Defaults to `_start`.

**`[extensions.build]` (optional):**

* `command` (required) — The command to build the function, invoked by the Shopify CLI build command. Can be omitted for JavaScript.
* `path` (optional) — The relative path to the function's WebAssembly module (e.g. `build/my-module.wasm`). Defaults to `dist/index.wasm`.
* `watch` (optional) — Relative paths that Shopify CLI watches during the dev command. Changes trigger a build and update your application drafts. Accepts a single path/glob or an array. For JS/TS functions defaults to `['src/**/*.js', 'src/**/*.ts']`. Only paths inside the function directory are allowed (no `../`). Input queries are automatically included in watch paths.
* `wasm_opt` (optional) — Whether to optimize your module before upload. Defaults to `true`.

**`[extensions.ui]` (optional):**

* `handle` (optional) — The handle of another UI extension in your app that serves as the Shopify admin for merchants to configure the function.
* `enable_create` (optional) — Whether the function displays in the Shopify admin to merchants to create workflows.

**`[extensions.ui.paths]` (optional):**

* `create` (optional) — The path within your app launched when a merchant clicks to create a new customization with this function.
* `details` (optional) — The edit path launched when a merchant clicks a customization.

**`[extensions.input.variables]` (optional):** The variables to use in your input query (for inserting dynamic values when using `hasTags`/`hasCollections`).

* `namespace` (optional) — A container for a group of metafields.
* `key` (optional) — The name for the metafield.

```toml
api_version = "2026-01"


[[extensions]]
name = "t:name"
handle = "my-discount-function"
type = "function"
uid = "aad83b55-634c-f168-7ece-00d492c84058ddd4a6b4"


  [[extensions.targeting]]
  target = "cart.lines.discounts.generate.run"
  input_query = "src/run.graphql"
  export = "run"


  [extensions.build]
  command = "cargo build --target=wasm32-unknown-unknown --release"
  path = "target/wasm32-unknown-unknown/release/discount.wasm"
  watch = [ "src/**/*.rs" ]


  # note: mutually exclusive to extension.ui.paths
  [extensions.ui]
  enable_create = true
  handle = "ui-extension-handle"


  # note: mutually exclusive to extension.ui
  [extensions.ui.paths]
  create = "/discount/function-handle/new"
  details = "/discount/function-handle/:id"


  [extensions.input.variables]
  namespace = "my-namespace"
  key = "my-key"
```

#### GraphQL schema and versioning

Each Function API has a GraphQL schema representation, which you can use with tools like the VS Code GraphQL plugin and language-specific code generation tools such as `graphql_client` for Rust. On creation, each function includes a copy of the GraphQL schema in `schema.graphql`. We recommend that your function always uses the latest supported schema version.

Function APIs are versioned. Updates are released quarterly; details are in the developer changelog. Your function will be configured for the latest version when you update the API version specified in your configuration file, generate the latest schema, or (if using JavaScript) regenerate types based on your input query.

```toml
api_version = "<api-version-in-configuration-file>"
```

```bash
shopify app function schema
```

```bash
shopify app function typegen
```

To generate the latest GraphQL schema for your function, use the `function schema` command. This outputs the latest schema based on your function's API type and version to `schema.graphql`. You can output to `STDOUT` with `--stdout`, or pipe it into a code generation tool:

```bash
shopify app function schema
```

```bash
shopify app function schema --stdout
```

```bash
shopify app function schema --stdout > <FILE_PATH>
```

#### API availability

* **All plans:** Except as noted in individual API pages, stores on any plan can use public apps distributed through the Shopify App Store that contain functions.
* **Shopify Plus:** Only stores on a Shopify Plus plan can use custom apps that contain Shopify Function APIs.

#### Limitations

Your function must adhere to resource limits. Performance is critical because functions run in the context of key purchase flows like discounts and checkout. Shopify strongly recommends Rust as the most performant language choice.

The following apply to all functions:

* Apps can reference only their own functions in GraphQL Admin API mutations, such as `discountAutomaticAppCreate` and `cartTransformCreate`. Referencing a function from another app results in a `Function not found` error.
* Shopify doesn't allow nondeterminism in functions — you can't use any randomizing or clock functionality.
* You can't debug your function by printing out `STDOUT` or `STDERR`.
* The Shopify App Store doesn't permit apps that provide dynamic editing and execution of function code.
* Some functions support network access (see network access). You can also pre-populate data using metafields on products and customers, or passing data using cart attributes.

##### Fixed limits

| Resource | Limit |
| - | - |
| Compiled binary size | 256 kB |
| Runtime linear memory | 10,000 kB |
| Runtime stack memory | 512 kB |
| Logs written | 1 kB (truncated) |

**Note:** Function resource limits treat 1 kilobyte (kB) as 1000 bytes.

##### Dynamic limits

Certain limits are dynamic and scale based on the number of line items in a cart. For carts with more than 200 line items, these values scale proportionally. Calculated limits for a function execution are available in your Dev Dashboard and can be tested with Shopify CLI.

| Resource | Limit (up to 200 line items) |
| - | - |
| Execution instruction count | 11 million instructions |
| Function input | 128 kB |
| Function output | 20 kB. This limit doesn't support bulk price transformations across all line items. Use discount functions, B2B catalogs, or target specific products instead. |

##### Input query limits

* The maximum size for an input query, excluding comments, is 3000 bytes.
* Metafields with values exceeding 10,000 bytes in size will not be returned.
* Field arguments and input query variables of list type can't exceed 100 elements.
* Function input queries can have a maximum calculated query cost of 30. Field costs:

| Field | Example | Cost value |
| - | - | - |
| `__typename` | | 0 |
| Any field that returns a `Metafield` object | `metafield` on a `Product` object | 3 |
| Any field on a `Metafield` object | `value` | 0 |
| `metaobject` root field | `metaobject(handle: "...")` or `metaobject(id: "...")` | 1 |
| `field(key:)` on a `Metaobject` | `field(key: "price-tier")` | 3 |
| `hasAnyTag` | | 3 |
| `hasTags` | | 3 |
| Any field on a `HasTagResponse` object | `hasTag` | 0 |
| `inAnyCollection` | | 3 |
| `inCollections` | | 3 |
| Any field on a `CollectionMembership` object | `isMember` | 0 |
| Other leaf nodes | `id` or `sku` on a `ProductVariant` object | 1 |

---

### Language considerations

> Fonte: https://shopify.dev/docs/apps/build/functions/programming-languages

Shopify Functions support any language that compiles to WebAssembly (Wasm), such as Rust, Zig, or TinyGo. Functions compiled to Wasm need to meet Shopify's WebAssembly API specifications and platform binary and performance limitations.

#### Functions environment

Shopify Functions operate in critical buyer flows such as Checkout. For a given Checkout request there may be multiple functions executed, each one adding to the overall latency of the checkout request. For this reason, Shopify places a number of platform limits, many of which can be measured locally using Shopify CLI.

#### Choosing a language

Languages that compile directly to WebAssembly, such as Rust, perform better than dynamic languages, such as JavaScript. If your function targets a public app, expects to operate on a large number of line items, or is computationally complex, then choose Rust to stay within the Shopify Functions instruction count requirements.

For prototyping ideas, JavaScript is a good starting point if you're familiar with the language. However, expect to run into instruction limits sooner than if you wrote the equivalent function logic in a language that compiles to WebAssembly directly, such as Rust.

#### Available language support

* **Rust** — Support for Rust in Shopify Functions.
* **JavaScript** — Support for JavaScript and TypeScript in Shopify Functions.
* **WebAssembly** — Using other languages that support WebAssembly in Shopify Functions.

---

### WebAssembly for Functions

> Fonte: https://shopify.dev/docs/apps/build/functions/programming-languages/webassembly-for-functions

You can write your functions in any language that can compile to WebAssembly (Wasm), such as Rust, Zig, or TinyGo. This guide describes how to generate Wasm that conforms to Shopify Functions standards.

#### Shopify Wasm API

The Shopify Wasm API provides imported functions that your Wasm module uses to read input data and write output data. It defines a structured interface between your Shopify Function and the Shopify platform, including standardized value representations, status and error codes, and a compact NaN-boxed encoding format. Using these API functions, your module can access data lazily at runtime instead of loading everything upfront. This eliminates the overhead of embedding a JSON parser into your compiled binary, resulting in smaller and more efficient Functions.

#### Supported first party languages

* **Rust:** Supported through the `shopify_function` crate, version 1.0.0 and above. Refer to the migration guide to upgrade existing functions.
* **JavaScript:** Supported through the `@shopify/shopify_function` npm package, version 2.0.0 and above, and the latest version of Shopify CLI.

#### Requirements

Functions that are compiled to Wasm must meet the following requirements:

* Conform with the Shopify Function Wasm API specification.
* For each target implemented by the extension, the module must export a function of type `(func)`, which takes no arguments, and has no return values. Function modules are multi-call executables that have exports mapped to Shopify targets in the function extension configuration.
* Write debug logs with the `shopify_function_log_new_utf8_str` imported Wasm function.

#### NaN-box Value Structure (64-bit)

Input values in the Wasm API are represented as 64-bit NaN-boxed values, represented as `i64` constants in WebAssembly. NaN-boxing provides a performant way to represent multiple value types (numbers, strings, booleans, objects, arrays, or errors) within 64 bits, without requiring additional memory allocations for type information.

```text
63  62        52 51 50 49    46 45       32 31                 0
+---+------------+--+--+--------+-----------+--------------------+
| 0 | 11111111111| 1 | 1 | TTTT  |   LENGTH  |       VALUE        |
+---+------------+--+--+--------+-----------+--------------------+
^        ^         ^     ^          ^              ^
Sign  Exponent   Quiet  Tag bits   Length      Value bits
(0)   (all 1s)   NaN    (type)    (14 bits)   (32 bits - data/ptr)
```

* **Sign bit**: 0
* **Exponent**: 11 bits, all 1's.
* **Quiet NaN**: 1 bit set to 1.
* **Tag bits (TTTT)**: 4 bits indicating value type (0-15).
* **Length field**: 14 bits for string/array length.
* **Value field**: 32 bits for actual data or a pointer to heap-allocated structures.

When a value is a floating-point number (type tag `2`), it is not encoded through NaN-boxing. Instead, it directly uses the standard IEEE 754 double-precision binary floating-point format:

```text
63  62        52 51                                         0
+---+------------+--------------------------------------------+
| S |  Exponent  |                  Mantissa                  |
+---+------------+--------------------------------------------+
^       ^                             ^
Sign  Exponent                      Mantissa
(variable) (variable)              (variable)
```

**Value Types** (the `Tag bits (TTTT)`):

* **0**: `Null` — Null value
* **1**: `Bool` — Boolean value (true/false)
* **2**: `Number` — Numeric value (f64)
* **3**: `String` — UTF-8 encoded string (pointer + length)
* **4**: `Object` — Key-value collection (pointer + length)
* **5**: `Array` — Indexed collection of values (pointer + length)
* **15**: `Error` — Read error codes

#### Reading Data

To read input data, your Wasm module uses a set of imported API functions to access the root input value and traverse complex data structures. Each read operation returns a NaN-boxed value interpreted per the structure above. For a complete list and detailed signatures, refer to the C header file or the WebAssembly Text Format definition.

**Read Error Codes (i32 type)** — when a 64-bit NaN-boxed value has its type tag bits set to `15` (Error), the lower 32 bits contain one of:

* **0**: `DecodeError` — Value could not be decoded
* **1**: `NotAnObject` — Expected an object but received another type
* **2**: `ByteArrayOutOfBounds` — Byte array index out of bounds
* **3**: `ReadError` — Error occurred during reading
* **4**: `NotAnArray` — Expected an array but received another type
* **5**: `IndexOutOfBounds` — Array index out of bounds
* **6**: `NotIndexable` — Value is not indexable (not an object or array)

Shopify does not consider additions to this list to be a breaking change, so developers are encouraged to handle new error values.

#### Writing Data

To write output data, your Wasm module uses a corresponding set of imported API functions. Most write operations return an `i32` status code; `0` (Success) indicates success.

**Write Status Codes (i32 type):**

* **0**: `Success`
* **1**: `IoError`
* **2**: `ExpectedKey`
* **3**: `ObjectLengthError`
* **4**: `ValueAlreadyWritten`
* **5**: `NotAnObject`
* **6**: `ValueNotFinished`
* **7**: `ArrayLengthError`
* **8**: `NotAnArray`

Shopify does not consider additions to this list to be a breaking change.

#### Migrating from the V1 Wasm API to the V2 Wasm API

1. Change any imports from the `shopify_function_v1` module to import from the `shopify_function_v2` module.
2. Stop passing the context pointer to any Wasm API functions as they no longer accept a context pointer as a parameter.
3. Remove any imports and calls to `shopify_function_context_new` and `shopify_function_output_finalize` as these functions have been removed from the API.
4. Call `shopify_function_log_new_utf8_str` to log a string instead of writing to standard error. Any writes to standard error will be ignored instead of logged.

#### Module example

```wat
(module
 (func $run (export "run")
   ...
 )
)
```

```toml
[[extensions.targeting]]
target = "cart.lines.discounts.generate.run"
input_query = "src/run.graphql"
export = "run" # This matches the name of the wasm export.
```

---

### Rust for Functions

> Fonte: https://shopify.dev/docs/apps/build/functions/programming-languages/rust-for-functions

You can write your functions in Rust. This guide describes the [`shopify_function`](https://crates.io/crates/shopify_function) Rust crate that Shopify provides.

#### How it works

The `shopify_function` Rust crate performs type generation, reduces boilerplate, and makes it easier to test various function inputs. Components:

| Component | Description |
| - | - |
| `typegen` | A macro to enable struct generation from the Function API, based on the provided GraphQL schema and input query. |
| `shopify_function` | An attribute macro that marks the given function as the entrypoint for Shopify Functions, by exporting a WebAssembly function with the specified name (which must match the target export in the function extension configuration) and providing an efficient API to manage the function's input and output. |
| `run_function_with_input` | A utility for unit testing that enables you to add new tests based on a given JSON input string. |

#### Viewing the generated types

```terminal
cargo doc --open
```

```terminal
cargo install cargo-expand
cargo expand --doc
```

#### Development tools

Install the rust-analyzer VSCode extension for code completion, go to definition, real-time error checking, and type information on hover.

**Note:** The generated `.output.graphql` files are used for output type generation purposes. You can add these files to your `.gitignore` file.

#### Example implementations

* [Rust Shopify Function example](https://github.com/Shopify/shopify-function-rust/tree/main/example_with_targets)
* [Rust Shopify Function example for earlier versions](https://github.com/Shopify/shopify-function-rust/tree/main/example) (compatible with API versions 2023-07 and earlier)

#### Binary size tips

Shopify Functions compiled Wasm file must be under 256 kB. Tips:

* Update the `shopify_function` crate to the latest version.
* For regular expressions, use the `regex_lite` crate.
* Follow tips in the johnthagen/min-sized-rust GitHub repository.
* Use `wasm-snip` to remove panicking code, then `wasm-opt` to strip debug information:

```text
# Change this line:
export WASM_PATH=target/wasm32-unknown-unknown/release/your-function-name.wasm


RUSTFLAGS="-C strip=none" cargo build --target=wasm32-unknown-unknown --release \
  && wasm-snip --snip-rust-panicking-code $WASM_PATH \
  | wasm-opt -O3 --enable-bulk-memory --strip-debug -o function.no-panic.wasm -
```

* Use `to_ascii_uppercase` and `to_ascii_lowercase` when possible to avoid pulling in Unicode tables, unless needed.
* Only query for data you need. Code generation happens for all types and fields in input queries (e.g. `run.graphql`); remove unused parts.
* Keep JSON metafields that require deserialization as small as possible.
* Bring your own types and deserializers — instead of the generated structs, write struct definitions and derive deserializers using `mini_serde`. Benchmark instruction count if you do.
* Update the `shopify_function` crate to version `1.0.0` and above.

#### Updating existing function to using shopify_function 2.0.0 and higher

If you are using a version less than `1.0.0`, update to version `1.1.1` (steps below) before following these steps.

1. Update to the latest Shopify CLI version.
2. Install the `wasm32-unknown-unknown` build target:

   ```terminal
   rustup target add wasm32-unknown-unknown
   ```

3. Update your build `command` and `path` in `[extensions.build]` to use `wasm32-unknown-unknown` instead of `wasm32-wasip1`. Replace `RUST-PACKAGE-NAME` with the `name` from your `Cargo.toml`:

   ```toml
   [extensions.build]
   command = "cargo build --target=wasm32-unknown-unknown --release"
   path = "target/wasm32-unknown-unknown/release/[RUST-PACKAGE-NAME].wasm"
   ```

4. Update any references to `eprintln!` to use `log!`:

   ```rust
   #[shopify_function]
   fn run(input: schema::run::Input) -> Result<schema::FunctionRunResult> {
     log!("This will be logged");
     todo!();
   }
   ```

5. Update any references to `process::exit(1)` to use `process::abort()`:

   ```rust
   #[shopify_function]
   fn run(input: schema::run::Input) -> Result<schema::FunctionRunResult> {
     log!("Please invoke a named export.");
     process::abort();
   }
   ```

#### Updating existing function to using shopify_function 1.0.0 and higher

1. In `main.rs`, add imports for `shopify_function`:

   ```rust
   use shopify_function::prelude::*;
   ```

2. In `main.rs`, add type generation under your imports (remove any `generate_types!` references):

   ```rust
   #[typegen("schema.graphql")]
   pub mod schema {
     #[query("src/run.graphql")]
     pub mod run {}
   }
   ```

   If your function has multiple targets each with their own input query, add a nested module for each:

   ```rust
   #[typegen("schema.graphql")]
   pub mod schema {
     #[query("src/fetch.graphql")]
     pub mod fetch {}


     #[query("src/run.graphql")]
     pub mod run {}
   }
   ```

3. Ensure you have a `main` function that returns an error indicating to invoke a named export:

   ```rust
   fn main() {
     log!("Invoke a named import");
     std::process::abort();
   }
   ```

4. If you have an input query to retrieve a JSON metafield value (e.g.):

   ```graphql
   query Input {
       deliveryCustomization {
           metafield(namespace: "delivery-customization", key: "function-configuration") {
             jsonValue
           }
       }
   }
   ```

   You can deserialize the `jsonValue` directly into an object you define and annotate:

   ```rust
   #[derive(Deserialize)]
   #[shopify_function(rename_all = "camelCase")]
   pub struct DeliveryConfiguration {
       state_province_code: String,
       message: String,
   }
   ```

   Then use `custom_scalar_overrides` to link the `jsonValue` with its object definition in `main.rs`:

   ```rust
   #[typegen("schema.graphql")]
   mod schema {
       #[query("src/run.graphql",
           custom_scalar_overrides = {
               "Input.deliveryCustomization.metafield.jsonValue" => super::run::DeliveryConfiguration,
           }
       )]
       pub mod run {}
   }
   ```

5. Ensure your source file with the function logic includes:

   ```text
   use shopify_function::prelude::*;
   use shopify_function::Result;
   use super::schema;
   ```

6. Replace any `#[shopify_function_target]` with `#[shopify_function]`, and change its return type:

   ```rust
   #[shopify_function]
   fn run(input: schema::run::Input) -> Result<schema::FunctionRunResult> {
   ```

7. Update types and fields to the new auto-generated structs:

   | Old | New |
   | - | - |
   | `input::ResponseData` | `schema::run::Input` |
   | `input::InputDiscountNodeMetafield` | `schema::run::input::discount_node::Metafield` |
   | `input::InputDiscountNode` | `schema::run::input::DiscountNode` |
   | `output::FunctionRunResult` | `schema::FunctionRunResult` |
   | `output::DiscountApplicationStrategy::FIRST` | `schema::DiscountApplicationStrategy::First` |

#### Updating to Rust 1.84 and higher

As of Rust version 1.84, the WebAssembly build target used by `cargo-wasi` was removed.

1. Update to the latest Shopify CLI version.
2. Remove the deprecated `wasm32-wasi` build target: `rustup target remove wasm32-wasi`
3. Update your Rust version: `rustup update stable`
4. Install the new `wasm32-unknown-unknown` build target: `rustup target add wasm32-unknown-unknown`
5. Update your build `command` and `path` in `[extensions.build]`:

   ```toml
   [extensions.build]
   command = "cargo build --target=wasm32-unknown-unknown --release"
   path = "target/wasm32-unknown-unknown/release/[RUST-PACKAGE-NAME].wasm"
   ```

These changes are compatible with Rust 1.78 and higher.

**Note:** The `cargo-wasi` crate also optimized binary size using the Binaryen toolchain. Shopify CLI will now optimize your module by default; configure this via the `wasm_opt` configuration property.

#### Migrating from JavaScript

Migrating a JavaScript Shopify Function to Rust can significantly improve performance and help you stay within platform fuel limits.

1. Generate a new function: `shopify app generate extension`
2. When prompted, choose the same function type, name it like your current function but append `-rs`, and select `Rust`.
3. Copy your existing GraphQL query, making adjustments: copy `run.graphql` to the new Rust function's `src`, rename the query from `RunInput` to `Input`, and add `__typename` to any fragments on interfaces or unions:

   ```graphql
   # Before (JavaScript):
   # query RunInput {
   #   cart {
   #     lines {
   #       merchandise {
   #         ... on ProductVariant {
   #           id
   #         }
   #       }
   #     }
   #   }
   # }


   # After (Rust):
   query Input {
     cart {
       lines {
         merchandise {
           __typename
           ... on ProductVariant {
             id
           }
         }
       }
     }
   }
   ```

4. Port your JavaScript logic to the generated `src/run.rs` file.

**Reusing extension UIDs** — by reusing the extension UID from your JavaScript function, you can seamlessly replace the existing function on the server. The `uid` is the unique identifier that determines which function gets updated.

```toml
# JavaScript function's configuration
name = "your-function"
handle = "your-existing-handle"
uid = "your-existing-uid"  # The uid is the critical identifier
```

```toml
# Rust function's configuration
name = "your-function-rs"
handle = "your-existing-handle"
uid = "your-existing-uid"  # The uid ensures the right function gets updated
```

Disable the JavaScript function by renaming its config file:

```terminal
mv extensions/your-function/shopify.extension.toml extensions/your-function/shopify.extension.disabled.toml
```

**Caution:** If you deploy both functions, they will both appear in the merchant admin, which may cause confusion. Always ensure you've disabled the JavaScript function before deploying the Rust version.

**Validating the migration:** test locally (`shopify app function run --input input.json`), deploy to a dev store and verify, confirm only one function appears in the merchant admin, then delete the JavaScript function directory.

---

### JavaScript for Functions

> Fonte: https://shopify.dev/docs/apps/build/functions/programming-languages/javascript-for-functions

You can write your functions in JavaScript. This guide describes the process of building a Shopify Function using JavaScript or TypeScript.

**Caution:** For prototyping ideas, JavaScript is a good starting point if you're familiar with the language. However, expect to run into instruction limits sooner than if you wrote the equivalent function logic in a language that compiles to WebAssembly directly, such as Rust. Shopify strongly recommends Rust.

#### How it works

Shopify CLI compiles your JavaScript code using Javy, a JavaScript-to-WebAssembly toolchain. There is also a Shopify Functions JavaScript library.

**Note:** To write functions in JavaScript, you must install Node.js 16 or higher. If you previously installed Shopify CLI, make sure you're using the latest version. To achieve smaller binary sizes and faster function execution, use the latest version of Shopify CLI and v2.0.0+ of the `@shopify/shopify_function` JavaScript package.

**Javy** is part build tool, part runtime engine:

* **Build tool**: Takes a JavaScript file and compiles it into a WebAssembly module, which contains both your code and a full JavaScript engine embedded.
* **Runtime engine**: Javy implements a handful of APIs required to make JavaScript work well for Shopify Functions.

**Shopify Functions JavaScript library** — provides convenient functions and hides repetitive boilerplate. It includes a TypeScript type generator that inspects your GraphQL query to allow your IDE to provide autocomplete suggestions.

#### Available JavaScript APIs

**ECMAScript 2020** — The Javy runtime implements the ECMAScript 2020 specification. However, Javy doesn't enable JavaScript's event loop. This means `async`/`await` and promises will compile fine, but will throw an error when your function executes:

```txt
thread '<unnamed>' panicked at 'called `Result::unwrap()` on an `Err` value: Adding tasks to the event queue is not supported
```

**Javy globals** — Javy exposes additional IO globals for reading and writing from `STDIO`. The `javy` npm package provides convenience methods over the built-in functions. Javy also exposes an encoding API which is W3C-compatible, with exceptions: support for UTF-8 encoding exclusively; no `TextEncoderStream`/`TextDecoderStream`; no `TextEncoder.encodeInto`; no setting the `stream` property to `true` in `TextDecoder.decode`.

**Not available in Javy or Shopify Functions:**

* Web-specific browser APIs such as `setTimeout`, `fetch`, `crypto`, or `URL`. (Exception: `TextEncoder` and `TextDecoder`, which Javy provides.)
* Node.js-specific globals and imports such as `process`, `node:buffer`, `node:http`, or `node:util`.

#### JavaScript functions and Shopify CLI

The quickest way to get started is to use the Shopify Functions JavaScript library with Shopify CLI. Shopify CLI helps scaffold projects and uses ESBuild to preprocess JavaScript and TypeScript — you can install and import `npm` dependencies, bundled before everything compiles to WebAssembly. Shopify CLI also supports TypeScript and type annotations from GraphQL schemas and input queries, and uses Javy to compile a WebAssembly module conforming to requirements, automatically generating exports from targets.

**Compatibility with earlier versions** — Shopify CLI provides backwards compatibility with API versions 2023-07 and earlier, compiling a module that exports a `_start` function.

#### Sample apps

* [Discounts](https://github.com/Shopify/function-examples/tree/main/sample-apps/discounts)
* [Payment customizations](https://github.com/Shopify/function-examples/tree/main/sample-apps/payment-customizations)
* [Delivery customizations](https://github.com/Shopify/function-examples/tree/main/sample-apps/delivery-customizations)

---

### Metafields for input queries

> Fonte: https://shopify.dev/docs/apps/build/functions/input-queries/metafields-for-input-queries

To make your code reusable, you can replace hard-coded variables in your function with metafield values. Using metafields enables merchants and staff to customize your function by entering values and options in interfaces provided by your app.

#### How it works

Shopify Functions belong to and can affect the behavior of objects in the Shopify data model. The object associated with a function is known as the **function owner**. For example, the owner of a Discount API function is a discount. You use an admin UI extension or App Home page to create merchant interfaces for managing function owners and their metafields. Then you use input queries to provide the metafields as input to your function.

> **Tip:** Metafields and metaobjects are platform primitives available across Shopify's data model. You can query metafields from products, customers, carts, and more in your input queries. Metaobjects are not tied to resources; consider them when configuring multiple related fields, or when metaobject entries should be created and managed by shop staff directly in the Shopify admin. Metaobjects must be app-owned metaobjects.

#### Creating your merchant interface

Some Function APIs enable you to create a merchant interface for configuring your function using either App Home pages or admin UI extensions.

**Using admin UI extensions** — specify the `extension.ui.handle` property in `shopify.extension.toml`; its value must match the handle of the corresponding UI extension in your app.

```toml
[extension.ui]
handle = "ui-extension-handle"
```

**Using App Home pages** — use App Bridge and Polaris to create a seamless merchant experience. Configure routes merchants use to create and edit the function owner. The default path for both is the app root (`/`).

| Property | Description | Example |
| - | - | - |
| `ui.paths.create` | The route to create a new function owner. | `/my-discount-type` |
| `ui.paths.details` | The route to edit the function owner. | `/my-discount-type/:id` |

```toml
[extensions.ui.paths]
create = "/my-discount-type/function-handle"
details = "/my-discount-type/function-handle/:id"
```

**Dynamic ID values** — if you specify `:id` in `ui.paths`:

| URL Path | Update | Availability |
| - | - | - |
| `:id` | The `:id` is dynamically replaced by the ID of the function owner. | `ui.paths.details` |

**Creating Metafields with GraphQL** — use the GraphQL Admin API to create and update your function owner and its metafields. Example mutation that sets metafields on a discount function owner:

```graphql
mutation CreateDiscount {
  discountAutomaticAppCreate(automaticAppDiscount: {
    functionId: "f0c17828-da1a-4748-810d-3c3cab2bc977",
    title: "My Discount",
    startsAt: "2022-06-01T00:00:00Z",
    metafields: [
      {
        namespace: "$app:my-function",
        type: "json",
        key: "function-configuration",
        value: "{\"value\":\"42\"}"
      }
    ]
  }) {
    automaticAppDiscount {
      discountId
    }
    userErrors {
      field
      message
    }
  }
}
```

**Configuring creation workflows for function owners** — you can configure the function to opt-out of the default function owner creation workflow, so the app is solely responsible for creating the function owner. The merchant can still edit, activate, or deactivate one created by the app.

| Property | Description | Type |
| - | - | - |
| `ui.enable_create` | Whether the merchant can create a function owner in the Shopify admin. Default `true`. | Boolean |

#### Reading metafields with input queries

All Function APIs provide access to the function owner and its metafields as part of their GraphQL schema. Example input query that retrieves a metafield on a discount function owner:

```graphql
{
  discountNode {
    metafield(namespace: "$app:my-function", key: "function-configuration") {
      value
    }
  }
}
```

#### Best practices

* **Use a reserved prefix in your metafield namespace**, so other apps can't use your metafields.
* **Use JSON metafields for complex configurations** — functions often require nested and/or repeating data structures; a single JSON metafield simplifies management and querying.
* **Manage configuration changes with new metafields** — to make breaking changes, implement the Parallel Change (Expand and Contract) pattern:
  1. Update your function's logic to read configuration from existing and new metafields, preferring newer data if present.
  2. Change your function UI to update both existing and new metafields.
  3. Use the GraphQL Admin API to migrate existing data from old metafields to new.
  4. After migration, remove UI and function logic for old metafields.
  5. Use the GraphQL Admin API to remove old metafields.

> **Tip:** To edit metafields outside of a merchant's web session (e.g. an offline maintenance job), request an offline access token during app installation.

---

### Use variables in input queries

> Fonte: https://shopify.dev/docs/apps/build/functions/input-queries/use-variables-input-queries

Function input queries can be customized on each function owner using input query variables. This is helpful when using fields with arguments like `inAnyCollection`. Consider:

```graphql
# without-input-query-variables.graphql
query Input {
  cart {
    lines {
      id
      merchandise {
        ... on ProductVariant {
          id
          product {
            inExcludedCollection: inAnyCollection(ids: ["gid://shopify/Collection/1", "gid://shopify/Collection/2", "gid://shopify/Collection/3"])
            inVIPCollection: inAnyCollection(ids: ["gid://shopify/Collection/4", "gid://shopify/Collection/5"])
          }
        }
      }
    }
  }
}
```

This input query will only work on the shop where those collections are defined, and there's no way to update them without deploying a new version. Input query variables make these arguments configurable.

#### Step 1: Specify variables for your query

Replace field argument values with a variable with a matching type. For the `ids` argument of `inAnyCollection`, the type is `[ID!]`.

```graphql
# with-input-query-variables.graphql
query Input($excludedCollectionIds: [ID!], $vipCollectionIds: [ID!]) {
  cart {
    lines {
      id
      merchandise {
        ... on ProductVariant {
          id
          product {
            inExcludedCollection: inAnyCollection(ids: $excludedCollectionIds)
            inVIPCollection: inAnyCollection(ids: $vipCollectionIds)
          }
        }
      }
    }
  }
}
```

#### Step 2: Specify values for variables

Input query variables are populated by reading a JSON metafield on the function owner. Each top-level key corresponds to a variable name, and each value matches that variable's type:

```json
{
  "excludedCollectionIds": [
    "gid://shopify/Collection/1",
    "gid://shopify/Collection/2",
    "gid://shopify/Collection/3"
  ],
  "vipCollectionIds": [
    "gid://shopify/Collection/4",
    "gid://shopify/Collection/5"
  ]
}
```

**Tip:** For any variables which do not appear as top level keys in the metafield, a value of `null` is used. If the metafield is not set, all variables use `null`. If a variable is declared as required using `!` and a value of `null` is passed, function execution will fail.

Set the metafield on the function owner (here via `metafieldsSet`):

```graphql
# set-metafield.graphql
mutation SetMetafield {
  metafieldsSet(metafields: [
    {
      namespace: "$app:my-namespace",
      key: "my-key",
      ownerId: "OWNER_ID",
      type: "json",
      value: "{\"excludedCollectionIds\"=>[\"gid://shopify/Collection/1\", \"gid://shopify/Collection/2\", \"gid://shopify/Collection/3\"], \"vipCollectionIds\"=>[\"gid://shopify/Collection/4\", \"gid://shopify/Collection/5\"]}{\"selectedCollectionIds\":[\"gid://shopify/Collection/1\",\"gid://shopify/Collection/2\",\"gid://shopify/Collection/3\"]}"
    }
  ]) {
    metafields {
      id
    }
  }
}
```

**Caution:** Ensure you set metafields on the function owner. For example, Discount API variables would be set on the discount, Checkout Validation API variables on the validation, Cart Transform API variables on the cart transform, and so on. Input query variables do not utilize metafields on the shop or app installation. Use a reserved prefix in your metafield namespace.

#### Step 3: Specify which metafield to use for input queries

Set the values in the `extensions.input.variables` section of the function's configuration file:

```toml
# shopify.extension.toml
[extensions.input.variables]
namespace = "$app:my-namespace"
key = "my-key"
```

If you're using a previous version of the configuration file that doesn't have an `[[extensions]]` section, the configuration section is called `[input.variables]`. Once deployed, your function loads that metafield at runtime to populate your input query variables.

#### Limitations

* Only JSON type metafields are supported.
* Metafields above the size limit won't be returned. Use separate metafields in these cases.
* Input query variables return errors for any GraphQL list variable with a value that exceeds 100 elements.

---

### About network access for Shopify Functions

> Fonte: https://shopify.dev/docs/apps/build/functions/network-access

Network access for Shopify Functions allows you to configure HTTP requests for your functions to use data from an external service as an input to your function logic. It's available primarily for merchants on Shopify for enterprises.

#### Availability of network access for functions

| Function | Availability |
| - | - |
| Cart and Checkout Validation | Shopify for enterprises with custom apps |
| Local Pickup Delivery Option Generator | Shopify for enterprises with custom apps |
| Pickup Point Delivery Option Generator | Development stores and Shopify Plus with custom apps |
| Discount Functions | Shopify for enterprises with custom apps |

Network access for functions needs to be enabled by Shopify, as it's currently not available on dev stores or in a feature preview. Contact Support for more information about which Functions support network access.

#### How it works

Network access enables you to define your HTTP request using the fetch target of the function. When your function is executed, Shopify performs the HTTP request and includes the response in the input of the run target.

1. The `fetch` function target defines an HTTP request based on the existing function input query.
2. The outcome of `FunctionFetchResult` conveys an `HttpRequest` to be executed.
3. Shopify schedules the request with optimizations (see Performance & resilience for caching).
4. Shopify executes network calls to the external service.
5. The `run` function target contains the main logic and has access to the HTTP response through the input query.
6. The outcome of `FunctionRunResult` conveys the function's final output.

#### Alternatives to network access

Instead of fetching data with an external network call, consider retrieving the data from a metafield in your functions. Most objects support metafields, including products, locations, and customers. Fetching data from metafields during checkout is more efficient as it doesn't involve an external network call, and lets you depend on Shopify for the uptime, scalability, and durability of the data storage. Use the GraphQL Admin or Storefront APIs to write metafields on the store before a buyer reaches checkout.

#### API restrictions

* GraphQL Storefront API types are supported only when used in conjunction with the Storefront API `@defer` directive.
* Online store cart Ajax API endpoints aren't supported. If you call an unsupported API endpoint, the function still executes locally, but no actual network request is sent; the run target receives a network response with the status `502 - Not supported`.

---

### Use network access (tutorial)

> Fonte: https://shopify.dev/docs/apps/build/functions/network-access/use-network-access

You can use a Shopify Function to create network requests and handle responses. In this tutorial, you use the Cart and Checkout Validation Function API to query an external system for user-specific cart limits based on the email entered at checkout.

#### What you'll learn

* Define a function that declares an HTTP request to an external system, where additional information is available.
* Use the HTTP response to apply further logic to the function.

#### Requirements

* Ensure your function is allowed to use network access.
* You're using the latest version of Shopify CLI.
* You have an HTTP server (this tutorial uses a NodeJS Express server).

#### Step 1: Create the validation function

```terminal
cd <directory>
```

```terminal
shopify app generate extension --template cart_checkout_validation --name validation-using-network-access
```

**Tip:** Shopify Functions support any language that compiles to WebAssembly. Select the Wasm template option when using a language other than Rust that can conform to the Wasm API.

```terminal
?  What would you like to work in?
> (1) Rust
  (2) JavaScript
  (3) TypeScript
  (4) Wasm
```

Configure the extension definition in `shopify.extension.toml` with two targets: `cart.validations.generate.fetch` (declares a network HTTP request) and `cart.validations.generate.run` (applies logic from the response).

**Rust:**

```toml
api_version = "2025-04"

[[extensions]]
handle = "validation-using-network-access"
name = "t:name"
description = "t:description"
type = "function"
uid = "00b5f691-3209-5775-898c-8da78b3c6e7fe63dacd6"

[[extensions.targeting]]
# An extension identifier.
target = "cart.validations.generate.fetch"
# The local GraphQL file used for code generation.
input_query = "src/cart_validations_generate_fetch.graphql"
# The generated WASM export name for the given target.
export = "cart_validations_generate_fetch"

[[extensions.targeting]]
# An extension identifier.
target = "cart.validations.generate.run"
# The local GraphQL file used for code generation.
input_query = "src/cart_validations_generate_run.graphql"
# The generated WASM export name for the given target.
export = "cart_validations_generate_run"

[extensions.build]
command = "cargo build --target=wasm32-unknown-unknown --release"
watch = [ "src/**/*.rs" ]
path = "target/wasm32-unknown-unknown/release/validation-using-network-access.wasm"
```

**JavaScript:**

```toml
api_version = "2024-04"

[[extensions]]
handle = "validation-using-network-access"
name = "t:name"
description = "t:description"
type = "function"
uid = "00b5f691-3209-5775-898c-8da78b3c6e7fe63dacd6"

[[extensions.targeting]]
# An extension identifier.
target = "cart.validations.generate.fetch"
# The local GraphQL file used for code generation.
input_query = "src/cart_validations_generate_fetch.graphql"
# The generated WASM export name for the given target.
export = "cart-validations-generate-fetch"

[[extensions.targeting]]
# An extension identifier.
target = "cart.validations.generate.run"
# The local GraphQL file used for code generation.
input_query = "src/cart_validations_generate_run.graphql"
# The generated WASM export name for the given target.
export = "cart-validations-generate-run"

[extensions.build]
command = ""
path = "dist/function.wasm"
```

Entry points for both targets:

**Rust:**

```rust
use shopify_function::prelude::*;
use std::process;

pub mod cart_validations_generate_fetch;
pub mod cart_validations_generate_run;

#[typegen("schema.graphql")]
pub mod schema {
    #[query("src/cart_validations_generate_fetch.graphql")]
    pub mod cart_validations_generate_fetch {}

    #[query(
        "src/cart_validations_generate_run.graphql",
        custom_scalar_overrides = {
            "Input.fetchResult.jsonBody" => CartValidationsGenerateRunResult,
        }
    )]
    pub mod cart_validations_generate_run {}
}

fn main() {
    log!("Please invoke a named export.");
    process::abort();
}
```

**JavaScript:**

```js
export * from './cart_validations_generate_fetch';
export * from './cart_validations_generate_run';
```

Project dependencies (`Cargo.toml` / `package.json`):

**Rust:**

```toml
[package]
name = "validation-using-network-access"
version = "1.0.0"
edition = "2021"

[dependencies]
shopify_function = "1.1.0"

[profile.release]
lto = true
opt-level = 'z'
strip = true
```

**JavaScript:**

```json
{
  "name": "validation-using-network-access",
  "version": "0.0.1",
  "license": "UNLICENSED",
  "scripts": {
    "shopify": "npm exec -- shopify",
    "typegen": "npm exec -- shopify app function typegen",
    "build": "npm exec -- shopify app function build",
    "preview": "npm exec -- shopify app function run",
    "test": "vitest"
  },
  "codegen": {
    "schema": "schema.graphql",
    "documents": "src/*.graphql",
    "generates": {
      "./generated/api.ts": {
        "plugins": [
          "typescript",
          "typescript-operations"
        ]
      }
    },
    "config": {
      "omitOperationSuffix": true
    }
  },
  "devDependencies": {
    "vitest": "2.1.9"
  },
  "dependencies": {
    "@shopify/shopify_function": "2.0.0"
  }
}
```

#### Step 2: Retrieve the latest GraphQL schema

```terminal
shopify app function schema --path ./extensions/validation-using-network-access
```

#### Step 3: Create a network request using fetch

The `cart.validations.generate.fetch` target declares a network request to an external system.

**Input query — Rust:**

```graphql
query Input {
  cart {
    buyerIdentity {
      email
      isAuthenticated
    }
    cost {
      totalAmount {
        amount
        currencyCode
      }
    }
  }
}
```

**Input query — JavaScript:**

```graphql
query CartValidationGenerateFetchInput {
  cart {
    buyerIdentity {
      email
      isAuthenticated
    }
    cost {
      totalAmount {
        amount
        currencyCode
      }
    }
  }
}
```

Resulting input:

```json
{
  "cart": {
    "buyerIdentity": {
      "email": "user@example.com",
      "isAuthenticated": false
    },
    "cost": {
      "totalAmount": {
        "amount": "1234.0",
        "currencyCode": "CAD"
      }
    }
  }
}
```

Regenerate types if using JavaScript: `shopify app function typegen`.

**Fetch function — Rust** (`src/cart_validations_generate_fetch.rs`):

```rust
use super::schema;
use shopify_function::prelude::*;
use shopify_function::Result;
use std::collections::BTreeMap;

#[shopify_function]
fn cart_validations_generate_fetch(input: schema::cart_validations_generate_fetch::Input) -> Result<schema::CartValidationsGenerateFetchResult> {
  let mut request: Option<schema::HttpRequest> = None;

  if let Some(buyer_identity) = &input.cart().buyer_identity() {
    if buyer_identity.email().is_some() {
      let http_request = build_request(&input);
      request = Some(http_request);
    }
  }

  Ok(schema::CartValidationsGenerateFetchResult { request })
}

fn build_request(input: &schema::cart_validations_generate_fetch::Input) -> schema::HttpRequest {
  static SERVER_URL: &'static str = "https://server_url.com/api";

  let json_body = JsonValue::Object(BTreeMap::from([(
    "cart".to_string(),
    JsonValue::Object(BTreeMap::from([
      (
        "buyerIdentity".to_string(),
        JsonValue::Object(BTreeMap::from([
          (
            "email".to_string(),
            JsonValue::String(
              input
                .cart()
                .buyer_identity()
                .and_then(|bi| bi.email().map(|s| s.to_string()))
                .unwrap_or_default(),
            ),
          ),
          (
            "isAuthenticated".to_string(),
            JsonValue::Boolean(
              input
                .cart()
                .buyer_identity()
                .map(|bi| *bi.is_authenticated())
                .unwrap_or_default(),
            ),
          ),
        ])),
      ),
      (
        "cost".to_string(),
        JsonValue::Object(BTreeMap::from([(
          "totalAmount".to_string(),
          JsonValue::Object(BTreeMap::from([(
            "amount".to_string(),
            JsonValue::Number(input.cart().cost().total_amount().amount().as_f64()),
          )])),
        )])),
      ),
    ])),
  )]));

  schema::HttpRequest {
    method: schema::HttpRequestMethod::Post,
    url: SERVER_URL.to_string(),
    headers: [schema::HttpRequestHeader {
      name: "accept".to_string(),
      value: "application/json".to_string(),
    }]
    .to_vec(),
    body: None,
    json_body: Some(json_body),
    policy: schema::HttpRequestPolicy {
      read_timeout_ms: 2000,
    },
  }
}
```

**Fetch function — JavaScript:**

```js
import { HttpRequestMethod } from "../generated/api"

export function cartValidationsGenerateFetch(input) {
  let request = null

  if (input.cart.buyerIdentity?.email) {
    request = buildRequest(input)
  }
  return { request }
}

function buildRequest(input) {
  const SERVER_URL = "https://server_url.com/api";

  const body = {
    cart: {
      buyerIdentity: {
        email: input.cart.buyerIdentity?.email,
        isAuthenticated: input.cart.buyerIdentity?.isAuthenticated
      },
      cost: {
        totalAmount: {
          amount: input.cart.cost.totalAmount.amount,
        }
      }
    }
  }

  return {
    method: HttpRequestMethod.Post,
    url: SERVER_URL,
    headers: [
      { name: "accept", value: "application/json" }
    ],
    jsonBody: body,
    policy: {
      readTimeoutMs: 2000
    }
  };
}
```

Output of the fetch target:

```json
{
  "request": {
    "method": "POST",
    "url": "https://example.com/api",
    "headers": [
      {
        "name": "accept",
        "value": "application/json"
      }
    ],
    "jsonBody": {
      "cart": {
        "buyerIdentity": {
          "email": "user@example.com",
          "isAuthenticated": false
        },
        "cost": {
          "totalAmount": {
            "amount": "1234.0"
          }
        }
      }
    },
    "policy": {
      "readTimeoutMs": 2000
    }
  }
}
```

#### Step 4: Handle the network request

The HTTP request is managed by Shopify, as set up by the fetch target. The HTTP response is provided to the run target.

**Business logic** — if the total cart amount exceeds 1,000, the server validates that the buyer is authenticated and that they provide an email authorizing them to place an order; otherwise it returns a validation error:

```js
const handle = (body) => {
  let input = JSON.parse(body)


  if (parseFloat(input.cart.cost.totalAmount.amount) > 1000.0) {
    if (!input.cart.buyerIdentity.isAuthenticated) {
      return json({
        operations: [{
          validationAdd: {
            errors: [{
              message: "There is an order maximum of 1,000 USD for non-authenticated buyers",
              target: "cart"
            }]
          }
        }]
      });
    }


    if (!input.cart.buyerIdentity.email.includes('+allowed@')) {
      return json({
        operations: [{
          validationAdd: {
            errors: [{
              message: "There is an order maximum of 1,000 USD for buyers without established order history",
              target: "cart"
            }]
          }
        }]
      });
    }
  }


  return json({ operations: [] });
};
```

**JWT verification** — every request is accompanied by a verification header, `x-shopify-request-jwt`, containing a JSON Web Token (JWT) signed using the secret client key of the app. This token includes claims that assist in validating that the request was sent from Shopify.

```js
const authenticate = async (request) => {
  const requestJwtHeader = request.headers.get("x-shopify-request-jwt");
  const requestIdHeader = request.headers.get("x-shopify-request-id");

  const secretKey = process.env.APP_SECRET;
  // Include the headers explicitly specified in the HttpRequest of the fetch target.
  const includedVerificationHeaders = process.env.JWT_HEADERS.split(",");
  const shopId = parseInt(process.env.JWT_SHOP_ID);

  // Validate the JWT signature and ensure it hasn't expired.
  const decoded = jwt.verify(requestJwtHeader, secretKey);

  // Validate the JWT claims. The following checks are optional, but they enhance the authenticity of the request.

  // Validate the method
  const method = request.method;
  if (decoded.method !== method) {
    throw new Error("JWT invalid method.");
  }

  // Validate the URL
  const fullUrl = request.url;
  const url_sha256 = await hashWithSHA256(fullUrl);
  if (decoded.url_sha256 !== url_sha256) {
    throw new Error("JWT invalid url.");
  }

  // Validate the headers
  const headers = Array.from(request.headers);
  const canonicalHeaders = headers
    .filter(([k, v]) => includedVerificationHeaders.includes(k.toLowerCase()))
    .map(([k, v]) => `${k.toLowerCase()}:${v}`)
    .sort()
    .join(',');
  const headersSha256 = await hashWithSHA256(canonicalHeaders);
  if (decoded.headers_sha256 !== headersSha256) {
    throw new Error("JWT invalid headers.");
  }

  // Validate the body
  const body = await request.text();
  if (body) {
    const body_sha256 = await hashWithSHA256(body);
    if (decoded.body_sha256 !== body_sha256) {
      throw new Error("JWT invalid body.");
    }
  }

  // Validate the issuer Shop
  if (decoded.iss !== shopId) {
    throw new Error("JWT invalid issuer shop.");
  }

  // Validate the request ID. Each request ID is unique and can be used as a measure to prevent replay attacks.
  if (decoded.x_shopify_request_id !== requestIdHeader) {
    throw new Error("JWT invalid x_shopify_request_id.");
  }

  return body;
};

const hashWithSHA256 = async (input) => {
  const encoder = new TextEncoder();
  const data = encoder.encode(input);
  const hashBuffer = await subtle.digest('SHA-256', data);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
  return hashHex;
};
```

Encoded JWT:

```text
eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOjY4NTY4NDE2NTY3LCJleHAiOjE2OTMyMzczOTEsInhfc2hvcGlmeV9yZXF1ZXN0X2lkIjoiZWNhMjEyNDMtYzA1OC00OWZmLThiMzUtYmUxYTAwNjE2MDRkIiwibWV0aG9kIjoiUE9TVCIsInVybF9zaGEyNTYiOiIxYmI1NmMwZGI1NjA4NDExZGJjZGFhOTAyZWVjMjM4NzgxZjU4NjNmMjQxMDA3NGQ4MDRjYTg5MWYwODFiN2RiIiwiaGVhZGVyc19zaGEyNTYiOiIxZjEyM2Q3YTI0MzFmYWVhMmEwMzljM2VmMGZhZDRmYmQxYzRkNzVmYWVlOWY3ZTQ3OTE4OTJiOGVmZjNmNmVmIiwiYm9keV9zaGEyNTYiOiI5Yjk3NzZkODY2ZWU3NTI2ZmNlOTJiYzlmZjI4OGNjYTIxNjg1MGZmNGE0ZmNhMGJlMzc0ZTMzYjAyNzBiMjI3In0.lce8eWBd-EnxZ6fwvasWGODR0S8nKEGv5Qb2s1teNyE
```

Decoded JWT:

```json
// Header
{
  "alg": "HS256"
}

// Payload
{
  "iss": 68568416567,
  "exp": 1693237391,
  "x_shopify_request_id": "eca21243-c058-49ff-8b35-be1a0061604d",
  "method": "POST",
  "url_sha256": "1bb56c0db5608411dbcdaa902eec238781f5863f2410074d804ca891f081b7db",
  "headers_sha256": "1f123d7a2431faea2a039c3ef0fad4fbd1c4d75faee9f7e4791892b8eff3f6ef",
  "body_sha256": "9b9776d866ee7526fce92bc9ff288cca216850ff4a4fca0be374e33b0270b227"
}
```

**Server example** (Remix app handling POST at `/api`):

```terminal
npx create-remix@latest --template remix-run/remix/templates/remix-javascript
```

```terminal
npm i jsonwebtoken
```

`.env`:

```json
# Found in the Dev Dashboard
APP_SECRET=0123456789abcdef0123456789abcdef

# JWT headers for verification
JWT_HEADERS=accept,content-type

# JWT shop ID
JWT_SHOP_ID=12345678
```

`routes/api.js`:

```js
import { json } from "@remix-run/node";
import jwt from "jsonwebtoken";
import { TextEncoder } from "util";
import { subtle } from "crypto";

export const action = async ({ request }) => {
  if (request.method.toUpperCase() !== 'POST') {
    return json({ error: 'Invalid request method. Only POST requests are allowed.' }, { status: 405 });
  }

  let body;

  try {
    body = await authenticate(request);
  } catch (err) {
    return json({ error: err.message }, { status: 401 });
  }

  return handle(body);
};

const authenticate = async (request) => {
  const requestJwtHeader = request.headers.get("x-shopify-request-jwt");
  const requestIdHeader = request.headers.get("x-shopify-request-id");

  const secretKey = process.env.APP_SECRET;
  // Include the headers explicitly specified in the HttpRequest of the fetch target.
  const includedVerificationHeaders = process.env.JWT_HEADERS.split(",");
  const shopId = parseInt(process.env.JWT_SHOP_ID);

  // Validate the JWT signature and ensure it hasn't expired.
  const decoded = jwt.verify(requestJwtHeader, secretKey);

  // Validate the JWT claims. The following checks are optional, but they enhance the authenticity of the request.

  // Validate the method
  const method = request.method;
  if (decoded.method !== method) {
    throw new Error("JWT invalid method.");
  }

  // Validate the URL
  const fullUrl = request.url;
  const url_sha256 = await hashWithSHA256(fullUrl);
  if (decoded.url_sha256 !== url_sha256) {
    throw new Error("JWT invalid url.");
  }

  // Validate the headers
  const headers = Array.from(request.headers);
  const canonicalHeaders = headers
    .filter(([k, v]) => includedVerificationHeaders.includes(k.toLowerCase()))
    .map(([k, v]) => `${k.toLowerCase()}:${v}`)
    .sort()
    .join(',');
  const headersSha256 = await hashWithSHA256(canonicalHeaders);
  if (decoded.headers_sha256 !== headersSha256) {
    throw new Error("JWT invalid headers.");
  }

  // Validate the body
  const body = await request.text();
  if (body) {
    const body_sha256 = await hashWithSHA256(body);
    if (decoded.body_sha256 !== body_sha256) {
      throw new Error("JWT invalid body.");
    }
  }

  // Validate the issuer Shop
  if (decoded.iss !== shopId) {
    throw new Error("JWT invalid issuer shop.");
  }

  // Validate the request ID. Each request ID is unique and can be used as a measure to prevent replay attacks.
  if (decoded.x_shopify_request_id !== requestIdHeader) {
    throw new Error("JWT invalid x_shopify_request_id.");
  }

  return body;
};

const hashWithSHA256 = async (input) => {
  const encoder = new TextEncoder();
  const data = encoder.encode(input);
  const hashBuffer = await subtle.digest('SHA-256', data);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
  return hashHex;
};

const handle = (body) => {
  let input = JSON.parse(body)

  if (parseFloat(input.cart.cost.totalAmount.amount) > 1000.0) {
    if (!input.cart.buyerIdentity.isAuthenticated) {
      return json({
        operations: [{
          validationAdd: {
            errors: [{
              message: "There is an order maximum of $1,000 for non-authenticated buyers",
              target: "cart"
            }]
          }
        }]
      });
    }

    if (!input.cart.buyerIdentity.email.includes('+allowed@')) {
      return json({
        operations: [{
          validationAdd: {
            errors: [{
              message: "There is an order maximum of $1,000 for buyers without established order history",
              target: "cart"
            }]
          }
        }]
      });
    }
  }

  return json({ operations: [] });
};
```

Start the server with `shopify app dev`. The server must be accessible on the public internet.

#### Step 5: Create the validation logic

The `cart.validations.generate.run` target applies logic from the network response.

**Input query — Rust:**

```graphql
query Input {
      fetchResult {
        status
        dateHeader: header(name: "date") {
          value
        }
        cacheControlHeader: header(name: "cache-control") {
          value
        }
        jsonBody
      }
    }
```

**Input query — JavaScript:**

```graphql
query CartValidationsGenerateRunInput {
      fetchResult {
        status
        dateHeader: header(name: "date") {
          value
        }
        cacheControlHeader: header(name: "cache-control") {
          value
        }
        jsonBody
      }
    }
```

Resulting input:

```json
{
      "fetchResult": {
        "status": 200,
        "dateHeader": {
          "value": "Mon, 08 Jul 2024 19:24:21 GMT"
        },
        "cacheControlHeader": {
          "value": "max-age=604800"
        },
        "jsonBody": {
          "operations": [{
            "validationAdd": {
              "errors": [{
                "message": "There is an order maximum of $1,000 for non-authenticated customers",
                "target": "cart"
              }]
            }
          }]
        }
      }
    }
```

**Run function — Rust:**

```rust
use super::schema;
    use shopify_function::prelude::*;
    use shopify_function::Result;

    #[shopify_function]
    fn cart_validations_generate_run(input: schema::cart_validations_generate_run::Input) -> Result<schema::CartValidationsGenerateRunResult> {
        let Some(fetch_result) = input.fetch_result() else {
            // Optimization for when there are no requests.
            // In this simple example, there are no fallbacks, but there is room to implement one if needed.
            // See fetch.rs.
            return Ok(schema::CartValidationsGenerateRunResult { operations: vec![] });
        };

        // When the server returns an unexpected response.
        // Optionally: Apply a local fallback error message.
        if *fetch_result.status() != 200 {
            panic!("Server response unprocessable (status)");
        }

        let json_body = fetch_result.json_body().expect("Missing response body");

        return Ok(json_body.clone());
    }
```

**Run function — JavaScript:**

```js
export function cartValidationsGenerateRun(input) {
      const fetchResult = input.fetchResult;

      if (!fetchResult) {
        return { operations: [] };
      }

      if (fetchResult.status !== 200) {
        throw new Error("Server response unprocessable (status)");
      }

      if (!fetchResult.jsonBody) {
        throw new Error("Server response unprocessable (body)");
      }

      return fetchResult.jsonBody;
    }
```

Output:

```json
{
  "operations": [
    {
      "validationAdd": {
        "errors": [
          {
            "message": "There is an order maximum of $1,000 for non-authenticated customers",
            "target": "cart"
          }
        ]
      }
    }
  ]
}
```

#### Steps 6–9: Preview, activate, test, and view logs

* **Preview:** ensure `build.watch` is configured for non-JS languages, then `shopify app dev` and follow the prompts.
* **Activate:** in the Shopify admin go to **Settings > Checkout**, in **Checkout Rules** click **Add rule**, select the validation, click **Activate**, and **Save**. Optionally control behavior on runtime exceptions via **Allow all customers to submit checkout**.
* **Test:** create a cart over $1,000 without logging in, proceed to checkout, verify a warning displays and progress is blocked; confirm `cartLinesAdd` mutation `userErrors` contains the message; review function executions in `shopify app dev`; replay locally with `shopify app function replay`.
* **View logs:** use Shopify CLI log streaming to see network access logs, including request execution times and caching information.

---

### About performance and resilience (network access)

> Fonte: https://shopify.dev/docs/apps/build/functions/network-access/performance-and-resilience

Network access gives your app specific control points to declare what information you want to request. Shopify handles the execution of the network operations.

#### Timeouts

Network requests have a maximum execution timeout. The permissible range is between 100ms and 2000ms. Configure the timeout value using the `HttpRequestPolicy` input of an `HttpRequest`:

```graphql
# schema.graphql
input HttpRequestPolicy {
   """
   Read timeout in milliseconds.
   """
   readTimeoutMs: Int!
}
```

#### Request cache

Customers engage with Shopify multiple times throughout their checkout journey. To ensure a stable and efficient experience, Shopify implements a network cache layer. The cache key comprises all of the HTTP request attributes (method, URL, headers, and body). Cache isolation is enforced between stores.

Successful responses are cached for up to 300 seconds. Connection errors and responses with 5xx and 429 status codes are cached for up to 30 seconds. Persistent connection errors may trigger a circuit breaker per host and port, lasting more than 20 seconds. These values are subject to change. **Cache-Control headers are not honored.**

**Increasing the cache hit rate** — because the request cache is shared across all checkout sessions within the same store, leveraging caching reduces buyer wait times and alleviates load on external servers. Requests broad in scope are particularly suited for this. For example, when retrieving pickup points based on delivery address coordinates, slightly reducing the precision of latitude and longitude covers a broader grid area:

**Rust** (`src/fetch.rs`):

```rust
fn fetch(input: fetch::input::ResponseData) -> Result<fetch::output::FunctionFetchResult> {
        let delivery_address = &input.delivery_address;

        if let (Some(latitude), Some(longitude)) = (&delivery_address.latitude, &delivery_address.longitude) {
            let latitude_with_reduced_precision = format!("{:.3}", latitude);
            let longitude_with_reduced_precision = format!("{:.3}", longitude);

            return Ok(fetch::output::FunctionFetchResult {
                request: Some(fetch::output::HttpRequest {
                    method: fetch::output::HttpRequestMethod::GET,
                    url: format!(
                        "https://api.pickuppoint.io/search?lat={}&lon={}",
                        latitude_with_reduced_precision,
                        longitude_with_reduced_precision
                    ),
                    headers: vec![],
                    body: None,
                    policy: fetch::output::HttpRequestPolicy {
                        read_timeout_ms: 500,
                    },
                }),
            });
        }

        Ok(fetch::output::FunctionFetchResult { request: None })
    }
```

**JavaScript:**

```js
export function fetch(input) {
        let { latitude, longitude } = input.deliveryAddress;

        if (latitude && longitude) {
            let latitudeWithReducedPrecision = latitude.toFixed(3);
            let longitudeWithReducedPrecision = longitude.toFixed(3);

            return {
                request: {
                    method: 'GET',
                    url: `https://api.pickuppoint.io/search?lat=${latitudeWithReducedPrecision}&lon=${longitudeWithReducedPrecision}`,
                    headers: [],
                    body: null,
                    policy: {
                        readTimeoutMs: 500,
                    },
                },
            };
        }

        return { request: null };
    }
```

This ensures coordinates such as `(45.4193479, -75.6965198)` and `(45.419534, -75.6967035)` generate identical requests:

```json
{
          "method": "GET",
          "url": "https://pickuppoints.com/search?lat=45.419&lon=-75.696",
          "headers": [],
          "body": null,
          "policy": {
              "readTimeoutMs": 500
          }
      }
```

#### Error management

During a network call, various issues can occur: DNS errors, connection errors, SSL errors, gateway errors, encoding errors, and timeouts. Shopify categorizes and repackages the possible error paths into a `fetchResult: HttpResponse` with a `5xx` status code:

* **Encoding error**: `{ "status": 501, "body": "501 Encoding charset not supported. Use 'UTF-8' encoding." }`
* **Timeout error**: `{ "status": 504, "body": "504 Gateway Timeout" }`
* **Connection error**: `{ "status": 502, "body": "502 Bad Gateway (Connection Failed)" }`
* **SSL error**: `{ "status": 502, "body": "502 Bad Gateway (SSL Error)" }`
* **Compression error**: `{ "status": 502, "body": "502 Bad Gateway (Data Compression Error)" }`
* **Response size error**: `{ "status": 502, "body": "502 Bad Gateway (Headers and body exceed 100KB limit)" }`
* **Unsupported context**: `{ "status": 502, "body": "Network access isn't supported in this context." }`

You can configure the function to either apply a locally defined fallback or to throw an error (which applies the default platform fallback):

**Rust** (`src/run.rs`):

```rust
fn run(input: run::input::ResponseData) -> Result<run::output::FunctionRunResult> {
        let fetch_result = input.fetch_result.unwrap();

        // Fallback on errors
        if fetch_result.status != 200 {
            let fallback_result = "..."
            return Ok(run::output::FunctionRunResult { fallback_result });
        }

        // Successful request code...
    }
```

**JavaScript:**

```js
export function run(input) {
      const fetchResult = input.fetchResult;

      // Fallback on errors
      if (fetchResult.status !== 200) {
        const fallbackResult = "..."
        return { fallbackResult };
      }

      // Successful request code...
    }
```

#### Network retry

To handle transient failures, Shopify implements an automated retry mechanism. If the failure is temporary and the retried call is successful, the system recovers transparently. If the retried call failed, the communication error is exposed to the function's subsequent target.

---

### Test and debug Shopify Functions

> Fonte: https://shopify.dev/docs/apps/build/functions/test-debug-functions

This guide describes recommended practices for testing and debugging functions. Depending on your needs, you'll use a combination of testing on Shopify, local execution, and unit tests.

#### Testing on your dev store

When you run `app dev`, Shopify CLI streams execution logs for your functions to your terminal, and writes details of the function execution input, output, and more to your filesystem. The `app logs` command can also stream logs for a dev store with additional capabilities such as log filtering and JSON output. All function runs for dev stores are logged in your Dev Dashboard.

1. For non-JS/TS languages, configure `build.watch` in your function extension configuration.
2. Start the dev preview: `shopify app dev`. Keep it running as you work; changes to a watched file rebuild the function and update the extension's drafts.
3. Follow the CLI prompts to preview your app on your development store.
4. Enable the function and test it on your dev store (steps depend on the function API; see use case tutorials).
5. Add debugging logs by writing to `log!` in Rust, `console.log` in JavaScript, or `shopify_function_log_new_utf8_str` in other languages.

   > **Caution:** Always remove debugging logs before deploying and releasing your function.

6. When your function executes, review debug logs in the `app dev` output.
7. To review execution details, click **Open log file** in the terminal output, or navigate to the output file path.

   > **Info:** Windows Terminal users can enable hyperlinks in Shopify CLI by setting the `FORCE_HYPERLINK=1` environment variable.

8. To stream detailed logs for a single function:

   ```terminal
   shopify app logs --source extensions.<function_handle>
   ```

   > **Info:** You can list log sources for your app with the `app logs sources` command.

#### Execute the function locally using Shopify CLI

Shopify CLI can mimic production execution of your function's WebAssembly module — allowing faster local testing of function output and measuring against function performance restrictions.

The `app function replay` command quickly executes the function using input from a previously logged execution, and re-executes as you make changes. The `app function run` command performs a single function execution using a provided JSON input.

> **Info:** Use the `--json` argument of `app function run` to get function measurements and output as JSON, for automated testing and scripts.

**Replay a function locally:**

1. In the output of `app dev`, copy the six-character log file identifier (e.g. `9f1f0e`).
2. Open a separate terminal window and `cd` to your function extension folder.
3. Use the `--log` argument:

   ```terminal
   shopify app function replay --log <log_file_identifier>
   ```

   > **Info:** Without a log file identifier, run `app function replay` and select from a list of recent executions.

4. After your function has the desired output, re-test on your dev store.

#### Writing unit tests for functions

Writing unit tests lets you validate your function logic repeatedly. Unit tests are also useful for debugging via step debugging using native tooling.

> **Caution:** Unit tests don't run in WebAssembly, which in rare cases might cause different results than what's found in production.

You can retrieve a valid input JSON result for your input query from the log files output by `app dev`, the output of `app logs`, function run logs in your Dev Dashboard, or by constructing your own mock input.

Recommended tools by language:

* For Rust, the `shopify_function` crate provides a `run_function_with_input` utility to simplify unit testing with `cargo test`.
* For JavaScript or TypeScript, use Vitest. Input JSON can be used directly in your JavaScript code to execute the function.

#### Writing Wasm integration tests for functions

Use integration tests to validate the behaviour of your function's WebAssembly module — that the compiled binary in production continues to produce the expected output for a given input. When you generate a function from a template, it contains a `tests/` directory:

* `default.test.js` — The test file that compiles your function and runs it against fixtures.
* `fixtures/log.json` — A default test fixture with sample input and expected output.

The integration tests use the `@shopify/shopify-function-test-helpers` package, which provides:

* `buildFunction()` — Compiles your function source code to WebAssembly.
* `loadFixture()` — Loads and parses fixture JSON files.
* `validateTestAssets()` — Validates input queries and fixtures against your GraphQL schema.
* `runFunction()` — Executes your compiled WebAssembly module with test inputs.

Run integration tests with `npm test` (you might need `npm install` in your app root first). The default test ensures: your function compiles to WebAssembly; your input query is valid; each fixture has valid input and output; and the WebAssembly module produces the expected output.

**Add additional test fixtures** — create additional `.json` files in `tests/fixtures/`. Each fixture file must contain:

* **`export`** — The WebAssembly export function name.
* **`target`** — The function API target (e.g. `cart.transform.run`, `payment.customization.run`). Determines which GraphQL schema validates your fixture.
* **`input`** — The input data matching your function's input query GraphQL schema.
* **`output`** — The expected output.

**Create a fixture from logged function execution** — when you run `app dev`, Shopify CLI automatically creates log files in your app's `.shopify/logs` directory; drag and drop them into `tests/fixtures/`. Or manually create them from Dev Dashboard executions:

```json
{
  "payload": {
    "export": "your-export-name",
    "target": "your.target.name",
    "input": {
      // Paste the input JSON from your log here
    },
    "output": {
      // Paste the expected output JSON from your log here
    }
  }
}
```

#### Debugging functions in production

For production stores, all function runs are visible in your Dev Dashboard. Run details are available when your app has the access scopes required by the function's input query. When you open a run that your app can't access, the Dev Dashboard lists the scopes it's missing. You can also reproduce the issue on a dev store or with one of the local testing options.

---

### Monitoring and handling errors in production

> Fonte: https://shopify.dev/docs/apps/build/functions/monitoring-and-errors

This guide describes how you can monitor and debug your functions in production.

#### How it works

Functions can fail by raising an exception, exceeding memory or time limits, or returning data that doesn't match the schema of the specific Function API. In other cases, the function can run successfully but return unexpected results due to a bug. To aid in debugging, information about each function run is stored and made available through the Dev Dashboard — metadata (when the run occurred, the shop), and function run details (input and output).

#### Access function run details

The visibility of these details is controlled by the access scopes a merchant has granted to your app. Shopify derives the scopes required to view a run from the fields your function's input query reads. If run details are hidden, your app is missing required scopes. Choose the request method that fits your use case:

* **Request scopes during app installation** — for scopes your app consistently needs.
* **Request protected customer data scopes when accessing customer data** — some fields (customer details and addresses) require protected customer data access.
* **Use optional scopes for occasional or debugging access** — merchants can grant or revoke optional scopes without reinstalling your app.

After the required scopes are granted, run details are visible the next time you view the log.

**Note:** If you have access to the store as a staff member or collaborator, you can see all run details regardless of your app's access scopes. Run details on your organization's dev stores are always accessible.

#### Debug a function

From the app's **Logs** section in your Dev Dashboard:

1. Go to **Apps**.
2. Click the app you deployed your function to.
3. Click **Logs**.
4. Click **Functions**.

The function details page contains a list of function runs.

**Note:** Functions are deterministic — any time they execute with a given input, they always return the same output. You can copy the input in a function run and accurately reproduce the failing execution locally using Shopify CLI or a unit test.

Run details include:

1. **Input (STDIN)**: The JSON formatted input that you can copy to your clipboard.
2. **Output (STDOUT)**: Contains the output, if the function returned output.
3. **Logs (STDERR)**: Contains the logs of the function.

   **Caution:** Function logs are truncated after 1 kB.

#### List of errors

| Error name | Description |
| - | - |
| `RuntimeError` | The function raised an exception or exited with a non-zero status code during execution. |
| `InstructionCountLimitExceededError` | Shopify stopped the function after it exceeded the maximum instruction count. |
| `StackMemoryLimitExceededError` | Shopify stopped the function after it exceeded the maximum stack memory size. |
| `LinearMemoryLimitExceededError` | Shopify stopped the function after it exceeded the maximum linear memory size. |
| `InvalidOutputError` | The function returned malformed or invalid output. |
| `OutputTooLargeError` | The function's output exceeded the maximum allowed output size. |
| `InputSizeLimitExceededError` | The function's input exceeded the maximum allowed input size. |
| `InputListSizeLimitExceededError` | A variable array in the function's input query exceeded the maximum allowed list length. |
| `InvalidModuleError` | The Wasm module failed validation at deployment. |
| `InvalidInputQueryError` | The function's input query is invalid for its API version. |
| `UnsupportedVersionError` | The function is using an unsupported API version. It has been removed from all merchant stores. Upgrade to a later API version and redeploy your app. |
| `InvalidVariableValueError` | The function's input query variables metafield was invalid. This can occur if the metafield value doesn't conform to the variables definitions, or if the metafield type isn't `json`. |

---

### Migrating from Shopify Scripts to Shopify Functions

> Fonte: https://shopify.dev/docs/apps/build/functions/migrating-from-shopify-scripts

> **Deprecated:** Shopify Scripts will be sunset on June 30, 2026. All existing Shopify Scripts will stop functioning after this date. Migrate your scripts to Shopify Functions before the deadline to avoid disruption to your store's checkout, shipping, and payment customizations.

Shopify Scripts allow you to customize cart behavior, shipping, and payment methods. With Shopify Functions, these customizations are handled through dedicated Function APIs that offer better performance and flexibility. This guide shows how to migrate without disrupting customers.

#### Function APIs mapping

| Shopify Script type | Shopify Function API | Use case |
| - | - | - |
| Line item scripts | Discounts API | Apply discounts to products, or the entire cart. |
| Line item scripts | Cart Transform API | Modify cart line items (bundle, merge, or add items). |
| Line item scripts | Cart and Checkout Validation API | Validate cart contents and block checkout under specific conditions. |
| Shipping scripts | Delivery Customization API and Discounts API | Hide, rename, or reorder delivery methods, and apply discounts to delivery methods. |
| Payment scripts | Payment Customization API | Hide, rename, or reorder payment methods. |

#### Step 1: Create a preview link for your existing script

1. In the Shopify admin, go to **Apps > Script Editor**.
2. Create a temporary script with the following code but don't publish it:

   ```
   Output.cart = Input.cart
   ```

3. Save the script as a draft and note the preview URL:

   ```
   https://{your-store}.myshopify.com/admin/scripts/preview?script_id={script_id}
   ```

   When accessed, this preview link runs the temporary passthrough script instead of your published script, effectively disabling your current script's logic for that session.

#### Step 2: Add testing logic to your Function

Target specific test users; the most reliable method is using customer tags.

1. In the Shopify admin, go to **Customers** and add a tag like `TESTER` to customers who should experience the new Function behavior.
2. In your Function's input query, include customer tag information:

   ```graphql
   query Input {
     cart {
       buyerIdentity {
         customer {
           hasAnyTag(tags: ["TESTER"])
         }
       }
       # ... rest of your query
     }
   }
   ```

Conditional logic:

**Rust:**

```rust
// Check if the customer has the TESTER tag
let has_tester_tag = input
    .cart()
    .buyer_identity()
    .and_then(|bi| bi.customer())
    .map(|customer| customer.has_any_tag())
    .unwrap_or(&false);

if *has_tester_tag {
    // Apply new Function logic here
    // ... your function implementation
} else {
    // Return no changes (let existing script handle it)
    return Ok(FunctionRunResult { operations: vec![] });
}
```

**JavaScript:**

```javascript
const customer = input.cart.buyerIdentity?.customer;
const hasTesterTag = customer?.hasAnyTag ?? false;

if (hasTesterTag) {
    // Apply new Function logic here
    // ... your function implementation
} else {
    // Return no changes (let existing script handle it)
    return { operations: [] };
}
```

#### Step 3: Deploy and test in production

* **Development testing:** test thoroughly in a dev store (`shopify app dev`); verify the Function behaves identically to your existing Script.
* **Option A: App with configuration UI** — use the app to enable and configure the Function in production.
* **Option B: GraphiQL deployment** (works best for Functions that don't require ongoing merchant configuration). Use the Shopify GraphiQL App to enable the Function directly:

  ```graphql
  query getFunctions {
    shopifyFunctions(first: 100) {
      edges {
        node {
          id
          title
          apiType
        }
      }
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }
  ```

  Use the Function's `id` in the appropriate creation mutation (e.g. `discountAutomaticAppCreate` or `deliveryCustomizationCreate`).
* **Testing process:** tag test users with `TESTER`; have them access your store using the preview link from Step 1 to disable the existing script; verify the Function produces the same results as the original Script for tagged users while untagged users continue with the original behavior.

#### Step 4: Complete the migration

1. **Remove testing code** — remove the customer tag conditional logic.
2. **Deploy the final version:** `shopify app deploy`
3. **Deactivate the Script** — in **Apps > Script Editor**, unpublish your existing Script.

#### Best practices

* Always test in a dev store before deploying to production.
* Keep the testing period short to minimize code complexity.
* Monitor your store's performance and error logs after migration.
* Have a rollback plan ready if issues arise.
* Document any differences in behavior between Scripts and Functions.
* Test edge cases that might behave differently between Scripts and Functions.

#### Troubleshooting

* **Function not triggering**: Verify the Function is properly enabled and configured.
* **Different behavior**: Check for differences in input data structure between Scripts and Functions.

---

## Discounts (Product, Order, Shipping)

### Discount Function API

> Fonte: https://shopify.dev/docs/api/functions/latest/discount

The Discount Function API provides a unified schema for creating function extensions. A single function processes one discount (either code-based or automatic), but can apply savings across three discount classes: product, order, and shipping. For example, one discount can simultaneously reduce both order total and delivery costs.

Shopify Functions enable you to customize Shopify's backend logic. The Discount Function API integrates this logic into the checkout flow.

**Note:** You can activate a maximum of 25 discount functions on each store. All discount functions run concurrently, and have no knowledge of each other. The potential discount that a function outputs can be combined with the candidate from another discount, in alignment with the combination and stacking rules set on the discount node.

#### Use Cases

* Exclusions, where the discount doesn't apply to some cart lines in the order.
* Tiered discounts on products, orders, and shipping when orders include qualifying item, subtotal, and delivery requirements.
* Discount to cartlines that contain specific properties, such as an engraving on a ring.

#### Function Target — Checkout — Compatibility with Shopify Surfaces

| Surface | Status |
|---------|--------|
| B2B | Supported |
| Cart | Supported |
| Checkout | Supported |
| Create Order API | Not supported |
| Draft Order (Admin) | Partially supported — Discount functions with network access aren't supported on draft orders |
| Draft Order (Checkout) | Partially supported — Discount functions with network access aren't supported on draft orders |
| Order Edit (Admin) | Not supported |
| Order Edit (Checkout) | Partially supported — The function isn't re-run when editing an order |
| POS | Supported |
| Pre-order and Try Before You Buy | Not supported |
| Shopify Admin | Supported |
| Storefront | Supported |
| Storefront Accelerated Checkout | Supported |
| Subscription (Recurring Orders) | Partially supported — The function isn't re-run when recurring orders are created. Any shipping discount applied to the origin order defaults to a 100% shipping discount on recurring orders, regardless of the original discount value |

**Fetch Target — Limited access:** limited to custom apps installed on Shopify Plus and Enterprise stores. You'll also need to request network access for Functions, as it's not currently available on development stores or in a development preview.

#### Getting Started

```terminal
shopify app generate extension --template discount
```

Tutorial: [Build a discount function](https://shopify.dev/docs/apps/build/discounts/build-product-discount-function)

#### Targets

A target is an identifier in `shopify.extension.toml` that specifies where you're injecting code. The name begins with a broad Shopify context and ends with the behavior of the extensible element.

**Note:** You can't configure discount classes from a checkout UI extension. Discount classes are assigned based on their associated Discount Function targets: `OrderDiscountCandidateTarget`, `ProductDiscountCandidateTarget`, and `DeliveryDiscountCandidateTarget`.

#### Cart Run Target — `cart.lines.discounts.generate.run`

The run target calculates and applies discounts to cart lines, orders, and shipping based on the provided cart context and discount configuration, including metafields. When your function is executed, Shopify provides the cart context as input — cart lines, prices, quantities, buyer identity, and optionally fetch results from external providers. The target returns an ordered list of operations for calculating discounts.

##### Input (full schema)

The `Input` object is the complete GraphQL schema that your function can query. Your function only receives the fields you request in the input query.

**`cart`** (Cart!, required) — The cart where the Function is running.

* `attribute(key: String)` — The custom attributes associated with a cart (key-value pairs); fields `key` (String!), `value` (String).
* `billingAddress` (MailingAddress) — `address1`, `address2`, `city`, `company`, `countryCode` (CountryCode), `firstName`, `lastName`, `latitude` (Float), `longitude` (Float), `name`, `phone`, `provinceCode`, `zip`, `market` (Market, deprecated).
* `buyerIdentity` (BuyerIdentity) — Information about the customer interacting with the cart.
  * `customer` (Customer): `amountSpent` (MoneyV2!: `amount` Decimal!, `currencyCode` CurrencyCode!), `displayName` (String!), `email`, `firstName`, `hasAnyTag(tags:[String!]!)` (Boolean!), `hasTags(tags:[String!]!)` ([HasTagResponse!]! with `hasTag`/`tag`), `id` (ID!), `lastName`, `metafield` (Metafield), `numberOfOrders` (Int!).
  * `email` (String), `isAuthenticated` (Boolean!), `phone` (String).
  * `purchasingCompany` (PurchasingCompany): `company` (Company! — `createdAt`, `externalId`, `id`, `metafield`, `name`, `updatedAt`), `contact` (CompanyContact — `createdAt`, `id`, `locale`, `title`, `updatedAt`), `location` (CompanyLocation! — `createdAt`, `externalId`, `id`, `locale`, `metafield`, `name`, `ordersCount` Int!, `totalSpent` MoneyV2!, `updatedAt`).
* `cost` (CartCost!) — `subtotalAmount` (MoneyV2!), `totalAmount` (MoneyV2!), `totalDutyAmount` (MoneyV2), `totalTaxAmount` (MoneyV2).
* `deliverableLines` ([DeliverableCartLine!]!) — `attribute` (Attribute), `id` (ID!), `merchandise` (Merchandise! — CustomProduct or ProductVariant), `quantity` (Int!).
* `deliveryGroups` ([CartDeliveryGroup!]!) — A collection of items grouped by shared delivery characteristics. In the legacy Order Discount and Product Discount APIs, `cart.deliveryGroups` is always an empty array; use the Discount Function API to apply discounts to shipping costs. Each group: `cartLines` ([CartLine!]! — `attribute`, `cost` CartLineCost!, `discountAllocations` [DiscountAllocation!]!, `id`, `merchandise`, `parentRelationship` CartLineParentRelationship, `quantity`, `sellingPlanAllocation` SellingPlanAllocation), `deliveryAddress` (MailingAddress), `deliveryOptions` ([CartDeliveryOption!]! — `code`, `cost` MoneyV2!, `deliveryMethodType` DeliveryMethod! {LOCAL, NONE, PICK_UP, PICKUP_POINT, RETAIL, SHIPPING}, `description`, `handle`, `title`), `discountAllocations` ([DiscountAllocation!]!), `groupType` (CartDeliveryGroupType! {ONE_TIME_PURCHASE, SUBSCRIPTION}), `id` (ID!), `selectedDeliveryOption` (CartDeliveryOption).
  * `DiscountAllocation`: `discountApplication` (DiscountApplication! — `allocationMethod` {ACROSS, EACH}, `metafield`, `targetSelection` {ALL, ENTITLED, EXPLICIT}, `targetType` {LINE_ITEM, SHIPPING_LINE}, `totalAllocatedAmount` MoneyV2!, `value` PricingValue! [MoneyV2 or PricingPercentageValue]), `discountedAmount` (MoneyV2!).
* `discountApplications` ([DiscountApplication!]!) — The discounts applied to the cart.
* `lines` ([CartLine!]!) — The items in a cart that the customer intends to purchase.
* `localizedFields(keys:[LocalizedFieldKey!]!)` ([LocalizedField!]!) — Additional fields required for international orders (customs/tax info). Keys include SHIPPING_CREDENTIAL_* and TAX_CREDENTIAL_* values (BR, CL, CN, CO, CR, EC, ES, GT, ID, IT, KR, MX, MY, PE, PT, PY, TR, TW, plus TAX_CREDENTIAL_TYPE_*, TAX_CREDENTIAL_USE_MX, TAX_EMAIL_IT). Fields: `key`, `title`, `value`.
* `metafield` (Metafield) — A custom field on the cart.
* `poNumber` (String) — A purchase order number for B2B transactions.
* `retailLocation` (Location) — `address` (LocationAddress! — `address1`, `address2`, `city`, `country`, `countryCode`, `formatted` [String!]!, `latitude`, `longitude`, `phone`, `province`, `provinceCode`, `zip`), `handle`, `id`, `metafield`, `name`.

**`discount`** (Discount!, required) — The discount node that owns the Shopify Function. `discountClasses` ([DiscountClass!]! {ORDER, PRODUCT, SHIPPING}), `metafield` (Metafield).

**`enteredDiscountCodes`** ([EnteredDiscountCode!]!, required) — Discount codes entered by the buyer at checkout, excluding gift cards. For `cart.lines.discounts.generate.run` and `cart.delivery-options.discounts.generate.run`, codes are validated (not deleted, active status, eligible for the current cart). For fetch targets, all entered codes are included (excluding gift cards). Fields: `code` (String!), `rejectable` (Boolean!).

**`fetchResult`** (HttpResponse) — The result of the fetch target. Only available in `cart.lines.discounts.generate.run` and `cart.delivery-options.discounts.generate.run`. Fields: `body` (String), `header(name:String!)` (HttpResponseHeader: `name`, `value`), `jsonBody` (JSON), `status` (Int!), `headers` (deprecated).

**`localization`** (Localization!, required) — `country` (Country! — `isoCode` CountryCode!), `language` (Language! — `isoCode` LanguageCode!), `market` (deprecated).

**`presentmentCurrencyRate`** (Decimal!, required) — The exchange rate used to convert discounts between the shop's default currency and the currency that displays to the customer.

**`shop`** (Shop!, required) — `localTime` (LocalTime! — `date`, `dateTimeAfter`, `dateTimeBefore`, `dateTimeBetween`, `timeAfter`, `timeBefore`, `timeBetween`), `metafield`, `metaobject(handle: MetaobjectHandleInput | id: ID)` (only app-owned metaobjects with the `$app` reserved prefix; fields `field(key:String!)` {jsonValue, key, type, value}, `handle`, `type`).

**`triggeringDiscountCode`** (String) — The discount code entered by a customer that caused the Discount Function to run. Only available in `cart.lines.discounts.generate.run` and `cart.delivery-options.discounts.generate.run`.

##### Cart Run Function — Output: `CartLinesDiscountsGenerateRunResult`

The object contains the operations to generate, validate, and apply discounts to the cart.

**`operations`** ([CartOperation!]!, required):

* **EnteredDiscountCodesAcceptOperation** — Selects which entered discount codes to accept (validate codes from external systems). `codes` ([DiscountCode!]! with `code` String!).
* **EnteredDiscountCodesRejectOperation** — Rejects entered discount codes with a custom message. Can only be used if the function is backed by an automatic discount. `codes` ([RejectedDiscountCode!]!), `message` (String!).
* **OrderDiscountsAddOperation** — Applies order discounts that share a selection strategy. `candidates` ([OrderDiscountCandidate!]!), `selectionStrategy` (OrderDiscountSelectionStrategy! {FIRST, MAXIMUM}).
  * `OrderDiscountCandidate`: `associatedDiscountCode` (AssociatedDiscountCode — `code`), `conditions` ([Condition!] — CartLineMinimumQuantity {ids, minimumQuantity}, CartLineMinimumSubtotal {ids, minimumAmount}, OrderMinimumSubtotal {excludedCartLineIds, minimumAmount}), `message` (String), `targets` ([OrderDiscountCandidateTarget!]! — OrderSubtotalTarget {excludedCartLineIds}), `value` (OrderDiscountCandidateValue!).
* **ProductDiscountsAddOperation** — Applies product discounts that share a selection strategy. `candidates` ([ProductDiscountCandidate!]!), `selectionStrategy` (ProductDiscountSelectionStrategy!).

#### Delivery Run Target — `cart.delivery-options.discounts.generate.run`

The run target responsible for generating the discount on shipping costs using Shopify data, hardcoded values, or fetch results. It evaluates carts against discount rules, calculates applicable reductions, and returns the final shipping discount.

**Note:** Checkouts and orders can include multiple delivery methods (shipping and pickup in the same order). Iterate over all delivery groups or fulfillment orders to determine the delivery method for each; don't assume one method.

**Output: `CartDeliveryOptionsDiscountsGenerateRunResult`** — `operations` ([DeliveryOperation!]!): an ordered list of operations to generate delivery discounts.

#### Examples

##### Apply a Percentage-Off Shipping Discount (`cart.delivery-options.discounts.generate.run`)

Applies a percentage discount to the cheapest shipping method based on cart subtotal.

Input Query (Rust):

```graphql
query Input {
  cart {
    cost {
      subtotalAmount {
        amount
      }
    }
    deliveryGroups {
      deliveryOptions {
        handle
        cost {
          amount
        }
      }
    }
  }
  discount {
    metafield(namespace: "$app:delivery-discounts", key: "configuration") {
      jsonValue
    }
  }
}
```

Input Query (JavaScript): same as above but `query DeliveryInput { ... }`.

Function Code (Rust):

```rust
use super::schema;
use shopify_function::prelude::*;
use shopify_function::Result;

#[derive(Deserialize, Default)]
pub struct DiscountTier {
    threshold: f64,
    percentage: f64,
}

#[derive(Deserialize, Default)]
pub struct Configuration {
    tiers: Vec<DiscountTier>,
}

#[shopify_function]
fn cart_delivery_options_discounts_generate_run(input: schema::cart_delivery_options_discounts_generate_run::Input) -> Result<schema::CartDeliveryOptionsDiscountsGenerateRunResult> {
    // Parse configuration from metafield
    let config: &Configuration = match input.discount().metafield() {
        Some(metafield) => metafield.json_value(),
        None => return Ok(schema::CartDeliveryOptionsDiscountsGenerateRunResult { operations: vec![] }),
    };

    // Get cart subtotal
    let subtotal = input.cart().cost().subtotal_amount().amount().0;

    // Find the highest applicable tier
    let applicable_tier = config.tiers.iter()
        .filter(|tier| subtotal >= tier.threshold)
        .max_by(|a, b| a.threshold.partial_cmp(&b.threshold).unwrap_or(std::cmp::Ordering::Equal));

    // If no tier applies, return empty operations
    let Some(tier) = applicable_tier else {
        return Ok(schema::CartDeliveryOptionsDiscountsGenerateRunResult { operations: vec![] });
    };

    let mut operations = vec![];

    // Process each delivery group
    for delivery_group in input.cart().delivery_groups() {
        // Find the cheapest delivery option
        if let Some(cheapest_option) = delivery_group.delivery_options().iter()
            .min_by(|a, b| {
                let a_cost = a.cost().amount().0;
                let b_cost = b.cost().amount().0;
                a_cost.partial_cmp(&b_cost).unwrap_or(std::cmp::Ordering::Equal)
            }) {
            // Add discount operation for the cheapest option
            operations.push(schema::DeliveryOperation::DeliveryDiscountsAdd(schema::DeliveryDiscountsAddOperation {
                selection_strategy: schema::DeliveryDiscountSelectionStrategy::All,
                candidates: vec![schema::DeliveryDiscountCandidate {
                    targets: vec![schema::DeliveryDiscountCandidateTarget::DeliveryOption(
                        schema::DeliveryOptionTarget {
                            handle: cheapest_option.handle().clone(),
                        },
                    )],
                    value: schema::DeliveryDiscountCandidateValue::Percentage(schema::Percentage {
                        value: Decimal(tier.percentage),
                    }),
                    message: Some(format!("{}% off shipping", tier.percentage)),
                    associated_discount_code: None,
                }],
            }));
        }
    }

    Ok(schema::CartDeliveryOptionsDiscountsGenerateRunResult { operations })
}
```

Performance Cost (Rust): 62222 instructions.

Function Code (JavaScript):

```javascript
// @ts-check
import { DeliveryDiscountSelectionStrategy } from '../generated/api';

/**
 * @typedef {Object} DiscountTier
 * @property {number} threshold
 * @property {number} percentage
 */

/**
 * @typedef {Object} Configuration
 * @property {DiscountTier[]} tiers
 */

/**
 * @typedef {import('../generated/api').DeliveryInput} DeliveryInput
 * @typedef {import('../generated/api').DeliveryOperation} DeliveryOperation
 * @typedef {import('../generated/api').DeliveryDiscountCandidate} DeliveryDiscountCandidate
 */

/**
 * cartDeliveryOptionsDiscountsGenerateRun
 * @param {DeliveryInput} input - The DeliveryInput
 * @returns {{operations: DeliveryOperation[]}} - The function result with discounts.
 */
export function cartDeliveryOptionsDiscountsGenerateRun(input) {
  // Parse configuration from metafield
  let config;
  try {
    config = input.discount?.metafield 
      ? JSON.parse(JSON.stringify(input.discount.metafield.jsonValue))
      : { tiers: [] };
  } catch (e) {
    return { operations: [] };
  }

  // If no config or invalid tiers, return empty operations
  if (!config || !Array.isArray(config.tiers)) {
    return { operations: [] };
  }

  // Get cart subtotal
  const subtotal = input.cart?.cost?.subtotalAmount?.amount || 0;

  // Find the highest applicable tier
  const applicableTier = config.tiers
    .filter(tier => subtotal >= tier.threshold)
    .reduce((highest, current) => 
      !highest || current.threshold > highest.threshold ? current : highest, 
      null);

  // If no tier applies, return empty operations
  if (!applicableTier) {
    console.log('no tier applies');
    return { operations: [] };
  }

  const operations = [];

  // Process each delivery group
  for (const deliveryGroup of input.cart.deliveryGroups) {
    if (!deliveryGroup.deliveryOptions?.length) {
      continue;
    }

    // Find the cheapest delivery option
    let cheapestOption = deliveryGroup.deliveryOptions[0];
    for (let i = 1; i < deliveryGroup.deliveryOptions.length; i++) {
      const option = deliveryGroup.deliveryOptions[i];
      if (option.cost.amount < cheapestOption.cost.amount) {
        cheapestOption = option;
      }
    }

    /** @type {DeliveryOperation} */
    const operation = {
      deliveryDiscountsAdd: {
        candidates: [{
          message: `${applicableTier.percentage}% off shipping`,
          targets: [{
            deliveryOption: {
              handle: cheapestOption.handle,
            },
          }],
          value: {
            percentage: {
              value: String(applicableTier.percentage.toFixed(1)),
            },
          },
        }],
        selectionStrategy: DeliveryDiscountSelectionStrategy.All,
      },
    };
    operations.push(operation);
  }

  return { operations };
}
```

Performance Cost (JavaScript): 486851 instructions.

Output JSON (Rust):

```json
{
  "operations": [
    {
      "deliveryDiscountsAdd": {
        "candidates": [
          {
            "associatedDiscountCode": null,
            "message": "15% off shipping",
            "targets": [
              {
                "deliveryOption": {
                  "handle": "standard"
                }
              }
            ],
            "value": {
              "percentage": {
                "value": "15.0"
              }
            }
          }
        ],
        "selectionStrategy": "ALL"
      }
    }
  ]
}
```

##### Apply Order + Product Discount (`cart.lines.discounts.generate.run`)

Function Code (Rust):

```rust
use super::schema;
use shopify_function::prelude::*;
use shopify_function::Result;

#[shopify_function]
fn cart_lines_discounts_generate_run(input: schema::cart_lines_discounts_generate_run::Input) -> Result<schema::CartLinesDiscountsGenerateRunResult> {
    let max_cart_line = input
        .cart()
        .lines()
        .iter()
        .max_by(|a, b| {
            a.cost()
                .subtotal_amount()
                .amount()
                .partial_cmp(b.cost().subtotal_amount().amount())
                .unwrap_or(std::cmp::Ordering::Equal)
        })
        .ok_or("No cart lines found")?;

    Ok(schema::CartLinesDiscountsGenerateRunResult {
        operations: vec![
            schema::CartOperation::OrderDiscountsAdd(schema::OrderDiscountsAddOperation {
                selection_strategy: schema::OrderDiscountSelectionStrategy::First,
                candidates: vec![schema::OrderDiscountCandidate {
                    targets: vec![schema::OrderDiscountCandidateTarget::OrderSubtotal(
                        schema::OrderSubtotalTarget {
                            excluded_cart_line_ids: vec![],
                        },
                    )],
                    message: Some("10% OFF ORDER".to_string()),
                    value: schema::OrderDiscountCandidateValue::Percentage(schema::Percentage {
                        value: Decimal(10.0),
                    }),
                    conditions: None,
                    associated_discount_code: None,
                }],
            }),
            schema::CartOperation::ProductDiscountsAdd(schema::ProductDiscountsAddOperation {
                selection_strategy: schema::ProductDiscountSelectionStrategy::First,
                candidates: vec![schema::ProductDiscountCandidate {
                    targets: vec![schema::ProductDiscountCandidateTarget::CartLine(schema::CartLineTarget {
                        id: max_cart_line.id().clone(),
                        quantity: None,
                    })],
                    message: Some("20% OFF PRODUCT".to_string()),
                    value: schema::ProductDiscountCandidateValue::Percentage(schema::Percentage {
                        value: Decimal(20.0),
                    }),
                    associated_discount_code: None,
                }],
            }),
        ],
    })
}
```

Performance Cost (Rust): 49374 instructions.

Function Code (JavaScript):

```javascript
// @ts-check

import {
  OrderDiscountSelectionStrategy,
  ProductDiscountSelectionStrategy,
} from '../generated/api';

/**
 * @typedef {import("../generated/api").Input} CartInput
 * @typedef {import("../generated/api").CartLinesDiscountsGenerateRunResult} CartLinesDiscountsGenerateRunResult
 */

/**
 * cartLinesDiscountsGenerateRun
 * @param {CartInput} input - The CartInput
 * @returns {CartLinesDiscountsGenerateRunResult} - The function result with discounts.
 */
export function cartLinesDiscountsGenerateRun(input) {
    if (!input.cart.lines.length) {
        throw new Error('No cart lines found');
    }
    const maxCartLine = input.cart.lines.reduce((maxLine, line) => {
        if (line.cost.subtotalAmount.amount > maxLine.cost.subtotalAmount.amount) {
            return line;
        }
        return maxLine;
    }, input.cart.lines[0]);
    return {
        operations: [
            {
                orderDiscountsAdd: {
                    candidates: [
                        {
                            message: '10% OFF ORDER',
                            targets: [
                                {
                                    orderSubtotal: {
                                        excludedCartLineIds: [],
                                    },
                                },
                            ],
                            value: {
                                percentage: {
                                    value: "10.0",
                                },
                            },
                        },
                    ],
                    selectionStrategy: OrderDiscountSelectionStrategy.First,
                },
            },
            {
                productDiscountsAdd: {
                    candidates: [
                        {
                            message: '20% OFF PRODUCT',
                            targets: [
                                {
                                    cartLine: {
                                        id: maxCartLine.id,
                                    },
                                },
                            ],
                            value: {
                                percentage: {
                                    value: "20.0",
                                },
                            },
                        },
                    ],
                    selectionStrategy: ProductDiscountSelectionStrategy.First,
                },
            },
        ],
    };
}
```

Performance Cost (JavaScript): 420610 instructions.

Output JSON (Rust):

```json
{
  "operations": [
    {
      "orderDiscountsAdd": {
        "candidates": [
          {
            "associatedDiscountCode": null,
            "conditions": null,
            "message": "10% OFF ORDER",
            "targets": [
              { "orderSubtotal": { "excludedCartLineIds": [] } }
            ],
            "value": { "percentage": { "value": "10.0" } }
          }
        ],
        "selectionStrategy": "FIRST"
      }
    },
    {
      "productDiscountsAdd": {
        "candidates": [
          {
            "associatedDiscountCode": null,
            "message": "20% OFF PRODUCT",
            "targets": [
              { "cartLine": { "id": "gid://shopify/CartLine/0", "quantity": null } }
            ],
            "value": { "percentage": { "value": "20.0" } }
          }
        ],
        "selectionStrategy": "FIRST"
      }
    }
  ]
}
```

##### Create a Tiered Discount Based on Line Subtotals

A Discount Function that implements tiered fixed-amount discounts for cart lines based on their individual subtotals: $10 off for lines totaling $100+, $20 off for lines totaling $200+, and $30 off for lines totaling $300+ (applied as a fixed amount per line). Input query and input object follow the `cart.lines.discounts.generate.run` shape with line subtotals (e.g. lines totaling 50, 150, 250, 350).

#### Legacy Discount APIs

The Discount Function API supersedes the legacy **Order Discount** (`https://shopify.dev/docs/api/functions/reference/order-discounts`) and **Product Discount** (`https://shopify.dev/docs/api/functions/reference/product-discounts`) APIs. In those legacy APIs, `cart.deliveryGroups` is always an empty array, so you can't apply discounts to shipping costs — use the unified Discount Function API instead.


---

## Cart Transform (bundles, line item changes)

### Cart Transform Function API

> Fonte: https://shopify.dev/docs/api/functions/latest/cart-transform

A cart represents the merchandise that a customer intends to purchase, and the estimated cost. Transforming a cart refers to changing the pricing and presentation of items in a cart. To modify the appearance of cart items — updating titles and images, changing prices, and bundling items — you can only use the Cart Transform API.

Use the API to add product bundles to a store or break down bundled products into individual components, with associated data such as buyer identity, quantity, cost, and subscription information.

**Note:** You can install a maximum of one cart transform function per app on each store. If a store has cart transform functions from more than one app, all of them run.

#### Use cases

* Expand a cart line item to display the bundled items it contains.
* Merge multiple cart lines into a single line that represents a bundle.
* Update the presentation of line items in a cart to override their price, title, or image.

**Note:** Only development stores or stores on a Shopify Plus plan can use apps with `lineUpdate` (and `update`) operations.

#### Function target — Cart — Compatibility with Shopify surfaces

| Surface | Status |
|---------|--------|
| B2B | Supported |
| Cart | Supported |
| Checkout | Partially supported |
| Create Order API | Not supported |
| Draft Order (Admin) | Supported |
| Draft Order (Checkout) | Supported |
| Order Edit (Admin) | Not supported |
| Order Edit (Checkout) | Not supported |
| POS | Partially supported |
| Pre-order and Try Before You Buy | Not supported |
| Shopify Admin | Supported |
| Storefront | Supported |
| Storefront Accelerated Checkout | Supported |
| Subscription (Recurring Orders) | Not supported |

* **Checkout note:** Shopify rejects `lineExpand`, `linesMerge`, and `lineUpdate` operations if a selling plan is present.
* **POS note:** `ProductVariant.requiresComponents` boolean has to be `true` for complete cartTransform support on POS.

#### Getting started

```terminal
shopify app generate extension --template cart_transform
```

Tutorial: [Build a cart transform function](https://shopify.dev/docs/apps/build/product-merchandising/bundles/add-customized-bundle-function)

#### Run target — `cart.transform.run`

The run target modifies the pricing and presentation of items in a cart using Shopify data or hardcoded values. The target returns a list of operations to be applied to cart line items. For example, automatically add a warranty when a specific product is added to a cart.

##### Input

The `Input` object provides the complete GraphQL schema. Top-level fields:

* **`cart`** (Cart!) — `attribute(key)`, `billingAddress` (MailingAddress), `buyerIdentity` (BuyerIdentity with `customer`, `email`, `isAuthenticated`, `phone`, `purchasingCompany`), `lines` ([CartLine!]! — each with `attribute`, `cost` CartLineCost! {`amountPerQuantity`, `compareAtAmountPerQuantity`, `subtotalAmount`, `totalAmount`}, `discountAllocations`, `id`, `merchandise` (CustomProduct | ProductVariant), `parentRelationship` (CartLineParentRelationship {`parent`}), `quantity`, `sellingPlanAllocation`), `metafield`, `retailLocation` (Location).
* **`cartTransform`** (CartTransform!) — A customization that changes the pricing and presentation of items in a cart. `metafield` (Metafield).
* **`localization`** (Localization!) — `country` {`isoCode`}, `language` {`isoCode`}, `market` (deprecated).
* **`presentmentCurrencyRate`** (Decimal!) — Exchange rate for currency conversion.
* **`shop`** (Shop!) — `localTime`, `metafield`, `metaobject` (app-owned metaobjects with `$app` prefix).

(The nested `Cart`/`BuyerIdentity`/`ProductVariant`/`Metafield` fields are identical to those documented in the Discount API above.)

##### Run Function — Output: `CartTransformRunResult`

* `operations` ([Operation!]!) — The ordered list of operations to apply to the cart. Each operation is one of:

**LineExpandOperation** — Expands a single cart line item to form a bundle of components.

* `cartLineId` (ID!), `expandedCartItems` ([ExpandedItem!]!), `image` (ImageInput {`url`}), `price` (PriceAdjustment), `title` (String).
* `ExpandedItem`: `attributes` ([AttributeOutput!] {`key`, `value`}), `merchandiseId` (ID!), `price` (ExpandedItemPriceAdjustment), `quantity` (Int!, max 2000).
* `ExpandedItemPriceAdjustment`: `adjustment` (ExpandedItemPriceAdjustmentValue! — FixedPricePerUnitAdjustment {`amount`} or PercentageAdjustment {`percentage`}).

**LinesMergeOperation** — Merges multiple cart line items into a single line, representing a bundle of components.

* `attributes` ([AttributeOutput!]), `cartLines` ([CartLineInput!]! — `cartLineId`, `quantity` max 2000), `image` (ImageInput), `parentVariantId` (ID!), `price` (PriceAdjustment), `title` (String).

**LineUpdateOperation** — Overrides the price, title, and image of a cart line item. Only stores on a Shopify Plus plan can use apps with `update` operations.

* `cartLineId` (ID!), `image` (ImageInput — visible in checkout only, not persisted to orders), `price` (LineUpdateOperationPriceAdjustment — FixedPriceAdjustment {`amount`} or PercentageAdjustment {`percentage`}), `title` (String).

#### Examples

##### Example 1: Add gift wrapping to cart items

When a customer adds an item with the "Gift Wrap" attribute, the function checks for the attribute and expands the cart line to add a $5 gift wrap add-on as a separate line item with a fixed price.

Input Query (Rust):

```graphql
query Input {
  presentmentCurrencyRate
  cart {
    lines {
      id
      quantity
      cost {
        amountPerQuantity {
          amount
          currencyCode
        }
      }
      # Access the cart line attribute to decide if we should add a warranty
      giftWrapAdded: attribute(key: "Gift Wrap Added") {
        value
      }
      merchandise {
        __typename
        ... on ProductVariant {
          id
          title
          product {
            # Access the metafield value to determine the cost of the gift wrap
            giftWrapCost: metafield(namespace: "$app:gift-wrap", key: "cost") {
              type
              jsonValue
            }
          }
        }
      }
    }
  }
  cartTransform {
    # Access the variant ID that represents the warranty product
    giftWrapVariantID: metafield(namespace: "$app:optional-add-ons", key: "function-configuration") {
      value
    }
  }
}
```

Function Code (Rust):

```rust
use crate::schema;
use shopify_function::prelude::*;
use shopify_function::Result;


#[derive(Debug, Deserialize)]
#[shopify_function(rename_all = "camelCase")]

pub struct Money {
  pub amount: String,
  pub currency_code: String,
}

#[shopify_function]
fn cart_transform_run(input: schema::cart_transform_run::Input) -> Result<schema::CartTransformRunResult> {
    let presentment_currency_rate_f64 = input.presentment_currency_rate().0;
    let cart_operations: Vec<schema::Operation> = get_update_cart_operations(
        &input.cart(),
        &input.cart_transform(),
        presentment_currency_rate_f64,
    );

    Ok(schema::CartTransformRunResult {
        operations: cart_operations,
    })
}

fn get_update_cart_operations(
    cart: &schema::cart_transform_run::input::Cart,
    cart_transform: &schema::cart_transform_run::input::CartTransform,
    presentment_currency_rate: f64,
) -> Vec<schema::Operation> {
    cart.lines()
        .iter()
        .filter_map(|line| {
            let gift_wrap_added = get_gift_wrap_added(line);
            let gift_wrap_cost = get_gift_wrap_cost(line);
            let gift_wrap_variant_id = &cart_transform.gift_wrap_variant_id();
            if let (schema::cart_transform_run::input::cart::lines::Merchandise::ProductVariant(variant), Some(_gift_wrap_variant_id)) =
                (&line.merchandise(), gift_wrap_variant_id)
            {
                if gift_wrap_added && gift_wrap_cost > 0.0 {
                    let original_item = schema::ExpandedItem {
                        merchandise_id: variant.id().clone(),
                        quantity: 1,
                        price: Some(schema::ExpandedItemPriceAdjustment {
                            adjustment: schema::ExpandedItemPriceAdjustmentValue::FixedPricePerUnit(
                                schema::ExpandedItemFixedPricePerUnitAdjustment {
                                    amount: Decimal(line.cost().amount_per_quantity().amount().0),
                                },
                            ),
                        }),
                        attributes: None,
                    };
                    let expanded_cart_item = schema::ExpandedItem {
                        merchandise_id: _gift_wrap_variant_id.value().clone(),
                        quantity: 1,
                        price: Some(schema::ExpandedItemPriceAdjustment {
                            adjustment: schema::ExpandedItemPriceAdjustmentValue::FixedPricePerUnit(
                                schema::ExpandedItemFixedPricePerUnitAdjustment {
                                    amount: Decimal(
                                            gift_wrap_cost
                                            * presentment_currency_rate,
                                    ),
                                },
                            ),
                        }),
                        attributes: None,
                    };
                    let expand_operation = schema::LineExpandOperation {
                        cart_line_id: line.id().clone(),
                        title: variant.title().to_owned().cloned(),
                        image: None,
                        price: None,
                        expanded_cart_items: vec![original_item, expanded_cart_item],
                    };
                    Some(schema::Operation::LineExpand(expand_operation))
                } else {
                    None
                }
            } else {
                None
            }
        })
        .collect()
}

fn get_gift_wrap_added(line: &schema::cart_transform_run::input::cart::Lines) -> bool {
    match &line.gift_wrap_added() {
        Some(input_cart_lines_gift_wrap_added) => match &input_cart_lines_gift_wrap_added.value() {
            Some(text) => text.as_str() == "Yes",
            None => false,
        },
        None => false,
    }
}

fn get_gift_wrap_cost(line: &schema::cart_transform_run::input::cart::Lines) -> f64 {
    match &line.merchandise() {
        schema::cart_transform_run::input::cart::lines::Merchandise::ProductVariant(variant) => {
            if let Some(gift_wrap_cost) = variant.product().gift_wrap_cost() {
                let money = gift_wrap_cost.json_value();
                money.amount.parse::<f64>().unwrap_or(5.00)
            } else {
                5.00
            }
        },
        _ => 5.00,
    }
}
```

Performance Cost (Rust): 91707 instructions.

Function Code (JavaScript):

```javascript
// @ts-check

/*
A straightforward example of a function that expands a single line into a bundle with add-on products.
The add-on options are are stored in a line item property and metafield on the product.
*/

/**
 * @typedef {import("../generated/api").RunInput} RunInput
 * @typedef {import("../generated/api").CartTransformRunResult} CartTransformRunResult
 * @typedef {import("../generated/api").Operation} Operation
 */

/**
 * @type {CartTransformRunResult}
 */
const NO_CHANGES = {
  operations: [],
};

/**
 * @param {RunInput} input
 * @returns {CartTransformRunResult}
 */
export function cartTransformRun(input) {
  const operations = input.cart.lines.reduce(
    /** @param {Operation[]} acc */
    (acc, cartLine) => {
      const expandOperation = optionallyBuildExpandOperation(cartLine, input);

      if (expandOperation) {
        return [...acc, { lineExpand: expandOperation }];
      }

      return acc;
    },
    []
  );

  return operations.length > 0 ? { operations } : NO_CHANGES;
}

/**
 * @param {RunInput['cart']['lines'][number]} cartLine
 * @param {RunInput} input
 */
function optionallyBuildExpandOperation(
  { id: cartLineId, merchandise, giftWrapAdded, cost},
  { cartTransform: { giftWrapVariantID }, presentmentCurrencyRate }
) {
  const hasGiftWrapMetafields =
    merchandise.__typename === "ProductVariant" &&
    !!merchandise.product.giftWrapCost &&
    !!giftWrapVariantID;
  const shouldAddGiftWrap = giftWrapAdded?.value === "Yes";
  const giftWrapCost = merchandise.__typename === "ProductVariant" &&
    merchandise.product?.giftWrapCost?.value
      ? JSON.parse(merchandise.product.giftWrapCost.value).amount
      : "5.0";

  if (
    merchandise.__typename === "ProductVariant" &&
    hasGiftWrapMetafields &&
    shouldAddGiftWrap
  ) {
    return {
      cartLineId,
      title: `${merchandise.title}`,
      expandedCartItems: [
        {
          merchandiseId: merchandise.id,
          quantity: 1,
          price: {
            adjustment: {
              fixedPricePerUnit: {
                amount: cost.amountPerQuantity.amount,
              },
            },
          },
        },
        {
          merchandiseId: giftWrapVariantID.value,
          quantity: 1,
          price: {
            adjustment: {
              fixedPricePerUnit: {
                amount: (
                  parseFloat(giftWrapCost) *
                  presentmentCurrencyRate
                ).toFixed(1),
              },
            },
          },
        },
      ],
    };
  }

  return null;
}
```

Performance Cost (JavaScript): 492416 instructions.

Output JSON (Rust):

```json
{
  "operations": [
    {
      "lineExpand": {
        "cartLineId": "gid://shopify/CartLine/2",
        "expandedCartItems": [
          {
            "attributes": null,
            "merchandiseId": "gid://shopify/ProductVariant/456",
            "price": { "adjustment": { "fixedPricePerUnit": { "amount": "100.0" } } },
            "quantity": 1
          },
          {
            "attributes": null,
            "merchandiseId": "gid://shopify/ProductVariant/2",
            "price": { "adjustment": { "fixedPricePerUnit": { "amount": "5.0" } } },
            "quantity": 1
          }
        ],
        "image": null,
        "price": null,
        "title": "Something that is wrapped"
      }
    }
  ]
}
```

##### Example 2: Create a cart bundle with an add-on

Same pattern as Example 1 but using an "Assembly Service Added" attribute and an `$app:assembly-service`/`cost` metafield, expanding the line to include the assembly service add-on at a fixed price (e.g. $25). Performance: Rust 92394, JavaScript 495305 instructions.

##### Example 3: Expand a product bundle into component items

When a customer adds a bundle product (e.g. a "Holiday Package"), it's automatically expanded into its individual components, each with its own price. Uses `LineExpandOperation` with multiple `expandedCartItems` (e.g. three variants at $25 each).

---

## Cart and Checkout Validation

### Cart and Checkout Validation Function API

> Fonte: https://shopify.dev/docs/api/functions/latest/cart-and-checkout-validation

Cart and checkout validation implements checks and rules to ensure that orders meet specific criteria before allowing customers to proceed with their purchase — including express checkouts such as Shop Pay, PayPal, Google Pay, and Apple Pay. To validate a cart and checkout server-side, you can only use this API.

Use the API to generate the validations and specify the message to display in checkout when the function returns a validation error. You can target specific checkout fields with the validation error message, and use the cart as a global object to target with a validation error message.

**Note:** You can activate a maximum of 25 validation functions on each store. Errors from validation functions are exposed to the Storefront API's `Cart` object, in themes that use the `cart` template, and during checkout.

#### Use Cases

* Use tokengating or require a customer membership at checkout.
* Verify the age or ID of a customer when they proceed through checkout.
* Provide B2B product minimums, maximums, and multiples.
* Provide B2B location order minimums, maximums, or credit limits.
* Specify quantity limits in a flash sale.
* Validate purchase order numbers for B2B customers.
* Apply billing address restrictions.

#### Function Target — Checkout — Compatibility with Shopify Surfaces

| Surface | Support |
|---------|---------|
| B2B | Supported |
| Cart | Supported |
| Checkout | Supported |
| Create Order API | Not supported |
| Draft Order (Admin) | Supported |
| Draft Order (Checkout) | Supported |
| Order Edit (Admin) | Not supported |
| Order Edit (Checkout) | Not supported |
| POS | Not supported |
| Pre-order and Try Before You Buy | Not supported |
| Shopify Admin | Supported |
| Storefront | Supported |
| Storefront Accelerated Checkout | Supported |
| Subscription (Recurring Orders) | Not supported |

**Fetch Target — Limited access:** limited to custom apps installed on Enterprise stores. You'll also need to request network access for Functions.

#### Getting Started

```terminal
shopify app generate extension --template cart_checkout_validation
```

Tutorial: [Build a Validation Function](https://shopify.dev/docs/apps/build/checkout/cart-checkout-validation/create-server-side-validation-function)

#### Run Target — `cart.validations.generate.run`

The run target generates cart and checkout validations using Shopify data, hardcoded values, or fetch results. The target returns a list of operations to be applied to validations applied to the cart and checkout.

##### Input (top-level fields)

* **buyerJourney** (BuyerJourneyStep!) — Current step in the buyer's purchasing process (CART_INTERACTION, CHECKOUT_COMPLETION, CHECKOUT_INTERACTION).
* **cart** (Cart!) — The cart where the Function is running, containing merchandise and customer information.
* **fetchResult** (HttpResponse) — The response from a fetch target HTTP request.
* **localization** (Localization!) — Regional and language settings.
* **presentmentCurrencyRate** (Decimal!) — Exchange rate for converting discounts.
* **shop** (Shop!) — Shop information including timezone and metafields.
* **validation** (Validation!) — Configuration controlling how merchants define validation rules.

##### Run Function — Output: `CartValidationsGenerateRunResult`

* **operations** ([Operation!]!) — An ordered list of operations for the validations associated with the cart and checkout processes.
* **ValidationAddOperation** — Adds validations to the cart and checkout. `errors` ([ValidationError!]!) — the validation errors that block a customer from proceeding through checkout.
* **ValidationError** — `message` (String!): a description of the validation error; `target` (String!): the identifier specifying where to display the error in checkout.

#### Examples

##### Prevent Shipping to PO Boxes

Input Query (Rust):

```graphql
query Input {
  cart {
    deliveryGroups {
      deliveryAddress {
        address1
        address2
      }
    }
  }
}
```

Function Code (Rust):

```rust
use crate::schema;
use shopify_function::prelude::*;
use shopify_function::Result;

#[shopify_function]
fn cart_validations_generate_run(input: schema::run::Input) -> Result<schema::CartValidationsGenerateRunResult> {
    let mut operations = Vec::new();
    let mut errors = Vec::new();

    for group in input.cart().delivery_groups() {
        let Some(address) = &group.delivery_address() else { continue };

        let address1 = address.address_1().map_or("", |v| v);
        let address2 = address.address_2().map_or("", |v| v);

        if is_po_box(address1) || is_po_box(address2) {
            errors.push(schema::ValidationError {
                message: "PO Box addresses are not allowed for shipping.".to_string(),
                target: "$.cart.deliveryGroups[0].deliveryAddress.address1".to_string(),
            });
        }
    }

    let operation = schema::ValidationAddOperation { errors };
    operations.push(schema::Operation::ValidationAdd(operation));

    Ok(schema::CartValidationsGenerateRunResult { operations })
}

fn is_po_box(address: &str) -> bool {
    let normalized = address.to_ascii_lowercase().replace(".", "").replace(" ", "");
    normalized.contains("pobox") || normalized.contains("afpo") || normalized.contains("postoffice") || normalized.contains("postbox")
}
```

Function Code (JavaScript):

```javascript
// @ts-check

/**
 * @typedef {import("../generated/api").CartValidationsGenerateRunInput} CartValidationsGenerateRunInput
 * @typedef {import("../generated/api").CartValidationsGenerateRunResult} CartValidationsGenerateRunResult
 */

/**
 * @param {string} address
 * @returns {boolean}
 */
function isPoBox(address) {
  const normalized = address.toLowerCase().replace(/\./g, '').replace(/\s/g, '');
  return normalized.includes('pobox') ||
         normalized.includes('afpo') ||
         normalized.includes('postoffice') ||
         normalized.includes('postbox');
}

/**
 * @param {CartValidationsGenerateRunInput & { cart: Cart }} input
 * @returns {CartValidationsGenerateRunResult}
 */
export function cartValidationsGenerateRun(input) {
  const errors = [];

  for (const group of input.cart.deliveryGroups) {
    if (!group.deliveryAddress) continue;

    const address1 = group.deliveryAddress.address1 || '';
    const address2 = group.deliveryAddress.address2 || '';

    if (isPoBox(address1) || isPoBox(address2)) {
      errors.push({
        message: "PO Box addresses are not allowed for shipping.",
        target: "$.cart.deliveryGroups[0].deliveryAddress.address1"
      });
    }
  }

  const operations = [
    {
      validationAdd: {
        errors
      },
    },
  ];

  return { operations };
}
```

Performance: Rust 28850, JavaScript 222785 instructions.

Output JSON:

```json
{
  "operations": [
    {
      "validationAdd": {
        "errors": [
          {
            "message": "PO Box addresses are not allowed for shipping.",
            "target": "$.cart.deliveryGroups[0].deliveryAddress.address1"
          }
        ]
      }
    }
  ]
}
```

##### Validate Required Localized Fields at Checkout

Adds a configurable validation to one or more localized fields (e.g. tax credentials) during checkout completion.

Input Query (Rust):

```graphql
query Input($localizedFields: [LocalizedFieldKey!]! = []) {
  cart {
    localizedFields(keys: $localizedFields) {
      key
      title
      value
    }
  }
  buyerJourney {
    step
  }
}
```

Function Code (Rust):

```rust
use crate::schema;
use shopify_function::prelude::*;
use shopify_function::Result;

#[shopify_function]
fn cart_validations_generate_run(input: schema::run::Input) -> Result<schema::CartValidationsGenerateRunResult> {
    let mut operations = Vec::new();
    let mut errors = Vec::new();

    // Validate only during checkout completion
    if input.buyer_journey().step() == Some(&schema::BuyerJourneyStep::CheckoutCompletion) {
        for field in input.cart().localized_fields() {
            if field.value().is_none() || field.value().as_ref().unwrap().trim().is_empty() {
                // Use the title for user-facing message, key for the target path
                let field_key = format!("{}", field.key());
                errors.push(schema::ValidationError {
                    message: format!("The field '{}' is required to complete checkout.", field.title()),
                    target: format!("$.cart.localizedFields.{}", field_key),
                });
            }
        }
    }

    let operation = schema::ValidationAddOperation { errors };
    operations.push(schema::Operation::ValidationAdd(operation));

    Ok(schema::CartValidationsGenerateRunResult { operations })
}
```

Function Code (JavaScript):

```javascript
// @ts-check

/**
 * @typedef {import("../generated/api").CartValidationsGenerateRunInput} CartValidationsGenerateRunInput
 * @typedef {import("../generated/api").CartValidationsGenerateRunResult} CartValidationsGenerateRunResult
 */

/**
 * @param {CartValidationsGenerateRunInput} input
 * @returns {CartValidationsGenerateRunResult}
 */
export function cartValidationsGenerateRun(input) {
  const errors = [];

  // Validate only during checkout completion
  if (input.buyerJourney?.step === 'CHECKOUT_COMPLETION') {
    for (const field of input.cart.localizedFields) {
      if (!field.value || field.value.trim() === '') {
        errors.push({
          message: `The field '${field.title}' is required to complete checkout.`,
          target: `$.cart.localizedFields.${field.key}`
        });
      }
    }
  }

  const operations = [
    {
      validationAdd: {
        errors
      },
    },
  ];

  return { operations };
}
```

Performance: Rust 41956, JavaScript 203540 instructions.

##### Validate a Gift Note Attribute on the Cart

Validates a required line item attribute is set during checkout completion or interaction. Reads `attribute(key: "gift_note")` and `attribute(key: "gift_note_validated")`; targets `$.cart`. Performance: Rust 20992, JavaScript 144300.

```rust
use crate::schema;
use shopify_function::prelude::*;
use shopify_function::Result;

#[shopify_function]
fn cart_validations_generate_run(input: schema::run::Input) -> Result<schema::CartValidationsGenerateRunResult> {
    let mut operations = Vec::new();
    let mut errors = Vec::new();

    // Only validate during checkout steps
    if input.buyer_journey().step() == Some(&schema::BuyerJourneyStep::CheckoutInteraction)
        || input.buyer_journey().step() == Some(&schema::BuyerJourneyStep::CheckoutCompletion)
    {
        // Check if gift note is present or already validated
        let is_validated = input
            .cart()
            .a_2()
            .and_then(|attr| attr.value())
            .map(|value| value == "true")
            .unwrap_or(false);

        if input.cart().a_1().is_none() && !is_validated {
            errors.push(schema::ValidationError {
                message: "Gift note is required for this cart".to_string(),
                target: "$.cart".to_string(),
            });
        }
    }

    let operation = schema::ValidationAddOperation { errors };
    operations.push(schema::Operation::ValidationAdd(operation));

    Ok(schema::CartValidationsGenerateRunResult { operations })
}
```

##### Limit Product Quantity Based on Product Metafields

Checks a `custom`/`limits` metafield (if it exists) and limits the quantity of a product to that limit; targets `$.cart`. Performance: Rust 30862, JavaScript 186324.

```rust
use crate::schema;
use shopify_function::prelude::*;
use shopify_function::Result;

#[shopify_function]
fn cart_validations_generate_run(input: schema::run::Input) -> Result<schema::CartValidationsGenerateRunResult> {
    let mut operations = Vec::new();
    let mut errors = Vec::new();

    for line in input.cart().lines().iter() {
        let product = match &line.merchandise() {
            schema::run::input::cart::lines::Merchandise::ProductVariant(variant) => &variant.product(),
            _ => continue,
        };

        if let Some(metafield) = &product.metafield() {
            if let Ok(limit) = metafield.value().parse::<i32>() {
                if *line.quantity() > limit {
                    errors.push(schema::ValidationError {
                        message: format!(
                            "You can only purchase up to {} units of this product.",
                            limit
                        ),
                        target: "$.cart".to_string(),
                    });
                }
            }
        }
    }

    let operation = schema::ValidationAddOperation { errors };
    operations.push(schema::Operation::ValidationAdd(operation));

    Ok(schema::CartValidationsGenerateRunResult { operations })
}
```

#### Supported Checkout Field Targets

| Field | Target Value |
|-------|--------------|
| cart | `$.cart` |
| email | `$.cart.buyerIdentity.email` |
| phone | `$.cart.buyerIdentity.phone` |
| deliveryAddress.address1 | `$.cart.deliveryGroups[0].deliveryAddress.address1` |
| deliveryAddress.address2 | `$.cart.deliveryGroups[0].deliveryAddress.address2` |
| deliveryAddress.city | `$.cart.deliveryGroups[0].deliveryAddress.city` |
| deliveryAddress.company | `$.cart.deliveryGroups[0].deliveryAddress.company` |
| deliveryAddress.countryCode | `$.cart.deliveryGroups[0].deliveryAddress.countryCode` |
| deliveryAddress.firstName | `$.cart.deliveryGroups[0].deliveryAddress.firstName` |
| deliveryAddress.lastName | `$.cart.deliveryGroups[0].deliveryAddress.lastName` |
| deliveryAddress.phone | `$.cart.deliveryGroups[0].deliveryAddress.phone` |
| deliveryAddress.provinceCode | `$.cart.deliveryGroups[0].deliveryAddress.provinceCode` |
| deliveryAddress.zip | `$.cart.deliveryGroups[0].deliveryAddress.zip` |
| billingAddress.address1 | `$.cart.billingAddress.address1` |
| billingAddress.address2 | `$.cart.billingAddress.address2` |
| billingAddress.city | `$.cart.billingAddress.city` |
| billingAddress.company | `$.cart.billingAddress.company` |
| billingAddress.countryCode | `$.cart.billingAddress.countryCode` |
| billingAddress.firstName | `$.cart.billingAddress.firstName` |
| billingAddress.lastName | `$.cart.billingAddress.lastName` |
| billingAddress.phone | `$.cart.billingAddress.phone` |
| billingAddress.provinceCode | `$.cart.billingAddress.provinceCode` |
| billingAddress.zip | `$.cart.billingAddress.zip` |
| poNumber | `$.cart.poNumber` |
| localizedFields | `$.cart.localizedfield.key` |

**Note:** Checkouts and orders can include multiple delivery methods. Iterate over all delivery groups or fulfillment orders to determine the delivery method for each; don't assume one method for the order.

---

## Delivery Customization

### Delivery Customization Function API

> Fonte: https://shopify.dev/docs/api/functions/latest/delivery-customization

A delivery customization enables you to rename, sort, and hide the delivery options available to customers during checkout. Examples include shipping carriers, local delivery, or pickup options. The Delivery Customization Function API is the only tool for this customization task.

Shopify Functions enable you to customize Shopify's backend logic. The Delivery Customization API integrates this logic into the checkout flow, displaying unique delivery options with associated data such as buyer identity, delivery groups, delivery addresses, and cost.

**Note:** You can activate a maximum of 25 delivery customization functions on each store.

#### Use Cases

- Hide delivery options for certain products or customers
- Reorder delivery options according to user preference
- Hide delivery options for PO Box addresses
- Add messaging to delivery option titles

#### Function Target — Checkout — Compatibility with Shopify Surfaces

| Surface | Status |
|---------|--------|
| B2B | Supported |
| Cart | Not supported |
| Checkout | Supported |
| Create Order API | Not supported |
| Draft Order (Admin) | Not supported |
| Draft Order (Checkout) | Supported |
| Order Edit (Admin) | Not supported |
| Order Edit (Checkout) | Not supported |
| POS | Partially supported (only available when shipping to a store) |
| Pre-order and Try Before You Buy | Not supported |
| Shopify Admin | Not supported |
| Storefront | Not supported |
| Storefront Accelerated Checkout | Supported |
| Subscription (Recurring Orders) | Not supported |

#### Getting Started

```terminal
shopify app generate extension --template delivery_customization
```

Tutorial: [Build a Delivery Customization Function](https://shopify.dev/docs/apps/build/checkout/delivery-shipping/delivery-options/build-function)

#### Run Target — `cart.delivery-options.transform.run`

The run target renames, sorts, and hides delivery options available to customers at checkout, using Shopify data or hardcoded values. The target returns a list of operations to be applied to delivery options. Example: hide a "Same-Day Delivery" option for B2B customers.

**Note:** Checkouts and orders can include multiple delivery methods. Iterate over all delivery groups or fulfillment orders to determine the delivery method for each.

##### Input (top-level fields)

* `cart` (Cart!) — The cart where the Function is running.
* `deliveryCustomization` (DeliveryCustomization!) — Backend logic defining how delivery options are sorted, hidden, or renamed, including associated metafields.
* `localization` (Localization!) — Regional and language settings.
* `presentmentCurrencyRate` (Decimal!) — Exchange rate.
* `shop` (Shop!) — Shop information including timezone and metafields.

##### Output — `CartDeliveryOptionsTransformRunResult`

The ordered list of `operations`:

* **DeliveryOptionHide** — `deliveryOptionHandle` (Handle!): the handle of the delivery option to hide.
* **DeliveryOptionMove** — `deliveryOptionHandle` (Handle!), `index` (Int!): the target index within the delivery group.
* **DeliveryOptionRename** — `deliveryOptionHandle` (Handle!), `title` (String!): the new name.

> Note: The carrier name is automatically prepended to the delivery option title at checkout when using `DeliveryOptionRenameOperation`. For example, "UPS Standard" could become "UPS Standard Shipping," but not "Standard Shipping."

#### Examples

##### Hide Free Delivery for Perishable Items

Hides the free delivery option if the product has a `perishable` tag and the delivery address country matches configured countries stored in a JSON metafield (`$app:delivery-customization`/`function-configuration`).

Function Code (Rust):

```rust
use crate::schema;
use shopify_function::prelude::*;
use shopify_function::Result;

#[derive(Deserialize, Default, PartialEq)]
#[shopify_function(rename_all = "camelCase")]
pub struct Configuration {
    country_code: Option<Vec<String>>,
}

#[shopify_function]
fn cart_delivery_options_transform_run(
    input: schema::cart_delivery_options_transform_run::Input,
) -> Result<schema::CartDeliveryOptionsTransformRunResult> {
    let no_changes = schema::CartDeliveryOptionsTransformRunResult { operations: vec![] };

    // Parse configuration from metafield
    let config: &Configuration = match input.delivery_customization().metafield() {
        Some(metafield) => &metafield.json_value(),
        None => return Ok(no_changes),
    };

    // Extract configured countries from configuration
    let configured_countries = match config.country_code.as_ref() {
        Some(countries) if !countries.is_empty() => countries,
        _ => return Ok(no_changes),
    };

    // Check delivery address country code
    let cart = &input.cart();

    let delivery_groups = &cart.delivery_groups();
    if delivery_groups.is_empty() {
        return Ok(no_changes);
    }

    let country_code = match &delivery_groups[0].delivery_address() {
        Some(address) => &address.country_code(),
        None => return Ok(no_changes),
    };

    // Check if the country code matches any configured country
    let found = if let Some(code) = country_code {
        configured_countries.iter().any(|c| c == *code)
    } else {
        false
    };

    if !found {
        return Ok(no_changes);
    }

    // Check if any product has the perishable tag
    let cart_lines = &cart.lines();

    let has_perishable_item = cart_lines.iter().any(|line| {
        // Check if merchandise is a ProductVariant
        match &line.merchandise() {
            schema::cart_delivery_options_transform_run::input::cart::lines::Merchandise::ProductVariant(variant) => {
                let product = &variant.product();
                product.has_tags().iter().any(|tag_response| {
                    *tag_response.has_tag() && tag_response.tag() == "perishable"
                })
            }
            _ => false,
        }
    });

    if !has_perishable_item {
        return Ok(no_changes);
    }

    // Find the free delivery option
    let delivery_options = &delivery_groups[0].delivery_options();
    let free_delivery_option = delivery_options.iter().find(|option| {
        let cost = &option.cost();
        let amount_str = cost.amount().to_string();
        if let Ok(amount) = amount_str.parse::<f64>() {
            return amount == 0.0;
        }
        false
    });

    let free_delivery_option = match free_delivery_option {
        Some(option) => option,
        None => return Ok(no_changes),
    };

    // Hide the free delivery option
    let hide_operation = schema::DeliveryOptionHideOperation {
        delivery_option_handle: free_delivery_option.handle().clone(),
    };

    // Create the operations vector
    let mut operations = Vec::new();
    operations.push(schema::Operation::DeliveryOptionHide(hide_operation));

    Ok(schema::CartDeliveryOptionsTransformRunResult { operations })
}
```

Performance Cost (Rust): 62308 instructions.

Function Code (JavaScript):

```javascript
// @ts-check

/**
 * @typedef {import("../generated/api").RunInput} RunInput
 * @typedef {import("../generated/api").CartDeliveryOptionsTransformRunResult} CartDeliveryOptionsTransformRunResult
 */

/**
 * @type {CartDeliveryOptionsTransformRunResult}
 */
const NO_CHANGES = {
  operations: [],
};

/**
 * @param {RunInput} input
 * @returns {CartDeliveryOptionsTransformRunResult}
 */
export function cartDeliveryOptionsTransformRun(input) {
  // Parse configuration from metafield
  const configuration = JSON.parse(
    input?.deliveryCustomization?.metafield?.value ?? "{}"
  );

  // Extract configured countries from configuration
  const configuredCountries = configuration.countryCode || [];
  if (!configuredCountries.length) return NO_CHANGES;

  // Check delivery address country code
  const deliveryGroups = input.cart?.deliveryGroups || [];
  if (!deliveryGroups.length) return NO_CHANGES;

  const countryCode = deliveryGroups[0]?.deliveryAddress?.countryCode;
  if (!configuredCountries.includes(countryCode)) return NO_CHANGES;

  // Check if any product has the perishable tag
  const cartLines = input.cart?.lines || [];
  const hasPerishableItem = cartLines.some(line => {
    // More flexible check that doesn't require __typename
    return (line.merchandise?.product  &&
      line.merchandise?.product)?.hasTags?.some(tagResponse =>
        tagResponse.hasTag && tagResponse.tag === "perishable"
      );
  });

  if (!hasPerishableItem) return NO_CHANGES;

  // Find the free delivery option, comparing the cost to 0.0
  const deliveryOptions = deliveryGroups[0]?.deliveryOptions || [];
  const freeDeliveryOption = deliveryOptions.find(option =>
    parseFloat(option.cost?.amount) === 0
  );

  if (!freeDeliveryOption) return NO_CHANGES;


  // Hide the free delivery option
  return {
    operations: [
      {
        deliveryOptionHide: {
          deliveryOptionHandle: freeDeliveryOption.handle
        }
      }
    ]
  };
}
```

Performance Cost (JavaScript): 322566 instructions.

Output JSON:

```json
{
  "operations": [
    {
      "deliveryOptionHide": {
        "deliveryOptionHandle": "dc4b9f18d30098469af5fabec87f3434-7bf1540a5810819fcc43fd9808d43db9"
      }
    }
  ]
}
```

##### Hide Express Delivery Options

Hides the express delivery option based on the title of the delivery option.

```rust
use crate::schema;
use shopify_function::prelude::*;
use shopify_function::Result;

#[shopify_function]
fn cart_delivery_options_transform_run(
    input: schema::cart_delivery_options_transform_run::Input,
) -> Result<schema::CartDeliveryOptionsTransformRunResult> {
    let mut operations = vec![];

    // Process each delivery group
    let cart = &input.cart();
    for group in cart.delivery_groups() {
        for option in group.delivery_options() {
            let is_express = option
                .title()
                .as_ref()
                .map_or(false, |t| t.to_lowercase().contains("express"));

            if is_express {
                operations.push(schema::Operation::DeliveryOptionHide(
                    schema::DeliveryOptionHideOperation {
                        delivery_option_handle: option.handle().clone(),
                    },
                ));
            }
        }
    }

    Ok(schema::CartDeliveryOptionsTransformRunResult { operations })
}
```

Performance: Rust 42067, JavaScript 227367 instructions.

##### Add Delivery Timeframes to Express Shipping (rename)

Renames the express delivery option to append the shipping timeline (e.g. "Express (1-2 days)").

```rust
use crate::schema;
use shopify_function::prelude::*;
use shopify_function::Result;

#[shopify_function]
fn cart_delivery_options_transform_run(
    input: schema::cart_delivery_options_transform_run::Input,
) -> Result<schema::CartDeliveryOptionsTransformRunResult> {
    let no_changes = schema::CartDeliveryOptionsTransformRunResult { operations: vec![] };

    let mut operations = Vec::new();

    // Process each delivery group
    let cart = &input.cart();
    if cart.delivery_groups().is_empty() {
        return Ok(no_changes);
    }

    for group in cart.delivery_groups() {
        for option in group.delivery_options() {
            if let Some(title) = option.title() {
                if title.to_lowercase().contains("express") {
                    let rename_op = schema::DeliveryOptionRenameOperation {
                        delivery_option_handle: option.handle().clone(),
                        title: format!("{} (1-2 days)", title),
                    };

                    operations.push(schema::Operation::DeliveryOptionRename(rename_op));
                }
            }
        }
    }

    if operations.is_empty() {
        return Ok(no_changes);
    }

    Ok(schema::CartDeliveryOptionsTransformRunResult { operations })
}
```

Performance: Rust 46002, JavaScript 245120 instructions.

##### Hide Shipping Options by Zip Code Using Metaobjects

Hides specific shipping methods when the buyer's zip code is on a restricted list, with configurations stored in a shop-level metaobject (`$app:shipping_restriction`/`default`, fields `restricted_zip_codes` and `hidden_delivery_option_title`). Matches by title, then hides the option by handle.

---

## Payment Customization

### Payment Customization Function API

> Fonte: https://shopify.dev/docs/api/functions/latest/payment-customization

A payment customization enables you to rename, reorder, and hide the payment methods available to customers during checkout, set payment terms, and add a review requirement for a specific order. Customizable payment methods include credit cards, gift cards, and wallets such as Shop Pay, Apple Pay, and Google Pay.

Payment terms allow buyers to pay for their order at a later date instead of at checkout, and can be set as fixed, net, or event-based terms with optional deposits. A review requirement enables you to control whether an order is submitted as a draft for review (B2B orders only). To customize payment methods and payment terms in checkout, you can use the Payment Customization Function API.

**Note:** You can activate a maximum of 25 payment customization functions on each store.

#### Use Cases

- Hide payment methods for carts with totals above or below a given value.
- Reorder payment methods according to customer preference.
- Hide payment methods based on the customer's country.
- Hide and disable gift cards based on data such as cart contents and country.
- Set payment terms with deposits for high-value orders.
- Apply net payment terms based on buyer identity.
- Set a review requirement for specific orders, such as high-value ones.

#### Function Target — Checkout — Compatibility with Shopify Surfaces

| Surface | Status |
|---------|--------|
| B2B | Supported |
| Cart | Not supported |
| Checkout | Supported |
| Create Order API | Not supported |
| Draft Order (Admin) | Not supported |
| Draft Order (Checkout) | Supported |
| Order Edit (Admin) | Not supported |
| Order Edit (Checkout) | Not supported |
| POS | Not supported |
| Pre-order and Try Before You Buy | Supported |
| Shopify Admin | Not supported |
| Storefront | Not supported |
| Storefront Accelerated Checkout | Partially supported (payment terms aren't supported in storefront accelerated checkouts) |
| Subscription (Recurring Orders) | Not supported |

**Note:** Payment terms are incompatible with subscriptions. Payment customization functions cannot set payment terms when the cart contains items with subscription selling plans.

#### Getting Started

```terminal
shopify app generate extension --template payment_customization
```

Tutorial: [Build a payment customization function](https://shopify.dev/docs/apps/build/checkout/payments)

#### Run Target — `cart.payment-methods.transform.run`

The run target customizes payment methods using Shopify data or hardcoded values. The target returns an ordered list of operations to be applied to payment methods, payment terms, and review requirements.

##### Input (top-level fields)

* `cart` (Cart!) — The cart where the function is running.
* `localization` (Localization!) — Regional and language settings.
* `paymentCustomization` (PaymentCustomization!) — Configuration of the app that owns the function.
* `paymentMethods` ([PaymentCustomizationPaymentMethod!]!) — List of payment methods available during checkout.
* `presentmentCurrencyRate` (Decimal!) — Exchange rate.
* `shop` (Shop!) — Shop information including timezone and metafields.

##### Output — `CartPaymentMethodsTransformRunResult`

* `operations` ([Operation!]!) — The ordered list of operations:
  * **PaymentMethodHide** — `paymentMethodId` (ID!), `placements` ([PaymentCustomizationPaymentMethodPlacement!], optional; if not provided, all placements are hidden).
  * **PaymentMethodMove** — `paymentMethodId` (ID!), `index` (Int!).
  * **PaymentMethodRename** — `paymentMethodId` (ID!), `name` (String!).
  * **PaymentTermsSet** — `paymentTerms` (PaymentTerms — `event` EventPaymentTerms, `fixed` FixedPaymentTerms, `net` NetPaymentTerms; nil for no payment terms). Available on Shopify Plus stores only.
  * **OrderReviewAdd** — `reason` (String!): the reason for the review requirement (the checkout will be submitted as a draft, requiring merchant review). B2B purchases on Shopify Plus stores only.

#### Examples

##### Reorder Payment Methods

Reorders payment methods based on a configurable desired order stored in an app metafield (`$app:payment-customization`/`configuration`).

```rust
use crate::schema;
use shopify_function::prelude::*;
use shopify_function::Result;

#[derive(Deserialize, Default, PartialEq)]
pub struct Configuration {
    payment_methods: Vec<String>,
}

#[shopify_function]
fn cart_payment_methods_transform_run(input: schema::run::Input) -> Result<schema::CartPaymentMethodsTransformRunResult> {
    let config: &Configuration = match input.payment_customization().metafield() {
        Some(metafield) => metafield.json_value(),
        None => return Ok(schema::CartPaymentMethodsTransformRunResult { operations: vec![] }),
    };

    let mut operations = vec![];

    for (index, method_name) in config.payment_methods.iter().enumerate() {
        if let Some(method) = input.payment_methods().iter().find(|m| m.name() == method_name) {
            operations.push(schema::Operation::PaymentMethodMove(schema::PaymentMethodMoveOperation {
                payment_method_id: method.id().to_string(),
                index: index as i32,
            }));
        }
    }

    Ok(schema::CartPaymentMethodsTransformRunResult { operations })
}
```

```javascript
// @ts-check

/**
 * @typedef {import("../generated/api").CartPaymentMethodsTransformRunInput} CartPaymentMethodsTransformRunInput
 * @typedef {import("../generated/api").CartPaymentMethodsTransformRunResult} CartPaymentMethodsTransformRunResult
 */

/**
 * @param {CartPaymentMethodsTransformRunInput} input
 * @returns {CartPaymentMethodsTransformRunResult}
 */
export function cartPaymentMethodsTransformRun(input) {
  // Parse configuration from metafield, defaulting to empty payment_methods array
  const configuration = {
    payment_methods: [],
    ...(input.paymentCustomization.metafield?.jsonValue ?? {})
  };

  const operations = [];

  // Create move operations for each configured payment method
  configuration.payment_methods.forEach((methodName, index) => {
    const method = input.paymentMethods?.find(paymentMethod => paymentMethod.name === methodName);
    if (method) {
      operations.push({
        paymentMethodMove: {
          paymentMethodId: method.id,
          index
        }
      });
    }
  });

  return { operations };
}
```

Performance: Rust 44481, JavaScript 252136 instructions. Output: a list of `paymentMethodMove` operations with `index` 0..n.

##### Rename Payment Methods

Renames payment methods based on a configurable map stored in an app-owned metafield (e.g. "Credit Card" → "Visa/MasterCard").

```rust
use std::collections::HashMap;

use crate::schema;
use shopify_function::prelude::*;
use shopify_function::Result;

#[derive(Deserialize, Default, PartialEq)]
#[shopify_function(rename_all = "camelCase")]
pub struct RenameConfiguration {
    rename_map: HashMap<String, String>,
}

#[shopify_function]
fn cart_payment_methods_transform_run(input: schema::run::Input) -> Result<schema::CartPaymentMethodsTransformRunResult> {
    // Extract configuration from metafield
    let config: &RenameConfiguration = match input.payment_customization().metafield() {
        Some(metafield) => metafield.json_value(),
        None => return Ok(schema::CartPaymentMethodsTransformRunResult { operations: vec![] }),
    };

    // Convert to case-insensitive map
    let rename_map: HashMap<String, String> = config.rename_map.clone()
        .into_iter()
        .map(|(k, v)| (k.to_ascii_lowercase(), v))
        .collect();

    // Create rename operations based on the configuration, using case-insensitive comparison
    let operations: Vec<schema::Operation> = input.payment_methods()
        .iter()
        .filter_map(|method| {
            rename_map.get(&method.name().to_ascii_lowercase()).map(|new_name| {
                schema::Operation::PaymentMethodRename(schema::PaymentMethodRenameOperation {
                    payment_method_id: method.id().to_string(),
                    name: new_name.clone(),
                })
            })
        })
        .collect();

    Ok(schema::CartPaymentMethodsTransformRunResult { operations })
}
```

Performance: Rust 49642, JavaScript 273553 instructions.

##### Hide Payment Methods Based on Customer Tags

Hides a configurable payment method for customers without a specific tag (configuration in an app-owned metafield). Reads `cart.buyerIdentity.customer.hasTags(tags: $tags_list)`.

```rust
use crate::schema;
use shopify_function::prelude::*;
use shopify_function::Result;
use std::collections::HashMap;

#[derive(Deserialize, Default, PartialEq)]
pub struct PaymentRules {
    payment_methods: HashMap<String, Vec<String>>,
}

#[shopify_function]
fn cart_payment_methods_transform_run(input: schema::run::Input) -> Result<schema::CartPaymentMethodsTransformRunResult> {
    let customer_tags = input
        .cart()
        .buyer_identity()
        .and_then(|identity| identity.customer())
        .map(|customer| {
            customer
                .has_tags()
                .iter()
                .filter(|tag| *tag.has_tag())
                .map(|tag| tag.tag().to_string())
                .collect::<Vec<String>>()
        })
        .unwrap_or_default();

    let payment_rules: &PaymentRules = match input.payment_customization().metafield() {
        Some(metafield) => metafield.json_value(),
        None => return Ok(schema::CartPaymentMethodsTransformRunResult { operations: vec![] }),
    };

    let mut operations = vec![];

    for method in input.payment_methods() {
        let mut should_hide = true;

        // Check if this payment method is allowed for any of the customer's tags
        for tag in &customer_tags {
            if let Some(allowed_methods) = payment_rules.payment_methods.get(tag) {
                if allowed_methods.contains(&method.name()) {
                    should_hide = false;
                    break;
                }
            }
        }

        if should_hide {
            operations.push(schema::Operation::PaymentMethodHide(schema::PaymentMethodHideOperation {
                payment_method_id: method.id().to_string(),
                placements: None,
            }));
        }
    }

    Ok(schema::CartPaymentMethodsTransformRunResult { operations })
}
```

Performance: Rust 53722, JavaScript 260275 instructions.

##### Hide Payment Methods for Small Orders

Hides certain payment methods when the cart total is below a configurable threshold (`minimum_amount` + `payment_method_ids` in a metafield).

```rust
use crate::schema;
use shopify_function::prelude::*;
use shopify_function::Result;

#[derive(Deserialize, Default, PartialEq)]
pub struct Configuration {
    minimum_amount: f64,
    payment_method_ids: Vec<String>,
}

#[shopify_function]
fn cart_payment_methods_transform_run(input: schema::run::Input) -> Result<schema::CartPaymentMethodsTransformRunResult> {
    // Get configuration or return empty result if no metafield is set
    let config: &Configuration= match input.payment_customization().metafield() {
        Some(metafield) => metafield.json_value(),
        None => return Ok(schema::CartPaymentMethodsTransformRunResult { operations: vec![] }),
    };

    let cart_total = input.cart().cost().total_amount().amount().0;

    // If cart total is below minimum, hide specified payment methods
    if cart_total < config.minimum_amount {
        let payment_methods: std::collections::HashSet<String> =
            input.payment_methods()
                .into_iter()
                .map(|method| method.id().to_string())
                .collect();

        let operations = config.payment_method_ids
            .iter()
            .filter(|id| payment_methods.contains(*id))
            .map(|id| {
                schema::Operation::PaymentMethodHide(schema::PaymentMethodHideOperation {
                    payment_method_id: id.clone(),
                    placements: None,
                })
            })
            .collect();

        return Ok(schema::CartPaymentMethodsTransformRunResult { operations });
    }

    Ok(schema::CartPaymentMethodsTransformRunResult { operations: vec![] })
}
```

Performance: Rust 34975, JavaScript 171374 instructions.

##### Hide Payment Methods Based on Customer Location

Hides certain payment methods based on the buyer's country code (`localization.country.isoCode`), with per-method `excluded_countries` in a metafield. Performance: Rust 47301, JavaScript 257924 instructions.

---

## Fulfillment Constraints

### Fulfillment Constraints Function API

> Fonte: https://shopify.dev/docs/api/functions/latest/fulfillment-constraints

Use the Fulfillment Constraints Function API to configure constraints for fulfilling orders. You can specify a list of locations where cart items can be fulfilled from, or specify that cart items must be fulfilled from the same location. If cart items with fulfillment constraints aren't available at the same location or any listed locations, buyers won't see shipping options at checkout — instead, a message displays which items are out of stock, preventing purchase completion. This API is the only way to configure these constraints.

The Fulfillment Constraints API integrates this logic into the checkout flow, allowing you to customize fulfillment and delivery strategies for specific cart items using associated data such as buyer identity, metafields, and location addresses.

**Note:** You can activate a maximum of 25 fulfillment constraint functions on each store.

#### Use Cases

* Fulfill specific items in a cart from the same location.
* Fulfill specific items in a cart from any of the locations in a list.

#### Function Target — Checkout — Compatibility with Shopify Surfaces

| Surface | Support Level |
|---------|---------------|
| B2B | Supported |
| Cart | Supported |
| Checkout | Supported |
| Create Order API | Supported |
| Draft Order (Admin) | Supported |
| Draft Order (Checkout) | Supported |
| Order Edit (Admin) | Partially supported (new items only) |
| Order Edit (Checkout) | Not supported |
| POS | Partially supported (shipping to customer only) |
| Pre-order and Try Before You Buy | Not supported |
| Shopify Admin | Supported |
| Storefront | Partially supported (Buy with Prime only) |
| Storefront Accelerated Checkout | Supported |
| Subscription (Recurring Orders) | Supported |

#### Getting Started

```terminal
shopify app generate extension --template fulfillment_constraints
```

Tutorial: [Build a Fulfillment Constraints Function](https://shopify.dev/docs/apps/build/orders-fulfillment/order-routing-apps/build-fulfillment-constraints-function)

#### Run Target — `cart.fulfillment-constraints.generate.run`

The run target indicates which locations fulfill specific cart items, using Shopify data or hardcoded values. The target returns a list of operations applying fulfillment constraints. Example: fulfill specific cart items from any locations in a list.

##### Input (top-level fields)

* `cart` (Cart!) — The cart where the Function runs.
* `fulfillmentConstraintRule` (FulfillmentConstraintRule!) — Backend logic for determining order fulfillment, including associated metafields.
* `localization` (Localization!) — Regional and language settings.
* `locations` ([Location!]!) — All geographical locations where inventory is stored (warehouses, retail locations, distribution centers).
* `presentmentCurrencyRate` (Decimal!) — Exchange rate.
* `shop` (Shop!) — Shop information including timezone and metafields.

**Caution:** If `CartFulfillmentConstraintsGenerateRunResult` returns mutually exclusive constraints, checkout won't return shipping rates. For example, you may not fulfill an item from two locations or two items together if they require different locations.

##### Output — `CartFulfillmentConstraintsGenerateRunResult`

* `operations` ([Operation!]!):
  * **deliverableLinesMustFulfillFromAdd** (DeliverableLinesMustFulfillFromAddOperation) — Force specific items to fulfill from designated locations. `deliverableLineIds` ([ID!]), `locationIds` ([ID!]!). If cart items aren't stocked at specified locations, checkout won't return shipping rates and completing checkout is blocked.
  * **deliverableLinesMustFulfillFromSameLocationAdd** (DeliverableLinesMustFulfillFromSameLocationAddOperation) — Force specific items to fulfill from the same location. `deliverableLineIds` ([ID!]). If constrained items aren't stocked at the same location, checkout won't return shipping rates.

#### Examples

##### Example 1: Prevent Splitting Low-Subtotal Carts

Checks if the cart is below a configurable subtotal; if so, returns a constraint preventing the cart from splitting into multiple shipments (`$app:fulfillment-constraints`/`configuration` metafield with `threshold`).

```rust
use crate::schema;
use shopify_function::prelude::*;
use shopify_function::Result;

#[derive(Deserialize, Default, PartialEq)]
pub struct Configuration {
    threshold: f64,
}

#[shopify_function]
fn cart_fulfillment_constraints_generate_run(
    input: schema::cart_fulfillment_constraints_generate_run::Input,
) -> Result<schema::CartFulfillmentConstraintsGenerateRunResult> {
    // Parse configuration from metafield
    let config = match input.fulfillment_constraint_rule().metafield() {
        Some(metafield) => metafield.json_value(),
        None => &Configuration::default(),
    };

    // Get the cart subtotal and convert threshold to Decimal
    let subtotal = input.cart().cost().subtotal_amount().amount();
    let threshold = Decimal::from(config.threshold);

    // If the subtotal is below the threshold, prevent splitting
    if subtotal.lt(&threshold) {
        let deliverable_line_ids: Vec<String> = input
            .cart()
            .deliverable_lines()
            .iter()
            .map(|line| line.id().clone())
            .collect();

        let operations = vec![
            schema::Operation::DeliverableLinesMustFulfillFromSameLocationAdd(
                schema::DeliverableLinesMustFulfillFromSameLocationAddOperation {
                    deliverable_line_ids: Some(deliverable_line_ids),
                },
            ),
        ];

        return Ok(schema::CartFulfillmentConstraintsGenerateRunResult { operations });
    }

    // No constraints if the subtotal is above the threshold
    Ok(schema::CartFulfillmentConstraintsGenerateRunResult { operations: vec![] })
}
```

```javascript
// @ts-check

/**
 * @typedef {import("../generated/api").RunInput} RunInput
 * @typedef {import("../generated/api").CartFulfillmentConstraintsGenerateRunResult} CartFulfillmentConstraintsGenerateRunResult
 */

/**
 * @type {CartFulfillmentConstraintsGenerateRunResult}
 */
const NO_CHANGES = {
  operations: [],
};

/**
 * @param {RunInput} input
 * @returns {CartFulfillmentConstraintsGenerateRunResult}
 */
export function cartFulfillmentConstraintsGenerateRun(input) {
  // Parse configuration from metafield
  const configuration = input.fulfillmentConstraintRule.metafield?.jsonValue ?? "{}"

  // If no configuration is provided, return no changes
  if (!configuration.threshold) {
    return NO_CHANGES;
  }

  // Get the cart subtotal
  const subtotal = parseFloat(input.cart.cost.subtotalAmount.amount);

  // If the subtotal is below the threshold, prevent splitting
  if (subtotal < configuration.threshold) {
    return {
      operations: [
        {
          deliverableLinesMustFulfillFromSameLocationAdd: {
            deliverableLineIds: input.cart.deliverableLines.map(line => line.id)
          }
        }
      ]
    };
  }

  // No constraints if the subtotal is above the threshold
  return NO_CHANGES;
}
```

Performance: Rust 33239, JavaScript 192667 instructions.

##### Example 2: Ensure Bundle Items Fulfill from Same Location

Groups items with the same `bundle` attribute value and returns a constraint requiring all same-bundle items to fulfill from the same location.

```rust
use crate::schema;
use shopify_function::prelude::*;
use shopify_function::Result;

#[shopify_function]
fn cart_fulfillment_constraints_generate_run(
    input: schema::cart_fulfillment_constraints_generate_run::Input,
) -> Result<schema::CartFulfillmentConstraintsGenerateRunResult> {
    let mut bundle_groups: std::collections::HashMap<String, Vec<String>> =
        std::collections::HashMap::new();

    // Group deliverable lines by their bundle attribute value
    for line in input.cart().deliverable_lines().iter() {
        if let Some(attribute) = &line.attribute() {
            if attribute.key() == "bundle" {
                if let Some(value) = &attribute.value() {
                    bundle_groups
                        .entry(value.to_string())
                        .or_insert_with(Vec::new)
                        .push(line.id().clone());
                }
            }
        }
    }

    // Create constraints for each bundle group
    let operations: Vec<schema::Operation> = bundle_groups
        .values()
        .filter(|group| group.len() > 1) // Only create constraints for groups with more than one item
        .map(|group| {
            schema::Operation::DeliverableLinesMustFulfillFromSameLocationAdd(
                schema::DeliverableLinesMustFulfillFromSameLocationAddOperation {
                    deliverable_line_ids: Some(group.clone()),
                },
            )
        })
        .collect();

    Ok(schema::CartFulfillmentConstraintsGenerateRunResult { operations })
}
```

Performance: Rust 40411, JavaScript 234106 instructions.

##### Example 3: Require Large Orders to Fulfill from Warehouses

Builds a constraint requiring all items to fulfill from a warehouse once the cart exceeds a configurable item limit. Filters locations by a `custom`/`type` metafield equal to `warehouse`, and applies `deliverableLinesMustFulfillFromAdd` with `locationIds`.

```rust
use crate::schema;
use shopify_function::prelude::*;
use shopify_function::Result;

#[derive(Deserialize, Default, PartialEq)]
struct Configuration {
    item_limit: i32,
}

#[shopify_function]
fn cart_fulfillment_constraints_generate_run(
    input: schema::cart_fulfillment_constraints_generate_run::Input,
) -> Result<schema::CartFulfillmentConstraintsGenerateRunResult> {
    // Parse item limit from metafield
    let item_limit: i32 = input
        .fulfillment_constraint_rule()
        .metafield()
        .as_ref()
        .and_then(|metafield| metafield.value().parse().ok())
        .unwrap_or(i32::MAX);

    // Check if the cart exceeds the item limit
    let cart_item_count = input.cart().deliverable_lines().len() as i32;
    if cart_item_count <= item_limit {
        return Ok(schema::CartFulfillmentConstraintsGenerateRunResult { operations: vec![] });
    }

    // Filter locations that are marked as warehouses
    let warehouse_locations: Vec<String> = input
        .locations()
        .iter()
        .filter(|location| {
            location
                .metafield()
                .as_ref()
                .map_or(false, |m| m.value() == "warehouse")
        })
        .map(|location| location.id().clone())
        .collect();

    if warehouse_locations.is_empty() {
        return Ok(schema::CartFulfillmentConstraintsGenerateRunResult { operations: vec![] });
    }

    // Create fulfillment constraint
    let operations = vec![schema::Operation::DeliverableLinesMustFulfillFromAdd(
        schema::DeliverableLinesMustFulfillFromAddOperation {
            deliverable_line_ids: Some(
                input
                    .cart()
                    .deliverable_lines()
                    .iter()
                    .map(|line| line.id().clone())
                    .collect(),
            ),
            location_ids: warehouse_locations,
        },
    )];

    Ok(schema::CartFulfillmentConstraintsGenerateRunResult { operations })
}
```

Performance: Rust 44382, JavaScript 241495 instructions.

##### Example 4: Prevent Fulfillment at Capacity Locations

Requires all items to fulfill from other locations when a location has a `capacity`/`is_at_capacity` metafield set to `"true"`. Performance: Rust 36030, JavaScript 210384 instructions.

##### Example 5: Prevent Discounted Items from Retail Location Fulfillment

Removes retail locations from fulfillment options if the cart has discounted items (compares `amountPerQuantity` vs `compareAtAmountPerQuantity`). Retail locations are identified by a `custom`/`location_type` metafield value of `retail`. Performance: Rust 63503, JavaScript 363041 instructions.

---

## Order Routing (Location Rule)

### Order Routing Location Rule Function API

> Fonte: https://shopify.dev/docs/api/functions/latest/order-routing-location-rule

The Order Routing Location Rule Function API enables merchants to define custom rules that prioritize fulfillment locations during order routing. Order routing determines the location to fulfill each item in a cart. A set of rules are used to evaluate an order and prioritize fulfillment locations. Location rules enable splitting multi-unit orders across different fulfillment locations.

**Key capabilities:**

* Customize Shopify's backend order fulfillment logic through Shopify Functions.
* Integrate custom rules into checkout flows, draft orders, order editing, and order imports.
* Access and re-trigger logic via the Shopify admin or API after checkout.

**Beta Status:** This API is exclusively available by request for merchants with a Shopify Plus plan and enrolled in the Partners program.

#### Use Cases

* Fulfill orders from the nearest location serving the shop's market.
* Prioritize location groups such as warehouses or retail stores.
* Rank locations relative to each other based on product metafields.
* Deprioritize locations exceeding maximum daily order capacity.
* Prioritize locations with faster fulfillment or specific inventory rotation levels.

#### Function Target — Checkout — Supported Surfaces

| Surface | Status | Notes |
|---------|--------|-------|
| B2B | Supported | — |
| Cart | Supported | — |
| Checkout | Supported | — |
| Create Order API | Supported | — |
| Draft Order (Admin) | Supported | — |
| Draft Order (Checkout) | Supported | — |
| Order Edit (Admin) | Partially supported | New items only |
| Order Edit (Checkout) | Not supported | — |
| POS | Partially supported | Shipping to customer only |
| Pre-order and Try Before You Buy | Not supported | — |
| Shopify Admin | Supported | — |
| Storefront | Partially supported | Buy with Prime only |
| Storefront Accelerated Checkout | Supported | — |
| Subscription (Recurring Orders) | Not supported | — |

#### Getting Started

```terminal
shopify app generate extension --template order_routing_location_rule
```

Tutorial: [Build an Order Routing Location Rule Function](https://shopify.dev/docs/apps/build/orders-fulfillment/order-routing-apps/location-rules/build-location-rule-function)

#### Run Target — `cart.fulfillment-groups.location-rankings.generate.run`

Ranks locations using Shopify data or hardcoded values. Locations must be associated with a fulfillment group to be ranked. The target returns operations applied to locations within fulfillment groups. Example: prioritize warehouses over storefront locations.

##### Input (top-level fields)

* **cart** (Cart!) — The cart being processed.
* **fulfillmentGroups** ([FulfillmentGroup!]!) — Fulfillment locations containing items to ship together.
* **locations** ([Location!]!) — All geographical inventory storage locations.
* **localization** (Localization!) — Regional/language settings.
* **locationRule** (OrderRoutingLocationRule!) — Backend order routing logic and associated metafields.
* **presentmentCurrencyRate** (Decimal!) — Exchange rate.
* **shop** (Shop!) — Shop information including timezone and metafields.

##### Output — `CartFulfillmentGroupsLocationRankingsGenerateRunResult`

* `operations` ([Operation!]!) — Each operation specifies location rankings for a fulfillment group.
* **FulfillmentGroupLocationRankingAddOperation** — `fulfillmentGroupHandle` (Handle!), `rankings` ([RankedLocation!]! — `locationHandle` (Handle!), `rank` (Int!)).

#### Examples

##### Example 1: Location Priority Rule for Perishable Products

Prioritizes locations with a metafield `is_perishable` when the cart contains products tagged "perishable."

Input Query (Rust):

```graphql
query Input {
  fulfillmentGroups {
    handle
    inventoryLocationHandles
    lines {
      merchandise {
        __typename
        ... on ProductVariant {
          product {
            id
            hasTags(tags: ["perishable"]) {
              hasTag
              tag
            }
          }
        }
      }
    }
  }
  locations {
    handle
    metafield(namespace: "custom", key: "is_perishable") {
      jsonValue
    }
  }
}
```

Function Code (Rust):

```rust
use crate::schema;
use shopify_function::prelude::*;
use shopify_function::Result;
use std::collections::HashMap;

#[derive(Deserialize, PartialEq)]
#[shopify_function(rename_all = "camelCase")]
pub struct Configuration {
    is_perishable: bool,
}

#[shopify_function]
fn cart_fulfillment_groups_location_rankings_generate_run(
    input: schema::cart_fulfillment_groups_location_rankings_generate_run::Input,
) -> Result<schema::CartFulfillmentGroupsLocationRankingsGenerateRunResult> {
    // Create a map of location handles to their perishable status
    let mut perishable_locations = HashMap::new();

    for location in input.locations() {
        let is_perishable = match &location.metafield() {
            Some(metafield) => {
                let config: &Configuration = metafield.json_value();
                config.is_perishable
            }
            None => false,
        };

        perishable_locations.insert(location.handle().clone(), is_perishable);
    }

    let operations = input
        .fulfillment_groups()
        .iter()
        .map(|group| {
            // Check if any products in this group have the perishable tag
            let has_perishable_product = group
                .lines()
                .iter()
                .filter_map(|line| {
                    match &line.merchandise() {
                        schema::cart_fulfillment_groups_location_rankings_generate_run::input::fulfillment_groups::lines::Merchandise::ProductVariant(variant) => {
                            Some(variant.product())
                        },
                        _ => None,
                    }
                })
                .any(|product| {
                    product.has_tags().iter().any(|tag_resp| *tag_resp.has_tag())
                });

            let rankings = group
                .inventory_location_handles()
                .iter()
                .map(|location_handle| {
                    let mut rank = 0;

                    // If we have perishable products, prioritize locations with perishable:true metafield
                    if has_perishable_product {
                        // Locations that can handle perishables get rank 0, others get rank 1 (lower priority)
                        if let Some(is_perishable_location) = perishable_locations.get(location_handle) {
                            if !is_perishable_location {
                                rank = 1; // Deprioritize locations that can't handle perishables
                            }
                        } else {
                            rank = 1; // If location not found in our map, deprioritize it
                        }
                    }

                    schema::RankedLocation {
                        location_handle: location_handle.clone(),
                        rank,
                    }
                })
                .collect::<Vec<schema::RankedLocation>>();

            schema::Operation::FulfillmentGroupLocationRankingAdd(schema::FulfillmentGroupLocationRankingAddOperation {
                fulfillment_group_handle: group.handle().clone(),
                rankings,
            })
        })
        .collect();

    Ok(schema::CartFulfillmentGroupsLocationRankingsGenerateRunResult { operations })
}
```

Function Code (JavaScript):

```javascript
// @ts-check

/**
 * @typedef {import("../generated/api").RunInput} RunInput
 * @typedef {import("../generated/api").CartFulfillmentGroupsLocationRankingsGenerateRunResult} CartFulfillmentGroupsLocationRankingsGenerateRunResult
 */

/**
 * @param {RunInput} input
 * @returns {CartFulfillmentGroupsLocationRankingsGenerateRunResult}
 */
export function cartFulfillmentGroupsLocationRankingsGenerateRun(input) {
  // Create a map of location handles to their perishable status
  const perishableLocations = new Map();

  if (input.locations) {
    input.locations.forEach(location => {
      let isPerishable = false;

      if (location.metafield && location.metafield.jsonValue) {
        try {
          // Handle both string JSON and already parsed objects
          const metafieldValue = typeof location.metafield.jsonValue === 'string'
            ? JSON.parse(location.metafield.jsonValue)
            : location.metafield.jsonValue;

          // Check for isPerishable (camelCase)
          isPerishable = metafieldValue.isPerishable === true;
        } catch (error) {
          // If parsing fails, assume the location is not perishable
          isPerishable = false;
        }
      }

      perishableLocations.set(location.handle, isPerishable);
    });
  }

  const operations = input.fulfillmentGroups.map((group) => {
    // Check if any products in this group have the perishable tag
    const hasPerishableProduct = (group.lines || []).some(line =>
      line.merchandise &&
      line.merchandise.__typename === "ProductVariant" &&
      line.merchandise.product &&
      Array.isArray(line.merchandise.product.hasTags) &&
      line.merchandise.product.hasTags.some(tagResp => tagResp.hasTag)
    );

    const rankings = (group.inventoryLocationHandles || []).map((inventoryLocationHandle) => {
      let rank = 0;

      // If we have perishable products, prioritize locations with perishable:true metafield
      if (hasPerishableProduct) {
        // Locations that can handle perishables get rank 0, others get rank 1 (lower priority)
        const isPerishableLocation = perishableLocations.get(inventoryLocationHandle) || false;
        if (!isPerishableLocation) {
          // Deprioritize locations that can't handle perishables
          rank = 1;
        }
      }

      return {
        locationHandle: inventoryLocationHandle,
        rank,
      };
    });

    return {
      fulfillmentGroupLocationRankingAdd: {
        fulfillmentGroupHandle: group.handle,
        rankings,
      },
    };
  });

  return {operations};
}
```

Output JSON:

```json
{
  "operations": [
    {
      "fulfillmentGroupLocationRankingAdd": {
        "fulfillmentGroupHandle": "1",
        "rankings": [
          { "locationHandle": "91260846373", "rank": 0 },
          { "locationHandle": "91260879141", "rank": 1 }
        ]
      }
    }
  ]
}
```

##### Further examples (summaries)

* **Example 2: Deprioritize Fulfillment Locations for Age-Restricted Products** — Deprioritizes locations when the cart contains products tagged "21 year plus."
* **Example 3: Prioritize Locations for B2B Orders** — Checks for B2B orders via `cart.buyerIdentity.purchasingCompany`; routes to locations with a `routing.acceptsb2b` metafield set to `"true"`.
* **Example 4: Prioritize Locations Based on Delivery Address** — Prioritizes locations in the same province as the delivery address.

---

## Delivery methods: Local Pickup & Pickup Point generators

### Local Pickup Delivery Option Generator Function API

> Fonte: https://shopify.dev/docs/api/functions/unstable/local-pickup-delivery-option-generator

Local pickup enables customers to retrieve online orders from retail locations instead of receiving shipped items. The Local Pickup Delivery Option Generator Function API is the sole method for displaying these pickup options. Use this API to permit local pickup during specific timeframes, or designate products available exclusively for pickup at particular locations.

**Note:** Checkouts and orders can include multiple delivery methods. Iterate over all delivery groups or fulfillment orders to determine the delivery method for each.

**Note:** Only custom apps installed on stores on the Shopify Plus plan can use this API. Merchants must participate in the Partners program to implement custom apps and location rules.

#### Use Cases

* Display local pickup options even when location inventory is depleted, provided items can transfer from another location.
* Restrict local pickup options to VIP customers exclusively.
* Adjust pickup lead times based on cart contents.
* Apply fees for in-store local pickup orders (such as $5 USD for two-hour pickup, free otherwise).

#### Function Target — Checkout — Compatibility with Shopify Surfaces

| Surface | Status |
|---------|--------|
| B2B | Not supported |
| Cart | Supported |
| Checkout | Supported |
| Create Order API | Not supported |
| Draft Order (Admin) | Supported |
| Draft Order (Checkout) | Supported |
| Order Edit (Admin) | Not supported |
| Order Edit (Checkout) | Not supported |
| POS | Not supported |
| Pre-order and Try Before You Buy | Not supported |
| Shopify Admin | Supported |
| Storefront | Not supported |
| Storefront Accelerated Checkout | Partially supported (decelerated checkouts only; payment sheet unsupported) |
| Subscription (Recurring Orders) | Not supported |

**Fetch Target — Limited access:** restricted to custom apps on Enterprise stores and requires a network access request.

#### Getting Started

```terminal
shopify app generate extension --template local_pickup_delivery_option_generator
```

Tutorial: [Generate local pickup delivery options](https://shopify.dev/docs/apps/build/orders-fulfillment/order-routing-apps/build-local-pickup-options-function)

#### Run Target — `purchase.local-pickup-delivery-option-generator.run`

The run target generates custom local pickup options using Shopify data or hardcoded values, returning a list of operations to display local pickup options.

##### Input (top-level fields)

* `cart` (Cart!), `deliveryOptionGenerator` (DeliveryOptionGenerator!), `fetchResult` (HttpResponse), `fulfillmentGroups` ([FulfillmentGroup!]!), `localization` (Localization!), `locations` ([Location!]!), `presentmentCurrencyRate` (Decimal!), `shop` (Shop!).

##### Output — `FunctionRunResult`

* `operations` ([Operation!]!):
  * `add` (LocalPickupDeliveryOption!): `cost` (Decimal, defaults to zero), `metafields` ([MetafieldOutput!]), `pickupLocation` (PickupLocation! — `locationHandle` (Handle!), `pickupInstruction` (String)), `title` (String, defaults to location name).

#### Examples

##### Create Local Pickup Options with Fees

Adds fees based on a `custom`/`pickup_fee` location metafield; only includes locations where `localPickup.enabled` is true.

Input Query (Rust):

```graphql
query Input {
  locations {
    handle
    pickupFee: metafield(namespace: "custom", key: "pickup_fee") {
      value
    }
    localPickup {
      enabled
    }
  }
}
```

Function Code (Rust):

```rust
use crate::schema;
use shopify_function::prelude::*;
use shopify_function::Result;

const DEFAULT_PICKUP_INSTRUCTION: &str = "Pickup available within 24 hours.";

#[shopify_function]
fn run(input: schema::run::Input) -> Result<schema::FunctionRunResult> {
    let mut delivery_options = vec![];
    let pickup_instruction = DEFAULT_PICKUP_INSTRUCTION.to_string();

    for location in input.locations().iter() {
        if !location.local_pickup().enabled() {
            continue;
        }

        // Get pickup fee from metafield, default to 0 if not set or invalid
        let pickup_fee = location
            .pickup_fee()
            .as_ref()
            .map_or(Decimal::from(0.0), |metafield| {
                metafield.value().parse::<f64>()
                    .map_or(Decimal::from(0.0), Decimal::from)
            });

        delivery_options.push(schema::Operation {
            add: schema::LocalPickupDeliveryOption {
                title: None,
                cost: Some(pickup_fee),
                pickup_location: schema::PickupLocation {
                    location_handle: location.handle().clone(),
                    pickup_instruction: Some(pickup_instruction.clone()),
                },
                metafields: None,
            },
        });
    }

    Ok(schema::FunctionRunResult { operations: delivery_options })
}
```

Function Code (JavaScript):

```javascript
// @ts-check

/**
 * @typedef {import("../generated/api").RunInput} RunInput
 * @typedef {import("../generated/api").FunctionRunResult} FunctionRunResult
 */

const DEFAULT_PICKUP_INSTRUCTION = "Pickup available within 24 hours.";

/**
 * @param {RunInput} input
 * @returns {FunctionRunResult}
 */
export function run(input) {
  const operations = [];

  for (const location of input.locations) {
    if (!location.localPickup?.enabled) {
      continue;
    }

    // Get pickup fee from metafield, default to "0.0" if not set or invalid
    const pickupFee = location.pickupFee?.value || "0.0";

    operations.push({
      add: {
        cost: pickupFee,
        pickupLocation: {
          locationHandle: location.handle,
          pickupInstruction: DEFAULT_PICKUP_INSTRUCTION
        }      }
    });
  }

  return { operations };
}
```

Output JSON (Rust):

```json
{
  "operations": [
    {
      "add": {
        "cost": "5.0",
        "metafields": null,
        "pickupLocation": {
          "locationHandle": "1",
          "pickupInstruction": "Pickup available within 24 hours."
        },
        "title": null
      }
    }
  ]
}
```

Performance: Rust 27995, JavaScript 163144 instructions.

##### Further examples (summaries)

* **Apply Fees and Delayed Pickup for Bulky Items** — Charges higher fees and extends pickup timeframes for products tagged "bulky". (Rust 33579 / JS 205764)
* **Exclude Locations at Capacity from Local Pickup Options** — Removes options for locations hitting capacity limits stored in metafields. (Rust 33640 / JS 192838)
* **Limit Available Pickup Locations** — Finds inventory locations fulfilling all cart items, capping results at two locations. (Rust 60247 / JS 320160)
* **Create Pickup Locations with Custom Instructions** — Modifies pickup instructions based on shop metafield `jsonValue` values, with fallback defaults. (Rust 27457)

---

### Pickup Point Delivery Option Generator Function API

> Fonte: https://shopify.dev/docs/api/functions/unstable/pickup-point-delivery-option-generator

The Pickup Point Delivery Option Generator Function API enables you to generate custom pickup points available to buyers during checkout. A pickup point is a third-party location, such as a post office or convenience store, where customers can choose to have their orders delivered at checkout. To generate pickup point delivery options, you can only use this API unless merchants are in specific regions wanting to use selected carrier services that Shopify already integrates with.

**Note:** Checkouts and orders can include multiple delivery methods. Iterate over all delivery groups or fulfillment orders to determine the delivery method for each.

#### Use Cases

Add nearby pickup points for customers to select at checkout and provide associated costs, distance, and hours of operation.

#### Function Target — Checkout — Compatibility with Shopify Surfaces

| Surface | Status |
|---------|--------|
| B2B | Not supported |
| Cart | Not supported |
| Checkout | Supported |
| Create Order API | Not supported |
| Draft Order (Admin) | Not supported |
| Draft Order (Checkout) | Supported |
| Order Edit (Admin) | Not supported |
| Order Edit (Checkout) | Not supported |
| POS | Not supported |
| Pre-order and Try Before You Buy | Not supported |
| Shopify Admin | Supported |
| Storefront | Not supported |
| Storefront Accelerated Checkout | Supported |
| Subscription (Recurring Orders) | Not supported |

#### Getting Started

```terminal
shopify app generate extension --template pickup_point_delivery_option_generator
```

Tutorial: [Generate pickup point delivery options](https://shopify.dev/docs/apps/build/checkout/delivery-shipping/delivery-methods/generate-pickup-points)

#### Targets

##### Fetch Target — `purchase.pickup-point-delivery-option-generator.fetch`

**Limited access:** available for custom apps installed on either development stores or stores on the Shopify Plus plan. The fetch target constructs an HTTP request that queries external pickup point providers and passes the result to the `fetchResult` field.

Input (top-level): `cart`, `deliveryAddress` (shipping/destination address), `localization`, `shop`.

Output: **FunctionFetchResult** — `request` (HttpRequest: `body` (String), `headers` ([HttpRequestHeader]), `jsonBody` (JSON), `method` (HttpRequestMethod: GET or POST), `policy` (HttpRequestPolicy with `readTimeoutMs`), `url` (URL)).

##### Run Target — `purchase.pickup-point-delivery-option-generator.run`

The run target generates pickup point delivery options using Shopify data, hardcoded values, or fetch results. Query the `fetchResult` field to access cached responses from the fetch target.

Output: **FunctionRunResult** — `operations` ([Operation]):

* `add` (PickupPointDeliveryOption):
  * `cost` (Decimal, optional)
  * `metafields` ([MetafieldOutput] — `key`, `namespace`, `type`, `value`)
  * `pickupPoint` (PickupPoint):
    * `address` (PickupAddress — `address1`, `address2`, `city`, `country`, `countryCode`, `latitude`, `longitude`, `phone`, `province`, `provinceCode`, `zip`)
    * `businessHours` ([BusinessHours] — `day` (Weekday: MONDAY–SUNDAY), `periods` ([BusinessHoursPeriod] — `openingTime`, `closingTime` as TimeWithoutTimezone))
    * `externalId` (String) — Third-party service's unique ID
    * `name` (String) — Third-party assigned pickup point name
    * `provider` (Provider — `logoUrl` (URL, must be a `https://cdn.shopify.com` base), `name` (String))

#### Example: Create Pickup Point Options from an External API

Demonstrates how to fetch pickup points from an external API and format the data into output JSON: use the fetch query to get parameters for the external API, pass them to an external API that returns pickup points, use the run query to access the cached response, and format external data into the required output JSON.

**Important:** Output must always be valid JSON without comments. Always include every day of the week for `businessHours`. Pass parameters from `fetch.graphql` exactly as provided — do not truncate or remove decimal places from longitude and latitude.

Fetch Target Input Query (Rust):

```graphql
query Input {
  deliveryAddress {
    countryCode
    longitude
    latitude
  }
}
```

Fetch Target Function Code (Rust):

```rust
use crate::schema;
use shopify_function::prelude::*;
use shopify_function::Result;

#[shopify_function]
fn fetch(input: schema::fetch::Input) -> Result<schema::FunctionFetchResult> {
    let delivery_address = &input.delivery_address();
    if let (Some(country_code), Some(longitude), Some(latitude)) = (
        &delivery_address.country_code(),
        &delivery_address.longitude(),
        &delivery_address.latitude(),
    ) {
        if country_code.as_str() == "CA" {
            return Ok(schema::FunctionFetchResult {
                request: Some(build_external_api_request(latitude, longitude)),
            });
        }
    }

    Ok(schema::FunctionFetchResult { request: None })
}

fn build_external_api_request(latitude: &f64, longitude: &f64) -> schema::HttpRequest {
    // The latitude and longitude parameters are included in the URL for demonstration purposes only. They do not influence the result.
    let url = format!("https://cdn.shopify.com/s/files/1/0628/3830/9033/files/pickup-points-external-api-dev-assistant.json?v=1747238482&lat={}&lon={}", latitude, longitude);

    schema::HttpRequest {
        method: schema::HttpRequestMethod::Get,
        url,
        headers: vec![schema::HttpRequestHeader {
            name: "Accept".to_string(),
            value: "application/json; charset=utf-8".to_string(),
        }],
        body: None,
        json_body: None,
        policy: schema::HttpRequestPolicy {
            read_timeout_ms: 500,
        },
    }
}
```

Fetch Target Function Code (JavaScript):

```javascript
export function fetch(input) {
  let { countryCode, longitude, latitude } = input.deliveryAddress;
  if (longitude && latitude && countryCode === "CA") {
    return {
      request: buildExternalApiRequest(latitude, longitude),
    };
  }
  return { request: null };
}

function buildExternalApiRequest(latitude, longitude) {
  let url = `https://cdn.shopify.com/s/files/1/0628/3830/9033/files/pickup-points-external-api-dev-assistant.json?v=1747238482&lat=${latitude}&lon=${longitude}`;

  return {
    method: "GET",
    url,
    headers: [
      {
        name: "Accept",
        value: "application/json; charset=utf-8",
      },
    ],
    body: null,
    policy: {
      readTimeoutMs: 500,
    },
  };
}
```

Fetch Target Output JSON (Rust):

```json
{
  "request": {
    "body": null,
    "headers": [
      { "name": "Accept", "value": "application/json; charset=utf-8" }
    ],
    "jsonBody": null,
    "method": "GET",
    "policy": { "readTimeoutMs": 500 },
    "url": "https://cdn.shopify.com/s/files/1/0628/3830/9033/files/pickup-points-external-api-dev-assistant.json?v=1747238482&lat=45.3884227&lon=-75.66808"
  }
}
```

Run Target Input Query (Rust):

```graphql
query Input {
  fetchResult {
    status
    jsonBody
  }
}
```

Run Target Function Code (Rust):

```rust
use crate::schema;
use shopify_function::prelude::*;
use shopify_function::Result;

#[derive(Deserialize)]
#[shopify_function(rename_all = "camelCase")]
pub struct PickupPoints {
    delivery_points: Vec<schema::PickupPoint>
}

#[shopify_function]
fn run(input: schema::run::Input) -> Result<schema::FunctionRunResult> {
    if let Some(fetch_result) = input.fetch_result() {
        if *fetch_result.status() == 200 {
            if let Some(pickup_points) = fetch_result.json_body() {
                let operations = build_pickup_point_delivery_option_operations(&pickup_points.delivery_points);
                return Ok(schema::FunctionRunResult { operations });
            }
        }
    }
    Ok(schema::FunctionRunResult { operations: vec![] })
}

fn build_pickup_point_delivery_option_operations(
    pickup_points: &[schema::PickupPoint],
) -> Vec<schema::Operation> {
    pickup_points
        .iter()
        .map(|pickup_point| {
            schema::Operation {
                add: schema::PickupPointDeliveryOption {
                    cost: None,
                    pickup_point: pickup_point.clone(),
                    metafields: Some(vec![]),
                }
            }
        })
        .collect()
}
```

Run Target Function Code (JavaScript):

```javascript
export function run(input) {
  const { fetchResult } = input;
  const status = fetchResult?.status;
  const body = fetchResult?.body;

  let operations = [];

  if (status === 200 && body) {
    const { deliveryPoints } = JSON.parse(body);
    operations = buildPickupPointDeliveryOptionOperations(deliveryPoints);
  }

  return { operations };
}

function buildPickupPointDeliveryOptionOperations(deliveryPoints) {
  return deliveryPoints.map((deliveryPoint) => ({
    add: {
      cost: null,
      metafields: [],
      pickupPoint: deliveryPoint,
    },
  }));
}
```

Performance: fetch — Rust 26654 / JS 277271; run — Rust 345811 / JS 1588336 instructions.

Run Target Output JSON (Rust) — each operation contains a full `add.pickupPoint` with `address`, all seven days of `businessHours`, `externalId`, `name`, and `provider`. Example first operation:

```json
{
  "operations": [
    {
      "add": {
        "cost": null,
        "metafields": [],
        "pickupPoint": {
          "address": {
            "address1": "620 King St W",
            "address2": null,
            "city": "Toronto",
            "country": "Canada",
            "countryCode": "CA",
            "latitude": 43.644664618786685,
            "longitude": -79.40066267417106,
            "phone": null,
            "province": "Ontario",
            "provinceCode": "ON",
            "zip": "M5V 1M6"
          },
          "businessHours": [
            { "day": "MONDAY",    "periods": [ { "closingTime": "21:00:00", "openingTime": "09:00:00" } ] },
            { "day": "TUESDAY",   "periods": [ { "closingTime": "21:00:00", "openingTime": "09:00:00" } ] },
            { "day": "WEDNESDAY", "periods": [ { "closingTime": "21:00:00", "openingTime": "09:00:00" } ] },
            { "day": "THURSDAY",  "periods": [ { "closingTime": "21:00:00", "openingTime": "09:00:00" } ] },
            { "day": "FRIDAY",    "periods": [ { "closingTime": "21:00:00", "openingTime": "09:00:00" } ] },
            { "day": "SATURDAY",  "periods": [ { "closingTime": "18:00:00", "openingTime": "10:00:00" } ] },
            { "day": "SUNDAY",    "periods": [] }
          ],
          "externalId": "001",
          "name": "Toronto Store",
          "provider": {
            "logoUrl": "https://cdn.shopify.com/s/files/1/0628/3830/9033/files/shopify_icon_146101.png?v=1706120545",
            "name": "Shopify pickup point function demo"
          }
        }
      }
    }
  ]
}
```

---

## Pagine aggiuntive

The following per-function deep type/GraphQL reference and tutorial pages are referenced by the captured pages but not reproduced verbatim here (the per-type schema overviews above cover their substantive content). Capture on demand:

* Network access GraphQL reference — https://shopify.dev/docs/apps/build/functions/network-access/graphql
* Discount network access guide — https://shopify.dev/docs/apps/build/discounts/network-access
* Legacy Order Discounts reference — https://shopify.dev/docs/api/functions/reference/order-discounts
* Legacy Product Discounts reference — https://shopify.dev/docs/api/functions/reference/product-discounts
* Tutorials linked from the guides: build-product-discount-function, add-customized-bundle-function, create-server-side-validation-function, delivery-options/build-function, payments, build-fulfillment-constraints-function, location-rules/build-location-rule-function, build-local-pickup-options-function, generate-pickup-points, create-local-pickup-charges-function.
* Localization practices for Shopify Functions — https://shopify.dev/docs/apps/build/functions/localization-practices-shopify-functions
