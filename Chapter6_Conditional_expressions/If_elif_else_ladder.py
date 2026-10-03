age = int(input("Enter your age :"))

# if-elif-else ladder

if(age>=18):
    print("You are above the age of consent ")
    
elif(age==0):
    print("Age cannot be equal to zero ")
    
elif(age<0):
    print("Please enter valid age , age cannot be in negative ")
    
else:
    print("you are below the age of consent")