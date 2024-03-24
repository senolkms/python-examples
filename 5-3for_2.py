#Kullanıcıdan gireceği sayılar arasındaki sayıların ortalamasını yazdırmak
s1=int(input("Başlangıç değerini giriniz\t:"))
s2=int(input("Bitiş değerini giriniz\t\t:"))
tp=0
if s1>s2:
    s1,s2=s2,s1
for i1 in range(s1,s2+1):
    tp+=i1
print("Sayıların ortalaması",tp/(s2-s1+1))