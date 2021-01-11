from util.token_credentials import TokenCredentials
from source_connector.abstract_connector import AbstractConnector
from data.resource import Resource
from googleapiclient.discovery import build

class GoogleSheetsConnector(AbstractConnector):

	def __init__(self, service, version, filepath):
		super().__init__()
		self.data = None
		self.parsed_data = []
		self.service = service
		self.version = version
		self.filepath = filepath

	def get_data(self, sheet_id, range):
		token_credentials = TokenCredentials()
		token_credentials.get_credentials(self.filepath)

		service = build(self.service, self.version, credentials=creds)

		sheet = service.spreadsheets()
	    result = sheet.values().get(spreadsheetId=sheet_id,
	                                range=range).execute()

	    self.data = result.get('values', [])

	def parse_data(self):
		if self.data:
			for row in self.data:
				self.parsed_data.append({'name': row[1], row[4]})

	def convert_data(self):
		return [ Resource(element['name'], element['value']) for element in self.parsed_data ]