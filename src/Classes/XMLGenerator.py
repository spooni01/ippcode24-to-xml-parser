#############################################
# File:		XML generator class 			#
# Author: 	Adam Ližičiar (xlizic00)		#
# Date: 	10.2.2024						#
#############################################

import xml.dom.minidom

class XMLGenerator:

	order = 1
    
	def __init__(self):
		self.doc = xml.dom.minidom.Document()

		self.program = self.doc.createElement("program")
		self.doc.appendChild(self.program)

	# Add element to program
	def addElement(self, sub1 = None, sub2 = None, sub3 = None):
		element = self.doc.createElement("instruction")
		element.setAttribute("order", str(self.order))
		self.order += 1
		self.program.appendChild(element)

		if sub1 is not None:
			self.addSubelement(element, 1)
		if sub2 is not None:
			self.addSubelement(element, 2)
		if sub3 is not None:
			self.addSubelement(element, 3)

	# Add subelement to element
	def addSubelement(self, rootElement, subElemOrder):
		subElement = self.doc.createElement("arg"+str(subElemOrder))
		subElementText = self.doc.createTextNode("xxx")
		subElement.appendChild(subElementText)
		rootElement.appendChild(subElement)

	# Convert document to string and print
	def flush(self):
		xml_str = self.doc.toprettyxml(indent="	", encoding="UTF-8").decode("UTF-8")
		print(xml_str)