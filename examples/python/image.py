"""
图片生成 - GPT-Image-2 / Gemini Image
"""
from openai import OpenAI

client = OpenAI(
    api_key="sk-xxx",
    base_url="http://xdhdancer.top/v1",
)

resp = client.images.generate(
    model="gpt-image-2",                       # 也可换 gemini-3.1-flash-image
    prompt="a cyberpunk cat sitting on a neon-lit rooftop, 4k illustration",
    size="1024x1024",
    n=1,
)

# resp.data[0].url 或 resp.data[0].b64_json（取决于 endpoint 返回）
print("Image URL:", resp.data[0].url)
