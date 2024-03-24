class personel():
    def __init__(self,ad="",soyad=""):
        print("Taban sınıf oluşturuldu!")
        self.ad=ad
        self.soyad=soyad
class bilgiIslem(personel):
    def __init__(self,maas=300):
        print("Alt bilgi işlem sınıfı oluşturuldu!")
        self.ucret=maas
p1=personel()
p1.ad="pAd1"
p1.soyad="pSoyad1"
print(f"Ad: {p1.ad}\nSoyad :{p1.soyad}")
'print(f"Ad: {p1.ad}\nSoyad :{p1.soyad}\nÜcret : {p1.ucret}")'
'p1.ucret hatalıdır. taban sınıf alt sınıfın özellik ve metotlarını kullanamaz'
b1 = bilgiIslem(800)
b1.ad="bAd1"
b1.soyad="bSoyad1"
print(f"Ad: {b1.ad}\nSoyad :{b1.soyad}\nÜcret : {b1.ucret}")
b2 = bilgiIslem()
b2.ad="bAd2"
b2.soyad="bSoyad2"
print(f"Ad: {b2.ad}\nSoyad :{b2.soyad}\nÜcret : {b2.ucret}")
b2.ucret=600
print(f"Ad: {b2.ad}\nSoyad :{b2.soyad}\nÜcret : {b2.ucret}")