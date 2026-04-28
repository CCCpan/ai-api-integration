// Multi-model CLI chat demo — chat with any LLM through one OpenAI-compatible endpoint.
//
// Usage:
//   export API_KEY=sk-xxx
//   export BASE_URL=http://xdhdancer.top/v1   // optional
//   go mod tidy && go run chat.go
//
// Commands inside the REPL:
//   /model <id>       switch model
//   /image <prompt>   generate an image with gpt-image-2
//   /clear            clear chat history
//   /exit             quit

package main

import (
	"bufio"
	"context"
	"fmt"
	"io"
	"os"
	"strings"

	openai "github.com/sashabaranov/go-openai"
)

func main() {
	apiKey := os.Getenv("API_KEY")
	baseURL := os.Getenv("BASE_URL")
	if baseURL == "" {
		baseURL = "http://xdhdancer.top/v1"
	}
	if apiKey == "" {
		fmt.Fprintln(os.Stderr, "error: API_KEY environment variable not set")
		os.Exit(1)
	}

	cfg := openai.DefaultConfig(apiKey)
	cfg.BaseURL = baseURL
	client := openai.NewClientWithConfig(cfg)

	model := "claude-opus-4-7"
	var history []openai.ChatCompletionMessage

	fmt.Printf("connected to %s\n", baseURL)
	fmt.Printf("current model: %s\n", model)
	fmt.Println("type /exit to quit, /model <id> to switch, /image <prompt> to generate")
	fmt.Println()

	scanner := bufio.NewScanner(os.Stdin)
	for {
		fmt.Print("> ")
		if !scanner.Scan() {
			break
		}
		line := strings.TrimSpace(scanner.Text())
		if line == "" {
			continue
		}
		if line == "/exit" {
			break
		}
		if line == "/clear" {
			history = nil
			fmt.Println("(history cleared)")
			continue
		}
		if strings.HasPrefix(line, "/model ") {
			model = strings.TrimSpace(strings.TrimPrefix(line, "/model "))
			fmt.Printf("(switched to %s)\n", model)
			continue
		}
		if strings.HasPrefix(line, "/image ") {
			prompt := strings.TrimSpace(strings.TrimPrefix(line, "/image "))
			generateImage(client, prompt)
			continue
		}

		history = append(history, openai.ChatCompletionMessage{
			Role:    openai.ChatMessageRoleUser,
			Content: line,
		})
		reply, err := chatStream(client, history, model)
		if err != nil {
			history = history[:len(history)-1]
			fmt.Printf("error: %v\n", err)
			continue
		}
		history = append(history, openai.ChatCompletionMessage{
			Role:    openai.ChatMessageRoleAssistant,
			Content: reply,
		})
	}
}

func chatStream(client *openai.Client, history []openai.ChatCompletionMessage, model string) (string, error) {
	ctx := context.Background()
	stream, err := client.CreateChatCompletionStream(ctx, openai.ChatCompletionRequest{
		Model:    model,
		Messages: history,
		Stream:   true,
	})
	if err != nil {
		return "", err
	}
	defer stream.Close()

	var sb strings.Builder
	for {
		resp, err := stream.Recv()
		if err == io.EOF {
			break
		}
		if err != nil {
			return "", err
		}
		if len(resp.Choices) > 0 {
			delta := resp.Choices[0].Delta.Content
			fmt.Print(delta)
			sb.WriteString(delta)
		}
	}
	fmt.Println()
	return sb.String(), nil
}

func generateImage(client *openai.Client, prompt string) {
	ctx := context.Background()
	resp, err := client.CreateImage(ctx, openai.ImageRequest{
		Model:  "gpt-image-2",
		Prompt: prompt,
		Size:   "1024x1024",
		N:      1,
	})
	if err != nil {
		fmt.Printf("error: %v\n", err)
		return
	}
	if len(resp.Data) > 0 {
		fmt.Printf("image: %s\n", resp.Data[0].URL)
	}
}
