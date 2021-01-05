from util.string_generator import StringGenerator
from data_generator.abstract_generator import AbstractGenerator

class SwiftResourceGenerator(object):
	def __init__(self):
		super().__init__()
		self.stringGenerator = None

	def transform_data(self, data):
		self.stringGenerator = StringGenerator(data)
		self.stringGenerator.generate_strings_file()

	def save_data(self, filename):
		self.stringGenerator.write_strings_file(filename)