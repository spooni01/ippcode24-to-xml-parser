#############################################
# File:		Main file						#
# Author: 	Adam Ližičiar (xlizic00)		#
# Date: 	9.2.2024						#
#############################################

import sys
import argparse
import xml.dom.minidom
from Classes.Error import Error
from Classes.Arguments import Arguments
from Classes.XMLGenerator import XMLGenerator

# Init classes
err = Error()
args = Arguments(sys.argv[1:])
xmlGenerator = XMLGenerator()

#############################################

# todo: Parse arguments
# todo: Lopp throug input
# todo: Generate xml

xmlGenerator.addElement("int",1)
xmlGenerator.addElement()
xmlGenerator.addElement(1)
xmlGenerator.addElement(1,1,1)
xmlGenerator.flush()