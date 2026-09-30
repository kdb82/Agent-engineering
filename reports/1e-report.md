# Homework 1e Report

## Overview

This assignment tested reasoning models on basic mathematics and logic puzzles. I compared a simple math session with no reasoning effort against several attempts at a six-house logic puzzle using `medium` and `xhigh` reasoning. I also compared the resulting time, token usage, cost, and correctness.

The main result is that reasoning was much more useful for the logic puzzle than for the basic math questions. However, more reasoning did not guarantee correctness by itself. The model sometimes produced a confident, well-formatted answer that violated one of the clues. The most reliable answers came from longer reasoning runs plus checking every clue explicitly.

## Experiments

### Basic math

The no-reasoning session covered a percentage calculation, a quadratic equation, and an expected-value question. All three were answered correctly, suggesting that visible reasoning was unnecessary for these short, familiar problems.

### Five-house logic puzzle

The simpler of my two logic puzzles involved five houses, residents, pets, drinks, and thirteen clues. The runs produced conflicting conclusions: one incorrectly claimed the clues were inconsistent, while a medium-reasoning run produced a table that appears to satisfy them. The puzzle benefited from reasoning because an early plausible placement can make a later clue impossible; case analysis or exhaustive verification is needed.

All runs for this puzzle were done with `luna`.

### Six-house logic puzzle

The more complex puzzle added house colors and several exclusive-or clues. A medium-reasoning run on `gpt-5.6-luna` confidently produced an invalid answer: coffee was in house 5 while blue was in house 1, violating the clue that coffee must be left of blue. Longer `xhigh` reasoning on the same model and a `medium` run on `gpt-5.6-sol` produced the same valid solution:

| House | Resident | Pet | Drink | Color |
|---:|---|---|---|---|
| 1 | Cara | turtle | coffee | red |
| 2 | Ben | rabbit | lemonade | black |
| 3 | Ava | cat | tea | white |
| 4 | Eli | fish | water | blue |
| 5 | Faye | bird | juice | yellow |
| 6 | Dev | dog | milk | green |

The strongest responses eliminated alternative placements and listed the truth value of every exclusive-or clue, making the final table easier to verify.

## Timing and Cost

The math session reported 891 input tokens, 325 output tokens, and a cost of `$0.000568`. The individual math responses took approximately 1.69, 2.55, 1.57, and 2.18 seconds, or about 2 seconds per request.

The recorded logic-puzzle runs were:

| Run | Settings | Time | Input tokens | Output tokens | Reasoning tokens | Cost |
|---|---|---:|---:|---:|---:|---:|
| `logic1` | medium | 32.04 s | 265 | 3,021 | 1,804 | `$0.003678` |
| `logic1` second attempt | medium | 36.06 s | 3,773 | 3,951 | 2,677 | `$0.005496` |
| `logic2` | medium | 33.02 s | 273 | 3,602 | 2,685 | `$0.004377` |
| `logic3` | medium | 53.88 s | 635 | 5,572 | 4,142 | `$0.006813` |
| `logic4` | xhigh | 303.49 s | 635 | 32,591 | 30,560 | `$0.039236` |
| `logic5` | `gpt-5.6-sol`, medium | 141.89 s | 635 | 8,902 | 7,398 | `$0.180580` |

This gives me some practical intuition:

- A medium-reasoning logic response took roughly 15 to 25 times as long as one basic math response.
- The `xhigh` run took about 150 times as long as a basic math response.
- The `xhigh` run used approximately 30,560 reasoning tokens, compared with 2,685 reasoning tokens in one medium run.
- Compared with the math session's total cost, the medium `logic2` run cost about 8 times as much, the `xhigh` run about 69 times as much, and the `gpt-5.6-sol` run about 318 times as much. The last comparison is especially affected by the different model pricing.

My intuition after these experiments is that a basic response usually takes a few seconds and costs very little. A difficult constraint-solving problem can take tens of seconds with medium reasoning and several minutes with very high reasoning. Cost can increase by an order of magnitude or more, especially when the model spends thousands of hidden reasoning tokens and produces a long explanation.

## Where Reasoning Helps

Reasoning is most valuable when:

- Many constraints must be satisfied simultaneously.
- A wrong early assumption makes the rest of the answer inconsistent.
- The task requires case analysis, planning, or multi-step deduction.
- The answer needs to be checked against several conditions rather than merely generated.
- The prompt explicitly asks the model to explain why alternatives fail.

The six-house puzzle is a good example. The model needed to track people, pets, drinks, colors, adjacency, distance, ordering, and exclusive-or conditions at the same time. The successful answers used the extra reasoning budget to eliminate cases and verify the final table.

Reasoning was less important for the percentage calculation, quadratic equation, and expected-value question. These problems have short, familiar solution paths. A normal response could solve them correctly with a compact explanation.

## Where Reasoning Did Not Make a Clear Difference

More reasoning did not automatically improve reliability. The incorrect medium response to the six-house puzzle was presented with confidence and substantial detail. It failed a basic ordering clue that should have been checked directly.

The first five-house response also showed that extended prose can conceal an error. It announced that no solution existed while presenting conclusions that contradicted its own earlier deductions. More tokens created more explanation, but not necessarily more verification. This seems to be the classic "respond first, justify later" failure mode. This could have been mitigated by specifying in my output to reason first then come up with the solution.

