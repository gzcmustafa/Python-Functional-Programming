x=()
print(type(x))

x=("veli","ali",1)
print(x)
print(x[0])
#x[0]="aslı" # hata verir demetler sonradan güncellenemezler

#demetlerde çoklu atama
gizliler=("ali","123")
user,sifre=gizliler
print(user,sifre)

#temp değişkeni kullanarak değişkenlerin yerini değiştirme
x=15
y=14
print(x,y)
temp=x
x=y
y=temp
print(x,y)
#temp değişkeni kullanmadan değişkenlerin yerini değiştirme
x=23
y=11
print(x,y)
x,y=y,x
print(x,y)