---
name: web-fetch
description: "Use when you need to read the content of a specific URL — verify a paper, check a webpage, extract data from a known source"
complexity: low
model-minimum: glm-5
disable-model-invocation: false
allowed-tools: ["web_fetch"]
---

# /web-fetch <url>

Fetch a URL and return its text content with HTML stripped.

## When to use

- Verifying a paper URL (arxiv, semantic scholar, etc.) during literature review
- Reading a blog post, documentation page, or API reference
- Extracting data from a known webpage
- Following up on a search result to get full details

## Step 1: Validate the URL

Ensure the URL is well-formed (starts with http:// or https://). For arxiv papers, prefer the abstract page (`https://arxiv.org/abs/XXXX.XXXXX`).

## Step 2: Fetch

Call `web_fetch` with the URL. Returns:
- Plain text content (HTML stripped, max 3000 chars)
- Error message if the fetch fails (timeout, 404, non-text content)

## Step 3: Interpret

- Extract the key information the user or task needs
- For verification tasks: confirm title, authors, and core claims match expectations
- For data extraction: pull out specific facts, numbers, or quotes

## Constraints

- Only fetches text/html and application/json content
- 15-second timeout per request
- Content truncated at 3000 characters
- Cannot handle login-protected pages or CAPTCHAs
- Do not fetch binary files (images, PDFs, videos)
