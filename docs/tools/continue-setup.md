# Continue (VS Code) 接入大模型 API

> [Continue](https://continue.dev) 是 VS Code 开源 AI 编程助手，对标 Cursor 的免费 fork 替代。

## 配置步骤

### 1. 安装 VS Code 插件

VS Code Extensions 搜 **Continue** 安装。

### 2. 配置 config.json

`Cmd/Ctrl + Shift + P` → 选 **Continue: Configure Models** → 编辑 `~/.continue/config.json`：

```json
{
  "models": [
    {
      "title": "Claude Opus 4.7",
      "provider": "openai",
      "model": "claude-opus-4-7",
      "apiBase": "http://xdhdancer.top/v1",
      "apiKey": "sk-xxx"
    },
    {
      "title": "GPT-5",
      "provider": "openai",
      "model": "gpt-5",
      "apiBase": "http://xdhdancer.top/v1",
      "apiKey": "sk-xxx"
    },
    {
      "title": "DeepSeek V3.2",
      "provider": "openai",
      "model": "deepseek-v3.2",
      "apiBase": "http://xdhdancer.top/v1",
      "apiKey": "sk-xxx"
    }
  ],
  "tabAutocompleteModel": {
    "title": "Codex Fast",
    "provider": "openai",
    "model": "gpt-5-mini",
    "apiBase": "http://xdhdancer.top/v1",
    "apiKey": "sk-xxx"
  }
}
```

### 3. 验证

重启 VS Code，按 `Cmd + L` 打开 Continue 侧边栏。模型选择器应该列出上面配置的 3 个模型 + tab 补全。

## Continue 各功能模型选择

- **Chat（侧边栏对话）**：`claude-opus-4-7`
- **Inline edit（Cmd+I）**：`claude-sonnet-4-6` 或 `gpt-5`
- **Tab autocomplete**：`gpt-5-mini` 或 `claude-haiku-4-5`（要求快）

