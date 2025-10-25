
# 🧩 Gerador de QR Code com Espaço para Logo / QR Code Generator with Logo Space / Generador de QR con Espacio para Logo

---

## 🚀 DICA RÁPIDA — Windows & GitHub Codespaces (Quick Start)
- **Windows (.BAT):**
  ```bat
  gerador_qr_code.bat <URL> <FORMATO>
  ```
  Ex.: `gerador_qr_code.bat http://nao-por-acaso.blogspot.com svg`

- **Codespaces/Linux (.SH):**
  ```bash
  ./run_qrcode.sh <URL> <FORMATO>
  ```
  Ex.: `./run_qrcode.sh http://nao-por-acaso.blogspot.com jpg`

> Formatos: `jpg`, `bmp`, `svg` • Saída: `output/qrcode_logo.<formato>` • Ambiente `.venv` criado automaticamente.

---

## 🇧🇷 Português

### 📘 Descrição
Ferramenta em Python para gerar **QR Codes personalizados** (`JPG`, `BMP`, `SVG`) com **quadrado central branco** para inserir o **logo da empresa**. Ideal para marketing, impressão e uso corporativo.

---

## 🪟 Passo a passo — **Windows**
> Recomendado usar **Prompt de Comando (CMD)** ou **PowerShell**. Em **Git Bash**, use `cmd /c gerador_qr_code.bat ...`.

1. **Clonar o repositório**
   ```bat
   git clone https://github.com/SEU_USUARIO/python-qrcode-logo-generator.git
   cd python-qrcode-logo-generator
   ```

2. **(Opcional) Permitir scripts no PowerShell**
   ```powershell
   Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
   ```

3. **Executar com o .BAT (cria .venv e instala deps)**
   ```bat
   gerador_qr_code.bat <URL> <FORMATO>
   ```
   Ex.: `gerador_qr_code.bat http://exemplo.com svg`

4. **Ver o resultado**
   - Arquivo gerado em: `output/qrcode_logo.<formato>`

5. **Dicas**
   - Para atualizar o `pip` corretamente no .BAT, use `python -m pip install --upgrade pip`.
   - Se usar **Git Bash**, rode: `cmd.exe /c gerador_qr_code.bat http://exemplo.com jpg`.

---

## ☁️ Passo a passo — **GitHub Codespaces**
> Codespaces roda Linux (Ubuntu) com VS Code no navegador.

### A. Abrir no Codespaces
1. No GitHub, clique em **Code → Codespaces → Create codespace on main**.
2. Aguarde o container iniciar (instalará extensões e Python).

### B. (Opcional) Arquivos para automação
Crie a pasta `.devcontainer/` com `devcontainer.json` para instalar deps automaticamente ao abrir:

**`.devcontainer/devcontainer.json`**
```json
{
  "name": "QRCode Generator",
  "image": "mcr.microsoft.com/devcontainers/python:3.11",
  "postCreateCommand": "pip install -r requirements.txt",
  "customizations": {
    "vscode": { "extensions": ["ms-python.python"] }
  },
  "remoteUser": "vscode"
}
```

> Adicione também o script Linux **`run_qrcode.sh`** (já incluso no repo; se não estiver, crie-o):  
**`run_qrcode.sh`**
```bash
#!/bin/bash
set -e
if [ -z "$1" ]; then
  echo "Uso: ./run_qrcode.sh <URL> <FORMATO>"; exit 1
fi
URL=$1
FORMAT=${2:-jpg}
if [ ! -d ".venv" ]; then python -m venv .venv; fi
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python gerador_qr_code.py "$URL" "$FORMAT"
echo "Saída: output/qrcode_logo.$FORMAT"
```

Torne o script executável (apenas 1 vez):
```bash
chmod +x run_qrcode.sh
```

### C. Executar no terminal do Codespaces
```bash
./run_qrcode.sh http://exemplo.com svg
```
Saída em `output/qrcode_logo.svg`.

### D. Dicas Codespaces
- Para rodar automaticamente após criar o container, adicione ao `devcontainer.json`:
  ```json
  "postCreateCommand": "pip install -r requirements.txt && chmod +x run_qrcode.sh"
  ```
- Para depurar, abra o terminal integrado (**Ctrl+`**) e rode os comandos manualmente.

---

## 🇪🇸 Español

### 📘 Descripción
Herramienta en Python para generar **Códigos QR personalizados** (`JPG`, `BMP`, `SVG`) con un **cuadro central blanco** para insertar el **logo de la empresa**.

### 🪟 Paso a paso — Windows
1. Clonar:
   ```bat
   git clone https://github.com/SU_USUARIO/python-qrcode-logo-generator.git
   cd python-qrcode-logo-generator
   ```
2. Ejecutar:
   ```bat
   gerador_qr_code.bat <URL> <FORMATO>
   ```
   Ej.: `gerador_qr_code.bat http://ejemplo.com jpg`  
   Salida: `output/qrcode_logo.<formato>`

> En Git Bash use: `cmd.exe /c gerador_qr_code.bat ...`

### ☁️ Paso a paso — GitHub Codespaces
1. Crear Codespace: **Code → Codespaces → Create codespace on main**.
2. Dar permisos al script y ejecutar:
   ```bash
   chmod +x run_qrcode.sh
   ./run_qrcode.sh http://ejemplo.com svg
   ```
   Salida: `output/qrcode_logo.svg`

---

## 🇬🇧 English

### 📘 Description
Python tool to generate **custom QR Codes** (`JPG`, `BMP`, `SVG`) with a **central white square** to place a **company logo**.

### 🪟 Step-by-step — Windows
1. Clone:
   ```bat
   git clone https://github.com/YOUR_USER/python-qrcode-logo-generator.git
   cd python-qrcode-logo-generator
   ```
2. Run:
   ```bat
   gerador_qr_code.bat <URL> <FORMAT>
   ```
   Example: `gerador_qr_code.bat http://example.com bmp`  
   Output: `output/qrcode_logo.<format>`

> In Git Bash use: `cmd.exe /c gerador_qr_code.bat ...`

### ☁️ Step-by-step — GitHub Codespaces
1. Create Codespace: **Code → Codespaces → Create codespace on main**.
2. Make script executable & run:
   ```bash
   chmod +x run_qrcode.sh
   ./run_qrcode.sh http://example.com svg
   ```
   Output: `output/qrcode_logo.svg`

---

## 📦 Dependências / Dependencies
```
Python 3.9+
pip install -r requirements.txt
```

## 📁 Estrutura
```
.
├─ gerador_qr_code.py
├─ gerador_qr_code.bat        # Windows
├─ run_qrcode.sh              # Linux/Codespaces
├─ requirements.txt
├─ .devcontainer/ (opcional)
└─ output/
```

## 🧩 Observações
- Para **SVG** com quadrado central, o script injeta um `<rect>` no SVG.
- Para **JPG/BMP**, o quadrado central é desenhado com PIL.
- Logs são gravados no console via `loguru`.

---

📄 Autor: Desenvolvedor Python Full Stack • Versão: 1.2.0 • Licença: MIT
