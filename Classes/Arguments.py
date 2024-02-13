#############################################
# File:		Arguments class 				#
# Author: 	Adam Ližičiar (xlizic00)		#
# Date: 	13.2.2024						#
#############################################

import sys
import re
from Classes.Error import Error


#
#	Class for handling arguments
#
class Arguments:
	statsParametersHandler = [] # for example: {"file":"name.x", "params":{"--comments", "--labels"}}

	def __init__(self, parameters):
		# Check if there is help	
		if '--help' in parameters or '-h' in parameters:
			if len(parameters) > 1:
				Error(10)
			else:
				self.printHelpMessage()
				sys.exit(0)

		# Parse parameters
		if len(parameters) > 0:
			self.parseParameters(parameters)

	# Parse parameter one by one
	def parseParameters(self, parameters):
		if re.match(r"--stats=(\w+)", parameters[0]):	# Check if first parameters is --stats
			tmpStatsSourceFile = None
			tmpStatsLineParams = []
			firstIteration = True

			# Loop through all parameters
			for param in parameters:
				match = re.match(r"--stats=(\w+)", param)

				# If parameter is --stats
				if(match is not None):	
					# Append to statsParametersHandler if is done iteration for current stats file
					if firstIteration != True:
						self.statsParametersHandler.append({"file":tmpStatsSourceFile, "params":tmpStatsLineParams})
						tmpStatsSourceFile = None
						tmpStatsLineParams = []
					else:
						firstIteration = False

					tmpStatsSourceFile = param.split("=", 1)[1]

				# If parameter is not --stats
				else:
					# Delete '--' from the beginning, check if param exist, if yes append it to temporaly variable tmpStatsLineParams
					param = param[2:]
					if (param not in {"stats","loc","comments","labels","jumps","fwjumps","backjumps","badjumps","frequent","eol"}) and (not re.match(r"print=(.*)", param)):
						Error(10)
					else:
						tmpStatsLineParams.append(param)

			# For the last iteration, it is neccesary to save last file
			self.statsParametersHandler.append({"file":tmpStatsSourceFile, "params":tmpStatsLineParams})

		else:
			Error(10)

	# Print help message on STDOUT 
	def printHelpMessage(self):
		print("\n")
		print("IPPcode24 to XML parser")
		print("\n")
		print("About:\n")
		print("The program takes IPPcode24 code from STDIN and returns it formatted in XML to STDOUT. It is possible to use several files for the statistics statement, first of all it is necessary to enter the name of the file (--source=file) to which you want to write and then all the parameters for the statement. For other files, it is necessary to use --source again and then give again the parameters that have to be output into file.")
		print("\nParameters:")
		print("\t[-h/--help] for help message")
		print("\t[--stats=file] for specifying the file to write statistics to")
		print("\t[--loc] to count lines with instructions")
		print("\t[--comments] to count lines with comments")
		print("\t[--labels] to count defined labels")
		print("\t[--jumps] to count jump instructions and function returns")
		print("\t[--fwjumps] to count forward jumps")
		print("\t[--backjumps] to count backward jumps")
		print("\t[--badjumps] to count bad jumps")
		print("\t[--frequent] to output most frequent operation codes")
		print("\t[--print=string] to output the specified string")
		print("\t[--eol] to output end of line character")
		print("\n")
