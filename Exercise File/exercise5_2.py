# ask the user the amount of rain
# ask the user 10 times
# sum the amount of rain
total = 0
for x in range(12):
    number = int(input("Give the amount of rain:\n"))
    x = x + 1
    total = total + number
# calculate the average of the amount of rain fell
# print the result
average = total / x
print(f"Your average amount of rain = {average}mm")