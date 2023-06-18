## convert passphrase (word) to Private Key (HEX)

### generate Private Key Hex From Word (Passphrase)

example for convert passphrase word (string) to hex private key:

```python
from Blockthon.Wallet import PrivateKey_From_Passphrase
# passphrase word :
passphrase_string = 'Mmdrza.Com'
# Convert Passphrase Word to Private Key Hex:
privatekey = PrivateKey_From_Passphrase(passphrase=passphrase_string)
```