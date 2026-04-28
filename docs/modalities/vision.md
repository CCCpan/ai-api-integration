# 视觉理解 / 多模态输入

> 让模型"看图"——上传图片让 AI 分析、提取信息、回答问题。

## 支持视觉的模型

| 模型 ID | 视觉能力 |
|---------|---------|
| `gpt-5` | ✓ 高质量 |
| `claude-opus-4-7` | ✓ 业界最强 OCR + 图表理解 |
| `claude-sonnet-4-6` | ✓ |
| `gemini-3.1-pro` | ✓ 长视频理解 |
| `gemini-3.1-flash` | ✓ 速度快 |

## 调用示例

### URL 方式

```python
from openai import OpenAI

client = OpenAI(api_key="sk-xxx", base_url="http://xdhdancer.top/v1")

resp = client.chat.completions.create(
    model="claude-opus-4-7",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "图里有几个人？他们在做什么？"},
            {"type": "image_url", "image_url": {
                "url": "https://example.com/photo.jpg"
            }},
        ],
    }],
)
print(resp.choices[0].message.content)
```

### 本地图片（base64）

```python
import base64

with open("./photo.jpg", "rb") as f:
    b64 = base64.b64encode(f.read()).decode()

resp = client.chat.completions.create(
    model="gpt-5",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "提取图中的所有文字"},
            {"type": "image_url", "image_url": {
                "url": f"data:image/jpeg;base64,{b64}"
            }},
        ],
    }],
)
```

## 典型应用场景

- **OCR 识别**：从截图里提取代码 / 表格 / 文字
- **图表理解**：分析柱状图 / 饼图数据
- **设计稿转代码**：上传 UI 设计图，让模型生成 HTML/React
- **截图调试**：把报错截图给模型，让它分析

完整代码：[examples/python/vision.py](../../examples/python/vision.py)
