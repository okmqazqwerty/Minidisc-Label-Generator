@echo off
echo ========================================================
echo   Building MiniDisc Label Generator EXE Application...
echo ========================================================

pip install pywebview pyinstaller

pyinstaller --noconfirm --onedir --windowed --add-data "MiniDisc_Label_Generator.html;." --name "MiniDisc_Label_Generator" main.py

echo.
echo ========================================================
echo   Build finished! EXE location: dist/MiniDisc_Label_Generator/
echo ========================================================
pause
