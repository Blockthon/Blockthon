## Generated Private Key and Convert To WIF

generated random private key hex to wif with `Blockthon`:
```python
from Blockthon.Wallet import PrivateKey, PrivateKey_To_Wif

# Generated Private Key Hex:
privatekey = PrivateKey()
# convert hex Private key to wif:
wif = PrivateKey_To_Wif(privatekey)
```
for convert private key hex to `wif compress` or `wif uncompress`:
```python
from Blockthon.Wallet import PrivateKey, PrivateKey_To_Wif

privatekey = PrivateKey()
# Convert private key hex to wif compressed
wif_compress = PrivateKey_To_Wif(privatekey, compress=True)
# convert Private key hex to uncompress wif 
wif_uncompress = PrivateKey_To_Wif(privatekey, compress=False)
```
