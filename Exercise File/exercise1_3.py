# Calculate fuel consumption of a car by Lenght
# Give Lenght
trip = input("Give the trip lenght:\n")
trip = float(trip)
# Get fuel consumed
fuel = (trip * 0.065)
fuel = round(fuel, 1)
print(f"Consumption: {fuel} l")
