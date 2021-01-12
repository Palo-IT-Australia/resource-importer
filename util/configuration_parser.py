import configparser

class ConfigurationParser():

	def __init__(self, filepath):
		self.config = None
		self.filepath = filepath

	def parse_config(self):
		self.config = configparser.ConfigParser()
		self.config.read(self.filepath)
		return self.config