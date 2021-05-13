#!/usr/bin/env python3

import os
import fnmatch

EXCLUDE = ["/usr", "/home", "/var", "C:/Python/myCode"]

def find(pattern, path):
    result = []
    for root, dirs, file in os.walk(path):
            for name in file:
                if fnmatch.fnmatch(name, pattern):
                    result.append(os.path.join(root, name))
    return result

lookfor = input("pattern, like *.txt: \n>")
lookwhere = input("where: \n>")

print(find(lookfor, lookwhere))


def find_givenPath(pattern, path):
    """search through filesystem based on given path location"""
    result = []
    for root, dirs, files in os.walk(path, topdown=True):
        print(root)
        if root in EXCLUDE:
            dirs[:] = [] # remove directory list for this iteration
            files[:] = [] # remove the file list for this iteration
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

lookfor = input("pattern, like *.txt: \n>")
lookwhere = input("where: \n>")
print(find_givenPath(lookfor, lookwhere))