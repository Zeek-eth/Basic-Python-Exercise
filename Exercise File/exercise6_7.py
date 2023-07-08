# ask the user for range
range_1 = int(input("Give the range start:\n"))
range_2 = int(input("Give the range end:\n"))
range_1 = range_1 - 1
# for every number in range given by user
# check if it's divisible by 5
# check if it's divisible by 7
for number in range(range_1, range_2):
    number = number + 1
# if number is divisible by 5 and 7
# print 'this' and break
# if not print Suitable number not found
    if number % 5 == 0 and number % 7 == 0:
        print(f"The number {number} is divisible 5 and 7!")
        break
    if number % 5 != 0:
        numb = 5
    elif number % 7 != 0:
        numb = 7
    print(f"{number} is not divisible by {numb}, skip.")
    continue
else:
    print("Suitable number not found")
