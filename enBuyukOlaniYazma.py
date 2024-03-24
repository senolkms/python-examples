#Girilen 3 sayıdan büyük olanı ekrana yazdırmak
s1=int(input("1. Sayıyı Giriniz: "))
s2=int(input("2. Sayıyı Giriniz: "))
s3=int(input("3. Sayıyı Giriniz: "))
if s1>s2 and s1>s3:
    print(s1,"sayısı en büyüktür.")
elif s2>s3:
    print(s2, "sayısı en büyüktür.")
else:
    print(s3, "sayısı en büyüktür.")