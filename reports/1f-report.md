# Homework 1f Report

## Overview

I added tool calling to my chatbot. I used `tools.py`'s `ToolBox` decorator written by Dr. Bean to turn Python functions into OpenAI function tools, and changed `agent.py` so that each user message runs through `run_turn`. That function keeps calling the model until it stops asking for tools. For each `function_call` item, it runs the matching Python function and sends the result back as a `function_call_output` with the same `call_id`.

I built three tools:

- `random_int(low, high)`: returns a real random integer.
- `fetch_url(url)`: downloads a web page and returns its text.
- `get_conference_index()`: fetches the April 2026 General Conference index and lists each talk as `title | speaker -> URL`. October 2026 has not happened yet, so April 2026 is the most recent conference.

The quote finder uses a developer prompt (`prompts/1f/gc_quote.md`). It tells the model to get the index, find the speaker's URL, fetch the talk, and reproduce the matching passage verbatim.

## Random Numbers: Tools vs. No Tools

Without tools (`random1.md`), the model's "random" numbers were clearly not random. When asked for 20 numbers between 1 and 10, it returned every number from 1 to 10 exactly twice. A truly random draw almost never does that. It was producing numbers that *look* random rather than sampling them.

With the tool (`random.md`), the model called `random_int` for every request and got results with natural repeats (4 then 4, 7 appearing twice).

## General Conference Quote Finder

In `conference.md` I asked for Elder Kearon's story about being called as assistant ward clerk. The model found his talk, "About His Business," and returned a full paragraph with the correct URL. I then asked about Elder Bednar's latest talk. The model summarized "All Who Have Endured Valiantly" and followed up with five more quotes when asked. I verified all quotes and the they were verbatim. Although the model did not use italicize or bold conventions for some of the words that the talk itself did.

When I asked whether a line was a quote or a summary, the model said it was verbatim, which was true. However, in its first Bednar answer it mixed its own summary and a real quote in the same response. The blockquote formatting was the only thing separating them.

## Takeaways

- Tools fix things models are bad at, especially when you need a deterministic (or truly non-deterministic in the case of a random number generator) output.
- Simple tools worked well. Plain-text page content was enough for the model to find speakers and passages.
- Verbatim quoting was reliable because the model had the real text in context instead of recalling it from memory.
