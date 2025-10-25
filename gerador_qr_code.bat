@echo off
setlocal enabledelayedexpansion

REM ======================================================
REM Script: gerador_qr_code.bat
REM Descrição: Cria venv, instala dependências e gera QRCode.
REM Uso: gerador_qr_code.bat <URL> <FORMATO>
REM Exemplo: gerador_qr_code.bat http://nao-por-acaso.blogspot.com svg
REM ======================================================

if "%~1"=="" (
    echo Uso: gerador_qr_code.bat ^<URL^> ^<FORMATO^>
    echo Exemplo: gerador_qr_code.bat http://exemplo.com jpg
    exit /b 1
)

set URL=%~1
set FORMATO=%~2

if "%FORMATO%"=="" (
    set FORMATO=jpg
)

echo ==========================================
echo Gerador de QRCode - Ambiente Python Virtual
echo ==========================================

if not exist ".venv" (
    echo Criando ambiente virtual...
    python -m venv .venv
)

echo Ativando ambiente virtual...
call .venv\Scripts\activate.bat

echo Instalando dependencias...
python -m pip install --upgrade pip >nul
pip install -r requirements.txt >nul

echo Gerando QRCode...
python gerador_qr_code.py %URL% %FORMATO%

echo.
echo ==========================================
echo QRCode gerado com sucesso!
echo Formato: %FORMATO%
echo ==========================================

endlocal
pause
