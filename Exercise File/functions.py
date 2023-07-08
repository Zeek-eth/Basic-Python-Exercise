# i had to import math to get pi
import math
# i also had to import random for the lottery numbers
import random


# functions to print info on 3 different lines
def show_personal_info():
    print("James Thomas")
    print("Ireland")
    print("Solidity Developer")


# function to get total amount of seconds
def count_seconds(hours, minutes, seconds):
    total_seconds = (hours * 60 * 60) + (minutes * 60) + seconds
    return total_seconds


# function to check serial number
def magazine_serial_check(serial):
    if serial[4] != "-":
        return False
    if len(serial) != 9:
        return False
    if not serial.replace("-", "").isdigit():
        return False
    else:
        return True


# functions to show numbered list
def show_numbered_list(title, data):
    print(title)
    for i, name in enumerate(data):
        print(f"{i + 1}. {name}")
    print()


# create 3 different functions
# volume of a box
def box_volume(width, height, depth):
    formula = width * height * depth
    formula = round(formula, 2)
    return formula


# volume of a ball
def ball_volume(radius):
    formula = (4 * math.pi * radius ** 3) / 3
    formula = round(formula, 2)
    return formula


# volume of a pipe
def pipe_volume(radius, length):
    formula = (math.pi * radius ** 2 * length)
    formula = round(formula, 2)
    return formula


def generate_lottery_numbers():
    # Generate a list of 7 unique numbers between 1 and 40
    numbers = random.sample(range(1, 41), 7)
    return numbers

