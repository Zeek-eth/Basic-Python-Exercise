# get functions from the functions file
from functions import *

# ask all the names as one string from user
people_string = input("Write all participants, separated by a comma:\n")

# convert the text into a list
people = people_string.split(",")

# remove extra space-characters from each name (from the beginning and end)
people = [p.strip() for p in people]

# print the names in the original order
title = "Original Order:"
results = show_numbered_list(title, people)

# print the title
# sort the names in alphabetical order and print the result
title = "Alphabetic order by first name:"
people.sort()
result = show_numbered_list(title, people)

# print the title and sort the name in alphabetical order of the last name
title = "Alphabetic order by last name:"

# to get the last name
# sort the last name, then print the result
people = [" ".join(reversed(p.split(" "))) for p in people]
people.sort()
result = show_numbered_list(title, people)


