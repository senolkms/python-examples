'classlarda listeler'
class personel():
    bilgi=""
    def __init__(self):
        id=input("Id Bilgisi Giriniz: ")
        ad=input("Adınızı Giriniz: ")
        sad=input("Soyadınızı Giriniz: ")
        dYil=int(input("Doğum Yılı Giriniz: "))
        self.bilgi=[id, ad, sad, dYil]
p1=personel()