#############################################
# File:		Arguments class 				#
# Author: 	Adam Ližičiar (xlizic00)		#
# Date: 	13.2.2024						#
#############################################

import sys
import argparse
from Classes.Error import Error


#
#	Class for handling arguments
#
class Arguments:

	def __init__(self, parameters):
		self.parameters = parameters
		self.parse_arguments()

	# Parse arguments from input STDIN
	def parse_arguments(self):
		self.check_help_and_other_parameters()

		parser = argparse.ArgumentParser(description="IPPcode24 to XML parser: The program takes IPPcode24 code from STDIN and returns it formatted in XML to STDOUT.")
		args = parser.parse_args()

	# Check if --help is provided along with other parameters
	def check_help_and_other_parameters(self):
		if '--help' in sys.argv[1:] and len(sys.argv) > 2:
			err = Error(10)