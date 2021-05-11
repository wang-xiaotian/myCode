#!/usr/bin/env python3

# Lab 17
##create the string hostname
from typing import SupportsRound


hostname = "MTG"

if hostname == "MTG":
    print("The hostname was ound to be mtg")

hostname = input("What value should we set for hostname?\n>")
if hostname == "MTG":
    print("The hostname was found to be mtg")
else:
    print(f"The hostname was not mtg, but {hostname}")

hostname = input("What value should we set for hostname?\n>")
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
else:
    print(f"The hostname (lowercase) was not mtg, but {hostname}")

# Lab 18 - ipv4 testing
ipchk = "192.168.0.1"

if ipchk:
    print(f"Looks like the IP address was set:{ipchk}")
else:
    print("Ip address is empty")

ipchk = input("Apply and IP address: \n>")
if ipchk == "192.168.70.1":
    print(f"Looks like the IP addressof the Gateway was set:{ipchk}. This is not recommanded.")
elif ipchk:
    print(f"Looks like the ip was set {ipchk}")
else:
    print("You did not provide input")


#lab 21 while loop
round = 0

while True:
    round += 1
    print('Finish the move title, "Monty Python\'s The life of _____')
    answer = input("Your guess --> \n>")
    if answer.lower() == "brian":
        print('Correct')
        break
    elif round == 3:
        print("Sorry, the answer was Brian")
        break
    else:
        print("Sorry! Try again!")

round = 0
#
while round < 3 and answer.lower() != "brian":
    round += 1
    print('Finish the move title, "Monty Python\'s The life of _____')
    answer = input("Your guess --> \n>")
    if answer.lower() == "brian":
        print('Correct')
    elif round == 3:
        print("Sorry, the answer was Brian")
    else:
        print("Sorry! Try again!")

    