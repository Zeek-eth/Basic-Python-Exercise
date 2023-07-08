# import random
import random

# the file handle
file_handle = open("wisewords.txt", "r")
content = file_handle.read()

# split all the contents
lines = content.split("\n")

# number of proverbs
proverbs = len(lines) - 1
proverbs = int(proverbs)

# pick a random proverb
choice = random.randint(0, proverbs)
proverb = lines[choice]

# close the file
file_handle.close()

# print proverb
print("Today's proverb:")
print(proverb)
