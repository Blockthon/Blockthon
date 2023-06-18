# Dogecoin With Blockthon

## Generated and Convert Private Key (HEX) To Dogecoin Address
```python
from Blockthon.Dogecoin import PrivateKey_To_DOGE
import os

# Generate Random Private Key
key = os.urandom(32).hex()
# Convert Private Key To Dogecoin Address
Dogecoin_Address = PrivateKey_To_DOGE(key)
```
### Generated Dogecoin Address From Mnemonic
```python
from Blockthon.Wallet import getMnemonic
from Blockthon.Dogecoin import Mnemonic_To_DOGE

# Generated Random Mnemonic with 12 word
mnemonicWords = getMnemonic(12)
# Convert To Dogecoin Address
Dogecoin_Address = Mnemonic_To_DOGE(mnemonicWords)
```

### Check Value Balance on Dogecoin Address :
```python
from Blockthon.Dogecoin import Balance_DOGE

Dogecoin_Address = 'ADDRESS_Dogecoin_WALLET'
# checking return value on string
Balance = Balance_DOGE(Dogecoin_Address)
```
