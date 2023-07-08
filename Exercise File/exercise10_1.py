# open the file
# open a connection to our file
file = open("artists.txt", "r")

# read all contents to a variable
# print message
contents = file.readlines()
print(f"Some of the best-selling music album in history:\n")

# for every content in contents print into a new line
for content in contents:
    print("->" + content, end='')

# close the file handle
file.close()


