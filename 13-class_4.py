import math
class nokta():
    def degerAl(self):
        self.x=int(input("Noktanın x değerini giriniz : "))
        self.y=int(input("Noktanın y değerini giriniz : "))
    def degerYaz(self):
        print(f"Noktanın x ve y değerleri {self.x} ve {self.y}'dir.")
n1=nokta()
n1.degerAl()
n1.degerYaz()
n2=nokta()
n2.degerAl()
n2.degerYaz()
print(f"({n1.x},{n1.y}) ile ({n2.x},{n2.y}) noktaları arasındaki uzaklık {math.sqrt((n1.x-n2.x)**2+(n1.y-n2.y)**2)}'dir.")