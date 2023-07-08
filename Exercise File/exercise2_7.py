# Import Math
# ask for the values of a,b and c
import cmath
import math

a = float(input("value of a\n"))
b = float(input("value of b\n"))
c = float(input("value of c\n"))
# Break down the calculations into steps
# execute the calculations
# print answers
e = math.pow(b, 2) - (4 * a * c)

if e < 0:
    e = complex(cmath.sqrt(e))
    x1 = (-b + e) / (2 * a)
    x2 = (-b - e) / (2 * a)
    print(f"First value of x:{x1}")
    print(f"Second value of x:{x2}")
elif e == 0:
    x1 = -b // 2 * a
    x1 = round(x1, 2)
    print(f"First value of x:{x1}")

elif e > 0:
    x1 = (-b + math.sqrt(e)) / (2 * a)
    x2 = (-b - math.sqrt(e)) / (2 * a)
    x1 = round(x1, 2)
    x2 = round(x2, 2)
    print(f"First value of x:{x1}")
    print(f"Second value of x:{x2}")
