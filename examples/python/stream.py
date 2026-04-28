"""
流式输出 - 实时打印
"""
from openai import OpenAI

client = OpenAI(
    api_key="sk-xxx",
    base_url="http://xdhdancer.top/v1",
)

stream = client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role": "user", "content": "用 100 字介绍 Python 的协程"},
    ],
    stream=True,
)

for chunk in stream:
    delta = chunk.choices[0].delta
    if delta.content:
        print(delta.content, end="", flush=True)
print()
