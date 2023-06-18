## Generated and convert Private Key Hex To Mnemonic Word's:

generated private key with blockthon and convert private key (hex) to mnemonic:

`PrivateKey_To_Mnemonics(privatekey: str)`
```python
from Blockthon.Wallet import PrivateKey_To_Mnemonics, PrivateKey

# Private Key Hex [str]
privatekey = PrivateKey()
# convert Private Key [hex] to Mnemonic string (word's)
mnemonic_Words = PrivateKey_To_Mnemonics(privatekey)
```

### Generated Private Key , Convert To Mnemonic and Create compress & uncompress address bitcoin wallet:

**example** : generated private key hex convert To mnemonic word's and create compress and uncompress bitcoin address wallet with check value balance per address:

```python
from Blockthon.Wallet import PrivateKey, PrivateKey_To_Mnemonics
from Blockthon.Bitcoin import Balance_BTC, PrivateKey_To_Address

# counter per process
count = 0
# counter total found address with value balance
found = 0
while True:
    count += 1
    # Generated Private Key HEX Without Repeat
    key = PrivateKey()
    # Convert Private Key To Mnemonic String
    mnemonicWords = PrivateKey_To_Mnemonics(key)
    # Convert Private Key To Compress Bitcoin Address
    compressAddr = PrivateKey_To_Address(key, 'compress')
    # Convert Private Key To UnCompress Bitcoin Address
    uncompressAddr = PrivateKey_To_Address(key, 'uncompress')
    # Check Balance Value Compress Address
    balance_compress = Balance_BTC(compressAddr)
    # Check Balance Value UnCompress Address
    balance_uncompress = Balance_BTC(uncompressAddr)
    if balance_uncompress != '0' or balance_compress != '0':
        found += 1
        # if Value Balance per Address > 0 Save All Detail's To Found.txt
        open('Found.txt', 'a').write(f'{compressAddr} - {balance_compress}\n{uncompressAddr} - {balance_compress}\n{key}\n{mnemonicWords}\n')
    else:
        # else , Balance == 0 print detail's 
        print(f"Checked:{count} / Found:{found} # {compressAddr} : {balance_compress}")
        print(f"Checked:{count} / Found:{found} # {uncompressAddr} : {balance_uncompress}")
        print(f"Checked:{count} / Found:{found} # {key}")
        print(f"Checked:{count} / Found:{found} # {mnemonicWords}")
        print(f"{'-' * 70}")
```
