# Give the price
price = input("Give the price without VAT:\n")
price = float(price)
# Calculate the value plus vat and round it up
# Print your answers
vat = (price * 1.24)
vat = round(vat, 2)
print(f"Price with VAT:\t{vat}€")
