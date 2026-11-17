numbers = [10, 20, 10, 30, 20, 40, 50]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Original List:", numbers)
print("After Removing Duplicates:", unique)
