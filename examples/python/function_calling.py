"""
Function calling / Tool use - 让模型调用外部函数
"""
import json
from openai import OpenAI

client = OpenAI(api_key="sk-xxx", base_url="http://xdhdancer.top/v1")

tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current weather for a city",
        "parameters": {
            "type": "object",
            "properties": {"city": {"type": "string"}},
            "required": ["city"],
        },
    },
}]

# 第一轮：让模型决定是否调工具
resp = client.chat.completions.create(
    model="claude-opus-4-7",
    messages=[{"role": "user", "content": "天气怎么样？北京。"}],
    tools=tools,
)

msg = resp.choices[0].message
if msg.tool_calls:
    tool_call = msg.tool_calls[0]
    args = json.loads(tool_call.function.arguments)
    print(f"模型要调用 {tool_call.function.name}({args})")
    
    # 模拟工具结果
    tool_result = {"city": args["city"], "temp": 22, "condition": "sunny"}
    
    # 第二轮：把工具结果丢回去
    resp2 = client.chat.completions.create(
        model="claude-opus-4-7",
        messages=[
            {"role": "user", "content": "天气怎么样？北京。"},
            msg,
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(tool_result),
            },
        ],
    )
    print(resp2.choices[0].message.content)
