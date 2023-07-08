# get functions from the functions file
from functions import *

# ask for the respective parameters
hours = int(input("Give Hours:\n"))
minutes = int(input("Give Minutes:\n"))
seconds = int(input("Give seconds:\n"))

time = int(input(f"{hours}h {minutes}min {seconds}sec"))
# total amount of seconds
total_seconds = count_seconds(hours, minutes, seconds)

# print total amount of seconds
print(f"{total_seconds} seconds in total.")
