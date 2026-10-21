word = "Donkey"

with open(r"C:\Users\Satyarth Upadhyay\Desktop\Python Programming\Chapter9_File_Input_Output\wordsremoval.txt" , "r") as f:
    content = f.read()
    newcontent = content.replace(word , "######")

with open(r"C:\Users\Satyarth Upadhyay\Desktop\Python Programming\Chapter9_File_Input_Output\wordsremoval.txt" , "w") as g:
    g.write("File without any change:\n")
    g.write(content + "\n")
    g.write("File After changing:\n")
    g.write(newcontent + "\n")