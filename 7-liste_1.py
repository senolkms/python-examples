#20 sayıya -50 ile +50 arasında rastgele değer atayan, bu işlemden sonra ekrana sayıları sırayla yazdıran, bu işlemden
# sonra da sayıları tersten çıktı olarak veren kodu yazınız.
import random
lst=list()
for i1 in range(0,20):
    lst.append(int(random.randint(-50,51)))
print("Liste Yazdırılıyor...")
for i1 in range(0,20):
    print(f"{i1+1}.Sayı = {lst[i1]}")
print("\nListe Tersten Yazdırılıyor...")
for i1 in range(19,-1,-1):
    print(f"{i1+1}.Sayı = {lst[i1]}")