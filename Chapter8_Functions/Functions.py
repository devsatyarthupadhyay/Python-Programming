print("Find average of any three number")

def avg():
    a = int(input("Enter your first number :"))
    b = int(input("Enter your Second number :"))
    c = int(input("Enter your third number :"))
    average = (a+b+c)/3
    print(f"Average of {a} , {b} , {c} is {average}")
    
avg()