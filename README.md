# Blockthon
Blockthon Python Package for Generate and Converting Wallet Private Key and Mnemonic for Address Bitcoin

```bash
# on windows
pip install Blockthon

# on Linux
pip3 install Blockthon
```

or for download manual:
```bash
git clone https://github.com/Blockthon/Blockthon
cd Blockthon
make
```


### Generate Private Key (Hex) [Random]:

generated private key hex random with Blockthon in Python very fast for any os:

### Generated Private Key:
```python
from Blockthon.Wallet import PrivateKey

privatekey = PrivateKey()
```
### Convert Private Key (HEX) To Compress & Un Compress Address:

for generated compressed and uncompress address bitcoin wallet use this example:
```python

from Blockthon.Wallet import PrivateKey, PrivateKey_To_CompressAddr, PrivateKey_To_UnCompressAddr

# Generate Private Key 
privatekey = PrivateKey()
# Convert Private key Hex To Compress Address Bitcoin
compressAddress = PrivateKey_To_CompressAddr(privatekey)
uncompressAddress = PrivateKey_To_UnCompressAddr(privatekey)
```
another example with new Format for all Bitcoin address Type in `Blockthon`:

- Data Entered `privatekey [hex]` with `string` type
- Data Entered `format` with `string` type: `compress` , `uncompress`, `P2PKH`, `P2SH`, `P2WSH`, `P2WPKH`, `P2WPKHinP2SH`, `P2WSHinP2SH`.

Here Convert example for privatekey hex with return P2PKH address:

`PrivateKey_To_Address(privatekey, Type='P2PKH')`

now , another example for convert private key hex to compress address and uncompress address:

```python
from Blockthon.Wallet import PrivateKey
from Blockthon.Bitcoin import PrivateKey_To_Address

privatekey = PrivateKey()
compressAddress = PrivateKey_To_Address(privatekey, Type='compress')
uncompressAddress = PrivateKey_To_Address(privatekey, Type='uncompress')
```

### Check Value Balance From Address Bitcoin Wallet:
for checking balance per address bitcoin wallet with any type format can use example :

```python
from Blockthon.Bitcoin import Balance_BTC

address = "bc1qu8dccq3yetd93m4nge0yay53lwgwvxngj8a80s"
balance = Balance_BTC(address)
# return value balance to string can / 100000000
```
### Generate and Convert Private Key HEX To Ethereum Address:

example: generate privatekey hex and convert to ethereum address:
```python
from Blockthon.Wallet import PrivateKey_To_ETH
import os

privatekey = os.urandom(32).hex()
addressEthereum = PrivateKey_To_ETH(privatekey)
```
check value balance Ethereum from address:
```python
from Blockhton.Ethereum import Balance_ETH

address = "0x3628c7978C69278fA19A88a5B16718F47f5BEfe8"
balance = Balance_ETH(address)
```

