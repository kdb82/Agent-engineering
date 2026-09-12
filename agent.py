from dotenv import load_dotenv
import argparse
import sys
from pathlib import Path
from time import time
from usage import print_usage
from openai import OpenAI


load_dotenv()

def main(model, reasoning, prompt=None):
    start = time()
    models_by_cost = ["gpt-4o-mini", "gpt-5.6-luna", "gpt-5.6-terra", "gpt-5.4", "gpt-5.6-sol", ]
    client = OpenAI()

    if not model:
        model = models_by_cost[-1]
    if not prompt:
        print("Prompt: ", end="", file=sys.stderr, flush=True)
        prompt = sys.stdin.readline().rstrip("\n")
    request: dict = {
        "model": model,
        "input": prompt,
        "instructions": "if any code is written, syntax should be valid for that language.",
    }
    if reasoning is not None:
        request["reasoning"] = reasoning

    response = client.responses.create(**request)
    print('\n' + response.output_text + '\n')

    print(f'{round(time()-start, 2)} seconds elapsed', file=sys.stderr)
    print_usage([(model, response.usage)])

if __name__ == "__main__":
    parser = argparse.ArgumentParser('AI Response')
    parser.add_argument('prompt_file', nargs='?', type=Path)
    parser.add_argument('--model', default='gpt-5.6-luna')
    parser.add_argument('--reasoning', choices=('low', 'medium', 'high'), default='low')
    args = parser.parse_args()
    reasoning_models = {"gpt-5.6-luna", "gpt-5.6-terra", "gpt-5.4", "gpt-5.6-sol"}
    reasoning = {"effort": args.reasoning} if args.model in reasoning_models else None
    prompt = args.prompt_file.read_text() if args.prompt_file else None
    main(args.model, reasoning, prompt)