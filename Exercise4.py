def greet():
    print("Welcome to Python for AI!")

greet()

def greet_student(name):
    print(f"Hello, {name}!")

greet_student("Aung Aung")
greet_student("Su Su")
print("-" * 30)



def calculate_total(scores):
    return sum(scores)



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

def count_passed(scores):
    passed_count = 0
    for score in scores:
        if score >= 40:
            passed_count += 1
    return passed_count