## Convert Private Key Hex to Binary

### Binary from Private Key Hex

in this example can see how to created new private key (hex) and convert to binary with `blockthon`
```python
from Blockthon.Wallet import PrivateKey, PrivateKey_To_Binary
# generated private key random
key = PrivateKey()
# convert Private key (hex) to binary:
binary_data = PrivateKey_To_Binary(key)
```
