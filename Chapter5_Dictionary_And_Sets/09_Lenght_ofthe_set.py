s = set()
s.add(20)
s.add(20.0)     
s.add("20")

print(len(s))   # python compares floating point number and integer number even after decimal , 20 = 20.0