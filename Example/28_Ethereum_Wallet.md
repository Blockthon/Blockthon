# Ethereum With Blockthon

## Generated and Convert Private Key (HEX) To Ethereum Address
```python
from Blockthon.Ethereum import PrivateKey_To_ETH
import os

# Generate Random Private Key
key = os.urandom(32).hex()
# Convert Private Key To Ethereum Address
Ethereum_Address = PrivateKey_To_ETH(key)
```
### Generated Ethereum Address From Mnemonic
```python
from Blockthon.Wallet import getMnemonic
from Blockthon.Ethereum import Mnemonic_To_ETH

# Generated Random Mnemonic with 12 word
mnemonicWords = getMnemonic(12)
# Convert To Ethereum Address
Ethereum_Address = Mnemonic_To_ETH(mnemonicWords)
```

### Check Value Balance on Ethereum Address :
```python
from Blockthon.Ethereum import Balance_ETH

Ethereum_Address = 'ADDRESS_Ethereum_WALLET'
# checking return value on string
Balance = Balance_ETH(Ethereum_Address)
```