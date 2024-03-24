def sGiris ():
    global s1, s2
    s1=int(input("1. sayıyı giriniz : "))
    s2=int(input("2. sayıyı giriniz : "))
def sYaz (s1,s2):
    print(f"Girilen 1. sayı: {s1}")
    print(f"Girilen 2. sayı: {s2}")
def sTopla():
    return s1+s2
sGiris()
sYaz(s1,s2)
print("Girilen sayıların toplamı : ",sTopla())

