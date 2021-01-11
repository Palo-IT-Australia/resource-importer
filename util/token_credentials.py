import os.path
import pickle
from google.auth.transport.requests import Request

class TokenCredentials():

	SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

	def __init__(self):
		self.token = None
		self.creds = None

	def get_credentials(self, filepath):
		_check_existing_token(filepath)
		return self.creds

	def _check_existing_token(self, filepath):
		creds = None
		# filepath = 'token.pickle'
		if os.path.exists(filepath):
			with open(filepath, 'rb') as token:
				creds = pickle.load(token)
		if not creds or not creds.valid:
			if creds and creds.expired and creds.refresh_token:
				creds.refresh(Request())
			else:
				flow = InstalledAppFlow.from_client_secrets_file(
					'credentials.json', SCOPES)
				creds = flow.run_local_server(port=0)
			with open(filepath, 'wb') as token:
				pickle.dump(creds, token)
		self.creds = creds