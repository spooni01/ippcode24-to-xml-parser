#############################################
# File:		Instruction class				#
# Author: 	Adam Ližičiar (xlizic00)		#
# Date: 	13.2.2024						#
#############################################

from Classes.InstrArgument import InstrArgument


#
#   Class for handling instruction
#
class Instruction:
	order = None
	opCode = None
	arg1 = None
	arg2 = None
	arg3 = None

	# Init function for parsing line
	def __init__(self, line):
		lineArray = self.lineToArray(line) # Convert line to array

		# Check if line exists, if not, do not set anything
		if(len(lineArray) == 0):
			raise InstrEmptyLineArray()
		else:
			self.processArguments(lineArray) # Process the arguments if there are any
		
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
	def processArguments(self, lineArray):
		if len(lineArray) > 1:
			self.arg1 = InstrArgument(lineArray[1])
		if len(lineArray) > 2:
			self.arg2 = InstrArgument(lineArray[2])
		if len(lineArray) > 3:
			self.arg3 = InstrArgument(lineArray[3])


#
#   Exception class for empty line
#
class InstrEmptyLineArray(Exception):
    pass