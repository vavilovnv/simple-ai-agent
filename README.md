## 🤖 A simple AI agent with web search

`Ru` Простой AI агент, "под капотом" которого два AI-ассистента - обычный и "думающий". Оба ассистента умеют в web-поиск. Ассистентами управляет модель-судья, которая решает, какому из ассистентов передать пользовательский запрос на доработку.

The AI agent can generate a response using the regular assistant and the thinking assistant, if necessary. Both assistants can use web search via the [Tavily](https://app.tavily.com/home) API.

To run the application, you need to use an LLM that supports the OpenAI API (the application uses integration from [langchain](https://python.langchain.com/docs/integrations/llms/openai/)).

You can use either an online or offline model. For instance, for a local setup, you can use [openai/gpt-oss-20b](https://huggingface.co/openai/gpt-oss-120b) and the [LM-studio](https://lmstudio.ai/docs/app) server.

### 💡 How does an AI agent work?
The [landgraph superviser](https://github.com/langchain-ai/langgraph-supervisor-py) determines which AI assistant will answer the user's question and redirects the question:
- A regular AI assistant handles simple questions. 
- Questions that require analysis and reasoning are forwarded to a thinking AI assistant.

The AI assistant generates a response, calling the Tavily API to obtain missing data if necessary. 

The generated result is returned to the supervisor, and from there to the user.


### Setting up and starting a chat with a model:
1. Install a package manager uv:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
2. Install dependencies:
```bash
uv sync
```
3. Based on the .env_example file, create a .env file and fill in the variable values.
4. Run main.py:
```bash
python main.py
```

