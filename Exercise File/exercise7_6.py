# import var_dump
import var_dump as vd

# create an application that has multiple restaurants
rest_1 = {"name": "North Delish",
          "rating": 4.5,
          "reservations": True,
          "services": ["lunch", "dinner"],
          "price_level": 5,
          "location": "Rovaniemi"}

rest_2 = {"name": "Food Galore",
          "rating": 3.8,
          "reservations": False,
          "services": ["Breakfast", "lunch"],
          "price_level": 3,
          "location": "London"}

rest_3 = {"name": "Snacksy Ltd",
          "rating": 3.2,
          "reservations": False,
          "services": ["lunch", "dinner", "night"],
          "price_level": 2,
          "location": "Berlin"}

rest_4 = {"name": "Dalish Kitchen",
          "rating": 4.2,
          "reservations": True,
          "services": ["breakfast", "lunch", "dinner"],
          "price_level": 4,
          "location": "New York"}

rest_5 = {"name": "Cheers Cafe",
          "rating": 2.9,
          "reservations": False,
          "services": ["lunch", "night"],
          "price_level": 3,
          "location": "Oakland"}
# all restaurants into a single list
restaurants = [rest_1, rest_2, rest_3, rest_4, rest_5]

# All the questions needed to be asked
star_rate = int(input("Which star rating at least for the restaurant? (1-5)\n"))
price_lev = int(input("What is the maximum price level you're looking for? (1-5)\n"))
reserve = input("Would you like to make a reservation before hand? (y/n)\n")
time = int(input("In what time would you like to arrive? (0 – 23)\n"))

# set the time to integers intervals
if 0 <= time <= 5:
    time = "night"
elif 6 <= time <= 10:
    time = "breakfast"
elif 11 <= time <= 16:
    time = "lunch"
elif 17 <= time <= 24:
    time = "dinner"

# desired choice helper list
desired_rest = []

# Loop through all the restaurants
for rest in restaurants:
    rating = rest["rating"]
    price_level = rest["price_level"]
    reservation = rest["reservations"]
    name = rest["name"]
    service = rest["services"]
    location = rest["location"]

    # check for reservation status
    if reserve == "y":
        reservation = True
    elif reserve == "n":
        reservation = False

    # check for all criteria
    # print corresponding result
    if star_rate <= rating:
        if price_lev >= price_level:
            if time in service:
                if reservation is False:
                    desired_rest.append(name)
                elif reservation is True:
                    continue

if len(desired_rest) <= 0:
    print("No matching restaurants found,unfortunately!")
if len(desired_rest) > 0:
    result = "\n".join(desired_rest)
    print(result)
