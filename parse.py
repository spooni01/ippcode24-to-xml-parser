#############################################
# File:		Main file						#
# Author: 	Adam Ližičiar (xlizic00)		#
# Date: 	13.2.2024						#
#############################################

import sys
from functions import *
from Classes.Stats import *
from Classes.Arguments import *
from Classes.Instruction import *
from Classes.XMLGenerator import *


# Parse srguments
argv = Arguments(sys.argv[1:])
stats = Stats(argv.statsParametersHandler)
xmlGen = XMLGenerator()
intrCnt = 1	# Counter for instruction order
headerFlag = False # Handler if there was a header


# While cycle through STDIN line by line
for line in sys.stdin:

	# Check header
	if headerFlag is False:
		headerFlag = checkHeader(line, stats)
		continue

	# Check other lines
	try:
		instr = Instruction(intrCnt, line, stats)
		xmlGen.addInstr(instr)
		intrCnt += 1
		stats.incrementInstr()
	except InstrEmptyLineArray:
		continue 

if headerFlag == False: Error(21) # If there was not header, exit with error


# Summarize statistics
stats.summarize()

# Print parsed code on STDOU
xmlGen.print() 




