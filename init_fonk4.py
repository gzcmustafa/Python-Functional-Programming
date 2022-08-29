class Dikdörtgen():
    def __init__(self,uzunluk,yukseklik):
        self.uzunluk=uzunluk
        self.yukseklik=yukseklik
    
    def dikdortgen_alan(self):
        print("alan = ",self.uzunluk*self.yukseklik)

yenidikdortgen=Dikdörtgen(12,10)
yenidikdortgen.dikdortgen_alan()