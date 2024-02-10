#############################################
# File:		Arguments parser class 			#
# Author: 	Adam Ližičiar (xlizic00)		#
# Date: 	10.2.2024						#
#############################################

class Parser:
	order = 1
	headerFlag = False

	def __init__(self, err):
		self.err = err

	# Parse line and send it to XML Generator
	def parseLine(self, line, xmlGenerator):
		line = line.strip() # Remove \n  
		line = self.deleteComment(line) 
	
		# If line is empty, skip it
		if line == "":
			return
		
		# Separate line
		lineParts = line.split()

		# Header checker
		if self.headerFlag is False:
			self.checkHeader(lineParts)
			return
			

		# todo:remove comment (not in string?)
		# todo:split
		# type can be: int, bool, string, nil, label, type, var (podle toho, zda se jedná o literál, návěští, typ nebo proměnnou, a obsahuje textový element)



		if len(lineParts) > 1:
			arg1 = ["type", lineParts[1]]
		else:
			arg1 = None
		if len(lineParts) > 2:
			arg2 = ["type", lineParts[2]]
		else:
			arg2 = None
		if len(lineParts) > 3:
			arg3 = ["type", lineParts[3]]
		else:
			arg3 = None

		xmlGenerator.addElement(self.order, lineParts[0], arg1, arg2, arg3)
		self.order += 1

	# Delete comment from string
	def deleteComment(self, line):
		index = line.find('#')
		if index != -1:
			line = line[:index]
		return line			
	
	# Check if header is in correct format
	def checkHeader(self, lineParts):
		if (lineParts[0] != ".IPPcode24") or (len(lineParts) > 1):
			self.err.exit_program_with_err_msg(21)
		else:
			self.headerFlag = True
