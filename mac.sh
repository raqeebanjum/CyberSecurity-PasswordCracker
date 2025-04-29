#!/bin/bash

echo "[*] Creating virtual environment..."
python3 -m venv venv

echo "[*] Activating virtual environment..."
source venv/bin/activate

echo "[*] Installing requirements..."
pip install -r requirements.txt

echo "[*] Running password recovery tool..."

# Clear the console
clear

python3 src/main.py
