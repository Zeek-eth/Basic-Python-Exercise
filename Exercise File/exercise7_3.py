# Given a shopping cart
#  list that contains dictionaries
shopcart = [
    {"name": "Beehive - lamp", "price": 999.9},
    {"name": "Malm - bed", "price": 169.9},
    {"name": "Moomin - mug set", "price": 59.9},
    {"name": "Nemo - divan", "price": 699.9},
    {"name": "Ritz - armchair", "price": 369.9}
]
# print the receipt
# total
# total vat
total = 0
total_vat = 0
# print receipt
print(f"Receipt:")
# loops all the goods inside the cart
for goods in shopcart:
    # get the name and the price
    name = goods["name"]
    price = goods["price"]
    # get the total of price of the goods
    total = total + price
    # calculate vat of each goods
    r_price = price / 1.24
    r_price = round(r_price, 1)
    vat = price - r_price
    # calculate total vat and round it
    total_vat = total_vat + vat
    total_vat = round(total_vat, 1)
    # print all the goods
    print(f"- {name}")
# print all the result
print()
print(f"Total vat: {total_vat} €.")
print(f"Total sum: {total} €.")
print("Please come again!")


