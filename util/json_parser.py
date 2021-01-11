import json

class JsonParser():

	def __init__(self):
		self.filepath = None
		self.data = None

	def open_file(self, filepath):
		with open(filepath) as f:
			self.data = f.read()

	def parse(self):
		return json.loads(self.data)