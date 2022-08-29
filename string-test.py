def string_test(metin):
    d={"buyukharf":0,"kucukharf":0} 
    for karakter in  metin:
        if karakter.isupper():
            d["buyukharf"]+=1
        elif karakter.islower():
            d["kucukharf"]+=1
        else:
            pass
    print("BÜYÜK HARF SAYISI :",d["buyukharf"])
    print("KÜÇÜK HARF SAYISI :",d["kucukharf"])

string_test("PyThOn PrOGRaMlA ile FoNkSiYoNeL pRoGraMlAma")
       