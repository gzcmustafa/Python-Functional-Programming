x=" Python programlama, dili "

print(x[2:10]) #2.indisden 10.indise kadar git yazdır 10 dahil değil (range komutund olduğu gibi sondaki sayı dahil değil)

print(x[2:]) #2.indisden başla sonuna kadar 

print(x[:10]) #baştan başla 10.indise kadar

print(x[0::2]) #0'dan yani baştan başla sona kadar ikişer adımla

print(x[::-1]) #sondan başa -1 adım. yani ters çevirerek yaz.

print(x)
print(x.strip(' '))
print("*******************")
print(x)
print(x.replace(',',' '))
print("*******************")
print(x)
print(x.upper())
print("*******************")
print(x)
print(x.lower())
print("*******************")
a=x.split(' ')
print(a)
print("*******************")
print(':'.join(a))