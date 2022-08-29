#TÜM ÖRNEKLER
""" 
import random
print(random.randint(5,10))
"""

#string manipülasyonu
"""
x=" Python programlama, dili "
print(x.strip(' '))
print(x.replace(',',':'))
print(x.upper())
print(x.lower())
a=x.split(' ')
print(a)
print(':'.join(a))
"""

#döngülerde indislere erişmek
"""
x=[1,2,3,4,5]
for i in enumerate(x):
    print(i)
""" 

#çok boyutlu liste oluşturmak
"""
import random
x=[]
for i in range(5):
    x.append([random.randint(1,5) for c in range(4)])
print(x)
"""

#sözlükler
"""
from operator import le
x={"user":"ali","sifre":"123","login_count":"5"}
print(x["user"])
x["user"]="Mustafa"
print(x["user"])
x["tckimlik"]="1234566"
print(x["tckimlik"])
x.pop("tckimlik")
print(len(x))
"""

#sözlüklerde döngü yapıları
"""
y={"user":"ali","sifre":"123","login_count":"5"}
for k,v in y.items():
    print(k,":",v)

for k in y.keys():
    print(k)

for v in y.values():
    print(v)
""" 

#liste üreticiler
""" 
x=list(range(1,5))
y=[i for i in x]
print(y)
p=[i**2 for i in y]
print(p)
z=[[i,i**2] for i in x]
print(z)
""" 

#Sözlük üreticiler
""" 
x=list(range(1,5))
z=[{str(i):i} for i in x]
print(z)
""" 

#Üreticilere şart eklemek
""" 
x=["a",1,2,3,"b","c",4,5,6]
y1=[i for i in x ]
print(y1)
y2=[i for i in x if str(i).isdigit()]
print(y2)
""" 

#iç içe for döngüsü
"""
x=[1,2,3]
y=["a","b","c"]
z=[[i,k] for i in x for k in y]
print(z)
"""

#kullanıcı adlarında istemediğimiz karakter olan kullanıcılar listesi
"""
sifreler=["ali123.","veli123","kelam","kalem","gel.123"]
x=[i for i in sifreler if "." in i ]
print(x)
"""

#liste üreticileri kesişim,fark yol1
"""
x=["python","C#","java","go"]
y=["scala","python","matlab","java"]

kesisim=[i for i in x  if( i in x and  i in y) ]
fark=[i for i in x if (i in x and i not in y)]
print(fark)
print(kesisim)
"""

#ZİP KULLANIMI
"""
x=[1,2,3]
y=["a","b","c"]

z=list(zip(x,y)) # karşılıklı kodlar
print(z)
zip komutununçıktısı bir demettir
"""
 
# ITERATORLER
"""
x=[1,2,3]
y=iter(x)
print(next(y))
print(next(y))
print(next(y))
print(next(y))
"""

# ITERATOR-2
"""
a="Merhaba python"
b=iter(a)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
"""

# ITER SINIF YAZMAK
"""
class Ciftler:
    def __iter__(self):
        self.a=2
        return self
    
    def __next__(self):
        x=self.a
        self.a+=2
        return x

sinif=Ciftler()
x=iter(sinif)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
"""

# SONLU ITER SINIF YAZMAK
"""
class Ciftler:
    def __iter__(self):
        self.a=2
        return self
    
    def __next__(self):
        if self.a <10:
          x = self.a
          self.a+=2
          return x
        else:
         raise StopIteration
         

sinif=Ciftler()
x=iter(sinif)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
"""


#genarators
"""
def test (a):
    a+= 1
    yield a

    a+=1
    yield a


x=test(5)

print(next(x))
print(next(x))
"""


#genarator ve liste üreticisi karşılaştırma
"""
x=[i**2 for i in [1,2,3]]
print(type(x))
y=(i**2 for i in [1,2,3])
print(type(y))
"""

#genarator örnek 
"""
def kareAl(liste):
    for i in liste:
        yield i*i

x=[1,2,3,4,5]
y=kareAl(x)

print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
"""


 #fibonacci sayısı iteratör ile 
""" 
class Fibo:
    def __iter__(self):
        self.f1=0
        self.f2=1
        return self 
    
    def __next__(self):
        self.f1,self.f2= self.f2,self.f1 + self.f2
        return self.f2

fibos=Fibo()
x=iter(fibos)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
"""

