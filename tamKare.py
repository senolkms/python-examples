#Girilen bir sayının tam kare olup olmadığını ekrana yazdırmak
#4, 9, 16, 25 tam karedir (bir sayını karesi olmak)
#100: 10*10, 81: 9*9, 50:XXX, 99: XXX
#Bir sayının tam kareliği nasıl anlaşılır?
import math
s1=int(input("Bir sayı giriniz: "))
kk=math.sqrt(s1)
print("Sayı\t:",s1,"\nKarekökü:",kk)
if kk==(kk//1):
    print(s1,"sayısı tam karedir.")
else:
    print(s1, "sayısı tam kare değildir.")