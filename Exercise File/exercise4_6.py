# ask for temperature and humidity
temp = int(input("Temperature:\n"))
hum = int(input("Humidity:\n"))
# Assign the boolean variables to each situation
freezing = False
heatwave = False
raining = False
hailstorm = False
# if temperature is less tha 0
if temp < 0:
    freezing = True
    raining = False
    # if temperature is less than -20
    if temp < -20:
        hailstorm = True
        raining = False
# if temperature is greater than 20
elif temp > 20:
    heatwave = True
# if humidity is greater than 80
if hum > 80:
    raining = True
    if temp < 0:
        raining = False
# print the result
weather = ""
if freezing:
    weather = "It's freezing outside."
if hailstorm:
    weather = "There's a hailstorm, be careful!"
if heatwave:
    weather = "Heatwave! Remember to hydrate!"
if raining is True:
    weather = "It's raining."
# if there's rain and heatwave
if raining and heatwave:
    weather = "It's damp and hot."
print(f"Temperature is {temp}°C, {weather}")
