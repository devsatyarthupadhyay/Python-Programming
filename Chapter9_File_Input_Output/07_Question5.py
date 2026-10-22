Words = ["Donkey","bad","ugly"]

with open(r"C:\Users\Satyarth Upadhyay\Desktop\Python Programming\Chapter9_File_Input_Output\Multiplewordsremoval.txt" , "r") as f :
    content = f.read()
    newcontent = content
    
for word in Words :
    newcontent = newcontent.replace(word , "#"* len(word))
    
with open(r"C:\Users\Satyarth Upadhyay\Desktop\Python Programming\Chapter9_File_Input_Output\Multiplewordsremoval.txt" , "w") as f :
    f.write("Before changing file is :\n")
    f.write(content + "\n")
    f.write("After changing the file :\n")
    f.write(newcontent + "\n")
    