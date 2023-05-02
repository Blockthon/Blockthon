# Blockthon
Blockthon Python Package for Generate and Converting Wallet Private Key and Mnemonic for Address Bitcoin

### Generate Private Key (Hex) [Random]:

generated private key hex random with Blockthon in Python very fast for any os:

```python
import Blockthon
PrivateKey = Blockthon.PrivateKey()
``` 

---

#### Blockthon / `Python` Example:

---

Generated Compressed Address and Un Compressed Address Wallet Bitcoin From Private Key Hex : example to [ `AddrFromHex_CheckBalance.py` ](https://github.com/Blockthon/Blockthon/blob/main/example/AddrFromHex_CheckBalance.py)

---

#### Example Blockthon on `bash`:
```bash
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

```bash
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
