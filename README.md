# Blockthon
Blockthon Python Package for Generate and Converting Wallet Private Key and Mnemonic for Address Bitcoin


#### Example Blockthon on `bash`:
```bash:
source Blockthon.sh

# counter for total generated
count=0
# for repeate new generated
while true
do
    ((count++))
    # from blockthon file import for generated new private key
    key=$(PrivateKey)
    # for print or echo detail's
    echo $count $key
done

```

Generated Random Private Key from Integer (Number) on bash With Blockthon:

```
#!/bin/bash
source Blockthon.sh

z=0
while true
do
  d=$((19999999999999999 + RANDOM % 999999999999999999999999999999999999))
  key=$(PrivateKey $d)
  ((z++))
  echo -ne "Total: $z $key\r"
done
```
