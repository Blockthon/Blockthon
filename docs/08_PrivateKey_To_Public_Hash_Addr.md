## Public Key Hash Address

### convert private key hex to public key hash address 

```python
from Blockthon.Wallet import PrivateKey_To_PublicHash, PrivateKey
# generated private key hex
key = PrivateKey()
# convert and generated hash address from private key hex
hashAddr = PrivateKey_To_PublicHash(key)
```