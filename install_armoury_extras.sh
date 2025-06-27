#!/usr/bin/env bash
# install_armoury_extras.sh
# ────────────────────────────────────────────────────────────────
# Installs / fixes:  Certipy • Kerbrute • PKINITtools • PyWhisker
# Works on both ARM64 and AMD64 Kali.  Run INSIDE the armoury venv.
set -euo pipefail

# ───────────────────────── 0. Preconditions ─────────────────────────
if [[ -z "${VIRTUAL_ENV:-}" ]]; then
  echo "[!] Please 'source ~/armoury-venv/bin/activate' first." >&2
  exit 1
fi

BIN="$VIRTUAL_ENV/bin"
EXT="$VIRTUAL_ENV/ext"
mkdir -p "$BIN" "$EXT"

python -m ensurepip --upgrade
python -m pip install --upgrade pip wheel

# ───────────────────────── 1. Certipy (pip) ─────────────────────────
pip install --upgrade certipy-ad

# ───────────────────────── 2. Go cache inside venv ──────────────────
export GOPATH="$VIRTUAL_ENV/go"
export GOMODCACHE="$GOPATH/pkg/mod"
export GOCACHE="$GOPATH/cache"
export GOBIN="$BIN"
mkdir -p "$GOMODCACHE" "$GOCACHE" "$GOBIN"

# ───────────── 2a. Kerbrute via go install  (with fallback) ─────────
echo "[*] Installing Kerbrute…"
if ! go install github.com/ropnop/kerbrute@latest 2>/dev/null; then
  echo "[!] go install failed – fetching pre-built binary."
  ARCH=$(uname -m)
  case "$ARCH" in
    aarch64|arm64) KB_URL="https://github.com/ropnop/kerbrute/releases/latest/download/kerbrute_linux_arm64";;
    x86_64|amd64)  KB_URL="https://github.com/ropnop/kerbrute/releases/latest/download/kerbrute_linux_amd64";;
    *) echo "[!] Unknown arch $ARCH – skipping Kerbrute."; KB_URL="";;
  esac
  if [[ -n "$KB_URL" ]]; then
    curl -sSL "$KB_URL" -o "$BIN/kerbrute" && chmod +x "$BIN/kerbrute"
  fi
fi

# ─────────────────── 3. PKINITtools (+dependencies) ─────────────────
echo "[*] Installing PKINITtools…"
pip install --upgrade impacket minikerberos
pip install -I git+https://github.com/wbond/oscrypto.git

if [[ ! -d "$EXT/PKINITtools" ]]; then
  git clone -q https://github.com/dirkjanm/PKINITtools "$EXT/PKINITtools"
fi
ln -sf "$EXT/PKINITtools/gettgtpkinit.py" "$BIN/gettgtpkinit.py"
ln -sf "$EXT/PKINITtools/getNThash.py"    "$BIN/getNThash"

# ───────────────────── 4. PyWhisker (git + setup.py) ────────────────
echo "[*] Installing PyWhisker…"
if [[ ! -d "$EXT/pywhisker" ]]; then
  git clone -q https://github.com/ShutdownRepo/pywhisker "$EXT/pywhisker"
fi
pip install -r "$EXT/pywhisker/requirements.txt"
python "$EXT/pywhisker/setup.py" install  # installs the 'pywhisker' entry-point

# ──────────────────────── 5. Success banner ────────────────────────
echo -e "\n[✓] Extras ready in $VIRTUAL_ENV/bin :"
printf "  • %s\n" \
  "$(command -v certipy   || echo 'certipy (missing)')" \
  "$(command -v kerbrute  || echo 'kerbrute (missing)')" \
  "$(command -v gettgtpkinit.py || echo 'gettgtpkinit.py (missing)')" \
  "$(command -v getNThash || echo 'getNThash (missing)')" \
  "$(command -v pywhisker || echo 'pywhisker (missing)')"
