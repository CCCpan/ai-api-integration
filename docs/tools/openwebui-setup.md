# Open WebUI 接入大模型 API

> [Open WebUI](https://github.com/open-webui/open-webui) 是自部署 Ollama / OpenAI 兼容 UI，社区活跃。GitHub 80k+ stars。

## Docker 部署 + 配置

```bash
docker run -d --name open-webui \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://xdhdancer.top/v1 \
  -e OPENAI_API_KEY=sk-xxx \
  -v open-webui:/app/backend/data \
  --restart always \
  ghcr.io/open-webui/open-webui:main
```

访问 http://localhost:3000，注册管理员账号。

## 在 Web UI 里配置

设置 → **Connections** → **OpenAI API** → 填：

- API Base URL：`http://xdhdancer.top/v1`
- API Key：`sk-xxx`

保存后回主界面，模型下拉里会出现 `gpt-5` / `claude-opus-4-7` 等。

## 多模型管理

Open WebUI 支持**模型黑/白名单**——管理员后台可控制哪些模型对普通用户可见。

适合**多用户共享部署**的场景：管理员统一对接产灵 API，多个用户使用同一套 Key。

