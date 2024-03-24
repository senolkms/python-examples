#3 kişi için ad, soyad, vize, final notları tutan bir liste ve işlemler
lst=list()
for i1 in range(1,3):
    ad=input(str(i1)+". Kişinin Adını Giriniz: ")
    sad=input(str(i1) + ". Kişinin Soyaadını Giriniz: ")
    vz=int(input(str(i1)+". Kişinin Vize Notunu Giriniz: "))
    fnl=int(input(str(i1) + ". Kişinin Vize Final Giriniz: "))
    lst.append([ad,sad,vz,fnl])
print(lst)
print("Liste Elemanları Yazdırılıyor...")
print("    Adınız  Soyadınız Vizeniz Finaliniz Ortalamanız Durumunuz")
for i1 in range(1,3):
    print("%10s %10s %7d %9d %11.2f" % (lst[i1-1][0],lst[i1-1][1], lst[i1-1][2],lst[i1-1][3],lst[i1-1][2]*0.4+lst[i1-1][3]*0.6), end="")
    if (lst[i1-1][2]*0.4+lst[i1-1][3]*0.6)>=60 and lst[i1-1][3]>=50:
        print("     GEÇTİ")
    else:
        print("     KALDI")