# helper method farm picker
def farmPicker(farmsList, farmName):
    for item in farmsList:
        if(farmName != None and item["name"] == farmName):
            print(item)
    return 0;