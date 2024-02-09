#############################################
# File:		Makefile						#
# Author: 	Adam Ližičiar (xlizic00)		#
# Date: 	9.2.2024						#
#############################################

PYTHON = python3.10
SRC_DIR = src
MAIN_FILE = parse.py

.PHONY: run

# Run program without parameters
run:
	$(PYTHON) $(SRC_DIR)/$(MAIN_FILE) 


