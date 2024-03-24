#Kenar uzunlukları girilen üçgenin çeşidini yazdırmak (eşkenar, ikizkenar, çeşitkenar)
k1=int(input("1. Kenar Uzunluğunu Giriniz: "))
k2=int(input("2. Kenar Uzunluğunu Giriniz: "))
k3=int(input("3. Kenar Uzunluğunu Giriniz: "))
if k1==k2 and k1==k3:
    print("Kenarları",k1,",",k2,"ve",k3,"olan üçgen eşkenar üçgendir.")
elif k1==k2 or k1==k3 or k2==k3:
    print("Kenarları",k1,",",k2,"ve",k3,"olan üçgen ikizkenar üçgendir.")
else:
    print("Kenarları",k1,",",k2,"ve",k3,"olan üçgen çeşitkenar üçgendir.")