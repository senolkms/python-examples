s1=int(input("1. Sayıyı Giriniz  :"))
s2=int(input("2. Sayıyı Giriniz  :"))
s3=int(input("3. Sayıyı Giriniz  :"))

if  s1>s2 and s1>s3:
    if s2>s3:
        print("Büyüğü    : ",s1)
        print("Ortancası : ",s2)
        print("Küçüğü    : ",s3)
    else:
        print("Büyüğü    : ", s1)
        print("Ortancası : ", s3)
        print("Küçüğü    : ", s2)
elif s2>s1 and s2>s3:
    if s1>s3:
        print("Büyüğü    : ", s2)
        print("Ortancası : ", s1)
        print("Küçüğü    : ", s3)
    else:
        print("Büyüğü    : ", s2)
        print("Ortancası : ", s3)
        print("Küçüğü    : ", s1)

elif s3>s1 and s3>s2:
    if s2>s1:
        print("Büyüğü    : ", s3)
        print("Ortancası : ", s2)
        print("Küçüğü    : ", s1)
    else:
        print("Büyüğü    : ", s3)
        print("Ortancası : ", s1)
        print("Küçüğü    : ", s2)
else:
    print("Farklı sayılar giriniz..")