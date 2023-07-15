![Blockthon - Python Package Generated Private Key Mnemonic Wallet](./media/Header.png 'Blockthon - Python Package Generated Private Key Mnemonic Wallet')

---
# Blockthon
---

[Installation](#installation) | [Example](/example) | [Donate](#donate) | [Contact](#contact)

---

### installation

Blockthon Python Package for Generate and Converting Wallet Private Key and Mnemonic for Address Bitcoin

```bash
# on windows
pip install Blockthon

# on Linux
pip3 install Blockthon
```

if problem on installing on linux / debian :
```bash
sudo apt-get update&&sudo apt-get upgrade -y
sudo apt-get install -y autoconf automake build-essential libffi-dev libtool pkg-config python3-dev
```

or for download manual:
```bash
git clone https://github.com/Blockthon/Blockthon
cd Blockthon
make
```
---

### Private Key

generated random private key without repeat :

```python
from Blockthon import Wallet

Privatekey = Wallet.getPrivateKey()
```
---
### Mnemonic
Generated random mnemonic with standard size :
```python
from Blockthon import Wallet
# default size 12 . can use [12, 18, 24]
mnemonicString = Wallet.getMnemonic(size=12)
```
----
### Bytes (seed)

Generated Random Bytes Without Repeat :

```python
from Blockthon import Wallet
byte = Wallet.getBytes()
```
---
### Binary
Generate Random Binary Without repeat `0/1`:

```python
from Blockthon import Wallet

binary_string = Wallet.getBin(256)
```
---
### Private Key To Bytes
```python
from Blockthon import Wallet

privatekey = Wallet.getPrivateKey()
# Convert Private Key HEX To Bytes SEED
byte = Wallet.PrivateKey_To_Bytes(privatekey)

```
---
### Private Key To Wif

generated private key (hex) and convert to wif compressed and uncompressed.
```python
from Blockthon import Wallet

privatekey = Wallet.getPrivateKey()
# Convert Private key Hex To Wif
# wif compressed
wif_compress = Wallet.PrivateKey_To_Wif(privatekey, compress=True)
# wif Uncompressed
wif_uncompress = Wallet.PrivateKey_To_Wif(privatekey, compress=False)
```
---
### Private Key To Mnemonic

```python
from Blockthon import Wallet

privatekey = Wallet.getPrivateKey()
# convert private key [hex] To mnemonic
mnemonic_string = Wallet.PrivateKey_To_Mnemonics(privatekey, size=12)
# for size mnemonic can use [12, 18, 24]
```
---
### Private Key To Binary

```python
from Blockthon import Wallet

privatekey = Wallet.getPrivateKey()
# convert hex to bin
binary_string = Wallet.PrivateKey_To_Binary(privatekey)
```
---
### Private Key To Decimal (int)
```python
from Blockthon import Wallet

privatekey = Wallet.getPrivateKey()
# convert private key hex to number (dec)
dec = Wallet.PrivateKey_To_Dec(privatekey)
```
---
### Private Key To RIPEMD160
```python
from Blockthon import Wallet

privatekey = Wallet.getPrivateKey()
# convert private key to ripemd160 (hash160)
ripemd160 = Wallet.PrivateKey_To_RIPEMD160(privatekey)
```
---
### Private Key To Address

convert private key `Hex` to Compress and Uncompress Address
```python
from Blockthon import Wallet

privatekey = Wallet.getPrivateKey()
# convert private key to compress address
compress_Address = Wallet.PrivateKey_To_Address(privatekey, compress=True)
# convert to uncompress address
uncompress_Address = Wallet.PrivateKey_To_Address(privatekey, compress=False)
```
---
### Private Key To Public Key

generated private key and convert to public key compress and uncompress:

```python
from Blockthon import Wallet

privatekey = Wallet.getPrivateKey()
# convert to public key uncompress
public_uncompress = Wallet.PrivateKey_To_PublicKey(privatekey)
# convert private key hex to public key compress
public_compress = Wallet.PrivateKey_To_PublicKey(privatekey, compress=True)
```
---
### Bytes To Private Key
```python
from Blockthon import Wallet

byte = Wallet.getBytes()
# convert bytes to hex (private key)
privatekey = Wallet.Bytes_To_PrivateKey(byte)
```
### Bytes To mnemonic 
convert bytes to mnemonic with default `size=12`

can use standard sizr: `12, 18, 24`

```python
from Blockthon import Wallet

byte = Wallet.getBytes()
# Convert bytes to mnemonic with default size 12
mnemonic_words = Wallet.Bytes_To_Mnemonic(byte, 12)
```
---
### Bytes To Wif
convert bytes To wif Compress and uncompress:
```python
from Blockthon import Wallet

byte = Wallet.getBytes()
# compress wif
wif_compress = Wallet.Bytes_To_Wif(byte, compress=True)
#uncompress Wif
wif_uncompress = Wallet.Bytes_To_Wif(byte, compress=False)
```
---
### Bytes To Public Key

convert bytes to public key compress and uncompress
```python
from Blockthon import Wallet

byte = Wallet.getBytes()
# compress Publickey
Pub_compress = Wallet.Bytes_To_PublicKey(byte, compress=True)
#uncompress Wif
Pub_uncompress = Wallet.Bytes_To_PublicKey(byte, compress=False)
```
---
### Bytes to Dec (number)

convert bytes to decimal number

```python
from Blockthon import Wallet

byte = Wallet.getBytes()
#convert to integer 
dec = Wallet.Bytes_To_Dec(byte)
```
---
### Wif To Public Key
convert wif to public key compress and uncompress
```python
from Blockthon import Wallet

wif = "WIF_STRING_HERE"
pub_compress = Wallet.Wif_To_PublicKey(wif, compress=True)
pub_uncompress = Wallet.Wif_To_PublicKey(wif)
```
---
### Wif To Mnemonic 
convert Wif To Mnemonic With Default `size=12`, Can use Standard Size `12, 18, 24`
```python
from Blockthon import Wallet

wif = "WIF_STRING_HERE"
mnemonic_string = Wallet.Wif_To_Mnemonic(wif, 12)
```
---
### Wif To RIPEMD160
convert wif to RIPEMD160 return `hex string` 
```python
from Blockthon import Wallet

wif = "WIF_STRING_HERE"
RIPEMD160 = Wallet.Wif_To_RIPEMD160(wif)
```
### Mnemonic To Root Key (XPRV)
```python
from Blockthon import Wallet

mnemonic_string = Wallet.getMnemonic(12)
xprv = Wallet.Mnemonic_To_RootKey(mnemonic_string)
```
---
### Mnemonic To Private key
```python
from Blockthon import Wallet

mnemonic_string = Wallet.getMnemonic(12)
pivatekey = Wallet.Mnemonic_To_PrivateKey()

```
---
### Mnemonic To Address
convert mnemonic to compressed and uncompressed Address
```python
from Blockthon import Wallet

mnemonic_string = Wallet.getMnemonic(12)
# compress Address
compress_Address = Wallet.Mnemonic_To_Address(mnemonic_string, True)
# uncompress Address
uncompress_Address = Wallet.Mnemonic_To_Address(mnemonic_stringm False)
```
---
### Passphrase To Private Key
convert word passphrase to private key (hex)
```python
from Blockthon import Wallet
passphrase = 'Mmdrza.Com'
privatekey = Wallet.Passphrase_To_PrivateKey(passphrase)
```
---
### Passphrase to Wif
```python
from Blockthon import Wallet

passphrase = 'Mmdrza.Com'

wif = Wallet.Passphrase_To_Wif(passphrase)
```
---
Example:
```python
from Blockthon import Wallet, Ethereum, Tron, Dogecoin, Bitcoin, Litecoin, Dash, Digibyte, BitcoinGold, Ravencoin, Qtum, zCash

seed = Wallet.getSeed()
privatekey = Wallet.Bytes_To_PrivateKey(seed)
mnemonics = Wallet.Bytes_To_Mnemonic(seed, 12)
wif_compress = Wallet.Bytes_To_Wif(seed, compress=True)
wif_uncompress = Wallet.Bytes_To_Wif(seed, compress=False)
dec = Wallet.Bytes_To_Dec(seed)
xprv = Wallet.Mnemonic_To_RootKey(mnemonics)
publickey = Wallet.Bytes_To_PublicKey(seed)
ripemd160 = Wallet.Bytes_To_RIPEMD160(seed)
compressAddress = Wallet.Bytes_To_Address(seed, compress=True)
uncompressAddress = Wallet.Bytes_To_Address(seed, compress=False)
p2pkhAddress = Bitcoin.Address_From_PrivateKey(privatekey, Type='P2PKH')
p2shAddress = Bitcoin.Address_From_PrivateKey(privatekey, Type='P2SH')
p2wpkhAddress = Bitcoin.Address_From_PrivateKey(privatekey, Type='P2WPKH')
p2wshAddress = Bitcoin.Address_From_PrivateKey(privatekey, Type='P2WSH')
p2wpkhSegwit = Bitcoin.Address_From_PrivateKey(privatekey, Type='P2WPKHinP2SH')
p2wshSegwit = Bitcoin.Address_From_PrivateKey(privatekey, Type='P2WSHinP2SH')
p2pkh_ltc = Litecoin.Address_From_PrivateKey(privatekey, 'P2PKH')
p2sh_ltc = Litecoin.Address_From_PrivateKey(privatekey, 'P2SH')
p2wpkh_ltc = Litecoin.Address_From_PrivateKey(privatekey, 'P2WPKH')
p2wsh_ltc = Litecoin.Address_From_PrivateKey(privatekey, 'P2WSH')
ethereumAddress = Ethereum.Address_From_PrivateKey(privatekey)
tronAddress = Tron.Address_From_PrivateKey(privatekey)
dogeAddress = Dogecoin.Address_From_PrivateKey(privatekey)
dashAddress = Dash.Address_From_PrivateKey(privatekey)
digibyteAddress = Digibyte.Address_From_PrivateKey(privatekey)
RVNAddress = Ravencoin.Address_From_PrivateKey(privatekey)
QtumAddress = Qtum.Address_From_PrivateKey(privatekey)
zcashAddress = zCash.Address_From_PrivateKey(privatekey)
print(f"""
Seed : {seed}
PrivateKey [Hex]: {privatekey}
Mnemonic: {mnemonics}
Wif Compressed: {wif_compress}
Wif UnCompressed: {wif_uncompress}
Decimal: {dec}
RIPEMD160: {ripemd160}
{'-' * 22} Address's {'-' * 22}
Compressed Address: {compressAddress}
UnCompressed Address: {uncompressAddress}
Bitcoin P2PKH: {p2pkhAddress}
Bitcoin P2SH: {p2shAddress}
Bitcoin P2WPKH: {p2wpkhAddress}
Bitcoin P2WSH: {p2wshAddress}
Bitcoin P2WPKH in Segwit: {p2wpkhSegwit}
Bitcoin P2WSH in Segwit: {p2wshSegwit}
Litecoin P2PKH: {p2pkh_ltc}
Litecoin P2SH: {p2sh_ltc}
Litecoin P2WSH: {p2wsh_ltc}
Litecoin P2WPKH: {p2wpkh_ltc}
Ethereum: {ethereumAddress}
Tron: {tronAddress}
Dogecoin: {dogeAddress}
DASH: {dashAddress}
DigiByte: {digibyteAddress}
Ravencoin: {RVNAddress}
QTUM: {QtumAddress}
zCASH: {zcashAddress} 
""")
```
### contact

Programmer & Owner : Mmdrza.Com

Email : PyMmdrza@Gmail.Com

Github: [Blockthon/Blockthon](https://github.com/Blockthon/Blockthon)

Document: [Blockthon](https://blockthon.github.io/Blockthon)

---
### Donate:

Bitcoin (BTC): `1MMDRZA19y8RmmEEqjv6w7tLFDK2uHh5qD`

Ethereum & USDT (ERC20): `0x348e3C3b17784AafD7dB67d011b85F838F16E2D1`

USDT & TRON (TRC20): `TR4mA5quGVHGYS186HKDuArbD8SVssiZVx`

Litecoin (LTC): `ltc1qtgvxc6na9pxvznu05yys3j5rq9ej6kahe2j50v`
