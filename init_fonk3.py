class Ayakkabı:
    def __init__(self,boyut,indirim,malzeme,fiyat):
         self.boyut=boyut
         self.indirim=indirim
         self.malzeme=malzeme
         self.fiyat=fiyat
    
class Sandalet(Ayakkabı):
    def __init__(self, boyut, indirim, malzeme, fiyat,sugecirmez):
         self.boyut=boyut
         self.indirim=indirim
         self.malzeme=malzeme
         self.fiyat=fiyat
         self.sugecirmez=sugecirmez
    def printBilgi(self):
        print("sandalet no:",self.boyut,"malzeme: ",self.malzeme,"fiyat: ",self.fiyat,"sugeccirmez: ",self.sugecirmez)

sandalet1=Sandalet(36,False,"deri",81,True)

sandalet1.printBilgi()