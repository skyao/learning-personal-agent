来源：https://poke.com/docs/creating-recipes
取文：2026-11-09，直接下载

Creating Recipes

## Overview

Kitchen is where you create, publish, and track your own Poke recipes.

A recipe bundles:

- onboarding context and first-message behavior
- required integrations (MCP templates)
- a share/install link for users

## Before You Start

- A Poke account with Kitchen access at [poke.com/kitchen](https://poke.com/kitchen)
- For CLI workflows: Node.js 18+ and the `poke` npm package (run through `npx poke@latest`)

## Create a Recipe in Kitchen

### Open the wizard

Go to [poke.com/kitchen](https://poke.com/kitchen) and click **Create recipe**.

### Complete Basics

Set a recipe name. Description is optional.

### Configure Onboarding

Optionally set:

- **What context Poke needs from the user** (`inputContext`)
- **Prefilled first message** (`prefilledFirstText`)

### Select Integrations

Choose required integrations from the picker.

If an integration supports local credential sharing, you can mark it as shared so users don't need to set it up themselves.

## Manage a Recipe

From **Kitchen -> Recipes -> your recipe**, you can:

- edit onboarding context and prefilled first message
- change required integrations and credential sharing settings

For published recipes, changes will only affect new sign-ups.

## Publish and Share

Publishing a recipe:

- marks it **Published**
- generates a referral/share link
- makes it eligible for payouts

You will typically share links like:

- `https://poke.com/r/<referralCode>`

---

## How `npx poke` Fits In

The `poke` npm package helps you bring integrations into your account and, with `--recipe`, can bootstrap a shareable recipe flow.

Package: [npmjs.com/package/poke](https://www.npmjs.com/package/poke)

### 1) Authenticate CLI

```
npx poke@latest login
```

This opens your browser for authentication. Enter the code shown in your terminal to log in.

Other auth commands:

```
npx poke@latest logout   # Clear stored credentials
npx poke@latest whoami   # Display current user info
```

### 2) Add or expose an MCP integration

```
# Remote MCP server
npx poke@latest mcp add https://mcp.example.com/sse -n "My Server"
 
# With API key authentication
npx poke@latest mcp add https://mcp.example.com/sse -n "My Server" -k "sk-your-api-key"
 
# Local MCP server over tunnel
# The tunnel only forwards the port — start your MCP server first, then tunnel it:
npx poke@latest tunnel http://localhost:3000/mcp -n "Local Dev MCP"
```

The tunnel **only forwards the local port** — it does not start or manage the MCP server itself. Start your server first, then run the tunnel command pointing at it.

The tunnel stays active until you press `Ctrl+C`. Tools are synced automatically every 5 minutes.

Then open Kitchen and select that integration in your recipe.

Some MCP servers require OAuth and must be added through the web app integrations flow instead of CLI.

### 3) Create a shareable recipe from CLI (`--recipe`)

```
npx poke@latest tunnel http://localhost:3000/mcp -n "Local Dev MCP" --recipe
```

With `--recipe`, the CLI creates a connection and returns a recipe link and QR code in the terminal. The recipe can then be managed further in Kitchen.

The tunnel must stay active for shared users to access your local server. If you stop the tunnel, the connection will go offline.

### CLI configuration

Credentials are stored at `~/.config/poke/credentials.json` (or `$XDG_CONFIG_HOME/poke/credentials.json` if set). The CLI defaults to `https://poke.com` and can be overridden with environment variables:

| Variable | Default | Description |
| --- | --- | --- |
| `POKE_API` | `https://poke.com/api/v1` | Backend API base URL |
| `POKE_FRONTEND` | `https://poke.com` | Frontend base URL |

---

## Payouts and Operations

Kitchen also includes **Payouts** where you can:

- view unique-user totals and lifetime earnings
- set your payout destination (Venmo phone/email/handle)
- review payout history
