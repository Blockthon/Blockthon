# Mnemonic To XPRV (Root Key)

## Generated and Convert Mnemonic Word's To XPRV (Root Key):

```python
from Blockthon.Wallet import Mnemonic_To_RootKey, getMnemonic

# Generated Random mnemonic with 12 word
mnemonicWords = getMnemonic(12)
# Convert mnemonic to Root key (xprv)
xprv = Mnemonic_To_RootKey(mnemonicWords)
```