@echo off
echo [*] Creating virtual environment...
python -m venv venv

echo [*] Activating virtual environment...
call venv\Scripts\activate

echo [*] Installing requirements...
pip install -r requirements.txt

echo [*] Running password recovery tool...

:: Clear the console
cls

python src\main.py
