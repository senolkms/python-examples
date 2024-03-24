'classlarda private/public özellik/metotlar'
class personel():
    __id=0
    ad=""
    sad=""
    dYil=0
    def __init__(self):
        self.__id=input("Id Bilgisi Giriniz: ")
        self.ad=input("Adınızı Giriniz: ")
        self.sad=input("Soyadınızı Giriniz: ")
        self.dYil=int(input("Doğum Yılı Giriniz: "))
    def yaz1(self):
        print(f"1-Id: {self.__id}\nAd: {self.ad}\nSoyadınız: {self.sad}\nDoğum Yılınız ({2021-self.dYil}): {self.dYil}")
        self.__yaz2()
    def __yaz2(self):
        print(f"2-Id: {self.__id}\nAd: {self.ad}\nSoyadınız: {self.sad}\nDoğum Yılınız ({2021-self.dYil}): {self.dYil}")
p1=personel()
p1.yaz1()