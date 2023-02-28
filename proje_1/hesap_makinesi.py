from math import sqrt,factorial,log10

class IslemBir:
    def __init__(self):
        self.value=int(input("Sayı giriniz:"))

    def faktoriyel(self):
        if self.value<=0:
            print("Lütfen tekrar deneyiniz")
        else:
            value=factorial(self.value)
            print(f"Girdiğiniz sayının faktöriyel değeri: {value}")

    def basamak_sayisi(self):
        if self.value==0:
            print("Girdiğiniz sayının basamak değeri yoktur")
            
        else:
            value=log10(self.value)
            virgulsuz_basamak=round(value)
            print(f"Girdiğiniz basamak değerinin {virgulsuz_basamak+1} adet basamak değeri vardır.")
    def asal_sayi(self):
        for i in range(1,self.value):
            if i%self.value==0:
                print(f"Girdiğiniz {self.value} sayısı asal sayı değildir.")
                break
        else:
            print(f"Girdiğiniz {self.value} sayısı asal sayıdır.")
        

    def karekok_degeri(self):
        value=sqrt(self.value)
        print(f"Girdiğiniz sayının karrekök değeri: {value}")  
      
p1=IslemBir()
p1.basamak_sayisi()
p1.asal_sayi()
p1.faktoriyel()
p1.karekok_degeri()

