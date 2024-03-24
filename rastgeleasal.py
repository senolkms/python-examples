#2 ile 500 arasında rastgele oluşturulan 20 sayıdan asal olanları çıktı olarak veren kodu yazınız.
import random
for s1 in range(20):
    s1 = int(random.randint(2, 501))
    if s1>1:
        for i in range(2,s1):
            if s1%i==0:
                break
        else:
            print(f"{s1} Asaldır..")
