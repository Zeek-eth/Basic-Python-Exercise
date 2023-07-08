# are you a student?
status = input("Are you a student?: (y/n)\n ")
# Travel month
month = input("Travel month? (1-12)\n")
month = int(month)
# set special price to false
special_price = False
# if status is yes
if status == 'y':
    special_price = True

if special_price and (month != 6) and (month != 7) and (month != 8):
    print("Special price!")
else:
    print("Normal price.")
