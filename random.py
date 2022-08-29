import random
print(random.random()) #rastgele bir sayı üretir. 0-1 aralığında

# sadece random komutunu kullanarak tam sayı sonuç üretme
a=5
b=10
x= a + (int)((b-a)*random.random())
print(x)

#yukarıdaki kodun daha kısa yönetmi vardır.
#random.randint(a,b) ile bunu daha kısa yoldan yapabiliriz.(b dahil değil)
print(random.randint(5,10))