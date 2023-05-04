from Blockthon import PrivateKey, Addr_From_PrivateKey

# Generate Private Key Hex Random
key = PrivateKey()
# Generated Compressed Address From Private Key Hex (key)
compress_addr = Addr_From_PrivateKey(key, compress=True)
# Generated un Compressed Address From Private Key Hex (key)
uncompress_addr = Addr_From_PrivateKey(key)

print("Compressed Address:", compress_addr)
print("unCompressed Address:", uncompress_addr)
print("Private Key:", key)
