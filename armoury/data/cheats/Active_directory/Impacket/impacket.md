# Impacket

% impacket, windows, smb, 445

## lookupsid - SID User Enumeration
Extracts information about existing users and their SIDs.
#plateform/linux #target/remote #cat/RECON 

```
lookupsid.py <domain>/<user>:<password_or_hash>@<rhost>
```

## reg.py - Query remote registry information
Queries registry information on a remote host.
#plateform/linux #target/remote #cat/RECON 
```
reg.py <domain>/<user>:<password_or_hash>@<rhost> query -keyName HKLM\SOFTWARE\Policies\Microsoft\Windows -s
```

## rpcdump.py - List RPC endpoints
Lists RPC endpoints on a remote host.
#plateform/linux #target/remote #cat/RECON 
```
rpcdump.py <domain>/<user>:<password_or_hash>@<rhost>
```

## services.py - Remote service management
Manages services on a remote host (start, stop, delete, read status, config, list, create, change).
#plateform/linux #target/remote #cat/RECON  #cat/ATTACK/EXPLOIT  
```
services.py <domain>/<user>:<password_or_hash>@<rhost> <action>
``` 

## getArch.py - Find target architecture
Determines if the target system is 64 or 32-bit.
#plateform/linux #target/remote #cat/RECON 
```
getArch.py -target <rhost>
```

## netview.py - Network enumeration tool
Enumerates shares, sessions, and logged-on users. Requires DNS to be set up.
#plateform/linux #target/remote #cat/RECON 
```
netview.py <domain>/<user>:<password_or_hash> -target <rhost> -users <users.txt>
```


