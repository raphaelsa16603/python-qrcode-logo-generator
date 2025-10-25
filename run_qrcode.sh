#!/bin/bash
# ==========================================
# Script: run_qrcode.sh
# Descrição: Cria ambiente virtual, instala dependências e gera QRCode
# Uso: ./run_qrcode.sh <URL> <FORMATO>
# Exemplo: ./run_qrcode.sh http://nao-por-acaso.blogspot.com svg
# ==========================================

set -e  # encerra se ocorrer erro

if [ -z "$1" ]; then
  echo "Uso: ./run_qrcode.sh <URL> <FORMATO>"
  echo "Exemplo: ./run_qrcode.sh http://exemplo.com jpg"
  exit 1
fi

URL=$1
FORMAT=${2:-jpg}

# Cria venv se não existir
if [ ! -d ".venv" ]; then
  echo "🔧 Criando ambiente virtual..."
  python3 -m venv .venv
fi

# Ativa o ambiente virtual
source .venv/bin/activate

# Instala dependências
echo "📦 Instalando dependências..."
pip install --upgrade pip
pip install -r requirements.txt

# Executa o gerador
echo "🚀 Gerando QRCode..."
python gerador_qr_code.py "$URL" "$FORMAT"

echo "✅ QRCode gerado em: output/qrcode_logo.$FORMAT"
