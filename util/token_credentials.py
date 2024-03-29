import os.path
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class TokenCredentials():

	def get_credentials(self, token, credentials, scopes):
		return self._check_existing_token(token, credentials, scopes)

	def _check_existing_token(self, token_file, credentials_file, scopes):
		creds = None
		# filepath = 'token.pickle'
		if os.path.exists(token_file):
			with open(token_file, 'rb') as token:
				creds = pickle.load(token)
		if not creds or not creds.valid:
			if creds and creds.expired and creds.refresh_token:
				creds.refresh(Request())
			else:
				flow = InstalledAppFlow.from_client_secrets_file(
					credentials_file, [scopes])
				creds = flow.run_local_server(port=0)
			with open(token_file, 'wb') as token:
				pickle.dump(creds, token)
		return creds