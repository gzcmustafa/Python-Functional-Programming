
t=list(range(1,5))

u=[[i,i**2] for i in t]
print(u)

a=list(range(1,5))
b=[{str(i):i} for i in a]
print(b)

x=["a",1,2,3,"b","c",4,5,6,7,8,9,11]
y=[i for i in x if str(i).isdigit()]
print(y)



