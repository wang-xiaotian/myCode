#!/usr/bin/env python3
import shutil
import os

HOME = "/home/student/myCode/lab16_renameFiles/"
TARGET_FILE1 = "raynor.obj"
TARGET_FILE2 = "kerrigan.obj"
TARGET_FOLDER ="ceph_storage/"

os.chdir(HOME)
xname = input("what is the new name for kerrigan.obj?\n>")

shutil.move(TARGET_FILE1, TARGET_FOLDER)
#rename current kerrigan.obj
shutil.move(TARGET_FOLDER + TARGET_FILE2, TARGET_FOLDER + xname)
