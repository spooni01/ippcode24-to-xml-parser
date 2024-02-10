#############################################
# File:		Main file						#
# Author: 	Adam Ližičiar (xlizic00)		#
# Date: 	9.2.2024						#
#############################################

import sys
from Classes.Error import Error
from Classes.Arguments import Arguments
from Classes.Parser import Parser
from Classes.XMLGenerator import XMLGenerator

# Init classes
err = Error()
argv = Arguments(sys.argv[1:], err)
parser = Parser(err)
xmlGenerator = XMLGenerator()

# Open the source file
try:
    with open(argv.source, "r") as sourceFile:
        line = sourceFile.readline()

        while line:
            parser.parseLine(line, xmlGenerator)
            line = sourceFile.readline()
            
except FileNotFoundError:
    err.exit_program_with_err_msg(11)

# Print xml
xmlGenerator.print()