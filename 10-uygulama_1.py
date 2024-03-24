#araSınav
def sGiris():
    global s1,s2
    s1=int(input("1. Sayıyı Giriniz :"))
    s2=int(input("2. Sayıyı Giriniz :"))

def sYaz(x,y):
    print(f"Girilen 1. Sayı ={x}")
    print(f"Girilen 2. Sayı ={y}")

def sTopla():
    global s1,s2
    return s1+s2

sGiris()
sYaz(s1,s2)
print(f"Sayıların Toplamı ={sTopla()}")