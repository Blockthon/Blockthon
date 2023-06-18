## convert binary to private key hex

### Private Key From Binary

generated random binary string for convert to hex private key
```python
from Blockthon.Wallet import getBin

# generated binary with 256 size (default: 256)
binary_string = getBin(256)
```
convert binary to private key hex with `Blockthon`:

```python
from Blockthon.Wallet import PrivateKey_From_Binary, getBin

# generated random binary with 256 size 
binary_atring = getBin(size=256)
# convert binary to private key hex:
privatekey = PrivateKey_From_Binary(binary_atring)
```