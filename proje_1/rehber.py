#REHBER UYGULAMASI
rehber={}
while True:
    
    print("""
    [1] Rehberi göster
    [2] Sorgula
    [3] Kişi Ekle
    [4] Kişi sil
    [0] Çıkış
 
    """)
    secim=int(input("Seçim giriniz:"))
    if secim==1:
        print(rehber)




    if secim==2:
        kisi=input("Kişiyi giriniz:")
        if kisi in rehber.keys():
            print("Girdiğiniz kişi bulunuyor".format(kisi))
        else:
            print(f"Aradığınız {kisi} kişisi rehberde bulunmuyor! Eklemek için seçim kısmına '3' yazınız!")




    if secim==3:
        kisi_1=input("Kişinin adını giriniz:")
        telefon_numarasi=int(input("Kişinin telefon numarasını giriniz:"))
        rehber.setdefault(kisi_1,telefon_numarasi)




    if secim==4:
        silinecek_kisi=input("Silinecek kişiyi giriniz:")
        rehber.pop(silinecek_kisi)
        varmi=silinecek_kisi in rehber.keys()
        if varmi:
            rehber.pop(silinecek_kisi)
        elif varmi==False:
            print(f"Silmek istediğiniz {silinecek_kisi} adlı kullanıcı gözükmüyor.")

    if secim==0:
        break
