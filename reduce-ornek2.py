from functools import reduce
f=lambda a1,a2:a1*a2
s=reduce(f,range(1,5))
print(s)