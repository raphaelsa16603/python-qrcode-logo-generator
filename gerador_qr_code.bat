
@echo off
setlocal enabledelayedexpansion

for %%A in (%*) do (
  if /I "%%~A"=="-h" set HELP=1
  if /I "%%~A"=="--help" set HELP=1
)
if defined HELP (
  echo Uso:
  echo   gerador_qr_code.bat --url=URL --filetype=jpg^|bmp^|png^|svg --squareratio=25 --squarecolor=white --size=600
  echo   gerador_qr_code.bat URL FORMATO
  exit /b 0
)

set "URL="
set "FILETYPE="
set "SQUARERATIO="
set "SQUARECOLOR="
set "SIZE="

for %%A in (%*) do (
  for /F "tokens=1,2 delims==" %%K in ("%%~A") do (
    set "K=%%~K"
    set "V=%%~L"
    if /I "!K!"=="--url" set "URL=!V!"
    if /I "!K!"=="--filetype" set "FILETYPE=!V!"
    if /I "!K!"=="--squareratio" set "SQUARERATIO=!V!"
    if /I "!K!"=="--squarecolor" set "SQUARECOLOR=!V!"
    if /I "!K!"=="--size" set "SIZE=!V!"
  )
)

if not defined URL (
  if not "%~1"=="" set "URL=%~1"
  if not "%~2"=="" set "FILETYPE=%~2"
)

if not defined URL (
  echo ERRO: URL obrigatoria. Use --help para exemplos.
  exit /b 1
)

if not defined FILETYPE set "FILETYPE=jpg"
if not defined SQUARERATIO set "SQUARERATIO=25"
if not defined SQUARECOLOR set "SQUARECOLOR=white"
if not defined SIZE set "SIZE=600"

if not exist ".venv" (
  echo Criando ambiente virtual...
  py -m venv .venv 2>nul || python -m venv .venv
)
call .venv\Scripts\activate.bat

python -m pip install --upgrade pip >nul
pip install -r requirements.txt >nul

python gerador_qr_code.py --url="%URL%" --filetype="%FILETYPE%" --squareratio=%SQUARERATIO% --squarecolor="%SQUARECOLOR%" --size=%SIZE%

echo Saida: output\qrcode_logo.%FILETYPE%
endlocal
