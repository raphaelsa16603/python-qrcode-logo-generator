
# 🧩 Gerador de QR Code com Espaço para Logo / QR Code Generator with Logo Space / Generador de QR con Espacio para Logo

> **Este README mostra apenas COMO USAR** (Windows e GitHub Codespaces).  
> Os arquivos e scripts já estão no repositório.

---

## 🚀 Quick Start (PT/ES/EN)

- **Windows (.BAT):**
  ```bat
  gerador_qr_code.bat <URL> <FORMATO>
  ```
  Ex.: `gerador_qr_code.bat http://nao-por-acaso.blogspot.com svg`

- **GitHub Codespaces / Linux (.SH):**
  ```bash
  ./run_qrcode.sh <URL> <FORMATO>
  ```
  Ej.: `./run_qrcode.sh http://nao-por-acaso.blogspot.com jpg`

**Formatos suportados / Supported formats / Formatos soportados:** `jpg`, `bmp`, `svg`  
**Saída / Output / Salida:** `output/qrcode_logo.<formato>`

---

## 🇧🇷 Como usar no Windows (CMD/PowerShell)

1) **Abrir terminal na raiz do projeto** (onde estão `gerador_qr_code.bat` e `requirements.txt`).  
2) **Executar:**
   ```bat
   gerador_qr_code.bat <URL> <FORMATO>
   ```
   **Exemplos:**
   ```bat
   gerador_qr_code.bat https://minhaempresa.com.br jpg
   gerador_qr_code.bat http://nao-por-acaso.blogspot.com svg
   ```
3) **Resultado:** arquivo gerado em `output/qrcode_logo.<formato>`.

> 💡 Dica: Se estiver no **Git Bash**, rode via `cmd.exe /c gerador_qr_code.bat ...`.

---

## ☁️ Como usar no GitHub Codespaces

1) **Abrir o Codespace** deste repositório (Code → Codespaces → *Open*).  
2) **No terminal do Codespaces, na raiz do projeto**, execute:
   ```bash
   ./run_qrcode.sh <URL> <FORMATO>
   ```
   **Exemplos:**
   ```bash
   ./run_qrcode.sh https://minhaempresa.com.br bmp
   ./run_qrcode.sh http://nao-por-acaso.blogspot.com svg
   ```
3) **Resultado:** arquivo gerado em `output/qrcode_logo.<formato>`.

> 🔐 Na primeira vez, se necessário, torne o script executável: `chmod +x run_qrcode.sh`.

---

## 🇪🇸 Uso en Windows (CMD/PowerShell)

1) **Abra la terminal** en la carpeta del proyecto.  
2) **Ejecute:**
   ```bat
   gerador_qr_code.bat <URL> <FORMATO>
   ```
   **Ejemplos:**
   ```bat
   gerador_qr_code.bat https://miempresa.com jpg
   gerador_qr_code.bat http://nao-por-acaso.blogspot.com svg
   ```
3) **Salida:** `output/qrcode_logo.<formato>`

> 💡 En **Git Bash**: `cmd.exe /c gerador_qr_code.bat ...`

---

## ☁️ Uso en GitHub Codespaces

1) **Abra el Codespace** de este repo.  
2) **En la terminal del Codespace**, ejecute:
   ```bash
   ./run_qrcode.sh <URL> <FORMATO>
   ```
   **Ejemplos:**
   ```bash
   ./run_qrcode.sh https://miempresa.com bmp
   ./run_qrcode.sh http://nao-por-acaso.blogspot.com svg
   ```
3) **Salida:** `output/qrcode_logo.<formato>`

> 🔐 Primera vez: `chmod +x run_qrcode.sh` si hace falta.

---

## 🇬🇧 Usage on Windows (CMD/PowerShell)

1) **Open a terminal** in the project root.  
2) **Run:**
   ```bat
   gerador_qr_code.bat <URL> <FORMAT>
   ```
   **Examples:**
   ```bat
   gerador_qr_code.bat https://mycompany.com jpg
   gerador_qr_code.bat http://nao-por-acaso.blogspot.com svg
   ```
3) **Output:** `output/qrcode_logo.<format>`

> 💡 On **Git Bash**: `cmd.exe /c gerador_qr_code.bat ...`

---

## ☁️ Usage in GitHub Codespaces

1) **Open the Codespace** for this repo.  
2) **In the terminal**, run:
   ```bash
   ./run_qrcode.sh <URL> <FORMAT>
   ```
   **Examples:**
   ```bash
   ./run_qrcode.sh https://mycompany.com bmp
   ./run_qrcode.sh http://nao-por-acaso.blogspot.com svg
   ```
3) **Output:** `output/qrcode_logo.<format>`

> 🔐 First time: `chmod +x run_qrcode.sh` if required.

---

### Notas / Notes / Notas
- SVG: o script injeta um `<rect>` central (placeholder do logo).  
- JPG/BMP: o quadrado é desenhado com PIL.  
- Logs: exibidos no terminal via `loguru`.

