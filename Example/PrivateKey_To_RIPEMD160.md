## RIPEMD160 Key Hash Address

### convert private key hex to RIPEMD160 hash address 

```python
from Blockthon import Wallet
# generated private key random
key = Wallet.getPrivateKey()
# convert private key hex To ripemd160 
ripemd160 = Wallet.PrivateKey_To_RIPEMD160(key)

```