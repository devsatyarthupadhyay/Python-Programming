math = int(input("Enter marks in maths:"))
science = int(input("Enter marks in science:"))
english = int(input("Enter marks in english:"))

percentage = (math+science+english)/3

if(percentage>=40):
    if(math>=33 and science>=33 and english>=33):
        print("pass")
    else:
        print("Student's percentage is less than 33% in individual subject , Fail")
else:
    print("Student's total percentage is less than 40% , FAIL")