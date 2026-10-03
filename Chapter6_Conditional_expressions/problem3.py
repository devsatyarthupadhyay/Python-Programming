p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click here"

comment = input("enter your comment :")

if(p1 in comment or p2 in comment or p3 in comment or p4 in comment):
    print("This comment is a spam")
else:
    print("This message is not a spam")