# Import all the modules I need
import requests
import var_dump as vd

# load data from internet
url = 'https://edu.frostbit.fi/api/weather/'
req = requests.get(url)
data = req.json()
# weather now contains our data
weather = data

weak_location = ""
strong_location = ""
weakest_wind = 0
strongest_wind = 0
sum_wind = 0

# helper variables for cities wind
lapland = []
middle = []
south = []

# loop through the data in the weather
for var in weather:
    location = var["location"]
    snow = var["snow"]
    wind = var["wind"]
    area = var["area"]

    if wind < weakest_wind or weakest_wind == 0:
        weakest_wind = wind
        weak_location = var["location"]

    if wind > strongest_wind:
        strongest_wind = wind
        strong_location = var["location"]

    if area == "south":
        wind = var["wind"]
        south.append(wind)

    if area == "lapland":
        wind = var["wind"]
        lapland.append(wind)

    if area == "middle":
        wind = var["wind"]
        middle.append(wind)

# get average for southern finland
sum_south = sum(south)
amount = len(south)
average = round(sum_south/amount, 2)

# get average for lapland
sum_lapland = sum(lapland)
amount1 = len(south)
average1 = round(sum_lapland/amount1, 2)

# get average for middle finland
sum_middle = sum(middle)
amount2 = len(middle)
average2 = round(sum_middle/amount2, 2)

# Print the result
# The average wind of each area
# the city that has the strongest and weakest wind
print(f"Average wind, lapland: {average1} m/s")
print(f"Average wind, Middle part of Finland: {average2} m/s")
print(f"Average wind, Southern Finland: {average} m/s")
print()
print(f" Strongest wind today at location: {strong_location}, {strongest_wind}m/s")
print(f" Weakest wind today at location: {weak_location}, {weakest_wind}m/s")
