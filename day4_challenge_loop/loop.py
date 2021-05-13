#!/usr/bin/env python3

# print number of dots
def printDots(num):
    for i in range(0, num):
        print('*', end='')

# print dots like stairs
def printStairs(num):
    # increase 
    for i in range(1, num):
        printDots(i)
        print()
    # decrease
    for i in range(num, 0, -1):
        printDots(i)
        print()

# wrap up solution 1
def dotsPrinting1(num):
    print(f"Solution # 1 - Printing dots: {num}")
    printStairs(num)

# decrease number of dots for solution 2
def printDotsDecrese(num):
    if num == 0:
        return
    else:
        printDots(num)
        print()
        printDotsDecrese(num-1)

# increase number of dots for solution 2
def printDotsIncrease(num):
    if num == 0:
        return
    else:
        printDotsIncrease(num-1)
        printDots(num)
        print()

# wrap up solution 2
def dotsPrinting2(num):
    printDotsIncrease(num)
    printDotsDecrese(num-1)

# output
dotsPrinting1(5)
dotsPrinting2(5)