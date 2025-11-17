@echo off
chcp 65001 > nul
title ECU DSG AI Assistant Kurulumu
color 0A

echo.
echo ════════════════════════════════════════════════
echo    🚗 ECU DSG AI ASSISTANT - KURULUM
echo ════════════════════════════════════════════════
echo.

echo 📦 1. Python kontrolü yapılıyor...
python --version > nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python bulunamadı!
    echo 💡 Lütfen Python'u yükleyin: https://python.org
    echo 💡 Kurulum sırasında "Add Python to PATH" işaretleyin!
    pause
    exit /b 1
)
echo ✅ Python kurulu

echo.
echo 📦 2. Gereksinimler yükleniyor...
pip install --upgrade pip
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo ❌ Pip kurulumu başarısız! Alternatif deneyelim...
    pip install pandas numpy scikit-learn matplotlib seaborn jupyter
)

echo.
echo 🔨 3. C simülasyonu derleniyor...
cd simulations
gcc dsg_simulator.c -o dsg_simulator.exe -lm

if %errorlevel% neq 0 (
    echo.
    echo ❌ GCC derleme hatası! MinGW kurulu mu?
    echo 💡 MinGW indir: https://mingw-w64.org/
    pause
    exit /b 1
)

echo.
echo 🎯 4. Test verisi oluşturuluyor...
dsg_simulator.exe

echo.
echo ════════════════════════════════════════════════
echo           ✅ KURULUM TAMAMLANDI!
echo ════════════════════════════════════════════════
echo.
echo 🏃 ÇALIŞTIRMAK İÇİN:
echo.
echo 1. 📊 Simülasyon çalıştır: 
echo    simulations\dsg_simulator.exe
echo.
echo 2. 🤖 AI Analizi çalıştır:
echo    python src\data_analysis\analyzer.py
echo.
echo 3. 📈 Sonuçları görüntüle:
echo    results\ klasörünü aç
echo.
echo ════════════════════════════════════════════════
pause