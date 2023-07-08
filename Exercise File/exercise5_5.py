# create tuple for the montrhs
# this is a tuple
months = ("January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December")
# ask the user for the number of month
choice = input("Give the number in the month:\n")
# covert to integer
# Subtract 1 to get the exact number for each month
choice = int(choice) - 1
# print the month for each choice
print(months[choice])
