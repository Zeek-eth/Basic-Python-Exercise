choice = input("Letter or parcel? (l/p):")
# calculations for letter
if choice == 'l':
    print("User choose letter!")
    let = int(input("Weight:\n"))
    base = 50
    pin = let // 100
    pine = pin * 4
    price = pine + base

    pine2 = pin * 7
    price2 = pine2 + base
    if let < 200:
        print(f"Total cost is {base} cent")
    elif 200 < let < 500:
        print(f"Extra cost is {pine} cent")
        print(f"Total cost is {price} cent")
    elif let > 500:
        print(f"Extra cost is {pine2} cent")
        print(f"Total cost is {price2} cent")
# calculations for parcel
elif choice == 'p':
    print("User choose Parcel!")
    par = int(input("Weight:\n"))
    baseprice = 2
    parcel = par // 100
    pined = parcel * 8
    pricepaid = pined + baseprice

    pined2 = parcel * 14
    pricepaid2 = pined2 + baseprice
    if par < 200:
        print(f"Total cost is 2,{baseprice} € ")
    elif 200 < par < 500:
        print(f"Extra cost is 2,{pined} €")
        print(f"Total cost is 2,{pricepaid} €")
    elif par > 500:
        print(f"Extra cost is 2,{pined2} €")
        print(f"Total cost is 2,{pricepaid2} €")
else:
    print("Incorrect selection.")
print("Thank you for using our application!")
