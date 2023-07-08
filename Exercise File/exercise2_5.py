# Generate random numbers
# Generate random rectangle sides
# Calculate the area of the random sides
import random

rnum = random.randint(1, 10)
print(f"Random number: {rnum}")
side_1 = random.randint(2, 10)
side_2 = random.randint(2, 10)
area = side_1 * side_2
print(f"First random side: {side_1}")
print(f"Second random side: {side_2}")
print(f"Rectangle area: {area}")
