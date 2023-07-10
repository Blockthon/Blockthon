## Generated Private Key and Convert To WIF

generated random private key hex to wif with `Blockthon`:
```python
from Blockthon import Wallet
# generated private key random
key = Wallet.getPrivateKey()
# convert a hex Private key to wif:
seed = Wallet.PrivateKey_To_Bytes(key)
# convert Bytes (seed) To WIF Compress
wif_compress = Wallet.Bytes_To_Wif(seed, compress=True)
# convert Bytes (seed) To Wif UnCompress
wif_uncompress = Wallet.Bytes_To_Wif(seed, compress=False)
```