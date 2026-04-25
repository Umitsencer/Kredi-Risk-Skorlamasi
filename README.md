# 🏦 Kredi Risk Skorlaması (Makine Öğrenmesi)

Bu proje, bankacılık sektöründe kredi kartı veya kredi başvurularının onaylanıp onaylanmayacağına karar veren klasik bir Sınıflandırma (Classification) problemidir.

## 🎯 Projenin Amacı
Bir bankanın elindeki geçmiş müşteri verilerini (yaş, gelir, geçmiş kredi durumu) kullanarak, yeni başvuran bir müşterinin kredisini geri ödeyip (0) ödeyemeyeceğini (1) makine öğrenmesi algoritmalarıyla tahmin etmek.

## 🛠 Kullanılan Teknolojiler
* **Python** (Veri İşleme ve Modelleme)
* **Pandas & NumPy** (Veri Analizi)
* **Scikit-Learn & XGBoost** (Makine Öğrenmesi Algoritmaları)

## 🧠 Mühendislik Yaklaşımı
Bu çalışma, sadece bir model eğitimi değil; bankacılık sektöründeki **risk yönetimi süreçlerini** optimize etmek amacıyla kurgulanmıştır. Proje kapsamında; sentetik veri üretimi ile gizlilik kurallarına (KVKK) sadık kalınmış, istatistiksel modeller ve **Random Forest** algoritması kullanılarak yüksek doğruluklu bir karar destek mekanizması oluşturulmuştur.

## 📊 Örnek Çıktı
Programı çalıştırdığınızda aşağıdaki gibi bir analiz raporu alırsınız:
```text
📊 MODEL BAŞARI RAPORU
Doğruluk Oranı (Accuracy): %96.50

Detaylı Metrikler:
              precision    recall  f1-score   support
     Ret (0)       0.98      0.95      0.96       112
    Onay (1)       0.94      0.98      0.96        88
```

## 🚀 Nasıl Çalıştırılır?
```bash
pip install -r requirements.txt
python train_model.py
```