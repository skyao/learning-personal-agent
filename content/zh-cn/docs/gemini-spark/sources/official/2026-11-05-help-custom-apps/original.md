来源：https://support.google.com/gemini/answer/17209137?hl=en
取文：2026-11-06，直接下载

You can connect your personal or third-party apps to build highly customized workflows in tasks or take quick actions in chat. To do this, add a custom app with its Model Context Protocol (MCP) server URL in the Gemini web app. After it’s connected, you can use the custom connected app in both the Gemini mobile app and Gemini web app.

**For developers:** You can integrate your app and MCP server with Google’s agentic products, like Gemini Apps, using the new [Connected Apps Platform](https://developers.google.com/connected-apps). You can also debug, validate schemas, and test your custom apps with [Gemini Developer Mode](https://developers.google.com/connected-apps/mcp/dev-mode).

## What you need

To connect a custom app to Gemini Apps, you must:

- **Be 18 or over and in the US.**
- **Sign in to the Gemini app with a personal Google Account.** For now, this feature isn’t available if you sign in with a work or school Google Account. [Learn how to sign in to Gemini Apps](https://support.google.com/gemini/answer/13278668).
- **Have [Keep Activity](https://myactivity.google.com/product/gemini?utm_source=help) on.** Custom apps are unavailable when this setting is off.
- **Have the MCP server URL for the custom app.** The MCP server must follow the standard MCP specifications.

**Important:** For now, custom Connected Apps are:

- Only available in English.
- Only available in the Gemini mobile app and the Gemini web app at [gemini.google.com](https://gemini.google.com).

## Before you connect a custom app

Google does not control, monitor, or secure third-party MCP servers. You’re responsible for supervising the MCP server. Make sure you understand the actions an MCP server supports and trust the provider before connecting it to Gemini Apps.

[Learn more about the risks of connecting custom apps](#risks).

## Connect a custom app

**Important:** You can only connect custom apps in the Gemini web app. Once connected, they’re available on both the Gemini mobile app and Gemini web app.

You can add a custom app by linking its MCP server in your [Connected Apps settings](https://gemini.google.com/apps).

1. On your computer, go to [gemini.google.com](https://gemini.google.com).
2. At the bottom, click Settings ![](images/img-01-1c0260.png) ![and then](images/img-02-bfcdbc.png) **Connected Apps** ![](images/img-03-aa3481.png).

   - If you don’t find “Connected Apps,” first click **Personal Intelligence** ![and then](images/img-02-bfcdbc.png) **Connected Apps**. [Learn about Personal Intelligence and Connected Apps](https://support.google.com/gemini/answer/16598406).
3. Under "Custom apps," find the “Add a custom app link to get started” field, or if you already connected a custom app, click **Add a custom app** ![](images/img-04-e8b4c8.png).
4. Enter the app’s MCP server URL.
   - If the server doesn’t support Dynamic Client Registration, next to “Advanced features,” click **Show more**, then enter your credentials.
5. Click **Next**.
6. Follow the on-screen instructions.

**Tips:**

- To make sure Gemini uses your connected custom app for a prompt, enter `@` and select the custom app.
- To debug, validate schemas, and test your custom apps, try [Gemini Developer Mode](https://gemini.google.com/devmode). [Learn more about Gemini Developer Mode](https://developers.google.com/connected-apps/mcp/dev-mode).

## Disconnect a custom app

1. On your computer, go to [gemini.google.com](https://gemini.google.com).
2. At the bottom, click Settings ![](images/img-01-1c0260.png) ![and then](images/img-02-bfcdbc.png) **Connected Apps** ![](images/img-03-aa3481.png).

   - If you don’t find “Connected Apps,” first click **Personal Intelligence** ![and then](images/img-02-bfcdbc.png) **Connected Apps**. [Learn about Personal Intelligence and Connected Apps](https://support.google.com/gemini/answer/16598406).
3. Under "Custom apps," find the app you want to disconnect and turn it off ![](images/img-05-923460.png).
4. Follow any on-screen instructions.

## Unlink an MCP server from your Google Account

You can unlink an MCP server from your Google Account and revoke its permissions in your [Connected Apps settings](https://gemini.google.com/apps). This also disconnects the custom app so that Gemini can’t use it, but doesn’t remove it from your Connected Apps settings. You can reconnect the custom app anytime by relinking the MCP server.

1. On your computer, go to [gemini.google.com](https://gemini.google.com).
2. At the bottom, click Settings ![](images/img-01-1c0260.png) ![and then](images/img-02-bfcdbc.png) **Connected Apps** ![](images/img-03-aa3481.png).

   - If you don’t find “Connected Apps,” first click **Personal Intelligence** ![and then](images/img-02-bfcdbc.png) **Connected Apps**. [Learn about Personal Intelligence and Connected Apps](https://support.google.com/gemini/answer/16598406).
3. Under "Custom apps," find the custom app that you want to disconnect.
4. Click **More details** ![and then](images/img-02-bfcdbc.png) **Disconnect**.

**Tip:** You can also unlink an MCP server from your [Google Account’s Linked apps page](https://myaccount.google.com/linkedapps). [Learn how to manage linked apps](https://support.google.com/accounts/answer/13533235#link_account).

## Remove a custom connected app

If you no longer want Gemini to use a custom connected app, you can remove it. When you remove a custom app, it also unlinks the MCP server from your Google Account.

1. On your computer, go to [gemini.google.com](https://gemini.google.com).
2. At the bottom, click Settings ![](images/img-01-1c0260.png) ![and then](images/img-02-bfcdbc.png) **Connected Apps** ![](images/img-03-aa3481.png).

   - If you don’t find “Connected Apps,” first click **Personal Intelligence** ![and then](images/img-02-bfcdbc.png) **Connected Apps**. [Learn about Personal Intelligence and Connected Apps](https://support.google.com/gemini/answer/16598406).
3. Under "Custom apps," find the custom app that you want to remove.
4. Click **More details** ![and then](images/img-02-bfcdbc.png) **Remove app**.
5. Follow the on-screen instructions.

## Understand risks of connecting custom Connected Apps

Custom third-party Model Context Protocol (MCP) servers, or custom connected apps, extend Gemini's capabilities. But, it’s important to understand the associated risks and data privacy considerations:

- **Outside Google’s control:** Google does not control, monitor, or secure custom third-party MCP servers. After your data leaves Gemini and is sent to a custom connected app, it’s subject to that app's privacy practices. Currently, Gemini requires manual confirmation for any write actions, but Gemini can make mistakes. This is why it’s very important that you know and trust the custom third-party MCP server before connecting.
- **Your responsibility:** Because custom third-party MCP servers operate outside of Google's control, we recommend that you do not connect them unless you trust the underlying application. Supervise these closely. Always verify that you trust the provider and review their Privacy Policy and Terms of Service, which explain how they will use your data, before connecting.
- **Excessive data requests:** Custom apps may request data beyond what is strictly needed for your request. This can include data you consider sensitive so pay attention to what data is being written into these servers.
- **Data sharing:** When you use a custom connected app, Gemini may share information from your chat and other available sources, like Connected Apps, Personal Intelligence, skills, tasks, and logged-in websites. This introduces risks of unintended data exposure or unauthorized account access, even for servers that are not malicious.

## What you can do to protect your data

- **Thoroughly review:** Make sure you trust the third-party. Read the app's Privacy Policy, Terms of Service, and available documentation before connecting so that you understand how it works.
- **Monitor and remove:** Regularly review your custom Connected Apps. If you no longer need a custom connected app, disconnect and remove it from Gemini to revoke access.

[Learn how Google helps you share data safely using Google Account Linking](https://support.google.com/accounts/answer/13867826).

For more general privacy information, review the [Gemini Apps Privacy Hub](https://support.google.com/gemini/answer/13594961#extensions).

## Related resources

- [Gemini Apps Privacy Hub](https://support.google.com/gemini/answer/13594961)
- [Manage your tasks & workflows in Gemini Apps](https://support.google.com/gemini/answer/17094507)
- [Manage links between your Google Account & apps from other developers](https://support.google.com/accounts/answer/13533235)
- [Use & manage Connected Apps in Gemini](https://support.google.com/gemini/answer/13695044)
