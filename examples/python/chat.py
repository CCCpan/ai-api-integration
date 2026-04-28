"""
基础 chat completion - 同步调用
"""
from openai import OpenAI

client = OpenAI(
    api_key="sk-xxx",                          # 替换为你的 API Key
    base_url="http://xdhdancer.top/v1",        # 统一网关
)

resp = client.chat.completions.create(
    model="claude-opus-4-7",                   # 任意模型 ID
    messages=[
        {"role": "system", "content": "You are a concise assistant."},
        {"role": "user", "content": "Explain RAG in one sentence."},
    ],
    temperature=0.3,
    max_tokens=500,
)

print(resp.choices[0].message.content)
print(f"\n[tokens used: {resp.usage.total_tokens}]")
