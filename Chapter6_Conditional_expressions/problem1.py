a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))
c = int(input("Enter the Third number :"))
d = int(input("Enter the forth number :"))

if(a>b and a>c and a>d):
    print(f"{a} is greatest number")
    
elif(b>a and b>c and b>d):
    print(f"{b} is greatest")
    
elif(c>a and c>b and c>d):
    print(f"{c} is the greatest")
    
else:
    print(f"{d} is the greatest")
    
    