# Litecoin With Blockthon

## Generated and Convert Private Key (HEX) To Litecoin Address With All Type's : `P2PKH`/`P2SH`/`P2WPKH`/`P2WSH`
```python

from Blockthon import Litecoin, Wallet, Check

privatekey = Wallet.getPrivateKey()
#convert To Bitcoingold Address
p2pkh_ltc = Litecoin.Address_From_PrivateKey(privatekey, 'P2PKH')
p2sh_ltc = Litecoin.Address_From_PrivateKey(privatekey, 'P2SH')
p2wpkh_ltc = Litecoin.Address_From_PrivateKey(privatekey, 'P2WPKH')
p2wsh_ltc = Litecoin.Address_From_PrivateKey(privatekey, 'P2WSH')
# Check Balance Address
Balance_p2pkh = Check.Ltc_Balance(p2sh_ltc)
Balance_p2wpkh = Check.Ltc_Balance(p2wpkh_ltc)
Balance_p2sh = Check.Ltc_Balance(p2sh_ltc)
Balance_p2wsh = Check.Ltc_Balance(p2wsh_ltc)
```