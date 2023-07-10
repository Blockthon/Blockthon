from Blockthon import Wallet
# variable's ----------------------------------------------------------
# generated random privatekey without repeat
pvk = Wallet.PVK()
# * ------------------------------------------------------- * #
# private key hex to bytes (seed)
seed = Wallet.unHexlify(pvk)
# * ------------------------------------------------------- * #
# convert seed bytes to mnemonic word's
mnemonic_str = Wallet.Bytes_To_Mnemonic(seed, 12)
# * ------------------------------------------------------- * #
# bytes to wif compress
wif_compress = Wallet.Bytes_To_Wif(seed, compress=True)
# bytes to wif uncompress
wif_uncompress = Wallet.Bytes_To_Wif(seed)
# * ------------------------------------------------------- * #
# bytes to public key compress
publicKey_compress = Wallet.Bytes_To_PublicKey(seed, compress=True)
# bytes to public key uncompress
publicKey_uncompress = Wallet.Bytes_To_PublicKey(seed)
# * ------------------------------------------------------- * #
# bytes to ripemd160
ripemd160 = Wallet.Bytes_To_RIPEMD160(seed)
# * ------------------------------------------------------- * #
# private key hex to binary
Binary_str = Wallet.PrivateKey_To_Binary(pvk)
# * ------------------------------------------------------- * #
# private key to decimal number
dec = Wallet.PrivateKey_To_Dec(pvk)
# * ------------------------------------------------------- * #
# bytes to compress address wallet
compress_Address = Wallet.Bytes_To_Address(seed, compress=True)
# bytes to uncompress address wallet
uncompress_address = Wallet.Bytes_To_Address(seed)
# * ------------------------------------------------------- * #
print('Private Key (hex) : ', pvk)
print('seed', seed)
print('mnemonic : ', mnemonic_str)
print('Wif Compress : ', wif_compress)
print('Wif UnCompress: ', wif_uncompress)
print('Public Key Compress : ', publicKey_compress)
print('Public Key Uncompress : ', publicKey_uncompress)
print('Ripemd160 (hash160) : ', ripemd160)
print('Binary : ', Binary_str)
print('Decimal : ', dec)
print('compress address : ', compress_Address)
print('uncompress address : ', uncompress_address)
