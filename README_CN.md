# ai-api-integration

[![License](https://img.shields.io/github/license/CCCpan/ai-api-integration)](LICENSE)
[![Stars](https://img.shields.io/github/stars/CCCpan/ai-api-integration?style=social)](https://github.com/CCCpan/ai-api-integration/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/CCCpan/ai-api-integration)](https://github.com/CCCpan/ai-api-integration/commits/main)

通过统一的 OpenAI 兼容协议接入 GPT-5、Claude Opus 4.7、Gemini 3.1、Sora 2、Suno 等主流大模型 API 的实战教程。

🇬🇧 [English](README.md)

## 示例

```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-xxx",
    base_url="http://xdhdancer.top/v1",
)

resp = client.chat.completions.create(
    model="claude-opus-4-7",
    messages=[{"role": "user", "content": "你好"}],
)
print(resp.choices[0].message.content)
```

只需要修改 `model` 参数即可切换到其他模型（`gpt-5`、`gemini-3.1-pro`、`deepseek-v3.2` 等），代码其他部分不变。

## 模型清单

精选条目。完整列表和模型说明见 [docs/modalities/](docs/modalities/)。

| 模型 ID | 厂商 | 上下文 | 说明 |
|---|---|---|---|
| `gpt-5` | OpenAI | 128k | 通用推理、代码 |
| `gpt-5-mini` | OpenAI | 128k | 速度快、价格低 |
| `o3-pro` | OpenAI | 200k | 深度推理 |
| `claude-opus-4-7` | Anthropic | 200k | 长上下文编程 |
| `claude-sonnet-4-6` | Anthropic | 200k | 性价比 |
| `claude-haiku-4-5` | Anthropic | 200k | 延迟最低 |
| `gemini-3.1-pro` | Google | 2M | 长文档 |
| `deepseek-v3.2` | DeepSeek | 128k | 中文强、价格低 |
| `kimi-k2` | Moonshot | 200k | 中文长文档 |
| `gpt-image-2` | OpenAI | — | 图片生成 |
| `sora-2` | OpenAI | — | 视频生成 |
| `suno-v4` | Suno | — | 音乐生成 |

## 工具接入

- [Cursor](docs/tools/cursor-setup.md) —— AI 优先的 IDE
- [Cline](docs/tools/cline-setup.md) —— VS Code AI 代理插件
- [Claude Code](docs/tools/claude-code-setup.md) —— Anthropic 官方 CLI
- [ChatBox](docs/tools/chatbox-setup.md) —— 跨平台桌面客户端
- [Dify](docs/tools/dify-setup.md) —— 低代码 LLM 工作流
- [LobeChat](docs/tools/lobechat-setup.md) —— 自部署 Chat UI
- [Open WebUI](docs/tools/openwebui-setup.md) —— 自部署 Web UI
- [Continue](docs/tools/continue-setup.md) —— VS Code 编程助手
- [LangChain](docs/tools/langchain-setup.md) —— LLM 应用框架
- [LlamaIndex](docs/tools/llamaindex-setup.md) —— RAG / 数据框架

## 多模态教程

[文本](docs/modalities/text-models.md) · [代码](docs/modalities/code-generation.md) · [图片](docs/modalities/image-generation.md) · [视频](docs/modalities/video-generation.md) · [音频](docs/modalities/audio.md) · [视觉](docs/modalities/vision.md) · [Embeddings](docs/modalities/embeddings.md)

## 代码示例

[Python](examples/python/) · [Node.js](examples/node/) · [curl](examples/curl/)

## 常见问题

**为什么用统一网关而不直接调各家 API？**
统一计费、统一 Key、切换模型只需改一行代码。适合需要对比多个模型或在多家厂商之间做容错的场景。

**可以用自己的网关吗？**
可以。把 `base_url` 替换成你自己运行的 OpenAI 兼容 endpoint 即可。本仓库的示例代码不依赖任何特定的 provider。

**没有示例里那个网关的账号也能跑吗？**
能。所有示例使用标准 OpenAI 兼容协议——直接指向 `https://api.openai.com/v1` 或任何兼容服务都能运行。

**新手应该从哪个模型开始？**
日常对话和编程任务推荐 `claude-sonnet-4-6`。长文档场景用 `gemini-3.1-pro`。中文且预算敏感用 `deepseek-v3.2` 或 `kimi-k2`。

## 说明

本仓库示例使用 [产灵 API](http://xdhdancer.top) 作为网关 provider。任何 OpenAI 兼容的服务都能以相同方式接入。

## License

MIT
