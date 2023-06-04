# Litecoin With Blockthon

## Generated and Convert Private Key (HEX) To Litecoin Address
```python
from Blockthon.Litecoin import PrivateKey_To_LTC
import os

# Generate Random Private Key
key = os.urandom(32).hex()
# Convert Private Key To Litecoin Address
Litecoin_Address = PrivateKey_To_LTC(key)
```
### Generated Litecoin Address From Mnemonic
```python
from Blockthon.Wallet import getMnemonic
from Blockthon.Litecoin import Mnemonic_To_LTC

# Generated Random Mnemonic with 12 word
mnemonicWords = getMnemonic(12)
# Convert To Litecoin Address
Litecoin_Address = Mnemonic_To_LTC(mnemonicWords)
```

### Check Value Balance on Litecoin Address :
```python
from Blockthon.Litecoin import Balance_LTC

Litecoin_Address = 'ADDRESS_Litecoin_WALLET'
# checking return value on string
Balance = Balance_LTC(Litecoin_Address)
```