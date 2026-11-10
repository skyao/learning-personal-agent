来源：https://poke.com/docs/managing-integrations
取文：2026-11-09，直接下载

Managing Integrations

## Overview

Integrations let you connect your favorite apps and services to Poke. Once connected, Poke can access information and perform actions across apps and services through natural conversation.

The easiest way to add an integration is to use a **Recipe** - a prebuilt template that handles the integration and gives Poke a useful starting behavior (e.g. "summarize my assigned Linear issues every morning").

## Adding an Integration

### Browse Recipes

Go to [poke.com/recipes](https://poke.com/recipes) to browse all first-party and approved third-party recipes. You'll find prebuilt recipes for popular services:

- **Linear** - Automate issue and project management
- **Todoist** - Create and edit tasks and projects
- **Notion** - Read and write pages and databases
- **Asana** - Manage tasks and project workflows
- **GitHub** - Manage code and repositories
- **DeepWiki** - Search and navigate documentation
- **Sentry** - Track errors and performance
- **Vercel** - Deploy and manage web applications
- **Netlify** - Deploy and manage web applications
- **Supabase** - Manage databases and backend services
- **Ramp** - Analyze spend and financial data
- **Webflow** - Design and deploy websites visually
- More coming soon!

Filter by category or search for the service you want.

### Use the Recipe

Open a recipe and click **Get Started**. Poke will walk you through any auth steps (OAuth, API key, etc.) and connect the underlying integration for you.

### Start using it

Your integration is now active! Try asking Poke something like:

- "What do I have due today in Linear and Todoist?"
- "When was the last Vercel deployment on my portfolio website?"
- "How much was my last Ramp transaction?"
- "What's the status of pull request #123?"
- "Create a Notion page summarizing this week's to-dos"
- "Find documentation on React hooks in DeepWiki"
- Or anything else your connected integrations support!

## Managing Your Integrations

Visit [poke.com/integrations](https://poke.com/integrations) to view and manage everything you've connected.

### View Connected Integrations

1. Go to [poke.com/integrations](https://poke.com/integrations)
2. View all active integrations and connected accounts
3. Select one to see more details or manage it

### Disconnect an Integration

1. Go to [poke.com/integrations](https://poke.com/integrations)
2. Find the integration
3. Click on it
4. Click "Disconnect from Poke"

### Reconnect or Refresh

If an integration stops working:

1. Go to [poke.com/integrations](https://poke.com/integrations)
2. Look for error indicators
3. Click on the integration
4. Click "Retry Connection" or "Refresh Connection"
5. Re-authenticate if needed

## Custom Integrations (Advanced)

If the service you want isn't available as a Recipe, you can connect any MCP-compatible server directly:

1. Go to [poke.com/integrations/new](https://poke.com/integrations/new)
2. Enter the integration **Name**
3. Enter the **MCP Server URL** (e.g., `https://mcp.example.com/sse`)
4. Add an **API Key** if the service requires authentication (optional)
5. Click **Create Integration**

If you provide an API key, it will be used for authentication. Leave it empty
unless your integration needs it.

## Tips for Using Integrations

**Be specific** - Mention the integration name or functionality to ensure it's invoked.

**Start simple** - Connect one or two integrations first, learn how they work, then add more.

**Keep them updated** - If an integration stops working, try refreshing it before disconnecting/reconnecting.
