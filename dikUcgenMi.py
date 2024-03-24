#Kenar uzunlukları girilen üçgenin dik üçgen olup/olmadığını yazdırmak
k1=int(input("1. Kenar Uzunluğunu Giriniz: "))
k2=int(input("2. Kenar Uzunluğunu Giriniz: "))
k3=int(input("3. Kenar Uzunluğunu Giriniz: "))
#2 kenarının kareleri toplamı diğer kenarın karesine eşitse dik üçgendir
if k1*k1==(k2*k2+k3*k3) or k2*k2==(k1*k1+k3*k3) or k3*k3==(k1*k1+k2*k2):
    print("Kenarları",k1,",",k2,"ve",k3,"olan üçgen dik üçgendir.")
else:
    print("Kenarları",k1,",",k2,"ve",k3,"olan üçgen dik üçgen değildir.")