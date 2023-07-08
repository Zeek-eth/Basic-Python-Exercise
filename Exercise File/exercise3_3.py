# Ask for hours
hour = float(input("How many workhours this week?\n"))
# Ask for salary per hours
salary = float(input("Your hourly salary?\n"))
# Print weekly wage
# If the hours is less than 40 hours
wage = hour * salary
wage = round(wage, 2)
# new wage for overtime
wage2 = 40 * salary
overtime = (hour - 40) * (salary * 1.5)
total = wage2 + overtime
total = round(total, 2)
# Less than 40
if hour <= 40:
    print(f"Your weekly age: {wage}€")
# if the hours is more than 40
elif hour > 40:
    print(f"Your weekly wage: {total}€")
