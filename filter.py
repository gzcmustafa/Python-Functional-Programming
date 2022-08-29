x=list(range(10))

f=lambda a: a%2==0
s=filter(f,x)
print(list(s))