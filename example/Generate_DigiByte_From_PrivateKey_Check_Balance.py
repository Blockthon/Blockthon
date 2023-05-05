import Blockthon

z = 0
while True:
    z += 1
    # Generate Private Key Hex (Random)
    PrivateKey = Blockthon.PrivateKey()
    # Mnemonic_str = Blockthon.PrivateKey_To_Mnemonic(PrivateKey)
    # Generated Address From Private Key HEX
    Addr = Blockthon.DigiByte_From_PrivateKey(PrivateKey)
    # Check Value Balance
    balance = Blockthon.Balance_DigiByte(Addr)
    # ------------------------------------------------------------------------
    print('Total:', z, 'Address:', Addr, 'Balance:', int(balance) / 1000000000)
    print('PrivateKey:', PrivateKey)
    print('-' * 66)
