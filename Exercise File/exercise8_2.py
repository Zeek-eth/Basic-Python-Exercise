# import necessary modules
import random
from colorama import Back, Style

# the random number
target = random.randint(1, 20)

# while loop to check
# print corresponding reply
# break to stop the loop
while True:
    guess = int(input("Guess the number (1,20):\n"))
    if guess < target:
        print(Back.BLUE + "Too low.")
    elif guess > target:
        print(Back.RED + "Too high.")
    elif guess == target:
        print(Back.GREEN + "CONGRATULATIONS!!")
        break
    print(Style.RESET_ALL)