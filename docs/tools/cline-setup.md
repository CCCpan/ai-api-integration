# Cline 接入大模型 API

> Cline (原 Claude Dev) 是 VS Code 里的 AI 编程代理插件，支持 OpenAI 兼容 API。

## What is Cline

[Cline](https://github.com/cline/cline) 是 VS Code 上最火的 AI Agent 插件——它不只是补全，能**自主分析项目、执行命令、修改多个文件**。GitHub 30k+ stars。

## 配置步骤

### 1. 安装 Cline 插件

在 VS Code Extensions 搜索 **Cline** 安装。

### 2. 配置 API Provider

打开 Cline 侧边栏（左侧机器人图标）→ 右上角设置图标 → **API Provider** 选 **OpenAI Compatible**。

| 字段 | 填写值 |
|------|--------|
| Base URL | `http://xdhdancer.top/v1` |
| API Key | `sk-xxx` |
| Model ID | `claude-opus-4-7`（或其他模型 ID） |

### 3. 推荐模型组合

Cline 任务复杂度高，建议用强模型：

| 任务类型 | 模型 |
|---------|------|
| 代码重构、多文件改动 | `claude-opus-4-7` |
| 简单单文件修改 | `claude-sonnet-4-6` |
| Bug 排查 | `gpt-5` |
| 学习新代码库 | `claude-opus-4-7` |

### 4. 测试

让 Cline 做一个简单任务："帮我看看 `package.json` 里有哪些依赖，列出来"。

如果 Cline 能正常打开文件 + 回答 = 配置成功。

## 控制 token 消耗的技巧

Cline 默认会读很多文件，token 用量大。优化建议：

- 在 Settings → **Auto-approve** 区域关闭"自动读所有文件"
- 用 `claude-haiku-4-5` 做小任务，`opus` 做大任务
- 启用 **Prompt caching**（Cline 自动支持）减少重复 token

## 常见问题

### Q: Cline 报 "Context length exceeded"

A: Cline 把很多文件塞进上下文。换长上下文模型如 `claude-opus-4-7`（200k tokens）或 `gemini-3.1-pro`（2M tokens）。

### Q: 想用国产模型省钱

A: 把 Model ID 换成 `deepseek-v3.2` 或 `kimi-k2`，Cline 仍然能跑——只是简单任务质量略降。

### Q: 不知道当前模型支持的最大 token

A: 用 [examples/python/chat.py](../../examples/python/chat.py) 调用一次，error 信息会告诉你 max_tokens 限制。

