line = int(input("Enter the number of input :"))

for i in range(1,line+1):
    if(i==1 or i==line):
        print("*"*line)
    else:
        print("*",end="")
        print(" "*(line-2),end="")
        print("*",end="")
        print("")