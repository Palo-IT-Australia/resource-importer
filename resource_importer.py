import argparse

from data_generator.android_resource import AndroidResourceGenerator
from data_generator.swift_ios_resource import SwiftResourceGenerator
from source_connector.local_connector import LocalConnector
from source_connector.google_sheets_connector import GoogleSheetsConnector
from util.json_parser import JsonParser
from util.csv_parser import CsvParser
from util.configuration_parser import ConfigurationParser

class ResourceImporter():

	file_format = {
		"csv": CsvParser,
		"json": JsonParser
	}

	platform = {
		"android": AndroidResourceGenerator,
		"ios": SwiftResourceGenerator
	}

	source = {
		"local": LocalConnector,
		"google_sheets": GoogleSheetsConnector
	}

	def __init__(self, args, filepath):
		self.config = None
		self.args = args
		self.filepath = filepath

	def _read_config(self):
		configuration_parser = ConfigurationParser(self.filepath)
		self.config = configuration_parser.parse_config()
		
	def _get_resources(self, source, platform, fileformat):
		connector = source()
		platform = platform()
		parser = fileformat()

		connector.get_data(parser, "resources." + self.args.fileformat)
		connector.parse_data()
		data = connector.convert_data()

		platform.transform_data(data)
		platform.save_data(self.config[self.args.platform]['ResourceFileName'])

	def set_source_and_platform(self):
		self._read_config()
		self._get_resources(self.source[args.source], self.platform[args.platform], self.file_format[args.fileformat])


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("source", type=str, choices=["local", "google_sheets"], 
					help="set the data source")
	parser.add_argument("platform", type=str, choices=["android", "ios"],
					help="set the platform to generate files")
	parser.add_argument("-f", "--fileformat", type=str, choices=["csv", "json", "xml"],
                    default="json", help="set file format")
	args = parser.parse_args()
	resourceImporter = ResourceImporter(args, "configuration.ini")
	resourceImporter.set_source_and_platform()