import math
import random

def rastgeleSayi():
    dusuk= int(input("Dusuk sayiyi girin:"))

    yuksek= int(input("yukseks sayiyi giriniz"))


    rastgele = random.randint(dusuk,yuksek)
    print(round(math.log(yuksek-dusuk+1,2)), "kere deneme sansiniz var!!")

    deneme=0 

    while deneme < math.log(yuksek-dusuk+1,2) :
        deneme+= 1

        tahmin = int(input("tahmininizi girin: "))

        if tahmin == rastgele:
            print("tebrikler sayiyi ", deneme ,"tekrarda bildiniz")
            break

        elif tahmin < rastgele:
            print("daha yuksek bir sayi deneyin")

        elif tahmin > rastgele:
            print("daha kucuk bir sayi deneyin")

    if deneme > math.log(yuksek-dusuk+1,2) :
        print("sayi %d idi" % rastgele)

    tekrar = str(input("tekrar denemek icin Y'ye basin: "))
    if tekrar == 'y' or tekrar == 'Y':
        rastgeleSayi()
    else:
        pass
    
rastgeleSayi()
        
                       