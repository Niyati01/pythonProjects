
student_scores = {
    "John" : 54,
    "Emily" : 65,
    "Jack" : 73,
    "Ava" : 98,
    "Ema" : 81,
}

student_grades = {}

for student in student_scores:
    if student_scores[student] >= 91 and student_scores[student] <= 100:
        student_grades[student] = "OutStanding"
    
    elif student_scores[student] >= 81 and student_scores[student] <= 90:
        student_grades[student] = "Exceeds Expectation"
    
    elif student_scores[student] >= 71 and student_scores[student] <= 80:
        student_grades[student] = "Acceptable"
    
    else:
        student_grades[student] = "Fail"

print(student_grades)
    