# Ask for exam points
# program gives grades
# If its outside 0-100
# print invalid point value
points = int(input("Exam points:\n"))
if 0 <= points <= 50:
    print(f"Grade: 0")
elif 51 <= points <= 60:
    print(f"Grade: 1")
elif 61 <= points <= 70:
    print(f"Grade: 2")
elif 71 <= points <= 80:
    print(f"Grade: 3")
elif 81 <= points <= 90:
    print(f"Grade: 4")
elif 91 <= points <= 100:
    print(f"Grade: 5")
else:
    print("Invalid points value.")
