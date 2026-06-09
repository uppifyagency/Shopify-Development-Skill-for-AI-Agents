# 4. Developer Tools

Shopify provides a range of tools to help you build, test, share, and maintain Shopify themes faster. This chapter is a faithful extraction of the "Developer tools" section of the Shopify Themes documentation. It covers the command-line interface (Shopify CLI), the GitHub integration for version control, the VS Code extension and Liquid Language Server, the Prettier plugin, LiquidDoc, Theme Check (linting), the web-based theme and code editors, access tools (Theme Access app, dev stores, collaborator accounts), and performance tooling (Theme Inspector and Lighthouse CI).

Each section below preserves the original page content 1:1 and includes a `> Fonte:` line pointing to the source URL on shopify.dev.

---

## Table of contents

1. [Tools for building Shopify themes (Overview)](#tools-for-building-shopify-themes-overview)
2. [Shopify CLI for themes](#shopify-cli-for-themes)
   - [Theme environments for Shopify CLI](#theme-environments-for-shopify-cli)
   - [Use Shopify CLI in a CI/CD pipeline](#use-shopify-cli-in-a-cicd-pipeline)
   - [Migrate to Shopify CLI 3.0+](#migrate-to-shopify-cli-30)
   - [Shopify Liquid Language Server](#shopify-liquid-language-server)
3. [Shopify GitHub integration for themes](#shopify-github-integration-for-themes)
4. [Shopify Liquid VS Code extension](#shopify-liquid-vs-code-extension)
5. [Shopify Liquid Prettier Plugin](#shopify-liquid-prettier-plugin)
6. [LiquidDoc](#liquiddoc)
7. [Theme Check](#theme-check)
   - [Theme Check configuration](#theme-check-configuration)
   - [Theme Check commands](#theme-check-commands)
   - [Checks reference](#checks-reference)
8. [The theme editor](#the-theme-editor)
9. [The code editor](#the-code-editor)
10. [Manage theme access (Theme Access app)](#manage-theme-access-theme-access-app)
11. [Dev stores](#dev-stores)
    - [Generated test data](#generated-test-data)
12. [Collaborator accounts](#collaborator-accounts)
13. [Shopify Theme Inspector for Chrome](#shopify-theme-inspector-for-chrome)
    - [Identify Liquid render issues using Shopify Theme Inspector](#identify-liquid-render-issues-using-shopify-theme-inspector)
14. [Shopify Lighthouse CI GitHub Action](#shopify-lighthouse-ci-github-action)

---

## Tools for building Shopify themes (Overview)

> Fonte: https://shopify.dev/docs/storefronts/themes/tools

# Tools for building Shopify themes

Shopify provides a range of tools to help you build Shopify themes faster.

## Tools for building and editing themes

The following tools help you quickly scaffold, test, share, and develop Shopify themes.

**Shopify CLI** - A powerful command-line tool for building Shopify themes, and exploring Liquid code in a REPL interface.

**Shopify Liquid VS Code extension** - Use the Shopify Liquid Visual Studio Code extension to improve your local development experience.

### Legacy tools

**Shopify CLI 2.x** - The previous major version of Shopify CLI.

**Theme Kit** - A legacy command-line tool for building Shopify themes.

## Web-based editors for themes

The following tools can be used by merchants and developers to customize themes in the Shopify admin. As a developer, you should account for these tools when developing your theme to ensure the best merchant experience.

**Admin theme editor** - An interactive editor that lets merchants customize their online store and theme.

**Admin code editor** - A code editor built into the Shopify admin.

## Access tools

The following tools allow you to access Shopify infrastructure for testing, and help you to safely access merchant stores.

**Development stores** - A free Shopify account that you can use to build and test themes.

**Collaborator accounts** - An account that lets you access and manage a merchant's store through the Partner Dashboard.

**Theme Access app** - An app that grants programmatic access to themes in a particular store. Used with Shopify CLI and Theme Kit.

## Version control tools

The Shopify GitHub integration helps you to track and push changes to and from a theme in a Shopify store by using Git.

**Shopify GitHub integration** - Manage your Shopify theme code by using Git version control.

## Testing tools

The following tools help you to optimize and detect errors in your theme code.

**Theme Check** - A command-line based linter for themes. Also offered as part of the Shopify Liquid Visual Studio Code extension.

**Liquid Prettier Plugin** - Use the Liquid Prettier Plugin to format your Liquid and HTML in a consistent style.

**Shopify Theme Inspector for Chrome** - Profile and debug your Liquid template performance with this extension for Chrome Developer Tools.

**Lighthouse CI** - Ensure that your theme is performant by using the Lighthouse CI GitHub Action.

**LiquidDoc** - Enable enhanced tooling features for Liquid snippets.

## Tools for learning Liquid

The following tools help you to learn and write Liquid.

**Imagery** - Learn how to write image tags, and understand how images are dynamically transformed with Imagery.

---

## Shopify CLI for themes

> Fonte: https://shopify.dev/docs/storefronts/themes/tools/cli

# Shopify CLI for themes

Shopify CLI is a command-line interface tool that helps you build Shopify apps and themes. It quickly generates Shopify apps, themes, and custom storefronts. You can also use it to automate many common development tasks.

This documentation explains how to use Shopify CLI for theme development. To learn how to use Shopify CLI for other tasks, refer to the following documentation:

* [Shopify CLI for apps](https://shopify.dev/docs/apps/build/cli-for-apps)
* [Shopify CLI for Hydrogen storefronts](https://shopify.dev/docs/api/shopify-cli/hydrogen)

**Tip:** You can use Shopify CLI together with the [Shopify GitHub integration](https://shopify.dev/docs/storefronts/themes/tools/github) to add version control to themes that you're developing.

## Features

Shopify CLI accelerates your theme development process with the following features:

* Safely preview, test, and share changes to themes using [development themes](https://shopify.dev/docs/storefronts/themes/tools/cli#development-themes)
* Hot reload CSS and section changes, or automatically refresh a page on file change, when previewing a theme
* Initialize a new theme
* Push and publish themes from the command line
* Work on multiple themes using [environments](#environments)
* Run [Theme Check](https://shopify.dev/docs/storefronts/themes/tools/theme-check/configuration) on your theme

### Development themes

Development themes are temporary, hidden themes that are connected to the Shopify store that you're using for development. When you connect your theme to a store as a development theme, you can use that store's data for local testing.

You can create a development theme using the [`shopify theme dev`](https://shopify.dev/docs/api/shopify-cli/theme/theme-dev) command.

You can use development themes on a Shopify store or a [development store](https://shopify.dev/docs/storefronts/themes/tools/development-stores). Development themes don't count toward your theme limit, and are deleted from the store after seven days of inactivity.

Your development theme is deleted when you run `shopify auth logout`. If you want a preview link for the theme that can be accessed after you log out, then you should [push](https://shopify.dev/docs/api/shopify-cli/theme/theme-push) your development theme to an unpublished theme on your store.

Your development theme can be used to perform the following tasks:

* View changes in real time to a theme that you're developing locally
* Customize and interact with the theme using the Shopify admin [theme editor](https://shopify.dev/docs/storefronts/themes/tools/online-editor)
* Share a password-protected [preview](https://help.shopify.com/manual/online-store/themes/adding-themes#share-a-theme-preview-with-others) of the theme with other developers

### Environments

Many command configurations, such as the theme and store to be used with the command, are passed using flags. To avoid passing multiple flags with each command, and to easily switch projects or contexts, you can use environments. Environments are sets of command configurations that can be referenced by name using a single `--environment` flag.

You might want to use environments in the following cases:

* You need to switch between development stores frequently.
* You access multiple stores using [Theme Access](https://shopify.dev/docs/storefronts/themes/tools/theme-access) passwords.
* You want to deploy your project to development, staging, and production instances of your theme.

[Learn how to configure and use environments](https://shopify.dev/docs/storefronts/themes/tools/cli/environments).

## Installation

To learn how to install Shopify CLI on Windows, macOS, or Linux, refer to [Install Shopify CLI](https://shopify.dev/docs/api/shopify-cli).

## Getting started

Refer to the following tutorials for details about creating or working on a Shopify theme using Shopify CLI:

[Start building a theme](https://shopify.dev/docs/storefronts/themes/getting-started/create)

Learn how to set up your theme development environment and create a new theme.

[Customize an existing theme](https://shopify.dev/docs/storefronts/themes/getting-started/customize)

Learn how to set up your development environment to work on a theme in a Shopify store.

## Command reference

Refer to the [Shopify CLI theme command reference](https://shopify.dev/docs/api/shopify-cli/theme) to explore the commands available to build themes with Shopify CLI.

## Authenticating and accessing stores

As a theme developer, you might want to use a Shopify store to test your theme, or to share your theme with stakeholders. You also might need to work on multiple stores, or use a different set of credentials to authenticate with a particular store. Learn about the authentication methods that you can use to work on stores using Shopify CLI, and how to switch between accounts and stores.

### Authentication

You can use the following authentication methods to work on a theme in a Shopify store using Shopify CLI:

* [Log in with a Shopify account](#log-in-with-a-shopify-account)
* [Provide a Theme Access password](#theme-access-password)
* [Provide a custom app access token](#custom-app-access-token)

#### Log in with a Shopify account

You can use the following types of Shopify accounts to access the store you want to work on:

* A [collaborator account](https://shopify.dev/docs/storefronts/themes/tools/collaborator-accounts) with the **Manage themes** permission
* A [staff account](https://help.shopify.com/manual/your-account/staff-accounts) with the **Themes** permission
* The store owner account

To authenticate with a Shopify account, run a command that requires store access. You'll be prompted to log in.

**Caution:** To use a dev store with [Shopify CLI](https://shopify.dev/docs/apps/build/cli-for-apps), you need to be the store owner, or have a [staff account](https://help.shopify.com/manual/your-account/staff-accounts) on the store. If you create a dev store, then you're assigned as the store owner. Other staff members must be added to the store.

##### Switching between accounts

If you need to switch between accounts, then log out of the current account using the following command:

```terminal
shopify auth logout
```

The next time you enter a command that requires authentication, you'll be prompted to log in, and can enter a new set of credentials.

#### Theme Access password

You can use a Theme Access password to authenticate with the store that you want to work on. Theme Access passwords are generated for a store using the [Theme Access app](https://shopify.dev/docs/storefronts/themes/tools/theme-access).

To use a Theme Access password, pass the `--password` flag with each command that you want to run against the store. If you run a command without the `--password` flag, then Shopify CLI attempts to use your Shopify account credentials to run the command.

#### Custom app access token

You can use a [custom app access token](https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/generate-app-access-tokens-admin) to authenticate with the store that you want to work on.

To authenticate using an access token, pass the `--password` flag with each command that you want to run against the store. If you run a command without the `--password` flag, then Shopify CLI attempts to use your Shopify account credentials to run the command.

Your custom app needs to have the `read_themes` and `write_themes` [API access scopes](https://shopify.dev/docs/api/usage/access-scopes). To enable hot reloading, you also need to add the `unauthenticated_read_content` access scope for Storefront API integration, and pass the tokens as [environment variables](https://shopify.dev/docs/storefronts/themes/tools/cli/environments) instead of using the `--password` flag.

### Connecting to a store

The first time you enter a command that requires you to interact with a Shopify store, pass the `--store` flag with the command and specify the store that you want to interact with:

```terminal
shopify theme dev --store my-store
```

The store that you specify is used for future commands until a new store is specified.

If you want to change the store that you're interacting with, pass the `--store` flag with your command, specifying the new store that you want to interact with.

To check which store you're using, run `shopify theme info`:

```terminal
shopify theme info
```

Output:

```terminal
THEME CONFIGURATION
-----------------------
Store   my-store.myshopify.com
...
```

## Directory structure

You can run certain theme commands, such as `shopify theme dev`, only if the directory you're using matches the default Shopify theme [directory structure](https://shopify.dev/docs/storefronts/themes/architecture#directory-structure-and-component-types). This structure represents a buildless theme, or a theme that has already gone through any necessary [file transformations](https://shopify.dev/docs/storefronts/themes/best-practices/file-transformation). If you use build tools to generate theme files, then you might need to run commands from the directory where the generated files are stored.

The default Shopify theme directory structure is as follows:

```text
└── project
    ├── assets
    ├── blocks
    ├── config
    ├── layout
    ├── locales
    ├── sections
    ├── snippets
    └── templates
        └── customers
```

## Excluding files from Shopify CLI

If you have files in the same repository as your theme that you don't want to interact with using Shopify CLI, then you can add them to a `.shopifyignore` at the root of the theme.

`.shopifyignore` accepts references to files in the following formats:

* Simple file names: `templates/product.temp.json`
* Wildcards: `config/*_secret.json`, `*.jpg`
* Regular expressions: `/\.(txt|gif|bat)$/`

You can also exclude specific files or patterns during a `push` or `pull` using the `--ignore` flag. If files are excluded using `.shopifyignore`, then both the contents of `.shopifyignore` and the `--ignore` flag are respected.

## Using Shopify CLI for continuous integration

If you have a theme that you want to work with programmatically, then you can integrate Shopify CLI into your CI/CD pipeline to perform actions like pushing, pulling, and publishing a theme.

[Learn more about running Shopify CLI in a CI/CD pipeline](https://shopify.dev/docs/storefronts/themes/tools/cli/ci-cd).

## Upgrade Shopify CLI

To upgrade Shopify CLI to the latest version, run the [`upgrade`](https://shopify.dev/docs/api/shopify-cli#upgrade) command from your theme directory:

```terminal
shopify upgrade
```

To check your CLI version, run the [`version`](https://shopify.dev/docs/api/shopify-cli/common-commands/version) command from your theme directory:

```terminal
shopify version
```

## Migrate to Shopify CLI 3.0+

In October 2022, support for themes was added to Shopify CLI 3.0. Shopify CLI 3.0+ provides a streamlined authentication and store management experience.

To learn about the differences between Shopify CLI 2.x and 3.0+, how to upgrade to Shopify CLI 3.0+, or how to use both Shopify CLI 2.x and 3.0+ on the same machine, refer to [Migrate to Shopify CLI 3.0+](https://shopify.dev/docs/storefronts/themes/tools/cli/migrate).

## Usage reporting

Anonymous usage statistics are collected by default. To opt out, you can use the environment variable `SHOPIFY_CLI_NO_ANALYTICS=1`.

## Contributing to Shopify CLI

Shopify CLI is open source. [Learn how to contribute](https://github.com/Shopify/cli/wiki/Contributors:-Introduction) to our GitHub repository.

## Where to get help

* **[Open a GitHub issue](https://github.com/shopify/cli/issues)** - To report bugs or request new features, open an issue in the Shopify CLI repository.
* **[.dev Community](https://community.shopify.dev/)** - Visit our forums to connect with the community and learn more about Shopify CLI development.

---

### Theme environments for Shopify CLI

> Fonte: https://shopify.dev/docs/storefronts/themes/tools/cli/environments

# Theme environments for Shopify CLI

Multiple command configurations, such as the theme and store used with commands, are typically passed using flags. To streamline this process and easily switch between projects or contexts, you can use environments. Environments are sets of command configurations that you reference by name using a single `--environment` flag.

## When to Use Environments

Consider using environments in these scenarios:

* You need to switch between development stores frequently.
* You access multiple stores using Theme Access passwords.
* You want to deploy your project to development, staging, and production instances of your theme.

Environments are configured per theme repository using a `shopify.theme.toml` configuration file.

## Configure environments

To configure an environment for your local theme project:

1. Create a file called `shopify.theme.toml` at the root of the project.
2. For each environment, add a table heading using the syntax `[environments.YOUR_ENVIRONMENT_NAME]`.
3. Below the heading, add key-value pairs for the flags and flag values for that environment.

You can set environment-specific values for any flag except `environment`, `path`, and `verbose`, which are ignored.

For Boolean flags, specify `true` as the value.

### Example shopify.theme.toml

```toml
[environments.env1]
theme = "123456789012"
store = "my-store"
password  = "shptka_123456"
ignore = "sections/header.liquid"


[environments.env2]
store = "another-store"
path = "./dist"
ignore = ["sections/announcement-bar.liquid", "sections/header.liquid"]
output = "json"
live = true
allow-live = true
```

**Caution:** Some shared flags like `force` have different meanings depending on the command. Including these flags in your environment might have unintended consequences. For example, `force` on the `delete` command will delete a theme without confirmation.

## Use an environment

To use an environment, pass the environment name with your command:

```terminal
shopify theme dev --environment env1

# using the flag alias
shopify theme dev -e env1
```

The CLI displays which flag values are applied:

```terminal
shopify theme dev --environment env1

╭─ info ─────────────────────────────────────────────────╮
│                                                        │
│  Using applicable flags from env1 environment:         │
│                                                        │
│    • store: my-store                                   │
│    • password: *******456                              │
│    • ignore = "sections/header.liquid"                 │
│                                                        │
╰────────────────────────────────────────────────────────╯
```

### Set a default environment

Create an environment named `[environments.default]` to avoid specifying the `--environment` flag with every theme command. Theme commands use this environment by default.

You can override the default by specifying an `--environment` flag.

### How environment flags are applied

Environment flags follow these precedence rules:

* Flags included in an environment but not accepted by the command are ignored.

* Incorrect data types or mutually exclusive flags in an environment throw an error.

* Flag values are applied in this order of precedence:

  1. Command-level flags
  2. Environment variables
  3. Environment settings from `shopify.theme.toml`

If you pass a flag at the command level, that value overrides the environment flag value:

```terminal
shopify theme dev --environment env1 --store my-new-store --password shptka_102938

╭─ info ─────────────────────────────────────────────────╮
│                                                        │
│  Using applicable flags from env1 environment:         │
│                                                        │
│    • ignore = "sections/header.liquid"                 │
│                                                        │
╰────────────────────────────────────────────────────────╯
```

## Use multiple environments

These theme commands support multiple environments:

* `check`
* `delete`
* `info`
* `list`
* `publish`
* `pull`
* `push`
* `rename`
* `share`

To use multiple environments, pass the environment names with your command:

```terminal
shopify theme delete --environment env1 --environment env2 --development
```

**Caution:** When using multiple environments, the CLI doesn't prompt for missing information. Include all required flags in the command or your `shopify.theme.toml` file. If a required flag is missing, the environment is skipped and a warning is shown.

If the command doesn't accept a `--force` flag, it runs immediately. Otherwise, a confirmation prompt appears:

```terminal
?  Run delete in the following environments?

   ┃  Environment
   ┃  • env1 store: my-store.myshopify.com, password, development: true
   ┃  • env2 store: another-store.myshopify.com, password, development: true

>  (y) Yes, proceed
   (n) Cancel
```

---

### Use Shopify CLI in a CI/CD pipeline

> Fonte: https://shopify.dev/docs/storefronts/themes/tools/cli/ci-cd

# Use Shopify CLI in a CI/CD pipeline

If you have a theme that you want to work with programmatically, then you can integrate Shopify CLI into your CI/CD pipeline to perform actions like pushing, pulling, and publishing a theme.

***

## What you'll learn

In this tutorial, you'll learn how to set up your CI/CD pipeline to work with themes programmatically. To do so, you'll gather the credentials necessary to run the CLI commands, and then add a step to your CI/CD pipeline that installs Shopify CLI and runs CLI commands.

***

## Requirements

* [Shopify CLI 3.20 or higher](https://shopify.dev/docs/storefronts/themes/tools/cli/cli-2/commands)

**Tip:** [Learn how to check your Shopify CLI version](https://shopify.dev/docs/storefronts/themes/tools/cli/cli-2/commands#version).

***

## Step 1: Get a Theme Access password for the store

For each store that you want to interact with programmatically using Shopify CLI, you need to get a Theme Access password. These are generated using the [Theme Access](https://apps.shopify.com/theme-access) app.

To learn about the requirements for installing and using the Theme Access app, and instructions on how to generate a new password, refer to [Manage theme access](https://shopify.dev/docs/storefronts/themes/tools/theme-access).

***

## Step 2: Integrate Shopify CLI into your pipeline

After you get a Theme Access password for the store, you can integrate Shopify CLI into your continuous deployment pipeline using your CI/CD provider.

The CD pipeline step should install Shopify CLI and all of its [dependencies](https://shopify.dev/docs/api/shopify-cli#requirements).

To run Shopify CLI theme commands programmatically using your CD pipeline step, include the following:

* Environment variables (or equivalent flags):

  | Name | Required? | Value |
  | - | - | - |
  | `SHOPIFY_CLI_THEME_TOKEN` | Yes | The [Theme Access password](#step-1-get-a-theme-access-password-for-the-store) that you generated or were given by a merchant |
  | `SHOPIFY_FLAG_STORE` | Yes | The store that you want to interact with |
  | `SHOPIFY_FLAG_FORCE` | No | Pass this variable with a value of `1` to turn off interactive prompts. You may want to use this variable if your Shopify CLI pipeline step is timing out. |

  Where possible, you should protect the Theme Access password by masking it or storing it as a secret.

* A step that sets up Node.js.

* A step that installs Shopify CLI globally.

* A step that runs the CLI command that you want to execute.

### Example (GitHub Actions)

Below is an example of a step that you might add to your GitHub Actions workflow. It pushes a theme to a Shopify store when code is pushed to the `main` branch.

## .github/workflows/deploy-theme.yml

```yml
name: Theme deploy

on: [push]

jobs:
  deploy:
    name: Deploy
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20

      - name: Install Shopify CLI
        run: npm install -g @shopify/cli

      - name: Upload theme
        run: |
          shopify theme push \
            --json \
            --theme your-theme-name-or-id \
            --store ${{ secrets.SHOPIFY_FLAG_STORE }} \
            --password ${{ secrets.SHOPIFY_CLI_THEME_TOKEN }}
```

---

### Migrate to Shopify CLI 3.0+

> Fonte: https://shopify.dev/docs/storefronts/themes/tools/cli/migrate

# Migrate to Shopify CLI 3.0+

Learn how to update your theme development environment to use the newest version of Shopify CLI.

## Overview

In October 2022, support for themes was added to Shopify CLI 3.0. Shopify CLI 3.0+ provides a streamlined authentication and store management experience.

On this page, you can learn about the differences between Shopify CLI 2.x and 3.0+, and how to update your theme development environment.

---

## Getting started

Refer to the following tutorials for details about creating or working on a Shopify theme using Shopify CLI:

**[Start building a theme](https://shopify.dev/docs/storefronts/themes/getting-started/create)**

Learn how to set up your theme development environment and create a new theme.

**[Customize an existing theme](https://shopify.dev/docs/storefronts/themes/getting-started/customize)**

Learn how to set up your development environment to work on a theme in a Shopify store.

---

## Workflow changes

Some changes were made to theme workflows to reduce the number of commands that need to be entered, simplify the command structure, and create a more consistent experience when developing across themes, apps, and custom storefronts.

| Feature | 2.0 | 3.0 |
|---------|-----|-----|
| **Authentication** | Authenticate with Shopify CLI using `shopify login` | You don't need to log in explicitly. If you aren't logged in, then you're prompted to log in when you run a command that requires authentication. |
| | View the organization you're currently logged into using `shopify whoami` | *No longer supported* |
| **Store selection** | Select a store using `shopify login --store` | Pass a `--store` flag the first time you run a command that requires connection to a store. This store is used in subsequent commands. |
| | Switch between stores using `shopify switch` | Pass a `--store` flag with a new value when you want to run a command against a new store |
| | Run `shopify store` to view which store you're currently using. | Run `shopify theme info` to view which store you're currently using |
| **General** | Preview your theme in a store using `shopify theme serve` | Command is renamed to `shopify theme dev` |
| | Populate stores using `shopify populate [ products \| draftorders \| customers ]` | *No longer supported* |
| | Specify the directory that you want to use using the `[root]` positional argument | Specify the directory that you want to use using the `–-path` flag |

---

## Migrate to Shopify CLI 3.0+

Follow the steps below to migrate your theme development environment to Shopify CLI 3.0+.

### macOS and Homebrew

If you use Homebrew to manage your Shopify CLI installation on macOS, then you don't need to uninstall the previous version of Shopify CLI to migrate. Instead, you can upgrade to Shopify CLI 3.0+ directly.

In addition to the requirements for Shopify CLI 2.x, Shopify CLI 3.0+ requires [Node.js](https://nodejs.org/en/download/) 18 or higher. Homebrew installs Node.js for you when you upgrade to the latest version of Shopify CLI.

```terminal
brew upgrade shopify-cli
```

### Other

#### Step 1: Install new requirements

In addition to the requirements for Shopify CLI 2.x, Shopify CLI 3.0+ requires [Node.js](https://nodejs.org/en/download/) 18 or higher. If you use macOS, then Homebrew will install Node.js for you when you upgrade to the latest version of Shopify CLI.

For a complete list of requirements, refer to [Install Shopify CLI](https://shopify.dev/docs/api/shopify-cli).

#### Step 2: Uninstall Shopify CLI 2.x

Consider uninstalling the previous version of Shopify CLI. Uninstalling the previous version avoids any collisions between the two versions.

If you want to keep both versions of Shopify CLI installed, then refer to [Using both Shopify CLI 2.x and 3.0+](#using-both-shopify-cli-2x-and-30) to learn how to work with both versions in the same environment.

Shopify CLI can be removed from your system using the same package manager that you used to install it:

**apt**

```terminal
sudo apt remove shopify-cli
```

**Yum**

```terminal
sudo yum remove shopify-cli
```

**RubyGems**

```terminal
gem uninstall shopify-cli
```

If you're using a legacy version of Shopify CLI (lower than `0.9.0`), then you need to [uninstall it manually](https://shopify.dev/docs/storefronts/themes/tools/cli/cli-2/upgrade-uninstall#uninstall-the-legacy-shopify-app-cli).

#### Step 3: Install Shopify CLI 3.0+

Follow the instructions here to install [Shopify CLI](https://shopify.dev/docs/api/shopify-cli).

**Note:** apt, Yum, and RubyGems installations are no longer supported.

#### Step 4: Verify the installation

To verify that Shopify CLI is installed properly, run the following command:

```sh
shopify version
```

The command returns a version number.

---

## Using both Shopify CLI 2.x and 3.0+

If you have both versions of Shopify CLI installed, then the two versions might conflict because they both use the same program name (`shopify`).

Whichever version is listed first in your `PATH` will run. You can update your path to change the default CLI, or temporarily uninstall one version to avoid confusion.

---

### Shopify Liquid Language Server

> Fonte: https://shopify.dev/docs/storefronts/themes/tools/cli/language-server

# Shopify Liquid Language Server

The [Language Server Protocol](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/) allows developers to deliver code editing capabilities across all editors through a unified codebase.

## Installation

The Shopify Liquid Language Server functions as a [Shopify CLI](https://shopify.dev/docs/storefronts/themes/tools/cli/cli-2/commands) theme command.

## Usage basics

Launch the Language Server using this command:

```terminal
shopify theme language-server
```

## Features

The Language Server includes these capabilities:

* Documentation on hover
* Code completion and documentation
* Code formatting
* Theme checks
* Code navigation

For detailed information about these features, consult the [Shopify Liquid VS Code extension user guide](https://shopify.dev/docs/storefronts/themes/tools/cli/language-server).

## Editor integration

Each editor requires its own setup method for Language Servers, though the fundamental approach remains consistent: configuring the editor to launch the Language Server.

[Explore example implementations available in the Theme Tools repository](https://github.com/Shopify/theme-tools/wiki).

## Contributing to the Language Server

The Shopify Liquid Language Server operates as open source software within the broader theme developer tools ecosystem.

Review contribution guidelines for the [`theme-tools` repository](https://github.com/Shopify/theme-tools/blob/main/docs/contributing.md).

---

## Shopify GitHub integration for themes

> Fonte: https://shopify.dev/docs/storefronts/themes/tools/github

# Shopify GitHub integration for themes

The [Shopify GitHub app](https://shopify.dev/docs/api/github-app) lets you connect your GitHub and Shopify accounts. This lets you sync theme code to and from GitHub repositories and collaborate with other developers on your themes.

---

## Features

* Automatically pull and push theme code from any organization or repository associated with your GitHub account
* Connect one or more branches from a repository to easily develop and test new theme features or campaigns
* Keep a theme up to date with commits to a branch, and track edits made in the Shopify admin, including the [code editor](https://shopify.dev/docs/storefronts/themes/tools/code-editor) and [theme editor](https://shopify.dev/docs/storefronts/themes/tools/online-editor)
* Connect branches to unpublished or published themes

---

## How it works

The GitHub theme integration updates your theme in the Shopify admin whenever the connected branch is updated. It also commits changes made through the Shopify admin to the branch to ensure that the branch and theme in the Shopify admin always match.

**Note:**

"Files are updated in GitHub whenever changes are made to a connected theme. This can't be disabled." If you want to separate the code that Shopify has access to from the rest of your code, then consider using multiple repositories or subtrees. For more information, refer to [Version control best practices for Shopify themes](https://shopify.dev/docs/storefronts/themes/best-practices/version-control).

### Commits by Shopify

When your theme is edited through the Shopify admin, any changes are automatically committed to your repository by Shopify. A commit is created when any owner, staff member, or collaborator makes changes. Changes are added as a commit to the connected branch when they are saved.

You can edit your theme in the following areas of the Shopify admin:

* The [theme editor](https://shopify.dev/docs/storefronts/themes/tools/online-editor). When you customize a theme using the theme editor, these customizations are stored in [setting files](https://shopify.dev/docs/storefronts/themes/architecture/settings), which are part of the theme code.
* The [code editor](https://shopify.dev/docs/storefronts/themes/tools/code-editor).
* [Theme apps](https://shopify.dev/docs/apps/build/online-store) installed in the Online Store.

#### Organization access

If you grant the Shopify GitHub app access to repositories in a GitHub organization, then any user that has a GitHub account that is part of the organization, and has the **Manage themes** permission or **Themes** permission, can view any repository that the app has access to in the list of available repositories. However, these users can only connect branches for which they have write permissions, and the branch needs to match the required [repository structure](#repository-structure).

If you want to prevent users from viewing certain repositories, then you should grant Shopify's GitHub app access to only the repositories that you want to connect to the Shopify store. If you grant access to only specific repositories and you create a new repository that you want to use with Shopify, then you need to [grant the app access to the repository through GitHub](https://docs.github.com/en/organizations/keeping-your-organization-secure/reviewing-your-organizations-installed-integrations).

### Conflicts and error handling

If a user is editing an open file in the theme editor while the same file is being edited in GitHub or the code editor, then the user is warned that they're overriding the new changes when they save.

There are currently no conflict alerts in the code editor. The version of the file in the code editor overwrites the GitHub version of the file.

In case of a conflict in commits or pushes made outside Shopify, the developer has a chance to resolve it in GitHub or force push the change to overwrite the file in Shopify.

In limited cases, conflicts might occur if a file is saved in the theme editor or code editor and a change is pushed to the GitHub branch simultaneously. In this case, the commit coming from Shopify might be viewed as outdated and rejected by GitHub.

If you suspect that an error has occurred when pushing or pulling changes, then you can view the logs for the last few version control events by clicking **View logs** beside the **Last saved** timestamp on the theme card.

If you believe that the theme has fallen out of date with the branch, then you can pull the latest version of the branch manually by going to the theme card and selecting **Actions** > **Reset to last commit**.

---

## Limitations

* Only repositories to which you have write access can be used to create a new theme.
* Outside collaborators can't connect branches. Only members of the organization with write access can.
* Personal repositories where you're a collaborator, but not the owner, aren't visible in the list of available repositories.

---

## Repository structure

You can connect only branches that match the default Shopify theme [folder structure](https://shopify.dev/docs/storefronts/themes/architecture#directory-structure-and-component-types). This structure represents a buildless theme, or a theme that has already gone through any necessary [file transformations](https://shopify.dev/docs/storefronts/themes/best-practices/file-transformation).

Folders in the repository that don't match the default theme structure are ignored.

---

## Branch management strategies

Consider the following when managing themes connected to GitHub repositories in Shopify:

* You can't reconnect a branch to a theme after it has been disconnected. If you reconnect a branch, then it's added as a new theme.

* If an unpublished theme is connected to a branch and then published, then it maintains its connection to the branch.

  To understand the relationship between branches and themes, and how to optimize your workflow to use branches effectively, refer to our [version control best practices](https://shopify.dev/docs/storefronts/themes/best-practices/version-control).

---

## Step 1: Connect a theme repo

Make sure you've installed the [Shopify GitHub app](https://shopify.dev/docs/api/github-app) first.

1. From your Shopify admin, go to **Online Store** > **Themes**.
2. In the **Theme library** section, click **Add theme** > **Connect from GitHub**.
3. In the **Connect theme** pane, select your organization or account.
4. Under **Repository**, select your repo.
5. Under **Branch**, search for the branch you want to connect.

The theme appears in your theme library. Themes that are connected to GitHub list the repository, branch name, and last commit time on the theme card.

---

## Step 2: Test the connection

Try making a small change to the theme and then verify that a commit was made in the branch.

1. From your Shopify admin, go to **Online Store** > **Themes**.
2. On the theme that's connected to GitHub, click **Customize**.
3. Change any setting in your theme. For example, in Dawn, you might change the text on the announcement bar.
4. Click **Save**, and then exit the theme editor.
5. In the theme library, on the card for the theme, click the name of the branch to navigate to GitHub.
6. Note the most recent commit. It should list the `shopify` bot as the author of the commit.

![A commit from Shopify in the GitHub repo](https://shopify.dev/assets/assets/images/themes/github/github-update-CZXTUcSD.png)

If desired, you can also push a change to the branch from your local machine. After you push a commit to your branch, the **Last saved** date on the theme updates and the change is visible in the theme.

![The card for a theme that's connected to GitHub](https://shopify.dev/assets/assets/images/themes/github/github-card-C62fPPvl.png)

---

## Step 3: Publish the theme

To track changes to your published theme, you need to publish a theme from your theme library that's connected to a GitHub branch. You might add your main branch as a theme so you can keep your [published theme up to date](https://shopify.dev/docs/storefronts/themes/best-practices/version-control) using Git.

---

## Shopify Liquid VS Code extension

> Fonte: https://shopify.dev/docs/storefronts/themes/tools/shopify-liquid-vscode

# Shopify Liquid VS Code extension

## Installation

The Shopify Liquid Visual Studio Code extension is available on [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=Shopify.theme-check-vscode).

> Install the Shopify Liquid extension in VS Code for the Web to enable intelligent code
> completion, syntax highlighting, and other features for working with themes directly in your browser.

## Features

The Shopify Liquid Visual Studio Code extension is built on top of Shopify's [Liquid Language Server](https://shopify.dev/docs/storefronts/themes/tools/cli/language-server) and offers the following features:

* Syntax highlighting
* Documentation on hover
* Liquid code completion and documentation
* Schema tag code completion
* JSON code completion
* HTML element renaming
* Code formatting
* Code navigation
* Auto-closing pairs
* Theme checks
* Fixes
* Suggestions

### Syntax highlighting

The extension provides syntax highlighting through an officially maintained grammar. "The syntax highlighting grammar is officially maintained by Shopify" and is the same one that GitHub uses to highlight Liquid code.

### Documentation on hover

Hovering over Liquid, HTML, or JSON code reveals its definition, type, and documentation. The hover menu includes clickable links to the official reference.

### Liquid code completion and documentation

The extension contextually completes these elements:

* Liquid tags, filters, objects, and object properties
* HTML tags, attributes, and attribute values
* Theme, section and block settings
* Translation keys
* Snippet names
* Schema tags

A quick information window is available by clicking the caret in the completion menu or pressing the completion keyboard shortcut a second time.

**Keyboard shortcuts:** `Control+Space` (macOS and Windows)

### Schema tag code completion

Valid elements of JSON schema tags are contextually completed.

### JSON code completion

Valid elements of the `config/settings_schema.json` file are contextually completed.

### HTML element renaming

Open and close tags of HTML elements can be renamed together.

**Keyboard shortcuts:** `F2` (Mac and Windows)

### Code formatting

Code formatting is powered by the [Liquid Prettier plugin](https://shopify.dev/docs/storefronts/themes/tools/liquid-prettier-plugin) and can be applied by:

* Automatically on save
* Selecting the **Format Document** right-click menu item
* Running the **Format Document** command in the command palette
* Pressing the **Format Document** keyboard shortcut

**Keyboard shortcuts:** `Shift+Option+F` (Mac), `Shift+Alt+F` (Windows)

### Code navigation

References to other files in Shopify themes are underlined in VS Code. Navigate to associated files using `Command+Click` on Mac or `Control+Click` on other platforms. If the file doesn't exist, you can create one.

### Auto-closing pairs

The extension automatically closes Liquid and HTML character pairs.

### Theme checks

Theme check is "a linter for Shopify Themes." When problems are found, red or yellow wavy lines appear under the code. Errors and warnings also display in the Problems Tab.

**Keyboard shortcuts:** `Command+Shift+M` (Mac), `Control+Shift+M` (Windows)

### Fixes

Auto-fixable diagnostics are indicated by a blue light bulb. Fixes can be applied by:

* Automatically on save
* Selecting it in the **Code Actions** menu (click the blue lightbulb)
* Selecting it from the menu after right-clicking the diagnostic in the **Problems** tab
* Running the **Auto fix...** command in the command palette
* Pressing the **Auto fix...** keyboard shortcut

**Keyboard shortcuts:** `Option+Command+.` (Mac), `Control+Alt+.` (Windows)

### Suggestions

Yellow light bulbs indicate diagnostics with suggestions. These can be applied by:

* Clicking the yellow lightbulb to access the **Code Actions** menu
* Running the **Quick fix...** command in the command palette
* Pressing the **Quick fix...** keyboard shortcut
* Right-clicking the diagnostic in the **Problems** tab

**Keyboard shortcuts:** `Command+.` (Mac), `Control+.` (Windows)

## Contributing to the VS Code extension

The VS Code extension is open source and part of the suite of theme developer tools. Learn how to contribute to the [`theme-tools` repository](https://github.com/Shopify/theme-tools/blob/main/docs/contributing.md).

---

## Shopify Liquid Prettier Plugin

> Fonte: https://shopify.dev/docs/storefronts/themes/tools/liquid-prettier-plugin

# Shopify Liquid Prettier Plugin

The Shopify Liquid Prettier Plugin is an opinionated code formatter for enforcing a consistent style in Liquid and HTML code.

---

## Installation

You can install the Shopify Liquid Prettier Plugin using either npm or Yarn.

### npm

```terminal
npm install --save-dev prettier @shopify/prettier-plugin-liquid
```

### Yarn

```terminal
yarn add --dev prettier @shopify/prettier-plugin-liquid
```

For Prettier version 3 and above, the plugin must also be declared in the configuration.

### .prettierrc

```json
{
  "plugins": ["@shopify/prettier-plugin-liquid"]
}
```

---

## Configuration

The Shopify Liquid Prettier Plugin supports the following configuration options:

| Name | Default value | Description |
| --- | --- | --- |
| `printWidth` | `120` | The number of characters allowed on a line before wrapping. To learn more about the `printWidth` option, refer to the [Prettier documentation](https://prettier.io/docs/en/options.html#print-width). |
| `tabWidth` | `2` | The number of spaces included in each indentation level. To learn more about the `tabWidth` option, refer to the [Prettier documentation](https://prettier.io/docs/en/options.html#tab-width). |
| `useTabs` | `false` | Whether to indent lines with tabs or spaces. To learn more about the `useTabs` option, refer to the [Prettier documentation](https://prettier.io/docs/en/options.html#tabs). |
| `singleQuote` | `false` | Whether to use single or double quotes. To learn more about the `singleQuote` option, refer to the [Prettier documentation](https://prettier.io/docs/en/options.html#quotes). |
| `liquidSingleQuote` | `true` | Whether to use single quotes instead of double quotes in Liquid tags and objects. |
| `embeddedSingleQuote` | `true` | Whether to use single quotes instead of double quotes in embedded languages (JavaScript, CSS, TypeScript inside `<script>`, `<style>` or Liquid equivalent). |
| `htmlWhitespaceSensitivity` | `css` | The HTML whitespace sensitivity. To learn more about the `htmlWhitespaceSensitivity` option, refer to the [Prettier documentation](https://prettier.io/docs/en/options.html#html-whitespace-sensitivity). |
| `singleLineLinkTags` | `false` | Whether to print `<link />` tags on a single line. |
| `indentSchema` | `false` | Whether to indent the contents of `{% schema %}` tags. |

---

## Usage

You can use the Shopify Liquid Prettier Plugin in the following environments:

* Terminal
* Browser
* Editor

You can also use the plugin as a pre-commit hook or with a bundler.

---

## Use the plugin in the terminal

You can use Prettier in the terminal as either a local or global dependency.

### Local dependency

To use Prettier as a local dependency, add it as a script in your `package.json` file:

```json
{
  "scripts": {
    "prettier": "prettier"
  }
}
```

Then you can run it using either npm or Yarn:

#### npm

```terminal
npm run prettier -- path/to/file.liquid --write
```

#### Yarn

```terminal
yarn run prettier path/to/file.liquid --write
```

### Global dependency

If you install Prettier as a global dependency, then you can run it with the following command:

```terminal
prettier path/to/file.liquid --write
```

---

## Use the plugin in the browser

The Shopify Liquid Prettier Plugin exposes a `standalone.js` file that can be used alongside Prettier's own `standalone.js` file.

To use Prettier and the Shopify Liquid Prettier Plugin in the browser, include both `standalone` files using an npm CDN, such as [UNPKG](https://unpkg.com/).

```html
<script src="https://unpkg.com/prettier/standalone.js"></script>
<script src="https://unpkg.com/@shopify/prettier-plugin-liquid/standalone.js"></script>
```

With the `standalone` scripts included, you can format code like the following:

```js
prettier.format(YOUR_CODE, {
  plugins: [prettierPluginLiquid],
  parser: 'liquid-html',
});
```

---

## Use the plugin in an editor

You can use the Shopify Liquid Prettier Plugin in the following editors:

* Visual Studio Code
* Vim
* WebStorm

### Visual Studio Code

You can use the Shopify Liquid Prettier Plugin in Visual Studio Code through one of the following extensions:

* Shopify Liquid
* Prettier

#### The Shopify Liquid extension

The [Shopify Liquid](https://marketplace.visualstudio.com/items?itemName=Shopify.theme-check-vscode) extension includes the Shopify Liquid Prettier Plugin by default.

If you'd like to activate format-on-save, then you can add the following setting:

```json
{
  "[liquid]": {
    "editor.defaultFormatter": "Shopify.theme-check-vscode",
    "editor.formatOnSave": true
  }
}
```

To learn about how to format files with Prettier in Visual Studio Code, refer to the [documentation for the Prettier extension](https://github.com/prettier/prettier-vscode#usage).

#### The Prettier extension

Using the Shopify Liquid Prettier Plugin with the Prettier extension requires the following steps:

1. Install the [Prettier extension](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode).
2. [Install the Shopify Liquid Prettier Plugin](#installation) locally in your repository.

To learn about how to format files with Prettier in Visual Studio Code, refer to the [documentation for the Prettier extension](https://github.com/prettier/prettier-vscode#usage).

### Vim

Using the Shopify Liquid Prettier Plugin in Vim requires the following steps:

1. Install [vim-plug](https://github.com/junegunn/vim-plug).
2. Install [vim-prettier](https://github.com/prettier/vim-prettier).
3. [Install the Shopify Liquid Prettier Plugin](#installation) locally in your repository.

To learn about how to format files with Prettier in Vim, refer to the [documentation for vim-prettier](https://github.com/prettier/vim-prettier#usage).

### WebStorm

Using the Shopify Liquid Prettier Plugin in WebStorm requires the following steps:

1. Install the [Prettier plugin](https://plugins.jetbrains.com/plugin/10456-prettier).
2. [Install the Shopify Liquid Prettier Plugin](#installation) locally in your repository.
3. Restart WebStorm.
4. Search for **Prettier** in the WebStorm preferences and update **Run for files** to include `liquid`.
   * You can also tick the **On save** checkbox to format-on-save.
5. Click **Ok** to save your settings.

To learn about how to format files with Prettier in WebStorm, refer to [the WebStorm documentation](https://www.jetbrains.com/help/webstorm/prettier.html#ws_prettier_reformat_code).

---

## Use the plugin as a pre-commit hook

You can use Prettier with a pre-commit tool. Pre-commit tools can reformat your "staged" files before you commit them.

To learn about pre-commit tools that are compatible with Prettier and how to install them, refer to [Prettier's documentation](https://prettier.io/docs/en/precommit.html).

---

## Use the plugin with a bundler

The Shopify Liquid Prettier Plugin exposes a `standalone.js` file that can be used alongside Prettier's own `standalone.js` file.

To use Prettier and the Shopify Liquid Prettier Plugin with bundlers, such as webpack, Rollup, or Browserify, import both `standalone` files.

```js
import prettier from 'prettier/standalone';
import liquidPlugin from '@shopify/prettier-plugin-liquid/standalone';
```

With the `standalone` files imported, you can format code like the following:

```js
prettier.format(YOUR_CODE, {
  plugins: [liquidPlugin],
  parser: 'liquid-html',
});
```

---

## Contributing to the Shopify Liquid Prettier Plugin

The Shopify Liquid Prettier Plugin is open source.

* Learn how to contribute to the [prettier-plugin-liquid repository](https://github.com/Shopify/theme-tools/blob/main/packages/prettier-plugin-liquid/CONTRIBUTING.md)
* [Report an issue](https://github.com/Shopify/prettier-plugin-liquid/issues/new/choose)

---

## LiquidDoc

> Fonte: https://shopify.dev/docs/storefronts/themes/tools/liquid-doc

# LiquidDoc

LiquidDoc gives you a way to create a structured interface for Liquid snippets and blocks, allowing you to specify input parameters, add descriptions, and provide usage examples. These details are exposed through theme checks, code completions, and hover information, making development faster and more reliable.

---

## Why use LiquidDoc?

It can be easy to make a small mistake when writing Liquid code:

* Missing required parameters don't trigger warnings
* Unrecognized parameters pass through silently
* No type checking ensures values match expected formats
* Parameter discovery requires reading the code

For example, these misspelled parameters won't trigger errors:

```liquid
{% render 'loading-spinner', produt: product, show_vendorr: true %}
```

LiquidDoc solves these problems by providing structured documentation that development tools can recognize, offering real-time feedback during development.

---

## Syntax reference

LiquidDoc uses a JSDoc-inspired syntax to document snippets and blocks. The following tags are supported:

* [@description](#descriptions-description) - explains the purpose
* [@param](#parameters-param) - documents expected parameters
* [@example](#examples-example) - shows usage examples

### Basic structure

Place LiquidDoc content at the top of a snippet or a block file inside a `doc` tag:

```liquid
{% doc %}
  Provides an example of a snippet description.


  @param {string} title - The title to display
  @param {number} [max_items] - Optional maximum number of items to show


  @example
  {% render 'example-snippet', title: 'Featured Products', max_items: 3 %}
{% enddoc %}
```

### Descriptions (`@description`)

You can document the purpose of your snippet or block in two ways:

```liquid
{% doc %}
The description can be placed before any @ annotations without needing a tag.


@description You can also use this tag to place a description anywhere.
{% enddoc %}
```

#### Usage notes

* You can omit the `@description` tag by providing a description before any `@` annotations.
* If you provide multiple descriptions, then only the first one will appear when hovering over a render tag.
* Multi-line descriptions are automatically formatted to start on a new line.

### Parameters (`@param`)

Parameters define the inputs accepted by a snippet or a static block with the following format:

`@param {type} name - description`

| Component | Required | Description |
| - | - | - |
| **Type** | Optional | A data type in curly braces `{}`. Must be one of the [supported types](#supported-parameter-types). |
| **Name** | Required | A parameter identifier. For optional parameters, wrap in `[]`. For example, `[max_items]`. |
| **Description** | Optional | An explanation of the parameter's purpose. |

The following example shows how to use parameters:

```liquid
{% doc %}
  Product card snippet


  @param {string} title - Main product title
  @param {number} price - Product price value
  @param {boolean} show_vendor - Whether to display vendor name
  @param {object} product - Product object
  @param {string} [subtitle] - Optional secondary text
{% enddoc %}
```

#### Supported parameter types

| Type | Description |
| - | - |
| `string` | Text values |
| `number` | Numeric values |
| `boolean` | True/false values. All values in Liquid have truthy or falsy evaluation. |
| `object` | Complex Liquid types or anything that's not a primitive |

### Examples (`@example`)

Examples demonstrate how a snippet or a static block should be used:

```liquid
{% doc %}
  Price display snippet


  @param {number} price - Price value
  @param {boolean} [show_compare_at] - Whether to show compare-at price


  @example
  {% render 'price', price: product.price, show_compare_at: true %}


  @example
  {% render 'price',
    price: variant.price,
    show_compare_at: false
  %}
{% enddoc %}
```

#### Usage notes

* Multiple examples help demonstrate different usage patterns.
* Multi-line examples are automatically formatted to start on a new line.

---

## Editor features

LiquidDoc speeds up development while catching parameter errors, typos, and type mismatches in real-time.

### Hover documentation

See comprehensive information when hovering over a name in a render tag.

### Code completion

Get smart suggestions for parameter names when using documented snippets or static blocks.

### Parameter validation

Receive warnings when required parameters are missing.

### Type checking

Get appropriate suggestions and validation based on type annotations in `@param` tags.

When a type mismatch is detected, the editor suggests converting to these fallback values:

| Type | Fallback value |
| - | - |
| `string` | `''` |
| `number` | `0` |
| `boolean` | `false` |
| `object` | `N/A` |

### Theme Check

LiquidDoc integrates with Theme Check to validate your snippets and blocks through:

* **Documentation checks** - Validate syntax and structure inside `{% doc %}` blocks
* **Usage checks** - Ensure `{% render %}` tags properly use documented parameters

#### Documentation checks

| Check | Description |
| - | - |
| [UniqueDocParamNames](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/unique-doc-param-names) | Each parameter defined in LiquidDoc needs to have a unique name. |
| [UnsupportedDocTag](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/unsupported-doc-tag) | The `doc` tag can only be used within a liquid snippet file. |
| [ValidDocParamTypes](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-doc-param-types) | Each parameter defined in LiquidDoc should be `string`, `number`, `boolean`, `object`, or any liquid object that isn't exclusively a global object. |
| [UnusedDocParam](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/unused-doc-param) | The parameters defined within the `doc` tag must be used within the scope of the variable. |

#### Usage checks

| Check | Description |
| - | - |
| [DuplicateContentForArguments](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/duplicate-content-for-arguments) | Each named argument should be passed into the `content_for` tag only once. |
| [DuplicateRenderSnippetArguments](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/duplicate-render-snippet-arguments) | Each named argument should be passed into the `render` tag only once. |
| [MissingContentForArguments](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/missing-content-for-arguments) | When you render a static block, you must provide all required arguments defined in that block file's LiquidDoc. |
| [MissingRenderSnippetArguments](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/missing-render-snippet-arguments) | When you render a snippet, you must provide all required arguments defined in that snippet file's LiquidDoc. |
| [UnrecognizedContentForArguments](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/unrecognized-content-for-arguments) | All arguments provided when rendering a static block must match the arguments defined in that block's LiquidDoc. |
| [UnrecognizedRenderSnippetArguments](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/unrecognized-render-snippet-arguments) | All arguments provided when rendering a snippet must match the arguments defined in that snippet's LiquidDoc. |
| [ValidContentForArgumentTypes](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-content-for-argument-types) | All arguments provided when rendering a static block must match the respective parameter's type defined in that block's LiquidDoc. |
| [ValidRenderSnippetArgumentTypes](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-render-snippet-argument-types) | All arguments provided when rendering a snippet must match the respective parameter's type defined in that snippet's LiquidDoc. |

### Limitations

#### Dynamic validation

Usage checks are disabled when the name is a variable:

##### ✗ Disabled

```liquid
{% assign snippetName = 'price' %}
{% render snippetName %}
```

##### ✓ Enabled

```liquid
{% render 'price' %}
```

#### Dynamic type validation

We don't currently validate the types of objects or variables passed as parameters:

##### ✗ Disabled

```liquid
{% render 'price', price: product.price %}
```

##### ✓ Enabled

```liquid
{% render 'price', price: 100 %}
```

---

## Next steps

* [Learn more about Liquid syntax](https://shopify.dev/docs/api/liquid).
* [Explore theme development best practices](https://shopify.dev/docs/storefronts/themes/best-practices).

---

## Theme Check

> Fonte: https://shopify.dev/docs/storefronts/themes/tools/theme-check

# Theme Check

Theme Check is a linter for the Liquid and JSON inside your theme and [theme app extensions](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions). It "detects errors and enforces Liquid best practices."

## What Theme Check Can Identify

Theme Check can identify several issues in your theme code:

* Syntax errors
* Missing templates
* Unused variables and snippets
* Unknown and deprecated tags
* Performance issues

Programming and style errors display directly in your console or code editor. Each error includes a link to the failed check's documentation, allowing you to debug issues quickly.

## How to Use Theme Check

You can use Theme Check in the following ways:

* **Through Shopify CLI** - Run checks against your theme on demand, in CI or with our Language Server.
* **Via the Shopify Liquid Visual Studio Code extension** - Theme Check is included in the extension.

## Installation

* [Install Theme Check with Shopify CLI](https://shopify.dev/docs/api/shopify-cli)
* [Install the Shopify Liquid Visual Studio Code extension](https://shopify.dev/docs/storefronts/themes/tools/cli/language-server)

## Configuration

You can customize check options to override defaults, enable or disable specific checks, or reference your own custom checks. To learn more, refer to [Theme Check configuration](https://shopify.dev/docs/storefronts/themes/tools/theme-check/configuration).

## Creating Your Own Checks

You can write your own checks in TypeScript and reference them in your configuration. To learn how existing checks are written, explore the [`theme-tools` repository](https://github.com/Shopify/theme-tools/blob/main/docs/theme-check-common/writing-your-own-check).

## Using Theme Check in Other Editors

Theme Check is available for integration in other editors using Shopify's [Language Server](https://shopify.dev/docs/storefronts/themes/tools/cli/language-server).

## Contributing to Theme Check

Theme Check is open source and part of Shopify's theme developer tools suite. Learn how to contribute to the [theme-tools repository](https://github.com/Shopify/theme-tools/blob/main/docs/contributing.md).

---

### Theme Check configuration

> Fonte: https://shopify.dev/docs/storefronts/themes/tools/theme-check/configuration

# Theme Check configuration

You can configure Theme Check to override default check options, enable or disable specific checks, or point to your own custom checks. You can make these changes using a [config file](#config-file), disable checks using [comments](#disable-checks-using-liquid-comments), or selectively run checks using command line flags. To learn more about theme check command line flags, refer to [Theme Check commands](https://shopify.dev/docs/storefronts/themes/tools/theme-check/commands).

## Config file

Add a `.theme-check.yml` file to the root of your theme to override check defaults.

You can generate a new `.theme-check.yml` file using the command `shopify theme check --init`.

You can adjust the following settings:

| Setting | Type | Description |
|---------|------|-------------|
| `root` | `string` | If your theme isn't using the standard theme directory structure, you can provide root path for finding the `templates`, `sections`, and `snippets` directories. For example, If you generate code from a `src` directory, then you should point your Theme Check configuration at your corresponding `dist` directory. |
| `extends` | `string or string[]` | If you want to compose configuration files, or start off the recommended one, you can use the `extends` setting to reference a configuration file. Also supports the following magic settings: `theme-check:all`, `theme-check:recommended`, `theme-check:theme-app-extension`. When multiple configurations are extended; objects are deep merged, arrays are concatenated, and the latest one in the list takes priority. |
| `require` | `string or string[]` | If you want to use a [custom or third party set of checks](https://shopify.dev/docs/storefronts/themes/tools/theme-check#creating-your-own-checks), then add a CommonJS import path. |
| `ignore` | `string[]` | Exclude directories in the theme from Theme Check. |
| Check settings | `object` | For each check, set `enabled` to `true` or `false`, set the check [severity](#check-severity), set specific `ignore` files and paths for the check, and configure any other check options. |

All settings are optional.

### Example .theme-check.yml

```yaml
# The directory where theme folders are located (optional)
root: dist

# Configuration files are extensible
extends:
  - theme-check:recommended # or theme-check:all, theme-check:theme-app-extension
  - '@acme/my-custom-checks/recommended.yml'
  - '../configs/.theme-check.yml'

# Paths to custom checks
require:
  - ./path/to/my_custom_check.js # path to file or module
  - '@acme/my-custom-checks'     # for node_modules checks

# Paths to ignore (don't lint those!)
ignore:
  - 'node_modules/**'
  - 'snippets/*-icon.liquid' # minimatch globs are supported

# Disable a check
TemplateLength:
  enabled: false
  severity: warning
  ignore:
    - templates/index.liquid
  # Configure options for a check
  max_length: 300

# Enable a custom check
MyCustomCheck:
  enabled: true
  severity: error
```

### Check severity

The check severity indicates the relative importance of a check to the functionality and optimization of your theme. Severity levels include `error`, `warning`, and `info`. You can change the severity of a check in your config file.

If you're running theme check as part of your CI process, the severity levels of the failed checks can determine the exit code that you receive. By default, Theme Check fails, or returns an exit code of 1, when one or more issues with severity `error` are detected. You can configure the severity that causes a run of theme check to fail using the [`--fail-level`](https://shopify.dev/docs/storefronts/themes/tools/theme-check/commands) flag.

The `theme-check:recommended` and `theme-check:all` configurations, and the file generated by `shopify theme check --init`, specify severities as integers. The string and integer forms are equivalent, and you can use either form when configuring a check:

| String | Integer |
|--------|---------|
| `error` | `0` |
| `warning` | `1` |
| `info` | `2` |

The string form is preferred for readability.

## Disable checks using Liquid comments

You can disable all checks or specific checks using comments. You can disable checks for a specific section of your theme code, or for an entire file.

Disable all checks for a section of code:

```liquid
{% # theme-check-disable %}
{% assign x = 1 %}
{% # theme-check-enable %}
```

Disable all checks for the next line:

```liquid
{% # theme-check-disable-next-line %}
{% assign x = 1 %}
```

Disable a specific check for a section of code:

```liquid
{% # theme-check-disable UnusedAssign %}
{% assign x = 1 %}
{% # theme-check-enable UnusedAssign %}
```

Disable a specific check for the next line:

```liquid
{% # theme-check-disable-next-line UnusedAssign %}
{% assign x = 1 %}
```

Disable multiple checks for a section of code by including checks in a comma-separated list:

```liquid
{% # theme-check-disable UnusedAssign, UndefinedObject %}
{% assign x = 1 %}
{% echo y %}
{% # theme-check-enable UnusedAssign, UndefinedObject %}
```

Disable multiple checks for the next line by including checks in a comma-separated list:

```liquid
{% # theme-check-disable-next-line UnusedAssign, UndefinedObject %}
{% assign x = y %}
```

Disable checks for the entire document by placing the comment on the first line:

```liquid
{% # theme-check-disable UnusedAssign %}

{% assign x = 1 %}
```

---

### Theme Check commands

> Fonte: https://shopify.dev/docs/storefronts/themes/tools/theme-check/commands

# Theme Check commands

If you run Theme Check through the command line, then you can use the [Shopify CLI](https://shopify.dev/docs/storefronts/themes/tools/cli/cli-2/commands) commands and flags described in this guide to call and run Theme Check. Learn more about [the checks that Theme Check runs](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks).

## Requirements

To run Theme Check commands, you need to install the [`@shopify/cli`](https://www.npmjs.com/package/@shopify/cli) and [`@shopify/theme`](https://www.npmjs.com/package/@shopify/theme) packages using Homebrew on macOS, or install the packages globally on Windows or Linux. For more information, refer to [Install Shopify CLI](https://shopify.dev/docs/api/shopify-cli).

## Usage

Lints theme code.

```sh
shopify theme check [flags]
```

### Flags

| Flag | Alias | Description | Environment variable |
| - | - | - | - |
| `--config <PATH>` | `-C <PATH>` | The path to your custom [Theme Check config](https://shopify.dev/docs/storefronts/themes/tools/theme-check/configuration). This config overrides `.theme-check.yml`, if it is present in the directory being analyzed. | `SHOPIFY_FLAG_CONFIG` |
| `--fail-level <LEVEL>` | | The [severity level](https://shopify.dev/docs/storefronts/themes/tools/theme-check/configuration#check-severity) that causes a run of theme check to fail (exit code 1). Options include `error`, `suggestion`, and `style`. | `SHOPIFY_FLAG_FAIL_LEVEL` |
| `--auto-correct` | `-a` | Automatically fixes correctable offenses. | `SHOPIFY_FLAG_AUTO_CORRECT` |
| `--init` | | Generates a new [Theme Check config file](https://shopify.dev/docs/storefronts/themes/tools/theme-check/configuration). | `SHOPIFY_FLAG_INIT` |
| `--output` | `-o` | Outputs the results of the check to a file. Options include `json` and `text` (default). | `SHOPIFY_FLAG_OUTPUT` |
| `--print` | | Outputs the active config to STDOUT. | `SHOPIFY_FLAG_PRINT` |
| `--list` | `-l` | Lists the active checks. | `SHOPIFY_FLAG_LIST` |
| `--environment <ENV_NAME>` | `-e <ENV_NAME>` | The [environment](https://shopify.dev/docs/storefronts/themes/tools/cli/environments) that you want to use. | `SHOPIFY_FLAG_ENVIRONMENT` |
| `--version` | `-v` | Prints the version of Theme Check being used. | `SHOPIFY_FLAG_VERSION` |
| `--path <path>` | | The path to your theme directory. | `SHOPIFY_FLAG_PATH` |
| `--verbose` | | Provides more detailed output in the logs. | `SHOPIFY_FLAG_VERBOSE` |

---

### Checks reference

> Fonte: https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks

# Checks reference

You can run the following checks as part of Theme Check. Each check identifies a specific error or a place in your code where a best practice is not being followed.

To learn more about the check and its options, click on the name of the check.

---

## Liquid file checks

These checks analyze the style and validity of Liquid code. Some of these checks support auto-correction using the `--auto-correct` flag.

| Check | Severity | Purpose | Auto-correction |
| - | - | - | - |
| [AppBlockValidTags](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/app-block-valid-tags) | Error | Identifies forbidden Liquid tags in theme app extension app block and app embed block code. | |
| [AssetPreload](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/asset-preload) | Warning | Encourages preloading of assets using Liquid filters, rather than HTML attributes. | |
| [AssetSizeAppBlockCSS](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/app-block-valid-tags) | Error | Prevents theme app extensions from using CSS files larger than the configured threshold. | |
| [AssetSizeAppBlockJavascript](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/app-block-valid-tags) | Error | Prevents theme app extensions from using JavaScript files and external scripts with a compressed size larger than the configured threshold. | |
| [AssetSizeCSS](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/asset-size-css) | Error | Prevents themes from using CSS files larger than the configured threshold. | |
| [AssetSizeJavaScript](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/asset-size-javascript) | Error | Prevents using theme JavaScript files and external scripts with a compressed size greater than the configured threshold. | |
| [BlockIdUsage](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/block-id-usage) | Warning | Warns against the use of block IDs in conditional statements and case statements. | |
| [CdnPreconnect](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/cdn-preconnect) | Warning | This check is aimed at signaling the redundant preconnect to Shopify's CDN. | |
| [ContentForHeaderModification](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/cdn-preconnect) | Error | Identifies code that tries to parse `content_for_header`. | |
| [DeprecateBgsizes](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/deprecate-bgsizes) | Warning | Discourages use of the bgset extension instead of the image-set attribute for loading background images. | |
| [DeprecateLazysizes](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/deprecate-lazysizes) | Warning | Discourages use of the lazysizes library for lazy loading images, iframes, and scripts. | |
| [DeprecatedFilter](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/deprecated-filter) | Warning | Discourages using deprecated filters in themes. | Yes |
| [DeprecatedFontsOnSectionsAndBlocks](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/deprecated-fonts-on-sections-and-blocks) | Warning | Discourages using deprecated fonts in section and block schemas. | |
| [DeprecatedFontsOnSettingsData](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/deprecated-fonts-on-settings-data) | Warning | Discourages using deprecated fonts in the `config/settings_data.json` file. | |
| [DeprecatedFontsOnSettingsSchema](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/deprecated-fonts-on-settings-schema) | Warning | Discourages using deprecated fonts in the `settings_schema.json` file. | |
| [DeprecatedTag](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/deprecated-tag) | Error | Discourages using deprecated tags in themes. | |
| [DuplicateContentForArguments](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/duplicate-content-for-arguments) | Warning | Identifies when argument names provided for the `content_for` tag are not unique. | |
| [DuplicateRenderSnippetArguments](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/duplicate-render-snippet-arguments) | Warning | Identifies when argument names provided for the `render` tag are not unique. | |
| [EmptyBlockContent](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/empty-block-content) | Warning | Detects instances where the Liquid tag `{% content_for 'blocks' %}` is used when the associated schema `blocks` array is empty or undefined. | |
| [HardcodedRoutes](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/hardcoded-routes) | Warning | Encourages use of the routes object instead of hardcoding URLs. | |
| [ImgWidthAndHeight](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/img-lazy-loading) | Error | Enforces setting the `width` and `height` attributes on `img` tags. | |
| [LiquidFreeSettings](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/liquid-free-settings) | Warning | Identifies when a theme is using the `{% liquid %}` tag within `Settings` values. | |
| [LiquidHTMLSyntaxError](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/liquid-html-syntax-error) | Error | Identifies Liquid and HTML syntax errors. | |
| [MissingAsset](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/missing-asset) | Error | Makes sure that all asset files referenced by the `asset_url` filter exist. | |
| [AppBlockMissingSchema](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/app-block-missing-schema) | Error | Ensures schema is present in app blocks in theme app extensions. | |
| [MissingContentForArguments](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/missing-content-for-arguments) | Warning | Identifies when required arguments are not provided when using a `content_for` tag. | |
| [MissingRenderSnippetArguments](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/missing-render-snippet-arguments) | Warning | Identifies when required arguments are not provided when using a `render` tag. | |
| [MissingTemplate](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/missing-asset) | Warning | Identifies when a resource is referenced using a `render`, `section`, or `include` tag, but doesn't exist. | Yes |
| [OrphanedSnippet](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/orphaned-snippet) | Warning | Identifies snippets that exist but are never referenced or rendered in the theme. | |
| [PaginationSize](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/pagination-size) | Warning | Ensures that objects are paginated with performant sizes so too many objects are not loaded at once. | |
| [ParserBlockingJavaScript](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/parser-blocking-javascript) | Error | Identifies script tags that don't have defer or async attributes, avoiding parser-blocking JavaScript. | |
| [RemoteAsset](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/remote-asset) | Warning | Discourages use of third party domains for hosting assets. | |
| [RequiredLayoutThemeObject](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/required-layout-theme-object) | Error | Makes sure that the theme.liquid layout file contains the required `{{ content_for_header }}` and `{{ content_for_layout }}` objects. | Yes |
| [SchemaPresetsBlockOrder](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/schema-presets-block-order) | Warning | Makes sure that the section and block schema presets are correctly used in the `block_order`. | |
| [SchemaPresetsStaticBlocks](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/schema-presets-static-blocks) | Error | Warns if a preset static block doesn't have a `{% content_for "block" ... %}` tag in the Liquid code. | |
| [StaticStylesheetAndJavascriptTags](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/static-stylesheet-and-javascript-tags) | Error | Warns if Liquid code is used inside a `{% stylesheet %}` or `{% javascript %}` tag. | |
| [TranslationKeyExists](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/translation-key-exists) | Error | Identifies references to translations that don't exist. | |
| [UnclosedHTMLElement](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/unclosed-html-element) | Error | Identifies instances of unclosed HTML elements in branching code. | |
| [UndefinedObject](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/undefined-object) | Error | Identifies references to undefined Liquid objects. | |
| [UniqueStaticBlockId](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/unique-static-block-id) | Error | Identifies when two static blocks are using the same ID. | |
| [UnknownFilter](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/unknown-filter) | Error | Identifies references to unknown Liquid filters. | |
| [UnusedAssign](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/unused-assign) | Warning | Identifies variable definitions that aren't used. | |
| [UniqueDocParamNames](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/unique-doc-param-names) | Error | Identifies when parameter names in LiquidDoc are not unique. | |
| [UnrecognizedContentForArguments](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/unrecognized-content-for-arguments) | Warning | Identifies when unknown arguments for a static block are provided when using a `content_for` tag. | |
| [UnrecognizedRenderSnippetArguments](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/unrecognized-render-snippet-arguments) | Warning | Identifies when unknown arguments for a snippet are provided when using a `render` tag. | |
| [UnsupportedDocTag](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/unsupported-doc-tag) | Error | Identifies when LiquidDoc tag is used outside of snippets. | |
| [UnusedDocParam](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/unused-doc-param) | Warning | Identifies when parameters are defined within LiquidDoc, but are not used within the snippet. | |
| [ValidBlockTarget](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-block-target) | Error | Identifies when a block is using an invalid target. | |
| [ValidContentForArguments](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-content-for-arguments) | Error | Identifies invalid arguments passed to the `{% content_for %}` tag. | |
| [ValidContentForArgumentTypes](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-content-for-argument-types) | Warning | Identifies when arguments are provided when using a `content_for` tag, but the types of the arguments don't match the type defined in the block's LiquidDoc. | |
| [ValidDocParamTypes](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-doc-param-types) | Error | Identifies when invalid parameter types exist in LiquidDoc. | |
| [ValidLocalBlocks](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-local-blocks) | Error | Identifies when a local block is used incorrectly. | |
| [ValidRenderSnippetArgumentTypes](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-render-snippet-argument-types) | Warning | Identifies when arguments are provided when using a `render` tag, but the types of the arguments don't match the type defined in the snippet's LiquidDoc. | |
| [ValidSchema](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-schema) | Warning | Identifies invalid JSON in `{% schema %}` tags. | |
| [ValidSchemaName](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-schema-name) | Error | Identifies invalid values for the schema name property. | |
| [ValidSchemaTranslations](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-schema-translations) | Error | Identifies translation keys in schema tags that don't have a matching entry in the default schema locale file. | |
| [ValidScopedCSSClass](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-scoped-css-class) | Warning | Warns when a CSS class used in an HTML class attribute might be defined outside the current file's scope. | |
| [ValidSettingsKey](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-settings-key) | Error | Identifies when preset settings key, default settings key, or referenced block setting key is defined in their respective schema. | |
| [ValidStaticBlockType](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-static-block-type) | Error | Identifies when a static block is using an invalid type. | |
| [VariableName](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/variable-name) | Warning | Identifies variable names that don't adhere to a selected naming convention. | |

---

## JSON file checks

These checks analyze the syntax, content and structure of JSON files.

| Check | Severity | Purpose | Auto-correction |
| - | - | - | - |
| [JSONMissingBlock](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/json-missing-block) | Error | Identifies when a JSON template file is referencing block types that don't exist. | |
| [JSONSyntaxError](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/json-syntax-error) | Error | Identifies invalid JSON files in themes. | |
| [MatchingTranslations](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/matching-translations) | Warning | Identifies missing or additional translations in locale files. | Yes |
| [ValidHTMLTranslation](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-html-translation) | Warning | Identifies invalid HTML inside translations. | |

---

## The theme editor

> Fonte: https://shopify.dev/docs/storefronts/themes/tools/online-editor

# The theme editor

The [theme editor](https://shopify.com/admin/themes/current/editor) is a tool that lets merchants customize the content and appearance of their store, and preview changes to their theme in real time.

As a theme developer, you can allow merchants to customize their theme in the theme editor by introducing [settings](#allowing-for-customization-through-the-theme-editor), and by dividing your theme functionality into [modular sections and blocks](https://shopify.dev/docs/storefronts/themes/best-practices/templates-sections-blocks).

You need to [integrate your theme with the theme editor](#integrating-your-theme-with-the-theme-editor) to create a seamless editing experience for merchants. In the theme editor preview, the merchant should see exactly what will appear in the storefront when the theme is live.

![The theme editor in the Shopify admin](https://shopify.dev/assets/assets/images/themes/theme_editor-fhUF7rbL.png)

---

## Accessing the theme editor through the Shopify admin

Merchants can access the theme editor in the Shopify admin.

1. From the Shopify admin, go to **Online Store** > **Themes**.
2. Find the theme that you want to edit, and then click **Customize**.

---

## Accessing the theme editor during development

To understand how your theme settings appear to merchants, you can preview your theme in the theme editor. You can access the theme editor during development by using the following methods:

* Run your theme as a [development theme](https://shopify.dev/docs/storefronts/themes/tools/cli#development-themes) or [push your theme to a store](https://shopify.dev/docs/api/shopify-cli/theme/theme-push) using [Shopify CLI](https://shopify.dev/docs/api/shopify-cli/theme)
* Connect a GitHub branch to your store using the [Shopify GitHub integration](https://shopify.dev/docs/storefronts/themes/tools/github)
* Upload your theme as a ZIP to a Shopify store

You should choose the preview method that makes the most sense for your current development process.

---

## Allowing for customization through the theme editor

The settings that a merchant can access in the theme editor are controlled by the theme. Settings can be specified in the following places:

* The theme's [config/settings_schema.json](https://shopify.dev/docs/storefronts/themes/architecture/settings) file
* The setting attributes for each [section](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#settings) that's included in the theme.

When a merchant configures these settings using the theme editor, their configurations are saved. Learn more about [theme settings, and the types of settings that you can add to your theme](https://shopify.dev/docs/storefronts/themes/architecture/settings).

---

## Live preview

The theme editor can preview certain input settings as merchants interact with them, instead of refreshing the entire storefront preview after the merchant makes a selection.

The following input setting categories support live preview:

* [Color settings](#color-settings)
* [Text settings](#text-settings)

### Color settings

The theme editor can show a live preview of input settings that return a [`color` object](https://shopify.dev/docs/api/liquid/objects/color), including [color](https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings#color) and [color_background](https://shopify.dev/docs/themes/architecture/settings/input-settings#color_background).

To allow the theme editor to preview color setting changes live, reference the setting in a `{% style %}` tag in a Liquid template, a section, or a snippet. You can reference the `color` object directly, or the one of the following properties of the object:

* `red`
* `green`
* `blue`
* `rgb`

#### Limitations

The theme editor can't provide a live preview for color settings in the following cases.

##### Filtered settings

To support live preview, the theme editor renders color settings inside [`{% style %}`](https://shopify.dev/docs/api/liquid/tags/style) tags as a CSS variable (for example, `var(--shopify-variable)`) instead of the merchant's selected value. Any Liquid filter applied to a color setting operates on this rendered CSS variable string, not on the underlying color value, so the live preview can't update.

For example, the following pattern can't be previewed live because the [`replace` filter](https://shopify.dev/docs/api/liquid/filters/replace) operates on the CSS variable string, not on the color's `rgb` value:

| | |
| - | - |
| ![don't](https://shopify.dev/assets/assets/images/themes/templates-tutorial/x-BmGlFLqe.png) | ```liquid {% style %}   .h1 {     color: {{ settings.colors_accent_2.rgb \| replace: ' ', ',' }};   } {% endstyle %} ``` |

The same constraint affects using the [`default` filter](https://shopify.dev/docs/api/liquid/filters/default). In the editor, the setting value is never `nil` since it resolves to a CSS variable string. This causes the editor preview and the published storefront to differ.

While it is not possible to use Liquid filters and have live preview work, you can assign the setting to a Liquid variable outside the `{% style %}` tag, then reference the variable inside it. This will allow the filter to take effect in both the editor and the storefront.

For example, to set a fallback that takes effect in both the editor and the storefront:

| | |
| - | - |
| ![do](https://shopify.dev/assets/assets/images/themes/templates-tutorial/check-D2CvX7Jo.png) | ```liquid {% assign color_value = settings.colors_accent_1 \| default: '#000000' %} {% style %}   .h1 {     color: {{ color_value }};   } {% endstyle %} ``` |

##### Stylesheets

The theme editor can't provide a live preview for color settings that are referenced in stylesheets that are stored in the `/assets` directory of a theme. Instead, we recommend declaring a CSS variable in your `theme.liquid` layout file and referencing it in your theme's CSS files.

Refer to [theme.liquid](https://github.com/Shopify/dawn/blob/d902375db0a71d5d2d6091eea242b71a42aa16ad/layout/theme.liquid#L67) and [base.css](https://github.com/Shopify/dawn/blob/d902375db0a71d5d2d6091eea242b71a42aa16ad/assets/base.css#L5) in Dawn for an example implementation.

### Text settings

The theme editor can show a live preview of plain or rich text settings. This includes the following settings:

* [text](https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings#text)
* [textarea](https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings#textarea)
* [inline_richtext](https://shopify.dev/docs/themes/architecture/settings/input-settings#inline_richtext)
* [richtext](https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings#richtext)

To allow the theme editor to preview text settings live, the code where the setting is referenced must meet the following criteria:

* The setting value must be the only child of its parent HTML element:

| | |
| - | - |
| ![do](https://shopify.dev/assets/assets/images/themes/templates-tutorial/check-D2CvX7Jo.png) | ```liquid <h1>{{ section.settings.title }}</h1> ``` |
| ![do](https://shopify.dev/assets/assets/images/themes/templates-tutorial/check-D2CvX7Jo.png) | ```liquid <h1><span className="icon">...</span> <span>{{ section.settings.title }}</span></h1> ``` |
| ![don't](https://shopify.dev/assets/assets/images/themes/templates-tutorial/x-BmGlFLqe.png) | ```liquid <h1><span className="icon">...</span> {{ section.settings.title }}</h1> ``` |

* There must be no Liquid filters applied to the setting value, other than the [`escape` filter](https://shopify.dev/docs/api/liquid/filters/escape):

| | |
| - | - |
| ![do](https://shopify.dev/assets/assets/images/themes/templates-tutorial/check-D2CvX7Jo.png) | ```liquid <h1>{{ section.settings.title \| escape }}</h1> ``` |
| ![don't](https://shopify.dev/assets/assets/images/themes/templates-tutorial/x-BmGlFLqe.png) | ```liquid <h1>{{ section.settings.title \| replace: ' ', '-'  }}</h1> ``` |

* The setting must not be preceded by, followed by, or wrapped by other Liquid markup inside of the parent HTML element:

| | |
| - | - |
| ![do](https://shopify.dev/assets/assets/images/themes/templates-tutorial/check-D2CvX7Jo.png) | ```liquid {%- when 'heading' -%}   <h1>{{ block.settings.title }}</h1> {%- endwhen -%} ``` |
| ![don't](https://shopify.dev/assets/assets/images/themes/templates-tutorial/x-BmGlFLqe.png) | ```liquid <h1>   {%- assign title = block.settings.title -%}   {{ title }} </h1> ``` |
| ![don't](https://shopify.dev/assets/assets/images/themes/templates-tutorial/x-BmGlFLqe.png) | ```liquid <h1>   {%- when 'heading' -%}     {{ block.settings.title }}   {%- endwhen -%} </h1> ``` |

* The element must not be hidden when the page loads:

| | |
| - | - |
| ![don't](https://shopify.dev/assets/assets/images/themes/templates-tutorial/x-BmGlFLqe.png) | ```liquid {%- unless block.settings.title == blank -%}     <h1>{{ block.settings.title }}</h1> {%- endunless -%} ``` |

---

## Integrating your theme with the theme editor

You need to make sure that your theme behaves in the editor the same way it would in the storefront. In some cases, you need to adjust your theme's behavior when it's being previewed in the theme editor to give merchants this experience.

To make your theme context-aware, you need to integrate with the theme editor.

Integrating with the theme editor allows you to do the following:

* Disable any code that should be run only when the theme is viewed by a customer
* Enable or disable any code that should be run only when the theme is being edited
* Make sure that any necessary code is run or cleaned up when a section is added, removed, customized, or moved

### Detecting the theme editor

**Caution:**

You shouldn't use these methods to change the storefront preview that's displayed in the theme editor. In most cases, the preview that merchants see in the theme editor should match what their customers see on the live store.

A use case for this variable is to prevent theme editor session data from being included in any page tracking scripts. Another use case is working with a third-party API that returns and outputs any errors to the theme editor but never to the live store.

#### Using Liquid

The [`request.design_mode`](https://shopify.dev/docs/themes/liquid/reference/objects/request#request-design_mode) global variable can be used in your theme's Liquid files to detect whether the storefront is being viewed in the theme editor. The value of the variable is set to `true` when viewing the theme editor. Otherwise, it's set to `false`.

```liquid
{% if request.design_mode %}
<!-- This will only render in the theme editor -->
{% endif %}
```

#### Using JavaScript

The `Shopify.designMode` global variable can be used in your theme's JavaScript files to detect whether the storefront is being viewed in the theme editor. The value of the variable is set to `true` when viewing the theme editor. Otherwise, it's set to `undefined`.

```js
if (Shopify.designMode) {
// This will only happen in the theme editor
}
```

### Reacting to theme editor JavaScript events

When a merchant interacts with a section or block in the theme editor, or activates or deactivates the [theme editor preview inspector](https://help.shopify.com/manual/online-store/themes/customizing-themes/edit#preview-inspector), the theme editor emits JavaScript events. To learn about the actions that your code should take to account for these events, refer to [Integrate sections with the theme editor](https://shopify.dev/docs/storefronts/themes/best-practices/editor/integrate-sections-and-blocks).

---

## The code editor

> Fonte: https://shopify.dev/docs/storefronts/themes/tools/code-editor

# The code editor

The [code editor](http://shopify.com/admin/themes/current) lets you view and edit your theme's code directly in the Shopify admin.

## Access the code editor

### Desktop

1. From your Shopify admin, go to **Online Store** > **Themes**.
2. Find the theme that you want to edit, and then click **...** > **Edit code**.

### Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap **Store**.
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage all themes**.
4. Find the theme that you want to edit, and then tap **...** > **Edit code**.

## Navigate the code editor

"The code editor shows theme files in a directory on the left and an editing area on the right." You can open and edit multiple files simultaneously by clicking on any file.

## Add theme files

To add a file, select a folder, click **New file**, and enter the file name. You can also right-click a folder to add a file.

## Update theme files

When you edit a file, a dot appears next to the tab name to show unsaved changes. Click **Save** in the upper-right corner to save your changes.

**Tip:** Use `Cmd + S` (Mac) or `Ctrl + S` (Windows/Linux) to save changes.

### Rename files

Right-click a file and select **Rename...** to rename it.

### Track file changes

"You can also view past versions of any Liquid file." Find previous versions in the **Timeline** panel at the bottom right.

To revert changes, select an earlier version, review the differences, and click **Revert contents** in the upper-right corner.

## Delete theme files

To permanently delete a file, right-click it and select **Delete permanently**.

## Format theme code

To fix code indentation, open the Command Palette with `Cmd + Shift + P` (Mac) or `Ctrl + Shift + P` (Windows/Linux), type `format`, and select **Format document**.

**Tip:** Configure formatting options like auto-format on paste or save in settings. Click the cogwheel icon in the bottom left, select **Settings**, and search for `format`.

## Review code

"The code editor includes the Theme Check linter for Liquid and JSON files." It helps you catch errors and follow Shopify theme and Liquid best practices.

See the [Theme Check reference](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks) for available checks.

## Search for code

### Search for a file

Use `Cmd + P` (Mac) or `Ctrl + P` (Windows/Linux) to search for a file in the repository by its filename.

### Search within the file

Use `Cmd + F` (Mac) or `Ctrl + F` (Windows/Linux) to search within the open file.

**Tip:** To replace existing text, click the arrow next to the search field to open the replace field, and enter the new text.

### Search across all files

Click the search button in the left sidebar to search across all theme files. Results show every instance of your search term and which file it appears in.

---

## Manage theme access (Theme Access app)

> Fonte: https://shopify.dev/docs/storefronts/themes/tools/theme-access

# Manage theme access

The Theme Access app allows you to securely create and manage passwords that developers need to use to work on a theme using [Shopify CLI](https://shopify.dev/docs/apps/build/cli-for-apps) (and the deprecated [Theme Kit](https://shopify.dev/docs/storefronts/themes/tools/theme-kit)). This guide explains how to install the Theme Access app, and then share credentials with developers.

---

## Requirements

To set up the Theme Access app, you need to have access to the associated store through one of the following roles, which must have the corresponding permissions:

| Role | Permission category | Permission |
| - | - | - |
| Store owner | Not applicable | Not applicable |
| [Staff](https://help.shopify.com/manual/your-account/staff-accounts/staff-permissions/staff-permissions-descriptions) | Administration permissions | **Edit permissions** (including **Add and remove staff**) |
| Online store permissions | **Themes** | |
| [Collaborator](https://help.shopify.com/en/manual/your-account/staff-accounts/collaborator-accounts) | Online store permissions | **Themes** |

---

## How the Theme Access app works

The Theme Access app is available as a free download from the [Shopify App Store](https://apps.shopify.com/theme-access).

After you install the Theme Access app on your store, you can create passwords to share with developers that would like to access your themes. The app generates passwords that are scoped to grant developers with only write access to themes (`write_themes`).

After a developer receives a link to the password in their email, in order to connect to your store and begin making changes to themes, they can supply the password in different ways:

| Tool | Method |
| - | - |
| Shopify CLI | * [In a CI/CD pipeline](https://shopify.dev/docs/storefronts/themes/tools/cli/ci-cd), using the `SHOPIFY_CLI_THEME_TOKEN` environment variable. * In a terminal, using the `--password` flag. |
| Theme Kit (deprecated) | Using a [config file](https://shopify.dev/docs/storefronts/themes/tools/theme-kit/configuration-reference#config-file) or [environment variable](https://shopify.dev/docs/storefronts/themes/tools/theme-kit/configuration-reference#environment-variables). |

**Tip:**

"The Theme Access app was previously called the Theme Kit Access app. Passwords generated with either version of the app are interchangeable."

---

## Install the Theme Access app

To get started, install the Theme Access app on your store.

1. Go to the **Theme Access** app page on the [Shopify App Store](https://apps.shopify.com/theme-access).
2. On the **Theme Access** app page, click **Add app**.
3. In your Shopify admin, to authorize the use of the app, click **Install app**.

After the app is installed, you can view and use it from the **Apps** page in your Shopify admin.

---

## Create a password

To grant a developer access to develop your theme using [Shopify CLI](https://shopify.dev/docs/api/shopify-cli), you can create a password. "The password is sent to the developer's email, which contains a link to the password. The link expires after 7 days or after the password has been viewed by the developer. The developer can view the password only once."

1. From the **Theme Access** app, click **Create theme password**.
2. Enter the contact details for the developer that is working on your theme and click **Create password**.

---

## Resend a password

If the developer didn't receive the password or if their invitation expired, then you can resend the email containing the link to the password.

1. From the **Passwords** page in the **Theme Access** app, click **Details** next to developer that needs the password re-sent.
2. Click **Resend email**.

The password is sent to the developer's email address. The email that contains the password expires after 7 days or after the password has been viewed by the developer.

---

## Delete a password

You can delete a developer's password if they no longer need access to your store. "Deleting a password revokes access to the store's themes. If you wanted to grant access to the developer again, then you would need to create a new password."

1. From the **Passwords** page in the **Theme Access** app, click **Delete** next to the developer whose access you want to remove.
2. Click **Delete** to confirm removing the developer's password.

---

## Next steps

* [Learn more about Shopify CLI](https://shopify.dev/docs/api/shopify-cli/theme).
* [Set up a CI CD pipeline with Shopify CLI](https://shopify.dev/docs/storefronts/themes/tools/cli/ci-cd).

---

## Dev stores

> Fonte: https://shopify.dev/docs/storefronts/themes/tools/development-stores

# Dev stores

A dev store is a free Shopify store for building themes. You can use dev tools like Shopify CLI and the Shopify GitHub integration for themes to preview, test, and share the themes that you're building.

---

## Creating a dev store

To use a dev store with Shopify CLI, you need to be the store owner, or have a staff account on the store. If you create a dev store, then you're assigned as the store owner. Other staff members must be added to the store.

To create a dev store:

1. From your Dev Dashboard, click **Dev Stores**.
2. Click **Add dev store**.
3. Enter a name for your store. The store name is used to create the store's myshopify.com URL.
4. Choose the Shopify plan that you want to use.
5. Recommended: Select **Generate test data for store**. This will populate your store with test data generated by Shopify.
6. Optional: Select **Test a feature preview**. You can choose a feature preview to test capabilities that aren't available to all stores yet.
7. Click **Create store**.

### Generated test data

By default, Shopify stores are created empty, without any data. To speed up the development and testing process, you can create a dev store that's populated with test data generated by Shopify.

The generated test data set includes the most common commerce primitives and configurations that you need to test an app, theme, or custom storefront, including some Plus-specific features.

---

## Sharing your dev store

Dev stores are always password protected. You can remove the password page after you transfer the store to a merchant or switch to a paid plan. Dev store password pages can't be customized.

Visitors can view dev stores in the following ways:

* By entering a password on the dev store password page
* By logging into the dev store's Shopify admin
* Through a Shopify Theme Store or Shopify App Store demo link

### Viewing or setting the password

1. From your Shopify admin, go to **Online Store** > **Preferences**.
2. In the **Password protection** > **Password** field, enter a password. This is the password that you'll give to the visitors who you want to be able to access the online store. Don't use the same password that you use to log in to your admin.
3. Click **Save**.

**Note:**

The **Message for your visitors** field isn't editable for dev stores.

### Viewing and editing the customizable password page

The customizable password page isn't used to control access to your dev store, but you can view it after you log in and edit it from the Shopify admin.

To view the customizable password page, logged-in visitors can navigate to `https://your-store-name.myshopify.com/password`, where `your-store-name` is the name of the dev store.

You can edit the customizable password page using the theme editor, or by editing the theme's `password.liquid` file.

### Theme Store and App Store listings

You can use a dev store as a demo store in Shopify Theme Store or Shopify App Store listings. When a visitor clicks on the demo link in a listing, the dev store password page doesn't display. You don't need to change any settings in the dev store to enable this functionality.

---

## Features and limitations

You can do the following tasks while building and testing a dev store:

* Process an unlimited number of test orders
* Create an unlimited number of unique products
* Create up to 10 custom apps
* Assign a custom domain

A dev store has the following limitations:

* You can only install free apps and Partner-friendly apps.
* You can only test orders using the Bogus Test gateway or by enabling test mode for your payment provider. You can't test orders using real transactions through active payment providers.
* You can't remove the password page, or show a custom password page. You can still customize the password page and preview it.

A dev store with a feature preview enabled doesn't have access to domains.

---

## Next steps

* Create your first theme using a dev store
* Build a store for a merchant
* Connect to the dev store using the Shopify GitHub integration

---

### Generated test data

> Fonte: https://shopify.dev/docs/storefronts/themes/tools/development-stores/generated-data

# Generated test data

By default, Shopify stores are created empty, without any data. To speed up the development and testing process, you can create a dev store that's populated with test data generated by Shopify.

The generated test data set includes the most common commerce primitives and configurations that you need to test an app, theme, or custom storefront, including some Plus-specific features.

This reference lists objects, configurations, and relationships that are included in the development store test data set.

> **Caution:** Stores that start with generated test data can't be transferred to a merchant due to their unique configuration and the use of Shopify Plus features.

---

## Store configurations

Stores that use generated test data have the following configurations:

| Setting name | Configuration | Notes |
|---|---|---|
| Bogus payment gateway | Enabled | Used to create test orders |

---

## Products

The generated test data set contains the following products:

| Name | Configuration | Connected resources |
|---|---|---|
| The Minimal Snowboard | Only required fields populated | **Collection:** Home page<br>**Location:** Shop location |
| The Complete Snowboard | All fields populated<br>Contains variants: Dawn, Electric, Ice, Powder, Sunset | **Collection:** Automated Collection<br>**Location:** Shop location |
| The Hidden Snowboard | Product is hidden on the Online Store channel | **Collection:** Automated Collection<br>**Location:** Shop location |
| The Archived Snowboard | Status is set to archived | **Location:** Shop location |
| The Draft Snowboard | Status is set to draft | **Location:** Shop location |
| The Collection Snowboard: Hydrogen | All fields populated | **Collections:** Automated Collection, Hydrogen<br>**Location:** Shop location |
| The Collection Snowboard: Liquid | All fields populated | **Collections:** Automated Collection, Hydrogen<br>**Location:** Shop location |
| The Collection Snowboard: Oxygen | All fields populated | **Collection:** Hydrogen<br>**Location:** Shop location |
| The Multi-managed Snowboard | Fulfilled by both a fulfillment service and a store location (multi-managed inventory) | — |
| The Multi-location Snowboard | Has inventory at more than one store location (multi-location inventory) | **Collection:** Automated Collection<br>**Locations:** Shop location, My Custom Location |
| The 3p Fulfilled Snowboard | Has inventory with a fulfillment service only | **Fulfillment service:** Snow City Warehouse |

The following products are available on development stores created after April 13, 2023:

| Name | Configuration | Connected resources |
|---|---|---|
| The Out of Stock Snowboard | Inventory is tracked, but available quantity is set to 0 | **Location:** Shop location |
| The Inventory Not Tracked Snowboard | Inventory isn't tracked | **Location:** Shop location |
| The Compare at Price Snowboard | Has a compare at price | **Collection:** Automated Collection<br>**Location:** Shop location |
| The Videographer Snowboard | Has a video uploaded as media | **Location:** Shop location |
| Selling Plans Ski Wax | Has purchase options set | **Selling plans:** Preorder, Prepaid, Subscription, Try Before You Buy |
| Gift Card | Gift card<br>Contains variants: $10, $25, $50, $100 | **Collection:** Automated Collection |

---

## Collections

The generated test data set contains the following collections:

| Name | Configuration | Connected resources |
|---|---|---|
| Automated Collection | Automated collection<br>Condition: product price is greater than $200.00 and less than $800.00 | **Products:** The Complete Snowboard (all variants), The Hidden Snowboard, The Collection Snowboard: Hydrogen, The Collection Snowboard: Liquid, The Multi-managed Snowboard, The Multi-location Snowboard, The Compare at Price Snowboard, Gift Card |
| Hydrogen | Manual collection | **Products:** The Collection Snowboard: Hydrogen, The Collection Snowboard: Oxygen, The Collection Snowboard: Liquid |
| Home page | Manual collection | **Products:** The Minimal Snowboard |

---

## Customers

The generated test data set contains the following customers:

| Name | Configuration | Connected resources |
|---|---|---|
| Ayumu Hirano | Only required fields populated | **Gift Cards:** 0001 |
| Russell Winfield | All fields populated | **Orders:** Custom Item, Order Discount, Line Item Discount & Order Discount, Multiple Fulfillments |
| Karine Ruby | Associated with a company as the main contact | **Orders:** Custom Shipping Rate, Line Item Discount, Shipping Discount<br>**Company:** Snowdevil |

---

## Companies

The generated test data set contains the following companies:

| Name | Configuration | Connected resources |
|---|---|---|
| Powderbound | Only required fields populated | — |
| Snowdevil | All fields populated | **Customer:** Karine Ruby (Main Contact) |

---

## Locations

The generated test data set contains the following locations:

| Name | Configuration | Connected resources |
|---|---|---|
| My Custom Location | All fields populated | **Products (inventory):** The Multi-location Snowboard |
| Shop location | Only required fields populated | **Products (inventory):** The Minimal Snowboard, The Complete Snowboard (all variants), The Hidden Snowboard, The Archived Snowboard, The Draft Snowboard, The Collection Snowboard: Hydrogen, The Collection Snowboard: Liquid, The Collection Snowboard: Oxygen, The Multi-managed Snowboard, The Multi-location Snowboard, The Out of Stock Snowboard, The Inventory Not Tracked Snowboard, The Compare at Price Snowboard, The Videographer Snowboard, Selling Plans Ski Wax |

---

## Orders

> **Note:** In stores created after September 14, 2023, these orders are created as draft orders. You can convert a draft order to an order by marking the draft order as paid in the Shopify admin, or by using the GraphQL `draftOrderComplete` mutation to complete the order.

The generated test data set contains the following orders. Orders can be identified by their tags.

| Tag | Configuration | Connected resources |
|---|---|---|
| `Minimal Info` | Only required fields populated | **Product:** The Minimal Snowboard<br>**Location:** Shop location |
| `Custom Item` | Has a custom item | **Product:** Custom Snowboard<br>**Customer:** Russell Winfield<br>**Location:** Shop location |
| `International Market` | Placed from a single-country market with an associated price list | **Market:** Country<br>**Product:** The Complete Snowboard (Ice)<br>**Location:** Shop location |
| `Line Item Discount` | Has a line item discount | **Product:** The Complete Snowboard (Ice)<br>**Customer:** Karine Ruby (On behalf of Snowdevil)<br>**Company:** Snowdevil<br>**Location:** Shop location |
| `Order Discount` | Order Discount | **Product:** The Complete Snowboard (Dawn)<br>**Customer:** Russell Winfield<br>**Location:** Shop location |
| `Line Item Discount`, `Order Discount` | Has a line item and order discount | **Products:** The Complete Snowboard (Powder), The Complete Snowboard (Electric)<br>**Customer:** Russell Winfield<br>**Location:** Shop location |
| `Shipping Discount` | Has a shipping discount | **Product:** The Multi-location Snowboard<br>**Customer:** Karine Ruby (On behalf of Snowdevil)<br>**Company:** Snowdevil<br>**Location:** My Custom Location |
| `Custom Shipping Rate` | Has a custom shipping rate | **Product:** The Complete Snowboard (Sunset)<br>**Customer:** Karine Ruby (On behalf of Snowdevil)<br>**Company:** Snowdevil<br>**Location:** Shop location |
| `Multiple Fulfillments` | Fulfilled through multiple fulfillment providers | **Location:** Shop location<br>**Fulfillment service:** Snow City Warehouse<br>**Products:** The Complete Snowboard (Ice), The 3p Fulfilled Snowboard<br>**Customer:** Russell Winfield |

The following orders are available on development stores created after April 13, 2023:

| Tag | Configuration | Connected resources |
|---|---|---|
| `Edited` | Quantity has been edited | **Product:** The Minimal Snowboard<br>**Location:** Shop location |

---

## Discounts

The generated test data set contains the following discounts:

| Name | Configuration | Connected resources |
|---|---|---|
| Buy three, get 30% off | Automatic discount<br>Applies only to the Complete Snowboard Ice variant | **Product:** The Complete Snowboard (Ice) |
| Buy one, get the second 10% off | Automatic BXGY discount<br>Applies only to the Complete Snowboard Dawn variant | **Product:** The Complete Snowboard (Dawn) |
| CODE_DISCOUNT_BLACKFRIDAY | Basic code discount | — |
| FREESHIPPING2024 | Free shipping code discount | — |
| CODE_BXGY_DISCOUNT_SUMMERBOGO | BXGY code discount | — |

---

## Markets

The generated test data set contains the following markets:

| Name | Configuration |
|---|---|
| Mexico | Pricing: Price decrease of 5% |
| United States | — |
| International | — |

---

## Fulfillment orders

The generated test data set contains the following fulfillment orders:

| Configuration | Connected resources |
|---|---|
| Assigned | **Orders:** Minimal Info, Custom Item, International Market, Line Item Discount, Order Discount, Line Item Discount & Order Discount, Multiple Fulfillments |
| Re-assigned (fulfillment location changed from Shop location to My Custom Location) | **Order:** Shipping Discount |
| On hold | **Order:** Custom Shipping Rate |

---

## Fulfillment services

The generated test data set contains the following fulfillment services:

| Name | Connected resources |
|---|---|
| Snow City Warehouse | **Products (inventory):** The 3p Fulfilled Snowboard, The Multi-managed Snowboard |

---

## Gift cards

The generated test data set contains the following issued gift cards:

> **Note:** Gift card test data is available only on development stores created after April 13, 2023.

| Code ending | Configuration | Connected resources |
|---|---|---|
| `0001` | Remaining: $100<br>Issued: $100 | **Customer:** Ayumu Hirano |

---

## Selling plans

The generated test data set contains the following selling plans.

On live stores, selling plans are created and managed with an app. Products with selling plans generated by the test data allow you to view how selling plans look on the Shopify admin and in the storefront. However, subscription contracts created by checking out with a product with a selling plan won't generate additional orders.

> **Note:** Selling plan test data is available only on development stores created after April 13, 2023.

| Name | Configuration | Connected resources |
|---|---|---|
| Preorder | Preorder ski wax, delivered in a month | **Product:** Selling Plan Ski Wax: Special Selling Plans Ski Wax |
| Prepaid | A year supply of prepaid ski wax, delivered monthly | **Product:** Selling Plan Ski Wax |
| Subscription | Ski wax subscription, billed and delivered weekly | **Product:** Selling Plan Ski Wax |
| Try Before You Buy | Try our product risk-free for a week before needing to pay | **Product:** Selling Plan Ski Wax: Sample Selling Plans Ski Wax |

---

## Metafield definitions

The generated test data set contains the following metafield definitions:

> **Note:** Metafield test data is available only on development stores created after April 13, 2023.

| Name | Configuration | Connected resources |
|---|---|---|
| Alpine sport types | Type: list.single_line_text_field | **Shop** |
| Snowboard length | Type: dimension | **Products:** The Complete Snowboard, The Multi-managed Snowboard |
| Snowboard binding mount | Type: single line text | **Products:** The Collection Snowboard: Hydrogen, The Collection Snowboard: Liquid, The Collection Snowboard: Oxygen |

---

## Metafields

The generated test data set contains the following metafields:

> **Note:** Metafield test data is available only on development stores created after April 13, 2023.

| Name | Connected resources |
|---|---|
| `test_data.alpine_sports` | **Metafield definitions:** Chosen Alpine Sports<br>**Shop** |
| `test_data.snowboard_length` | **Metafield definitions:** Snowboard length<br>**Products:** The Complete Snowboard, The Multi-managed Snowboard |
| `test_data.binding_mount` | **Metafield definitions:** Snowboard binding mount<br>**Products:** The Collection Snowboard: Hydrogen, The Collection Snowboard: Liquid, The Collection Snowboard: Oxygen |
| `test_data.snowboard_weight` | **Product:** Hidden Snowboard |

---

## Themes

The generated test data set contains the following themes. Your theme architecture version determines the file types that make up your theme, the ways that you can customize your theme, and the ways that apps can integrate with your theme. The provided themes should only be used in development stores for testing purposes.

> **Note:** Themes are available only on development stores created after April 13, 2023.

| Name | Configuration |
|---|---|
| Test Data | Online Store 2.0 theme |
| Debut (vintage theme) | Vintage theme |

---

## Collaborator accounts

> Fonte: https://shopify.dev/docs/storefronts/themes/tools/collaborator-accounts

# Collaborator accounts

As a Shopify Partner, you can use collaborator accounts to access merchant stores directly through your own Partner Dashboard or using the Shopify app. Collaborator accounts give you access to only the sections of a store that a merchant wants you to access, and don't count toward a store's [staff limit](https://help.shopify.com/manual/your-account/staff-accounts). Any stores that you have access to by using a collaborator account are labeled as **Managed** stores in your Partner Dashboard.

If you're building or customizing a theme for a merchant, then you can use a collaborator account with the **Themes** permission to create and manage themes in the merchant's store.

---

## Prerequisites

To request collaborator access to a store, you need a [Shopify Partner account](https://www.shopify.com/partners).

---

## Limitations

You need to log in to the store through the **Stores** section of your **Partner Dashboard** instead of logging in directly to the store.

---

## Request access

If you want a collaborator account for a client's store, then you need to send a request to the store owner through your Partner Dashboard. You can also send your client [the Shopify Help Center page on collaborator permissions](https://help.shopify.com/manual/your-account/staff-accounts/collaborator-accounts/) to explain how collaborator accounts work.

If you already have a staff account for the client's store or have been invited by the store owner to activate a staff account, but not yet activated it, then your request for a collaborator account prompts the store owner to update your current account permissions to reflect those of your collaborator account.

As an additional layer of security, merchants can set up a 4-digit collaborator request code for their Shopify store. When a store has the code set up, you need to enter the code when you request access as a collaborator. If you enter an incorrect code, then you see an error in the Partner Dashboard and your request isn't sent to the merchant.

1. From your Partner Dashboard, click **Stores**.
2. Click **Add store**.
3. In the **Store type** section, select **Managed store**.
4. Enter the URL of the Shopify store that you want to access.
5. If the Shopify store requires a collaborator request code, then enter the code.
6. In the **Permissions** section, select the sections of the store that you want to access, or check **Full access**. The account owner can change these permissions after your account is created.
7. If you want to include a message to the store owner in your request, then enter a message in the **Add a message** section.
8. Click **Save**.

After you submit a request, the store owner receives an email about the request and a notification on their Shopify Home.

---

## Cancel a pending access request

If you requested access to a store but need to cancel the request, then you can do so through your Partner Dashboard.

1. From your Partner Dashboard, click **Stores**.
2. Beside the store with the access request that you want to cancel, click **Cancel request**.
3. Click **Cancel access request**.

---

## View your managed stores

You can view the stores that you've requested access to on the **Stores** page in your Partner Dashboard. There is no limit to the number of managed stores that you can have, but you can have only up to 10 pending requests open at a time.

If your access to a store is removed, then you can remove the store from your Stores list by clicking **Remove from list**.

---

## Manage access to a store

Partner organizations often have access to multiple development stores and managed stores, and have multiple staff members who perform different tasks in the organization. To increase oversight over your staff members and maintain merchant security, you can limit access to stores in your Partner organization to only the staff members who need to access them. [Learn more about managing access to merchant stores](https://help.shopify.com/en/partners/dashboard/managing-stores/manage-access).

---

## Remove your access to a store

If you no longer need to work on a client's store, then you can remove your access to the store. Removing your access deletes your collaborator account from the store.

If you need to do more work on the store after you remove access, then you'll need to request access to the client's store again.

After your access to a store is removed, you can remove the store from your Stores list by clicking **Remove from list**.

1. From your Partner Dashboard, click **Stores**.
2. Find the store you want to remove your access from in the list.
3. Click **Remove access**, and then click **Remove store**.

---

## Expired access

"Collaborator access to managed stores remains active as long as a user logs into the store at least once every 90 days." If there is no login activity within this period, then Shopify will automatically expire the Partner's access. If you need collaborator access after it has expired, then you can [request access](https://help.shopify.com/partners/dashboard/managing-stores/request-access) again through your Partner Dashboard.

---

## Next steps

* [Create](https://shopify.dev/docs/storefronts/themes/getting-started/create) or [customize](https://shopify.dev/docs/storefronts/themes/getting-started/customize) a theme for the merchant
* [Connect to the merchant's store using Shopify CLI](https://shopify.dev/docs/storefronts/themes/tools/cli/cli-2/commands)
* [Connect to the merchant's store using the Shopify GitHub integration](https://shopify.dev/docs/storefronts/themes/tools/github)

---

## Shopify Theme Inspector for Chrome

> Fonte: https://shopify.dev/docs/storefronts/themes/tools/theme-inspector

# Shopify Theme Inspector for Chrome

The Shopify Theme Inspector for Chrome is a browser plugin that visualizes Liquid render profiling data in a [flame graph](https://www.brendangregg.com/FlameGraphs/cpuflamegraphs.html#FlameGraph). You can use this graph and the profiling data to identify the parts of your theme code that are slowing down an online store.

Even if a theme is designed with performance in mind, apps and customizations made to theme code can cause the online store to slow down. Liquid customizations often contribute to these slowdowns. Slow Liquid templates impact server response times, which increases the time it takes for a page to start rendering.

After you identify the code that's slowing down the store, you can optimize it to make the store faster and convert more visitors.

The Shopify Theme Inspector for Chrome can be used to analyze Liquid on your personal store, or stores that you have [collaborator access](https://shopify.dev/docs/storefronts/themes/tools/collaborator-accounts) to.

Optimizing your Liquid code can improve the experience, conversion rate, and discoverability of an online store. [Learn more about online store and theme performance](https://shopify.dev/docs/storefronts/themes/best-practices/performance).

## Install the Shopify Theme Inspector

The Shopify Theme Inspector for Chrome is available in the [Chrome web store](https://chromewebstore.google.com/detail/shopify-theme-inspector-f/fndnankcflemoafdeboboehphmiijkgp).

## Run the Shopify Theme Inspector

To learn how to run the Shopify Theme Inspector and read the flame graph, refer to [Identify Liquid render issues using Shopify Theme Inspector](https://shopify.dev/docs/storefronts/themes/tools/theme-inspector/using-the-theme-inspector).

---

### Identify Liquid render issues using Shopify Theme Inspector

> Fonte: https://shopify.dev/docs/storefronts/themes/tools/theme-inspector/using-the-theme-inspector

# Identify Liquid render issues using Shopify Theme Inspector

The [Shopify Theme Inspector for Chrome](https://shopify.dev/docs/storefronts/themes/tools/theme-inspector) is a browser plugin that visualizes Liquid render profiling data in a flame graph. This guide teaches you how to run the Shopify Theme Inspector on an online store and identify common Liquid render issues using the flame graph.

---

## Running the Shopify Theme Inspector

To run the Shopify Theme Inspector on a store, you need to have the **Themes** [staff permission](https://help.shopify.com/manual/your-account/staff-accounts/staff-roles/permissions/permissions-descriptions#online-store-permissions) or a [collaborator account](https://help.shopify.com/manual/your-account/staff-accounts/security/collaborator-accounts) with the same permission. To verify that you have this permission, make sure that you can view the [Themes page](https://admin.shopify.com/themes) in the store's admin.

1. Navigate to the Shopify store that you want to analyze.

   If you have collaborator access for the store that you want to analyze, then you need to open the store from your Partner Dashboard.

2. From Google Chrome's extension area, click the **Shopify Theme Inspector for Chrome** icon.

3. Click **Sign In**, and then log in using your Shopify login.

   If you have collaborator access to the store that you want to analyze, then log in using the Partner account that has collaborator access to the store.

4. Open [Chrome DevTools](https://developer.chrome.com/docs/devtools/) and then select the **Shopify** tab. If the tab isn't visible, then click the `>>` button to check for it in the overflow list. This tab is only available when you are viewing a Shopify store.

5. Navigate to a page in the store that you want to profile.

6. To generate a flame graph for the page, click the `⟳` or **Load Profile** button.

---

## Understanding the flame graph

The Shopify Theme Inspector generates a flame graph that represents when each node of Liquid ran and how long each node took to run.

Starting from the top of the stack, the timeline represents the total sequence of events and total time taken to render the page.

Hover over the timeline and select a specific section to zoom in on.

The total rendering time isn't equivalent to the Time to First Byte (TTFB) as it doesn't include additional overheads, such as the time it takes for a user's request to reach Shopify's backend. For most users, this extra overhead should be less than 100ms.

Click on the relevant bar in the flame graph to learn more about each node. The following information is displayed, when available:

* **Time**: The time it took for the server to render the highlighted node, including any child nodes.
* **Percentage**: The percentage of the total time that the highlighted node took to render.
* **`tag:`, `variable:`**: Whether the highlighted node represents a Liquid tag or variable.
* **Code snippet**: The code that the server resolved.
* **Filename and line number**: The filename and line number where the code exists.

**Note:**

Render times might vary slightly each time that a page is profiled. This is due to optimizations in Shopify's infrastructure.

---

## Sandwich view

The Shopify Theme Inspector includes a sandwich view that aggregates the "Self" times for each node, displaying the sum of their execution times excluding their children, as well as the "Total" time, which includes the execution times of their children. This feature is useful for identifying which nodes contribute most to your page's rendering time.

For example, you might notice that certain nodes, like `filter:image_url`, have a quick execution time of approximately 50μs (0.05ms) each but are executed as many as 2000 times. This repetitive execution significantly extends the overall render time, highlighting areas where optimization might be necessary.

---

## What to look for when debugging

Below are some trends that you can observe in the Shopify Theme Inspector flame graph and their implications for your theme's performance.

**Tip:**

When identifying code that's slowing down a store, you should weigh the benefits of the related feature against its impact on the speed of the store. You might need to make some speed tradeoffs to build a user experience that leads to more sales.

### Too many nodes or deeply nested nodes

Some nodes are fast, but execute hundreds or thousands of times. This adds rendering time and increases your overall TTFB. The profile view supports the **Find** shortcut (`Control+F` or `Command+F`) to give you a count of how many times a node is executed.

Similarly, if your flame graph has many layers of nested nodes, then your code might not be optimized. Below are some of the common causes of nested nodes. Your code might contain a combination of these causes.

* Too many conditionals
* Nested loops
* Nested includes

### Complex operations inside of loops

Doing complex operations inside of a loop has adverse effects on Liquid render time. In some cases, you can simplify template logic and restructure the code to significantly improve Liquid performance.

In the example below, an `assign` tag is nested in a `for` loop. The code loops through the products in the collection and creates a list of `products_by_price` with each iteration. The code is unnecessarily repetitive because the value of `products_by_price` does not change per product.

```liquid
{%- for product in collection.products -%}
{% assign products_by_price = collection.products | sort: "price" %}


// some liquid code
{%- endfor -%}
```

You can simplify the code to only generate `products_by_price` once, as in the example below. In this example, the sorting of prices happens only once and can still be accessed within the loop when needed.

```liquid
{% assign products_by_price = collection.products | sort: "price" %}


{%- for product in collection.products -%}
   // some liquid code
{%- endfor -%}
```

### Non-visual sections

These sections could be for things like scripts, SEO, analytics, and more. Evaluate whether these sections are necessary or refactor them so they become more efficient.

---

## Troubleshooting

### Can I profile any Shopify store I want?

No, you can only profile a store in the following cases:

* The store is linked to your [Shopify ID](https://help.shopify.com/manual/your-account/logging-in/sso-migration-guide).

* You have a collaborator account for the store.

* The store is not a development store.

To run the Shopify Theme Inspector on a store, you need to have the **Themes** [staff permission](https://help.shopify.com/manual/your-account/staff-accounts/staff-roles/permissions/permissions-descriptions#online-store-permissions) or a [collaborator account](https://help.shopify.com/manual/your-account/staff-accounts/security/collaborator-accounts) with the same permission. To verify that you have this permission, make sure that you can view the [Themes page](https://admin.shopify.com/themes) in the store's admin.

### I can't see the Shopify tab in Chrome Dev​Tools

The **Shopify** tab only appears when you are viewing a Shopify store.

### This page cannot be profiled

You might see a **This page cannot be profiled** error in the following cases:

* Your account doesn't have access to the store that you're trying to profile.
* You're trying to profile a checkout page, which isn't supported by this extension.
* There was an unhandled error in the request, such as a timeout or a lost connection.

---

## Shopify Lighthouse CI GitHub Action

> Fonte: https://shopify.dev/docs/storefronts/themes/tools/lighthouse-ci

# Shopify Lighthouse CI GitHub Action

Optimizing your theme for [performance](https://shopify.dev/docs/storefronts/themes/best-practices/performance) is key to the success of the merchants that you support, and the experience of their customers. It directly influences conversion rates, repeat business, and search engine rankings.

Every change you make to your theme code can have an impact on performance. To make sure that you identify code that is slowing down your theme before it is in production, you can integrate Lighthouse tests into your theme development workflow using the Shopify Lighthouse CI GitHub Action.

The Shopify Lighthouse CI GitHub Action is a Shopify-specific GitHub Action based off of Google's [Lighthouse CI](https://github.com/googleChrome/lighthouse-ci). It runs a Lighthouse audit as part of your continuous integration process for every pull request that you create. It tests the performance of your theme's home page, a product page, and a collection page.

In this tutorial, you'll learn how to implement the Shopify Lighthouse CI GitHub Action and, optionally, add a status check for the action to GitHub.

---

## Requirements

* **A development store** - You should create a [development store](https://shopify.dev/docs/storefronts/themes/tools/development-stores) that is dedicated to running Lighthouse CI and manual performance tests.
* **Performance-specific store data** - To get consistent results from Lighthouse, you should [populate your store](https://help.shopify.com/manual/products/import-export/import-products) using the [test product csv](https://shopify.dev/csv/theme-performance-shop-product-data.csv). The store should have no other collections, products, or variants. This file contains the same data that is used to test themes before they are accepted into the [Shopify Theme Store](https://shopify.dev/docs/storefronts/themes/store).
* **API credentials for the development store** - Lighthouse CI uses a [Dev Dashboard app](https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard) to connect to your store. Create an app with the `read_products` and `write_themes` access scopes, install it on your store, and copy the `client_id` and `client_secret` from the app credentials.

---

## Step 1: Add your app credentials to GitHub

In your theme's GitHub repo, add the following information as [repository secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository):

* `SHOP_CLIENT_ID` - The client ID from your Dev Dashboard app.
* `SHOP_CLIENT_SECRET` - The client secret from your Dev Dashboard app.
* `SHOP_STORE` - Your store's [myshopify.com URL](https://help.shopify.com/manual/domains), in the format `your-store-name.myshopify.com`.

If your store is password protected, then you should also add a repository secret that contains your store password. If you don't provide it, then Lighthouse is redirected to the password page and can't accurately test your theme's performance.

---

## Step 2: Create a new GitHub Action workflow

1. Create a new GitHub Action workflow file that runs `shopify/lighthouse-ci-action`:

   ```yml
   name: Shopify Lighthouse CI
   on: [push]
   jobs:
     lhci:
       name: Lighthouse
       runs-on: ubuntu-latest
       steps:
       - uses: actions/checkout@v4
       - name: Lighthouse
         uses: shopify/lighthouse-ci-action@v1
         with:
           client_id: ${{ secrets.SHOP_CLIENT_ID }}
           client_secret: ${{ secrets.SHOP_CLIENT_SECRET }}
           store: ${{ secrets.SHOP_STORE }}
           password: ${{ secrets.SHOP_PASSWORD }}
   ```

2. Commit this code and create a pull request. You should see a GitHub Action that runs Lighthouse on your pull request's code.

---

## Step 3: Add Lighthouse CI as a GitHub status check (optional)

GitHub status checks let you see the status of your Lighthouse CI run in the GitHub UI. If you want to turn the performance and accessibility checks into [GitHub status checks](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-status-checks), then do the following:

1. Install the [Lighthouse CI GitHub app](https://github.com/apps/lighthouse-ci) as the owner of your theme's repo, and then copy the token provided.

2. In your theme's GitHub repo, create a new [repository secret](https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository) named `LHCI_GITHUB_APP_TOKEN`. The value should be the token from the previous step.

3. In the GitHub Action workflow file that you created in [step 2](#step-2-create-a-new-github-action-workflow), add a new configuration attribute called `lhci_github_app_token`. The attribute's value should be a reference to the `LHCI_GITHUB_APP_TOKEN` secret:

   ```yml
   name: Shopify Lighthouse CI
   on: [push]
   jobs:
     lhci:
       name: Lighthouse
       runs-on: ubuntu-latest
       steps:
       - uses: actions/checkout@v4
       - name: Lighthouse
         uses: shopify/lighthouse-ci-action@v1
         with:
           client_id: ${{ secrets.SHOP_CLIENT_ID }}
           client_secret: ${{ secrets.SHOP_CLIENT_SECRET }}
           store: ${{ secrets.SHOP_STORE }}
           password: ${{ secrets.SHOP_PASSWORD }}
           lhci_github_app_token: ${{ secrets.LHCI_GITHUB_APP_TOKEN }}
   ```

4. Commit this code and create a pull request. You should see a GitHub Action that runs Lighthouse on your pull request's code.

Your PRs will now pass or fail depending on whether they pass the Lighthouse CI checks.

---

## Arguments

The Shopify Lighthouse CI GitHub Action accepts the following arguments in the workflow configuration:

| Attribute | Description | Required |
| - | - | - |
| `client_id` | The client ID from your Dev Dashboard app. Provide together with `client_secret`. Required unless using `access_token`. | yes |
| `client_secret` | The client secret from your Dev Dashboard app. Provide together with `client_id`. Required unless using `access_token`. | yes |
| `access_token` | A legacy custom app Admin API access token. Use this only for apps created before January 2026. Required unless using `client_id` and `client_secret`. | yes |
| `store` | Your store's [myshopify.com URL](https://help.shopify.com/manual/domains), in the format `{shop}.myshopify.com`. | yes |
| `password` | The [password](https://shopify.dev/docs/storefronts/themes/tools/development-stores#sharing-your-development-store) for your store. Required for password-protected stores such as development stores. | no |
| `product_handle` | The product [handle](https://shopify.dev/docs/api/liquid/basics#handle) to run the product page Lighthouse test on. If no handle is specified, then the first product is used. | no |
| `theme_root` | The root directory of where theme files are uploaded in the repository. If a root directory isn't specified, then the root directory of the repository is used. | no |
| `collection_handle` | The collection [handle](https://shopify.dev/docs/api/liquid/basics#handle) to run the collection page Lighthouse test on. If no handle is specified, then the first collection is used. | no |
| `pull_theme` | The ID or name of a theme from which the settings and JSON templates should be pulled. If provided, those settings will be pulled into the development theme. If not provided, the default settings for the theme will be used. | no |
| `lhci_min_score_performance` | The minimum performance score for a Lighthouse audit to be marked as passed. This value must be a decimal number between 0 and 1. The default value is 0.6. | no |
| `lhci_min_score_accessibility` | The minimum accessibility score for a Lighthouse audit to be marked as passed. This value must be a decimal number between 0 and 1. The default value is 0.9. | no |

### Accepted tokens for GitHub status checks

You need to provide one of the following tokens to log Lighthouse CI runs as GitHub status checks. To understand the difference between the two token types, refer to the [Lighthouse CI documentation](https://github.com/GoogleChrome/lighthouse-ci/blob/main/docs/getting-started.md#github-status-checks).

| Attribute | Description |
| - | - |
| `lhci_github_app_token` | A token for the [Lighthouse GitHub app](https://github.com/apps/lighthouse-ci) to access the repo. |
| `lhci_github_token` | A GitHub personal access token. |

---

## Pagine non catturate

Nessuna pagina della sezione "Developer tools" è stata saltata o non catturata. Tutte le voci della sidebar e le relative pagine figlie sono state estratte.

Note sulle voci della sidebar:

- **Shopify CLI** — la voce di sidebar "Shopify CLI" punta al riferimento comandi `https://shopify.dev/docs/api/shopify-cli/theme` (sezione API, fuori dall'albero `/themes/tools/`). Il riferimento completo dei singoli comandi (es. `theme dev`, `theme push`, `theme pull`, `theme publish`, ecc.) non è stato espanso pagina-per-pagina perché risiede nella sezione API reference e non nella sezione Tools. Pagina indice di riferimento: https://shopify.dev/docs/api/shopify-cli/theme
- **Shopify CLI 2.x** e **Theme Kit** — elencati nell'overview come "Legacy tools". Non fanno parte dello scope principale "Developer tools" moderno richiesto e non sono stati estratti come capitoli a sé. URL: https://shopify.dev/docs/storefronts/themes/tools/cli/cli-2/commands e https://shopify.dev/docs/storefronts/themes/tools/theme-kit
- **Imagery** — strumento "per imparare Liquid", elencato nell'overview ma fuori dallo scope "Developer tools".
