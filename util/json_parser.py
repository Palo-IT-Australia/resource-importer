import json

class JsonParser():

	def __init__(self, data):
		self.data = data

	def parse(self):
		return json.loads(self.data)