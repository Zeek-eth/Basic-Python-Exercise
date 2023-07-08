#Temperature
temperature = input("Outside temperature:\n")
temperature = int(temperature)
#Humidity
humidity = input("humidity percentage:\n")
humidity = int(humidity)

print(f"Temperature: {temperature} C")
#Variables
freezing = False
heatwave = False
raining = False
hailstorm = False

if temperature <= 0:
    freezing = True

if freezing:
    print("It's freezing outside.")

if humidity > 80:
    raining = True

if raining:
    print("It's raining")

if temperature <= -20:
    hailstorm = True

if hailstorm:
    print("There's a hailstorm, be careful!")

if temperature >= 20:
    heatwave = True

if heatwave:
    print("Heatwave! Remember to hydrate!")

elif raining and heatwave:
    print("It's damp and hot!")