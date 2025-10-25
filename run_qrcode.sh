
#!/bin/bash
set -e

show_help() {
  cat <<'EOF'
Uso:
  run_qrcode.sh --url=URL [--filetype=jpg|bmp|png|svg] [--squareratio=25] [--squarecolor=white] [--size=600]
  run_qrcode.sh URL FORMATO   (modo legado)
EOF
}

URL=""; FILETYPE=""; SQUARERATIO=""; SQUARECOLOR=""; SIZE=""
OTHER=()

for arg in "$@"; do
  case "$arg" in
    -h|--help) show_help; exit 0 ;;
    --url=*) URL="${arg#*=}" ;;
    --filetype=*) FILETYPE="${arg#*=}" ;;
    --squareratio=*) SQUARERATIO="${arg#*=}" ;;
    --squarecolor=*) SQUARECOLOR="${arg#*=}" ;;
    --size=*) SIZE="${arg#*=}" ;;
    *) OTHER+=("$arg") ;;
  esac
done

if [ -z "$URL" ] && [ "${#OTHER[@]}" -ge 1 ]; then URL="${OTHER[0]}"; fi
if [ -z "$FILETYPE" ] && [ "${#OTHER[@]}" -ge 2 ]; then FILETYPE="${OTHER[1]}"; fi

if [ -z "$URL" ]; then echo "ERRO: URL obrigatoria."; show_help; exit 1; fi
: "${FILETYPE:=jpg}"; : "${SQUARERATIO:=25}"; : "${SQUARECOLOR:=white}"; : "${SIZE:=600}"

if [ ! -d ".venv" ]; then python3 -m venv .venv; fi
source .venv/bin/activate
python -m pip install --upgrade pip >/dev/null
pip install -r requirements.txt >/dev/null

python gerador_qr_code.py --url="$URL" --filetype="$FILETYPE" --squareratio="$SQUARERATIO" --squarecolor="$SQUARECOLOR" --size="$SIZE"
echo "Saida: output/qrcode_logo.$FILETYPE"
