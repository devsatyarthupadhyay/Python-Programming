class Employee:
    language = "Python"
    salary = 1200000
    
    @staticmethod
    def getinfo():
        print("Good Morning")

satyarth = Employee()
satyarth.language = "java"
satyarth.getinfo()
print(satyarth.language , satyarth.salary)