# ai-api-integration

[![License](https://img.shields.io/github/license/CCCpan/ai-api-integration)](LICENSE)
[![Stars](https://img.shields.io/github/stars/CCCpan/ai-api-integration?style=social)](https://github.com/CCCpan/ai-api-integration/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/CCCpan/ai-api-integration)](https://github.com/CCCpan/ai-api-integration/commits/main)

Integration recipes for accessing GPT-5, Claude Opus 4.7, Gemini 3.1, Sora 2, Suno and other major models through a single OpenAI-compatible endpoint.

🇨🇳 [中文版](README_CN.md)

## Example

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

Switch the `model` value to access a different backend (`gpt-5`, `gemini-3.1-pro`, `deepseek-v3.2`, etc.) — the rest of the code is unchanged.

## Models

Selected entries. The full list and per-model notes live in [docs/modalities/](docs/modalities/).

| Model id | Vendor | Context | Notes |
|---|---|---|---|
| `gpt-5` | OpenAI | 128k | General reasoning, code |
| `gpt-5-mini` | OpenAI | 128k | Faster, cheaper variant |
| `o3-pro` | OpenAI | 200k | Deep reasoning |
| `claude-opus-4-7` | Anthropic | 200k | Long-context coding |
| `claude-sonnet-4-6` | Anthropic | 200k | Balanced |
| `claude-haiku-4-5` | Anthropic | 200k | Lowest latency |
| `gemini-3.1-pro` | Google | 2M | Long documents |
| `deepseek-v3.2` | DeepSeek | 128k | Strong Chinese, low cost |
| `kimi-k2` | Moonshot | 200k | Long Chinese documents |
| `gpt-image-2` | OpenAI | — | Image generation |
| `sora-2` | OpenAI | — | Video generation |
| `suno-v4` | Suno | — | Music generation |

## Tool setup

- [Cursor](docs/tools/cursor-setup.md) — AI-first IDE
- [Cline](docs/tools/cline-setup.md) — VS Code agent extension
- [Claude Code](docs/tools/claude-code-setup.md) — Anthropic CLI
- [ChatBox](docs/tools/chatbox-setup.md) — Cross-platform desktop client
- [Dify](docs/tools/dify-setup.md) — Low-code LLM workflow
- [LobeChat](docs/tools/lobechat-setup.md) — Self-hosted chat UI
- [Open WebUI](docs/tools/openwebui-setup.md) — Self-hosted Ollama-style UI
- [Continue](docs/tools/continue-setup.md) — VS Code coding assistant
- [LangChain](docs/tools/langchain-setup.md) — LLM application framework
- [LlamaIndex](docs/tools/llamaindex-setup.md) — RAG / data framework

## Modality guides

[Text](docs/modalities/text-models.md) · [Code](docs/modalities/code-generation.md) · [Image](docs/modalities/image-generation.md) · [Video](docs/modalities/video-generation.md) · [Audio](docs/modalities/audio.md) · [Vision](docs/modalities/vision.md) · [Embeddings](docs/modalities/embeddings.md)

## Code examples

[Python](examples/python/) · [Node.js](examples/node/) · [curl](examples/curl/)

## FAQ

**Why a unified gateway instead of calling each provider directly?**
One API key and one billing surface for every model; switching backends is a one-line change. Useful when you need to compare models or fall back across providers.

**Does this work with my own gateway?**
Yes. Replace `base_url` with whichever OpenAI-compatible endpoint you operate. The code paths in this repo do not depend on the provider used in the examples.

**Can I run the examples without an account on the example gateway?**
Yes — every example accepts a standard `OPENAI_API_KEY`-style credential. Point `base_url` at OpenAI directly (`https://api.openai.com/v1`) or any compatible service and the examples still run.

**Which model should I start with?**
For chat / coding tasks, `claude-sonnet-4-6` is a reasonable default. For long documents, `gemini-3.1-pro`. For cost-sensitive Chinese workloads, `deepseek-v3.2` or `kimi-k2`.

## Notes

The examples in this repository use [产灵 API](http://xdhdancer.top) as the gateway provider. Any OpenAI-compatible endpoint works the same way.

## License

MIT
