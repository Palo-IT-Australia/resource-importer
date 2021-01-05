from abc import ABC, abstractmethod

class AbstractGenerator(ABC):

	def __init__(self):
		super().__init__()

	@abstractmethod
	def transform_data(self, data):
		pass

	@abstractmethod
	def save_data(self, filename):
		pass