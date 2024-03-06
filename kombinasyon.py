import tkinter as tk
from itertools import permutations
import random

def rastgele_renk():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))  # Rastgele renk oluştur

def kombinasyonlari_goster():
    kelime = kelime_giris.get()
    harfler = list(kelime)
    tum_kombinasyonlar = [''.join(p) for p in permutations(harfler)]
    
    sonuc_text.delete(1.0, tk.END)  # Önceki sonuçları temizle
    
    for kombinasyon in tum_kombinasyonlar:
        renk = rastgele_renk()
        sonuc_text.insert(tk.END, kombinasyon + '\n', kombinasyon)  # Her kombinasyonu renkli olarak ekle
        sonuc_text.tag_configure(kombinasyon, foreground=renk, font=('Helvetica', 12, 'bold'))

# Tkinter penceresini oluştur
pencere = tk.Tk()
pencere.title("Renkli Kelime Kombinasyonları")

# Kullanıcıdan kelimeyi girmesi için bir giriş kutusu
kelime_etiket = tk.Label(pencere, text="Kelimeyi girin:")
kelime_etiket.pack(pady=10)
kelime_giris = tk.Entry(pencere)
kelime_giris.pack(pady=10)

# Kombinasyonları gösterme düğmesi
kombinasyon_dugme = tk.Button(pencere, text="Kombinasyonları Göster", command=kombinasyonlari_goster)
kombinasyon_dugme.pack(pady=10)

# Sonuçları göstermek için bir metin kutusu
sonuc_text = tk.Text(pencere, height=10, width=30)
sonuc_text.pack(pady=10)

# Pencereyi çalıştır
pencere.mainloop()
