class Employee :
    language = "Python"
    salary = 1200000
    
    def getinfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")
        
satyarth = Employee()
satyarth.language = "java"
satyarth.getinfo()     # This line will be readed as Employee.getinfo(satyarth)