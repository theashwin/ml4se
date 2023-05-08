import json
import sys
import argparse
import openai
import time

# GET YOUR OPEN AI API KEY FROM : https://platform.openai.com/account/api-keys
# Save the key in config.json as { "OPENAI_API_KEY": "<KEY>" }

from prompt.reasoning import Reasoning
from prompt.data_control_mutation import DataControlMutation

with open("config.json", "r") as file:
    config = json.loads(file.read())

openai.api_key = config["OPENAI_API_KEY"]


def add_code_details(data, out):
    out.append("# Method Under Consideration")
    out.append("---")
    out.append("**func_id** : " + str(data['func_id']) + " <br/> \n "
               "**repository** : " + data['project_repo'] + " <br/> \n" +
               "**location** : " + data['location'] + " <br/> \n"
               "**flag** : " + data['flag'] + " <br/> \n" +
               "**function** : <br/> \n"
               "``` <br/> \n"
               "" + data['function'] + " \n"
               "``` \n")


def chat(i, task, out):
    init = task.get_init_prompt()

    task_prompt = [
        {
            "role": "system",
            "content": init
        }
    ]

    out.append("## Prompt")
    idx = 1
    # * are for italics
    out.append("**" + init + "**")
    while True:
        prompt = task.generate_prompt(idx)

        # To print the method body inside a code block in the output
        if idx == 1:
            out.append("**" + prompt + "**")
            out.append('```')
            out.append(task.get_code())
            out.append('```')

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

        if idx != 1:
            out.append("## Prompt")
            out.append("**" + prompt + "**")
        out.append("## Response")
        out.append(reply)

        idx += 1
        task_prompt.append({"role": "assistant", "content": reply})

        if not task.parse_response(idx, reply):
            task.store(i, out)
            return out[-1]
        time.sleep(20)

def extract_control_data(text):
    data = text.split("</DATA>")[0].split("<DATA>")[-1]
    control = text.split("</CONTROL>")[0].split("<CONTROL>")[-1]
    return [control, data]

def data_control(i, data_json, out, lang):
    out.append("# Task 1: Data Control")
    dc = DataControlMutation(i, data_json, lang)
    out.append("---")
    return extract_control_data(chat(i, dc, out))

def reasoning(i, data_json, out, lang, task):
    out.append(f"# Task 1: Reasoning for {task}")
    reasoning = Reasoning(i, data_json, lang)
    out.append("---")
    chat(i, reasoning, out)

def read_data(data_path):
    # Load Dataset
    with open(data_path, encoding='utf8') as file:
        data = json.load(file)

    return data


# Get lang argument and check is either java or python. If not then select default lang as java
p = argparse.ArgumentParser()

p.add_argument('--lang', '--language', dest='lang', default='java', help='language')
p.add_argument('--n', '--number', dest='num', default='5', help='number of data points to run', type=int)

args = p.parse_args()
lang = args.lang.lower()
num_data_pts = args.num

if lang not in ['java', 'python']:
    lang = 'java'


if num_data_pts > 50:
    num_data_pts = 50

print(f'Running the utility for {lang.upper()} code snippets')
print(f'Number of data points to run: {num_data_pts}')

data_path = "prompt/json/" + lang + ".json"
data_json = read_data(data_path)

for i in range(num_data_pts):
    out = []
    # Add code details to the md
    add_code_details(data_json[i], out)
    # Data Control Mutation
    print(f'Starting DATA CONTROL MUTATION task for the object #{i + 1}...')
    control, data = data_control(i + 1, data_json[i], out, lang)

    # Reasoning of Control Flow Mutated Function
    data_json[i]["function"] = control
    print(f'Starting REASONING task for the object #{i + 1}...')
    reasoning(i + 1, data_json[i], out, lang, "Control Flow Mutated Function")

    # Reasoning of Data Flow Mutated Function
    data_json[i]["function"] = data
    print(f'Starting REASONING task for the object #{i + 1}...')
    reasoning(i + 1, data_json[i], out, lang, "Data Flow Mutated Function")

    print()

print(f'Task Completed')
