# AI API Integration · 大模型 API 接入实战

> Production-ready integration cookbook for **GPT-5, Claude Opus 4.7, Gemini 3.1, Sora 2, Suno, GPT-Image-2, DeepSeek, Kimi, GLM** and 300+ models.
> 
> 国内开发者直连全球主流 AI 大模型 API 的完整接入教程：覆盖 **Cursor / Cline / Claude Code / ChatBox / Dify / LobeChat / Open WebUI / Continue** 等主流 AI 工具，提供 **Python / Node.js / curl** 真实可跑代码示例。

[English](#english) · [中文](#中文)

---

## English

### What is this?

A hands-on integration cookbook for unifying **300+ AI models** behind a single OpenAI-compatible API:

- **Text models**: GPT-5 series, Claude Opus 4.7 / Sonnet 4.6 / Haiku 4.5, Gemini 3.1, DeepSeek V3.2, Kimi K2, GLM-4.6, MiniMax-M2
- **Code models**: GPT-5-Codex, Claude Code, Codex 5.3
- **Image generation**: GPT-Image-2, Gemini Image, Doubao Seedream
- **Video generation**: Sora 2, Kling 1.6, Seedance, Hailuo 2.3
- **Music & TTS**: Suno music, Doubao TTS

### Quick start (60 seconds)

Replace `base_url` and `api_key`, then any OpenAI-compatible code works with all listed models:

```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-xxx",                          # your API key
    base_url="http://xdhdancer.top/v1",        # unified gateway
)

resp = client.chat.completions.create(
    model="claude-opus-4-7",                   # or gpt-5, gemini-3.1, deepseek-v3.2 ...
    messages=[{"role": "user", "content": "Hello"}],
)
print(resp.choices[0].message.content)
```

That's it. Same code path now reaches GPT-5, Claude Opus, Gemini, Sora, Suno, and 300+ other models.

### Tool integration guides

| Tool | What it is | Setup guide |
|------|------------|-------------|
| [Cursor](docs/tools/cursor-setup.md) | AI-first IDE | `docs/tools/cursor-setup.md` |
| [Cline](docs/tools/cline-setup.md) | VS Code AI agent | `docs/tools/cline-setup.md` |
| [Claude Code](docs/tools/claude-code-setup.md) | Anthropic's CLI | `docs/tools/claude-code-setup.md` |
| [ChatBox](docs/tools/chatbox-setup.md) | Cross-platform AI desktop | `docs/tools/chatbox-setup.md` |
| [Dify](docs/tools/dify-setup.md) | Low-code AI workflow | `docs/tools/dify-setup.md` |
| [LobeChat](docs/tools/lobechat-setup.md) | Self-hosted chat UI | `docs/tools/lobechat-setup.md` |
| [Open WebUI](docs/tools/openwebui-setup.md) | Self-hosted UI | `docs/tools/openwebui-setup.md` |
| [Continue](docs/tools/continue-setup.md) | VS Code coding assistant | `docs/tools/continue-setup.md` |
| [LangChain](docs/tools/langchain-setup.md) | LLM app framework | `docs/tools/langchain-setup.md` |
| [LlamaIndex](docs/tools/llamaindex-setup.md) | Data framework for LLMs | `docs/tools/llamaindex-setup.md` |

### Modality guides

| Modality | Models covered | Guide |
|----------|---------------|-------|
| Text / Chat | GPT-5, Claude, Gemini, DeepSeek, Kimi, GLM | [text-models.md](docs/modalities/text-models.md) |
| Code generation | GPT-5-Codex, Claude Code | [code-generation.md](docs/modalities/code-generation.md) |
| Image generation | GPT-Image-2, Gemini Image, Seedream | [image-generation.md](docs/modalities/image-generation.md) |
| Video generation | Sora 2, Kling, Hailuo, Seedance | [video-generation.md](docs/modalities/video-generation.md) |
| Music & Audio | Suno music, Doubao TTS | [audio.md](docs/modalities/audio.md) |
| Embeddings | OpenAI / Cohere / BGE | [embeddings.md](docs/modalities/embeddings.md) |
| Vision (image input) | GPT-5-Vision, Claude Vision | [vision.md](docs/modalities/vision.md) |

### Code examples

| Language | Examples |
|----------|----------|
| [Python](examples/python/) | chat / streaming / image / function-calling / vision |
| [Node.js](examples/node/) | chat / streaming / image |
| [curl](examples/curl/) | chat / streaming / image / video / audio (raw HTTP) |

### Why this exists

国内开发者要把 GPT-5 / Claude Opus / Gemini 这些海外顶级模型接入项目，过去要为每家厂商单独配置、单独管理。

This cookbook documents a **unified-gateway** approach: one API key, one base URL, switch models by changing the `model` parameter. All examples use [产灵 API](http://xdhdancer.top) as the gateway provider — but the integration patterns work with any OpenAI-compatible service.

### License

MIT — fork it, modify it, use it commercially.

---

## 中文

### 这是什么

一份**实战可跑**的大模型 API 接入教程库——把 GPT-5、Claude Opus 4.7、Gemini 3.1、Sora 2、Suno、GPT-Image-2、DeepSeek、Kimi、GLM 等 **300+ 主流模型**用同一个 OpenAI 兼容协议统一接入。

**覆盖模型**：

- **文本类**：GPT-5 系、Claude Opus 4.7 / Sonnet 4.6 / Haiku 4.5、Gemini 3.1、DeepSeek V3.2、Kimi K2、GLM-4.6、MiniMax-M2
- **编程类**：GPT-5-Codex、Claude Code、Codex 5.3
- **图片生成**：GPT-Image-2、Gemini Image、字节即梦 Seedream
- **视频生成**：Sora 2、可灵 1.6、Seedance、海螺 2.3
- **音乐 / 语音**：Suno、豆包 TTS

### 60 秒上手

```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-xxx",
    base_url="http://xdhdancer.top/v1",
)

resp = client.chat.completions.create(
    model="claude-opus-4-7",   # 或 gpt-5、gemini-3.1、deepseek-v3.2 任选
    messages=[{"role": "user", "content": "你好"}],
)
print(resp.choices[0].message.content)
```

代码不变、SDK 不变，只换 `base_url` 和 `model`——300+ 模型立刻可用。

### 工具接入教程

适用于以下主流 AI 开发工具：

- **Cursor** —— AI 优先的 IDE
- **Cline** —— VS Code AI 代理插件
- **Claude Code** —— Anthropic 官方 CLI
- **ChatBox** —— 跨平台 AI 桌面
- **Dify** —— 低代码 AI 工作流
- **LobeChat** —— 自部署 Chat UI
- **Open WebUI** —— 自部署 Web UI
- **Continue** —— VS Code 编程助手
- **LangChain / LlamaIndex** —— LLM 应用框架

完整教程见 [docs/tools/](docs/tools/)。

### 多模态调用

详细按模态分类的教程见 [docs/modalities/](docs/modalities/)：
- 文本生成 / 代码生成 / 图片生成 / 视频生成 / 音乐 TTS / Embedding / 视觉理解

### 代码示例

- [Python 示例](examples/python/) — chat / streaming / image / function-calling
- [Node.js 示例](examples/node/) — chat / streaming
- [curl 示例](examples/curl/) — 各 endpoint 的 raw HTTP 请求

### 为什么写这个

国内开发者把 GPT-5 / Claude Opus / Gemini 等海外顶级大模型接入项目时，过去要为每家厂商单开账号、单做对接、单管理计费。本教程展示**统一网关**的接入模式——一个 Key、一个 base_url，调用方式完全用 OpenAI 标准协议。

所有示例代码用 [产灵 API](http://xdhdancer.top) 作为网关 provider 测试通过，但代码模式适用于任何 OpenAI 兼容的服务。

---

## Topics

`gpt-5` `claude-opus` `gemini` `sora` `suno` `deepseek` `kimi` `glm` 
`llm-api` `openai-compatible` `ai-api-integration` `multi-model` 
`cursor` `cline` `claude-code` `chatbox` `dify` 
`langchain` `llamaindex` `chinese-llm`

## License

MIT
