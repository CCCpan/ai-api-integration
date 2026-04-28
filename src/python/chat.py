"""
Multi-model CLI chat demo — chat with any LLM through one OpenAI-compatible endpoint.

Usage:
    export API_KEY=sk-xxx
    export BASE_URL=http://xdhdancer.top/v1   # optional, this is the default
    python chat.py

Commands inside the REPL:
    /model <id>       switch model (e.g. /model gpt-5)
    /image <prompt>   generate an image with gpt-image-2
    /clear            clear chat history
    /exit             quit
"""
import os
import sys
from openai import OpenAI

API_KEY = os.environ.get("API_KEY")
BASE_URL = os.environ.get("BASE_URL", "http://xdhdancer.top/v1")

if not API_KEY:
    sys.exit("error: API_KEY environment variable not set")

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)


def chat(history, model):
    stream = client.chat.completions.create(
        model=model,
        messages=history,
        stream=True,
    )
    chunks = []
    for chunk in stream:
        delta = chunk.choices[0].delta
        if delta.content:
            print(delta.content, end="", flush=True)
            chunks.append(delta.content)
    print()
    return "".join(chunks)


def generate_image(prompt):
    resp = client.images.generate(
        model="gpt-image-2",
        prompt=prompt,
        size="1024x1024",
        n=1,
    )
    return resp.data[0].url


def main():
    model = "claude-opus-4-7"
    history = []
    print(f"connected to {BASE_URL}")
    print(f"current model: {model}")
    print("type /exit to quit, /model <id> to switch, /image <prompt> to generate")
    print()

    while True:
        try:
            user = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not user:
            continue
        if user == "/exit":
            break
        if user == "/clear":
            history = []
            print("(history cleared)")
            continue
        if user.startswith("/model "):
            model = user[len("/model "):].strip()
            print(f"(switched to {model})")
            continue
        if user.startswith("/image "):
            prompt = user[len("/image "):].strip()
            try:
                url = generate_image(prompt)
                print(f"image: {url}")
            except Exception as e:
                print(f"error: {e}")
            continue

        history.append({"role": "user", "content": user})
        try:
            reply = chat(history, model)
            history.append({"role": "assistant", "content": reply})
        except Exception as e:
            history.pop()
            print(f"error: {e}")


if __name__ == "__main__":
    main()
