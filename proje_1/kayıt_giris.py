class KayitOl():
    def __init__(self):
        self.kayit_kullanici_adi=input("Kayıt olmak için bir kullanıcı adı belirleyin:")
        self.kayit_sifre=input("Kayıt olmak için şifrenizi belirleyin:")
class GirisYap(KayitOl):
    def __init__(self):
        super().__init__()
        self.giris_kullanici_adi=input("Giriş yapmak için kullanıcı adını giriniz:")
        self.giris_sifre=input("Giriş yapmak için şifrenizi giriniz:")

    def giris(self):
        while True:
            if self.kayit_kullanici_adi==self.giris_kullanici_adi and self.kayit_sifre==self.giris_sifre:
                print("Giriş Başarılı!")
                break
            else:
                print("Giriş Başarısız!Lütfen tekrar deneyin")
                self.giris_kullanici_adi=input("Kullanıcı adınızı giriniz:")
                self.giris_sifre=input("Şifrenizi giriniz:")

p1=GirisYap()
p1.giris()

        