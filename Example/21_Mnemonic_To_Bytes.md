## Convert Mnemonic To Bytes

### Generated and Convert Mnemonic To Bytes (seed)

```python
from Blockthon.Wallet import Mnemonic_To_Bytes, getMnemonic

# generated random mnemonic 12 word
mnemonicWords = getMnemonic(size=12)
# convert Mnemonic to seed Bytes
bytes_string = Mnemonic_To_Bytes(mnemonicWords)
```