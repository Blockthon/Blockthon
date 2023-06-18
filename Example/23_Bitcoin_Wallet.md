# Bitcoin Wallet With Blockthon

## Generated and convert Private key To Mnemonic , seed (bytes) , Root Key , Passphrase , binary for Compress , Uncompress , P2PKH , P2SH , P2WSH, P2WPKH , P2WPKHinP2SH, P2WSHinP2SH Address Bitcoin Wallet

### Generated and Convert Private Key Hex To Compress and uncompress Bitcoin wallet
```python
from Blockthon.Wallet import PrivateKey_To_CompressAddr,PrivateKey_To_UnCompressAddr, PrivateKey

# generated private key
privatekey = PrivateKey()
# convert private key (hex) to compressed Bitcoin Address
compressAddress = PrivateKey_To_CompressAddr(privatekey)
# uncompress
uncompressAddress = PrivateKey_To_UnCompressAddr(privatekey)
```

## Generated and Convert Private Key HEX To Compressed and UnCompressed Bitcoin Address Wallet

can use `Blockthon.Bitcoin` import `PrivateKey_To_Address` with param `privatekey` & Just `Type='compress'`:
```python
from Blockthon.Wallet import PrivateKey_To_Addr, PrivateKey

privatekey = PrivateKey()
# compress bitcoin address
compressAddress = PrivateKey_To_Addr(privatekey, compress=True)
# uncompress bitcoin address
uncompressAddress = PrivateKey_To_Addr(privatekey, compress=False)
```
## Generated Convert Private Key To All Bitcoin Address Wallet Type

|     Blockthon.Wallet     |  privatekey  | Type          |                                                |
|:------------------------:|:------------:|:--------------|------------------------------------------------|
|    PrivateKey_To_Addr    | hex (string) | `compress`    | `PrivateKey_To_Addr(key, Type='compress')`     | 
|    PrivateKey_To_Addr    | hex (string) | `uncompress`  | `PrivateKey_To_Addr(key, Type='uncompress')`   | 
|    PrivateKey_To_Addr    | hex (string) | `P2PKH`       | `PrivateKey_To_Addr(key, Type='P2PKH')`        | 
|    PrivateKey_To_Addr    | hex (string) | `P2SH`        | `PrivateKey_To_Addr(key, Type='P2SH')`         | 
|    PrivateKey_To_Addr    | hex (string) | `P2WPKH`      | `PrivateKey_To_Addr(key, Type='P2WPKH')`       | 
|    PrivateKey_To_Addr    | hex (string) | `P2WSH`       | `PrivateKey_To_Addr(key, Type='P2WSH')`        | 
|    PrivateKey_To_Addr    | hex (string) | `P2WPKHinP2SH` | `PrivateKey_To_Addr(key, Type='P2WPKHinP2SH')` | 
|    PrivateKey_To_Addr    | hex (string) | `P2WSHinP2SH` | `PrivateKey_To_Addr(key, Type='P2WSHinP2SH')`  |

example :
```python
from Blockthon.Bitcoin import PrivateKey_To_Addr
import os

key = os.urandom(32).hex()
# Convert Private Key HEX To Compress Address
compress_Address = PrivateKey_To_Addr(key, 'compress')
# Convert Private Key HEX To Un Compress Address
uncompress_Address = PrivateKey_To_Addr(key, 'uncompress')
# Convert Private Key HEX To P2PKH Address Type
p2pkh_Address = PrivateKey_To_Addr(key, 'P2PKH')
# Convert Private Key HEX To P2SH Address Type
p2sh_Address = PrivateKey_To_Addr(key, 'P2SH')
# Convert Private Key HEX To P2WPKH Address Type
p2wpkh_Address = PrivateKey_To_Addr(key, 'P2WPKH')
# Convert Private Key HEX To P2WSH Address Type
p2wsh_Address = PrivateKey_To_Addr(key, 'P2WSH')
# Convert Private Key HEX To P2WPKH in P2SH Address Type
p2wpkhinp2sh_Address = PrivateKey_To_Addr(key, 'P2WPKHinP2SH')
# Convert Private Key HEX To P2WSH in P2SH Address Type
p2wshinp2sh_Address = PrivateKey_To_Addr(key, 'P2WSHinP2SH')
```
## Generated and Convert Mnemonic To Bitcoin Address Wallet

```python
from Blockthon.Wallet import getMnemonic
from Blockthon.Bitcoin import Mnemonic_To_PrivateKey

mnemonicword = getMnemonic(12)
# convert mnemonic to private key hex
privatekey = Mnemonic_To_PrivateKey(mnemonicword)
```

## Convert Wif To Bitcoin Address
```python
from Blockthon.Bitcoin import Wif_To_Addr

wif = "YOUR_WIF_KEY"
# convert wif to address bitcoin
address = Wif_To_Addr(wif)
```

## Convert Wif To Decimal (int)
```python
from Blockthon.Bitcoin import Wif_To_Dec

wif = "YOUR_WIF_KEY"
# convert wif to number (dec)
dec = Wif_To_Dec(wif)
```

## Convert Wif To Private Key (hex)

```python
from Blockthon.Bitcoin import Wif_To_HEX

wif = "YOUR_WIF_KEY"
# convert wif to private key hex
privatekey = Wif_To_HEX(wif)

```