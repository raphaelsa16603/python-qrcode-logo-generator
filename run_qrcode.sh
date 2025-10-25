
#!/bin/bash
set -e

# ===========================================
# QRCode Generator - Pass-through CLI (Linux/Codespaces)
# No parsing here. Everything is handled by Python.
# Ex.: ./run_qrcode.sh --url=http://site --filetype=png --squareratio=33 --squarecolor=black --size=900
# ===========================================

# venv
if [ ! -d ".venv" ]; then
  echo "[setup] Creating .venv ..."
  python3 -m venv .venv
fi
source .venv/bin/activate

# deps
python -m pip install --upgrade pip >/dev/null
pip install -r requirements.txt >/dev/null

# repassa todos os args ao Python
python gerador_qr_code.py "$@"
