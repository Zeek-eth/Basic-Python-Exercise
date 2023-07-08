# Calculate the hypotenuse of a right angled triangle
# Ask for the values of each leg
import math

a = float(input("Give the first leg:\n"))
b = float(input("Give the second leg:\n"))
# calculate the hypotenuse
c = math.sqrt(a ** 2 + b ** 2)
c = round(c, 2)
print(f"Hypotenuse: {c} m")
