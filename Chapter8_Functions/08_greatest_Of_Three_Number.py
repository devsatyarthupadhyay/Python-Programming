def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
a = int(input("Enter your First Numnber :"))
b = int(input("Enter your Second Number :"))
c = int(input("Enter your Third Number :"))

print(f"Greatest number amongst {a} , {b} and {c} is {greatest(a,b,c)}")