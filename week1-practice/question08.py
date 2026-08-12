# Student Skill Matcher

def match_skills(student_skills, required_skills):

    matched_skills = student_skills.intersection(required_skills)
    missing_skills = required_skills.difference(student_skills)
    extra_skills = student_skills.difference(required_skills)
    match_percentage = (len(matched_skills) / len(required_skills)) * 100

    return matched_skills, missing_skills, extra_skills, match_percentage


# Take input from user
student_skills = input()
required_skills = input()

student_skills = set(student_skills.split())
required_skills = set(required_skills.split())

matched_skills, missing_skills, extra_skills, match_percentage = match_skills(
    student_skills, required_skills
)

if match_percentage >= 70:
    status = "Eligible"
else:
    status = "Needs More Skills"

# Display results
print("Student Skills:", student_skills)
print("Required Skills:", required_skills)
print("Matched Skills:", matched_skills)
print("Missing Skills:", missing_skills)
print("Extra Skills:", extra_skills)
print("Match Percentage:", match_percentage)
print("Status:", status)