# Qtum With Blockthon

## Generated and Convert Private Key (HEX) To Qtum Address
```python
from Blockthon.Qtum import PrivateKey_To_QTUM
import os

# Generate Random Private Key
key = os.urandom(32).hex()
# Convert Private Key To Qtum Address
Qtum_Address = PrivateKey_To_QTUM(key)
```
### Generated Qtum Address From Mnemonic
```python
from Blockthon.Wallet import getMnemonic
from Blockthon.Qtum import Mnemonic_To_QTUM

# Generated Random Mnemonic with 12 word
mnemonicWords = getMnemonic(12)
# Convert To Qtum Address
Qtum_Address = Mnemonic_To_QTUM(mnemonicWords)
```

### Check Value Balance on Qtum Address :
```python
from Blockthon.Qtum import Balance_QTUM

Qtum_Address = 'ADDRESS_Qtum_WALLET'
# checking return value on string
Balance = Balance_QTUM(Qtum_Address)
```
