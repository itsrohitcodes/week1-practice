# Course enrollment analyzer

courses = {
    "Python": 25,
    "Java": 18,
    "SQL": 30,
    "Web": 15
}

# Display all courses and enrollment count
print("Course Enrollments:")
for course, enrollment in courses.items():
    print(course, ":", enrollment)

# Ask user for a course
course_name = input()

if course_name in courses:
    print("Current Enrollment:", courses[course_name])
else:
    print("Course not found.")

total_enrollments = sum(courses.values())
highest_course = max(courses, key=courses.get)
lowest_course = min(courses, key=courses.get)

more_than_20 = set()
for course, enrollment in courses.items():
    if enrollment > 20:
        more_than_20.add(course)

print("Total Enrollments:", total_enrollments)
print("Course with Highest Enrollment:", highest_course)
print("Course with Lowest Enrollment:", lowest_course)
print("Courses Having More Than 20 Students:", more_than_20)