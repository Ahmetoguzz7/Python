#integer değer
#print(4 - 0.5)
#print(9-0.862)
#print(3**0.8)
#print(11%2.87) # Mod alma operatörü ile işlem hallediliyor.
#print(11//2.87) #Burada yuvarlayarak mod alıyor

#ufak bir mod alma örneği
# alınacak maaş
#print(5000 - (5000*0.283)) 
 # ödenecek kredi
#print(5000 - (3000*0.25364))

#maasAli=5500
#maasAhmet=2871
#vergi=0.2453

#alimaas=print(maasAli * vergi)
#ahmetmaas=print(maasAhmet * vergi)

#x=1        #int
#y=2.523    #float

#name ="Çinar"  #string
#isStudent = True  #bool

#firstName="Ahmet"
#lastName="Mertoglu"
#print(firstName + lastName)

#Tek satırda birden fazla değişken tanımlama
#x, y, name ,isStudent =(1, 2.3, "Ahmet", True)

"""
1- Bir Müşterinin aşağıdaki bilgileri için değişken oluşturunuz.
 Müşteri Adı, Soyadı, ad+ soyad, Cinsiyet, tc kimlik, doğum yılı, adres bilgisi, yaşı

"""

#1.sorunun çözümü
"""
MüsteriAdi="Ahmet"
MüsteriSoyadi="Mertoğlu"
MüsteriCinsiyet = "Erkek"
MüsteriTc= 31486734264
MüsteriDoğumYili= "24.01.2003"
MüsteriAdresBilgisi=" İstiklal mah. Kirişhane Cad. Tarancı Sok. No:1 Kat:2"
MüsterininYaşi= 24

print(MüsteriAdi)
print(MüsteriSoyadi)
print(MüsteriAdi + MüsteriSoyadi)
print(MüsteriCinsiyet)
print(MüsteriTc)
print(MüsteriDoğumYili)
print(MüsteriAdresBilgisi)
print(MüsterininYaşi)

"""
"""
2- Aşağıdaki Siparişlerin Toplam Bilgisini Hesaplayınız.

Sipariş 1 => 110 TL
Sipariş 2 => 1100.5 TL
Sipariş 3 => 356.5 TL

"""
"""
siparis1=110
siparis2=1100.5
siparis3=356.5
total=siparis1 + siparis2 + siparis3

print(total)
"""

#İnputtan alınan değerin string değer olduğunu unutma
"""
x= input('1.sayı:')
y= input('2.sayı:')

toplam= int(x) + int(y) 
print(toplam) #Eğer int koymasaydık tring olarak yan yana getiriyordu sayıları
"""
"""
name= 'Ahmet'
surname = ' Mertoglu'
age=35
#age str type'ına dönüştürdüm. \n ile ondan sonrasını alt satıra getirerek kullandım.
#Aynı zamanda print içinde '' ile hem boşluk bıraktım hem ekliceklerimi gösterdim.
greeting = 'My name is' + name + '' + 'Surname' + surname + ' '+ 'and \n I am'+' '+ str(age) +' ' + 'years old.'

print(greeting[0])#bunu kullanırken parantez ve print'leri silerek işleme devam et
print(greeting[3])
print(len(greeting))
"""
#len() içeriğine yazdığımız şeyin kaç karakterli olduğunu söyler
#message. upper() #upper buradaki bütün karakterleri büyük harflere çevirir.
#message.lower()  #lower buradaki bütün karakterleri küçük harflere çevirir.
#.title() yazıldığında her kelimenin baş harfi büyük harfe çevrilir
#.capitalize() sadece cümlenin ilk harfini büyük harfe çevrilmiş olur.
#.strip() strip metodunu çalıştırdığımızda başta olan boşluk karakteri gider. Kullanıcı tarafından girilmiş olabilir
#.strip() baş ve sondaki
#.split() string'i boş karakterlerinden ayırır parça parça verir.
#.join() elemeanı parça parça olan mesajları birleştirecek ve öyle verir.
#.find() metodu ile aradığınız kelimenin cümle içinde var mı yok mu bulabilirsiniz. İndex Numarasını kelişmenin ilk harfinde geri gönderir.
#.startswith('h') cümlenin başlangıcının h ile başladığına baka. Evetse True döndürür yanlışsa false döndürür
#.endswith() Cümlenin aradığınız harf ile mi bitiyor görürsünüz.
#.replace('Ahmet', 'Ôğuz') bu fonk. ahmet yerine oğuz yazdırır.
#.append() listeye istedğiniizi ekle
#.insert(3, 78)  3.elemanın yerine 78 ekler ve bir yana kayar
#.pop() seçilen elemanı siler
#.remove(78)  aranan elemanı siler
#.sort() listeyi sıralar
#.reverse() tam tersine döndürür
"""
my_list=[1,2,3]
my_list = ['bir',2,True,5.6]
print(my_list)

list1 = ['one','two' ' There']
list2 = ['four', 'Five', 'Six']
numbers = list1 + list2
print(numbers)
"""
#Python Tuple
#list ile tuple arasında kullanım açısından bir fark yok
#tuple elemanı atandıktan sonra eleman üstünde dğişiklik veya atmaaya izişn vermiyor
#tuple.count() formülünü kullanabiliriz.
"""
list = [1,2,3]
tuple=(1, 'iki', 3)
print(type(list))
print(type(tuple))
"""


#key --value
#41=> kocalei 34 => İSTANBUL
#Kütüphane kullanmadan listeleme ile plaka bilgisine  ulaşabilirsiniz.

#Bu kullanımda sıraların birbirine uyması gerekiyor
#sehirler=['Kocaeli', ' İstanbul']
#plakalar=[41,34]
#print(plakalar[sehirler.index('Kocaeli')])

#listeden ulaşabilirsiniz.,
"""
plakalar={'kocaeli ': 41, 'istanbul': 34 }

print(plakalar['kocaeli'])
print(plakalar['istanbul'])
"""
#Set indexlenemeyen bir listedir. Döngülerle ulaşabilirsiniz.
fruits= {'orange', 'apple','banana' }
print(fruits)
#.add eklemek yapar
#.update(['mango', 'grape']) yeniler .# liste içerisinde olan elemanı eklemek istersen eklemez
#print(set()) yaparsak yinelenen elemanları siler
#pop için son eleman silinir
#discard() içine yazdığın elemanı siler

