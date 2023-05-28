
#opencv kütüphanelerinin kullanılması
import cv2
import numpy as np
import os
from itertools import combinations
from skimage.metrics import structural_similarity as compare_ssim

# Mesafeyi hesaplamak için bir fonksiyon
def resimleri_karsilastir(image1, image2):
    return compare_ssim(image1, image2)

# Dosya yolu
image_dosyası = "/Users/pelinustunel/Desktop/ALGORTIMA_ANALIZI_ODEV_SOURCES"
image_listesi = os.listdir(image_dosyası)

benzerlikler = []

# Her bir görüntü çifti için benzerliği karşılaştırma
for i in range(len(image_listesi)):
    img_path1 = os.path.join(image_dosyası, image_listesi[i])
    img1 = cv2.imread(img_path1, 0)  # gray scale
    img1 = cv2.resize(img1, (20, 20))  # Resmi 20x20 boyutuna dönüştürme

    for j in range(i + 1, len(image_listesi)):
        img_path2 = os.path.join(image_dosyası, image_listesi[j])
        img2 = cv2.imread(img_path2, 0)  # gray scale
        img2 = cv2.resize(img2, (20, 20))  # Resmi 20x20 boyutuna dönüştürme

        benzerlik = resimleri_karsilastir(img1, img2)
        benzerlikler.append(((image_listesi[i], image_listesi[j]), benzerlik))

# Benzerliklere göre sıralama
benzerlikler.sort(key=lambda x: -x[1])  # ssim ile, daha yüksek değer daha benzer anlamına gelir

# Sonuçları yazdırma
for (image_dosya1, image_dosya2), benzerlik in benzerlikler:
    benzerlik_percent = benzerlik * 100
    print(f" {image_dosya1} ve {image_dosya2} arasındaki, benzerlik: {benzerlik_percent:.2f}%")
