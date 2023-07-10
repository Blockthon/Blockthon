# Dogecoin With Blockthon

## Generated and Convert Private Key (HEX) To Dogecoin Address
```python

from Blockthon import Dogecoin, Wallet, Check

privatekey = Wallet.getPrivateKey()
#convert To Bitcoingold Address
Dogecoin_ADDR = Dogecoin.Address_From_PrivateKey(privatekey)
# Check Balance Address
Balance = Check.Doge_Balance(Dogecoin_ADDR)
```