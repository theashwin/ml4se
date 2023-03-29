import json
import sys

import openai

# GET YOUR OPEN AI API KEY FROM : https://platform.openai.com/account/api-keys
# Save the key in config.json as { "OPENAI_API_KEY": "<KEY>" }

from prompt.reasoning import Reasoning
from prompt.tests import Tests
from prompt.refactor import Refactor

with open("config.json", "r") as file:
    config = json.loads(file.read())

openai.api_key = config["OPENAI_API_KEY"]


# Python

def chat(i, task, out):
    init = task.get_init_prompt()

    task_prompt = [
        {
            "role": "system",
            "content": init
        }
    ]

    idx = 1
    out.append(init)
    while True:
        prompt = task.generate_prompt(idx)

        # To print the method body inside a code block in the output Markdown
        if idx == 1:
            out.append(prompt)
            out.append("```")
            out.append(task.get_code())
            out.append("```")

        prompt += task.get_code() if idx == 1 else ""

        task_prompt.append({
            "role": "user",
            "content": prompt
        })

        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=task_prompt
        )

        reply = chat.choices[0].message.content

        if idx > 1:
            out.append(prompt)
        out.append(reply)

        idx += 1
        task_prompt.append({"role": "assistant", "content": reply})

        if not task.parse_response(idx, reply):
            task.store(i, out)
            break


def reasoning(i, data_json, out, lang):
    out.append("# Reasoning")
    reasoning = Reasoning(i, data_json, lang)
    out.append("---")
    chat(i, reasoning, out)


def tests(i, data_json, out, lang):
    out.append("# Tests")
    tests = Tests(i, data_json, lang)
    out.append("---")
    chat(i, tests, out)


def refactor(i, data_json, out, lang):
    out.append("# Refactoring")
    refactor = Refactor(i, data_json, lang)
    out.append("---")
    chat(i, refactor, out)


def read_data(data_path):
    # Load Dataset
    with open(data_path) as file:
        data = json.load(file)

    return data


# Check if the 2nd argument is either java or python. If not then select default lang as java
try:
    lang = sys.argv[1].lower()
    if lang not in ['java', 'python']:
        lang = 'java'
except:
    lang = 'java'

print(f'Running the utility for {lang.upper()} language code snippets')
data_path = "prompt/json/" + lang + ".json"
data_json = read_data(data_path)

for i in range(len(data_json)):
    # Reasoning
    out = []
    print(f'Started REASONING task for the {i + 1}th object...')
    reasoning(i + 1, data_json[i], out, lang)
    print(f'Started UNIT TEST GENERATION task for the {i + 1}th object...')
    tests(i + 1, data_json[i], out, lang)
    print(f'Started SEMANTICALLY EQUIVALENT CODE GENERATION task for the {i + 1}th object...')
    refactor(i + 1, data_json[i], out, lang)
    print()
    break

print(f'Task Completed')
