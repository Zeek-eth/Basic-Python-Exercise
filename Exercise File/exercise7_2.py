# given list
fruits = ["apple", "pear", "banana"]
berries = ["strawberry", "blueberry", "blackberry"]
vegetables = ["carrot", "kale", "cucumber"]
# the inventory that has the 3 list in it
# invent has 3 goods in it
# print all on a separate line
inventory = [fruits, berries, vegetables]
for invent in inventory:
    for food in invent:
        print(food)

