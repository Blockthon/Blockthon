## Convert Private Key Hex to Binary

### Binary from Private Key Hex

in this example can see how to created new private key (hex) and convert to binary with `blockthon`
```python
from Blockthon import Wallet
# generated private key random
key = Wallet.getPrivateKey()
# convert Private key (hex) to binary:
binary_data = Wallet.PrivateKey_To_Binary(key)
```
