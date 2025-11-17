# 🚗 ECU DSG Optimization - AI Automotive Assistant

DSG (Dual-Clutch Transmission) şanzıman sistemleri için AI destekli anomali tespiti ve veri analizi aracı.

## 📊 Demo Görseller

![Anomali Analizi](results/anomaly_analysis.png)
![Korelasyon Matrisi](results/correlation_matrix.png)

## 🎯 Özellikler
- **C Dili** - DSG şanzıman simülasyonu
- **Python AI** - Anomali tespiti (%10 başarı)
- **Machine Learning** - Isolation Forest algoritması
- **Veri Görselleştirme** - Matplotlib & Seaborn
- **Gerçek Zamanlı Analiz** - CAN-bus benzeri veri akışı

## 🛠️ Kurulum

```bash
# 1. Simülasyonu derle ve çalıştır
cd simulations
gcc dsg_simulator.c -o dsg_simulator.exe -lm
./dsg_simulator.exe

# 2. AI analizini çalıştır
cd ..
python src/data_analysis/analyzer.py