import json
import sys
import argparse
import openai

# GET YOUR OPEN AI API KEY FROM : https://platform.openai.com/account/api-keys
# Save the key in config.json as { "OPENAI_API_KEY": "<KEY>" }

from prompt.reasoning import Reasoning
from prompt.tests import Tests
from prompt.refactor import Refactor

with open("config.json", "r") as file:
    config = json.loads(file.read())

openai.api_key = config["OPENAI_API_KEY"]


def add_code_details(task, prompt, out):
    out.append(prompt)
    out.append("> ### Method under consideration:\n"
               "> **func_id** : " + task.get_func_id() + " <br/> \n "
               "> **repository** : " + task.get_project_repo() + " <br/> \n" +
               "> **location** : " + task.get_location() + " <br/> \n"
               "> **flag** : " + task.get_flag() + " <br/> \n" +
               "> **function** : <br/> \n"
               "> ``` <br/> \n"
               ">> " + task.get_code().replace('\n', '\n>') + " \n"
               "> ``` \n")


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
            add_code_details(task, prompt, out)

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


# Get lang argument and check is either java or python. If not then select default lang as java
p = argparse.ArgumentParser()

p.add_argument('--lang', '--language', dest='lang', default='java', help='language')

args = p.parse_args()
lang = args.lang.lower()

if lang not in ['java', 'python']:
    lang = 'java'

print(f'Running the utility for {lang.upper()} language code snippets')
data_path = "prompt/json/" + lang + ".json"
data_json = read_data(data_path)
all_threads = []

for i in range(len(data_json)):
    out = []
    # Reasoning
    print(f'Started REASONING task for the {i + 1}th object...')
    reasoning(i + 1, data_json[i], out, lang)
    # Unit test
    print(f'Started UNIT TEST GENERATION task for the {i + 1}th object...')
    tests(i + 1, data_json[i], out, lang)
    # Semantically equivalent code
    print(f'Started SEMANTICALLY EQUIVALENT CODE GENERATION task for the {i + 1}th object...')
    refactor(i + 1, data_json[i], out, lang)
    print()
    break

print(f'Task Completed')
