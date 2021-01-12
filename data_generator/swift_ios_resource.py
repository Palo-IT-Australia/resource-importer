from util.string_generator import StringGenerator
from util.name_converter import NameConverter
from data.resource import Resource
from data_generator.abstract_generator import AbstractGenerator

class SwiftResourceGenerator(object):

	def __init__(self):
		super().__init__()
		self.stringGenerator = None
		self.nameConverter = NameConverter("iOS")

	def _convert_naming(self, data):
		converted_data = []
		for element in data:
			converted_data.append(
				Resource(
					element.name,
					self.nameConverter.replace_string_templates(element.value),
					element.description
					)
				)
		return converted_data

	def transform_data(self, data):
		self.stringGenerator = StringGenerator(self._convert_naming(data))
		self.stringGenerator.generate_strings_file()

	def save_data(self, filename):
		self.stringGenerator.write_strings_file(filename)