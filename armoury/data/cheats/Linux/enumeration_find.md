# Quick Enumeration with Find

## Search / with Find for ext
```
find / -type f -name "*.<EXT>" 2>/dev/null
```

## SUID Binaries
```
find / -type f -perm -4000 -exec ls -l {} \; 2>/dev/null
```

## SGID Binaries
```
find / -type f -perm -2000 -exec ls -l {} \; 2>/dev/null
```

## World Writeable Directories
```
find / -type d -perm -0002 -print 2>/dev/null
```

## World Writeable Files
```
find / -type f -perm -0002 -print 2>/dev/null
```

## User/Group Ownership
```
find / -type f -user <USER> -group <GROUP> 2>/dev/null
```

## Modified in last X days
```
find / -type f -mtime -<N> 2>/dev/null
```

## File Size Check
```
find / -type f -size <SIZE>c 2>/dev/null
```

## 10mb+ Files
```
find / -type f -size +10M 2>/dev/null
```

## Password Find
```
find / -type f -readable -exec grep -Il "password" {} \; 2>/dev/null
```

## Executable Files
```
find / -type f -executable -not -path "/proc/*" 2>/dev/null
```

## Hidden Files
```
find . -maxdepth <DEPTH> -type f -iname ".*" 2>/dev/null
```
