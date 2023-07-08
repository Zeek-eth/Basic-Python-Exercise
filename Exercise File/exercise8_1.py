# import the modules needed
import datetime
from colorama import Fore, Style


# helper list variable
all_years = []

# loop through number 1-5
# append all the years
for x in range(1, 6):
    year = int(input(f"Give birth year of {x}:\n"))
    all_years.append(year)

# print empty line and message
print()
print("Let's process all birth years...")

# to get the datetime module
today = datetime.datetime.now()

# loop through all the years
# get the corresponding age
# check the age and print corresponding message
for year in all_years:
    age = today.year - year
    if 1 <= age <= 125:
        print(Fore.GREEN + f"{age} years old, age OK!")
    else:
        print(Fore.RED + f"{age} years old, incorrect age." + Style.RESET_ALL)

# print final message
print("All done!")
