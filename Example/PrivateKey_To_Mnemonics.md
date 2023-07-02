## Generated and convert Private Key Hex To Mnemonic Word's:

generated private key with blockthon and convert private key (hex) to mnemonic:

`PrivateKey_To_Mnemonics(privatekey: str, size: int) -> str`
```python
from Blockthon import Wallet
# generated private key random
key = Wallet.getPrivateKey()
# convert Private Key [hex] to Mnemonic string (word's)
mnemonic_Words = Wallet.PrivateKey_To_Mnemonic(key, size=12)
```
