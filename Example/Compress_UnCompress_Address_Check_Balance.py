from Blockthon import Wallet, Check

# private key
privatekey = Wallet.PVK()
# convert Private key to bytes
seed = Wallet.PrivateKey_To_Bytes(privatekey)
# compress address from bytes (seed)
compressAddress = Wallet.Bytes_To_Address(seed, compress=True)
# uncompress address from bytes (seed)
uncompressAddress = Wallet.Bytes_To_Address(seed)
# balance compress address value
balance_compress = Check.Btc_Balance(compressAddress)
# balance uncompress address value
balance_uncompress = Check.Btc_Balance(uncompressAddress)
# * ---------------------------------------------------- * #
print('Private Key [HEX] : ', privatekey)
print('Compress Address : ', compressAddress, ' Balance :', balance_compress)
print('Uncompress Address : ', uncompressAddress, ' Balance :', balance_uncompress)
