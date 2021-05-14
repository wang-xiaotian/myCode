#!/usr/bin/env python3

# print out numbers from min to max
def fizzBuzz(min, max):
    for i in range(min, max+1):
        if i % 3 == 0 and i != 0:
             print('fizz ', end='')
        elif i % 5 == 0 and i != 0:
            print('buzz ', end='')
        else:
            print(f'{i} ', end='')
    print("\nDone")

def main():
    fizzBuzz(0,100)

if __name__ == "__main__":
    main()