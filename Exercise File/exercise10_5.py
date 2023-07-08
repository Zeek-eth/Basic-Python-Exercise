import json

file_handle = open("countries.json", "r")
content = file_handle.read()
file_handle.close()

countries = json.loads(content)

print("All countries and capitals:")
for y in countries:
    print(f"{y['country']}: {y['capital']}")

given_letter = input("Filter a country/capital with a starting letter (A-Z):\n")

for x in countries:
    if x['country'][0].lower() == given_letter:
        print(f"{x['country']}: {x['capital']}")



