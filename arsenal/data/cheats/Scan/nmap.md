# nmap

#plateform/linux #target/remote #cat/RECON #tag/scan

## nmap - hosts alive (ping scan)
```
nmap -sn <ip_range>
```

## nmap - classic scan (default scripts and version detection)
```
nmap -sC -sV <ip>
```

## nmap - read targets from a file
```
nmap -iL <targets_file>
```

## nmap - classic scan + save output to all formats
```
nmap -sC -sV -oA <output_file> <ip>
```

## nmap - quick scan top 100 ports
```
nmap --top-ports 100 --open -sV <ip>
```

## nmap - scan top 5000 ports
```
nmap --top-ports 5000 --open -sV <ip>
```

## nmap - full port scan
```
nmap -p- -sV <ip>
```

## nmap - scan specific ports
```
nmap -p<port_list> --open <ip>
```

## nmap - aggressive scan (includes OS detection, version detection, script scanning, and traceroute)
```
nmap -A <ip>
```

## nmap - comprehensive scan with vulnerability scripts
```
IP=<ip>;
ports=$(nmap -p- --min-rate=1000 -T4 $IP | grep ^[0-9] | cut -d '/' -f 1 | tr '\n' ',' | sed s/,$//);
nmap -p$ports -sC -sV --script=vuln,exploit,auth,discovery -oN scan.txt --reason $IP
```

## nmap - udp scan (top 100 ports)
```
nmap -sU --top-ports 100 <ip>
```

## nmap - slow and stealthy scan
```
nmap -sS -T2 --max-rate 50 <ip>
```

## massscan - fast full port scan
```
masscan -p1-65535 <ip> --rate=1000 -i <interface>
```

## nmap - check for SMB signing
```
nmap -p 445 --script=smb2-security-mode <ip>
```

## nmap - scan behind a proxy
```
proxychains nmap -sT -Pn -n --open -oA <output_file> -iL <targets_file>
```

