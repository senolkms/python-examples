class insan():
    ad=""
    soyad=""
    dYili=0
    def yaz(self):
        ad="ahmet"
        soyad="ali"
        print(f"Adınız :{self.ad}\nSoyadınız :{self.soyad}\nDoğum Yılınız :{self.dYili}\nYaşınız :{2021 - self.dYili}")

i1=insan()
i1.ad="mehmet"
i1.soyad="karaca"
i1.dYili=1980
i1.yaz()