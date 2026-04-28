#!/bin/bash
# Streaming chat completion
curl http://xdhdancer.top/v1/chat/completions \
  -H "Authorization: Bearer sk-xxx" \
  -H "Content-Type: application/json" \
  --no-buffer \
  -d '{
    "model": "gpt-5",
    "messages": [{"role": "user", "content": "Tell me a story"}],
    "stream": true
  }'
