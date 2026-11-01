# Student Records and Marks Analyzer
subjects = ("Python", "Maths", "DBMS")
students = []
unique_subjects = set(subjects)

n = int(input("How many students? "))
for i in range(n):
    student_id = input("\nStudent ID: ")
    name = input("Name: ")
    marks = {}

    for subject in subjects:
        marks[subject] = int(input(subject + " marks: "))
    student = {
        "name": name,
        "marks": marks
    }
    students.append({student_id: student})

print("\n----- STUDENT REPORT -----")
for record in students:
    for student_id, details in record.items():
        name = details["name"]
        marks = details["marks"]
        total = sum(marks.values())
        average = total / len(subjects)

        if average >= 75:
            result = "Distinction\n"
        elif average >= 40:
            result = "Pass\n"
        else:
            result = "Fail\n"

        print(student_id, "|", name, end=" \n")
        for subject, mark in marks.items():
            print(subject + ":", mark, end=", ")

        print("\nTotal:", total,
              "| Average:", format(average, ".2f"),
              "| Result:", result)
        
print("\nUnique subjects:", unique_subjects)
print("Students recorded:", len(students))



