# Ask for temperature in integers
# Program would let you know the weather condition
temp = int(input("Give the temperature:\n"))
if 0 <= temp <= 10:
    print("COLD")
elif 11 <= temp <= 15:
    print("CHILLY")
elif 16 <= temp <= 20:
    print("NORMAL TEMPERATURE")
elif 21 <= temp <= 25:
    print("WARM")
elif 26 <= temp <= 30:
    print("HOT")
