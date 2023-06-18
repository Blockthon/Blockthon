# Ravencoin With Blockthon

## Generated and Convert Private Key (HEX) To Ravencoin Address
```python
from Blockthon.Ravencoin import PrivateKey_To_RVN
import os

# Generate Random Private Key
key = os.urandom(32).hex()
# Convert Private Key To Ravencoin Address
Ravencoin_Address = PrivateKey_To_RVN(key)
```
### Generated Ravencoin Address From Mnemonic
```python
from Blockthon.Wallet import getMnemonic
from Blockthon.Ravencoin import Mnemonic_To_RVN

# Generated Random Mnemonic with 12 word
mnemonicWords = getMnemonic(12)
# Convert To Ravencoin Address
Ravencoin_Address = Mnemonic_To_RVN(mnemonicWords)
```

### Check Value Balance on Ravencoin Address :
```python
from Blockthon.Ravencoin import Balance_RVN

Ravencoin_Address = 'ADDRESS_Ravencoin_WALLET'
# checking return value on string
Balance = Balance_RVN(Ravencoin_Address)
```
