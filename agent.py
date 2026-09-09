from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
models_by_cost = ["gpt-4o-mini", "gpt-5.6-luna", "gpt-5.6-terra", "gpt-5.4", "gpt-5.6-sol", ]
prices_per_million = {
    "gpt-4o-mini": {"input": 0.15, "output": 0.60},
    "gpt-5.6-luna": {"input": 0.20, "output": 1.20},
    "gpt-5.6-terra": {"input": 2.00, "output": 12.00},
    "gpt-5.4": {"input": 2.50, "output": 15.00},
    "gpt-5.6-sol": {"input": 4.00, "output": 20.00},
}
client = OpenAI()

model = models_by_cost[-1]
request = {
    "model": model,
    "input": "Write python code that finds the first n numbers of the fibonacci sequence given argument n from sys.argv.",
    "instructions": "return only valid python code, with no markdown code fences. If you have any explanations, include them as comments within the code."
}
if model.startswith("gpt-5"):
    request["reasoning"] = {"effort": "high"}

response = client.responses.create(**request)
print('\n' + response.output_text + '\n')

print(f'#model: {model}')
print("#----USAGE----")
usage_dict = response.usage.model_dump()
print(f"#Input tokens: {usage_dict['input_tokens']}")
print(f"#Output tokens: {usage_dict['output_tokens']}")
reasoning_tokens = usage_dict.get("output_tokens_details", {}).get("reasoning_tokens", 0)
print(f"#Reasoning tokens: {reasoning_tokens}")

rates = prices_per_million[model]
input_cost = usage_dict["input_tokens"] / 1_000_000 * rates["input"]
output_cost = usage_dict["output_tokens"] / 1_000_000 * rates["output"]
total_cost = input_cost + output_cost

print(f"#Estimated cost: ${total_cost:.8f}")