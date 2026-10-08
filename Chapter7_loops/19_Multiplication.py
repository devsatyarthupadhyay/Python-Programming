num = int(input("Enter your number:"))
num2 = int(input("Enter the number upto you want your multiplication table:"))
for i in range(1,num2+1):
    print(f"{num}X{i}={num*i}")