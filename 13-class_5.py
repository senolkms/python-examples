class nokta():
    def __init__(self):
        print("Nokta nesnesi oluşturuldu!")
    def degerYaz(self):
        print(f"Noktanın x ve y değerleri {self.x} ve {self.y}'dir.")
n1=nokta()
n1.x=10
n1.y=30
n1.degerYaz()
