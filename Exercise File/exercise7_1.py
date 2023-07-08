# Given dictionary
cafe = {
    "name": "Imaginary Cafe Ltd.",
    "website": "https://edu.frostbit.fi/sites/cafe/en",
    "categories": [
        "cafe",
        "tea",
        "lunch",
        "breakfast"
    ],
    "location": {
        "city": "Rovaniemi",
        "address": "Test address 22",
        "zip_code": "FI-96100"
    }
}
# print details on a separate line
# Needed location variable to get zip_code and address
location = cafe["location"]
print(cafe["name"])
print(location["address"])
print(location["zip_code"], location["city"])
print()
print(cafe["website"])
# for all services in category
# print it on a single line
line = ", ".join(cafe["categories"])
print(f"Services: {line}")
