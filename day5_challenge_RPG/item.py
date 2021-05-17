"""
Item class contains item info

Attributes:
- name: item name
- descrition: item description

Mehtod:
__str__: toString()

"""

class Item:
    def __init__(self, name= "DEFAULT", description = "N/A"):
        self.name = name
        self.description = description
    
    def __str__(self):
        return f'(Item name: {self.name}, Item Description: {self.description})'
    
    # def __iter__(self):
    #     yield 'name', self.name
    #     yield 'description', self.description