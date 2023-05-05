import Blockthon

z = 0
while True:
    z += 1
    PrivateKey = Blockthon.PrivateKey()
    # Mnemonic_str = Blockthon.PrivateKey_To_Mnemonic(PrivateKey)
    Addr = Blockthon.LTC_From_PrivateKey(PrivateKey)
    balance = Blockthon.Balance_Litecoin(Addr)
    # ------------------------------------------------------------------------
    print('Total:', z, 'Address:', Addr, 'Balance:', int(balance) / 100000000)
    print('PrivateKey:', PrivateKey)
    print('-' * 66)
