# Ask for year
year = int(input("Give year:\n"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year: YES")
        else:
            print("Leap year: NO")
    else:
        print("Leap year: YES ")
else:
    print("Leap year: NO")
