## convert passphrase (word) to Private Key (HEX)

### generate Private Key Hex From Word (Passphrase)

example for convert passphrase word (string) to hex private key:

```python
from Blockthon import Wallet

passphrase_string = 'Mmdrza.Com' # Can Enter Any Word
# convert To Private Key Hex:
privatekey = Wallet.Passphrase_To_PrivateKey(passphrase_string)
```