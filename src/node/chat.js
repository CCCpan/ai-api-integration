/**
 * Multi-model CLI chat demo — chat with any LLM through one OpenAI-compatible endpoint.
 *
 * Usage:
 *   export API_KEY=sk-xxx
 *   export BASE_URL=http://xdhdancer.top/v1   # optional
 *   npm install && node chat.js
 *
 * Commands inside the REPL:
 *   /model <id>       switch model
 *   /image <prompt>   generate an image with gpt-image-2
 *   /clear            clear chat history
 *   /exit             quit
 */
import OpenAI from "openai";
import readline from "readline";

const apiKey = process.env.API_KEY;
const baseURL = process.env.BASE_URL || "http://xdhdancer.top/v1";

if (!apiKey) {
  console.error("error: API_KEY environment variable not set");
  process.exit(1);
}

const client = new OpenAI({ apiKey, baseURL });

let model = "claude-opus-4-7";
let history = [];

async function chat(userMessage) {
  history.push({ role: "user", content: userMessage });
  try {
    const stream = await client.chat.completions.create({
      model,
      messages: history,
      stream: true,
    });
    let reply = "";
    for await (const chunk of stream) {
      const delta = chunk.choices[0]?.delta?.content || "";
      process.stdout.write(delta);
      reply += delta;
    }
    process.stdout.write("\n");
    history.push({ role: "assistant", content: reply });
  } catch (err) {
    history.pop();
    console.error(`error: ${err.message}`);
  }
}

async function generateImage(prompt) {
  try {
    const resp = await client.images.generate({
      model: "gpt-image-2",
      prompt,
      size: "1024x1024",
      n: 1,
    });
    console.log(`image: ${resp.data[0].url}`);
  } catch (err) {
    console.error(`error: ${err.message}`);
  }
}

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

console.log(`connected to ${baseURL}`);
console.log(`current model: ${model}`);
console.log("type /exit to quit, /model <id> to switch, /image <prompt> to generate");
console.log();

function prompt() {
  rl.question("> ", async (input) => {
    const line = input.trim();
    if (!line) return prompt();
    if (line === "/exit") return rl.close();
    if (line === "/clear") {
      history = [];
      console.log("(history cleared)");
      return prompt();
    }
    if (line.startsWith("/model ")) {
      model = line.slice("/model ".length).trim();
      console.log(`(switched to ${model})`);
      return prompt();
    }
    if (line.startsWith("/image ")) {
      await generateImage(line.slice("/image ".length).trim());
      return prompt();
    }
    await chat(line);
    prompt();
  });
}

prompt();
