# the try section
# Ask for two numbers
# divide the number
# print the result
try:
    number1 = int(input("First number:\n"))
    number2 = int(input("Second number:\n"))
    divide = number1/number2
    print(divide)
# user didn't give a value
# print incorrect format
# user divided by zero
# print you can't divide by zero
except ValueError:
    print("Incorrect format.")
except ZeroDivisionError:
    print("You can't divide by zero.")
