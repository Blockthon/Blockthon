# DigiByte With Blockthon

## Generated and Convert Private Key (HEX) To DigiByte Address
```python

from Blockthon import Digibyte, Wallet

privatekey = Wallet.getPrivateKey()
#convert To Bitcoingold Address
DigiByte_ADDR = Digibyte.Address_From_PrivateKey(privatekey)
```