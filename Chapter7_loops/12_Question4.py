number = int(input("Enter your number : "))

for i in range (2,number):
    if(number%i==0):
        print("This Number is not prime")
        break
    else:
        print("This number is prime")
        break