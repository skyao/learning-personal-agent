来源：https://poke.com/docs/api
取文：2026-11-09，直接下载

Poke API

## Overview

The Poke API allows you to send messages programmatically from your applications, scripts, and automation tools. Messages sent via the API are processed by Poke with full access to email, calendar, reminders, and connected integrations.

**Use cases:**

- Desktop tools and browser extensions
- Automated triggers (CI/CD, webhooks, monitoring)
- Event-driven workflows (GitHub Actions, scheduled tasks)
- Bridging services without native integrations

## How It Works

Your script/tool → Poke API → Your assistant receives it → Takes action

The message appears in your Poke conversation and gets processed just like you texted it - but triggered programmatically.

## Get Your API Key

### Open Kitchen

Go to [Kitchen](https://poke.com/kitchen) and navigate to **API Keys**.

### Create API Key

Click **Add API Key** and name it (e.g., "Desktop Tools" or "GitHub Actions").
Keep it secure - anyone with your key can send messages to your Poke.

### Save It

Copy immediately - you won't see it again. Store it in a password manager or environment variable.

The legacy endpoint `POST /api/v1/inbound-sms/webhook` is deprecated. It only works with V1 API keys (`pk_`-prefixed) created in the Poke app (Settings → Advanced).

The new endpoint `/api/v1/inbound/api-message` requires a **V2 API key** created in [Kitchen](https://poke.com/kitchen). Existing `pk_` keys will not work with the new endpoint — you must create a new key in Kitchen.

## Send a Message

```
POST https://poke.com/api/v1/inbound/api-message
```

**Headers:**

- `Authorization: Bearer YOUR_API_KEY`
- `Content-Type: application/json`

**Body:**

Any JSON object. The entire body is forwarded to your agent as context.

```
{
  "message": "Your instruction or question here"
}
```

### Quick Example

```
curl 'https://poke.com/api/v1/inbound/api-message' \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"message": "Email the team our Q1 numbers and schedule a review call next week"}'
```

```
import requests
import os
 
API_KEY = os.environ['POKE_API_KEY']
 
requests.post(
    'https://poke.com/api/v1/inbound/api-message',
    headers={
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    },
    json={'message': 'Your instruction here'}
)
```

```
const response = await fetch("https://poke.com/api/v1/inbound/api-message", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${process.env.POKE_API_KEY}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    message: "Your instruction here",
  }),
});
```

### Response

```
{
  "success": true,
  "message": "Message sent successfully"
}
```

**`success`** *(boolean)* — Whether the message was delivered to your Poke

## When to Use This

### Desktop Capture

You're on your laptop, working in a browser or IDE. You want to send something to Poke without pulling out your phone.

**Example: Browser extension**

```
// Select text on webpage → right-click → "Send to Poke"
const selectedText = window.getSelection().toString();
const pageUrl = window.location.href;
 
fetch("https://poke.com/api/v1/inbound/api-message", {
  headers: {
    Authorization: `Bearer ${apiKey}`,
    "Content-Type": "application/json",
  },
  method: "POST",
  body: JSON.stringify({
    message: `Summarize this article and email key points to my team:\n\n${selectedText}\n\nSource: ${pageUrl}`,
  }),
});
```

### Event-Driven Automation

Services like GitHub, CI/CD pipelines, or monitoring tools can trigger Poke when something happens.

**Example: GitHub Action on failed deploy**

```
# .github/workflows/deploy.yml
- name: Alert via Poke
  if: failure()
  run: |
    curl 'https://poke.com/api/v1/inbound/api-message' \
      -H "Authorization: Bearer ${{ secrets.POKE_API_KEY }}" \
      -H "Content-Type: application/json" \
      -d "{\"message\": \"Deploy failed: ${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}. Create incident ticket and notify on-call.\"}"
```

### Bridge Non-Integrated Services

Any service that can POST a webhook can delegate to Poke - no need to wait for native integrations.

**Example: Typeform submission → Poke**

```
// Typeform webhook handler
app.post("/typeform-webhook", async (req, res) => {
  const { name, email, company } = req.body.form_response.answers;
 
  await fetch("https://poke.com/api/v1/inbound/api-message", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${process.env.POKE_API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      message: `New lead: ${name} from ${company}. Research their company, draft personalized follow-up email, and add meeting to my calendar next week.`,
    }),
  });
 
  res.sendStatus(200);
});
```

**Example: Custom CRM event**

```
# When deal closes in your CRM
def on_deal_closed(customer_info):
    message = f"""
    {customer_info['name']} just closed!
 
    - Send onboarding email with login details
    - Schedule kickoff call for next week
    - Create project in Notion
    - Set 30/60/90 day check-in reminders
    """
 
    requests.post(
        'https://poke.com/api/v1/inbound/api-message',
        headers={'Authorization': f'Bearer {POKE_API_KEY}', 'Content-Type': 'application/json'},
        json={'message': message}
    )
```

### Context-Rich Instructions

Pass URLs, selections, IDs, or structured data that makes your instruction immediately actionable.

**Example: VS Code extension**

```
// Send selected code with error context
const selection = editor.document.getText(editor.selection);
const filePath = editor.document.fileName;
const error = diagnostics[0].message;
 
await fetch("https://poke.com/api/v1/inbound/api-message", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${apiKey}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    message: `Debug this error:\n\nFile: ${filePath}\nError: ${error}\n\nCode:\n${selection}`,
  }),
});
```

## Tips

**Use environment variables** - Store your API key in `POKE_API_KEY` instead of hardcoding it.

**Be specific** - "Email John about Q1 review, suggest Tuesday or Wednesday" works better than "Contact John".

**Include context** - Pass URLs, file paths, or selections so Poke knows what to act on.

**Test first** - Send `{"message": "test"}` before building automation.

## Troubleshooting

### 401 Unauthorized

**Your API key is invalid or missing.**

Check:

1. Authorization header: `Bearer YOUR_KEY` (note the space after "Bearer")
2. Key hasn't been revoked in Settings
3. No extra spaces or newlines in the key

### Message not appearing

- Verify response shows `"success": true`
- Check your Poke app (refresh conversation)
- Try a simple test: `{"message": "test"}`
- Check notification settings in the app

### Rate limits

If you hit rate limits, consider:

- Batching multiple requests into one message
- Adding delays between automated messages
- Creating separate API keys for different automations

## Security

Keep your API key secure. Use environment variables, never commit keys to Git,
and revoke immediately if compromised. You can create multiple API keys - if one
is compromised, just revoke that key.

## What Happens Next

When your message arrives, Poke:

1. Evaluates what you're asking for
2. Decides which tools to use (email, calendar, integrations like Notion/Whoop/etc.)
3. Takes action and responds back to you
