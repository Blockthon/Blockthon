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

### Example `Blockthon`:

- [PrivateKey](https://github.com/Blockthon/Blockthon/blob/main/Example/01_PrivateKey.md 'private key (hex)')
- [PrivateKey To Binary](https://github.com/Blockthon/Blockthon/blob/main/Example/02_PrivateKey_To_Binary.md 'private key to binary')
- [PrivateKey To Bytes](https://github.com/Blockthon/Blockthon/blob/main/Example/03_PrivateKey_To_Bytes.md 'private key to bytes')
- [PrivateKey To Mnemonic](https://github.com/Blockthon/Blockthon/blob/main/Example/04_PrivateKey_To_Mnemonics.md 'private key to mnemonic') 
- [PrivateKey To Dec](https://github.com/Blockthon/Blockthon/blob/main/Example/05_PrivateKey_To_Dec.md 'private key to number dec')
- [PrivateKey To Root Key](https://github.com/Blockthon/Blockthon/blob/main/Example/06_PrivateKey_To_RootKey.md 'private key to root key xprv')
- [PrivateKey To Wif](https://github.com/Blockthon/Blockthon/blob/main/Example/07_PrivateKey_To_Wif.md 'private key to wif')
- [PrvateKey To Hash Address](https://github.com/Blockthon/Blockthon/blob/main/Example/08_PrivateKey_To_Public_Hash_Addr.md 'private key hex to hash address')
- [PrivateKey To Compress Address](https://github.com/Blockthon/Blockthon/blob/main/Example/09_PrivateKey_To_Compress_Addr.md 'private key to compressed address')
- [Private Key To Uncompressed Address](https://github.com/Blockthon/Blockthon/blob/main/Example/10_PrivateKey_To_UnCompress_Addr.md 'private key to uncompressed address')
- [Private Key From Binary](https://github.com/Blockthon/Blockthon/blob/main/Example/11_PrivateKey_From_Binary.md 'private key from binary')
- [Private Key From Dec](https://github.com/Blockthon/Blockthon/blob/main/Example/12_PrivateKey_From_Dec.md 'private key from number dec')
- [Private Key From Passphrase](https://github.com/Blockthon/Blockthon/blob/main/Example/13_PrivateKey_From_Passphrase.md 'private key from passphrase')
- [Private Key From Root Key (xprv)](https://github.com/Blockthon/Blockthon/blob/main/Example/14_PrivateKey_From_RootKey.md 'private key from xprv root key to hex')
- [Bytes (seed)](https://github.com/Blockthon/Blockthon/blob/main/Example/15_Bytes.md 'bytes seed')
- [Bytes To Mnemonic](https://github.com/Blockthon/Blockthon/blob/main/Example/16_Bytes_To_Mnemonic.md 'bytes to mnemonic')
- [Bytes To Private Key](https://github.com/Blockthon/Blockthon/blob/main/Example/17_Bytes_To_PrivateKey.md 'bytes to private key hex')
- [Bytes To Public Key](https://github.com/Blockthon/Blockthon/blob/main/Example/18_Bytes_To_PublicKey.md 'bytes to public key')
- [Bytes To Wif](https://github.com/Blockthon/Blockthon/blob/main/Example/19_Bytes_To_Wif.md 'Bytes to wif')
- [Mnemonic](https://github.com/Blockthon/Blockthon/blob/main/Example/20_Mnemonic.md 'Mnemonic')
- [Mnemonic to bytes](https://github.com/Blockthon/Blockthon/blob/main/Example/21_Mnemonic_To_Bytes.md 'mnemonic to bytes')
- [Mnemonic to root key (xprv)](https://github.com/Blockthon/Blockthon/blob/main/Example/22_Mnemonic_To_RootKey.md 'mnemonic to root key')
- [Bitcoin](https://github.com/Blockthon/Blockthon/blob/main/Example/23_Bitcoin_Wallet.md 'bitcoin')
- [Bitcoin Gold](https://github.com/Blockthon/Blockthon/blob/main/Example/24_BitcoinGold_Wallet.md 'bitcoin gold')
- [Dash](https://github.com/Blockthon/Blockthon/blob/main/Example/25_Dash_Wallet.md 'dash')
- [DigiByte](https://github.com/Blockthon/Blockthon/blob/main/Example/26_DigiByte_Wallet.md 'digibyte')
- [Dogecoin](https://github.com/Blockthon/Blockthon/blob/main/Example/27_Dogecoin_Wallet.md 'dogecoin')
- [Ethereum](https://github.com/Blockthon/Blockthon/blob/main/Example/28_Ethereum_Wallet.md 'ethereum')
- [Litecoin](https://github.com/Blockthon/Blockthon/blob/main/Example/29_Litecoin_Wallet.md 'litecoin')
- [Qtum](https://github.com/Blockthon/Blockthon/blob/main/Example/30_Qtum_Wallet.md 'qtume example generated')
- [Ravencoin](https://github.com/Blockthon/Blockthon/blob/main/Example/31_Ravencoin_Wallet.md 'rvn - ravencoin generated example')
- [Tron (TRX)](https://github.com/Blockthon/Blockthon/blob/main/Example/32_Tron_Wallet.md 'tron trx generated example')
- [zCash](https://github.com/Blockthon/Blockthon/blob/main/Example/33_zCash_Wallet.md 'zcash generated example')

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

=======
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

