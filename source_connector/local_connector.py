from util.json_parser import JsonParser
from source_connector.abstract_connector import AbstractConnector
from data.resource import Resource

class LocalConnector(AbstractConnector):

	def __init__(self):
		super().__init__()
		self.data = None
		self.parsed_data = None

	def get_data(self, filepath):
		with open(filepath) as f:
			self.data = f.read()
			
	def parse_data(self):
		jsonParser = JsonParser(self.data)
		self.parsed_data = jsonParser.parse()

	def convert_data(self):
		return [ Resource(element['name'], element['value']) for element in self.parsed_data ]