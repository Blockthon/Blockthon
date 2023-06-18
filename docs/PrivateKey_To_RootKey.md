## Generated Root Key (xprv) from Private Key hex

### convert Private Key hex to xprv (root key)

in example can see how to generated random private key (hex) and convert to root key (xprv) with `Blockthon`:
```python
from Blockthon.Wallet import PrivateKey_To_RootKey, PrivateKey

# generated random private key
key = PrivateKey()
# convert hex private key to xprv
xprv_rootKey = PrivateKey_To_RootKey(key)
```
