#############################################
# File:		Main file						#
# Author: 	Adam Ližičiar (xlizic00)		#
# Date: 	13.2.2024						#
#############################################

import sys
from Classes.Arguments import *
from Classes.Instruction import *
from Classes.XMLGenerator import *


# Parse srguments
argv = Arguments(sys.argv[1:])
xmlGen = XMLGenerator()
intrCnt = 1

# While cycle through STDIN line by line
for line in sys.stdin:
	try:
		instr = Instruction(intrCnt ,line)
		xmlGen.addInstr(instr)
		intrCnt += 1
	except InstrEmptyLineArray:
		continue 

# Print parsed code on STDOUT
xmlGen.print()