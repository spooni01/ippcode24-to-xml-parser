#############################################
# File:		Operand class       			#
# Author: 	Adam Ližičiar (xlizic00)		#
# Date: 	13.2.2024						#
#############################################


#
#   Class for handling intruction argument
#
class InstrArgument:
	type = None
	value = None
	
	# Init function for parsing operand
	def __init__(self, unprocessedOperand):
		self.type = unprocessedOperand
		self.value = unprocessedOperand

	
		

