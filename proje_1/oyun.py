from random import randint
def oyun():
    class Asker:
        def __init__(self):
            self.can=randint(30,70)#askerlerin can değerleri oluştururken rastgele oluşturuyor
            self.hasar=randint(30,90)#banna vurduklarında verdikleri hasar aynı şekilde randomla yaptım
            self.canli_mi=True #oyuna ilk başladığında bütün robotlar canlı oldukları için bunu true olarak döndürdük

            #Askerlerin ölebilmesi için ayrı bir metot tanımlamamız lazım
        def ol(self):
            self.canli_mi=False
        
            #Bu askerler ayrıca hasar alabilmeli.Bizim hasar verdiğimiz kadar onların can değeri düşmeli
        def hasaral(self,alinan_hasar:int):
            if alinan_hasar>=self.can:
                self.ol()
                
            else:
                self.can-=alinan_hasar  
                    #Canlının ölüp ölmediğine bakıyoruz




        #Sıra geldi oyuncu sınıfını tanımlamaya
    class Oyuncu:
        def __init__(self):
            self.can=randint(300,600)
            self.hasar=randint(30,90)
            self.canli_mi=True
        def ol(self):
            self.canli_mi=False
            print("Oyun bitti.Kaybettiniz!")
        def hasar_al(self,alinan_hasar:int):
            if alinan_hasar>=self.can:
                self.ol()
            else:
                self.can-=alinan_hasar
            
        #Şimdi ise terminale aktaralım
        
        #Oyun biz ölene dek ya da tüm düşmanlar ölene kadar devam edecek.

    askerler=[Asker() for i in range(10)] #10 adet düşman yarattık (liste üreteçleri)
    oyuncu=Oyuncu() #oyuncu oluşturma

        
    while True:#Askerler listelendikten sonra bu askerlerden birini çekecek ve ona vuracağız.O asker hasar aldıktan veya öldükten sonra kalan
        # askerlerin arasından rastgele olarak seçilecek olan asker de bize vuracaktır.Sonra başa dönecek ve askerler tekrar listenecek
        print("-------Oyuncu Bilgileri-------")
        print(f"Oyuncu Sağlık:{oyuncu.can} ---- Oyuncu Hasar:{oyuncu.hasar}")
        print("\n-------ASKERLER-------")
        for numara,asker in enumerate(askerler):
            if asker.canli_mi:
                print(f"{numara}.ASKER -------CAN DEĞERİ:{asker.can}, -------HASAR DEĞERİ:{asker.hasar}")
        secilen_asker=int(input("Saldırı için seçilen asker:")) #seçilen askere değer atadık
        if secilen_asker>len(askerler) -1 or secilen_asker<0:#eğerki oyuncu hatalı bir numara girerse (seçeceği asker) bir uyarı yazdırıp başa sarıyoruz
            print("Girilen asker numarası yanlış!") 
            continue
        else:
            askerler[secilen_asker].hasaral(oyuncu.hasar)
            if askerler[secilen_asker].canli_mi==False:
                askerler.remove(askerler[secilen_asker])#eğer asker canlı değilse bu askeri listeden siliyoruz.Bu sayede listede yalnızca canlı
                #askerler kaıyor.
            if askerler:
                saldiran_asker=randint(0,len(askerler)-1)#Bu koşul askerler listesinde hala yaşayan var mı yok mu diye bakar.
                oyuncu.hasar_al(askerler[saldiran_asker].hasar)#Belki de son asker saldırmış ve öldürülmüş olabiliriz.
            else:
                print("Tüm düşmanlar öldü kazandınız!")
                quit()
      