# BitcoinGold With Blockthon

## Generated and Convert Private Key (HEX) To BitcoinGold Address
```python
from Blockthon.BitcoinGold import PrivateKey_To_BTG
import os

# Generate Random Private Key
key = os.urandom(32).hex()
# Convert Private Key To BitcoinGold Address
BitcoinGold_Address = PrivateKey_To_BTG(key)
```
### Generated BitcoinGold Address From Mnemonic
```python
from Blockthon.Wallet import getMnemonic
from Blockthon.BitcoinGold import Mnemonic_To_BTG

# Generated Random Mnemonic with 12 word
mnemonicWords = getMnemonic(12)
# Convert To BitcoinGold Address
BitcoinGold_Address = Mnemonic_To_BTG(mnemonicWords)
```

### Check Value Balance on BitcoinGold Address :
```python
from Blockthon.BitcoinGold import Balance_BTG

BitcoinGold_Address = 'ADDRESS_BitcoinGold_WALLET'
# checking return value on string
Balance = Balance_BTG(BitcoinGold_Address)
```