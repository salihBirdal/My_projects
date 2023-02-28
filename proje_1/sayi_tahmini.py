from random import randint


class SayiTahmin:
    def __init__(self):
        
        print("""Merhaba!Sayı tahmini oyunu için iki aralık giriniz!Bu aralıkları sayı kendinize güvendiğiniz sayı aralığını yazın!
        örnek:1.değere 30,2.değere 50 yazdıysanız sizin tahmin etmeniz gereken sayı 30-50 arasıdır (30 ve 50 sayısı da dahil).Unutmayın 
        10 şansınız var zaten size kaç hak kaldığınızı söyleyeceğim ve ilk girdiğiniz sayıyı ikinci girdiğiniz sayıdan küçük olmalı.İyi şanslar!!""")

        self.birinci_aralik=int(input("Birinci değer aralığını giriniz:"))
        self.ikinci_aralik=int(input("İkinci değer aralığını giriniz:"))
        self.sayi_tahmin=randint(self.birinci_aralik,self.ikinci_aralik)
        self.hak=5
        print(f"Tahmin edilen sayı {self.birinci_aralik} ile {self.ikinci_aralik} arasındadır.Bol şans!")
        
    def oyna(self):
        while self.hak > 0:
            self.kullanici_sayisi=int(input("Tahmin ettiğiniz sayıyı giriniz:"))
            
            if self.kullanici_sayisi == self.sayi_tahmin:
                print("TEBRİKLER!!")
                break  # doğru tahminde döngüyü sonlandır
                
            elif self.kullanici_sayisi < self.sayi_tahmin:
                print(f"Girdiğiniz {self.kullanici_sayisi} tahmin etmekte olan sayınızdan daha büyüktür.Lütfen daha büyük bir sayı deneyiniz")
                
            elif self.kullanici_sayisi > self.sayi_tahmin:
                print(f"Girdiğiniz {self.kullanici_sayisi} tahmin etmekte olan sayınızdan daha küçüktür.Lütfen daha küçük bir sayı deneyiniz")
                
            self.hak -= 1
            print(f"{self.hak} hakkınız kaldı.")
            
        else:
            print(f"Hakkınız kalmamıştır.Tahmin edilen sayı:{self.sayi_tahmin}!")



p1=SayiTahmin()
p1.oyna()
