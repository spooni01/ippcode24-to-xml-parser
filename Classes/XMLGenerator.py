#############################################
# File:		XML generator class 			#
# Author: 	Adam Ližičiar (xlizic00)		#
# Date: 	13.2.2024						#
#############################################

import xml.dom.minidom


#
#   Class for XMLGenerator
#
class XMLGenerator:
    
	# Init function
	def __init__(self):
		# Init XML document
		self.doc = xml.dom.minidom.Document()

		# Add <program> element
		self.program = self.doc.createElement("program")
		self.program.setAttribute("language", "IPPcode24") # Add attributes <program> element
		self.doc.appendChild(self.program)

	# Add instruction and its arguments to XML
	def addInstr(self, instrPtr):
		element = self.doc.createElement("instruction")
		element.setAttribute("order", str(instrPtr.order))
		element.setAttribute("opcode", instrPtr.opCode.upper())
		self.program.appendChild(element)

		# If there are subelements, add them also
		if instrPtr.arg1 is not None:
			self.addSubelement(element, 1, instrPtr.arg1)
		if instrPtr.arg2 is not None:
			self.addSubelement(element, 2, instrPtr.arg2)
		if instrPtr.arg3 is not None:
			self.addSubelement(element, 3, instrPtr.arg3)

	# Add subelement to element
	def addSubelement(self, rootElement, subElemOrder, argPtr):
		subElement = self.doc.createElement("arg"+str(subElemOrder))
		subElement.setAttribute("type", str(argPtr.type))

		subElementValue = self.doc.createTextNode(argPtr.value)
		subElement.appendChild(subElementValue)
		rootElement.appendChild(subElement)

	# Convert document to string and print
	def print(self):
		xml_str = self.doc.toprettyxml(indent="	", encoding="UTF-8").decode("UTF-8")
		print(xml_str)