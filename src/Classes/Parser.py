#############################################
# File:		Arguments parser class 			#
# Author: 	Adam Ližičiar (xlizic00)		#
# Date: 	10.2.2024						#
#############################################

import re


class Parser:
	order = 1
	headerFlag = False
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

	# Initialization function for class
	def __init__(self, err):
		self.err = err

	# Parse line and send it to XML Generator
	def parseLine(self, line, xmlGenerator):
		line = line.strip() # Remove \n  
		line = self.deleteComment(line) 
	
		# If line is empty, skip it
		if line == "":
			return
		
		# Separate line
		lineParts = line.split()

		# Header checker
		if self.headerFlag is False:
			self.checkHeader(lineParts)
			return
			
		# Main parsing system
		paramsPattern = self.checkOpCodeAndGetParams(lineParts)	
		if(len(paramsPattern) != len(lineParts)-1):
			self.err.exit_program_with_err_msg(23)
		else:
			for i in range(0, len(paramsPattern)):
				if(paramsPattern[i] == "var"):
					if(i + 1 < len(lineParts) and not re.match(r'^(LF|GF|TF)@.+', lineParts[i+1])):
						self.err.exit_program_with_err_msg(23)	
				elif(paramsPattern[i] == "symb"):
					if(i + 1 < len(lineParts) and not re.match(r'^(LF|GF|TF)@.+', lineParts[i+1]) and not re.match(r'^(int|bool|string|nil|label|type|var)@.+', lineParts[i+1])):
						self.err.exit_program_with_err_msg(23)	
				elif(paramsPattern[i] == "label"):
					if(i + 1 < len(lineParts) and not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', lineParts[i+1])):
						self.err.exit_program_with_err_msg(23)	
				elif(paramsPattern[i] == "type"):
					if lineParts[i+1] not in {"int", "bool", "string", "nil", "label", "type", "var"}:
						self.err.exit_program_with_err_msg(23)	
				else:
					self.err.exit_program_with_err_msg(23)

		arguments = self.convertSymbToCorrectType(lineParts, paramsPattern)
		xmlGenerator.addElement(self.order, lineParts[0], arguments[0], arguments[1], arguments[2])
		self.order += 1

	# Delete comment from string
	def deleteComment(self, line):
		index = line.find('#')
		if index != -1:
			line = line[:index]
		return line			
	
	# Check if header is in correct format
	def checkHeader(self, lineParts):
		if (lineParts[0] != ".IPPcode24") or (len(lineParts) > 1):
			self.err.exit_program_with_err_msg(21)
		else:
			self.headerFlag = True

	# Check opCode and get params
	def checkOpCodeAndGetParams(self, lineParts):
		foundCommand = False

		# Iterate through operands
		for operand in self.operands:
			if operand["opCode"].upper() == lineParts[0]:
				paramsPattern = operand["params"]
				foundCommand = True
				break
	
		if foundCommand is not True:
			self.err.exit_program_with_err_msg(22)
		else:
			return paramsPattern
		
	# Change symb to correct format
	def changeSymb(self, linePart):
		if(re.match(r'^(LF|GF|TF)@.+', linePart)):
			return "var", linePart
		else:
			parts = linePart.split("@")
			return parts[0], parts[1]
		
	# Convert symb to correct type
	def convertSymbToCorrectType(self, lineParts, paramsPattern):
		arguments = [None, None, None]

		for i in range(1,3):
			if len(lineParts) > i:
				if(paramsPattern[i-1] == "symb"):
					pattern, part = self.changeSymb(lineParts[i])
					arguments[i-1] = [pattern, part]
				else:
					arguments[i-1] = [paramsPattern[i-1], lineParts[i]]
			else:
				arguments[i-1] = None

		return arguments
					