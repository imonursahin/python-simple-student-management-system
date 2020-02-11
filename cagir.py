import time

class Ogrenci(object):
    def __init__(self, isim=None, soyisim=None, numara=None, bölüm=None, vizeNot=None, finalNot=None, topDersSaat=None, devamsızlıkBil=None, danisman=None):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.bölüm = bölüm
        self.vizeNot = vizeNot
        self.finalNot = finalNot
        self.topDersSaat = topDersSaat
        self.devamsızlıkBil = devamsızlıkBil


def notlar(vize,final):
    vizeNotu=vize
    finalNotu=final
    ortalamaNot=int((0.4*vizeNotu)+(0.6*finalNotu))

    if(ortalamaNot>=88):
        print("[Vize Notu: {}] [Final Notu: {}] [Ortalaması: int{}] [Harf Notu: AA] [GEÇTİ]".format(vizeNotu,finalNotu,ortalamaNot))
    elif ortalamaNot>=82 and ortalamaNot<88 :
        print("[Vize Notu: {}] [Final Notu: {}] [Ortalaması: {}] [Harf Notu: BA] [GEÇTİ]".format(vizeNotu,finalNotu,ortalamaNot))
    elif ortalamaNot >= 76 and ortalamaNot < 82:
        print("[Vize Notu: {}] [Final Notu: {}] [Ortalaması: {}] [Harf Notu: BB] [GEÇTİ]".format(vizeNotu,finalNotu,ortalamaNot))
    elif ortalamaNot >= 66 and ortalamaNot < 76:
        print("[Vize Notu: {}] [Final Notu: {}] [Ortalaması: {}] [Harf Notu: CB] [GEÇTİ]".format(vizeNotu,finalNotu,ortalamaNot))
    elif ortalamaNot >= 60 and ortalamaNot < 66:
        print("[Vize Notu: {}] [Final Notu: {}] [Ortalaması: {}] [Harf Notu: CC] [GEÇTİ]".format(vizeNotu,finalNotu,ortalamaNot))
    elif ortalamaNot >= 55 and ortalamaNot < 60:
        print("[Vize Notu: {}] [Final Notu: {}] [Ortalaması: {}] [Harf Notu: DC] [KOŞULLU GEÇTİ]".format(vizeNotu,finalNotu,ortalamaNot))
    elif ortalamaNot >= 45 and ortalamaNot < 55:
        print("[Vize Notu: {}] [Final Notu: {}] [Ortalaması: {}] [Harf Notu: DD] [KOŞULLU GEÇTİ]".format(vizeNotu,finalNotu,ortalamaNot))
    else:
        print("[Vize Notu: {}] [Final Notu: {}] [Ortalaması: {}] [Harf Notu: FF] [KALDI]".format(vizeNotu,finalNotu,ortalamaNot))


def devamsizlik(haftaDersSaat,devamsızlık):
    hafta=haftaDersSaat
    devam=devamsızlık
    d_hakki = (hafta*70/100)
    d_hakki=hafta-d_hakki
    if (d_hakki <= devam):
        print("[Devamsızlıktan Kaldı]")
    else:
        print("[Geçti]")


def ogrencibilgisi(ogrenciNo):
    ogrenciList=[]

    ogrenciList.append(Ogrenci('Ali','Veli','1998','YBS')) 
    ogrenciList.append(Ogrenci('Onur','Şahin','2040','YBS'))   
    for ogr in ogrenciList: 
        if(ogr.numara==ogrenciNo):
            print("[Adı: {}]".format(ogr.isim))
            print("[Soyadı: {}]".format(ogr.soyisim))
            print("[No: {}]".format(ogr.numara))
            print("[Bölüm: {}]".format(ogr.bölüm))
            print("------Danışman Bilgisi----")
            akademisyenBilgisi()
        while True:
            print("""
                [1] Not Giriş
                [2] Devamsızlık Giriş
                [0] Çıkış Yap
                    """)

            islem=int(input("Lütfen Yapmak İstediğiniz İşleme Ait Numarayı Girin :"))
            if islem==1: # Öğrenci Bilgisi
               vizeNotu=int(input("Vize: "))
               finalNotu=int(input("Final: "))
               notlar(vizeNotu,finalNotu)
            elif islem==2:
               dersSaati=int(input("Haftalık Ders Saaati: "))
               devamsiz=int(input("Devamsızlık: "))
               devamsizlik(dersSaati,devamsiz)
               
            elif islem==0:
                print("Çıkış yaptınız")
                time.sleep(1)
                break
            else:
                print("Yanlış tuşlama yaptınız")
                pass


            break
        else:
            print("Bu numaraya sahip öğrenci bulunmamaktadır.")
            break
def akademisyenBilgisi():
        print("Adı: Onur")
        print("Soyadı: Şahin")
        print("Bölümü: YBS")
