from abc import ABC, abstractmethod

class AbstractConnector(ABC):

	def __init__(self):
		super().__init__()

	@abstractmethod
	def get_data(self, filepath):
		pass

	@abstractmethod
	def parse_data(self):
		pass

	@abstractmethod
	def convert_data(self):
		pass