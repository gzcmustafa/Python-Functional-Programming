class Dusman:

  def __init__(self,isim="Default",kalan_can=200,saldiri_gucu=200,mermi_sayisi=200):
    self.isim=isim
    self.kalan_can=kalan_can
    self.saldiri_gucu=saldiri_gucu
    self.mermi_sayisi=mermi_sayisi

  def print(self):
    print(" Saldırı Başlıyor.......")
    print("İsim: ",self.isim,"Kalan Can: ",self.kalan_can,"Saldırı Gücü: ",self.saldiri_gucu,"Mermi Sayısı: ",self.mermi_sayisi)

dusman1=Dusman("def",90,30,20)
dusman2=Dusman("abc",99,35,20)
dusman3=Dusman()

dusman1.print()
print("**********")
dusman2.print()
print("**********")
dusman3.print()




