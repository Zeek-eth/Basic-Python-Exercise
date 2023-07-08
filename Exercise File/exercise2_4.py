# Calculating for total fuel consumption
# Ask for kilometres driven inside and outside urban areas
kilo_out = float(input("Kilometers outside urban area:\n"))
kilo_in = float(input("Kilometers within urban area:\n"))
# Calculate for fuel consumption
# Add and print result
fuel_out = kilo_out * 0.051
fuel_in = kilo_in * 0.075
total_fuel = fuel_in + fuel_out
print(f"Consumption: {total_fuel} l")
