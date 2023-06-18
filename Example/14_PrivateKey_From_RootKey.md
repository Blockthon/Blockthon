## convert root key (xprv) to private key
### Private key from root key (xprv)
```python
from Blockthon.Wallet import PrivateKey_From_RootKey
# example root key , can enter your xprv 
xprv_string = 'xprv123456789...abcdefgABCDRFGTHG98741235'
# convert root key xprv to hex private key
privatekey = PrivateKey_From_RootKey(xprv=xprv_string)
```