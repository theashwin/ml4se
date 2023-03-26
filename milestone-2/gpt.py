import json

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

		out.append(prompt)
		out.append(reply)

		idx += 1
		task_prompt.append({"role": "assistant", "content": reply})

		if not task.parse_response(idx, reply):
			task.store(i, out)
			break


def reasoning(i, data_path, out):
	out.append("# Reasoning")
	reasoning = Reasoning(i, data_path)
	out.append("---")
	chat(i, reasoning, out)


def tests(i, data_path, out):
	out.append("# Tests")
	tests = Tests(i, data_path)
	out.append("---")
	chat(i, tests, out)


def refactor(i, data_path, out):
	out.append("# Refactoring")
	refactor = Refactor(i, data_path)
	out.append("---")
	chat(i, refactor, out)


data_path = "prompt/json/python.json"
for i in range(1, 51):
	# Reasoning
	out = []
	reasoning(i, data_path, out)
	tests(i, data_path, out)
	refactor(i, data_path, out)

	break
