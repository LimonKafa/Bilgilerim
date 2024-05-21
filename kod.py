import time

while True:
    #seçenekler
    print("\nBir sayı girin (1-4):")
    print("1: İsim ve Soyisim")
    print("2: Yaşı")
    print("3: Hobisi")
    print("4: Yaşadığı yer")
    print("5: Çıkış")
   

    #seçimi
    secim = input("Seçiminiz: ")

    #cevaplar
    if secim == '1':
        print("Yükleniyor...")
        time.sleep(2)
        print("Yusuf Demirayak")
    elif secim == '2':
        print("Yükleniyor...")
        time.sleep(2)
        print("15")
    elif secim == '3':
        print("Yükleniyor...")
        time.sleep(2)
        print("Araba koleksiyonu")
    elif secim == '4':
        print("Yükleniyor...")
        time.sleep(2)
        print("Balıkesir")
        
    elif secim == '5':
        print("Çıkış Yapılıyor...")
        time.sleep(2)
        break
    else:
        print("Öyle bir sayı bulunmamakta ")

