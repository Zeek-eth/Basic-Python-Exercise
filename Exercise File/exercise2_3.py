# Calculate the amount of money a user can spend and their taxes
# Ask for the value of the variables
salary = float(input("Your monthly salary:\n"))
tax = float(input("Your tax percentage:\n"))
# Calculate the Earnings
# Calculate the Taxes
# Round to two decimal places
# Print result
taxes = salary * (tax / 100)
earning = salary - (salary * (tax / 100))
taxes = round(taxes, 2)
earning = round(earning, 2)
print(f"Earnings: {earning} €")
print(f"Taxes: {taxes} €")
