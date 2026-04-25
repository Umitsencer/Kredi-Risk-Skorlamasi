import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import warnings
warnings.filterwarnings('ignore')

print("🏦 Kredi Risk Skorlama Modeli Başlatılıyor...\n")

# 1. SENTETİK VERİ ÜRETİMİ (Banka verisi gizli olduğu için)
# Yaş, Gelir, Kredi Geçmişi (0=Kötü, 1=İyi), Kredi Miktarı, Onay (0=Ret, 1=Onay)
np.random.seed(42)
data_size = 1000

print("[1/4] Sentetik Müşteri Verisi Üretiliyor...")
df = pd.DataFrame({
    'Yas': np.random.randint(18, 70, data_size),
    'Aylik_Gelir': np.random.randint(15000, 150000, data_size),
    'Kredi_Miktari': np.random.randint(10000, 500000, data_size),
    'Gecmis_Kredi_Puani': np.random.randint(300, 850, data_size)
})

# Basit bir mantık: Geliri yüksek ve kredi puanı 600'den büyük olanlar genelde onay alır.
df['Kredi_Onay'] = np.where((df['Aylik_Gelir'] > 30000) & (df['Gecmis_Kredi_Puani'] > 600), 1, 0)
df['Kredi_Onay'] = np.where((df['Kredi_Miktari'] > df['Aylik_Gelir'] * 20), 0, df['Kredi_Onay']) # Çok kredi isteyen ret yer

# 2. VERİ HAZIRLIĞI
X = df.drop('Kredi_Onay', axis=1)
y = df['Kredi_Onay']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("[2/4] Veri Eğitim (Train) ve Test olarak %80-%20 oranında bölündü.")

# 3. MODEL EĞİTİMİ (Random Forest)
print("[3/4] Random Forest Algoritması Eğitiliyor...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4. TAHMİN VE BAŞARI ÖLÇÜMÜ
print("[4/4] Test Verisi Üzerinde Tahminler Yapılıyor...\n")
y_pred = model.predict(X_test)

print("="*40)
print("📊 MODEL BAŞARI RAPORU")
print("="*40)
print(f"Doğruluk Oranı (Accuracy): %{accuracy_score(y_test, y_pred)*100:.2f}")
print("\nDetaylı Metrikler:")
print(classification_report(y_test, y_pred, target_names=['Ret (0)', 'Onay (1)']))

# 5. ÖRNEK MÜŞTERİ TESTİ
print("="*40)
print("🧑‍💼 YENİ MÜŞTERİ TESTİ")
yeni_musteri = pd.DataFrame({'Yas': [25], 'Aylik_Gelir': [45000], 'Kredi_Miktari': [50000], 'Gecmis_Kredi_Puani': [710]})
sonuc = model.predict(yeni_musteri)
karar = "ONAYLANDI ✅" if sonuc[0] == 1 else "REDDEDİLDİ ❌"
print(f"Müşteri Profili:\n{yeni_musteri.to_string(index=False)}")
print(f"Sistem Kararı: {karar}")
print("="*40)