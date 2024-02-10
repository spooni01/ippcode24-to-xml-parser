#############################################
# File:		Arguments parser class 			#
# Author: 	Adam Ližičiar (xlizic00)		#
# Date: 	10.2.2024						#
#############################################

import argparse

class Arguments:

	def __init__(self, parameters):
		self.parameters = parameters
		self.parse_arguments()

	# Parse arguments from input STDIN
	def parse_arguments(self):
		parser = argparse.ArgumentParser(description="IPPcode24 to XML parser")
		parser.add_argument("--source", type=str, help="path to the source file")
		args = parser.parse_args()

		if not args.source:
			parser.error("Source file is missing")


