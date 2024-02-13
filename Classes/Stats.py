#############################################
# File:		Stats class				        #
# Author: 	Adam Ližičiar (xlizic00)		#
# Date: 	13.2.2024						#
#############################################

import re
from Classes.Error import *


class Stats():
    outputFormatHandler = None
    loc = 0 # Number of lines with instructions
    comments = 0 # Number of lines with comments 
    labels = [] # Number of defined labels
    jumps = 0 # Number of jumps
    fwjumps = 0 # Number of forward jumps
    backjumps = 0 # Number of back jumps
    badjumps = 0 # Number of wrong jumps
    frequent = {"MOVE": 0,"CREATEFRAME": 0,"PUSHFRAME": 0,"POPFRAME": 0,"DEFVAR": 0,"CALL": 0,"RETURN": 0,"PUSHS": 0,"POPS": 0,"ADD": 0,"SUB": 0,"MUL": 0,"IDIV": 0,"LT": 0,"GT": 0,"EQ": 0,"AND": 0,"OR": 0,"NOT": 0,"INT2CHAR": 0,"STRI2INT": 0,"READ": 0,"WRITE": 0,"CONCAT": 0,"STRLEN": 0,"GETCHAR": 0,"SETCHAR": 0,"TYPE": 0,"LABEL": 0,"JUMP": 0,"JUMPIFEQ": 0,"JUMPIFNEQ": 0,"EXIT": 0,"DPRINT": 0,"BREAK": 0}

    statsFilesOpenSoFar = [] # Stores files that was open so far
    handlerForLabelsNotDefinedYet = []

    # Save format of output
    def __init__(self, outputFormatHandler):
        self.outputFormatHandler = outputFormatHandler

    # Summarize statistics (make calculations, output to files,...)
    def summarize(self):
        for currentOutput in self.outputFormatHandler:
            # Check if file was open
            self.checkFileNameDuplicite(currentOutput["file"])
            self.summarizeLabelsNotDefinedYet()

            tmpFile = open(currentOutput["file"], "w")
            
            # Iterate through the array and replace the values
            outputData = currentOutput["params"]
            for i in range(len(outputData)):
                if outputData[i] == 'loc':
                    outputData[i] = str(self.loc) + "\n"
                elif outputData[i] == 'comments':
                    outputData[i] = str(self.comments) + "\n"
                elif outputData[i] == 'labels':
                    outputData[i] = str(len(self.labels)) + "\n"
                elif outputData[i] == 'jumps':
                    outputData[i] = str(self.jumps) + "\n"
                elif outputData[i] == 'fwjumps':
                    outputData[i] = str(self.fwjumps) + "\n"
                elif outputData[i] == 'backjumps':
                    outputData[i] = str(self.backjumps) + "\n"
                elif outputData[i] == 'badjumps':
                    outputData[i] = str(self.badjumps) + "\n"
                elif re.match(r"print=(.*)", outputData[i]):
                    outputData[i] = outputData[i].split("=", 1)[1] + "\n"
                elif outputData[i] == "eol":
                    outputData[i] = "\n"
                elif outputData[i] == "frequent":
                    outputData[i] = self.getFrequent()

            tmpFile.writelines(outputData) 
            tmpFile.close()

    # Check if files was open so far
    def checkFileNameDuplicite(self, filename):
        if filename in self.statsFilesOpenSoFar:
            Error(12)
        else:
            self.statsFilesOpenSoFar.append(filename)

    # Summarize which jumps was forward and which bad
    def summarizeLabelsNotDefinedYet(self):
        for label in self.handlerForLabelsNotDefinedYet:
            if label in self.labels:
                self.fwjumps += 1
            else:
                self.badjumps += 1

    # Return most frequent opcodes in code
    def getFrequent(self):
        tmp = ""
        
        filteredFrequent = {key: value for key, value in self.frequent.items() if value != 0} # Delete all 0 values
        sortedFrequent = dict(sorted(filteredFrequent.items(), key=lambda item: item[1], reverse=True)) # Sord from highest to lowest
        
        for item in sortedFrequent:
            tmp += str(item) + ","
                               
        return str(tmp)

    # Increment 'loc' by 1
    def incrementInstr(self):
        self.loc += 1

    # Increment 'comments' by 1
    def incrementComments(self):
        self.comments += 1

    # Add label to 'labels' if is not yet in it
    def addLabel(self, label):
        self.labels.append(label)

    # Add label to 'labels' if is not yet in it
    def incrementJumps(self):
        self.jumps += 1

    # Increment one in frequent
    def addFrequent(self, opcode):
        self.frequent[opcode.upper()] += 1