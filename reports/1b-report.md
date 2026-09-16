# Homework 1B Report

## Required Tasks

I built a command-line agent with the OpenAI Responses API. The program loads its API key from a `.env` file, accepts a prompt file and model/reasoning command-line options, sends requests with `client.responses.create()`, and prints token usage and estimated cost at the end of a session.

I expanded the program into a multi-turn agent. Each user message is appended to `history`, and the completed API response output is appended after each turn. Passing `history` through the `input` parameter lets the model use the earlier conversation as context.

I also enabled streaming with `stream=True`. The program prints each `response.output_text.delta` event immediately, then saves the final response from the `response.completed` event for usage reporting and conversation history.

## Additional Exploration

I compared several models, including `gpt-4o-mini`, `gpt-4.1-nano`, `gpt-5.6-luna`, `gpt-5.6-terra`, and `gpt-5.6-sol`, using speech-summary prompts. I compared response quality, latency, token counts, caching, and reported cost.

I explored shell redirection by running commands such as `python3 agent.py prompt3.md > output4.md`. I updated the agent so redirected output creates a transcript containing both `USER:` messages and streamed `AGENT:` responses. The code checks `sys.stdout.isatty()` so normal terminal use has one input prompt, while redirected use records complete user messages in the Markdown file.

## Obstacles

Initially, VS Code could not resolve the `dotenv` or `openai` imports. I installed `python-dotenv` and `openai`, created a local `.venv`, and selected that interpreter for the workspace.

My first conversation-history attempt used a `history` argument with the Responses API, but that is not a supported parameter. I corrected it by passing the history list as `input`.

My first streaming implementation called `stream.get_final_response()`, which caused an `AttributeError` because the installed SDK's `Stream` object does not provide that method. I corrected this by saving `event.response` when the stream emits `response.completed`.

When I stopped the program with `Ctrl-C` while it was waiting for input, Python displayed a `KeyboardInterrupt` traceback. Ending a session with `exit` instead allows the `finally` block to print the usage summary cleanly.

## What I Learned

I learned the difference between standard input, standard output, and standard error, especially when output is redirected to a file. I also learned that streaming produces a sequence of typed events, so text can be displayed from delta events while the final response object is retained for metadata and future context.

I learned that client-side conversation history must use the API's supported request shape. I also learned that a local virtual environment makes installed dependencies and editor analysis more reliable.

## Relevance to Agent Engineering

An agent is more than a single model call. It needs a reliable runtime environment, conversation state, incremental output, graceful session handling, observability through usage data, and reproducible artifacts such as transcripts. These experiments show how API details, terminal behavior, and context management directly affect an agent's usability and reliability.

## Time Spent

Hours spent: **[enter your total hours here]**
