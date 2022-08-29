from operator import truediv


class Ayakkabı:
    def __init__(self,boyut,indirim,malzeme,fiyat):
         self.boyut=boyut
         self.indirim=indirim
         self.malzeme=malzeme
         self.fiyat=fiyat
    
    def printBilgi(self):
        print("ayakkabı bedeni= ",self.boyut,"yapımında kullanılan malzeme= ",self.malzeme,"fiyatı= ",self.fiyat)
    
    def indirim(self):
        self.indirim=true

ayakkabı1=Ayakkabı(37,"false","deri",500)
ayakkabı2=Ayakkabı(45,"false","spor",800)

print("*****")
ayakkabı1.printBilgi()
ayakkabı2.printBilgi()
