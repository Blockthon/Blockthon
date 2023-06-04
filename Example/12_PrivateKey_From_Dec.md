## convert number (dec) to Private key:

### generated random number (decimal) convert to Private key 

in this example can see how to generate random number and convert to private key (Private Key From Dec)

```python
from Blockthon.Wallet import PrivateKey_From_Dec
# dec or number just entered integer 
dec = 10000
# convert dec (10000) to private key hex 
privatekey = PrivateKey_From_Dec(dec)
```
another method , use `PrivateKey_From_Number`:
```python
from Blockthon.Wallet import PrivateKey_From_Number

dec = 10000
# convert number 10000 to private key hex:
privatekey = PrivateKey_From_Number(number=dec)
```