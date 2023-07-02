# Ethereum With Blockthon

## Generated and Convert Private Key (HEX) To Ethereum Address
```python

from Blockthon import Ethereum, Wallet, Check

privatekey = Wallet.getPrivateKey()
#convert To Bitcoingold Address
Ethereum_ADDR = Ethereum.Address_From_PrivateKey(privatekey)
# Check Balance Address
Balance = Check.Eth_Balance(Ethereum_ADDR)
```