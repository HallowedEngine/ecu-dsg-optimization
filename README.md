# Automotive DSG AI Assistant 🚗🤖

DSG (Dual-Clutch Transmission) sistemleri için AI destekli anomali tespiti ve veri analizi aracı.

## 🎯 Özellikler
- **C diliyle DSG simülasyonu**
- **Python AI analizi** 
- **Anomali tespiti** (Isolation Forest)
- **Görselleştirme ve raporlama**
- **Gerçek zamanlı veri analizi**

## 🚀 Hızlı Başlangıç

```bash
# 1. Simülasyonu çalıştır
cd simulations
gcc dsg_simulator.c -o dsg_simulator.exe -lm
dsg_simulator.exe

# 2. AI analizini çalıştır
cd ..
python src/data_analysis/analyzer.py