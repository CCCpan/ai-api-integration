import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "sk-xxx",
  baseURL: "http://xdhdancer.top/v1",
});

const resp = await client.chat.completions.create({
  model: "claude-opus-4-7",
  messages: [
    { role: "user", content: "Explain Node.js streams in one paragraph." },
  ],
});

console.log(resp.choices[0].message.content);
