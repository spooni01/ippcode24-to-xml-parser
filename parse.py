#############################################
# File:		Main file						#
# Author: 	Adam Ližičiar (xlizic00)		#
# Date: 	13.2.2024						#
#############################################

import sys
from Classes.Arguments import *
from Classes.Instruction import *


# Parse srguments
argv = Arguments(sys.argv[1:])


# While cycle through STDIN line by line
for line in sys.stdin:
	try:
		instr = Instruction(line)
	except InstrEmptyLineArray:
		continue 

	