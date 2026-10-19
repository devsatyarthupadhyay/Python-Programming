f = open("poem.txt")
content = f.read()
if ("twinkle" in content):
    print("The word twinkle present in the file poem.txt")
else:
    print("the word twinkle isn't present in the file poem.txt")
    
f.close()