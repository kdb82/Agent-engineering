# 2b-Report

## App iteration 1
The app I decided to build was a small chrome extension that allowed me to open any webpage, control a small stick figure on that webpage, and shoot pixelated guns to destroy the various elements of that page. Initially I just wrote a prompt in `game.md` and sent the agent off to implement the app based off that prompt. The agent did a decent job accomplishing my intention. However it didn't really address some obvious edge cases that were important to the functionality of the game. 

## App iteration 2
For the second iteration I wrote a python script that controlled 4 subagents that I designed with specific roles. These agents included:

- a planning agent
- an implementation agent
- a reviewer agent
- an architectural design agent

These each had specific roles and passed json output as input to the next agent. They iterated multiple times to accomplish the task. 

## Observations
I noticed that the development cycle took much longer compared to the first iteration. It was also more expensive token wise because multiple agents had to read context independently and do their own research. 

The benefit of this style was that their were fewer bugs, and the agents addressed the edge cases the first iteration missed without me needing to even say anything. Overall the second iteration was better and the dev experience was more fine tuned. But it did come at a runtime cost. 

Both iterations were given the same `game.md` prompt. 