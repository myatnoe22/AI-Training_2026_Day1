students = [
    {"name": "Aung Aung", "score": 85},
    {"name": "Su Su", "score": 92},
    {"name": "Mg Mg", "score": 35}
]

def classify_grade(score):
    if score >= 80:
        return "Excellent"
    elif score >= 60:
        return "Good"
    elif score >= 40:
        return "Pass"
    else:
        return "Fail"


print("All Students:")
print(students)

print("\nPassing Students:")

for student in students:
    score = student["score"]

    if score >= 40:
        grade = classify_grade(score)
        print(f"Name: {student['name']} | Score: {score} | Grade: {grade}")

students.append({"name": "Mya Mya", "score": 90})
print(students)