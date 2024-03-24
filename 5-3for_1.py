#Kullanıcıdan alınan 5 sayıdan pozitif olanların toplamını, negatif olanların  sayısını yazdırmak
tp=0
adt=0
for i1 in range(1,6):
    s1=int(input(f"{i1}. Sayıyı Giriniz :"))
    if s1>=0:
        tp+=s1
    else:
        adt+=1
print(f"Girilen 5 sayıdan pozitiflerin toplamı {tp} ve negatiflerin sayısı {adt}'tir.")