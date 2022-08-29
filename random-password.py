import random
import string

letters_lowercase = string.ascii_lowercase
letters_uppercase = string.ascii_uppercase
numbers = string.digits


def kontrol(sifre):
    buyuk_harf_kontrol=False
    kucuk_harf_kontrol=False
    for i in sifre:
        if letters_lowercase.find(i)>-1:
            buyuk_harf_kontrol=True
        if letters_uppercase.find(i)>-1:
            kucuk_harf_kontrol=True
    
    if buyuk_harf_kontrol==True and kucuk_harf_kontrol==True:
        print("ŞARTLARA UYGUN ŞİFRE OLUŞTURULDU")
    else:
        print("ŞARTLARA UYGUN ŞİFRE OLUŞTURULAMADI! :(")
            



# şifre üretme fonkisyonumuz
def sifre_uret(uzunluk):
    karakterler=letters_lowercase+letters_uppercase+numbers
    sifre=''.join(random.choice(karakterler) for i in range(uzunluk)) 
    kontrol(sifre)
    return sifre

print(sifre_uret(8))






 
