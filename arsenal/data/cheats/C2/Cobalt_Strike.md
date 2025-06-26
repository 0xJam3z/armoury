% cat/C2
# Cobalt Strike
## Basic Usage
### Start Teamserver
```
./teamserver <external_ip> <password>
```
### Start Client
```
./cobaltstrike
```
## Beacons
### Generate Listener
```
listener http { ... }
```
### Generate Payload (HTTP Beacon)
```
windows/beacon_http/reverse_http
```
### Generate Payload (HTTPS Beacon)
```
windows/beacon_https/reverse_https
```
### Generate Payload (DNS Beacon)
```
windows/beacon_dns/reverse_dns
```
### Generate Payload (SMB Beacon)
```
windows/beacon_smb/reverse_smb
```
