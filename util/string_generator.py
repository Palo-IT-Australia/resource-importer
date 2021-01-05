class StringGenerator():

	def __init__(self, data):
		self.data = data
		self.dict_array = []

	def generate_strings_file(self):
		for element in self.data:
			self.dict_array.append(f"\"{element.name.upper()}\" = \"{element.value.upper()}\"")

	def write_strings_file(self, filename):
		with open(filename, "w") as f:
			f.write(";\n".join(self.dict_array))