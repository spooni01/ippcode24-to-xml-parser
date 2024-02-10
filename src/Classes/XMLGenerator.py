#############################################
# File:		XML generator class 			#
# Author: 	Adam Ližičiar (xlizic00)		#
# Date: 	10.2.2024						#
#############################################

import xml.dom.minidom

class XMLGenerator:
    
	# Init XML DOM, add <program> element
	def __init__(self):
		self.doc = xml.dom.minidom.Document()
		self.program = self.doc.createElement("program")
		self.program.setAttribute("language", "IPPcode24")
		self.doc.appendChild(self.program)

	# Add element to program
	def addElement(self, order, opcode, sub1 = None, sub2 = None, sub3 = None):
		
		# Add instruction element
		element = self.doc.createElement("instruction")
		element.setAttribute("order", str(order))
		element.setAttribute("opcode", opcode.upper())
		self.program.appendChild(element)

		# If there are subelements, add them also
		if sub1 is not None:
			self.addSubelement(element, 1, sub1)
		if sub2 is not None:
			self.addSubelement(element, 2, sub2)
		if sub3 is not None:
			self.addSubelement(element, 3, sub3)

	# Add subelement to element
	def addSubelement(self, rootElement, subElemOrder, data):
		subElement = self.doc.createElement("arg"+str(subElemOrder))
		subElement.setAttribute("type", data[0])

		subElementValue = self.doc.createTextNode(data[1])
		subElement.appendChild(subElementValue)
		rootElement.appendChild(subElement)

	# Convert document to string and print
	def print(self):
		xml_str = self.doc.toprettyxml(indent="	", encoding="UTF-8").decode("UTF-8")
		print(xml_str)
