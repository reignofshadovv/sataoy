### Döngü Ödevi - Python Sayı Tahmin Uygulaması

import random

sayi=random.randint(0,50)
hak = 9

print("\n╔═╗╔═╗╦ ╦╦  ╔╦╗╔═╗╦ ╦╔╦╗╦╔╗╔  ╔═╗╦ ╦╦ ╦╔╗╔╦ ╦")    # ASCII
print("╚═╗╠═╣╚╦╝║   ║ ╠═╣╠═╣║║║║║║║  ║ ║╚╦╝║ ║║║║║ ║")      # Başlık
print("╚═╝╩ ╩ ╩ ╩   ╩ ╩ ╩╩ ╩╩ ╩╩╝╚╝  ╚═╝ ╩ ╚═╝╝╚╝╚═╝")
print("\n\n0 ile 50 arasında bir sayı tahmin edebilir misin?\n\n10 Hakkınız Var!")
### Döngü Başlar...
while True:
    # Oyuncudan sayı tahmini alınır.
    tahmin = int(input("\nSayı Giriniz --> "))
    # Tahmin edilen sayının daha önceden belirlenen sayıya eşit olması 
    # durumunda döngü kırılır.
    if tahmin == sayi:
        print("\n\n\_  _ ____ ___  ____ _  _ ___  _ _  _ ")      # ASCII
        print("|_/  |__|   /  |__| |\ | |  \ | |\ | ")                  # Kazandın
        print("| \_ |  |  /__ |  | | \| |__/ | | \| ")                  # Mesajı
        print("\nTebrikler! Doğru sayıyı bildiniz. :)\n")
        break
    # Tüm hakların tükenmesi durumunda döngü kırılır.
    elif hak == 0:
        print("\n\n_  _ ____ _   _ ___  ____ ___ ___ _ _  _")   # ASCII
        print("|_/  |__|  \_/  |__] |___  |   |  | |\ |")               # Kaybettin
        print("| \_ |  |   |   |__] |___  |   |  | | \|")               # Mesajı                  
        print("\nHiç Hakkınız Kalmadı! :(\n")
        break
    # Tahmin edilen sayının 0'dan küçük ve 50'den büyük, yani istenilen 
    # aralıkta olmaması durumunda hata mesajıyla haklar eksilmeden 
    # tekrar tahmin yapılması istenir.
    elif tahmin > 50 or tahmin < 0:
        print("\n\n           ***HATA***\n\nLütfen 0 ile 50 arasında bir değer giriniz.\n")
        print("( Kalan Tahmin Hakkınız: ", hak+1, ")")
    # Yanlış tahmin sonrası mesaj ve kalan hakların gösterimi
    else:
        hak -= 1
        print("Bilemedin...\n( Kalan Tahmin Hakkınız: ", hak+1, ")")