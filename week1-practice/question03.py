courses = {
    "Python": 25,
    "Java": 18,
    "SQL": 30,
    "Web": 15
}


print("Course Enrollments:")
for course, enrollment in courses.items():
    print(f"{course}: {enrollment}")


course_name = input().strip().lower()

for course in courses:
    if course.lower() == course_name:
        print(f"Current Enrollment: {courses[course]}")
        break
else:
    print("Course not found.")
    

total_enrollments = sum(courses.values())
highest_course = max(courses, key=courses.get)
lowest_course = min(courses, key=courses.get)

more_than_20 = [
    course
    for course, enrollment in courses.items()
    if enrollment > 20
]


print(f"Total Enrollments: {total_enrollments}")
print(f"Course with Highest Enrollment: {highest_course}")
print(f"Course with Lowest Enrollment: {lowest_course}")
print(f"Courses Having More Than 20 Students: {more_than_20}")
