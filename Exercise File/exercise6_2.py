# set the running variable to True
# use the while loop
running = True
while running is True:
    # ask the user for the multiplication table from (1-10)
    # 0 stops the application
    number = int(input("Which multiplication table do you want to see? (1-10). 0 stops the program:\n"))
    # if the number given is 0 application stops
    # print a message
    if number == 0:
        running = False
        print("Thank you for using our application!")
    # only create table for numbers from 1-10
    elif 1 <= number <= 10:
        for x in range(0, 10):
            x = x + 1
            result = number * x
            print(f"{number} x {x} = {result}")
        print()
    # print wrong format for any other number
    else:
        print("Wrong number format.")
        print()
