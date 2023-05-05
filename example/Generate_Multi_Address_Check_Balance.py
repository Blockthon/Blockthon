import Blockthon

# Total Generated and Counter
z = 0
while True:
    z += 1
    # Generate Private Key Hex (Random)
    PrivateKey = Blockthon.PrivateKey()
    # Convert Private key Hex To Mnemonic Word's
    Mnemonic_str = Blockthon.PrivateKey_To_Mnemonic(PrivateKey)
    # Create Compressed Address From Private Key Address Bitcoin
    compressAddr = Blockthon.Addr_From_PrivateKey(PrivateKey, compress=True)
    # Create Un Compressed Address From Private Key Address Bitcoin
    uncompressAddr = Blockthon.Addr_From_PrivateKey(PrivateKey)
    # Create Ethereum Address From Private Key HEX
    ethAddr = Blockthon.ETH_From_PrivateKey(PrivateKey)
    # Create Tron Address From Private Key HEX
    trxAddr = Blockthon.TRX_From_PrivateKey(PrivateKey)
    # Check Value Balance Compress Address Bitcoin
    cbal = Blockthon.Balance(compressAddr)
    # Check Value Balance Un Compress Address Bitcoin
    ubal = Blockthon.Balance(uncompressAddr)
    # Check Value Balance Ethereum Address
    ethBal = Blockthon.Balance_Ethereum(ethAddr)
    # Check Value Balance TRON Address
    trxBal = Blockthon.Balance_Tron(trxAddr)
    # --------------------------------------------------------------------------------
    print('Total:', z, 'BTC Compress:', compressAddr, 'Balance:', int(cbal) / 100000000)
    print('Total:', z, 'BTC Un Compress:', uncompressAddr, 'Balance:', int(ubal) / 100000000)
    print('Total:', z, 'ETH:', ethAddr, 'Balance:', int(ethBal) / 100000000000000)
    print('Total:', z, 'TRX:', trxAddr, 'Balance:', int(trxBal) / 10000000000)
    print('PrivateKey:', PrivateKey)
    print('Mnemonic: ', Mnemonic_str)
    print('-' * 66)
    # --------------------------------------------------------------------------------
