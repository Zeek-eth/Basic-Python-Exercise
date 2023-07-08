# ask the user number of students
number = int(input("How many students?:\n"))
# grades list
grades = []
# ask for every student in range of student
# append grades
for x in range(number):
    exam = int(input("Exam grade:\n"))
    grades.append(exam)
# sort the grades
# find the median
# find the average
# print the results
grades.sort()
mid = len(grades) // 2
median = (grades[mid] + grades[~mid]) / 2
res = sum(grades)
avg = res / len(grades)
avg = round(avg, 1)


# to calculate the most frequent
def most_frequent(grades):
    return max(set(grades), key=grades.count)


# get the most common grades
common = most_frequent(grades)
print(f"Most Common:{common}")
print(f"Median: {median}")
print(f"Average grade: {avg}")
# if statements to get the commentsa of the average grade
if 0 <= avg < 1:
    print("Bad Result")
elif 1 <= avg < 2:
    print("Weak Result")
elif 2 <= avg < 3:
    print("Average Result")
elif 3 <= avg < 4:
    print("Good Result")
elif 4 <= avg < 5:
    print("Excellent Result")
