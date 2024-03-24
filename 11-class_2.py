class insan():
    ad=""
    soyad=""
    dYili=0
    def ekranaYaz(self):
        print(f"1-Adınız :{self.ad}\nSoyadınız :{self.soyad}\nDoğum Yılınız :{self.dYili}\nYaşınız :{2021 - self.dYili}")

class bitki():
    ad=""
    renk=""
    yenirMi=False

i1=insan()
i1.ad="mehmet"
i1.soyad="karaca"
i1.dYili=1980
i1.ekranaYaz()
print(f"2-Adınız :{i1.ad}\nSoyadınız :{i1.soyad}\nDoğum Yılınız :{i1.dYili}\nYaşınız :{2021-i1.dYili}")
b1=bitki()
b1.ad="gül"
b1.renk="kırmızı"
b2=bitki()
b2.ad="domates"
b2.renk="kırmızı"
b2.yenirMi=True
print(f"Ad :{b1.ad}\nRenk :{b1.renk}\nYenir mi? :{b1.yenirMi}")
print(f"Ad :{b2.ad}\nRenk :{b2.renk}\nYenir mi? :{b2.yenirMi}")