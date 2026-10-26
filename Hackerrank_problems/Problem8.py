students = []
for _ in range(int(input())):
       name = input()
       grade = float(input())
       students.append([name , grade])
       
second_lowest = sorted(set([item[1] for item in students]))[1]

for name,grade in sorted(students):
    if grade == second_lowest:
        print(name)
    