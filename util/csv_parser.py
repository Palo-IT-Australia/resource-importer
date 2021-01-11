import csv

class CsvParser():

	def __init__(self):
		self.filepath = None
		self.data = []

	def open_file(self, filepath):
		with open(filepath) as f:
			data = csv.DictReader(f)
			for row in data:
				self.data.append(self._rename_dict_keys(row))

	# temp function
	# can store temporary keys in config file
	def _rename_dict_keys(self, dict_row):
		dict_row['name'] = dict_row.pop('Key (Mandatory)')
		dict_row['value'] = dict_row.pop('Value - $String as placeholder')
		return dict_row

	def parse(self):
		parsed_data = []
		for row in self.data:
			print(row)
			parsed_data.append(row)
		return parsed_data
