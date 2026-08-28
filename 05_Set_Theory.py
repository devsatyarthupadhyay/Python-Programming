s1 = {1,2,3,4,5,6,7}
s2 = {4,5,6,3,8,9,0}
s3 = {1,2,3,31}

union = s1.union(s2)
print(union)

intersection = s1.intersection(s2)
print(intersection)

print(s1-s2)

union2 = s1.union(s2).union(s3)
print(union2)

subset = s3.issubset(s1)
print(subset)