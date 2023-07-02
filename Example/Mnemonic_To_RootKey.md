# Mnemonic To XPRV (Root Key)

## Generated and Convert Mnemonic Word's To XPRV (Root Key):

```python
from Blockthon import Wallet
# generated random Mnemonic words [without repeat]
mnemonic_words = Wallet.getMnemonic(size=12)
# Convert mnemonic to Root key (xprv)
xprv = Wallet.Mnemonic_To_RootKey(mnemonic_words)
```
