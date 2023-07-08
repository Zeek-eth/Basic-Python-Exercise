# ask for total cost
cost = int(input("Cost:\n"))
# Ask for student status
student = str(input("Student(Y/N):\n"))
# Vip status
Vip = str(input("Vip(Y/N):\n"))
# Shipment cost
shipment = 7.95
# if customer is a VIP
# ask for points
# ask for special sales  code
# ask student status
if Vip == "Y":
    point = int(input("Points:\n"))
    sales = input("FALL22/BK2SCHOOL:\n")
    if sales == "FALL22":
        points = (cost // 10) * 100
        print(points)
        new_point = point + points
        print(new_point)
        new_points = new_point // 1000
        print(new_points)
        new_points = new_points * 5
        discount = cost * 0.1
        cost = cost - discount - new_points
        if 0 < cost < 99:
            cost = cost + shipment
            print(f"Total cost:{cost} €")
        else:
            print(f"Total cost:{cost} €")
    elif sales == "BK2SCHOOL" and student == "Y":
        points = (cost / 10) * 100
        new_point = point + points
        new_points = new_point / 1000
        print(new_points)
        discount = cost * 0.2
        cost = cost - discount - new_points
        if 0 <= cost <= 99:
            cost = cost + shipment
            print(f"Total cost:{cost} €")
        else:
            print(f"Total cost:{cost} €")
# if customer is not a vip
# also ask for sales code
# ask for student status
elif Vip == "N":
    sales = input("FALL22/BK2SCHOOL:\n")
    if sales == "FALL22":
        discount = cost * 0.1
        cost = cost - discount
        if 0 < cost < 99:
            cost = cost + shipment
            print(f"Total cost:{cost} €")
        else:
            print(f"Total cost:{cost} €")
    elif sales == "BK2SCHOOL" and student == "Y":
        discount = cost * 0.2
        cost = cost - discount
        if 0 < cost < 99:
            cost = cost + shipment
            print(f"Total cost:{cost} €")
        else:
            print(f"Total cost:{cost} €")
# for customer that is not a vip and with no special sales code.
else:
    if 0 < cost < 99:
        cost = cost + shipment
        print(f"Total cost:{cost} €")
    else:
        print(f"Total cost:{cost} €")
