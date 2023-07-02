## Convert Mnemonic To Bytes

### Generated and Convert Mnemonic To Bytes (seed)

```python
from Blockthon import Wallet
# generated random Mnemonic words [without repeat]
mnemonic_words = Wallet.getMnemonic(size=12)
# convert Mnemonic to seed Bytes
byte = Wallet.Mnemonic_To_Bytes(mnemonic_words)
```