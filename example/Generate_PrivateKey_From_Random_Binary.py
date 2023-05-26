# Programmer And Owner : Mmdrza.Com
# Telegram Channel : Cryptoixer.t.me
# Google Group : https://groups.google.com/g/mmdrza
# Blockthon : https://github.com/Blockthon/Blockthon

import Blockthon as block


count = 0
found = 0
while True:
    count += 1
    # Generated Random Binary
    bin_ = block.getBin(256)
    # Convert Binary To Hex For Private Key
    privatekey = block.PrivateKey_From_Binary(bin_)
    # Convert Private Key (HEX) To Mnemonic
    mnemonic_ = block.PrivateKey_To_Mnemonic(privatekey)
    # Generate UnCompressed Address Bitcoin From Private Key
    uncompressAddr = block.Addr_From_PrivateKey(privatekey)
    # Generate Compressed Address Bitcoin From Private Key
    compressAddr = block.Addr_From_PrivateKey(privatekey, True)
    # Generate Ethereum Address Wallet From Private Key (HEX)
    ethAddr = block.ETH_From_PrivateKey(privatekey)
    # Generate TRON Address Wallet From Private Key (HEX)
    trxAddr = block.TRX_From_PrivateKey(privatekey)
    # Generate Dogecoin Address Wallet From Private Key (HEX)
    dogeAddr = block.DOGE_From_PrivateKey(privatekey)
    # Generate Bitcoin Gold Address Wallet From Private Key (HEX)
    btgAddr = block.BTG_From_PrivateKey(privatekey)
    # Generate Litecoin Address Wallet From Private Key (HEX)
    ltcAddr = block.LTC_From_PrivateKey(privatekey)
    # Generate Dashcoin Address Wallet From Private Key (HEX)
    dashAddr = block.DASH_From_PrivateKey(privatekey)
    # Generate ZCASH Address Wallet From Private Key (HEX)
    zcashAddr = block.ZEC_From_PrivateKey(privatekey)
    # Generate Ravencoin Address Wallet From Private Key (HEX)
    rvnAddr = block.RVN_From_PrivateKey(privatekey)
    # Generate QTUM Address Wallet From Private Key (HEX)
    qtumAddr = block.QTUM_From_PrivateKey(privatekey)
    # Generate Digibyte Address Wallet From Private Key (HEX)
    dgbAddr = block.DigiByte_From_PrivateKey(privatekey)
    # Check Balance Value Bitcoin Compress Address
    compress_bal = block.Balance(compressAddr)
    # Check Balance Value Bitcoin un Compress Address
    uncompress_bal = block.Balance(uncompressAddr)
    # Check Balance Value Ethereum Address Wallet
    eth_bal = block.Balance_Ethereum(ethAddr)
    # Check Balance Value TRON Address Wallet
    trx_bal = block.Balance_Tron(trxAddr)
    # Check Balance Value Dogecoin Address Wallet
    doge_bal = block.Balance_Dogecoin(dogeAddr)
    # Check Balance Value Bitcoin Gold Address Wallet
    btg_bal = block.Balance_BitcoinGold(btgAddr)
    # Check Balance Value Litecoin Address Wallet
    ltc_bal = block.Balance_Litecoin(ltcAddr)
    # Check Balance Value DASH Address Wallet
    dash_bal = block.Balance_Dash(dashAddr)
    # Check Balance Value ZCASH Address Wallet
    zcash_bal = block.Balance_zCash(zcashAddr)
    # Check Balance Value Ravencoin Address Wallet
    rvn_bal = block.Balance_Ravencoin(rvnAddr)
    # Check Balance Value QTUM Address Wallet
    qtum_bal = block.Balance_Qtum(qtumAddr)
    # Check Balance Value DigiByte Address Wallet
    dgb_bal = block.Balance_DigiByte(dgbAddr)
    print(f"""
[+] ETH : {ethAddr} : {eth_bal}
[+] TRX : {trxAddr} :  {trx_bal}
[+] Doge: {dogeAddr} : {doge_bal}
[+] BTG : {btgAddr} : {btg_bal}
[+] LTC : {ltcAddr} : {ltc_bal}
[+] DASH: {dashAddr} : {dash_bal}
[+] ZEC : {zcashAddr} : {zcash_bal}
[+] RVN : {rvnAddr} : {rvn_bal}
[+] QTUM: {qtumAddr} : {qtum_bal}
[+] DGB : {dgbAddr} : {dgb_bal}
[+] BTC Compress : {compressAddr} : {compress_bal}
[+] BTC UnCompress : {uncompressAddr} : {uncompress_bal}
[+] Private Key : {privatekey}
[+] Mnemonic : {mnemonic_}
{'-' * 66}
    """)
