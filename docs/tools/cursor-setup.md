# Cursor 接入主流大模型 API（GPT-5 / Claude Opus / Gemini）

> 在 Cursor 里把 AI 模型源切换到 GPT-5 / Claude Opus 4.7 / Gemini 3.1 等海外顶级大模型，仅需修改 base_url。

## What is Cursor

[Cursor](https://cursor.sh) 是当前最流行的 AI-first IDE，原生集成 AI 编程能力（Tab 自动补全、Cmd+K 内联编辑、Cmd+L 对话）。默认用自家 endpoint，但**支持配置 OpenAI 兼容自定义 endpoint**。

## 配置步骤

### 1. 打开 Cursor 设置

`Cmd + ,`（macOS）或 `Ctrl + ,`（Windows）打开 Settings → 进入 **Models** 页面。

### 2. 配置 OpenAI API Key

在 **OpenAI API Key** 区域：

| 字段 | 填写值 |
|------|--------|
| API Key | `sk-xxx`（你的 API Key） |
| Override OpenAI Base URL | `http://xdhdancer.top/v1` |

点击 **Save** 保存。

### 3. 启用模型

在 **Available Models** 区域勾选要用的模型。也可以**手动添加**模型名（推荐，覆盖最全）：

```
gpt-5
gpt-5-mini
gpt-5-codex
claude-opus-4-7
claude-sonnet-4-6
claude-haiku-4-5
gemini-3.1-pro
gemini-3.1-flash
deepseek-v3.2
kimi-k2
```

### 4. 验证

打开任意文件按 `Cmd + L` 唤起 Chat，左下角模型选择器选 `claude-opus-4-7` 或 `gpt-5`，发送一个测试问题。

如果回复正常 = 配置成功。

## 各功能模式下的模型选择

| Cursor 功能 | 推荐模型 | 理由 |
|------------|---------|------|
| Tab 自动补全 | `gpt-5-mini` 或 `claude-haiku-4-5` | 速度快，便宜 |
| Cmd+K 内联编辑 | `claude-sonnet-4-6` 或 `gpt-5` | 平衡速度和质量 |
| Cmd+L 对话 | `claude-opus-4-7` | 复杂任务质量最高 |
| Composer（多文件） | `claude-opus-4-7` 或 `gpt-5` | 长上下文理解 |

## 常见问题

### Q: 报错 "Invalid API key"

A: 检查 API Key 是否带 `sk-` 前缀、是否完整、base_url 末尾是否有多余的 `/`。

### Q: 模型不在 Available Models 列表里

A: 在设置页找到 **Add custom model** 输入框，手动输入模型名（如 `claude-opus-4-7`）后点 **Add**。

### Q: 流式输出卡顿

A: 打开 Cursor 设置 → **Network**，关闭 **Code completions on slow networks**，并确认网络稳定。

## 验证脚本（用 Python 直接测）

确认网关可用后再配 Cursor。运行 [examples/python/chat.py](../../examples/python/chat.py) 跑通后再配置 IDE。

