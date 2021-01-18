import xml.etree.ElementTree as ET
from xml.dom import minidom

class XmlGenerator:

	def __init__(self, data):
		self.data = data
		self.tree = None
		self.xmlstr = None

	def generate_xml(self):
		comment = None
		root = ET.Element("resources")
		for element in self.data:
			if (element.description):
				root.append(ET.Comment(element.description.strip("// ")))
			if (element.name and element.value):
				ET.SubElement(root, "string", name=element.name).text = element.value
		self.tree = ET.ElementTree(root)
		# workaround until AWS Lambda starts to natively support Python 3.9
		self.xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ", encoding='UTF-8')

	def write_xml(self, filename):
		with open(filename, "w") as f:
			f.write(str(self.xmlstr.decode('UTF-8')))
		# ET.indent(self.tree) # introduced in Python 3.9
		# self.tree.write(filename, xml_declaration=True, encoding='utf-8')