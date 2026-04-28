# LobeChat 接入大模型 API

> [LobeChat](https://github.com/lobehub/lobe-chat) 是开源 ChatGPT 风格 UI，支持自部署、多模型、插件、知识库。GitHub 50k+ stars。

## 配置步骤

### Docker 部署

```bash
docker run -d --name lobe-chat \
  -p 3210:3210 \
  -e OPENAI_API_KEY=sk-xxx \
  -e OPENAI_PROXY_URL=http://xdhdancer.top/v1 \
  -e OPENAI_MODEL_LIST="+gpt-5,+claude-opus-4-7,+gemini-3.1-pro,+deepseek-v3.2,+kimi-k2" \
  lobehub/lobe-chat
```

打开 http://localhost:3210 即可。

### Web 版直接配置

去 [chat-preview.lobehub.com](https://chat-preview.lobehub.com) → 设置 → **Language Model** → **OpenAI** → 填写：

- API Key：`sk-xxx`
- API Proxy Address：`http://xdhdancer.top/v1`
- Custom Model Names：`gpt-5,claude-opus-4-7,gemini-3.1-pro,deepseek-v3.2`

## 启用图片 / 视觉模型

LobeChat 顶部模型选择器选支持视觉的模型（如 `gpt-5` / `claude-opus-4-7`），即可在对话框上传图片让 AI 分析。

## 常见问题

### Q: 模型列表为空

A: `OPENAI_MODEL_LIST` 环境变量必须用 `+` 前缀（表示添加）。例：`+gpt-5,+claude-opus-4-7`

