from .Utils import Wallet_, DOGE, Doge_Balance, Mnemonic_To_Bytes, Bytes_To_PrivateKey

def PrivateKey_To_DOGE(privatekey):
    Dg: Wallet_ = Wallet_(DOGE)
    Dg.from_private_key(privatekey)
    return Dg.p2pkh_address()

def Mnemonic_To_DOGE(mnemonicwords):
    seed = Mnemonic_To_Bytes(mnemonicwords)
    key = Bytes_To_PrivateKey(seed)
    Dg: Wallet_ = Wallet_(DOGE)
    Dg.from_private_key(key)
    return Dg.p2pkh_address()

def Balance_DOGE(addr): return Doge_Balance(addr)
