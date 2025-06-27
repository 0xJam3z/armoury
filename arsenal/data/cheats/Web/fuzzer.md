# gobuster

% fuzzer, fuzz, gobuster

#plateform/linux #target/remote #cat/ATTACK/FUZZ
## gobuster scan classic
```
gobuster dir -u <url> -w <wordlist>
```

## gobuster scan pentest classic fuzz
```
gobuster dir -u <url> -w <wordlist> -x json,html,php,txt,xml,md
```

## gobuster scan high rate
```
gobuster dir -u <url> -w <wordlist> -t 30
```

## gobuster scan with adding extension
```
gobuster dir -u <url> -w <wordlist> -x json,html,php,txt
```

# wfuzz

% fuzzer, fuzz, wfuzz
#plateform/linux #target/remote #cat/ATTACK/FUZZ
## wfuzz with number on url ( url : http://site/ )
```
wfuzz -z range,1-1000 -u <url>FUZZ
```

## wfuzz with wordlist on url ( url : http://site/ )
```
wfuzz -z file,<file> -u <url>FUZZ
```

## wfuzz on post parameter
```
wfuzz -z file,<file> -X post -u <url> -d 'FUZZ=1'
```

# ffuf

% fuzzer, fuzz, ffuf
#plateform/linux #target/remote #cat/ATTACK/FUZZ

## Directory FUZZ (directory-list-2.3-medium)
```
ffuf -u <URL>/FUZZ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

## Directory FUZZ (common.txt)
```
ffuf -u <URL>/FUZZ -w /usr/share/wordlists/dirb/common.txt
```

## Directory FUZZ (raft-large-directories.txt)
```
ffuf -u <URL>/FUZZ -w /usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt
```

## Directory FUZZ (big.txt)
```
ffuf -u <URL>/FUZZ -w /usr/share/seclists/Discovery/Web-Content/big.txt
```

## Subdomain FUZZ (subdomains-top1million-5000.txt)
```
ffuf -u <URL> -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -H "Host: FUZZ.<URL>"
```

## Subdomain FUZZ (namelist.txt)
```
ffuf -u <URL> -w /usr/share/seclists/Discovery/DNS/namelist.txt -H "Host: FUZZ.<URL>"
```

## Subdomain FUZZ (bitquark-subdomains-top100000.txt)
```
ffuf -u <URL> -w /usr/share/seclists/Discovery/DNS/bitquark-subdomains-top100000.txt -H "Host: FUZZ.<URL>"
```

## Subdomain FUZZ (fierce-hostlist.txt)
```
ffuf -u <URL> -w /usr/share/seclists/Discovery/DNS/fierce-hostlist.txt -H "Host: FUZZ.<URL>"
```

## Subdomain FUZZ (dns-Jhaddix.txt)
```
ffuf -u <URL> -w /usr/share/seclists/Discovery/DNS/dns-Jhaddix.txt -H "Host: FUZZ.<URL>"
```

## ffuf GET parameter fuzzing
```
ffuf -w <wordlist> -u <url>?<param>=FUZZ -fs <response_size>
```


# feroxbuster

% fuzzer, fuzz, ffuf, dirsearch, gobuster, dirb
#plateform/linux #target/remote #cat/ATTACK/FUZZ

## default scan
```
feroxbuster --url <url>
```

## default scan with wordlist
```
feroxbuster --url <url> -w <wordlist>
```

## Multiple headers
```
feroxbuster -u <url> -H "<header>" "<header>"
```

## IPv6, non-recursive scan with INFO-level logging enabled
```
feroxbuster -u <proto|https>://[<ipv6>] --no-recursion -vv
```
        
## Abort or reduce scan speed to individual directory scans when too many errors have occurred
```
feroxbuster -u <url> --auto-bail
```

= wordlist: /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
