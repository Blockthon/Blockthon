# Tron With Blockthon

## Generated and Convert Private Key (HEX) To Tron Address
```python
from Blockthon.Tron import PrivateKey_To_TRX
import os

# Generate Random Private Key
key = os.urandom(32).hex()
# Convert Private Key To Tron Address
Tron_Address = PrivateKey_To_TRX(key)
```
### Generated Tron Address From Mnemonic
```python
from Blockthon.Wallet import getMnemonic
from Blockthon.Tron import Mnemonic_To_TRX

# Generated Random Mnemonic with 12 word
mnemonicWords = getMnemonic(12)
# Convert To Tron Address
Tron_Address = Mnemonic_To_TRX(mnemonicWords)
```

### Check Value Balance on Tron Address :
```python
from Blockthon.Tron import Balance_TRX

Tron_Address = 'ADDRESS_Tron_WALLET'
# checking return value on string
Balance = Balance_TRX(Tron_Address)
```