class kare():
    def __init__(self,k=1):
        print("Kare Nesnesi oluşturuldu!")
        self.k=k
    def yaz(self):
        print(f"Kare kenarları : {self.k}")
    def alan(self):
        print(f"Karenin alanı = {self.k*self.k}'dir.")
class dikdortgen():
    def __init__(self,k1=1,k2=2):
        print("Dikdörtgen Nesnesi oluşturuldu!")
        self.k1=k1
        self.k2=k2
    def yaz(self):
        print(f"Dikdörtgen kenarları : {self.k1} ve {self.k2}")
    def alan(self):
        print(f"Dikdörtgen alanı = {self.k1*self.k2}'dir.")

k1=kare()
k1.yaz()
k1.alan()
d1=dikdortgen()
d1.yaz()
d1.alan()
d1=dikdortgen(5,6)
d1.yaz()
d1.alan()
d1=dikdortgen(10)
d1.yaz()
d1.alan()