
#!/usr/bin/env python3

# TLG python project topic: can you waste $1 million within a week?
# the purpose of this project is to practice if-else logic
# ONLY used integer in this project
# perfect target price: {"Day 1-7: selection 4,6,1,3,5,6"}
# 7 days and each day has 6 items to choose
DAYS_ITEMS_PRICES = [[135315,238917,345262,254153,123153,214253],[325415,133928,21929,451133,223233,111263],[75415,141224,61323,271251,63232,21268],[95413,51126,91629,24257,123232,211268],[99433,191141,113224,74551,173134,91326],[165311,31326,61324,114257,113739,161263],[195413,21124,12629,27257,133143,131449]] # items you can buy in 7 days
DAYS_TOPIC = ['Choose a hotel suite to stay in all week:', 'Choose a car to rent for the rest of the week:', 'Choose a venue to throw a kick-ass party:', 'Hire a celebrity to perform a private concert:', 'Choose a pricey restaurant to take 11 of your pals for dinner:', 'Choose an expensive bottle of wine to drink in one sitting:','Finally, choose a luxury SPA treatment so you can relax after a hard week of spending:']
DAYS_ITEMS = [['Royal 1', 'Royal 2', 'Royal 3', 'Royal 4','Royal 5','Royal 6'],['Ferrari 458 Italia', 'Maserati GranCabrio', 'Rolls Royce Phantom', 'Mayback 57S', 'McLaren MP4-12C', 'Lamborghini Ballardo Spyder'],['Madison Square, New York', 'Little Palm Island, Florida', 'The biltmore estate, North Carolina', 'Pelican Hill, CA', 'Odescalchi Castle, Italy', 'Chateaus Vaus-le-Vicomte'],['Aril Lavigne','Selena Gomez', 'Kendrick Lamar', 'Carly Rae Jepsen', 'Jason Drulo', 'Avicii'],['Sublimotion, Ibiza', 'Plaza Athenee, Paris', 'Ithaa Undersee Resturant', 'Aragawa, Tokyo', 'Restaurant Crissier, Switzerland', ' Masa, New York City'],['Chateau Margaus classe 1900', 'Domaine de la Romanee-Conti 1990', 'Chateau Lafite 1865', 'Heidsieck 1907', 'Chateau Mouton-Rothschild 1945', 'Cheval Blanc 1947'],["Evian Bath", "Gold Facial", "Diamond Massage", "Clay Body Treatment", "Turkish Bash", "Fish Pedicure"]]
PRICE = 1000000 # target price


#greeting message
def welcome():
    userName = input("What is your name?\n>").upper()
    # greetingMessage
    print(f"Congratulations {userName}! Here is your letter from the President of United States.\n")
    # letter body
    print(f"Dear {userName},\n\nAs you are probably well aware, a $1.9 trillion coronavirus relief package, known as the American Rescue Plan, aims to help individuals and families throughout the country as well as state and local governments.\n")
    # requirement
    print("In order to receive your $1,000,000 stimulus check. You have to spend exact $1,000,000 in one week, but you won't be shown any of the prices of the things you are buying.\nIf you cannot meet this requirement, the stimulus check will be moved to next lucky person. YOU ARE RESPONSIBLE FOR ALL YOURE EXPENSES. Have fun!\n")

# collection user input and calculate price
def gameStarts():
    totalPrice = 0;
    print(f"Warning: You can quit this program anytime by typing \"exit\" and press Enter.\n\n")
    # display items and collect user selection
    for i in range(0,7):
        printItems(i)
        # collect valid user input value or exit program
        while True:
            userInput = expenseQuestion()
            if userInput == -1 or userInput == 0 or userInput > 6:
                print("Come on! Just a number 1 - 6. Try again!")
            elif userInput == -2: # exit
                print(f"Good luck! You already spent ${totalPrice}. Pay your bill!")
                exit()
            else:
                totalPrice += itemPicker(i,userInput-1)
                break
        print('\n')

    print(f'You just spent ${totalPrice}!')
    leftOver = calculateLeftOver(totalPrice)
    if leftOver > 0 :
        print(f"It is over target price ${leftOver}. Pay your bill!")
    elif leftOver < 0:
        print(f"It is less than target price ${abs(leftOver)}. Pay your bill!")
    else:
        print("Well done! You just wasted $1,000,000!")
    return leftOver;

# determin item value from pre defined item list
def itemPicker(day, item):
    return DAYS_ITEMS_PRICES[day][item];

# collect user answer of which item the user want to buy
def expenseQuestion():
    result = -1;
    userInput = input("Please enter your item number 1-6:\n>")
    if userInput.isdigit():
        result = int(userInput);
        if result < 0:
            result = -1 # user input error
    elif userInput == "exit":
        result = -2
    return result

#　print with format
def printItems(day):
    print(f"Day {day+1}")
    index = 1;
    for item in DAYS_ITEMS[day]:
        print(f'#{index} - {item}')
        index += 1

# helper method: the goal is $1,000,000
# return how much left over
def calculateLeftOver(expense):
    return expense - PRICE

# entrance
def main() :
    welcome()
    gameStarts()

if __name__ == "__main__":
    main()