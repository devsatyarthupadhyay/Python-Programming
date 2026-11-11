# Program 1: Find smallest number

numbers = [25, 10, 45, 5, 30, 15]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest number is:", smallest)


# Program 2: Count vowels

word = input("Enter a word: ")

count = 0

for letter in word:
    if letter in "aeiouAEIOU":
        count = count + 1

print("Total vowels:", count)