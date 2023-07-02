# Ravencoin With Blockthon

## Generated and Convert Private Key (HEX) To Ravencoin Address
```python

from Blockthon import Ravencoin, Wallet, Check

privatekey = Wallet.getPrivateKey()
#convert To Bitcoingold Address
Ravencoin_ADDR = Ravencoin.Address_From_PrivateKey(privatekey)
# Check Balance Address
Balance = Check.Rvn_Balance(Ravencoin_ADDR)
```