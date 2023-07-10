# Bitcoin Wallet With Blockthon

## Generated and convert Private key To Mnemonic , seed (bytes) , Root Key , Passphrase , binary for Compress , Uncompress , P2PKH , P2SH , P2WSH, P2WPKH , P2WPKHinP2SH, P2WSHinP2SH Address Bitcoin Wallet

### Generated and Convert Private Key Hex To Compress and uncompress Bitcoin wallet
```python
from Blockthon import Wallet, Bitcoin
# convert private key (hex) to compressed Bitcoin Address
privatekey = Wallet.getPrivateKey()
compressAddress = Wallet.PrivateKey_To_Address(privatekey, compress=True)
# uncompress
uncompressAddress = Wallet.PrivateKey_To_Address(privatekey, compress=False)
```

## Generated Convert Private Key To All Bitcoin Address Wallet Type

|    Blockthon.Bitcoin    |  privatekey  | Type          |                                                |
|:-----------------------:|:------------:|:--------------|------------------------------------------------|
| `Address_From_PrivateKey` | hex (string) | `compress`    | `Bitcoin.Address_From_PrivateKey(key, Type='compress')`     | 
|   `Address_From_PrivateKey`    | hex (string) | `uncompress`  | `Bitcoin.Address_From_PrivateKey(key, Type='uncompress')`   | 
|   `Address_From_PrivateKey`    | hex (string) | `P2PKH`       | `Bitcoin.Address_From_PrivateKey(key, Type='P2PKH')`        | 
|   `Address_From_PrivateKey`    | hex (string) | `P2SH`        | `Bitcoin.Address_From_PrivateKey(key, Type='P2SH')`         | 
|   `Address_From_PrivateKey`    | hex (string) | `P2WPKH`      | `Bitcoin.Address_From_PrivateKey(key, Type='P2WPKH')`       | 
|   `Address_From_PrivateKey`    | hex (string) | `P2WSH`       | `Bitcoin.Address_From_PrivateKey(key, Type='P2WSH')`        | 
|   `Address_From_PrivateKey`    | hex (string) | `P2WPKHinP2SH` | `Bitcoin.Address_From_PrivateKey(key, Type='P2WPKHinP2SH')` | 
|   `Address_From_PrivateKey`    | hex (string) | `P2WSHinP2SH` | `Bitcoin.Address_From_PrivateKey(key, Type='P2WSHinP2SH')`  |

example :
```python
from Blockthon import Bitcoin
import os

key = os.urandom(32).hex()
# Convert Private Key HEX To Compress Address
compress_Address = Bitcoin.Address_From_PrivateKey(key, 'compress')
# Convert Private Key HEX To Un Compress Address
uncompress_Address = Bitcoin.Address_From_PrivateKey(key, 'uncompress')
# Convert Private Key HEX To P2PKH Address Type
p2pkh_Address = Bitcoin.Address_From_PrivateKey(key, 'P2PKH')
# Convert Private Key HEX To P2SH Address Type
p2sh_Address = Bitcoin.Address_From_PrivateKey(key, 'P2SH')
# Convert Private Key HEX To P2WPKH Address Type
p2wpkh_Address = Bitcoin.Address_From_PrivateKey(key, 'P2WPKH')
# Convert Private Key HEX To P2WSH Address Type
p2wsh_Address = Bitcoin.Address_From_PrivateKey(key, 'P2WSH')
# Convert Private Key HEX To P2WPKH in P2SH Address Type
p2wpkhinp2sh_Address = Bitcoin.Address_From_PrivateKey(key, 'P2WPKHinP2SH')
# Convert Private Key HEX To P2WSH in P2SH Address Type
p2wshinp2sh_Address = Bitcoin.Address_From_PrivateKey(key, 'P2WSHinP2SH')
```
