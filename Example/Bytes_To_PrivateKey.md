# Bytes To Private Key (HEX)

### Convert and Generated Bytes To Private Key (HEX)

```python
from Blockthon import Wallet
# generated random bytes without repeat
byte = Wallet.getSeed()
# convert bytes to hex private key
privatekey = Wallet.Bytes_To_PrivateKey(byte)
```