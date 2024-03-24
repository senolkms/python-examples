class dikdortgen():
    def __init__(self,k1=1,k2=2):
        print("Dikdörtgen Nesnesi oluşturuldu!")
        self.k1=k1
        self.k2=k2
    def yaz(self):
        print(f"Dikdörtgen kenarları : {self.k1} ve {self.k2}")

d1=dikdortgen(5,6)
d1.yaz()
d1.k1=10
d1.k2=20
d1.yaz()