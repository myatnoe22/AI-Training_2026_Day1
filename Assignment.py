
GRADE_CATEGORIES = ("Excellent", "Good", "Pass", "Fail")
def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)
def classify_grade(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 80:
        return "Excellent"
    elif score >= 60:
        return "Good"
    elif score >= 40:
        return "Pass"
    else:
        return "Fail"

def count_passed(students):
    count = 0

    for student in students:
        if student["score"] >= 40:
            count += 1

    return count

students = [
    {"name": "Aung Aung", "age": 21, "study_hours": 4.5, "score": 85},
    {"name": "Su Su", "age": 20, "study_hours": 3.0, "score": 65},
    {"name": "Mg Mg", "age": 22, "study_hours": 5.0, "score": 92},
    {"name": "Mya Mya", "age": 19, "study_hours": 2.5, "score": 35},
    {"name": "Hla Hla", "age": 21, "study_hours": 4.0, "score": 75}
]
print("=" * 45)
print(" =========STUDENT PERFORMANCE REPORT==========")
print("=" * 45)

for student in students:
    grade = classify_grade(student["score"])

    print(f"\nName: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Study Hours: {student['study_hours']}")
    print(f"Score: {student['score']}")
    print(f"Grade: {grade}")

scores = [student["score"] for student in students]

average_score = calculate_average(scores)
highest_score = max(scores)
lowest_score = min(scores)
passed_students = count_passed(students)
failed_students = len(students) - passed_students

top_student = max(students, key=lambda student: student["score"])

print("\n" + "=" * 45)
print("                  SUMMARY")
print("=" * 45)

print(f"Total Students: {len(students)}")
print(f"Average Score: {average_score:.2f}")
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
print(f"Passed Students: {passed_students}")
print(f"Failed Students: {failed_students}")
print(f"Top Student: {top_student['name']}")