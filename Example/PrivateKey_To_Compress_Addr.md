## Convert Private Key Hex to compress Address & Uncompress
 
generated random Private Key and convert to compress bitcoin address on `blockthon`:

```python
from Blockthon import Wallet
# generated private key random
key = Wallet.getPrivateKey()
# convert private key (hex) to compressed Bitcoin Address
compressAddress = Wallet.PrivateKey_To_Address(key, compress=True)
# convert private key (hex) to uncompressed Bitcoin Address
uncompressAddress = Wallet.PrivateKey_To_Address(key, compress=False)
```
