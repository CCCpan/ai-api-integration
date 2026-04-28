# ChatBox 接入大模型 API

> 跨平台 AI 桌面客户端，支持自定义 OpenAI 兼容 API。Mac / Windows / Linux 全平台。

## What is ChatBox

[ChatBox](https://chatboxai.app) 是开源跨平台 AI 桌面客户端，支持 OpenAI / Claude / Gemini / 自定义 API。

## 配置步骤

### 1. 下载安装

[chatboxai.app](https://chatboxai.app) → 下载对应平台版本 → 安装。

### 2. 配置 API

打开 ChatBox → 左下角 **Settings** → **AI Provider** → 选 **OpenAI API**。

| 字段 | 填写值 |
|------|--------|
| API Key | `sk-xxx` |
| API Host | `http://xdhdancer.top/v1` |
| Model | 输入 `claude-opus-4-7` 或其他模型 ID |

点 **Save**。

### 3. 测试

主界面新建一个会话，发"你好"。如果回复正常 = 配置成功。

## 多模型切换

ChatBox 支持**会话级别**模型切换——每个会话可以用不同模型。

- 复杂分析 → 切到 `claude-opus-4-7`
- 快速问答 → 切到 `claude-haiku-4-5` 或 `gpt-5-mini`
- 中文文档 → 切到 `kimi-k2` 或 `deepseek-v3.2`

## 常见问题

### Q: 回复中文乱码

A: ChatBox 设置 → 左侧 **Display** → 把字体改成支持中文的字体（默认就是）。一般是 endpoint 返回数据的问题，先用 [examples/python/chat.py](../../examples/python/chat.py) 验证 endpoint。

### Q: 流式输出不流畅

A: ChatBox 设置 → **Advanced** → 关闭 **Slow streaming protect**。

