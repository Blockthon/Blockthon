## Convert Private Key Hex to compress Address

generated random Private Key and convert to compress bitcoin address on `blockthon` with 3 different method 

```python
from Blockthon.Wallet import PrivateKey_To_CompressAddr, PrivateKey

# convert private key (hex) to compressed Bitcoin Address
compressAddress = PrivateKey_To_CompressAddr(PrivateKey())
```
or can use `PrivateKey_To_Addr` on `Blockthon.Wallet` , param:[privatekey(str), compress=True/False]
 return `compressAddress` on `string` type: 
```python
from Blockthon.Wallet import PrivateKey_To_Addr, PrivateKey

privatekey = PrivateKey()
compressAddress = PrivateKey_To_Addr(privatekey, compress=True)
```
or can use `Blockthon.Bitcoin` import `PrivateKey_To_Address` with param `privatekey` & Just `Type='compress'`:
```python
from Blockthon.Bitcoin import PrivateKey_To_Address
import os

privatekey = os.urandom(32).hex()
# in Type Parameter can use : P2PKH / P2SH / P2WPKH / P2WSH / P2WPKHinP2SH / P2WSHinP2SH / compress / uncompress
compressAddr = PrivateKey_To_Address(privatekey, Type='compress')
```
or use `Blockthon.Wallet` in `PrivateKey_To_Address` (Very Fast):
```python
from Blockthon.Wallet import PrivateKey_To_Address, PrivateKey

# convert hex to compressed address
compressed_Address = PrivateKey_To_Address(PrivateKey(), compress=True)
```
