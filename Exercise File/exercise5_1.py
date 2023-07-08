# print number 1-50 on separate lines
# using while loop
y = 1
while y <= 50:
    print(y)
    y = y + 1
# print number 1-50 on separate lines
# using for loop
x = 1
for x in range(50):
    x = x + 1
    print(x)
# create a loop to add the first 30 numbers
# print the sum of the letter
total = 0
for x in range(0, 30):
    x = x + 1
    total = total + x
print(f"Sum: {total}")
# print years in the range of 2005 - 2010
# print it in a single line
text = ""
for year in range(2004, 2010):
    year = year + 1
    text = text + str(year) + " "

print(f"{text}")
