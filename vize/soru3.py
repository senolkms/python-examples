lst=list()
print("Listeye eklenen sayılar...")
for i1 in range(0,5):
    sayi=int(input("Sayı giriniz..:"))
    lst.append([sayi])
    print(lst)

print("Liste elemanlarının alt alta yazılımı...")
for i1 in lst:
    for i2 in i1:
        print(i2)

print("Liste elemanlarının tersi ve alt alta yazılımı...")
lst.reverse()
for i1 in lst:
    for i2 in i1:
        print(i2)

print("Liste elemanlarının çift olanlarının ortalaması") #Hatayı çözemedim ve yukarıda gösteriyor?
cift=0
adet=len(lst)
for i1 in lst:
    if i1%2==0:
        cift+=i1
print(cift/adet)