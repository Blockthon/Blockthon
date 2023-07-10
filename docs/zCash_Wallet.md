# zCash With Blockthon

## Generated and Convert Private Key (HEX) To zCash Address
```python
from Blockthon.zCash import PrivateKey_To_ZEC
import os

# Generate Random Private Key
key = os.urandom(32).hex()
# Convert Private Key To zCash Address
zCash_Address = PrivateKey_To_ZEC(key)
```
### Generated zCash Address From Mnemonic
```python
from Blockthon.Wallet import getMnemonic
from Blockthon.zCash import Mnemonic_To_ZEC

# Generated Random Mnemonic with 12 word
mnemonicWords = getMnemonic(12)
# Convert To zCash Address
zCash_Address = Mnemonic_To_ZEC(mnemonicWords)
```

### Check Value Balance on zCash Address :
```python
from Blockthon.zCash import Balance_ZEC

zCash_Address = 'ADDRESS_zCash_WALLET'
# checking return value on string
Balance = Balance_ZEC(zCash_Address)
```
