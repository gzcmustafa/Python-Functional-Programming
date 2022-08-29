x=[0,1]
y=[x.append(x[i-1]+x[i]) for i in range(1,10)]
print(list(x))