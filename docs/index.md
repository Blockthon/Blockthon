# Blockthon
Blockthon Python Package for Generate and Converting Wallet Private Key and Mnemonic for Address Bitcoin

```bash
# on windows
pip install Blockthon

# on Linux
pip3 install Blockthon
```

on unix(debian base) if have problem curve or another library error's first need install this library's:
```bash
sudo apt-get update&&sudo apt-get upgrade -y
sudo apt-get install -y autoconf automake build-essential libffi-dev libtool pkg-config python3-dev
# after installing run cammand 
pip3 install blockthon
```

---

## Private Key

```python
from Blockthon.Wallet import PrivateKey

privatekey = PrivateKey()
```

## Mnemonic

```python
from Blockthon.Wallet import getMnemonic
# generated random mnemonic with 12 word
mnemonicWords = getMnemonic(12)
```
## Bytes
```python
from Blockthon.Wallet import getBytes

bytes_seed = getBytes()
```

## Binary
```python
from Blockthon.Wallet import getBin

binary_string = getBin(size=256)
```

## Private Key To Address
```python
from Blockthon.Wallet import PrivateKey_To_Address
import os

# generated privatekey
privatekey = os.urandom(32).hex()
# convert hex to compressed address
compressed_Address = PrivateKey_To_Address(privatekey, compress=True)
# convert hex to uncompress address
uncompress_Address = PrivateKey_To_Address(privatekey, compress=False)
```
## Private Key To WIF

```python
from Blockthon.Wallet import PrivateKey_To_WIF, PrivateKey

privatekey = PrivateKey()
wif_compress = PrivateKey_To_WIF(privatekey, compress=True)
wif_uncompress = PrivateKey_To_WIF(privatekey)
```

## Private Key To Bytes
```python
from Blockthon.Wallet import PrivateKey_To_Bytes, PrivateKey

byte_string = PrivateKey_To_Bytes(PrivateKey())
```
## Private Key To Binary
```python
from Blockthon.Wallet import PrivateKey, PrivateKey_To_Binary

binary_string = PrivateKey_To_Binary(PrivateKey())
```
## Private Key To Decimal (number)
```python
from Blockthon.Wallet import PrivateKey, PrivateKey_To_Dec

dec = PrivateKey_To_Dec(PrivateKey())
```
## Private Key To xprv
```python
from Blockthon.Wallet import PrivateKey, PrivateKey_To_RootKey

rootkey = PrivateKey_To_RootKey(PrivateKey())
```
## Private Key To Compressed Address
```python
from Blockthon.Wallet import PrivateKey, PrivateKey_To_Compress_Address
compress_addr = PrivateKey_To_Compress_Address(PrivateKey())
```
```python
from Blockthon.Wallet import PrivateKey, PrivateKey_To_Address

compress_addr = PrivateKey_To_Address(PrivateKey(), compress=True)
```

## Private Key To UnCompressed Address
```python
from Blockthon.Wallet import PrivateKey, PrivateKey_To_UnCompress_Address

uncompress_addr = PrivateKey_To_UnCompress_Address(PrivateKey())
```
```python
from Blockthon.Wallet import PrivateKey, PrivateKey_To_Address

uncompress_addr = PrivateKey_To_Address(PrivateKey(), compress=False)
```

## Private Key From Binary
```python
from Blockthon.Wallet import getBin, PrivateKey_From_Binary
privatekey = PrivateKey_From_Binary(getBin(256))
```
## Private Key From Number (decimal)
```python
from Blockthon.Wallet import PrivateKey_From_Dec
privatekey = PrivateKey_From_Dec(12345678987654321)
```

## Private Key From Passphrase
```python
from Blockthon.Wallet import PrivateKey_From_Passphrase
privatekey = PrivateKey_From_Passphrase('MMDRZA.COM')
```
## Private Key From XPRV (Root)
```python
from Blockthon.Wallet import PrivateKey_From_RootKey
privatekey = PrivateKey_From_RootKey('INSERT_ROOT_KEY_XPRV')
```
## Private Key To Ethereum

## Private Key To Tron

## Private Key To Litecoin

## Private Key To DASH

## Private Key To Dogecoin

## Private Key To BitcoinGold

## Private Key To Ravencoin

