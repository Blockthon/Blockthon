# BitcoinGold With Blockthon

## Generated and Convert Private Key (HEX) To BitcoinGold Address
```python

from Blockthon import BitcoinGold, Wallet

privatekey = Wallet.getPrivateKey()
#convert To Bitcoingold Address
BitcoinGold_ADDR = BitcoinGold.Address_From_PrivateKey(privatekey)
```