class Quiz:
    print("""Quiz uygulamasına hoşgeldiniz!Bugün yapacağımız şey size 10 soru yönlendirilecek ve bu 10 soru içinde 1 doğru şık olacak.
    Eğer doğru şıkkı işaretlerseniz 10 puan kazanırsınız.Lakin dikkat edin 4 yanlış 1 doğruyu götürüyor!Bol şans""")
    flag=input("Quize başlamak ister misiniz?(Evet veya Hayır)? ")
    if flag.upper()=="EVET":
        print("Quiz başlasın!")
        def __init__(self,score,yanlis_sayisi,total):    
            self.score=score
            self.yanlis_sayisi=yanlis_sayisi
            self.total=total
        def soru_1(self): 
                cevap_1=input("Bilgiler geçici olarak hangi bellek üzerinde tutulur?")
                if cevap_1.upper()=="RAM":
                    print("Cevap doğru tebrik ederiz!")
                    self.score+=10
                    print(self.score)
                else:
                    print("Yanlış cevap!")
                    self.yanlis_sayisi+=1
        def soru_2(self):
                cevap_2=input("""2)…………Temel Giriş – Çıkış , hesaplama ve kontrol işlemlerini yürüten ünitedir. 
                Barındırdığı emirler ile diğer birimleri çalıştırır ve denetler.""")
                if cevap_2.upper()=="CPU":
                    print("Doğru cevap tebrikler!")
                    self.score+=10
                else:
                    print("Yanlış cevap!")
                    self.yanlis_sayisi+=1
        def soru_3(self):
                cevap_3=input("3) Bilgisayardaki görüntüleri ………… oluşturur ve monitöre gönderir? ")
                if cevap_3.upper()=="EKRAN KARTI":
                    print("Doğru cevap!")
                    self.score+=10
                else:
                    print("Yanlış cevap!")
                    self.yanlis_sayisi+=1
        def soru_4(self):
                cevap_4=input("4) Kullanıcıya ait bilgiler kalıcı olarak …………………. de saklanabilir. ")
                if cevap_4.upper()=="HDD":
                    print("Doğru cevap!")
                    self.score+=10
                else:
                    print("Yanlış cevap!")
                    self.yanlis_sayisi+=1
        def soru_5(self):
                cevap_5=input("5)Donanım üniteleri arasında veri iletişiminin yapılmasını sağlayan birime verilen ad ?")
                if cevap_5.upper()=="ANAKART":
                    print("Doğru cevap!")
                    self.score+=10
                else:
                    print("Yanlış cevap!")
                    self.yanlis_sayisi+=1
                
        def soru_6(self):
                cevap_6=input("6)Bilgisayar bellek birimlerinden 1 byte, kaç bit’ ten oluşur??")
                if cevap_6.upper()=="8":
                    print("Doğru cevap!")
                    self.score+=10
                else:
                    print("Yanlış cevap!")
                    self.yanlis_sayisi+=1
        def soru_7(self):
                cevap_7=input("7)1 GB kaç MB?")
                if cevap_7.upper()=="1024":
                    print("Doğru cevap!")
                    self.score+=10
                else:
                    print("Yanlış cevap!")
                    self.yanlis_sayisi+=1
        def soru_8(self):
                cevap_8=input("8)Kâğıtta bulunan bilgiyi bilgisayara aktarmak için kullanılan cihaza ne ad verilir?")
                if cevap_8.upper()=="SCANNER":
                    print("Doğru cevap!")
                    self.score+=10
                else:
                    print("Yanlış cevap!")
                    self.yanlis_sayisi+=1
        def soru_9(self):
                cevap_9=input("9)Bilgisayarın her türlü elektronik aksamına ne ad verilir?")
                if cevap_9.upper()=="HARDWARE":
                    print("Doğru cevap!")
                    self.score+=10
                else:
                    print("Yanlış cevap!")
                    self.yanlis_sayisi+=1
        def soru_10(self):
                cevap_10=input("10)Aşağıdakilerden hangi tuş Cursorü (İmleci) satır başına getirir?")
                if cevap_10.upper()=="HOME":
                    self.score+=10
                else:
                    print("Yanlış cevap!")
                    self.yanlis_sayisi+=1
                    
        def hesaplama(self):
            self.total=self.score-((self.yanlis_sayisi//4)*10)
            print(f"""Yapmış olduğunuz quizde {10-self.yanlis_sayisi} kadar doğru yapıp {self.yanlis_sayisi} kadar yanlış yaptınız.
            Toplam puanınız:{self.total}""")
    elif flag.upper()=="HAYIR":
        print("Siz bilirsiniz :(")
    else:
        print("Lütfen tekrar deneyin")
        
    
p1=Quiz(score=0,yanlis_sayisi=0,total=0)
p1.soru_1()
p1.soru_2()
p1.soru_3()
p1.soru_4()
p1.soru_5()
p1.soru_6()
p1.soru_7()
p1.soru_8()
p1.soru_9()
p1.soru_10()
p1.hesaplama()









































































































