#!/bin/bash
# Function calling / Tool use - 让模型决定是否调用外部函数
# 第一轮：模型返回 tool_calls，第二轮：把工具执行结果丢回去得到最终答案

# 第一轮：让模型决定是否调工具
curl http://xdhdancer.top/v1/chat/completions \
  -H "Authorization: Bearer sk-xxx" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-opus-4-7",
    "messages": [
      {"role": "user", "content": "天气怎么样？北京。"}
    ],
    "tools": [{
      "type": "function",
      "function": {
        "name": "get_weather",
        "description": "Get current weather for a city",
        "parameters": {
          "type": "object",
          "properties": {"city": {"type": "string"}},
          "required": ["city"]
        }
      }
    }]
  }'

# 第二轮（拿到 tool_call_id 后）：把工具结果丢回去
# 把下面的 <TOOL_CALL_ID> 替换成上一轮返回的 tool_calls[0].id
curl http://xdhdancer.top/v1/chat/completions \
  -H "Authorization: Bearer sk-xxx" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-opus-4-7",
    "messages": [
      {"role": "user", "content": "天气怎么样？北京。"},
      {
        "role": "assistant",
        "tool_calls": [{
          "id": "<TOOL_CALL_ID>",
          "type": "function",
          "function": {"name": "get_weather", "arguments": "{\"city\":\"北京\"}"}
        }]
      },
      {
        "role": "tool",
        "tool_call_id": "<TOOL_CALL_ID>",
        "content": "{\"city\":\"北京\",\"temp\":22,\"condition\":\"sunny\"}"
      }
    ]
  }'
