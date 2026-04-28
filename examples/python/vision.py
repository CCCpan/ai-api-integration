"""
视觉理解 - 上传图片让模型分析
"""
import base64
from openai import OpenAI

client = OpenAI(api_key="sk-xxx", base_url="http://xdhdancer.top/v1")

# 方法 1：用图片 URL
resp = client.chat.completions.create(
    model="claude-opus-4-7",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "图里是什么？"},
            {"type": "image_url", "image_url": {
                "url": "https://example.com/sample.jpg"
            }},
        ],
    }],
)
print(resp.choices[0].message.content)

# 方法 2：本地图片转 base64
def image_to_data_url(path: str) -> str:
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    return f"data:image/jpeg;base64,{b64}"

resp = client.chat.completions.create(
    model="gpt-5",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "Describe this image."},
            {"type": "image_url", "image_url": {"url": image_to_data_url("./photo.jpg")}},
        ],
    }],
)
print(resp.choices[0].message.content)
