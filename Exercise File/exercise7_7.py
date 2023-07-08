# remember to install this module before using
import requests

# load data from internet
url = 'https://liukastumisvaroitus-api.beze.io/api/v1/warnings'
req = requests.get(url)

# covert it into json file
warnings = req.json()

# helper dictionary variable
total_city = {}

#
warnings.sort(key=lambda i: i['updated_at'], reverse=True)

# loop through all the warnings
for warning in warnings:
    city = warning['city']

    if city not in total_city:
        total_city[city] = 0

    total_city[city] = total_city[city] + 1

for warning in range(5):
    print(warnings[warning]['city'])

# print(latest)
# print the city with corresponding amount

print(total_city)


