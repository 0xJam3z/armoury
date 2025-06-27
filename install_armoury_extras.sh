#!/usr/bin/env bash
# install_armoury_extras.sh
# Installs / repairs:  Certipy · Kerbrute · PKINITtools · PyWhisker
# Works on both ARM64 and AMD64 Kali, idempotent & disk-space-aware.
# ---------------------------------------------------------------
set -euo pipefail

### 0. Preconditions ─────────────────────────────────────────────
if [[ -z "${VIRTUAL_ENV:-}" ]]; then
  echo "[!] Please 'source ~/armoury-venv/bin/activate' first." >&2
  exit 1
fi

BIN="${VIRTUAL_ENV}/bin"
EXT="${VIRTUAL_ENV}/ext"
mkdir -p "$BIN" "$EXT"

python -m ensurepip --upgrade     # make sure pip exists
python -m pip install --upgrade pip wheel

### 1. Certipy (pure-pip) ───────────────────────────────────────
pip install --upgrade certipy-ad

### 2. Relocate Go cache inside the venv (saves $HOME space) ────
export GOPATH="$VIRTUAL_ENV/go"
export GOMODCACHE="$GOPATH/pkg/mod"
export GOCACHE="$GOPATH/cache"
export GOBIN="$BIN"
mkdir -p "$GOMODCACHE" "$GOCACHE" "$GOBIN"

### 3. Kerbrute ─ try Go build first, fall back to binary drop ‐──
echo "[*] Installing Kerbrute…"
if ! go install github.com/ropnop/kerbrute@latest 2>/dev/null; then
  echo "[!] go install failed (likely disk space) – fetching pre-built."
  ARCH=$(uname -m)
  case "$ARCH" in
    aarch64|arm64) KB_URL="https://github.com/ropnop/kerbrute/releases/latest/download/kerbrute_linux_arm64" ;;
    x86_64|amd64)  KB_URL="https://github.com/ropnop/kerbrute/releases/latest/download/kerbrute_linux_amd64" ;;
    *)             KB_URL="" ;;
  esac
  if [[ -n "$KB_URL" ]]; then
    curl -sSL "$KB_URL" -o "$BIN/kerbrute" && chmod +x "$BIN/kerbrute"
  else
    echo "[!] Unsupported arch ($ARCH) – Kerbrute skipped." >&2
  fi
fi

### 4. PKINITtools (+ deps) ─────────────────────────────────────
echo "[*] Installing PKINITtools…"
pip install --upgrade impacket minikerberos
pip install -I git+https://github.com/wbond/oscrypto.git

if [[ ! -d "$EXT/PKINITtools" ]]; then
  git clone -q https://github.com/dirkjanm/PKINITtools "$EXT/PKINITtools"
fi
ln -sf "$EXT/PKINITtools/gettgtpkinit.py" "$BIN/gettgtpkinit.py"
ln -sf "$EXT/PKINITtools/getNThash.py"    "$BIN/getNThash"

### 5. PyWhisker ────────────────────────────────────────────────
echo "[*] Installing PyWhisker…"
if [[ ! -d "$EXT/pywhisker" ]]; then
  git clone -q https://github.com/ShutdownRepo/pywhisker "$EXT/pywhisker"
fi
pip install -r "$EXT/pywhisker/requirements.txt"
python "$EXT/pywhisker/setup.py" install   # adds the ‘pywhisker’ entry-point

### 6. Verification banner ─────────────────────────────────────
echo -e "\n[✓] Extras available in $BIN :"
for CMD in certipy kerbrute gettgtpkinit.py getNThash pywhisker; do
  if command -v "$CMD" &>/dev/null; then
    printf "  • %-18s → %s\n" "$CMD" "$(command -v "$CMD" | sed "s#${HOME}/##")"
  else
    printf "  • %-18s   (missing!)\n" "$CMD"
  fi
done
