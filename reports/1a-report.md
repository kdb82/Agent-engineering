# Homework Report - 1a

disclaimer - the numbered lists are organized as my responses to the 3 sections in the instructions. Each number in this report follows the corresponding section number.

1. My app is submitted in `agent.py`. It uses `usage.py` to print token usage and estimate costs. The agent accepts either an optional prompt file or an interactive prompt entered in the terminal. .

### Prompts
2.  I used several prompts to test code generation, instruction-following, and different model/reasoning settings. The saved `.py` and `.txt` artifacts provide evidence of these experiments:
    - I asked it to rank movies based off of 3 criteria "Story: plot clarity, pacing, originality, and how satisfying the ending is. Performances: how convincing and engaging the actors are in their roles.Technical quality: cinematography, editing, sound, visual effects, and production design." I used the same movies across various models to see if they classified them differently. I found that `gpt-4o-mini` had a preference for action movies. Newer models ranked drama's higher.
    - Fibonacci generation: I asked for a Python program that generates the first $n$ Fibonacci numbers. I wanted to see if different models had different approaches to the code itself. All of the newer models had almost identical code. Older models in the `gpt-4` family varied a bit more.
    - I asked for a Python program to "solve world hunger". I wanted to test the limits of what it would try to do. For all models I tested (sol, luna, and gpt-4o-mini), they wrote code addressing the needs of a very small civilization of about 4 towns they each made up. It was a deterministic program moving food stocks from these towns. Interestingly, `gpt-sol`'s program was much shorter than the older models. Additionally at the time I had instructed the agent to always speak in caveman. I wanted to see if that would change the quality of the code. The code didn't change much, just the comments did. 


### Other testing
---

3. 
    - I did various prompts asking: "day did Martin Luther King die?" to test if it would hallucinate the day. I didn't get any hallucinations from the models I tested. Including from the older models in the `gpt-4` family.
    - Large sequential output: I asked for output containing a long sequence of numbers. `output.txt` which I generated with it contains the comma-separated integers from `1` through `1000`, showing that the agent handled a response with a large amount of structured output. `gpt-4o-mini` would skip hundreds of numbers at a time while `gpt-5.6-luna` did not. 

    here's the prompt and response: 
    Prompt: count to 1000, don't skip any numbers

    Ugh! Counting big! Here go:

    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,  
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,  
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,  
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40,  
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50,  
    51, 52, 53, 54, 55, 56, 57, 58, 59, 60,  
    61, 62, 63, 64, 65, 66, 67, 68, 69, 70,  
    71, 72, 73, 74, 75, 76, 77, 78, 79, 80,  
    81, 82, 83, 84, 85, 86, 87, 88, 89, 90,  
    91, 92, 93, 94, 95, 96, 97, 98, 99, 100,  
    ...  
    Big long going, 101, 102, 103, ...  
    Keep counting!  
    ...  
    990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000!  

    Ugh! Big number! All done!

    10.36 seconds elapsed
    ----------- Usage ------------
    ~~~~~~~~~gpt-4o-mini~~~~~~~~~~
    Input (tokens): 46
    Output (tokens): 376
    No pricing rates configured for model gpt-4o-mini
    gpt-4o-mini cost (USD): $0.000000
    No pricing rates configured for model gpt-4o-mini
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Total cost (USD): $0.000000

Other outputs I created were poems, and a report about the purpose of the existence of ai. 

The biggest obstacle I encountered was trying to configure my agent so that I could correctly use a file for prompting, or read directly from stdin if I didn't include a file. That's just because my python is a little rusty. I also spent additional time reading [this article](https://hackerfactor.com/blog/index.php?/archives/1103-The-Most-Important-Lesson.html) about extensive testing on various models in a D&D style game. This link was shared by Dr. Bean. I thout it was interesting seeing how various models exhibited certain "personality traits" while being tested in this game. However one thing in common was that almost all of them would keep playing regardless if they kept failing the test. When humans were asked the same questions it didn't take long for them to recognize the pattern and either stop playing or launch into a separate tangent. I spent around 3.5 hours on the homework. Overall I gained a better grasp of the limitations and strengths of various generations of models.