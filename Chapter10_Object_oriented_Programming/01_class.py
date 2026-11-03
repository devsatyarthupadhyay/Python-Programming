class Employee :
    language = "py"     # This is class attribute 
    salary = 1500000    # This is class attribute 
    
satyarth = Employee()
satyarth.name = "Satyarth"   # This is object attribute 
print(satyarth.name , satyarth.language , satyarth.salary)

shriyansh = Employee()
shriyansh.name = "Shriyansh"
print(shriyansh.name , shriyansh.salary,shriyansh.language)

# Here name is object attribute and language & salary is class attribute 