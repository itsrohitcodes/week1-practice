# QUESTION 02

# Take Input from the user
student_name = input()
marks = []

for _ in range(5):
    mark = int(input())
    marks.append(mark)

total_marks = sum(marks)
average_marks = total_marks / len(marks)
highest_mark = max(marks)
lowest_mark = min(marks)

# Passed & Failed Subjects Count
passed_subject = 0
failed_subject = 0

for mark in marks:
    if mark >= 40:
        passed_subject += 1
    else:
        failed_subject += 1

# Grade Calculation based on average marks
if average_marks >= 90:
    grade = "A"
elif average_marks >= 75:
    grade = "B"
elif average_marks >= 60:
    grade = "C"
elif average_marks >= 40:
    grade = "D"
else:
    grade = "F"

# Print the results
print(f"Student Name: {student_name}")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Highest Mark: {highest_mark}")
print(f"Lowest Mark: {lowest_mark}")
print(f"Subjects Passed: {passed_subject}")
print(f"Subjects Failed: {failed_subject}")
print(f"Final Grade: {grade}")

print("Marks greater than average:")
for mark in marks:
    if mark > average_marks:
        print(mark)