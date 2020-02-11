import time
import cagir

print("""
==============================================
=                                            =
= Öğrenci Bilgi Sistemi - Akademisyen Girişi =
=       (k_adi: onur - sifre: 1903)          = 
=                                            =
==============================================
""")
ogr_kullanici = "onur"
ogr_sifre  = "1903"
giris_hakki = 3



while True:
    o_adi = input("Kullanıcı Adı :")
    o_sifre  = input("Parola :")

    if (giris_hakki == 0 ):
        print("Giriş Hakkınız Bitti... Daha sonra tekrar deneyin.")
        break

    elif (o_adi != ogr_kullanici and o_sifre == ogr_sifre):
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)
        print("Kullanıcı Adı Hatalı...")
        giris_hakki -= 1
        print("Giriş Hakkı: ", giris_hakki)
        
    elif (o_adi == ogr_kullanici and o_sifre != ogr_sifre):
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)
        print("Parola Hatalı...")
        giris_hakki -= 1
        print("Giriş Hakkı: ", giris_hakki)

    elif (o_adi != ogr_kullanici and o_sifre != ogr_sifre):
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)
        print("Kullanıcı Adı ve Parola Hatalı...")
        giris_hakki -= 1
        print("Giriş Hakkı: ", giris_hakki)
        
    else:
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)
        print("Başarıyla Sisteme Giriş Yaptınız...Lütfen Bekleyin.")
        time.sleep(1)
        while True:
            print("""

                [1] Öğrenci Bilgisi
                [2] Akademisyen Bilgisi
                [0] Çıkış Yap
            
                    """)

            islem=int(input("Lütfen Yapmak İstediğiniz İşleme Ait Numarayı Girin :"))
            if islem==1: # Öğrenci Bilgisi
                print("-------Kayıtlı Öğrenciler-----")
                
                print('[Ad: Ali]','[Soyad: Veli]','[Numarası: 1998]','[Bölümü: YBS]')
                print('[Ad: Onur]','[Soyad: Şahin]','[Numarası: 2040]','[Bölümü: YBS]')
                ogrenciNo=input("İşlem Yapmak İstediğiniz Ogrencinin Numarası :")
                cagir.ogrencibilgisi(ogrenciNo,)


            elif islem ==2: #Akademisyen Bilgisi
                print("")
                cagir.akademisyenBilgisi()

                        
            elif islem==0:
                print("Çıkış Yaptınız")
                break        
