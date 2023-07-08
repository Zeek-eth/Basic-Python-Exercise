# import necessary modules
from colorama import Back, Style


# the prime function
def is_prime(num):
    # check if the number is less than 2
    # return false
    if num < 2:
        return False

    # check if the number is divisible by any number from 2 to its square root
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    # If the number is not divisible by any number from 2 to its square root, it is prime
    return True


# print the corresponding message
for x in range(2, 101):
    if is_prime(x):
        print(Back.GREEN + f"{x}")
    else:
        print(Back.RED + f"{x}")
