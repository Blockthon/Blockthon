# Dash With Blockthon

## Generated and Convert Private Key (HEX) To Dash Address
```python
from Blockthon.Dash import PrivateKey_To_DASH
import os

# Generate Random Private Key
key = os.urandom(32).hex()
# Convert Private Key To Dash Address
Dash_Address = PrivateKey_To_DASH(key)
```
### Generated Dash Address From Mnemonic
```python
from Blockthon.Wallet import getMnemonic
from Blockthon.Dash import Mnemonic_To_DASH

# Generated Random Mnemonic with 12 word
mnemonicWords = getMnemonic(12)
# Convert To Dash Address
Dash_Address = Mnemonic_To_DASH(mnemonicWords)
```

### Check Value Balance on Dash Address :
```python
from Blockthon.Dash import Balance_DASH

Dash_Address = 'ADDRESS_Dash_WALLET'
# checking return value on string
Balance = Balance_DASH(Dash_Address)
```