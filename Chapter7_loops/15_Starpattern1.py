line = int(input("Enter the number of lines :"))

for i in range (1,line+1):
    print(" "*(line-i),end="")
    print("*" * (2*i-1),end="")
    print("\n")