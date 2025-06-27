#!/usr/bin/env bash
#
# addalias.sh — append Armoury aliases to the user’s shell rc file
#   * Works for Bash or Zsh   (auto-detects via $SHELL)
#   * Idempotent              (won’t duplicate lines)
# --------------------------------------------------------------------

set -euo pipefail

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

ARMOURY_ALIAS="alias armoury=\"\$HOME/armoury/run\""
A_ALIAS="alias a='( source \"\$HOME/armoury-venv/bin/activate\" && armoury \"\$@\" )'"

# choose rc file
case "${SHELL##*/}" in
  zsh)   RC_FILE="$HOME/.zshrc"  ;;
  bash)  RC_FILE="$HOME/.bashrc" ;;
  *)     RC_FILE="$HOME/.bashrc" ;;  # default
esac

echo "[*] Adding aliases to ${RC_FILE}"

# ensure rc file exists
touch "${RC_FILE}"

# append if not already present
grep -qxF "${ARMOURY_ALIAS}" "${RC_FILE}" || echo "${ARMOURY_ALIAS}" >> "${RC_FILE}"
grep -qxF "${A_ALIAS}"        "${RC_FILE}" || echo "${A_ALIAS}"      >> "${RC_FILE}"

echo "[+] Done.  Run:  source ${RC_FILE}"
echo
echo "── Manual examples for other shells ──"
echo "fish  :  echo \"${ARMOURY_ALIAS}\" >> ~/.config/fish/config.fish"
echo "bash  :  echo \"${ARMOURY_ALIAS}\" >> ~/.bash_aliases  # if you prefer"
