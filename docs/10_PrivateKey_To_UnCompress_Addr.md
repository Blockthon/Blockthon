## Convert Private Key Hex to uncompress Address

generated random Private Key and convert to uncompress bitcoin address on `blockthon` with 3 different method 

```python
from Blockthon.Wallet import PrivateKey_To_UnCompressAddr, PrivateKey

# generated private key
privatekey = PrivateKey()
# convert private key (hex) to uncompressed Bitcoin Address
uncompressAddress = PrivateKey_To_UnCompressAddr(privatekey)
```
or can use `PrivateKey_To_Addr` on `Blockthon.Wallet` , param:[privatekey(str), compress=True/False]
 return `uncompressAddress` on `string` type: 
```python
from Blockthon.Wallet import PrivateKey_To_Addr, PrivateKey

privatekey = PrivateKey()
uncompressAddress = PrivateKey_To_Addr(privatekey, compress=False)
```
or can use `Blockthon.Bitcoin` import `PrivateKey_To_Address` with param `privatekey` & Just `Type='uncompress'`:
```python
from Blockthon.Bitcoin import PrivateKey_To_Address
import os

privatekey = os.urandom(32).hex()
# in Type Parameter can use : P2PKH / P2SH / P2WPKH / P2WSH / P2WPKHinP2SH / P2WSHinP2SH / compress / uncompress
uncompressAddr = PrivateKey_To_Address(privatekey, Type='uncompress')
```
