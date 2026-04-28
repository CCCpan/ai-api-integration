# 文本类大模型调用指南

> 通过统一网关调用 GPT-5、Claude Opus 4.7、Gemini 3.1、DeepSeek V3.2、Kimi K2、GLM-4.6、MiniMax-M2 等主流文本大模型。

## 模型清单

| 模型 ID | 厂商 | 上下文 | 强项 |
|---------|------|--------|------|
| `gpt-5` | OpenAI | 128k | 复杂推理、代码 |
| `gpt-5-mini` | OpenAI | 128k | 速度快、便宜 |
| `o3-pro` | OpenAI | 200k | 深度推理 |
| `claude-opus-4-7` | Anthropic | 200k | 写代码、长文档 |
| `claude-sonnet-4-6` | Anthropic | 200k | 性价比 |
| `claude-haiku-4-5` | Anthropic | 200k | 速度最快 |
| `gemini-3.1-pro` | Google | 2M | 超长上下文 |
| `gemini-3.1-flash` | Google | 1M | 快速 |
| `deepseek-v3.2` | DeepSeek | 128k | 性价比、中文 |
| `kimi-k2` | Moonshot | 200k | 长文档、中文 |
| `glm-4.6` | 智谱 | 128k | 中文综合 |
| `minimax-m2` | MiniMax | 256k | 角色扮演 |

## Python 基础调用

```python
from openai import OpenAI

client = OpenAI(api_key="sk-xxx", base_url="http://xdhdancer.top/v1")

resp = client.chat.completions.create(
    model="claude-opus-4-7",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the difference between TCP and UDP?"},
    ],
    temperature=0.3,
)
print(resp.choices[0].message.content)
```

## 流式输出（推荐 UX）

```python
stream = client.chat.completions.create(
    model="gpt-5",
    messages=[{"role": "user", "content": "Write a poem"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

## 模型选型建议

| 场景 | 推荐 | 理由 |
|------|------|------|
| 复杂代码生成 | `claude-opus-4-7` | 当前业界最强代码能力 |
| 长文档分析（>50k token） | `gemini-3.1-pro` | 200 万上下文 |
| 中文撰写 / 客服 | `kimi-k2` 或 `deepseek-v3.2` | 中文质量好 + 价格低 |
| 高频简单查询 | `gpt-5-mini` 或 `claude-haiku-4-5` | 快、便宜 |
| 数学 / 逻辑推理 | `o3-pro` | 思维链最强 |

## 性能对比（参考）

不同模型对同一任务的延迟：

- `claude-haiku-4-5`：~1s 首 token
- `gpt-5-mini`：~1.5s
- `claude-opus-4-7`：~3-5s
- `o3-pro`：~10-30s（深度推理）

## 完整可跑代码

详见 [examples/python/chat.py](../../examples/python/chat.py)。

