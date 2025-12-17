student_scores = {
    "Deepak": 88,
    "Smriti": 98,
    "Golu": 78,
    "Nisha": 68,
    "Vijai Kumar": 99,
    "Ratna": 77
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]

    if score >=90:
        student_grades[student] = "A"
    elif score >=75:
        student_grades[student] = "B"
    elif score >=60:
        student_grades[student] = "C"
    elif score >=40:
        student_grades[student] = "D"
    else:
        student_grades[student] = "F"

print(student_grades)