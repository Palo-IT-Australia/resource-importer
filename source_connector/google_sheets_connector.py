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
        self.config_sheets = config['googlesheets']

    def get_data(self, parser, resource_id):
        self.parser = parser
        token_credentials = TokenCredentials()
        creds = token_credentials.get_credentials(self.token, self.credentials, self.scopes)

        sheet_id = self.config_sheets['GoogleSheetsId']
        sheet_range = self.config_sheets['GoogleSheetsSheetName']

        service = build(self.service, self.version, credentials=creds)

        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=sheet_id,
                                    range=sheet_range).execute()

        self.data = self._convert_response_to_dict(result.get('values'))

    def parse_data(self):
        self.parser.open_google_sheets(self.data)
        self.parsed_data = self.parser.parse()

    def convert_data(self):
        return [ Resource(element['name'], element['value'], element['description']) for element in self.parsed_data ]

    def _convert_response_to_dict(self, values):
        response_list = []
        headers = values[0]
        for i in range(1, len(values)):
            mapping = dict(zip(headers, values[i]))
            if (mapping):
                response_list.append(mapping)
        return response_list