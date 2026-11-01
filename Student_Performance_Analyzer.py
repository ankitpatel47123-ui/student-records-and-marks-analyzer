# Student Performance Analyzer
subjects = ["Python", "Maths", "DBMS"]
def add_student(student_id, name, marks):
    return {
        "id": student_id,
        "name": name,
        "marks": marks
    }
def calculate_total(marks, bonus=0):
    return sum(marks) + bonus
def calculate_average(total, count=3):
    return total / count
def class_total(*totals):
    return sum(totals)
def student_details(**details):
    return details
def get_averages(students):
    return list(map(
        lambda s: sum(s["marks"]) / len(s["marks"]),
        students
    ))
def high_performers(students):
    return list(filter(
        lambda s: sum(s["marks"]) / len(s["marks"]) >= 75,
        students
    ))
def recursive_sum(n):
    if n == 0:
        return 0
    return n + recursive_sum(n - 1)

def display_report(students):

    print("\n===== STUDENT PERFORMANCE REPORT =====")
    totals = []
    for student in students:
        name = student["name"]
        marks = student["marks"]
        total = calculate_total(marks)
        average = calculate_average(total, count=len(marks))
        totals.append(total)

        if average >= 75:
            grade = "Distinction\n"
        elif average >= 40:
            grade = "Pass\n"
        else:
            grade = "Fail"
        print(student["id"], "|", name,
              "| Marks:", marks,
              "\nTotal:", total,
              "| Average:", format(average, ".2f"),
              "| Grade:", grade)
        
    high = high_performers(students)
    names = list(map(lambda s: s["name"], high))
    print("\nHigh performers (average >= 75):", names)
    total_marks = class_total(*totals)
    class_average = total_marks / (len(students) * len(subjects))
    print("Class average:", format(class_average, ".2f"))

students = []
students.append(add_student("S101", "Aman", [78, 65, 88]))
students.append(add_student("S102", "Riya", [35, 72, 61]))
info = student_details(course="Python", module=4)
display_report(students)
print("Recursive sum from 1 to 5:", recursive_sum(5))
