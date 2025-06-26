# hashcat

% password recovery, password cracking

#plateform/linux  #target/local  #cat/CRACKING/PASSWORD 

## Hashcat - Crack MD5 (Joomla/WordPress) with wordlist
```
hashcat -a 0 -m 400 <hash_file> <wordlist>
```

## Hashcat - Crack MD5 (Joomla/WordPress) with wordlist and rules
```
hashcat -a 0 -m 400 <hash_file> <wordlist> -r /usr/share/doc/hashcat/rules/best64.rule
```

## Hashcat - Crack Kerberos TGS-REP (13100) with wordlist
```
hashcat -m 13100 -a 0 <hash_file> <wordlist>
```

## Hashcat - Crack LM (3000) with wordlist
```
hashcat -m 3000 -a 0 <hash_file> <wordlist>
```

## Hashcat - Crack NTLM (1000) with wordlist
```
hashcat -m 1000 -a 0 <hash_file> <wordlist>
```

## Hashcat - Crack NetNTLMv1 (5500) with wordlist
```
hashcat -m 5500 -a 0 <hash_file> <wordlist>
```

## Hashcat - Crack NetNTLMv2 (5600) with wordlist
```
hashcat -m 5600 -a 0 <hash_file> <wordlist>
```

## Hashcat - Crack NetNTLMv2 (5600) with combination attack
```
hashcat -m 5600 -a 1 <hash_file> <custom_wordlist> <custom_wordlist>
```

## Hashcat - Generate wordlist using rules
```
cat keywords.txt | hashcat -r <rule_file> --stdout > ./<custom_wordlist>
```

= wordlist: /usr/share/wordlist/rockyou.lst
= rule_file: /usr/share/doc/hashcat/rules/best64.rule 
= custom_wordlist: myCustomWordlist.txt
