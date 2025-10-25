
# 🧩 Gerador de QR Code com Espaço para Logo / QR Code Generator with Logo Space / Generador de QR con Espacio para Logo

---

## 🚀 **AGORA É MAIS FÁCIL — SUPORTE A FLAGS (Windows, Linux e Codespaces)**

Este projeto agora permite definir **todos os parâmetros** diretamente pela linha de comando usando **flags modernas**!  
Exemplo rápido:

### 🪟 Windows (CMD ou PowerShell)
```bat
gerador_qr_code.bat --url=http://nao-por-acaso.blogspot.com --filetype=jpg --squareratio=30 --squarecolor=white --size=600
```

### 🐧 Linux / GitHub Codespaces
```bash
./run_qrcode.sh --url=http://nao-por-acaso.blogspot.com --filetype=svg --squareratio=25 --squarecolor=#FFFFFF --size=800
```

### 💡 Flags disponíveis
| Flag | Descrição | Tipo / Intervalo | Padrão |
|------|------------|------------------|---------|
| `--url` | URL a ser codificada no QRCode | texto | **Obrigatório** |
| `--filetype` | Formato do arquivo (`jpg`, `bmp`, `png`, `svg`) | texto | `jpg` |
| `--squareratio` | Percentual do quadrado central (0–90) | número (%) | `25` |
| `--squarecolor` | Cor do quadrado central (CSS ou HEX) | texto | `white` |
| `--size` | Tamanho da imagem (lado, em pixels) | número (50–5000) | `600` |

**Saída:** `output/qrcode_logo.<formato>`

---

## 🇧🇷 Português

### 📘 Descrição
Ferramenta em Python para gerar **QR Codes personalizados** em vários formatos (`JPG`, `BMP`, `PNG`, `SVG`) com um **quadrado central branco** para inserir o **logo da empresa**.

Ideal para marketing, impressão e uso corporativo.

---

### ⚙️ Funcionalidades
- Gera QR Codes a partir de qualquer URL.
- Adiciona um quadrado central proporcional (para logo).
- Suporte a formatos: **JPG, BMP, PNG, SVG**.
- Cria automaticamente um ambiente virtual Python (`.venv`).
- Scripts prontos para Windows e Linux (Codespaces).
- Log detalhado do processo com `loguru`.

---

### 🧰 Requisitos

```bash
Python 3.9+
pip install -r requirements.txt
```

---

### 🚀 Uso moderno (com flags)

#### 🪟 Windows
```bat
gerador_qr_code.bat --url=http://nao-por-acaso.blogspot.com --filetype=jpg --squareratio=30 --squarecolor=white --size=600
```

#### 🐧 Linux / GitHub Codespaces
```bash
./run_qrcode.sh --url=http://nao-por-acaso.blogspot.com --filetype=svg --squareratio=25 --squarecolor=#FFFFFF --size=800
```

#### 📘 Ajuda
```bash
gerador_qr_code.bat --help
./run_qrcode.sh --help
```

---

### 💾 Modo legado (compatível com versões antigas)

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
├── run_qrcode.sh
├── requirements.txt
├── README.md
└── output/
```

---

## 🇪🇸 Español

### 📘 Descripción
Este proyecto genera **Códigos QR personalizados** (`JPG`, `BMP`, `PNG`, `SVG`) con un **cuadro central blanco** para colocar un **logo**.

Ideal para marketing, impresión y uso corporativo.

---

### 🚀 Ejemplo de uso con flags

#### 🪟 Windows
```bat
gerador_qr_code.bat --url=http://nao-por-acaso.blogspot.com --filetype=jpg --squareratio=30 --squarecolor=white --size=600
```

#### 🐧 Linux / Codespaces
```bash
./run_qrcode.sh --url=http://nao-por-acaso.blogspot.com --filetype=svg --squareratio=25 --squarecolor=#FFFFFF --size=800
```

#### 🆘 Ayuda
```bash
gerador_qr_code.bat --help
./run_qrcode.sh --help
```

---

## 🇬🇧 English

### 📘 Description
Python tool to generate **custom QR Codes** (`JPG`, `BMP`, `PNG`, `SVG`) with a **central white square** for a company logo.

Ideal for corporate branding, printing, or marketing.

---

### 🚀 Example using flags

#### 🪟 Windows
```bat
gerador_qr_code.bat --url=http://nao-por-acaso.blogspot.com --filetype=jpg --squareratio=30 --squarecolor=white --size=600
```

#### 🐧 Linux / Codespaces
```bash
./run_qrcode.sh --url=http://nao-por-acaso.blogspot.com --filetype=svg --squareratio=25 --squarecolor=#FFFFFF --size=800
```

#### 🆘 Help
```bash
gerador_qr_code.bat --help
./run_qrcode.sh --help
```

---

### 🧩 Output
All generated QR Codes will be saved in:
```
output/qrcode_logo.<format>
```

---

📄 Autor: Raphael Simões Andrade - Desenvolvedor Full Stack .NET e Python 

📅 Versão: 2.0.0  
🔗 Licença: MIT  
🌐 Compatível com: Windows, Linux, GitHub Codespaces
