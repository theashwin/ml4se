import json

from prompt.prompt import Prompt


class Tests(Prompt):
	path = "json/reasoning.json"

	def __init__(self):
		with open(self.path) as file:
			self.prompt = json.loads(file.read())

	def parse_response(self, response):
		# Returns True if prompt is parsed else False, give additional prompts if False
		return True

	def store(self):
		pass
