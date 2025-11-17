@echo off
chcp 65001 > nul
title ECU DSG AI Assistant - Güncelleme
color 0E

echo.
echo ════════════════════════════════════════════════
echo    🔄 ECU DSG AI ASSISTANT - GÜNCELLEME
echo ════════════════════════════════════════════════
echo.

echo 📥 GitHub'dan son değişiklikleri çekiyorum...
git pull origin main

echo.
echo 📦 Gereksinimleri güncelliyorum...
pip install --upgrade -r requirements.txt

echo.
echo 🔨 C kodunu yeniden derliyorum...
cd simulations
gcc dsg_simulator.c -o dsg_simulator.exe -lm
cd ..

echo.
echo ✅ Güncelleme tamamlandı!
echo.
pause