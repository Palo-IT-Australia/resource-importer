import xml.etree.ElementTree as ET
from xml.dom import minidom

class XmlGenerator:

	def __init__(self, data):
		self.data = data
		self.tree = None

	def generate_xml(self):
		comment = None
		root = ET.Element("resources")
		for element in self.data:
			if (element.description):
				root.append(ET.Comment(element.description.strip("// ")))
			if (element.name and element.value):
				ET.SubElement(root, "string", name=element.name).text = element.value
		self.tree = ET.ElementTree(root)

	def write_xml(self, filename):
		ET.indent(self.tree) # introduced in Python 3.9
		self.tree.write(filename, xml_declaration=True, encoding='utf-8')