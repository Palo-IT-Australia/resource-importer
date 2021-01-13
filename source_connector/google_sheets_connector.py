from util.token_credentials import TokenCredentials
from source_connector.abstract_connector import AbstractConnector
from data.resource import Resource
from googleapiclient.discovery import build

class GoogleSheetsConnector(AbstractConnector):

    def __init__(self, config):
        super().__init__()
        self.data = None
        self.parsed_data = None
        self.parser = None
        self.service = config['googleapi']['GoogleSheetsApi']
        self.version = config['googleapi']['GoogleSheetsVersion']
        self.credentials = config['googleapi']['GoogleApiCredentials']
        self.token = config['googleapi']['GoogleTokenFile']
        self.scopes = config['googleapi']['GoogleApiScopes']

    def get_data(self, parser, resource_id):
        self.parser = parser
        token_credentials = TokenCredentials()
        creds = token_credentials.get_credentials(self.token, self.credentials, self.scopes)

        service = build(self.service, self.version, credentials=creds)

        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=sheet_id,
                                    range=range).execute()

        self.data = result.get('values', [])

    def parse_data(self):
        self.parser.open_google_sheets(self.data)
        self.parsed_data = self.parser.parse()

    def convert_data(self):
        return [ Resource(element['name'], element['value']) for element in self.parsed_data ]