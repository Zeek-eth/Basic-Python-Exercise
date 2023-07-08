# get functions from the functions file
from functions import *

# the applications would be in a while true loop
while True:

    # ask for operation to be performed
    choice = int(input("Select the operation(1-3), 0 stops the application:\n"))

    # if choice is 0 exit the loop
    if choice == 0:
        print("Thank you for using our application!!")
        break

    # else if the choice is 1
    elif choice == 1:
        width = int(input("Whats the width of the box?:\n"))
        height = int(input("What is the height of the box?:\n"))
        depth = int(input("What is the depth of the box?:\n"))
        result = box_volume(width, height, depth)
        print(f"The volume of the box is {result} m")

    # else if the choice is 2
    elif choice == 2:
        radius = int(input("Radius of the ball?:\n"))
        result = ball_volume(radius)
        print(f"The volume of the ball is {result} m")

    # else if the choice is 3
    elif choice == 3:
        radius = int(input("Radius of the pipe?:\n"))
        length = int(input("length of the pipe?:\n"))
        result = pipe_volume(radius, length)
        print(f"The volume of the pipe is {result} m")

    # if none of the choices print this error message.
    else:
        print("Invalid Choice. Please try again!")
