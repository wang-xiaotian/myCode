# Project topic: can you waste $1 million within a week?
# 
#!/usr/bin/env python3

# 7 days and each day has 6 items to choose
DAYS_ITEMS_PRICES = [[10,20,30,40,10,20],[10,20,30,40,10,20],[10,20,30,40,10,20],[10,20,30,40,10,20],[10,20,30,40,10,20],[10,20,30,40,10,20],[10,20,30,40,10,20]] # items you can buy in 7 days
DAYS_TOPIC = ['Choose a hotel suite to stay in all week:', 'Choose a car to rent for the rest of the week:', 'Choose a venue to throw a kick-ass party:', 'Hire a celebrity to perform a private concert:', 'Choose a pricey restaurant to take 11 of your pals for dinner:', 'Choose an expensive bottle of wine to drink in one sitting:','Finally, choose a luxury SPA treatment so you can relax after a hard week of spending:']
DAYS_ITEMS = [['Royal 1', 'Royal 2', 'Royal 3', 'Royal 4','Royal 5','Royal 6'],['Ferrari 458 Italia', 'Maserati GranCabrio', 'Rolls Royce Phantom', 'Mayback 57S', 'McLaren MP4-12C', 'Lamborghini Ballardo Spyder'],['Madison Square, New York', 'Little Palm Island, Florida', 'The biltmore estate, North Carolina', 'Pelican Hill, CA', 'Odescalchi Castle, Italy', 'Chateaus Vaus-le-Vicomte'],['Aril Lavigne','Selena Gomez', 'Kendrick Lamar', 'Carly Rae Jepsen', 'Jason Drulo', 'Avicii'],['Sublimotion, Ibiza', 'Plaza Athenee, Paris', 'Ithaa Undersee Resturant', 'Aragawa, Tokyo', 'Restaurant Crissier, Switzerland', ' Masa, New York City'],['Chateau Margaus classe 1900', 'Domaine de la Romanee-Conti 1990', 'Chateau Lafite 1865', 'Heidsieck 1907', 'Chateau Mouton-Rothschild 1945', 'Cheval Blanc 1947'],["Evian Bath", "Gold Facial", "Diamond Massage", "Clay Body Treatment", "Turkish Bash", "Fish Pedicure"]];

# entrance
def main() :
    welcome()
    gameStarts()

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
    for i in range(0,6):
        printItems(i)
        while True:
            userInput = expenseQuestion()
            if userInput == -1 or userInput == 0 or userInput > 6:
                print("Come on! Just a number 1 - 6. Try again!")
            elif userInput == -2:
                print(f"Good luck!")
                exit()
            else:
                print(f"Price - {itemPicker(i,userInput-1)}")
                totalPrice += itemPicker(i,userInput-1)
                break
        print('\n')
    print(f'You just spent ${totalPrice}!')
    if totalPrice > 1000000:
        print("It is over $1,000,000. Pay your bills!")
    elif totalPrice < 1000000:
        print("It is less than $1,000,000. Pay your bills!")
    else:
        print("Well done! You just wasted $1,000,000!")
    return totalPrice;

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

def printItems(day):
    index = 0;
    for item in DAYS_ITEMS[day]:
        print(f'#{index} - {item}')

if __name__ == "__main__":
    main()