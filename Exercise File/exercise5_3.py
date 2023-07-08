# import math
import math

running = True
# ask the user radius of a circle
# calculate the area of the circle
# print the result
while running:
    rad = int(input("Give radius:\n"))
    area = (rad**2) * math.pi
    area = round(area, 2)
    print(f"Circle area: {area}")
# ask if the user wants to continue
# ask if yes/no
    ask = input("Do you want to continue? (y/n)\n")
# if no stop the program
    if ask == "n":
        running = False
        print("Thank you for using our application.")




