asal=True
x=17

for i in range(3,x):
    if x%i==0:
        asal=False
        break

print(x,"Asaldir") if asal else print(x,"asal değildir")