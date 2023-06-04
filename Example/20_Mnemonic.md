## Mnemonic
### Generated Random Mnemonic Word's

```python
from Blockthon.Wallet import getMnemonic
# generated random Mnemonic words [without repeat]
mnemonic_words = getMnemonic(size=12)
```
can changed param `size` with integer `12` . `18` , `24` , example if needed 24 word :
```python
from Blockthon.Wallet import getMnemonic
# with 24 word
mnemonicWords = getMnemonic(24)
# or with 18 word
mnemonicwords = getMnemonic(size=18)
```
size **default** : `size=12` type:`int`
