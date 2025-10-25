
# 🧩 Gerador de QR Code com Espaço para Logo / QR Code Generator with Logo Space / Generador de QR con Espacio para Logo

## 🇧🇷 Português

### 📘 Descrição
Este projeto gera **QR Codes personalizados** em diferentes formatos (`JPG`, `BMP`, `SVG`) com um **espaço central branco** destinado à inserção de um **logo da empresa**.

Ideal para uso corporativo, impressão, marketing e materiais digitais.

---

### ⚙️ Funcionalidades
- Gera QR Codes a partir de qualquer URL.
- Adiciona um quadrado central proporcional (para logo).
- Suporte a formatos: **JPG, BMP, SVG**.
- Cria automaticamente um ambiente virtual Python (`.venv`).
- Script `.bat` automatizado para Windows.
- Log detalhado do processo com `loguru`.

---

### 🧰 Requisitos

```bash
Python 3.9+
pip install -r requirements.txt
```

---

### 🚀 Execução Rápida

```bash
gerador_qr_code.bat <URL> <FORMATO>
```

**Exemplo:**  
```bash
gerador_qr_code.bat http://nao-por-acaso.blogspot.com svg
```

---

### 📁 Estrutura do Projeto

```
gerador_qr_code/
│
├── gerador_qr_code.py
├── gerador_qr_code.bat
├── requirements.txt
├── README.md
└── output/
```

---

### 🧩 Saída

O arquivo final será gerado em:
```
output/qrcode_logo.<formato>
```

---

## 🇪🇸 Español

### 📘 Descripción
Este proyecto genera **Códigos QR personalizados** en varios formatos (`JPG`, `BMP`, `SVG`) con un **cuadro central blanco** para insertar un **logo de empresa**.

Ideal para marketing, impresión y material digital.

---

### ⚙️ Características
- Genera códigos QR desde cualquier URL.
- Añade un cuadro central proporcional (para el logo).
- Formatos compatibles: **JPG, BMP, SVG**.
- Crea un entorno virtual Python automáticamente (`.venv`).
- Script `.bat` automatizado para Windows.
- Registro detallado con `loguru`.

---

### 🧰 Requisitos

```bash
Python 3.9+
pip install -r requirements.txt
```

---

### 🚀 Ejecución rápida

```bash
gerador_qr_code.bat <URL> <FORMATO>
```

**Ejemplo:**  
```bash
gerador_qr_code.bat http://nao-por-acaso.blogspot.com svg
```

---

### 📁 Estructura del Proyecto

```
gerador_qr_code/
│
├── gerador_qr_code.py
├── gerador_qr_code.bat
├── requirements.txt
├── README.md
└── output/
```

---

### 🧩 Salida

El archivo final se generará en:
```
output/qrcode_logo.<formato>
```

---

## 🇬🇧 English

### 📘 Description
This project generates **custom QR Codes** in multiple formats (`JPG`, `BMP`, `SVG`) with a **central white square** to insert your **company logo**.

Perfect for corporate, print, and digital marketing materials.

---





> **Este README no final mostra como USAR** (Windows e GitHub Codespaces).  
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

