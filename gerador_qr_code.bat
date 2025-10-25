
@echo off
setlocal

REM ==========================================
REM Gerador de QR Code - Pass-through CLI
REM Nao faz parsing aqui. Tudo vai direto pro Python.
REM Ex.: gerador_qr_code.bat --url=http://site --filetype=png --squareratio=33 --squarecolor=black --size=900
REM ==========================================

REM Cria .venv se nao existir
if not exist ".venv" (
  echo [setup] Criando ambiente virtual .venv...
  py -m venv .venv 2>nul || python -m venv .venv
)

REM Ativa venv
call .venv\Scripts\activate.bat

REM Dependencias
python -m pip install --upgrade pip >nul
pip install -r requirements.txt >nul

REM Repassa TODOS os parametros crus para o Python
python gerador_qr_code.py %*

endlocal
