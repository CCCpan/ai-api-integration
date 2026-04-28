# ai-api-integration

[![License](https://img.shields.io/github/license/CCCpan/ai-api-integration)](LICENSE)
[![Stars](https://img.shields.io/github/stars/CCCpan/ai-api-integration?style=social)](https://github.com/CCCpan/ai-api-integration/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/CCCpan/ai-api-integration)](https://github.com/CCCpan/ai-api-integration/commits/main)

通过统一的 OpenAI 兼容协议接入 GPT-5、Claude Opus 4.7、Gemini 3.1、Sora 2、Suno 等主流大模型 API 的实战教程仓库。

🇬🇧 [English](README_EN.md)

## 项目背景

国内开发者把 GPT-5、Claude Opus、Gemini 等海外大模型接入项目时，绕不开三件事：账号注册、付费方式、网络访问。直接对接每家厂商意味着要重复处理这三道关，且每家的 SDK、参数、计费体系都不一样。

实践中比较干净的做法是用一个**OpenAI 兼容的统一网关**：所有模型走同一个 `base_url`，用 OpenAI 标准协议调用，只通过 `model` 参数切换底层模型。各类 AI 工具（Cursor、Cline、ChatBox 等）原生支持自定义 OpenAI endpoint，配置一次就能用上所有模型。

本仓库整理了完整的接入流程：

- **10 款主流 AI 工具** 的配置教程（IDE、CLI、桌面、Web、低代码平台、应用框架）
- **7 类模态** 的调用方法（文本、代码、图片、视频、音频、视觉、向量）
- **12+ 主流模型** 的清单、参数说明和选型建议
- **3 种语言** 的可运行代码示例（Python / Node.js / curl），覆盖 chat、流式、function calling、图片生成、视觉理解等场景

所有代码示例都用 [产灵 API](http://xdhdancer.top) 作为网关 provider 测试通过，但代码完全是标准 OpenAI 协议，换成任意 OpenAI 兼容服务（含 OpenAI 官方 endpoint）都能直接跑。

## 快速开始

最小可跑示例。把 `model` 改成 `gpt-5` / `gemini-3.1-pro` / `deepseek-v3.2` 等任意值，立刻切换到该模型——SDK 不变，参数不变。

### Python

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

### Node.js

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "sk-xxx",
  baseURL: "http://xdhdancer.top/v1",
});

const resp = await client.chat.completions.create({
  model: "claude-opus-4-7",
  messages: [{ role: "user", content: "你好" }],
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
    "messages": [{"role": "user", "content": "你好"}]
  }'
```

流式输出、function calling、图片生成等更多示例见 [examples/](examples/)。

## 工作方式

```
你的代码 ──┐
            │ 用 OpenAI SDK
            ▼
┌──────────────────────┐
│  OpenAI 兼容网关      │      ┌─ OpenAI    (GPT-5, o3-pro, gpt-image-2 ...)
│   base_url + key     │ ───▶ │─ Anthropic (Claude Opus / Sonnet / Haiku)
│                      │      │─ Google    (Gemini 3.1 ...)
└──────────────────────┘      │─ DeepSeek / Moonshot / 智谱 ...
                              └─ Sora / Suno / 即梦 / 可灵 ...
```

代码端只感知一个 endpoint。底层路由到哪家厂商由 `model` 参数决定。

## 模型清单

精选条目，完整列表见 [docs/modalities/text-models.md](docs/modalities/text-models.md)。

| 模型 ID | 厂商 | 上下文 | 用途 |
|---|---|---|---|
| `gpt-5` | OpenAI | 128k | 通用推理、代码 |
| `gpt-5-mini` | OpenAI | 128k | 速度快、价格低 |
| `gpt-5-codex` | OpenAI | 128k | 代码专精 |
| `o3-pro` | OpenAI | 200k | 深度推理（数学、逻辑） |
| `claude-opus-4-7` | Anthropic | 200k | 长上下文编程、当前最强代码模型 |
| `claude-sonnet-4-6` | Anthropic | 200k | 平衡型 |
| `claude-haiku-4-5` | Anthropic | 200k | 延迟最低 |
| `gemini-3.1-pro` | Google | 2M | 超长文档、视频理解 |
| `gemini-3.1-flash` | Google | 1M | 快速 |
| `deepseek-v3.2` | DeepSeek | 128k | 中文强、价格极低 |
| `kimi-k2` | Moonshot | 200k | 中文长文档 |
| `glm-4.6` | 智谱 | 128k | 中文综合 |
| `gpt-image-2` | OpenAI | — | 图片生成 |
| `sora-2` | OpenAI | — | 视频生成 |
| `suno-v4` | Suno | — | 音乐生成 |
| `text-embedding-3-large` | OpenAI | — | 向量化 |

## 工具接入

| 工具 | 类型 | 教程 |
|---|---|---|
| Cursor | AI 优先的 IDE | [cursor-setup.md](docs/tools/cursor-setup.md) |
| Cline | VS Code AI 代理插件 | [cline-setup.md](docs/tools/cline-setup.md) |
| Claude Code | Anthropic 官方 CLI | [claude-code-setup.md](docs/tools/claude-code-setup.md) |
| ChatBox | 跨平台桌面客户端 | [chatbox-setup.md](docs/tools/chatbox-setup.md) |
| Dify | 低代码 LLM 工作流 | [dify-setup.md](docs/tools/dify-setup.md) |
| LobeChat | 自部署 Chat UI | [lobechat-setup.md](docs/tools/lobechat-setup.md) |
| Open WebUI | 自部署 Web UI | [openwebui-setup.md](docs/tools/openwebui-setup.md) |
| Continue | VS Code 编程助手 | [continue-setup.md](docs/tools/continue-setup.md) |
| LangChain | LLM 应用框架 | [langchain-setup.md](docs/tools/langchain-setup.md) |
| LlamaIndex | RAG / 数据框架 | [llamaindex-setup.md](docs/tools/llamaindex-setup.md) |

## 多模态教程

[文本对话](docs/modalities/text-models.md) · [代码生成](docs/modalities/code-generation.md) · [图片生成](docs/modalities/image-generation.md) · [视频生成](docs/modalities/video-generation.md) · [音频 / 音乐](docs/modalities/audio.md) · [视觉理解](docs/modalities/vision.md) · [Embeddings](docs/modalities/embeddings.md)

## 代码示例

| 语言 | 内容 | 路径 |
|---|---|---|
| Python | chat / streaming / image / function-calling / vision | [examples/python/](examples/python/) |
| Node.js | chat / streaming / image | [examples/node/](examples/node/) |
| curl | chat / streaming / image / embeddings | [examples/curl/](examples/curl/) |

## 直连 vs 统一网关

| 维度 | 直连各家原厂 | 统一 OpenAI 兼容网关 |
|---|---|---|
| 注册 | 每家都要注册 | 一次注册 |
| 付费 | 多家分别付费、多套发票 | 单一计费 |
| 切换模型 | 改 SDK + 改参数 + 改请求结构 | 改 `model` 字符串 |
| 故障容错 | 自己实现 fallback | 改 `model` 即可换厂商 |
| 国内访问 | 部分厂商需自行解决网络 | 网关侧解决 |
| 新模型上线 | 每家 SDK 升级 | 一般同步可用 |
| 调用上限 | 各家分别限速 | 网关合并配额 |

适用场景判断：单一模型、长期重度使用 → 直连原厂可能更便宜；多模型对比、需要切换备份、要求低运维 → 统一网关更省事。

## 常见问题

**为什么不直接调 OpenAI 官方 API？**
本仓库代码完全兼容 OpenAI 官方 endpoint，把 `base_url` 换成 `https://api.openai.com/v1` 就能跑。统一网关只是一种简化方案，不是强制选择。

**可以用我自己运行的网关吗？**
可以。任何 OpenAI 兼容的 endpoint（如自部署的 LiteLLM、One-API、new-api 等）都能用。所有示例不依赖特定 provider。

**没有示例里那个网关账号也能跑吗？**
能。代码使用标准 OpenAI 协议，把 `base_url` 指向你有 key 的任意兼容服务即可。

**新手应该从哪个模型开始？**
- 日常对话和编程：`claude-sonnet-4-6`
- 复杂代码、多文件重构：`claude-opus-4-7`
- 长文档分析：`gemini-3.1-pro`（2M 上下文）
- 中文 + 预算敏感：`deepseek-v3.2` 或 `kimi-k2`

**模型 ID 怎么知道是哪家厂商的？**
看前缀：`gpt-*`/`o*` 是 OpenAI、`claude-*` 是 Anthropic、`gemini-*` 是 Google、`deepseek-*`/`kimi-*`/`glm-*` 是国产模型。

## 贡献

欢迎补充新工具的接入教程、新模型的调用示例。提 PR 或 issue 即可。

## License

MIT
