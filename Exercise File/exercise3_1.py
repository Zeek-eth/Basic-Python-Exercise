# Ask for two integers
# check for the bigger one
# Print it
# If they are equal
# print they are equal
num1 = int(input("Give first number:\n"))
num2 = int(input("Give second number:\n"))
if num1 > num2:
    print(f"Bigger number = {num1}")
elif num2 == num1:
    print(f"Numbers are equal")
else:
    print(f"Bigger number = {num2}")
