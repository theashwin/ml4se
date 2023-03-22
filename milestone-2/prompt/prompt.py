from abc import ABC, abstractmethod


class Prompt(ABC):

	@abstractmethod
	def generate_prompt(self):
		pass

	@abstractmethod
	def parse_response(self):
		pass

	@abstractmethod
	def store(self):
		pass
