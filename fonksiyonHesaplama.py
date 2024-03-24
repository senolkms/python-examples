#Bir fonksiyonu giriş değerine göre hesaplamak ve sonucu yazdırmak
#f(x)={Sayı -10'dan küçükse x^3+2x, -10 ile +20 arasındaysa x^2, +20'den büyükse 3x}
s1=int(input("Bir sayı giriniz: "))
if s1<-10:
    print("f(", s1, ")= ", s1**3+2*s1,sep="")
elif s1>=-10 and s1<=20:
    print("f(", s1, ")= ", s1**2,sep="")
else:
    print("f(", s1, ")= ", 3*s1,sep="")