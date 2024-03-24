#Kullanıcıdan alınan 5 sayıdan pozitif olanların toplamını, negatif olanların  sayısını yazdırmak
tp=0
adt=0
i1=1
while i1<=5:
    s1=int(input(f"{i1}. Sayıyı Giriniz :"))
    if s1>=0:
        tp+=s1
    else:
        adt+=1
    i1+=1
print(f"Girilen 5 sayıdan pozitiflerin toplamı {tp} ve negatiflerin sayısı {adt}'tir.")