# 图片生成调用指南

> 通过统一网关调用 GPT-Image-2、Gemini Image、字节即梦 Seedream 等图片生成模型。

## 模型清单

| 模型 ID | 厂商 | 特点 |
|---------|------|------|
| `gpt-image-2` | OpenAI | 风格自由度高、prompt 理解强 |
| `gemini-3.1-flash-image` | Google | 速度快、风格多样 |
| `gemini-3-pro-image` | Google | 质量更高 |
| `doubao-seedream-4-0` | 字节 | 中文 prompt 友好 |

## 调用代码

### Python

```python
from openai import OpenAI

client = OpenAI(api_key="sk-xxx", base_url="http://xdhdancer.top/v1")

resp = client.images.generate(
    model="gpt-image-2",
    prompt="a cyberpunk cat sitting on a neon-lit rooftop, 4k illustration",
    size="1024x1024",
    n=1,
)
print(resp.data[0].url)
```

### curl

```bash
curl http://xdhdancer.top/v1/images/generations \
  -H "Authorization: Bearer sk-xxx" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-image-2",
    "prompt": "minimalist mountain at sunrise",
    "size": "1024x1024"
  }'
```

## Prompt 撰写技巧

1. **主体清晰**：`a robot` 优于 `something cool`
2. **风格描述**：`4k illustration / cinematic / oil painting`
3. **环境光线**：`neon-lit / sunset / dramatic lighting`
4. **构图**：`close-up / wide shot / isometric view`

例：
```
a futuristic city skyline at sunset, cyberpunk aesthetic, 
neon signs reflecting on wet streets, cinematic wide shot, 
ultra-detailed, 8k
```

## 完整可跑代码

详见 [examples/python/image.py](../../examples/python/image.py)。

