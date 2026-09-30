from dotenv import load_dotenv
import argparse
import sys
from pathlib import Path
from time import time
from usage import print_usage
from openai import OpenAI
from tools import ToolBox
import json
import random

load_dotenv()

toolbox = ToolBox()

@toolbox.tool
def random_int(low: int, high: int) -> int:
    """Return a random integer in [low, high] inclusive."""
    return random.randint(low, high)

def run_turn(client, model, reasoning, history, usage, toolbox, instructions):
    while True:
        stream = client.responses.create(
            model=model,
            input=history,
            instructions=instructions,
            reasoning=reasoning,
            tools=toolbox.tools,
            stream=True,
        )
        response = None
        for event in stream:
            if event.type == "response.output_text.delta":
                print(event.delta, end="", flush=True)
            elif event.type == "response.completed":
                response = event.response
        if response is None:
            return

        usage.append((model, response.usage))
        history.extend(response.output)

        calls = [item for item in response.output if item.type == "function_call"]
        if not calls:
            print()
            return
        for call in calls:
            func = toolbox.get_tool_function(call.name)
            try:
                result = func(**json.loads(call.arguments)) if func else f"Unknown tool {call.name}"
            except Exception as e:
                result = f"Error: {e}"
            print(f"\n[tool] {call.name}({call.arguments})", file=sys.stderr)
            history.append({
                "type": "function_call_output",
                "call_id": call.call_id,
                "output": str(result),
            })

INSTRUCTIONS = "if any code is written, syntax should be valid for that language. All responses should be valid markdown syntax."

def loop(client, model, reasoning, history, usage, writing_transcript, toolbox):
    try:
        while True:
            if writing_transcript:
                print("USER: ", end="", file=sys.stderr, flush=True)
                usr_msg = sys.stdin.readline().rstrip("\n")
            else:
                usr_msg = input("USER: ")
            if usr_msg == "exit" or usr_msg == "":
                break

            if writing_transcript:
                print(f"USER: {usr_msg}", flush=True)

            history.append({"role": "user", "content": usr_msg})
            start = time()
            print("\nAGENT: ", end="", flush=True)
            run_turn(client, model, reasoning, history, usage, toolbox, INSTRUCTIONS)
            print(f'{round(time()-start, 2)} seconds elapsed\n', file=sys.stderr)
    finally:
        print_usage(usage)

def main(model, reasoning, prompt=None):
    # models_by_cost = ["gpt-4o-mini", "gpt-5.6-luna", "gpt-5.6-terra", "gpt-5.4", "gpt-5.6-sol", ]
    client = OpenAI()
    usage = []
    history = (
        [{"role": "developer", "content": prompt}]
        if prompt
        else []
    )
    writing_transcript = not sys.stdout.isatty()

    loop(client, model, reasoning, history, usage, writing_transcript, toolbox)

if __name__ == "__main__":
    parser = argparse.ArgumentParser('AI Response')
    parser.add_argument('prompt_file', nargs='?', type=Path)
    parser.add_argument('--model', default='gpt-5.6-luna')
    parser.add_argument('--reasoning', choices=('none', 'minimal', 'low', 'medium', 'high', 'xhigh', 'max'), default='low')
    args = parser.parse_args()
    reasoning_models = {"gpt-5.6-luna", "gpt-5.6-terra", "gpt-5.4", "gpt-5.6-sol"}
    reasoning = {"effort": args.reasoning} if args.model in reasoning_models else None
    prompt = args.prompt_file.read_text() if args.prompt_file else None
    main(args.model, reasoning, prompt)