#!/usr/bin/env python3
FILE_DIR = "./lab28_readFromFiles/vlanconfig.cfg"

with open(FILE_DIR, 'r') as configFile:
    lines = configFile.readlines()
    print(lines)
    configFile.close()

with open(FILE_DIR, 'r') as configFile:
    for l in configFile:
        print(l, end = "")
    configFile.close()