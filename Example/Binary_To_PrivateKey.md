## convert binary to private key hex

### Private Key From Binary

generated random binary string for convert to hex private key
```python
from Blockthon import Wallet

binary_str = Wallet.getBin(256)
privatekey = Wallet.Binary_To_PrivateKey(binary_str)
```