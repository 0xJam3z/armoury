#!/usr/bin/env bash
# Armoury one-shot installer – multi-arch (AMD64 + ARM64)
set -euo pipefail

########################
# 0. detect architecture
########################
ARCH="$(dpkg --print-architecture)"   # amd64 | arm64 | armhf …
echo "[*] Detected architecture: ${ARCH}"

########################
# 1. apt prerequisites
########################
sudo apt-get update -y

# Common packages for both arches — keep this short
COMMON_PKGS=(
  python3-venv python3-pip git build-essential curl wget unzip jq
  golang-go default-jdk-headless
  bloodhound redis-tools ldap-utils oscanner postgresql-client
  smbclient rpcbind nfs-common samba-common-bin x11-utils
)

# Viewers / GUI helpers – arch-specific
AMD_PKGS=(tightvncviewer freerdp2-x11)
ARM_PKGS=(tigervnc-viewer remmina)   # substitutes available in Kali ARM repo

case "$ARCH" in
  amd64) sudo apt-get install -y --no-install-recommends "${COMMON_PKGS[@]}" "${AMD_PKGS[@]}";;
  arm64|armhf) sudo apt-get install -y --no-install-recommends "${COMMON_PKGS[@]}" "${ARM_PKGS[@]}";;
  *) echo "[!] Unknown arch (${ARCH}) – installing common set only"; sudo apt-get install -y --no-install-recommends "${COMMON_PKGS[@]}";;
esac

########################
# 2. python virtual-env
########################
if [[ ! -d "$HOME/armoury-venv" ]]; then
  python3 -m venv "$HOME/armoury-venv"
fi
# shellcheck source=/dev/null
source "$HOME/armoury-venv/bin/activate"
python -m ensurepip --upgrade
python -m pip install --upgrade pip wheel

# Ensure core runtime deps (docutils etc.) in case user skipped pip install -r …
if [[ -f requirements.txt ]]; then
  pip install --upgrade -r requirements.txt
fi

########################
# 3. extra deps for PKINITtools & Certipy
########################
pip install -I git+https://github.com/wbond/oscrypto.git
pip install certipy-ad   # <-- Certipy

########################
# 4. Go-based tools
########################
export GOBIN="$HOME/armoury-venv/bin"
go install github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
go install github.com/sensepost/gowitness@latest
go install github.com/ffuf/ffuf@latest
go install github.com/OJ/gobuster/v3@latest
go install github.com/ropnop/kerbrute@latest          # <-- Kerbrute
go install github.com/BishopFox/sliver/client@latest

########################
# 5. git-only / script tools
########################
EXT="$HOME/armoury-venv/ext"; mkdir -p "$EXT"

# 5-a PyWhisker
if [[ ! -d "$EXT/pywhisker" ]]; then
  git clone -q https://github.com/ShutdownRepo/pywhisker "$EXT/pywhisker"
  pip install -r "$EXT/pywhisker/requirements.txt"
  python "$EXT/pywhisker/setup.py" install
fi

# 5-b PKINITtools
if [[ ! -d "$EXT/PKINITtools" ]]; then
  git clone -q https://github.com/dirkjanm/PKINITtools "$EXT/PKINITtools"
fi
ln -sf "$EXT/PKINITtools/gettgtpkinit.py" "$HOME/armoury-venv/bin/gettgtpkinit.py"
ln -sf "$EXT/PKINITtools/getNThash.py"    "$HOME/armoury-venv/bin/getNThash"

# 5-c Coercer helper
if [[ ! -d "$EXT/Coercer-src" ]]; then
  git clone -q https://github.com/p0dalirius/Coercer "$EXT/Coercer-src"
fi
ln -sf "$EXT/Coercer-src/tools/machine_account_coerce_abuse.py" \
       "$HOME/armoury-venv/bin/machine_account_coerce_abuse"

# 5-d EyeWitness
if [[ ! -d "$EXT/EyeWitness" ]]; then
  git clone -q https://github.com/RedSiege/EyeWitness "$EXT/EyeWitness"
fi
ln -sf "$EXT/EyeWitness/EyeWitness.py" "$HOME/armoury-venv/bin/eyewitness"

# 5-e Havoc C2
if [[ ! -d "$EXT/Havoc" ]]; then
  git clone -q https://github.com/HavocFramework/Havoc "$EXT/Havoc"
fi

# 5-f Tplmap
if [[ ! -d "$EXT/tplmap" ]]; then
  git clone -q https://github.com/epinna/tplmap "$EXT/tplmap"
fi
ln -sf "$EXT/tplmap/tplmap.py" "$HOME/armoury-venv/bin/tplmap"

########################
# 6. odds & ends jars / binaries
########################
BIN="$HOME/armoury-venv/bin"
mkdir -p "$BIN"

wget -qO "$BIN/ysoserial.jar" https://jitpack.io/com/github/frohoff/ysoserial/master-SNAPSHOT/ysoserial-master-SNAPSHOT.jar
chmod +x "$BIN/ysoserial.jar"

wget -qO "$BIN/ysoserial.net" https://github.com/pwntester/ysoserial.net/releases/latest/download/ysoserial.net
chmod +x "$BIN/ysoserial.net"

wget -qO "$BIN/Rubeus.exe" https://github.com/GhostPack/Rubeus/releases/latest/download/Rubeus.exe

echo -e \"\\n[+] Armoury installation complete.\"
echo    \"[*] Activate with: source ~/armoury-venv/bin/activate\"
