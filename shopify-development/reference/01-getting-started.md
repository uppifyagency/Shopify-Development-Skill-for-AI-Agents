# 1. Getting Started

This chapter covers how to begin building Shopify themes: the section overview of the themes platform, and the two quick-start tutorials for creating a brand-new theme from Shopify's Skeleton reference theme and for customizing an existing merchant theme.

## Indice del capitolo

- [Overview — Build Shopify themes](#overview--build-shopify-themes)
- [Quick start: Build a new theme](#quick-start-build-a-new-theme)
- [Quick start: Customize a theme](#quick-start-customize-a-theme)

---

## Overview — Build Shopify themes

> Fonte: https://shopify.dev/docs/storefronts/themes

### Build Shopify themes

Build fast, flexible themes at scale using Liquid, Shopify's theme templating language, along with HTML, CSS, JavaScript, and JSON.

#### Build a new theme

Create a new theme based on Shopify's Skeleton theme.

#### Customize a theme

Update the look and feel of an existing theme to tailor it to a merchant's unique needs.

#### Key concepts

Shopify themes are a package of template files, building blocks, and supporting assets. Use these building blocks to create modular, customizable themes.

[Learn about key theme concepts](https://shopify.dev/docs/storefronts/themes/architecture)

#### Liquid

The Liquid templating language is the backbone of Shopify themes, and is used to load dynamic content on storefronts. Extend Liquid objects to store and present custom data using metafields.

[View the Liquid reference](https://shopify.dev/docs/api/liquid)

#### Best practices

To optimize your theme development experience, Shopify has established best practices for theme development and toolchain setup.

[Follow Best Practices](https://shopify.dev/docs/storefronts/themes/best-practices)

#### Ajax API for themes

Learn about the endpoints that Shopify provides to interact with your theme.

[Explore the Ajax API](https://shopify.dev/docs/api/ajax)

#### Section rendering API

Review the AJAX API that lets you update page content without reloading an entire page.

[Explore the Section Rendering API](https://shopify.dev/docs/api/ajax/section-rendering)

#### Liquid cheat sheet

Consult this interactive reference guide to the Liquid template language.

[Open the Liquid cheat sheet](https://www.shopify.ca/partners/shopify-cheat-sheet)

#### Liquid code examples

Build Shopify themes faster with this library of ready-to-use Liquid components.

[Browse Liquid code examples](https://shopify.github.io/liquid-code-examples/)

#### Migrate your theme to Online Store 2.0

Make your theme more flexible and easier to maintain by migrating it to the new architecture. Using Online Store 2.0, you can add and remove sections from any template, and prepare your theme for app blocks.

[Learn more about Online Store 2.0](https://shopify.dev/docs/storefronts/themes/os20)

#### Build fast with Shopify tools

Shopify provides a range of tools to help you to collaborate and build themes faster.

[Learn more about Shopify's tools for themes](https://shopify.dev/docs/storefronts/themes/tools)

##### Shopify CLI

Initialize, preview, test and share themes in your local development environment.

[Learn about Shopify CLI](https://shopify.dev/docs/storefronts/themes/tools/cli)

##### Shopify GitHub integrations

Integrate GitHub into your Shopify admin to manage your theme code.

[Learn about the Shopify GitHub integration](https://shopify.dev/docs/storefronts/themes/tools/github)

##### Theme Check

Detect errors and enforce best practices as you code, or as part of your CI pipeline.

[Learn about Theme Check](https://shopify.dev/docs/storefronts/themes/tools/theme-check)

#### Shopify Theme Store

Design beautiful, purpose-built themes for different markets, and sell them to millions of merchants on the Shopify Theme Store.

[Learn how to start selling](https://shopify.dev/docs/storefronts/themes/store)

---

## Quick start: Build a new theme

> Fonte: https://shopify.dev/docs/storefronts/themes/getting-started/create

### Create a theme

You're ready to create a new theme. You might be asking yourself: How can I quickly set up my development environment and start coding?

In this tutorial, you'll use Shopify CLI and the Skeleton reference theme to create a new theme and upload it to Shopify.

#### What you'll learn

After you've finished this tutorial, you'll have accomplished the following:

- Set up your local development environment
- Cloned the [Skeleton theme](https://github.com/shopify/skeleton-theme)
- Previewed changes made to your local code
- Pushed theme code to your Shopify store and published your theme

#### Requirements

- You've installed [Shopify CLI](https://shopify.dev/docs/api/shopify-cli).
- You've created a [dev store](https://shopify.dev/docs/storefronts/themes/tools/development-stores) (recommended for this tutorial).
- The URL of the store that you want to work on, such as `example.myshopify.com`.
- You have a [collaborator account](https://shopify.dev/docs/storefronts/themes/tools/collaborator-accounts) or [staff account](https://help.shopify.com/manual/your-account/staff-accounts) with the **Manage themes** permission or **Themes** permission for the store that you want to work on, or you're the store owner.

> **Caution:**
>
> To use a dev store with [Shopify CLI](https://shopify.dev/docs/apps/build/cli-for-apps), you need to be the store owner, or have a [staff account](https://help.shopify.com/manual/your-account/staff-accounts) on the store. If you create a dev store, then you're assigned as the store owner. Other staff members must be added to the store.

#### Step 1: Initialize a new theme

Use [`shopify theme init`](https://shopify.dev/docs/api/shopify-cli/theme/theme-init) to clone the Skeleton theme Git repository to your local machine.

The [Skeleton theme](https://github.com/shopify/skeleton-theme) is a minimal, carefully structured Shopify theme designed to help you quickly get started. Designed with modularity, maintainability, and Shopify's best practices in mind.

1. In a terminal, navigate to the working directory where you want to build your theme.

2. Enter the following command:

   ```terminal
   shopify theme init
   ```

3. You're prompted to enter a name for your theme, such as `my-new-theme`. The theme is cloned into a folder with the same name.

4. After the theme is cloned, navigate to the folder:

   ```terminal
   cd "my-new-theme"
   ```

> **Tip:**
>
> You can also use the `init` command to clone a theme from [another Git repository](https://shopify.dev/docs/api/shopify-cli/theme/theme-init).

#### Step 2: Start a local development server

After you initialize your theme, you can run [`shopify theme dev`](https://shopify.dev/docs/api/shopify-cli/theme/theme-dev) to interact with the theme in a browser. Shopify CLI uploads the theme as a [development theme](https://shopify.dev/docs/storefronts/themes/tools/cli#development-themes) on the store.

The command returns a URL that hot reloads local changes to CSS and sections, allowing you to preview changes in real time using the store's data. This preview is only available in Google Chrome.

The first time you run the `dev` command, you're prompted to log in to Shopify.

1. To serve your theme, run the following command, where `--store` represents the name of the store that you want to use to preview your theme:

   ```terminal
   shopify theme dev --store my-store
   ```

   You need to pass the `--store` flag the first time you preview your theme. The store that you specify is used for future commands until you pass the `--store` flag with a new value. To check which store you're connected to, run `shopify theme info`.

2. In Google Chrome, navigate to `http://127.0.0.1:9292` to open the theme preview.

> **Tip:**
>
> You can also use the `dev` to generate a [preview link](https://help.shopify.com/manual/online-store/themes/adding-themes#share-a-theme-preview-with-others) and a link to the [theme editor](https://shopify.dev/docs/storefronts/themes/tools/online-editor) for the development theme.

The following image shows a development server being started using `dev`:

![An image showing how to start a local development server.](https://shopify.dev/assets/assets/images/themes/getting-started/theme-dev-CIj782XX.png)

#### Step 3: Upload your theme to a store

If you want to share a permanent link to your theme, update the code of an existing theme, or prepare for your theme to be published, then you need to push your theme code to Shopify using the [`theme push`](https://shopify.dev/docs/api/shopify-cli/theme/theme-push) command.

The first time you push your theme code, you might want to upload the theme to your theme library as a new, unpublished theme. You can do this by running the command with the `--unpublished` flag. When you run the command using this flag, you're prompted to provide a name for the theme that appears in the theme library.

```terminal
shopify theme push --unpublished
```

After the theme is created, you can update your theme code by running the `push` command without any flags:

```terminal
shopify theme push
```

#### Step 4: Publish your theme

If you want to make your theme live on your store, then you can publish it using the [`theme publish`](https://shopify.dev/docs/api/shopify-cli/theme/theme-publish) command. Before you run this command, make sure that you've pushed all of your local changes to Shopify using the [`theme push`](https://shopify.dev/docs/api/shopify-cli/theme/theme-push) command.

1. Enter the following command:

   ```terminal
   shopify theme publish
   ```

2. Select the theme that you want to publish from the list.

3. Select `Yes` to confirm that you want to publish the specified theme.

The theme is published and is now the active theme for the store.

#### Next steps

Creating your first theme with our tools is only the first step in building your theme. Consider the following next steps:

- [Learn about theme architecture](https://shopify.dev/docs/storefronts/themes/architecture) — Learn more about the structure of a theme, and the role of each file and folder.
- [Review best practices](https://shopify.dev/docs/storefronts/themes/best-practices) — Build your theme with a set of principles to use themes to their full potential, and to create great ecommerce experiences.
- [Build as a team](https://shopify.dev/docs/storefronts/themes/tools) — Take advantage of developer tools to build effectively as a team.
- [Implement Shopify features](https://shopify.dev/docs/storefronts/themes/theme-features) — Enable Shopify features or add functionality to your theme.

---

## Quick start: Customize a theme

> Fonte: https://shopify.dev/docs/storefronts/themes/getting-started/customize

### Customize a merchant theme

As a theme developer, you can customize themes for Shopify merchants. These customizations might range from small tweaks to complete redesigns. Shopify Partners can offer theme customization services through the [Shopify Partner Directory](https://help.shopify.com/partners/directory).

In this tutorial, you'll use Shopify CLI to customize a merchant's theme and then share your progress with them.

If you're customizing a theme for a client, then you should also [review our best practices for working with merchants](https://shopify.dev/docs/storefronts/themes/best-practices/merchant-stores).

> **Caution:**
>
> This tutorial describes customizing themes that don't use the [Shopify GitHub integration](https://shopify.dev/docs/storefronts/themes/tools/github). If your merchant uses the Shopify GitHub integration to manage their theme code, then you can request access to the repository from them, or you can push changes to the theme that's connected to a branch of the repository using Shopify CLI.

#### What you'll learn

After you've finished this tutorial, you'll have accomplished the following:

- Gained access to the merchant's store
- Set up your local development environment
- Downloaded a copy of the merchant's theme
- Made a change and previewed it
- Shared your changes with the merchant
- Published your changes

#### Requirements

- You've installed [Shopify CLI](https://shopify.dev/docs/api/shopify-cli)
- The URL of the store that you want to work on, such as `example.myshopify.com`.

#### Step 1: Request access to the merchant's store

To work on a merchant's theme, you should request access to their store. Working on a theme in a merchant's store lets you test it with the merchant's products and other resources.

If you haven't done so already, you should request [a collaborator account](https://shopify.dev/docs/storefronts/themes/tools/collaborator-accounts) with the **Manage themes** permission for the store. Collaborator accounts give you access to only the sections of a store that a merchant wants you to access, and don't count toward a store's [staff limit](https://help.shopify.com/manual/your-account/staff-accounts).

> **Note:**
>
> You can also access themes using other accounts and credentials. [Learn more](https://shopify.dev/docs/storefronts/themes/tools/cli#authenticating-and-accessing-stores).

#### Step 2: Download the merchant's theme code

If the merchant doesn't have a [GitHub repository for their theme](https://shopify.dev/docs/storefronts/themes/tools/github), then you need to download a copy of the theme code to work on it locally.

1. Run the following command to retrieve a list of all of the themes in the store. You can optionally specify the local path where the theme should be stored using the `--path` flag.

   ```terminal
   shopify theme pull --store my-store
   ```

2. Select a theme from the list. Its contents are downloaded to the current folder or the specified folder.

   > **Tip:**
   >
   > If you haven't done so already, you're prompted to log in to Shopify when you run the `pull` command. Make sure that you log in using the account that was granted access to the store. If you're already logged in with an account that doesn't have appropriate access, then you can log out using `shopify auth logout`.

#### Step 3: Make a customization

After you've downloaded the merchant's theme, you can make any necessary changes to the theme code. For example, you can add support for multiple currencies and languages in the merchant's theme using our [localization](https://shopify.dev/docs/storefronts/themes/markets/multiple-currencies-languages) tutorial, or you can make an adjustment to the theme's CSS to change its appearance.

Refer to [Next steps](#next-steps) to explore additional feature tutorials.

#### Step 4: Preview your changes

After you make a change to the theme, you can run [`shopify theme dev`](https://shopify.dev/docs/api/shopify-cli/theme/theme-dev) to interact with the theme in a browser. Shopify CLI uploads the theme as a [development theme](https://shopify.dev/docs/storefronts/themes/tools/cli#development-themes) on the store that you're connected to.

The command returns a URL that hot reloads local changes to CSS and sections, allowing you to preview changes in real time using the store's data. This preview is only available in Google Chrome.

1. In a terminal, navigate to your working directory.

2. Serve your theme by using the following command:

   ```terminal
   shopify theme dev
   ```

3. In Google Chrome, navigate to `http://127.0.0.1:9292` to open the theme preview.

You can also use the `dev` command to generate a [preview link](https://help.shopify.com/manual/online-store/themes/adding-themes#share-a-theme-preview-with-others) and a link to the [theme editor](https://shopify.dev/docs/storefronts/themes/tools/online-editor) for the development theme.

The development theme is destroyed when you run `shopify auth logout`. If you need to share your progress with the merchant, then proceed to the next step.

#### Step 5: Share your changes

To share your changes with the merchant, you need to upload your changes to the theme to the merchant's store. You're prompted to select the theme that you want to update. This command returns a link to the [editor](https://shopify.dev/docs/storefronts/themes/tools/online-editor) for the theme in the Shopify admin and a [preview link](https://help.shopify.com/manual/online-store/themes/adding-themes#share-a-theme-preview-with-others), both of which you can share with the merchant.

```terminal
shopify theme push
```

> **Tip:**
>
> If you don't want to update an existing theme in the store with your changes, then you can upload your theme to the theme library as a new, unpublished theme using the [`--unpublished`](https://shopify.dev/docs/api/shopify-cli/theme/theme-push-flags) flag.

#### Step 6: Publish the updated theme

After the merchant approves the changes, you can publish the theme to make it live in the merchant's store. If you haven't yet pushed your changes to the store, then you need to do so before you publish the theme.

1. Enter the following command:

   ```terminal
   shopify theme publish
   ```

2. Select the theme that you want to publish from the list.

3. Select `Yes` to confirm that you want to publish the specified theme.

The theme is published and is now the active theme for the store.

#### Next steps

A theme determines the way that a Shopify [online store](https://help.shopify.com/manual/online-store) looks, feels, and functions for merchants and their customers.

Shopify themes are built using Shopify's theme templating language, [Liquid](https://shopify.dev/docs/api/liquid), along with HTML, CSS, JavaScript, and JSON. Using these languages, developers can create any look and feel that their clients want. Shopify provides several tools and best practices to accelerate the development process.

As a developer, you can build a custom theme for a specific merchant, customize a theme to meet a merchant's needs, or build a theme to sell in the Shopify Theme Store. You can also build apps that extend the functionality of a theme.

- [Learn about theme architecture](https://shopify.dev/docs/storefronts/themes/architecture) — Learn more about the structure of a theme, and the role of each file and folder.
- [Review best practices](https://shopify.dev/docs/storefronts/themes/best-practices) — Build your theme with a set of principles to use themes to their full potential, and to create great ecommerce experiences.
- [Build as a team](https://shopify.dev/docs/storefronts/themes/tools) — Take advantage of our developer tools to build effectively as a team.
- [Implement Shopify features](https://shopify.dev/docs/storefronts/themes/theme-features) — Enable Shopify features or add functionality to your theme.
