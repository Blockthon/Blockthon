# zCash With Blockthon

## Generated and Convert Private Key (HEX) To zCash Address
```python

from Blockthon import zCash, Wallet, Check

privatekey = Wallet.getPrivateKey()
#convert To Bitcoingold Address
zCash_ADDR = zCash.Address_From_PrivateKey(privatekey)
# Check Balance Address
Balance = Check.Zec_Balance(zCash_ADDR)
```