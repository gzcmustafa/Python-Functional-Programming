# map ile lambdayı birlikte kullanabiliriz
f=lambda a:a*a

x=map(f,[1,2,3,4,5,6])
print(list(x))

#bir farklı kullanımda ise x=map() içinde direk lambdayı da yazarız. 

x=map(lambda a:a*a,[1,2,3,4])
print(list(x))