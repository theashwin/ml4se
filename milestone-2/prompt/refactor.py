import json

from prompt.prompt import Prompt


class Refactor(Prompt):
	path = "prompt/json/refactor.json"

	def __init__(self, idx, data, lang):
		self.idx = idx
		self.data = data
		self.lang = lang
		# Load Prompts
		with open(self.path) as file:
			self.prompt = json.loads(file.read())

		# Replace the <LANG> with java or python
		self.prompt['init'] = self.prompt['init'].replace('<LANG>', lang)

	def parse_response(self, prompt_idx, response):
		# Idea here is to check the response from GPT and make sure it makes sense, else give additional prompts
		# to get the correct response.

		if len(self.prompt) <= prompt_idx:
			return False
		# Returns True if prompt is parsed else False, give additional prompts if False
		return True

	def store(self, idx, out):
		# Writing to a file based on the language passed in the command line
		with open("out/" + str(self.lang) + "/" + str(idx) + ".md", "w", encoding="utf8") as file:
			file.write("\n\n".join(out))