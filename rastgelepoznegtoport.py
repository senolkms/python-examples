#20 sayıya -50 ile +50 arasında rastgele değer atayan, bu sayılardan pozitif olanların toplamını, negatif olanların ise ortalamasını çıktı olarak veren kodu yazınız.
import random
tp=0
neg=0
adt=0
for i1 in range(20):
    s1 = int(random.randint(-50, 51))
    print(s1)
    if s1>0:
        tp+=s1
    elif s1<0:
        neg+=s1
        adt+=1
print("Pozitif sayıların toplamı:",tp)
print("Negatif sayıların ortalaması:",round(neg/adt,2))