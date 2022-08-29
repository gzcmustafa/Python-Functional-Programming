import random

print()
print("**********************************")
print()
#Listeleri birleştirme
a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)
print()
print("**********************************")
print()
# Çok boyutlu Listeler
x=[
   [1,0,0],
   [0,1,0],
   [0,0,1]   
  ]
print(x)
print(len(x)) # satır sayısını verir
print(len(x[0])) #ilk satırdaki sütun sayısını verir
print()
print("**********************************")
print()
#örnek
x=[]
for i in range(5):
    x.append([random.randint(1,5) for c in range(4)])
print(x)
print()
print("**********************************")
print()
x=[1,2,3,4,5]
print(x[0:4:2])
print(x[-1:-5:-2])
print(x[0:3])
x[0:3]=[3,5,8]
print(x)
print(sum(x))
x.sort()
print(x)
x.reverse()
print(x)
