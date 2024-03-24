#Kullanıcıdan alınan sayılar arasındaki sayıları yazdırmak
s1=int(input("Başlangıç değerini giriniz\t:"))
s2=int(input("Bitiş değerini giriniz\t\t:"))
if s1>s2:
    s1,s2=s2,s1
print(f"Başlangıç değeri {s1} ve bitiş değeri {s2}.")
print("FOR ile yazdırılıyor...")
for i1 in range(s1,s2+1,1):
    print(i1)

i1=s1
print(f"i1 değeri : {i1}")

print("WHILE ile yazdırılıyor...")
while i1<=s2:
    print(i1)
    i1+=1 #i1=i1+1