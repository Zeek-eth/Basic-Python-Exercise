# Ask user for money
money = int(input("Give money:\n"))
# Ask user for purchase cost
cost = int(input("Purchase cost:\n"))
# calculate the change
change = money - cost
# If change is greater than 0 print this
if change > 0:
    print(f"Thank you. Here's the change:{change}€")
# if change is lesser than 0 ask for more money
# calculate  change
# if change is greater than 0
# Give change
# if change is less than 0
# the user doesn't have enough money
elif change < 0:
    more = int(input("Not enough money, give more:\n"))
    new_money = money + more
    change = new_money - cost
    if change > 0:
        print(f"Thank you. Here's the change:{change}€")
    elif change < 0:
        print("You don't have enough money.")
