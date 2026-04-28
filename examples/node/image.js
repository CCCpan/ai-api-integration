import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "sk-xxx",
  baseURL: "http://xdhdancer.top/v1",
});

const resp = await client.images.generate({
  model: "gpt-image-2",
  prompt: "minimalist illustration of a fox in autumn forest",
  size: "1024x1024",
});

console.log("Image URL:", resp.data[0].url);
