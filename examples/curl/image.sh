#!/bin/bash
# Image generation
curl http://xdhdancer.top/v1/images/generations \
  -H "Authorization: Bearer sk-xxx" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-image-2",
    "prompt": "a robot reading a book in a cozy library",
    "size": "1024x1024",
    "n": 1
  }'
