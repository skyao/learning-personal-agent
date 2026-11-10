来源：https://poke.com/docs/mcp-servers
取文：2026-11-09，直接下载

MCP Servers

## Overview

Poke supports [Model Context Protocol (MCP)](https://modelcontextprotocol.io) servers, allowing you to extend Poke with custom tools and data sources. When you connect an MCP server, Poke can discover and call the tools it exposes during conversations.

## Connecting an MCP Server

You can connect an MCP server to Poke in three ways:

### Via the Web App

### Go to Integrations

Visit [poke.com/integrations/new](https://poke.com/integrations/new).

### Enter Server Details

Provide a **Name** and the **MCP Server URL** (e.g., `https://mcp.example.com/sse`). Add an **API Key** if required.

### Create

Click **Create Integration**. Poke will connect and discover available tools.

### Via the CLI

```
# Remote MCP server
npx poke@latest mcp add https://mcp.example.com/sse -n "My Server"
 
# With API key authentication
npx poke@latest mcp add https://mcp.example.com/sse -n "My Server" -k "sk-your-api-key"
 
# Local server via tunnel
npx poke@latest tunnel http://localhost:3000/mcp -n "Local Dev MCP"
 
# Tunnel with OAuth client credentials (for servers without DCR)
npx poke@latest tunnel http://localhost:3000/mcp -n "My OAuth Server" --client-id "your-id" --client-secret "your-secret"
```

The tunnel forwards your local port so Poke can reach it. Start your MCP server first, then run the tunnel command. The tunnel stays active until you press `Ctrl+C`.

### Via a Prefilled Link

If you're building an integration for others to use, consider [creating a recipe](https://poke.com/docs/creating-recipes) instead of sharing a raw prefilled link. With a recipe, you can update the server URL or configuration later without asking users to re-add the integration, and you earn revenue from MCP usage by users who install your recipe.

You can create a link that prefills the integration form, making it easy to share setup instructions with others:

```
https://poke.com/integrations/new?name=My%20Server&url=https://mcp.example.com/sse&apiKey=sk-your-api-key
```

| Parameter | Description | Required |
| --- | --- | --- |
| `name` | Integration display name | No |
| `url` | MCP server URL | No |
| `apiKey` | API key for authentication | No |

All parameters are optional — any provided values will be prefilled in the form, and users can edit them before submitting.

### OAuth Servers Without Dynamic Client Registration

If your MCP server requires OAuth but does not support [Dynamic Client Registration (DCR)](https://datatracker.ietf.org/doc/html/rfc7591), you can provide the client ID and secret in two ways:

**Via the CLI:** pass `--client-id` and `--client-secret` to the `tunnel` command (see above).

**Via Kitchen:** for hosted servers that don't need a tunnel:

### Create a Template

Go to [poke.com/kitchen](https://poke.com/kitchen) and click **New Template**. Enter the MCP server URL along with the OAuth **Client ID** and **Client Secret**.

### Create a Recipe

Create a recipe that includes the template you just set up as a required integration.

### Add the Integration

Install the integration through the recipe. Poke will handle the OAuth flow for each user who connects.

MCP servers that support Dynamic Client Registration (DCR) work automatically. Just add them via the web app or CLI. The flows above are only needed for OAuth servers that do not support DCR.

## What Poke Sends to Your Server

When Poke makes requests to your MCP server, it includes the following:

### Authentication

If you configured an API key or OAuth credentials, Poke includes an `Authorization` header on every request.

```
Authorization: Bearer {access_token}
```

### User Identification

Poke includes an `X-Poke-User-Id` header on every request. This is a unique identifier for the Poke user making the request.

```
X-Poke-User-Id: 00000000-0000-0000-0000-000000000000
```

You can use this header for:

- **Per-user rate limiting**
- **User-scoped data access**: return different results depending on which user is asking
- **Audit logging**: track which user triggered each request

### Example Request

```
POST /mcp HTTP/1.1
Host: mcp.example.com
Authorization: Bearer {access_token}
X-Poke-User-Id: 00000000-0000-0000-0000-000000000000
Content-Type: application/json
```

## Building an MCP Server

Any server implementing the [MCP specification](https://modelcontextprotocol.io) works with Poke. Popular frameworks include:

- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)

Your server exposes **tools** that Poke can discover and call. Each tool has a name, description, and input schema that Poke uses to decide when and how to invoke it.

You can re-sync your server's tool list at any time from the integrations page or by calling the sync endpoint. Poke also syncs tools automatically when a connection is first created or re-authenticated.
