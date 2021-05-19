#!/usr/bin/env python3
def sub(a, b):
    return a -b

'''
modify function insider another function
'''
def smart_sub(func):

    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a,b)
    return inner

print(sub(1,99))
sub = smart_sub(sub)
print(sub(1,99))

