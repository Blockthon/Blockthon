## Generated And Convert Private Key HEX To Bytes (seed)

generated random private key (hex) and Convert to seed (bytes) with `Blockthon`

```python
from Blockthon.Wallet import PrivateKey, PrivateKey_To_Bytes

# Generated Random Private Key
privatekey = PrivateKey()
# convert Private Key Hex To Bytes (seed)
bytes_string = PrivateKey_To_Bytes(privatekey)
```
