# Qtum With Blockthon

## Generated and Convert Private Key (HEX) To Qtum Address
```python

from Blockthon import Qtum, Wallet, Check

privatekey = Wallet.getPrivateKey()
#convert To Bitcoingold Address
Qtum_ADDR = Qtum.Address_From_PrivateKey(privatekey)
# Check Balance Address
Balance = Check.Qtum_Balance(Qtum_ADDR)
```