#Fibonacci sayılarını yield kullanarak oluşturma
"""
from re import X
def fibGen(n):
    f1,f2=0,1
    i=0
    while i<n:
        f1,f2=f2,f1+f2
        yield f2
        i+=1
    else:
     raise StopIteration

x=fibGen(10)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
"""

#Liste üreticisi ile Fibonacci
"""
x=[0,1]
[x.append(x[i-1]+x[i]) for i in range(1,10)]
print(x)
"""

#Lambda Kullanımı
"""
carpma=lambda a,b:a*b
print(carpma(5,6))
"""

#Map Kullanımı
"""
def myfunc(a):
    return len(a)

x = map(myfunc,('python','programlama','dili'))
print(list(x))
"""

#Map Kullanımı-2
"""
def f(a):
    return a*a

x=map(f,[1,2,3,4])
print(list(x))
"""

#Map Kullanımı-3
"""
f = lambda a:a*a
x=map(f,[1,2,3,4])
print(list(x))
"""

#Map Kullanımı-3
"""
x=map(lambda a:a*a,[1,2,3,4,5,6])
print(list(x))
"""

#Map Kullanımı-4
"""
f=lambda a,b:a+" "+b
x=map(f,["python","dili","fonksiyonel"],["programlama","ile","programlama"])
print(list(x))
print(" ".join(x))
"""

#Filter Kullanımı
"""
x=list(range(10))
f=lambda a: a%2==0
s=filter(f,x)
print(list(s))
"""

#Farklı bir filter kullanımı
"""
isim=["Mustafa","Elif","Osman"]
tarih=[2012,2022,2032]
x=zip(isim,tarih)
print(list(x))
y=list(filter(lambda a:2012<=a[1]<=2022,zip(isim,tarih)))
print(list(y))
"""

#Reduce Kullanımı
"""
f=lambda a1,a2: a1+a2
s=reduce(f,[1,2,3,4])
print(s)
"""

#Reduce ile faktoriyel hesaplama
"""
f=lambda a1,a2:a1*a2
s=reduce(f,range(1,6))
print(s)
"""

#Zip Kullanımı farklı bir örnek
"""
ages=[17,21,21,23,35]
names=["ali","mustafa","elif","selen","kerem"]

x=zip(names,ages)
print(list(x))

y=dict(zip(names,ages))
print(y)
"""

#Rekürsif ve özyineleme aynı şeyi ifade eder.(Kendi kendini çağıran fonksiyonlardır.)

#Fibonacci reküsif örneği
"""
def fibo(n):
    if n<=1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
print(fibo(5))
"""

# Fonksiyonu bir değişkene atamak.
"""
def shout (text):
    return text.upper()

buyut=shout
print(buyut("hello"))
"""

#Bir fonksiyonu başka bir fonksiyona parametre olarak geçirmek
"""
def buyut(text):
    return text.upper()

def kucult(text):
    return text.lower()

def test(func,str=""):
    sonuc=func(str)
    print(sonuc)

test(buyut,"python programmlama dili")
test(kucult,"PYTHON PROGRAMlamA Dili")
"""

#Fonksiyon döndüren Fonksiyonlar
"""
def toplayici(x):
    def topla(y):
        return x+y 
    
    return topla

ekle=toplayici(15)
print(ekle(10))
"""

#iç içe fonksiyon güzel bir örnek
"""
def mapPrefixes(string):
    def prefix(i):
        return string[:i]
    return map(prefix,range(1,len(string)+1))

print(list(mapPrefixes("python programlama")))
"""

#fonksiyon içinde map kullanımı
"""
def mapScale(factor,nums):
    return map (lambda n:factor*n, nums)

print(list(mapScale(3,[8,3,6,7,2,4])))
"""

#Fonksiyon içinde lambda kullanımı
"""
def mapPrefixes(string):
    return map(lambda i: string[:i+1], range(len(string)))
print(list(mapPrefixes('cat')))
"""

#fonk içinde map kullanımı-2
"""
def fonkekleme(ek,kelimeler):
    def birlestir(i):
        return ek+kelimeler[i]
    return map(birlestir,range(len(kelimeler)))

print(list(fonkekleme('com',["puter","pile","mute"])))
"""

# All- Any kullanımı
"""
print(all(map(lambda x: x>0,[1,2,3,4])))
print(all(map(lambda x:x>0, [-1,2,3,4])))
print(any(map(lambda x:x>0,[-1,2,3,4])))
print(any(map(lambda x:x>0,[-1,-2,-3,-4])))
"""
