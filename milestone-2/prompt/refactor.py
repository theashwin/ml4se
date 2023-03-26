import json

from prompt.prompt import Prompt


class Refactor(Prompt):
	path = "prompt/json/refactor.json"

	def __init__(self, idx, data_path):
		self.idx = idx
		# Load Prompts
		with open(self.path) as file:
			self.prompt = json.loads(file.read())

		# Load Dataset
		with open(data_path) as file:
			self.data = json.loads(file.read())

	def parse_response(self, prompt_idx, response):
		# Idea here is to check the response from GPT and make sure it makes sense, else give additional prompts
		# to get the correct response.

		if len(self.prompt) <= prompt_idx:
			return False
		# Returns True if prompt is parsed else False, give additional prompts if False
		return True

	def store(self, idx, out):
		with open("out/python/" + str(idx) + ".md", "w") as file:
			file.write("\n\n".join(out))