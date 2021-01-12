from util.xml_generator import XmlGenerator
from util.name_converter import NameConverter
from data.resource import Resource
from data_generator.abstract_generator import AbstractGenerator

class AndroidResourceGenerator(AbstractGenerator):

	def __init__(self):
		super().__init__()
		self.xmlGenerator = None
		self.nameConverter = NameConverter("Android")

	def _convert_naming(self, data):
		converted_data = []
		for element in data:
			converted_data.append(
				Resource(
					self.nameConverter.convert_dots_to_snake_case(element.name),
					self.nameConverter.replace_string_templates(element.value),
					element.description
					)
				)
		return converted_data

	def transform_data(self, data):
		self.xmlGenerator = XmlGenerator(self._convert_naming(data))
		self.xmlGenerator.generate_xml()

	def save_data(self, filename):
		self.xmlGenerator.write_xml(filename)