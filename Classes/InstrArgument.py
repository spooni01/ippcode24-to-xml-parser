#############################################
# File:		Operand class       			#
# Author: 	Adam Ližičiar (xlizic00)		#
# Date: 	13.2.2024						#
#############################################

import re
from Classes.Error import Error


#
#   Class for handling intruction argument
#
class InstrArgument:
	type = None
	value = None
	argPattern = None
	
	# Init function for parsing operand
	def __init__(self, unprocessedOperand, argPattern):
		self.argPattern = argPattern
		if(argPattern == "var"): self.processVar(unprocessedOperand)
		elif(argPattern == "symb"): self.processSymb(unprocessedOperand)
		elif(argPattern == "label"): self.processLabel(unprocessedOperand)
		elif(argPattern == "type"): self.processType(unprocessedOperand)
		else: Error(23)

	# Separate string by '@' and save it
	def separateAndSave(self, unprocessedOperand):
		parts = unprocessedOperand.split('@')

		# Check if the second part matches the pattern
		if len(parts) == 2 and re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', parts[1]):
			self.type = parts[0]
			self.value = parts[1]
		else:
			Error(23)

	# Get second value, predefined is empty string
	def getSecondValue(self, unprocessedOperand, typeOfConstant):
		secondValue = ""

		parts = unprocessedOperand.split('@', 1)
		if len(parts) > 1: 
			secondValue = parts[1]

		# Check correct format
		if typeOfConstant == "bool" and (secondValue != "true" and secondValue != "false"): Error(23)

		return secondValue

	# Process 'var'
	def processVar(self, unprocessedOperand):
		if(not re.match(r'^(LF|GF|TF)@[a-zA-Z_][a-zA-Z0-9_]*$', unprocessedOperand)):
			Error(23)
		else:
			self.type = "var"
			self.value = unprocessedOperand

	# Process 'symb'
	def processSymb(self, unprocessedOperand):
		if(re.match(r'^(LF|GF|TF)@[a-zA-Z_][a-zA-Z0-9_]*$', unprocessedOperand)):
			self.type = "var"
			self.value = unprocessedOperand
		elif(re.match(r'^bool@(true|false)', unprocessedOperand)):
			self.type = "bool"
			self.value = self.getSecondValue(unprocessedOperand, "bool")
		elif(re.match(r'^string@.*$', unprocessedOperand)):
			self.type = "string"
			self.value = self.getSecondValue(unprocessedOperand, "string")
		elif(re.match(r'^nil@nil', unprocessedOperand)):
			self.type = "nil"
			self.value = "nil"
		elif(re.match(r'^int@(-?0x[0-9a-fA-F]+|-?0o[0-7]+|-?\d+)$', unprocessedOperand)):
			self.type = "int"
			self.value = self.getSecondValue(unprocessedOperand, "int")
		else:
			Error(23)

	# Process 'label'
	def processLabel(self, unprocessedOperand):
		if(not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', unprocessedOperand)):
			Error(23)	
		else:
			self.type = "label"
			self.value = unprocessedOperand

	# Process 'type'
	def processType(self, unprocessedOperand):
		if unprocessedOperand not in {"int", "bool", "string", "nil", "label", "type", "var"}:
			Error(23)	
		else:
			self.type = "type"
			self.value = unprocessedOperand