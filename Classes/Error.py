#############################################
# File:		Error file						#
# Author: 	Adam Ližičiar (xlizic00)		#
# Date: 	9.2.2024						#
#############################################

import sys


#
#	Class for handling errors
#
class Error:
	
	# Dictionary mapping error numbers to error messages
	errors = {
		10: "missing script parameter or using prohibited combination of parameters",
		11: "problem with opening input file",
		12: "problem when opening output file",
		21: "wrong or missing header in the source code",
		22: "unknown or incorrect operation code in the source code",
		23: "other lexical or syntactic error of the source code",
		99: "internal error"
	}
	
	# Print error message to standard error output and program with error code
	def __init__(self, errCode):
		print("Error: " + self.errors[errCode] + "!", file=sys.stderr)
		sys.exit(errCode)

