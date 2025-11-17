@echo off
chcp 65001 > nul
title ECU DSG AI Assistant - Çalıştır
color 0B

echo.
echo ════════════════════════════════════════════════
echo    🚗 ECU DSG AI ASSISTANT - ÇALIŞTIR
echo ════════════════════════════════════════════════
echo.

echo 🔄 Simülasyon verisi güncelleniyor...
cd simulations
dsg_simulator.exe
cd ..

echo.
echo 🤖 AI analizi başlatılıyor...
python src\data_analysis\analyzer.py

echo.
echo ✅ Analiz tamamlandı! Sonuçlar:
echo    - 📊 results\anomaly_analysis.png
echo    - 📈 results\correlation_matrix.png
echo.
echo 🎯 results\ klasörünü açmak için Enter'a bas...
pause

start results\