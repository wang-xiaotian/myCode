#!/usr/bin/env python3
import shutil 
import os # os dependent functionality

HOME = "c:/Python/myCode"
TARGET_FILE = "copy.txt"
COPIED_FILE = "copy2.txt"
TARGET_FOLDER = "/lab6/"
COPIED_FOLDER = "/lab6_copy"

os.chdir(HOME)
shutil.copy(TARGET_FILE, COPIED_FILE)
shutil.copytree(HOME + TARGET_FOLDER, HOME + COPIED_FOLDER)



