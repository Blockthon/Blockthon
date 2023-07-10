## Mnemonic
### Generated Random Mnemonic Word's

```python
from Blockthon import Wallet
# generated random Mnemonic words [without repeat]
mnemonic_words = Wallet.getMnemonic(size=12)
```
can changed param `size` with integer `12` . `18` , `24` , example if needed 24 word :
```python
from Blockthon import Wallet
# generated random Mnemonic words [without repeat]
mnemonic_words = Wallet.getMnemonic(size=24)
# or with 18 word
mnemonicwords = Wallet.getMnemonic(18)
```
size **default** : `size=12` type:`int`
