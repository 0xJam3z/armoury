# Armoury

![](img/logo.png)
---

Armoury is a lightweight inventory, quick-access launcher, and command reference tool designed for penetration testers and red teamers.

![](img/armoury.gif)

---

## Credits & Contributions 
Armoury is a fork of the original [Arsenal](https://github.com/Orange-Cyberdefense/arsenal) project for more up-to-date and additional tools.
Authors of this project:
* 0xSA-X1
* 0xJam3z

Original Authors of [Arsenal](https://github.com/Orange-Cyberdefense/arsenal): 
* Guillaume Muh
* mayfly

---

# **New Features**

- Modernized color scheme and UI improvements
- GitHub-style clipboard notifications (top right, subtle, 1s)
- Default: **Copy command to clipboard** on Enter
- **Open command in a new terminal** with Space
- **Global variable management**: set, clear, and use variables like `<ip>`, `<lport>`, `<user>`, `<wordlist>`, etc.
- All global variables are persistent in `~/.armoury.json` (or `.armoury.json` in local mode)
- "Clear" command instantly wipes all global variables (no prompt)
- C2 Frameworks: Havoc, Cobalt Strike, Sliver
- bloodyAD with Bloodhound Edges: GenericAll, WriteOwner, ForceChangePassword, GenericWrite
- Installation scripts for all tools in Python venv
- Enumeration with `Find`
- Many new cheatsheets and tool integrations

---

## Installation

```sh
git clone https://github.com/0xJam3z/armoury.git
cd armoury
chmod +x install_armoury.sh 
chmod +x install_armoury_extras.sh
python3 -m venv ~/armoury-venv                  
source ~/armoury-venv/bin/activate
pip install -r requirements.txt 
pip install --no-binary :all: .
./install_armoury.sh
./install_armoury_extras.sh
./addalias.sh
```

Don't forget to `source`:
```sh
source ~/.bashrc
source ~/.zshrc
```

---

## Quick Start

Launch Armoury:
```sh
a
```
or
```sh
armoury
```

---

## Key Bindings

- **Enter**: Copy the selected command to clipboard (with notification)
- **Space**: Open the selected command in a new terminal window
- **Arrow keys**: Navigate the menu
- **Page Up/Page Down**: Scroll through the list
- **F10 or Esc**: Exit
- **Tab**: Autocomplete argument (where available)

---

## Global Variables

You can set and use global variables in any command. These are persistent and stored in `~/.armoury.json` (or `.armoury.json` in local mode).

### Setting a variable

```sh
>set ip=192.168.1.1
>set lport=4444
>set wordlist=/usr/share/wordlists/rockyou.txt
```

### Using variables

Any command with `<ip>`, `<lport>`, `<wordlist>`, etc. will automatically use your set values.

### Clearing all variables

Select the "Clear all global variables" entry in the menu, or type:
```sh
>clear
```
This will instantly wipe all global variables (no prompt).

---

## Add a Prefix To Commands

To prefix all commands (e.g., with `proxychains -q`):

```sh
>set armoury_prefix_cmd=proxychains -q
armoury -f
```

---

## Troubleshooting

(From [Arsenal](https://github.com/Orange-Cyberdefense/arsenal))

```
========== OSError ============
Armoury needs TIOCSTI enable for running
Please run the following commands as root to fix this issue on the current session :
sysctl -w dev.tty.legacy_tiocsti=1
If you want this workaround to survive a reboot,
add the following configuration to sysctl.conf file and reboot :
echo "dev.tty.legacy_tiocsti=1" >> /etc/sysctl.conf
More details about this bug here: https://github.com/0xJam3z/armoury/issues/77
```
