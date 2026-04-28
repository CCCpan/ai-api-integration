# Embeddings 向量调用指南

> 通过统一网关调用 OpenAI / Cohere / BGE 等 embedding 模型。

## 模型清单

| 模型 ID | 维度 | 用途 |
|---------|------|------|
| `text-embedding-3-small` | 1536 | 通用、便宜 |
| `text-embedding-3-large` | 3072 | 高质量 |
| `bge-large-zh` | 1024 | 中文优化 |

## 调用代码

```python
from openai import OpenAI

client = OpenAI(api_key="sk-xxx", base_url="http://xdhdancer.top/v1")

resp = client.embeddings.create(
    model="text-embedding-3-small",
    input=["The quick brown fox", "jumps over the lazy dog"],
)

for emb in resp.data:
    print(f"维度: {len(emb.embedding)}, 前 5: {emb.embedding[:5]}")
```

## 在 RAG 里用

参考 [LlamaIndex 接入](../tools/llamaindex-setup.md) 或 [LangChain 接入](../tools/langchain-setup.md)。

