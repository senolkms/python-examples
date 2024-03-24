class kare():
    def __init__(self,x=0):
        print("Kare nesnesi oluşturuldu!")
        self.x=x
        print("Kare kenarı :",self.x)
class dikdortgen():
    def __init__(self,x=0,y=0):
        print("Dikdörtgen nesnesi oluşturuldu!")
        self.x=x
        self.y=y
        print("Dikdörtgenler kenarları :",self.x,self.y)
k1=kare()
d1=dikdortgen()
k2=kare(5)
d2=dikdortgen(2,10)
d3=dikdortgen(15)