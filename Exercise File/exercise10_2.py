# Import json
# use the datetime module also
import json
from datetime import datetime

# request
request = input("Would you like to read or write into the guestbook? (r/w)\n")

# for writing into the file
if request == "w":
    append = open("guestbook.json", "a", encoding="utf-8")
    message = input("Write a message:\n")
    message = message
    append.write(message)
    print("File added")
    append.close()

# for the read file
# print everything
if request == "r":
    details = open("guestbook.json", "r")
    contents = details.readlines()
    for content in contents:
        print(content)
        details.close()




