#############################################
# File:		Arguments parser class 			#
# Author: 	Adam Ližičiar (xlizic00)		#
# Date: 	10.2.2024						#
#############################################

import sys
import argparse

class Arguments:

	def __init__(self, parameters, err):
		self.err = err
		self.parameters = parameters
		self.parse_arguments()

	# Parse arguments from input STDIN
	def parse_arguments(self):
		self.check_help_and_other_parameters()

		parser = argparse.ArgumentParser(description="IPPcode24 to XML parser")
		parser.add_argument("--source", type=str, help="path to the source file")
		args = parser.parse_args()

		if not args.source:
			parser.error("Source file is missing")
		else:
			self.source = args.source

	# Check if --help is provided along with other parameters
	def check_help_and_other_parameters(self):
		if '--help' in sys.argv[1:] and len(sys.argv) > 2:
			self.err.exit_program_with_err_msg(10)