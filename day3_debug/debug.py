#!/usr/bin/env python3
# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.


def add(num1,num2):
    print("\n" + str(num1) + " + " + str(num2) + " = " + str(num1 + num2))
    return num1 + num2
    
def sub(num1,num2):
    print("\n" + str(num1) + " - " + str(num2) + " = " + str(num1 - num2))
    return num1 - num2

def main():
    calc1 = 0.0
    calc2 = 0.0
    operation = ""
    calc1_input = ""
    calc2_input = ""
    while calc1_input != "q":

        print("\nWhat is the first operator? Or, enter q to quit: ")
        calc1_input = input().lower().strip()
        if continueRun(calc1_input) == -2:
            print("\n Not a valid entry. Restarting...")
            continue
        elif continueRun(calc1_input) == -1:
            break
        calc1 = float(calc1_input)

        print("\nWhat is the second operator? Or, enter q to quit: ")
        calc2_input = input().lower().strip()
        if continueRun(calc2_input) == -2:
            print("\n Not a valid entry. Restarting...")
            continue
        elif continueRun(calc2_input) == -1:
            break
        calc2 = float(calc2_input)

        print("Enter an operation to perform on the two operators (+ or -): ")
        operation = input()
        result = 0.0
        if operation == "+":
            result = add(calc1,calc2)
        elif operation == '-':
            result = sub(calc1, calc2)
        else:
            print("\n Not a valid entry. Restarting...")

        print(f'Result is {result}')

def continueRun(input):
    if input == "q":
        return -1
    else:
       if input.isdigit() != True:
           return -2
    return True

main()

