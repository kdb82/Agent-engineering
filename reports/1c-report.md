# Homework 1C Report

## Chatbot Implementation

I added `while` loop to read one user message at a time in my `agent.py`. It appends that message and each completed model response to a `history` list, and sends the complete history with the next API request. The program supports an optional prompt file and streams responses to the terminal. When standard output is redirected, it writes a reproducible transcript with `USER:` and `AGENT:` labels. This made it possible to save agent/user conversations as transcripts.

## Hidden-Instruction Prompt

My prompt is in `secret-game.md`. The game is similar to the "cat, dog, bird" game model. The prompt specifies the state transitions, plural and inflection handling, out-of-order failure behavior, a fifteen-message limit, and the required success message. The user is not told the sequence or the game objective.

## Conversation Results

The four saved conversations are included as `test1.md` through `test4.md`.

- In `test1.md`, a real participant discussed pets and eventually mentioned "our dog" before the agent had obtained `cat`. The agent correctly declared failure when the later target appeared out of order. The strategic mistake was asking broad animal questions, which allowed the participant to introduce an uncontrolled target word.
- In `test3.md`, the agent repeatedly forced animal and mascot trivia into a conversation about college football. The user recognized the pattern and challenged the unnatural topic changes. Although the agent later explained the failure accurately, the attempt demonstrated that conspicuous prompting undermines the game before the sequence can be completed.
- In `test4.md`, the successful restarted attempt used varied, contextually related wording. `CAT` appeared as a reverse complement in a bioinformatics discussion, `dog` appeared as the first k-mer of `DOGMA`, and `bird` appeared in the proverb "the early bird gets the worm." The agent announced the required win message after the ordered sequence. This was more natural than repeatedly asking about animals, though the user still noticed some abrupt transitions.

For each subsequent test, I appended the history of the last test after asking the agent to analyze it's own failures with the hopes that it might vary it's approaches and get better results. Initially it was very aggressive with it's responses in order to achieve the objective. Later on in began adding more nuance to it's strategies. Overall it's hard to say that it "learned" because I had to guide it a bit in its analysis to fix its mistakes.

## Things Learned

I think the biggest things I learned and started thinking about in the broader context of agent engineering is how to manage context, and how context can impact an agent's performance (whether for better or worse).

## Submission Contents

The submission archive contains `agent.py`, `secret-game.md`, `test1.md`, `test2.md`, `test3.md`, `test4.md`, and this report. The prompt and transcripts provide the requested prompt and example conversations.

## Time Spent

3.2 hours
