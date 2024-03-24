#araSınav
#lst=lst+[[ad,sad,vz,fnl]]
lst=list()
tp=0
syc=0
for i1 in range(1,6):
    s=int(input(f"{i1}. Sayıyı Giriniz :"))
    lst.append(s) #lst=lst+[s]
    if s%2==0:
        tp=tp+s
        syc=syc+1

for i1 in lst:
    print(i1)

print(f"Çift Olanların Ortalaması ={tp/syc}")