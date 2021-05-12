#!/usr/bin/env python3

import random
STRING = "Memology is a young man's game"


def convertString(input):
    newstring= ""
    for char in input:
        case= random.randint(0,1)
        if case == 0:
            newstring += char.upper()
        else:
            newstring += char.lower()
    return newstring

print(convertString(STRING))