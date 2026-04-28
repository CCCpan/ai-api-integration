# Demo: Multi-model CLI chat

Interactive command-line chat — same UX in three languages, all routing through one OpenAI-compatible endpoint.

## What it does

- Type a message → streamed reply from the current model
- `/model <id>` — switch model on the fly (e.g. `/model gpt-5`, `/model gemini-3.1-pro`)
- `/image <prompt>` — generate an image with `gpt-image-2`
- `/clear` — clear chat history
- `/exit` — quit

The same commands and behavior work in all three implementations.

## Run it

All versions read `API_KEY` and `BASE_URL` from environment variables. `BASE_URL` defaults to `http://xdhdancer.top/v1` (the example gateway). Replace with any OpenAI-compatible endpoint to use your own provider.

### Python

```bash
cd src/python
pip install -r requirements.txt
export API_KEY=sk-xxx
python chat.py
```

### Node.js

```bash
cd src/node
npm install
export API_KEY=sk-xxx
node chat.js
```

### Go

```bash
cd src/go
export API_KEY=sk-xxx
go mod tidy
go run chat.go
```

## Sample session

```
connected to http://xdhdancer.top/v1
current model: claude-opus-4-7
type /exit to quit, /model <id> to switch, /image <prompt> to generate

> 用一句话解释 RAG
RAG 是检索增强生成,先从知识库检索相关内容再让 LLM 基于这些内容生成答案。

> /model gpt-5
(switched to gpt-5)

> 同样的问题再回答一次
RAG (Retrieval-Augmented Generation) combines a retriever and a generator: ...

> /image a cyberpunk cat on a neon rooftop
image: https://...

> /exit
```

## Why three languages

Same protocol, same key, same endpoint — only the SDK differs. Pick whichever fits your stack.
