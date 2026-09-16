# Homework 1B Report

## Required Tasks
I controlled the summary format with detailed prompt instructions. The agent was asked to give a concise affirmation followed by a JSON code block containing key takeaways, messages important to the speaker, and a third category: the relationship to the Atonement of Jesus Christ. This produced a readable Markdown response and a structured JSON summary of a BYU devotional.

I found that when asking for JSON the agent typically was pretty faithful in ensuring it's output was only JSON. Rarely did I get responses in other formats. When I didn't give clear examples and followed a "no-shot" prompting style, mileage definitely varied. Additionally, the newer models were much better at giving a thorough summary and giving examples from the text itself. Older models gave a more conceptual summary of the devotional.

## Additional Exploration

I compared several models, including `gpt-4o-mini`, `gpt-4.1-nano`, `gpt-5.6-luna`, `gpt-5.6-terra`, and `gpt-5.6-sol`, asking each of these to summarize my a BYU devotional using various prompt techniques (no-shot and multi-shot prompting). In particular, I compared `gpt-5.6-luna` and `gpt-5.6-sol`. For roughly 4,800 input tokens, Luna cost about $0.0013 and Sol cost about $0.03, making Sol roughly 20 to 25 times more expensive in these runs. Both created useful structured summaries, while Sol generally gave a more complete and polished response. Luna was a much better value when concise extraction was sufficient. I thought it was interesting that the older models followed my EXACT instructions and only provided json with fields exact to my prompt instructions. Newer models treated my JSON as a guideline but not a barrier.

I explored shell redirection by running commands such as `python agent.py prompt3.md > output4.md`. I updated the agent so redirected output creates a transcript containing both `USER:` messages and streamed `AGENT:` responses.

## Obstacles

Initially, VS Code could not resolve the `dotenv` or `openai` imports. I installed `python-dotenv` and `openai`, created a local `.venv`, and selected that interpreter for the workspace.

My first conversation-history attempt used a `history` argument with the Responses API, but that is not a supported parameter. I corrected it by passing the history list as `input`.

## What I Learned
I learned that streaming produces a sequence of typed events, so text can be displayed from delta events while the final response object is retained for metadata and future context.

I learned that client-side conversation history must use the API's supported request shape. Finally, I learned that prompt formatting can guide a model toward a valid JSON result, but a JSON Schema is needed when an application must guarantee a stable output contract.

## Relevance to Agent Engineering

An agent is more than a single model call. It needs a reliable runtime environment, conversation state, structured output contracts, incremental output, graceful session handling, observability through usage data, and reproducible artifacts such as transcripts. These experiments show how these details can influence response quality. Additionally, fast prompt reproducibility makes it much easier to examine the boundaries of a given model.
## Time Spent

Hours spent: 3.0
