#############################################
# File:		Help functions					#
# Author: 	Adam Ližičiar (xlizic00)		#
# Date: 	13.2.2024						#
#############################################

from Classes.Error import Error


# Function check if there is header
def checkHeader(line):
	# Delete comments
	index = line.find('#')
	if index != -1:
		line = line[:index]

	# Split and check if header is correct
	lineArray = line.split()
	if len(lineArray) > 0 and len(lineArray) == 1 and lineArray[0] == ".IPPcode24":
		return True
	elif len(lineArray) > 0 and len(lineArray) == 1 and lineArray[0] != ".IPPcode24":
		err = Error(21)
	else:
		return False