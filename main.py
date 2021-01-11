from data_generator.android_resource import AndroidResourceGenerator
from data_generator.swift_ios_resource import SwiftResourceGenerator
from source_connector.local_connector import LocalConnector
from source_connector.google_sheets_connector import GoogleSheetsConnector
from util.json_parser import JsonParser
from util.csv_parser import CsvParser

def get_resources():
	jsonParser = JsonParser()
	csvParser = CsvParser()
	localConnector = LocalConnector()
	localConnector.get_data(jsonParser, "resources.json")
	localConnector.parse_data()
	data = localConnector.convert_data()
	localConnector.get_data(csvParser, "copy_deck.csv")
	localConnector.parse_data()
	data = localConnector.convert_data()

	googleSheetsConnector = GoogleSheetsConnector(
		"sheets",
		"v4",
		"token.pickle"
		)
	googleSheetsConnector.get_data(
		"1vYaaxgGQSqpJI4KUGw7ql__ZqAgTjMPnSI3vusQSnjo",
		"Sheet1!A3:E"
		)
	googleSheetsConnector.parse_data()
	data_google = googleSheetsConnector.convert_data()

	androidResourceGenerator = AndroidResourceGenerator()
	androidResourceGenerator.transform_data(data)
	androidResourceGenerator.save_data("strings.xml")
	swiftResourceGenerator = SwiftResourceGenerator()
	swiftResourceGenerator.transform_data(data)
	swiftResourceGenerator.save_data("localization.strings")

if __name__ == '__main__':
	get_resources()