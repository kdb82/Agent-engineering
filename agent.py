from dotenv import load_dotenv
import argparse
import sys
from pathlib import Path
from time import time
from usage import print_usage
from openai import OpenAI


load_dotenv()

def main(model, reasoning, prompt=None):
    # models_by_cost = ["gpt-4o-mini", "gpt-5.6-luna", "gpt-5.6-terra", "gpt-5.4", "gpt-5.6-sol", ]
    client = OpenAI()
    usage = []
    # history = [{"role": "user", "content": prompt if prompt else "You are a helpful AI assistant."}]
    history = []
    usr_msg = prompt
    writing_transcript = not sys.stdout.isatty()

    try:
        while True:
            if usr_msg is None:
                if writing_transcript:
                    print("USER: ", end="", file=sys.stderr, flush=True)
                    usr_msg = sys.stdin.readline().rstrip("\n")
                else:
                    usr_msg = input("USER: ")
            if usr_msg == "exit" or usr_msg == "":
                break

            if writing_transcript:
                print(f"USER: {usr_msg}", flush=True)
                
            # create request object for the OpenAI API
            history.append({"role": "user", "content": usr_msg})
            start = time()
            request: dict = {
                "model": model,
                "input": history,
                "instructions": "if any code is written, syntax should be valid for that language.",
                "reasoning": reasoning,
                "stream": True,
            }

            # Print response as it streams in
            stream = client.responses.create(**request)
            response = None
            print("\nAGENT: ", end="", flush=True)
            for event in stream:
                if event.type == "response.output_text.delta":
                    print(event.delta, end="", flush=True)
                elif event.type == "response.completed":
                    response = event.response

            print()

            if response is not None:
                usage.append((model, response.usage))
                history.extend(response.output)

            print(f'{round(time()-start, 2)} seconds elapsed\n', file=sys.stderr)
            usr_msg = None

    finally:
        print_usage(usage)

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