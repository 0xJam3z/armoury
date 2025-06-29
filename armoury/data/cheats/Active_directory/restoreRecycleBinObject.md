# Restoring Object from Recycle Bin (ESC5)

## 1. Find Object
```
Get-ADObject -Identity "<SID>"
```

## 2. Verify Feature
```
Get-ADOptionalFeature 'Recycle Bin Feature'
```

## 3. Find Specific Object
```
Get-ADObject -SearchBase "CN=Deleted Objects,DC=<DOMAIN>,DC=<DOMAIN_EXT>" -LDAPFilter "(objectClass=user)" -IncludeDeletedObjects -Properties objectSid, samAccountName, lastKnownParent, whenChanged
```

## 4. Get samAccountName
```
Get-ADObject -SearchBase "CN=Deleted Objects,DC=<DOMAIN>,DC=<DOMAIN_EXT>" -IncludeDeletedObjects -LDAPFilter "(samAccountName=<USERNAME>)"
```

## 5. Restore Object
```
Restore-ADObject -Identity '<GUID>'
```

## 6. Reset Password for Object
```
Set-ADAccountPassword -Identity '<USERNAME>' -Reset -NewPassword (ConvertTo-SecureString '<NEW_PASSWORD>' -AsPlainText -Force)
```

## 7. Enable Account
```
Enable-ADAccount -Identity '<USERNAME>'
```
