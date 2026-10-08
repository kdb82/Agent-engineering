# 1g Homework

### Tooling additions
I edited my agent.py to include 4 different tools. These included:
- write: writing files within the user's filesystem
- read: reading files from the user's filesystem
- edit: edit files within the user's filesystem
- bash: run bash commands in a separate bash subprocess

These 4 tools allowed the agent to interact with my computer directly. There are pros and cons to this. The agent gains a lot of power and because LLMs aren't inherently deterministic, it may make decisions I didn't plan for that have real consequences to my filesystem. However, despite this, it does make the agent much more powerful when it comes to interacting and making real world software. Some additional safeguards, tools may make it more useful to run autonomously in a safer way (like the "manual" mode that codex already has).

### Testing
Just to prove it works I asked my agent to write a poem and put that poem in a specific directory. All tool calls it used are within the transcript for that conversation. It correctly identified the directory and was able to write my poem.

### Additional Thoughts
Given enough time, I think I could build an agent that has capabilities comparable to Codex's or Claude's own apps. It would be just a matter of adding some additional built-in tools (like a web search), that would extend it's functionality. Doing this would allow me to leverage the model while injecting my own system prompts into the request to make it behave differently.