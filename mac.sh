#!/bin/bash

echo "[*] Creating virtual environment..."
python3 -m venv venv

echo "[*] Activating virtual environment..."
source venv/bin/activate

echo "[*] Installing requirements..."
pip install -r requirements.txt

echo "[*] Running password recovery tool..."

# Clear the screen before launching
clear

python3 src/main.py

echo
echo "[✔] Done. To run again later:"
echo "    source venv/bin/activate"
echo "    python3 src/main.py"