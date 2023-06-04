# DigiByte With Blockthon

## Generated and Convert Private Key (HEX) To DigiByte Address
```python
from Blockthon.DigiByte import PrivateKey_To_DGB
import os

# Generate Random Private Key
key = os.urandom(32).hex()
# Convert Private Key To DigiByte Address
DigiByte_Address = PrivateKey_To_DGB(key)
```
### Generated DigiByte Address From Mnemonic
```python
from Blockthon.Wallet import getMnemonic
from Blockthon.DigiByte import Mnemonic_To_DGB

# Generated Random Mnemonic with 12 word
mnemonicWords = getMnemonic(12)
# Convert To DigiByte Address
DigiByte_Address = Mnemonic_To_DGB(mnemonicWords)
```

### Check Value Balance on DigiByte Address :
```python
from Blockthon.DigiByte import Balance_DGB

DigiByte_Address = 'ADDRESS_DigiByte_WALLET'
# checking return value on string
Balance = Balance_DGB(DigiByte_Address)
```