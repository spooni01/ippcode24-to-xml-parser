#############################################
# File:		Error file						#
# Author: 	Adam Ližičiar (xlizic00)		#
# Date: 	9.2.2024						#
#############################################

import sys


class Error:

	def __init__(self):

		# All possible errors
		self.errors = {
			10: "missing script parameter or using prohibited combination of parameters",
			11: "problem with opening input file",
			12: "problem when opening output file",
			21: "wrong or missing header in the source code",
			22: "unknown or incorrect operation code in the source code",
			23: "other lexical or syntactic error of the source code",
			99: "internal error"
		}

	# Exit program with error message
	def exit_program_with_err_msg(self, errNum):
		print("Error: " + self.errors[errNum] + "!", file=sys.stderr)
		sys.exit(errNum)

