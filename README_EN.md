# ai-api-integration

[![License](https://img.shields.io/github/license/CCCpan/ai-api-integration)](LICENSE)
[![Stars](https://img.shields.io/github/stars/CCCpan/ai-api-integration?style=social)](https://github.com/CCCpan/ai-api-integration/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/CCCpan/ai-api-integration)](https://github.com/CCCpan/ai-api-integration/commits/main)

Integration recipes for accessing GPT-5, Claude Opus 4.7, Gemini 3.1, Sora 2, Suno and other major models through a single OpenAI-compatible endpoint.

🇨🇳 [中文](README.md)

## Background

Accessing major LLM APIs from regions where some providers require workarounds usually means dealing with three things per vendor: account creation, payment, and network reachability. Direct integration also means juggling different SDKs, parameters, and billing surfaces.

A cleaner pattern in practice is to route everything through an **OpenAI-compatible gateway**: same `base_url`, same OpenAI protocol, model selection via the `model` parameter. Most AI tools (Cursor, Cline, ChatBox, etc.) support custom OpenAI endpoints natively, so a one-time configuration unlocks all backend models.

This repository documents the full integration flow:

- **10 popular AI tools** (IDE, CLI, desktop, web UI, low-code platforms, application frameworks)
- **7 modalities** (text, code, image, video, audio, vision, embeddings)
- **12+ models** with context limits and selection guidance
- **3 languages** of runnable code samples (Python / Node.js / curl) covering chat, streaming, function calling, image generation, vision input

The example endpoint is [产灵 API](http://xdhdancer.top), but the code is plain OpenAI-protocol — pointing `base_url` at any compatible service (including OpenAI's official endpoint) works the same way.

## Quick start

Switch the `model` value to access a different backend (`gpt-5`, `gemini-3.1-pro`, `deepseek-v3.2`, etc.). The rest of the code is unchanged.

### Python

```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-xxx",
    base_url="http://xdhdancer.top/v1",
)

resp = client.chat.completions.create(
    model="claude-opus-4-7",
    messages=[{"role": "user", "content": "Hello"}],
)
print(resp.choices[0].message.content)
```

### Node.js

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "sk-xxx",
  baseURL: "http://xdhdancer.top/v1",
});

const resp = await client.chat.completions.create({
  model: "claude-opus-4-7",
  messages: [{ role: "user", content: "Hello" }],
});

console.log(resp.choices[0].message.content);
```

### curl

```bash
curl http://xdhdancer.top/v1/chat/completions \
  -H "Authorization: Bearer sk-xxx" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-opus-4-7",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

More examples (streaming, function calling, image generation, vision) in [examples/](examples/).

## How it works

```
your code ──┐
            │ standard OpenAI SDK
            ▼
┌──────────────────────┐
│  OpenAI-compatible   │     ┌─ OpenAI    (GPT-5, o3-pro, gpt-image-2 ...)
│  gateway             │ ──▶ │─ Anthropic (Claude Opus / Sonnet / Haiku)
│  base_url + key      │     │─ Google    (Gemini 3.1 ...)
└──────────────────────┘     │─ DeepSeek / Moonshot / Zhipu ...
                             └─ Sora / Suno / image / video providers ...
```

Your code only sees one endpoint. The `model` parameter decides which vendor handles the request.

## Models

Selected entries; full list in [docs/modalities/text-models.md](docs/modalities/text-models.md).

| Model id | Vendor | Context | Notes |
|---|---|---|---|
| `gpt-5` | OpenAI | 128k | General reasoning, code |
| `gpt-5-mini` | OpenAI | 128k | Faster, cheaper |
| `gpt-5-codex` | OpenAI | 128k | Code-specialized |
| `o3-pro` | OpenAI | 200k | Deep reasoning |
| `claude-opus-4-7` | Anthropic | 200k | Long-context coding |
| `claude-sonnet-4-6` | Anthropic | 200k | Balanced |
| `claude-haiku-4-5` | Anthropic | 200k | Lowest latency |
| `gemini-3.1-pro` | Google | 2M | Long documents, video |
| `gemini-3.1-flash` | Google | 1M | Fast |
| `deepseek-v3.2` | DeepSeek | 128k | Strong Chinese, low cost |
| `kimi-k2` | Moonshot | 200k | Long Chinese documents |
| `glm-4.6` | Zhipu | 128k | Chinese general-purpose |
| `gpt-image-2` | OpenAI | — | Image generation |
| `sora-2` | OpenAI | — | Video generation |
| `suno-v4` | Suno | — | Music generation |
| `text-embedding-3-large` | OpenAI | — | Embeddings |

## Tool setup

| Tool | Type | Guide |
|---|---|---|
| Cursor | AI-first IDE | [cursor-setup.md](docs/tools/cursor-setup.md) |
| Cline | VS Code agent | [cline-setup.md](docs/tools/cline-setup.md) |
| Claude Code | Anthropic CLI | [claude-code-setup.md](docs/tools/claude-code-setup.md) |
| ChatBox | Cross-platform desktop | [chatbox-setup.md](docs/tools/chatbox-setup.md) |
| Dify | Low-code LLM workflow | [dify-setup.md](docs/tools/dify-setup.md) |
| LobeChat | Self-hosted chat UI | [lobechat-setup.md](docs/tools/lobechat-setup.md) |
| Open WebUI | Self-hosted web UI | [openwebui-setup.md](docs/tools/openwebui-setup.md) |
| Continue | VS Code coding assistant | [continue-setup.md](docs/tools/continue-setup.md) |
| LangChain | LLM app framework | [langchain-setup.md](docs/tools/langchain-setup.md) |
| LlamaIndex | RAG / data framework | [llamaindex-setup.md](docs/tools/llamaindex-setup.md) |

## Modality guides

[Text](docs/modalities/text-models.md) · [Code](docs/modalities/code-generation.md) · [Image](docs/modalities/image-generation.md) · [Video](docs/modalities/video-generation.md) · [Audio](docs/modalities/audio.md) · [Vision](docs/modalities/vision.md) · [Embeddings](docs/modalities/embeddings.md)

## Code examples

| Language | Coverage | Path |
|---|---|---|
| Python | chat / streaming / image / function-calling / vision | [examples/python/](examples/python/) |
| Node.js | chat / streaming / image | [examples/node/](examples/node/) |
| curl | chat / streaming / image / embeddings | [examples/curl/](examples/curl/) |

## Direct vs gateway

| Aspect | Direct (per vendor) | Unified OpenAI-compatible gateway |
|---|---|---|
| Sign-up | One per vendor | Once |
| Billing | Multiple invoices | Single |
| Switching models | Different SDK + params + request shape | Change `model` string |
| Failover | Custom logic per vendor | Change `model` to switch backend |
| Network | Some vendors require workarounds | Handled by the gateway |
| New models | Each vendor's SDK update | Usually available immediately |
| Rate limits | Per-vendor quotas | Combined quota |

When direct is better: single-model, heavy long-term use — unit cost may be lower with the original vendor. When a gateway is better: multi-model comparisons, runtime fallback, low ops overhead.

## FAQ

**Why not call the OpenAI API directly?**
You can — the code is fully compatible. Replace `base_url` with `https://api.openai.com/v1`. The gateway approach is one option, not a requirement.

**Can I use my own gateway?**
Yes. Any OpenAI-compatible endpoint (LiteLLM, One-API, new-api, etc., self-hosted) works without code changes.

**Does this work without an account at the example gateway?**
Yes. Use any OpenAI-compatible endpoint where you have a key.

**Which model should I start with?**
- General chat and coding: `claude-sonnet-4-6`
- Heavy code, multi-file refactors: `claude-opus-4-7`
- Long-document analysis: `gemini-3.1-pro` (2M context)
- Chinese workloads, low budget: `deepseek-v3.2` or `kimi-k2`

**How do I tell which vendor a model id belongs to?**
By prefix: `gpt-*` / `o*` are OpenAI, `claude-*` is Anthropic, `gemini-*` is Google, `deepseek-*` / `kimi-*` / `glm-*` are Chinese providers.

## Contributing

Setup guides for additional tools or examples for new models are welcome. Open a PR or an issue.

## License

MIT
