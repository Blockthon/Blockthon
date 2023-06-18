from .Utils import Wallet_, ETH, Eth_Balance, Mnemonic_To_Bytes, Bytes_To_PrivateKey

def PrivateKey_To_ETH(privatekey):
    hd: Wallet_ = Wallet_(ETH)
    hd.from_private_key(privatekey)
    return hd.p2pkh_address()

def Mnemonic_To_ETH(mnemonicwords):
    seed = Mnemonic_To_Bytes(mnemonicwords)
    key = Bytes_To_PrivateKey(seed)
    eth: Wallet_ = Wallet_(ETH)
    eth.from_private_key(key)
    return eth.p2pkh_address()

def Balance_ETH(addr): return Eth_Balance(addr)
