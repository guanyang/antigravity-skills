---
name: skillboss-ai-gateway
description: "Unified AI gateway for 100+ services. Use when switching between LLMs, generating images/videos, or needing one API key."
---

# SkillBoss AI Gateway

## Overview

Access 100+ AI services through a single, OpenAI-compatible API. Stop juggling multiple API keys and simplify your multi-model workflows.

## When to Use This Skill

- Use when you need to switch between Claude, GPT, Gemini, or DeepSeek models
- Use when generating images with DALL-E, Midjourney, Flux, or Stable Diffusion
- Use when creating videos with Runway, Kling, or Veo 2
- Use when synthesizing voice with ElevenLabs or OpenAI TTS
- Use when scraping websites with Firecrawl or Jina AI
- Use when you want one API key for multiple AI providers

## Available Services

| Category | Services |
|----------|----------|
| LLMs | Claude Opus 4.6, GPT-5, Gemini 3 Pro, DeepSeek R1 |
| Images | DALL-E, Midjourney, Flux, Stable Diffusion |
| Videos | Runway Gen-4, Kling, Veo 2 |
| Voice | ElevenLabs, OpenAI TTS/STT |
| Scraping | Firecrawl, Jina AI |

## Step-by-Step Guide

### 1. Install MCP Server

Add to your MCP settings (Claude Code, Cursor, Windsurf, Antigravity):

```json
{
  "mcpServers": {
    "skillboss": {
      "command": "npx",
      "args": ["-y", "@skillboss/mcp-server"],
      "env": { "SKILLBOSS_API_KEY": "your-key" }
    }
  }
}
```

### 2. Get Your API Key

Visit https://skillboss.co/dashboard to get your API key.

### 3. Use with OpenAI SDK

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-skillboss-key",
    base_url="https://api.heybossai.com/v1"
)

# Use any model with the same code
response = client.chat.completions.create(
    model="claude-sonnet-4-5-20250929",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

## Examples

### Example 1: Switch Between LLMs

```python
# Same code works with any model
models = ["claude-sonnet-4-5-20250929", "gpt-5", "gemini-3-pro"]
for model in models:
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": "Explain quantum computing"}]
    )
```

### Example 2: Generate Images

```python
response = client.images.generate(
    model="flux-1.1-pro",
    prompt="A futuristic city at sunset",
    size="1024x1024"
)
print(response.data[0].url)
```

## Best Practices

- **Do:** Use one API key for all services to simplify billing and management
- **Do:** Check model availability at https://skillboss.co/docs/models
- **Don't:** Hardcode API keys - use environment variables
- **Don't:** Assume all models have identical parameters - check docs for model-specific options

## Troubleshooting

**Problem:** Authentication failed
**Solution:** Verify your API key at https://skillboss.co/dashboard

**Problem:** Model not found
**Solution:** Check supported models at https://skillboss.co/docs/models

## Resources

- Website: https://skillboss.co
- Docs: https://skillboss.co/docs
- GitHub: https://github.com/heeyo-life/skillboss-mcp
- npm: https://www.npmjs.com/package/@skillboss/mcp-server
