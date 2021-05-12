#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
ANIMALS = ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]
print(f"Here is the farms: {farms}")

# pick farm by farm name
def farmPicker(farmsList, farmName):
    result = []
    for item in farmsList:
        if(farmName != None and item["name"] == farmName):
            result.append(item)
    return result

# if animal is true, only collect animal
def farmPickerByType(farmsList, farmName, animalOnly=False):
    result = []
    myFarms = farmPicker(farmsList, farmName)
    for item in myFarms:
        things = item["agriculture"]
        for thing in things:
            if animalOnly:
                if thing in ANIMALS:
                    result.append(thing)
            else:
                result.append(thing)
    return result

# collect user input
def userChoice():
    for i in range(0, len(farms)):
        print(f'Farm ID:{i} - {farms[i]["name"]}')
    while True:
        try:
            userInput = input("Choose your farm by entering Farm ID:\n>")
            farmId = int(userInput)
            if farmId >= len(farms) and farmId < 0:
                break
            else:
                return farms[farmId]["name"]
        except:
            print("Invalid Input")

# Function 1
# • Write a for loop that returns all the animals from the NE Farm!
print(farmPickerByType(farms, "NE Farm", True))
print(farmPickerByType(farms, "SE Farm", True))

# Function 2
# • Ask a user to choose a farm (NE Farm, W Farm, or SE Farm). Return the plants/animals that are raised on that farm.
userFarm = userChoice()
print(farmPickerByType(farms, userFarm))

# Function 3
# • Ask a user to choose a farm (NE Farm, W Farm, or SE Farm)... but only return ANIMALS from that particular farm.
userFarm = userChoice()
print(farmPickerByType(farms, userFarm, True)) # only animals
