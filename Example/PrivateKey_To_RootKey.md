## Generated Root Key (xprv) from Private Key hex

### convert Private Key hex to xprv (root key)

in example can see how to generated random private key (hex) and convert to root key (xprv) with `Blockthon`:
```python
from Blockthon import Wallet
# generated private key random
key = Wallet.getPrivateKey()
# convert private key to mnemonic with size 12
Mnemonic_string = Wallet.PrivateKey_To_Mnemonic(key, 12)
# convert mnemonic to root key (XPRV)
xprv = Wallet.Mnemonic_To_RootKey(Mnemonic_string)
```
