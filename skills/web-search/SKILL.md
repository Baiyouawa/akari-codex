---
name: web-search
description: "Use when you need to find information on the internet — news, papers, facts, weather, events, or anything not in the repo"
complexity: low
model-minimum: glm-5
disable-model-invocation: false
allowed-tools: ["web_search", "web_fetch"]
---

# /web-search <query>

Search the internet using DuckDuckGo to find relevant information.

## When to use

- User asks about current events, weather, news, prices, etc.
- A task requires verifying facts or URLs from external sources
- Literature review or horizon scan needs to discover new papers or releases
- Any question whose answer depends on real-time or external data

## Step 1: Formulate queries

Convert the user's intent into effective search keywords:

- Be specific: "哈尔滨 天气 今天" > "天气"
- Include time context when relevant: "2026 GPT-5 release"
- Use multiple queries if the topic is broad (2-3 queries max)

## Step 2: Execute search

Call `web_search` with the query string. The tool returns:
- Top 5-8 results with titles and URLs
- If no results, try rephrasing the query

## Step 3: Evaluate results

For each result:
- **Relevant**: Title and snippet match the user's intent → proceed to fetch if details needed
- **Partial**: Tangentially related → note but don't fetch unless nothing better
- **Noise**: Irrelevant → skip

## Step 4: Deep-dive (optional)

If search snippets don't contain enough detail, use `web_fetch` to retrieve full page content from the most promising URLs. The tool strips HTML and returns plain text (truncated at 3000 chars).

**Verification discipline**: Never claim a fact from search snippets alone if accuracy matters. Fetch the source URL and confirm. This follows the same rigor as `/lit-review` and `/horizon-scan`.

## Output

Summarize findings naturally. Include source URLs for key claims. If nothing was found, say so honestly — do not fabricate information.

## Constraints

- Max 5 search queries per invocation to control cost
- Max 3 URL fetches per invocation
- Respect `web_fetch` timeouts (15s); if a site is slow, skip it
- Never fabricate URLs or cite pages you haven't fetched
