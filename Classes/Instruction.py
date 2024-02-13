#############################################
# File:		Instruction class				#
# Author: 	Adam Ližičiar (xlizic00)		#
# Date: 	13.2.2024						#
#############################################

from Classes.InstrArgument import InstrArgument
from Classes.Error import Error


#
#   Class for handling instruction
#
class Instruction:
	order = None
	opCode = None
	arg1 = None
	arg2 = None
	arg3 = None
	operands = [
		{"opCode": "MOVE", "params": ["var", "symb"]},
		{"opCode": "CREATEFRAME", "params": []},
		{"opCode": "PUSHFRAME", "params": []},
		{"opCode": "POPFRAME", "params": []},
		{"opCode": "DEFVAR", "params": ["var"]},
		{"opCode": "CALL", "params": ["label"]},
		{"opCode": "RETURN", "params": []},
		{"opCode": "PUSHS", "params": ["symb"]},
		{"opCode": "POPS", "params": ["var"]},
		{"opCode": "ADD", "params": ["var", "symb", "symb"]},
		{"opCode": "SUB", "params": ["var", "symb", "symb"]},
		{"opCode": "MUL", "params": ["var", "symb", "symb"]},
		{"opCode": "IDIV", "params": ["var", "symb", "symb"]},
		{"opCode": "LT", "params": ["var", "symb", "symb"]},
		{"opCode": "GT", "params": ["var", "symb", "symb"]},
		{"opCode": "EQ", "params": ["var", "symb", "symb"]},
		{"opCode": "AND", "params": ["var", "symb", "symb"]},
		{"opCode": "OR", "params": ["var", "symb", "symb"]},
		{"opCode": "NOT", "params": ["var", "symb", "symb"]},
		{"opCode": "INT2CHAR", "params": ["var", "symb"]},
		{"opCode": "STRI2INT", "params": ["var", "symb", "symb"]},
		{"opCode": "READ", "params": ["var", "type"]},
		{"opCode": "WRITE", "params": ["symb"]},
		{"opCode": "CONCAT", "params": ["var", "symb", "symb"]},
		{"opCode": "STRLEN", "params": ["var", "symb"]},
		{"opCode": "GETCHAR", "params": ["var", "symb", "symb"]},
		{"opCode": "SETCHAR", "params": ["var", "symb", "symb"]},
		{"opCode": "TYPE", "params": ["var", "symb"]},
		{"opCode": "LABEL", "params": ["label"]},
		{"opCode": "JUMP", "params": ["label"]},
		{"opCode": "JUMPIFEQ", "params": ["label", "symb", "symb"]},
		{"opCode": "JUMPIFNEQ", "params": ["label", "symb", "symb"]},
		{"opCode": "EXIT", "params": ["symb"]},
		{"opCode": "DPRINT", "params": ["symb"]},
		{"opCode": "BREAK", "params": []},
	]

	# Init function for parsing line
	def __init__(self, intrCnt, line):
		lineArray = self.lineToArray(line) # Convert line to array

		# Check if line exists, if not, do not set anything
		if(len(lineArray) == 0):
			raise InstrEmptyLineArray()
		else:
			self.order = intrCnt
			argumentsPattern = self.saveOpCode(lineArray[0])

			# Check if the number of arguments is correct
			if len(argumentsPattern) != len(lineArray) - 1:
				Error(23)
			else:
				self.processArguments(lineArray, argumentsPattern) # Process the arguments if there are any
		
	# Convert line to array
	def lineToArray(self, line):
		line = line.strip() # Delete \n
		line = self.deleteComment(line) # Remove comment
		lineArray = line.split() # Split parts
		return lineArray

	# Delete comment from line
	def deleteComment(self, line):
		index = line.find('#')
		if index != -1:
			line = line[:index]
		return line	
	
	# Process arguments
	def processArguments(self, lineArray, argumentsPattern):
		if len(lineArray) > 1:
			self.arg1 = InstrArgument(lineArray[1], argumentsPattern[0])
		if len(lineArray) > 2 :
			self.arg2 = InstrArgument(lineArray[2], argumentsPattern[1])
		if len(lineArray) > 3:
			self.arg3 = InstrArgument(lineArray[3], argumentsPattern[2])

	# Check if opcode is correct and save it
	def saveOpCode(self, instrOpCode):
		foundCommand = False	# Handler if OPCODE is correct

		# Iterate through operands
		for operand in self.operands:
			if operand["opCode"].upper() == instrOpCode:
				argumentsPattern = operand["params"]
				foundCommand = True
				break
	
		if foundCommand is True:
			self.opCode = instrOpCode
			return argumentsPattern	# Handler for pattern of argument
		else:
			Error(22)


#
#   Exception class for empty line
#
class InstrEmptyLineArray(Exception):
    pass
