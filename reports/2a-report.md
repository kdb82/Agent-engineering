# Agent Engineering Report: WeekFeed

I built WeekFeed, a local web app that drafts standups and weekly updates from git commits and notes. It also answers questions about my own work history and manages todos and blockers through an AI agent with Undo. I built it with Claude Code in one long session: FastAPI and SQLite on the backend, React on the frontend. It ended with 189 backend tests and 19 frontend tests.

## 1. Customizing AGENTS.md
I used `CLAUDE.md`, Claude Code's version of AGENTS.md. It holds the domain language (label, scope, item, batch), the stack, module boundaries, testing rules, and invariants such as "the agent can only touch items in its label." I wrote it before any code was written.

## 2. Vibecoding the app
**What it did well**
- I used the skill creator to creat a brainstorming skill that helped me brainstorm ideas along with aggressively ask me clarifying questions regarding the spec and implementation. The spec stayed useful: I built from it, and updated it whenever the code deviated.
- Test-first work gave a fully offline suite, using a scripted fake LLM and real temporary git repos.
- Checking the running app caught problems the unit tests couldn't. Clicking through in a browser and running one real OpenAI call were both worth it.
- It handled packages newer than its training knowledge (TypeScript 7, React Router 8) by testing them rather than assuming.

**What it did poorly**
- It over-explained basic web development until I told it to stop, and it only explained unfamiliar libraries after that.
- It's first UI proposal was too complex and had major feature-creep. I replaced it with a simple three-page layout after giving it a screenshot and further direction.
- It shipped two bugs the tests missed. Dates were shown in UTC, so an evening commit showed as the next day. And Undo reverted the todo but left it in the draft text. Both were fixed afterwards.
- It had small slips: a stray helper function, a README test count that was off by one, and a macOS command that doesn't exist.
- The fake LLM could not show whether the real model would behave. Only the real-API run did.

## 3. Do skills make a difference?
This isn't a controlled comparison; it's what I observed.
- Once the brainstorming skill was triggered, it then shaped the whole project: one question at a time, then design, then spec.
- A separate writing-plans skill I had installed previously triggered when I asked for a plan. I then told it to skip the plan, and the build still went smoothly because the spec was detailed. That suggests the spec mattered more than the plan.
- I have no run without skills to compare against.

## 4. Experimenting with instructions
- A saved memory of my preferences carried across context resets.

 One observation is that the spec-first approach spent many tokens up front, but there was little rework once coding started. The session's context also ran out once and had to be compacted.

## 5. Final project ideas
WeekFeed itself is a candidate and is already prototyped as v1. Ideas I noted but did not prototype:
- Streaming responses.
- A per-project switch to keep that project's data from being sent to OpenAI.
- Meaning-based (embedding) search in place of keyword search.

