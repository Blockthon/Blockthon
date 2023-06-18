## Generated Private Key and Convert To WIF

generated random private key hex to wif with `Blockthon`:
for convert private key hex to `wif compress` or `wif uncompress`:

```python
from Blockthon.Wallet import PrivateKey_To_WIF, PrivateKey

privatekey = PrivateKey()
wif_compress = PrivateKey_To_WIF(privatekey, compress=True)
wif_uncompress = PrivateKey_To_WIF(privatekey, compress=False)
```
