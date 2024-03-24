#2 ile 500 arasında rastgele oluşturulan 20 sayıdan mükemmel sayı olanları çıktı olarak veren kodu yazınız.
import random
tp=0
for s1 in range(20):
    s1 = int(random.randint(2, 501))
    for i in range(1,s1):
        if s1%i==0:
            tp+=i
    if s1==tp:
        print("Mükemmel sayıdır...",s1)