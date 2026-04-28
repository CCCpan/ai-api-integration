# Dify 接入大模型 API

> Dify 是开源 LLM 应用开发平台（低代码工作流），支持自定义 OpenAI 兼容模型源。

## What is Dify

[Dify](https://dify.ai) 是开源 LLM 应用开发平台——拖拽式构建 AI 应用、Agent、工作流。GitHub 80k+ stars。

## 配置步骤

### 1. 进入设置

Dify 控制台 → 右上角头像 → **Settings** → **Model Provider**。

### 2. 添加 OpenAI 兼容模型

找到 **OpenAI-API-compatible** → **Add model**。

| 字段 | 填写值 |
|------|--------|
| Model Type | LLM |
| Model Name | `claude-opus-4-7` （或其他你要用的模型 ID） |
| API Key | `sk-xxx` |
| API endpoint URL | `http://xdhdancer.top/v1` |
| Model context size | `200000` (Claude Opus 4.7) 或对应模型的上下文长度 |
| Maximum tokens (max_tokens) | `8192` |
| Function calling | Yes（如果模型支持 tool use） |
| Stream function calling | Yes |
| Vision support | Yes（如果模型支持图片输入） |

### 3. 重复添加多个模型

Dify 把每个模型视为一个独立 entry——多模型需要分别添加：

- `gpt-5` — context 128000
- `claude-opus-4-7` — context 200000
- `gemini-3.1-pro` — context 2000000
- `deepseek-v3.2` — context 128000

### 4. 在应用里使用

新建/编辑 Dify 应用 → 选择刚配的模型即可。

## 推荐场景

| Dify 应用类型 | 推荐模型 |
|--------------|---------|
| Chatbot | `claude-sonnet-4-6` 或 `gpt-5` |
| Agent（多步推理） | `claude-opus-4-7` |
| 工作流（中度任务） | `gpt-5` 或 `gemini-3.1-pro` |
| 简单分类/抽取 | `gpt-5-mini` 或 `kimi-k2` |

## 常见问题

### Q: 添加模型时 context size 填错怎么办

A: 直接编辑该模型 entry 改 context size。填超过模型实际支持值会导致请求失败。

### Q: Function calling 启用了但模型不调工具

A: 先确认模型支持 function calling（GPT-5 / Claude / Gemini 都支持）。再检查 Dify 应用的 Agent / Tools 配置。

### Q: 自部署 Dify 怎么填

A: 自部署版同样填上面的字段，没有差异。

