import random


def game():
    with open(r"C:\Users\Satyarth Upadhyay\Desktop\Python Programming\Chapter9_File_Input_Output\hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    
    print("you are playing the game ")
    score = random.randint(1,100)
    print(f"Your score is {score}")
    
    if(score>hiscore):
        with open(r"C:\Users\Satyarth Upadhyay\Desktop\Python Programming\Chapter9_File_Input_Output\hiscore.txt","w") as f:
            f.write(str(score))
            
    return score 

game()      