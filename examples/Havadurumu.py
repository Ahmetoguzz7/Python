import requests

def hava_durumu_al(sehir, api_anahtari):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api_anahtari}&units=metric"
    cevap = requests.get(url)
    veri = cevap.json()
    if veri["cod"] == 200:  # Hava durumu verisi başarılı bir şekilde alındıysa
        aciklama = veri["weather"][0]["description"]
        sicaklik = veri["main"]["temp"]
        nem = veri["main"]["humidity"]
        ruzgar_hizi = veri["wind"]["speed"]
        print(f"{sehir} için hava durumu:")
        print(f"Açıklama: {aciklama}")
        print(f"Sıcaklık: {sicaklik}°C")
        print(f"Nem: {nem}%")
        print(f"Rüzgar Hızı: {ruzgar_hizi} m/s")
    else:
        print("Hava durumu bilgisi alınamadı.")

if __name__ == "__main__":
    sehir = input("Hangi şehrin hava durumu bilgisini almak istersiniz? ")
    api_anahtari = "YOUR_API_KEY"  # Buraya kendi API anahtarınızı yerleştirin
    hava_durumu_al(sehir, api_anahtari)

#Bu Hava Durumunu Yapmaya Bak
    