# Calculate the Volume of a box and Volume of a sphere
# Ask the value for each side
import math
a = float(input("Give the first side:\n"))
b = float(input("Give the second side:\n"))
c = float(input("Give the third side:\n"))
# calculate volume and print
volume = a * b * c
print(f"Box Volume: {volume}m3")
# Calculate the volume of a sphere
# Ask values of radius
radius = float(input("Give the sphere radius:\n"))
#Calculate the volume,round and print
sphere_volume = (4/3) * math.pi * radius**3
sphere_volume = round(sphere_volume,2)
print(f"Sphere volume: {sphere_volume} m3")