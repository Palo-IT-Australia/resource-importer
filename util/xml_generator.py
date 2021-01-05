import xml.etree.ElementTree as ET
from xml.dom import minidom

class XmlGenerator:

	def __init__(self, data):
		self.data = data
		self.tree = None

	def generate_xml(self):
		root = ET.Element("resources")
		for element in self.data:
			ET.SubElement(root, "string", name=element.name).text = element.value
		self.tree = ET.ElementTree(root)

	def write_xml(self, filename):
		ET.indent(self.tree) # introduced in Python 3.9
		self.tree.write(filename, xml_declaration=True, encoding='utf-8')