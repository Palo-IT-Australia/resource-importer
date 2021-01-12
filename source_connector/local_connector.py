from source_connector.abstract_connector import AbstractConnector
from data.resource import Resource

class LocalConnector(AbstractConnector):

	def __init__(self):
		super().__init__()
		self.data = None
		self.parsed_data = None
		self.parser = None

	def get_data(self, parser, filepath):
		self.parser = parser
		self.parser.open_file(filepath)
			
	def parse_data(self):
		self.parsed_data = self.parser.parse()

	def convert_data(self):
		return [ Resource(element['name'], element['value'], element['description']) for element in self.parsed_data ]