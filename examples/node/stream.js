import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "sk-xxx",
  baseURL: "http://xdhdancer.top/v1",
});

const stream = await client.chat.completions.create({
  model: "gpt-5",
  messages: [{ role: "user", content: "Write a haiku about coding." }],
  stream: true,
});

for await (const chunk of stream) {
  process.stdout.write(chunk.choices[0]?.delta?.content || "");
}
console.log();
