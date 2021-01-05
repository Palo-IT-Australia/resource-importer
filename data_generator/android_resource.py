from util.xml_generator import XmlGenerator
from data_generator.abstract_generator import AbstractGenerator

class AndroidResourceGenerator(AbstractGenerator):

	def __init__(self):
		super().__init__()
		self.xmlGenerator = None

	def transform_data(self, data):
		self.xmlGenerator = XmlGenerator(data)
		self.xmlGenerator.generate_xml()

	def save_data(self, filename):
		self.xmlGenerator.write_xml(filename)