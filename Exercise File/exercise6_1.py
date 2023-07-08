# helper variable for largest number
largest = 0
# assign error to false
error = False
# ask the user for 5 positive integer
for x in range(5):
    number = int(input("Give a number:\n"))
# if number is lesser than 0
# print wrong input
    if number < 0:
        print("Wrong input")
        error = True
        break
    elif number >= 0:
        if number > largest:
            largest = number
# if not error print the largest number
if not error:
    print(f"The biggest number from user: {largest}")
