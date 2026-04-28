# ai-api-integration

Integration recipes for accessing GPT-5, Claude Opus 4.7, Gemini 3.1, Sora 2, Suno and other major models through a single OpenAI-compatible endpoint. Setup guides for Cursor, Cline, Claude Code, ChatBox, Dify, LangChain, LlamaIndex.

国内开发者接入海外大模型 API 的实战手册，所有示例可直接运行。

## Example

```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-xxx",
    base_url="http://xdhdancer.top/v1",
)

resp = client.chat.completions.create(
    model="claude-opus-4-7",
    messages=[{"role": "user", "content": "Hello"}],
)
print(resp.choices[0].message.content)
```

Switch the `model` value to access a different backend (`gpt-5`, `gemini-3.1-pro`, `deepseek-v3.2`, etc.) — the rest of the code is unchanged.

## Tool setup

- [Cursor](docs/tools/cursor-setup.md)
- [Cline](docs/tools/cline-setup.md)
- [Claude Code](docs/tools/claude-code-setup.md)
- [ChatBox](docs/tools/chatbox-setup.md)
- [Dify](docs/tools/dify-setup.md)
- [LobeChat](docs/tools/lobechat-setup.md)
- [Open WebUI](docs/tools/openwebui-setup.md)
- [Continue](docs/tools/continue-setup.md)
- [LangChain](docs/tools/langchain-setup.md)
- [LlamaIndex](docs/tools/llamaindex-setup.md)

## Modality guides

[Text](docs/modalities/text-models.md) · [Code](docs/modalities/code-generation.md) · [Image](docs/modalities/image-generation.md) · [Video](docs/modalities/video-generation.md) · [Audio](docs/modalities/audio.md) · [Vision](docs/modalities/vision.md) · [Embeddings](docs/modalities/embeddings.md)

## Code examples

[Python](examples/python/) · [Node.js](examples/node/) · [curl](examples/curl/)

## Notes

The examples use [产灵 API](http://xdhdancer.top) as the gateway. Any OpenAI-compatible endpoint works the same way — replace `base_url` with whichever provider you use.

## License

MIT
