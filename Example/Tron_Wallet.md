# Tron With Blockthon

## Generated and Convert Private Key (HEX) To Tron Address
```python

from Blockthon import Tron, Wallet, Check

privatekey = Wallet.getPrivateKey()
#convert To Bitcoingold Address
Tron_ADDR = Tron.Address_From_PrivateKey(privatekey)
# Check Balance Address
Balance = Check.Trx_Balance(Tron_ADDR)
```