# Claude Code 接入大模型 API

> Anthropic 官方 CLI 工具 Claude Code，支持自定义 API endpoint，可接 GPT/Gemini 等模型。

## What is Claude Code

[Claude Code](https://www.anthropic.com/claude-code) 是 Anthropic 官方推出的命令行 AI 编程助手。安装后输入 `claude` 直接进入对话/编程会话。

虽然名字叫 Claude Code，但它**支持任意 OpenAI 兼容 endpoint**——通过环境变量切换。

## 安装

```bash
npm install -g @anthropic-ai/claude-code
```

## 配置（关键）

Claude Code 通过环境变量配置 endpoint。在 `~/.zshrc` 或 `~/.bashrc` 添加：

```bash
export ANTHROPIC_BASE_URL=http://xdhdancer.top
export ANTHROPIC_AUTH_TOKEN=sk-xxx
```

应用配置：

```bash
source ~/.zshrc
```

## 运行

```bash
cd /path/to/your/project
claude
```

进入交互式 session 后可以：
- `> 帮我重构这个文件，让它更模块化`
- `> 给这个 API 加上单元测试`
- `> 找出代码里的潜在 bug`

## 模型选择

Claude Code 默认用 Claude Sonnet。如果你的网关支持 GPT-5/Gemini 等，启动时指定模型：

```bash
claude --model claude-opus-4-7
claude --model gpt-5             # 也行（兼容协议）
claude --model gemini-3.1-pro
```

或在 `~/.config/claude-code/config.json`：

```json
{
  "model": "claude-opus-4-7",
  "max_tokens": 8192
}
```

## 常见问题

### Q: `claude: command not found`

A: npm 全局 bin 目录可能没在 PATH 里。执行：

```bash
npm config get prefix
# 输出 /Users/xxx/.npm-global
# 把 /Users/xxx/.npm-global/bin 加到 PATH
```

### Q: 想保留官方 Anthropic API 同时配置网关

A: 不用环境变量，改用 `--base-url` flag：

```bash
claude --base-url http://xdhdancer.top --api-key sk-xxx
```

### Q: 报错 "model not found"

A: 你网关可能不支持该模型 ID。用 `claude --model gpt-5` 试一个支持的模型。

