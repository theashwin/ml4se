from abc import ABC, abstractmethod


class Prompt(ABC):
	prompt = None
	data = None
	idx = 1
	lang = None

	@abstractmethod
	def parse_response(self, prompt_idx, response):
		pass

	@abstractmethod
	def store(self, idx, store):
		pass

	def get_init_prompt(self):
		return self.prompt['init']

	def generate_prompt(self, idx=0):
		if len(self.prompt) <= idx:
			return None
		return self.prompt[str(idx)]

	# Dataset
	def get_code(self):
		return self.data['function']

	# def get_comment(self):
	# 	return self.data[str(self.idx)]['comment']
