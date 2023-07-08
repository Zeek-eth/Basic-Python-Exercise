# get functions from the functions file
from functions import *

# ask for serial number
code = input("Give an ISSN-serial:\n")

# to check the given code
check = magazine_serial_check(code)

# print the respective results
if check is False:
    print("Incorrect ISSN")
else:
    print("Valid ISSN")