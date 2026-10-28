students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")

    marks = list(map(int, input("Enter marks of 3 subjects: ").split()))

    total = sum(marks)
    percentage = total / 3

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "Fail"

    students[name] = {
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }

print("\n----- Student Report -----")

for name, details in students.items():
    print(f"\nName: {name}")
    print(f"Marks: {details['marks']}")
    print(f"Total: {details['total']}")
    print(f"Percentage: {details['percentage']:.2f}%")
    print(f"Grade: {details['grade']}")