#Bankamatik Uygulaması

print("ATM'ye hoşgeldiniz.")
Kullanici_Adi="Melih Yıldırım"
print(Kullanici_Adi)
Hesap_Bakiyesi=5000
print('Hesap Bakiyeniz:',Hesap_Bakiyesi)
islem=int(input("Hangi İşlemi Gerçekleştirmek İstiyorsunuz:"))


if islem==1:
      print("Para Yatirma")
      x=int(input("Yatirilacak Tutari Giriniz:"))
      sonuc= Hesap_Bakiyesi+x
      print('Yeni bakiyeniz:' ,sonuc)
if islem==2:
      print("Para Çekme")
      x=int(input("Çekilecel Tutari Giriniz:"))
      sonuc= Hesap_Bakiyesi-x
      print("Yeni bakiyeniz",sonuc)
if islem==3:
      print("Havale-Eft Ödemeler")
      x=int(input("Gönderilecek Tutari Giriniz:"))
      sonuc= Hesap_Bakiyesi-x
      print("Yeni bakiyeniz",sonuc)
if islem==4:
      print("Hesap Bakiyesi")
      print(Hesap_Bakiyesi)
if islem==6:
      print("Borç Ödeme")
      x=int(input("Ödenecek Tutari Giriniz:"))
      sonuc= Hesap_Bakiyesi-x
      print("Yeni bakiyeniz",sonuc)





