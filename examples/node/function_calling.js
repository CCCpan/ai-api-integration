/**
 * Function calling / Tool use - 让模型调用外部函数
 */
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "sk-xxx",
  baseURL: "http://xdhdancer.top/v1",
});

const tools = [
  {
    type: "function",
    function: {
      name: "get_weather",
      description: "Get current weather for a city",
      parameters: {
        type: "object",
        properties: { city: { type: "string" } },
        required: ["city"],
      },
    },
  },
];

const userMessage = { role: "user", content: "天气怎么样？北京。" };

// 第一轮：让模型决定是否调工具
const resp = await client.chat.completions.create({
  model: "claude-opus-4-7",
  messages: [userMessage],
  tools,
});

const msg = resp.choices[0].message;
if (msg.tool_calls?.length) {
  const toolCall = msg.tool_calls[0];
  const args = JSON.parse(toolCall.function.arguments);
  console.log(`模型要调用 ${toolCall.function.name}(${JSON.stringify(args)})`);

  // 模拟工具结果
  const toolResult = { city: args.city, temp: 22, condition: "sunny" };

  // 第二轮：把工具结果丢回去
  const resp2 = await client.chat.completions.create({
    model: "claude-opus-4-7",
    messages: [
      userMessage,
      msg,
      {
        role: "tool",
        tool_call_id: toolCall.id,
        content: JSON.stringify(toolResult),
      },
    ],
  });
  console.log(resp2.choices[0].message.content);
}
