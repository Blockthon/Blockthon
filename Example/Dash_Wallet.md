# Dash With Blockthon

## Generated and Convert Private Key (HEX) To Dash Address
```python

from Blockthon import Dash, Wallet

privatekey = Wallet.getPrivateKey()
#convert To Bitcoingold Address
Dash_ADDR = Dash.Address_From_PrivateKey(privatekey)
```