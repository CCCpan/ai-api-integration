#!/bin/bash
# Basic chat completion
curl http://xdhdancer.top/v1/chat/completions \
  -H "Authorization: Bearer sk-xxx" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-opus-4-7",
    "messages": [
      {"role": "user", "content": "Hello"}
    ]
  }'
