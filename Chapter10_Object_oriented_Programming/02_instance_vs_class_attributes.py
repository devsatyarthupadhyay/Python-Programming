class Employee:
    language = "Pyhton"
    salary = 120000
    
satyarth = Employee()
satyarth.language = "java"        # Here Instance attribute take preference over class attribute 
print(satyarth.language , satyarth.salary)  

shriyansh = Employee()
print(shriyansh.language , shriyansh.salary)
