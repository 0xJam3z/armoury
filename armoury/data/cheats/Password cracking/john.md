# john the ripper

% password recovery, password cracking

#plateform/linux  #target/local  #cat/CRACKING/PASSWORD 

## John - Crack LM hashes
```
john --wordlist=<wordlist> --format=lm hash.txt
```

## John - Crack NTLM hashes
```
john --wordlist=<wordlist> --format=nt hash.txt
```

## John - Crack NetNTLMv1 hashes
```
john --wordlist=<wordlist> --format=netntlm hash.txt
```

## John - Crack NetNTLMv2 hashes
```
john --wordlist=<wordlist> --format=netntlmv2 hash.txt
```

## John - Convert SSH private key to a crackable hash
```
python /usr/share/john/ssh2john.py <ssh_key> > <ssh_hash_file>
```

## John - Crack SSH private key hash
```
john --wordlist=<wordlist> <ssh_hash_file>
```

## John - Crack MD5 hashes
```
john --wordlist=<wordlist> --format=raw-md5 hash.txt
```

= wordlist: /usr/share/wordlist/rockyou.lst