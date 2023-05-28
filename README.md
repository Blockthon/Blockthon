# Blockthon
Blockthon Python Package for Generate and Converting Wallet Private Key and Mnemonic for Address Bitcoin

```bash
git clone https://github.com/Blockthon/Blockthon
cd Blockthon
make
```

### Generate Private Key (Hex) [Random]:

generated private key hex random with Blockthon in Python very fast for any os:

```python
import Blockthon
PrivateKey = Blockthon.PrivateKey()
``` 

---

## Blockthon / `Python` Example:

---

Generated Compressed Address and Un Compressed Address Wallet Bitcoin From Private Key Hex : example to [ `AddrFromHex_CheckBalance.py` ](https://github.com/Blockthon/Blockthon/blob/main/example/AddrFromHex_CheckBalance.py)

---
### Generated `Compress` and `Un Compress` Bitcoin Wallet Address :

```python
import Blockthon as block

PrivateKey_ = block.PrivateKey()
# Un Compress Bitcoin Wallet Address [Default : compress=false]
unCompress_Address = block.Addr_From_PrivateKey(PrivateKey_)
# Compress Bitcoin Wallet Address [Default : compress=True]
Compress_Address = block.Addr_From_PrivateKey(PrivateKey_, True)
```


### Generated `P2PKH` , `P2SH` , `P2WPKH` , `P2WSH` , `P2WSH in P2SH` and `P2WPKH in P2SH` Bitcoin Address Type From Private Key (hex) :

```python
import Blockthon as block

# Generated Random Private Key (HEX)
privatekey = block.PrivateKey()
# Generated P2PKH Address Bitcoin Address :
p2pkh = block.P2PKH_From_PrivateKey(privatekey)
# Generated P2SH Address Bitcoin Address :
p2sh = block.P2SH_From_PrivateKey(privatekey)
# Generated P2PKH Address Bitcoin Address :
p2wpkh = block.P2WPKH_From_PrivateKey(privatekey)
# Generated P2WSH Address Bitcoin Address :
p2wsh = block.P2WSH_From_PrivateKey(privatekey)
# Generated P2WPKH in P2SH Address Bitcoin Address :
p2wpkh_p2sh = block.P2WPKH_in_P2SH_From_PrivateKey(privatekey)
# Generated P2WSH in P2SH Address Bitcoin Address :
p2wsh_in_p2sh = block.P2WSH_in_P2SH_From_PrivateKey(privatekey)
```
### Check Balance (Value) Bitcoin Wallet Address:

for check balance per address wallet just use `Balance()` for bitcoin address's
```python
import Blockthon as block

bitcoinAddress = "179nEQKfizafpVkefed4XVSpdUpXzRSSvm"
balance_string = block.Balance(bitcoinAddress)

```

### Generated Ethereum Address From Private Key (HEX):

generated ethereum address wallet from private key (hex) , in this example first generated private key random , after that generated address from private key with `block.ETH_From_PrivateKey(privatekey)`, first needed import `import Blockthon as block` .

```python
import Blockthon as block

# Generated Random Hex (Private key)
privatekey = block.PrivateKey()
# Generated Ethereum Address From Private Key (HEX)
ethereum_Address = block.ETH_From_PrivateKey(privatekey)

```

Check Value Balance Ethereum Address :

```python
import Blockthon as block

address = "0xe36B47dC83228FA6c3a50B07A820d3CdF7fAa700"
# Check Value Balance Return [str]
balance = block.Balance_Ethereum(address)
```

---

### Generated Tron Address From Private Key (HEX):

generated Tron address wallet from private key (hex) , in this example first generated private key random , after that generated address from private key with `block.TRX_From_PrivateKey(privatekey)`, first needed import `import Blockthon as block` .

```python
import Blockthon as block

# Generated Random Hex (Private key)
privatekey = block.PrivateKey()
# Generated Tron Address From Private Key (HEX)
Tron_Address = block.TRX_From_PrivateKey(privatekey)
```
Check Value Balance Tron Address :

```python
import Blockthon as block

address = "TDbLEetdDFLJcq19DrKk3yJAHpWfkQ418r"
# Check Value Balance Return [str]
balance = block.Balance_Tron(address)
```

---


### Generated Dogecoin Address From Private Key (HEX):

generated Dogecoin address wallet from private key (hex) , in this example first generated private key random , after that generated address from private key with `block.DOGE_From_PrivateKey(privatekey)`, first needed import `import Blockthon as block` .

```python
import Blockthon as block

# Generated Random Hex (Private key)
privatekey = block.PrivateKey()
# Generated Dogecoin Address From Private Key (HEX)
Dogecoin_Address = block.DOGE_From_PrivateKey(privatekey)
```

Check Value Balance Dogecoin Address :

```python
import Blockthon as block

# Check Value Balance Return [str]
balance = block.Balance_Dogecoin(Dogecoin_Address)
```

---

### Generated Dash Address From Private Key (HEX):

generated Dash address wallet from private key (hex) , in this example first generated private key random , after that generated address from private key with `block.DASH_From_PrivateKey(privatekey)`, first needed import `import Blockthon as block` .

```python
import Blockthon as block

# Generated Random Hex (Private key)
privatekey = block.PrivateKey()
# Generated Dash Address From Private Key (HEX)
Dash_Address = block.DASH_From_PrivateKey(privatekey)
```

Check Value Balance Dash Address :

```python
import Blockthon as block

# Check Value Balance Return [str]
balance = block.Balance_Dash(Dash_Address)
```

---


### Generated Bitcoin Gold Address From Private Key (HEX):

generated Bitcoin Gold address wallet from private key (hex) , in this example first generated private key random , after that generated address from private key with `block.BTG_From_PrivateKey(privatekey)`, first needed import `import Blockthon as block` .

```python
import Blockthon as block

# Generated Random Hex (Private key)
privatekey = block.PrivateKey()
# Generated Bitcoin Gold Address From Private Key (HEX)
BitcoinGold_Address = block.BTG_From_PrivateKey(privatekey)
```

Check Value Balance BitcoinGold Address :

```python
import Blockthon as block

# Check Value Balance Return [str]
balance = block.Balance_BitcoinGold(BitcoinGold_Address)
```
Check Value Balance BitcoinGold Address :

```python
import Blockthon as block

# Check Value Balance Return [str]
balance = block.Balance_BitcoinGold(BitcoinGold_Address)
```
---

### Generated Litecoin Address From Private Key (HEX):

generated Litecoin address wallet from private key (hex) , in this example first generated private key random , after that generated address from private key with `block.LTC_From_PrivateKey(privatekey)`, first needed import `import Blockthon as block` .

```python
import Blockthon as block

# Generated Random Hex (Private key)
privatekey = block.PrivateKey()
# Generated Litecoin Address From Private Key (HEX)
Litecoin_Address = block.LTC_From_PrivateKey(privatekey)
```

Check Value Balance Litecoin Address :

```python
import Blockthon as block

# Check Value Balance Return [str]
balance = block.Balance_Litecoin(Litecoin_Address)
```

---

### Generated Ravencoin Address From Private Key (HEX):

generated Ravencoin address wallet from private key (hex) , in this example first generated private key random , after that generated address from private key with `block.RVN_From_PrivateKey(privatekey)`, first needed import `import Blockthon as block` .

```python
import Blockthon as block

# Generated Random Hex (Private key)
privatekey = block.PrivateKey()
# Generated Ravencoin Address From Private Key (HEX)
Ravencoin_Address = block.RVN_From_PrivateKey(privatekey)
```

Check Value Balance Ravencoin Address :

```python
import Blockthon as block

# Check Value Balance Return [str]
balance = block.Balance_Ravencoin(Ravencoin_Address)
```

---


### Generated DigiByte Address From Private Key (HEX):

generated DigiByte address wallet from private key (hex) , in this example first generated private key random , after that generated address from private key with `block.DigiByte_From_PrivateKey(privatekey)`, first needed import `import Blockthon as block` .

```python
import Blockthon as block

# Generated Random Hex (Private key)
privatekey = block.PrivateKey()
# Generated DigiByte Address From Private Key (HEX)
DigiByte_Address = block.DigiByte_From_PrivateKey(privatekey)
```

Check Value Balance DigiByte Address :

```python
import Blockthon as block

# Check Value Balance Return [str]
balance = block.Balance_DigiByte(DigiByte_Address)
```

---


### Generated VIA Address From Private Key (HEX):

generated VIA address wallet from private key (hex) , in this example first generated private key random , after that generated address from private key with `block.VIA_From_PrivateKey(privatekey)`, first needed import `import Blockthon as block` .

```python
import Blockthon as block

# Generated Random Hex (Private key)
privatekey = block.PrivateKey()
# Generated VIA Address From Private Key (HEX)
VIA_Address = block.VIA_From_PrivateKey(privatekey)
```

---

### Generated QTUM Address From Private Key (HEX):

generated QTUM address wallet from private key (hex) , in this example first generated private key random , after that generated address from private key with `block.QTUM_From_PrivateKey(privatekey)`, first needed import `import Blockthon as block` .

```python
import Blockthon as block

# Generated Random Hex (Private key)
privatekey = block.PrivateKey()
# Generated QTUM Address From Private Key (HEX)
QTUM_Address = block.QTUM_From_PrivateKey(privatekey)
```
Check Value Balance Qtum Address :

```python
import Blockthon as block

# Check Value Balance Return [str]
balance = block.Balance_Qtum(Qtum_Address)
```
---


### Generated ZCASH Address From Private Key (HEX):

generated ZCASH address wallet from private key (hex) , in this example first generated private key random , after that generated address from private key with `block.ZEC_From_PrivateKey(privatekey)`, first needed import `import Blockthon as block` .

```python
import Blockthon as block

# Generated Random Hex (Private key)
privatekey = block.PrivateKey()
# Generated ZEC Address From Private Key (HEX)
ZEC_Address = block.ZEC_From_PrivateKey(privatekey)
```
Check Value Balance zCash Address :

```python
import Blockthon as block

# Check Value Balance Return [str]
balance = block.Balance_zCash(zCash_Address)
```

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
