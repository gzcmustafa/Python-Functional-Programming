from functools import reduce
f=lambda a1,a2: a1+a2

s=reduce(f,[1,2,3,4])
print(s)