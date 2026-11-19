num = int(input("Enter a number: "))

original = num
total = 0
power = len(str(num))

while num > 0:
    digit = num % 10
    total = total + digit ** power
    num = num // 10

if original == total:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")