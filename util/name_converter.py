class NameConverter():

	def __init__(self, platform):
		self.platform = platform
		self.string_template = {
			"Android": f"%s",
			"iOS": f"%@"
		}

	def _separate_string_to_array(self, name):
		return name.split(".")

	def convert_snake_case_to_camelCase(self, string_value):
		pass

	def convert_camelCase_to_snake_case(self, string_value):
		pass

	def convert_dots_to_snake_case(self, string_value):
		return "_".join(self._separate_string_to_array(string_value))

	def convert_dots_to_camelCase(self, string_value):
		pass

	def replace_string_templates(self, string_value):
		return string_value.replace("$String", self.string_template[self.platform])