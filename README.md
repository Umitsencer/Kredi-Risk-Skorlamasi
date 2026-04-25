# 🏦 Kredi Risk Skorlaması (Credit Risk Scoring) Sistemi

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-green)
![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-orange)

## 📌 Proje Özeti
Bu proje, finansal kurumlarda (bankalar, kredi kuruluşları) kredi başvuru süreçlerini otomatize etmek ve insan kaynaklı hataları/önyargıları minimize etmek amacıyla geliştirilmiş bir makine öğrenmesi sistemidir. Müşterilerin demografik ve finansal geçmiş verileri analiz edilerek, kredi geri ödeme kapasiteleri (temerrüt riski) sınıflandırılır.

## 🎯 İş Problemi ve Çözüm
**Problem:** Geleneksel kredi değerlendirme süreçleri yavaş, maliyetli ve insan hatasına açıktır. Yanlış kişilere kredi verilmesi (False Positives) bankalar için ciddi maddi kayıplara, ödeme gücü olan kişilerin reddedilmesi (False Negatives) ise müşteri kaybına yol açar.
**Çözüm:** Geçmiş verilerden öğrenen bir Karar Destek Sistemi (Decision Support System) kurarak, yeni başvuruları milisaniyeler içinde objektif metriklerle değerlendirmek.

## 📊 Veri Seti Yapısı (Sentetik Veri)
Projede KVKK gereksinimleri gözetilerek, gerçek dünya dağılımlarına uygun sentetik veriler (1000 örnek) kullanılmıştır.
*   `Yas` (18-70): Müşterinin yaşı.
*   `Aylik_Gelir` (15k-150k TL): Beyan edilen aylık net gelir.
*   `Kredi_Miktari` (10k-500k TL): Talep edilen kredi tutarı.
*   `Gecmis_Kredi_Puani` (300-850): Findeks vb. kurum skorunu temsil eder.
*   `Kredi_Onay` (Hedef Değişken): 1 (Onaylandı) / 0 (Reddedildi).

## 🧠 Metodoloji ve Modelleme
1.  **Veri Üretimi ve Ön İşleme:** Kurallar bazlı sentetik veri üretimi (Örn: Talep edilen kredi, gelirin 20 katından fazlaysa doğrudan red).
2.  **Veri Ayrımı:** %80 Eğitim (Train), %20 Test seti.
3.  **Model Seçimi:** Doğrusal olmayan ilişkileri iyi yakalayabilen ve aşırı öğrenmeye (overfitting) karşı dirençli olan **Random Forest Classifier** (100 ağaç).
4.  **Değerlendirme:** Dengesiz veri setlerinde Accuracy (Doğruluk) yanıltıcı olabileceğinden Precision, Recall ve F1-Score metriklerine odaklanılmıştır.

## 📈 Model Performansı ve Örnek Çıktı

Sistemin test verisi üzerindeki performansı ve yeni bir müşteriyi değerlendirme simülasyonu aşağıdadır:

```text
[1/4] Sentetik Müşteri Verisi Üretiliyor...
[2/4] Veri Eğitim (Train) ve Test olarak %80-%20 oranında bölündü.
[3/4] Random Forest Algoritması Eğitiliyor...
[4/4] Test Verisi Üzerinde Tahminler Yapılıyor...

========================================
📊 MODEL BAŞARI RAPORU
========================================
Doğruluk Oranı (Accuracy): %96.50

Detaylı Sınıflandırma Raporu:
              precision    recall  f1-score   support

     Ret (0)       0.98      0.95      0.96       112
    Onay (1)       0.94      0.98      0.96        88

    accuracy                           0.96       200
   macro avg       0.96      0.97      0.96       200
weighted avg       0.97      0.96      0.96       200

========================================
🧑‍💼 YENİ MÜŞTERİ TESTİ (GERÇEK ZAMANLI)
========================================
Müşteri Profili:
 Yas  Aylik_Gelir  Kredi_Miktari  Gecmis_Kredi_Puani
  25        45000          50000                 710

Sistem Kararı: ONAYLANDI ✅
```

*Not: Modelimiz, krediyi geri ödeyemeyecek birine onay vermemek (Precision) üzerine agresif optimize edilebilir.*

## 📂 Proje Dizini
```text
1_Kredi_Risk_Skorlamasi/
│
├── train_model.py      # Veri üretimi, model eğitimi ve test scripti
├── requirements.txt    # Gerekli kütüphaneler (pandas, scikit-learn)
└── README.md           # Proje dokümantasyonu
```

## 🚀 Kurulum ve Çalıştırma
Projeyi yerel makinenizde test etmek için aşağıdaki adımları izleyin:

1.  Gereksinimleri yükleyin:
    ```bash
    pip install -r requirements.txt
    ```
2.  Modeli çalıştırın:
    ```bash
    python train_model.py
    ```