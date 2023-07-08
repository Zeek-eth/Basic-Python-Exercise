# import json file
import json

# the file handler
county = open("countries.json", "r")
content = county.read()
county.close()

countries = json.loads(content)

# print messages
print("All countries and capitals:")

# loop through all
for a in countries:
    print(f"{a['country']}: {a['capital']}")

# ask for the letter
given_letter = input("Filter a country/capital with a starting letter (A-Z):\n")

# print all result wrt to the given letter
for b in countries:
    if b['country'][0].lower() == given_letter:
        print(f"{b['country']}: {b['capital']}")



