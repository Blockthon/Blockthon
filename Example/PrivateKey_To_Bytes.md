## Generated And Convert Private Key HEX To Bytes (seed)

generated random private key (hex) and Convert to seed (bytes) with `Blockthon`

```python
from Blockthon import Wallet
# generated private key random
key = Wallet.getPrivateKey()
# convert Private Key Hex To Bytes (seed)
bytes_string = Wallet.PrivateKey_To_Bytes(key)
```