## Private Key To Qtum

## Private Key To ZCASH

```python
from Blockthon.Wallet import (
    PrivateKey_To_TRX,
    PrivateKey_To_ETH,
    PrivateKey_To_BTG,
    PrivateKey_To_DASH,
    PrivateKey_To_DOGE,
    PrivateKey_To_RVN,
    PrivateKey_To_QTUM,
    PrivateKey_To_LTC,
    PrivateKey_To_ZEC,
    PrivateKey
)

privatekey = PrivateKey()
trx_addr = PrivateKey_To_TRX(privatekey)
eth_addr = PrivateKey_To_ETH(privatekey)
doge_addr = PrivateKey_To_DOGE(privatekey)
ltc_addr = PrivateKey_To_LTC(privatekey)
dash_addr = PrivateKey_To_DASH(privatekey)
bitcoingold_addr = PrivateKey_To_BTG(privatekey)
rvn_addr = PrivateKey_To_RVN(privatekey)
qtum_addr = PrivateKey_To_QTUM(privatekey)
zec_addr = PrivateKey_To_ZEC(privatekey)

```
## Example 
(More detail's & script with `Blockthon`)
### convert private key to All Bitcoin Type address : [ `Example Link` ](https://github.com/Blockthon/Blockthon/blob/main/Example/23_Bitcoin_Wallet.md)

`generated and convert private key hex to bitcoin address type: p2pkh / p2sh / p2wsh / p2wpkh / p2wpkh in p2sh / p2wsh in p2sh`

### convert private key to tron address : [ `Example Link` ](https://github.com/Blockthon/Blockthon/blob/main/Example/32_Tron_Wallet.md)
`generated and convert private key hex to Tron (TRX) address`
### convert private key to Bitcoin Gold address : [ `Example Link` ](https://github.com/Blockthon/Blockthon/blob/main/Example/24_BitcoinGold_Wallet.md)
`generated and convert private key hex to bitcoin gold address`
### convert private key to dash address : [ `Example Link` ](https://github.com/Blockthon/Blockthon/blob/main/Example/25_Dash_Wallet.md)
`generated and convert private key hex to dash address`
### convert private key to dogecoin address : [ `Example Link` ](https://github.com/Blockthon/Blockthon/blob/main/Example/27_Dogecoin_Wallet.md)
`generated and convert private key hex to Dogecoin address`
### convert private key to digibyte address : [ `Example Link` ](https://github.com/Blockthon/Blockthon/blob/main/Example/26_DigiByte_Wallet.md)
`generated and convert private key hex to DigiByte address`
### convert private key to litecoin address : [ `Example Link` ](https://github.com/Blockthon/Blockthon/blob/main/Example/29_Litecoin_Wallet.md)
`generated and convert private key hex to Litecoin address`
### convert private key to ravencoin address : [ `Example Link` ](https://github.com/Blockthon/Blockthon/blob/main/Example/31_Ravencoin_Wallet.md)
`generated and convert private key hex to Ravencoin address`
### convert private key to Qtum address : [ `Example Link` ](https://github.com/Blockthon/Blockthon/blob/main/Example/30_Qtum_Wallet.md)
`generated and convert private key hex to Qtum address`
### convert private key to zCash address : [ `Example Link` ](https://github.com/Blockthon/Blockthon/blob/main/Example/33_zCash_Wallet.md)
`generated and convert private key hex to zcash (zec) address`

---

[![asciicast](https://asciinema.org/a/590054.svg)](https://asciinema.org/a/590054)
---

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

---

More Detail's : [documation](https://blockthon.gitbook.io/blockthon)

---

Programmer & Owner : [@Pymmdrza](https://github.com/Pymmdrza) | [official Website](https://mmdrza.com)

---
💲Donate:

Bitcoin (BTC): `bc1qu8dccq3yetd93m4nge0yay53lwgwvxngj8a80s`

Ethereum & USDT (ERC20): `0x3628c7978C69278fA19A88a5B16718F47f5BEfe8`

USDT & TRON (TRC20): `TFWg8KV8DUP8Ubb4cmS1oubsF2X6i8gnBU`

Litecoin (LTC): `ltc1qx4mznsl228u863u6723avge7xv0xsk3vt0vgxa`



---

