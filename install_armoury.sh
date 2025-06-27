#!/usr/bin/env bash
# Armoury one-shot installer (non-native-to-Kali tools)
# ----------------------------------------------------------------------
set -euo pipefail

########################
# 0. prerequisites
########################
sudo apt-get update -y
sudo apt-get install -y --no-install-recommends \
  python3-venv python3-pip git build-essential curl wget unzip jq \
  golang-go default-jdk-headless                                          \
  bloodhound redis-tools ldap-utils oscanner postgresql-client            \
  samba-client rpcbind tightvncviewer freerdp2-x11 x11-utils              \
  smbclient sqsh nfs-common samba-common-bin

########################
# 1. python virtual-env
########################
python3 -m venv ~/armoury-venv
source ~/armoury-venv/bin/activate
python -m pip install --upgrade pip wheel
pip install --upgrade -r requirements.txt

########################
# 2. extra deps for PKINITtools
########################
# (impacket & minikerberos are already installed above)
pip install -I git+https://github.com/wbond/oscrypto.git

########################
# 3. Go-based tools
########################
export GOBIN="$HOME/armoury-venv/bin"
go install github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
go install github.com/sensepost/gowitness@latest
go install github.com/ffuf/ffuf@latest
go install github.com/OJ/gobuster/v3@latest
go install github.com/ropnop/kerbrute@latest
go install github.com/BishopFox/sliver/client@latest

########################
# 4. git-only / script tools
########################
EXT="${HOME}/armoury-venv/ext"; mkdir -p "${EXT}"

## 4-a PyWhisker
git clone -q https://github.com/ShutdownRepo/pywhisker "${EXT}/pywhisker"
pip install -r "${EXT}/pywhisker/requirements.txt"
python "${EXT}/pywhisker/setup.py" install
# entry-point is installed by setup.py; nothing to symlink

## 4-b PKINITtools (gettgtpkinit.py, getNThash)
git clone -q https://github.com/dirkjanm/PKINITtools "${EXT}/PKINITtools"
ln -sf "${EXT}/PKINITtools/gettgtpkinit.py" ~/armoury-venv/bin/gettgtpkinit.py
ln -sf "${EXT}/PKINITtools/getNThash.py"    ~/armoury-venv/bin/getNThash

## 4-c Coercer + machine_account_coerce_abuse helper
git clone -q https://github.com/p0dalirius/Coercer "${EXT}/Coercer-src"
ln -sf "${EXT}/Coercer-src/tools/machine_account_coerce_abuse.py" \
       ~/armoury-venv/bin/machine_account_coerce_abuse

## 4-d EyeWitness
git clone -q https://github.com/RedSiege/EyeWitness "${EXT}/EyeWitness"
ln -sf "${EXT}/EyeWitness/EyeWitness.py" ~/armoury-venv/bin/eyewitness

## 4-e Havoc C2 framework
git clone -q https://github.com/HavocFramework/Havoc "${EXT}/Havoc"

## 4-f Tplmap
git clone -q https://github.com/epinna/tplmap "${EXT}/tplmap"
ln -sf "${EXT}/tplmap/tplmap.py" ~/armoury-venv/bin/tplmap

########################
# 5. odds & ends jars / binaries
########################
BIN="$HOME/armoury-venv/bin"

# ysoserial (Java)
wget -qO "$BIN/ysoserial.jar" \
  https://jitpack.io/com/github/frohoff/ysoserial/master-SNAPSHOT/ysoserial-master-SNAPSHOT.jar
chmod +x "$BIN/ysoserial.jar"

# ysoserial.net
wget -qO "$BIN/ysoserial.net" \
  https://github.com/pwntester/ysoserial.net/releases/latest/download/ysoserial.net
chmod +x "$BIN/ysoserial.net"

# Rubeus (Windows-side helper, convenient to keep around)
wget -qO "$BIN/Rubeus.exe" \
  https://github.com/GhostPack/Rubeus/releases/latest/download/Rubeus.exe

echo -e "\n[+] Armoury installation complete."
echo    "[*] Activate the toolkit with:  source ~/armoury-venv/bin/activate"
