# Assign Variables
cent = int(input("How many cents? (1-100):\n"))
# Divide by the value of each cent and find the remainder
# divide the remainder by the next value of cent and repeat
# keep this on repeat
cen1 = cent // 50
cen11 = cent % 50
cen2 = cen11 // 20
cen22 = cen11 % 20
cen3 = cen22 // 10
cen33 = cen22 % 10
cen4 = cen33 // 5
cen44 = cen33 % 5
cen5 = cen44 // 2
cen55 = cen44 % 2
cen6 = cen55 // 1
cen66 = cen55 % 1
# Prints the results
print(f"Amount of 50 cents: {cen1}")
print(f"Amount of 20 cents: {cen2}")
print(f"Amount of 10 cents: {cen3}")
print(f"Amount of 5 cents: {cen4}")
print(f"Amount of 2 cents: {cen5}")
print(f"Amount of 1 cents: {cen6}")
